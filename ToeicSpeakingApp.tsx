import React, { useState, useEffect, useMemo, useRef } from 'react';
import masterDataRaw from './data/toeic_parts_master.json';
import magicDataRaw from './data/magic_187_vocab.json';

interface SentenceItem {
  step?: string;
  en: string;
  chunking?: string;
  ko: string;
}

interface MagicSentenceItem {
  en: string;
  ko: string;
  tip?: string;
}

interface VocabItem {
  word: string;
  ipa: string;
  pos: string;
  meaning: string;
}

interface ScheduleTable {
  headerTitle: string;
  metaInfo: { label: string; value: string }[];
  rows: { date: string; time: string; event: string; location: string; note: string }[];
}

interface StandardQuestion {
  id: string;
  part: number;
  qNum: string;
  category?: string;
  typeId?: string;
  typeName?: string;
  typeBadge?: string;
  topic: string;
  prepTime: number;
  responseTime: number;
  imageRelPath?: string;
  imageBase64?: string;
  question?: string;
  questionKo?: string;
  sentences: SentenceItem[];
  magicSentences?: MagicSentenceItem[];
  vocabulary: VocabItem[];
  readingTips?: string;
  explanation?: string;
}

interface Part4Question {
  qId: string;
  qNum: string;
  topic: string;
  prepTime: number;
  responseTime: number;
  question: string;
  questionKo: string;
  sentences: SentenceItem[];
  magicSentences?: MagicSentenceItem[];
  vocabulary: VocabItem[];
  explanation?: string;
}

interface Part4Set {
  id: string;
  part: number;
  setNum: string;
  tableTypeId: string;
  tableTypeName: string;
  tableTypeBadge: string;
  topic: string;
  prepTime: number;
  scheduleTable: ScheduleTable;
  questions: Part4Question[];
}

interface MagicBookItem {
  id: string;
  part: number;
  category: string;
  en: string;
  ko: string;
  tip: string;
  keywords: string;
}

const masterData = masterDataRaw as {
  title: string;
  part3Types: { id: string; name: string }[];
  part4TableTypes: { id: string; name: string }[];
  part1: StandardQuestion[];
  part2: StandardQuestion[];
  part3: StandardQuestion[];
  part4: Part4Set[];
  part5: StandardQuestion[];
};

const magicData = magicDataRaw as {
  metadata: {
    title: string;
    total_count: number;
  };
  items: MagicBookItem[];
};

type ActivePart = 'part1' | 'part2' | 'part3' | 'part4' | 'part5';
type TimerStatus = 'idle' | 'prep' | 'resp' | 'done';

export const ToeicSpeakingApp: React.FC = () => {
  const [activePart, setActivePart] = useState<ActivePart>('part1');
  const [selectedIndex, setSelectedIndex] = useState<number>(0);
  const [part3TypeFilter, setPart3TypeFilter] = useState<string>('ALL');
  const [part4TableTypeFilter, setPart4TableTypeFilter] = useState<string>('ALL');

  // 모범답안 펼침 상태
  const [isAnswerOpen, setIsAnswerOpen] = useState<boolean>(false);
  const [p4AnswerOpenMap, setP4AnswerOpenMap] = useState<Record<string, boolean>>({});

  // Part 4 질문 지문 숨김 토글 상태 (듣기 시험 특성 반영)
  const [p4QuestionVisibleMap, setP4QuestionVisibleMap] = useState<Record<string, boolean>>({});

  // 문항 목록 드로어 상태
  const [isDrawerOpen, setIsDrawerOpen] = useState<boolean>(false);

  // 시계토끼 만능문장 187 모달 상태
  const [isVocabModalOpen, setIsVocabModalOpen] = useState<boolean>(false);
  const [modalPartFilter, setModalPartFilter] = useState<string>('ALL');
  const [modalSearch, setModalSearch] = useState<string>('');
  const [memorizedIds, setMemorizedIds] = useState<Record<string, boolean>>(() => {
    try {
      return JSON.parse(localStorage.getItem('toeic_memorized_187') || '{}');
    } catch {
      return {};
    }
  });

  // 3. 다크모드 상태 (로컬스토리지 연동)
  const [isDarkMode, setIsDarkMode] = useState<boolean>(() => {
    try {
      return localStorage.getItem('toeic_dark_mode') === 'true';
    } catch {
      return false;
    }
  });

  const toggleDarkMode = () => {
    setIsDarkMode(prev => {
      const next = !prev;
      localStorage.setItem('toeic_dark_mode', String(next));
      if (typeof document !== 'undefined') {
        document.documentElement.classList.toggle('dark', next);
      }
      return next;
    });
  };

  useEffect(() => {
    if (typeof document !== 'undefined') {
      document.documentElement.classList.toggle('dark', isDarkMode);
    }
  }, [isDarkMode]);

  // 2. 발음 선택 상태 (본문 칸 선택 후 하단 바에서 재생)
  const [selectedItemId, setSelectedItemId] = useState<string | null>(null);
  const [selectedSpeechText, setSelectedSpeechText] = useState<string>('');

  // 음성 재생 키
  const [playingKey, setPlayingKey] = useState<string | null>(null);

  // CBT 타이머 상태
  const [timerStatus, setTimerStatus] = useState<TimerStatus>('idle');
  const [timeLeft, setTimeLeft] = useState<number>(45);
  const timerIntervalRef = useRef<any>(null);

  // 1. Daniel 음성 고정 탐색
  const getDanielVoice = (): SpeechSynthesisVoice | null => {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    const daniel = voices.find(v => (v.name || '').toLowerCase().includes('daniel'));
    if (daniel) return daniel;

    const enMale = voices.find(v => {
      const n = (v.name || '').toLowerCase();
      const l = (v.lang || '').toLowerCase();
      return l.startsWith('en') && (n.includes('guy') || n.includes('andrew') || n.includes('tom') || n.includes('alex') || n.includes('evan'));
    });
    if (enMale) return enMale;

    return voices.find(v => (v.lang || '').toLowerCase().startsWith('en')) || voices[0] || null;
  };

  useEffect(() => {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = () => {
        getDanielVoice();
      };
    }
    return () => {
      if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
      if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    };
  }, []);

  // 독립 정지 함수
  const stopSpeech = () => {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    setPlayingKey(null);
  };

  const speakText = (text: string, rate: number, key: string) => {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) return;

    if (playingKey === key) {
      stopSpeech();
      return;
    }

    window.speechSynthesis.cancel();
    setPlayingKey(key);

    const cleaned = text.replace(/[↗↘↑↓/]/g, ' ').replace(/\s+/g, ' ').trim();
    const utter = new SpeechSynthesisUtterance(cleaned);
    const voice = getDanielVoice();
    if (voice) {
      utter.voice = voice;
      utter.lang = voice.lang || 'en-US';
    } else {
      utter.lang = 'en-US';
    }
    utter.rate = rate;
    utter.pitch = 0.98;

    utter.onend = () => {
      setPlayingKey(curr => (curr === key ? null : curr));
    };
    utter.onerror = () => {
      setPlayingKey(curr => (curr === key ? null : curr));
    };

    window.speechSynthesis.speak(utter);
  };

  // 1 & 2. 하단 플로팅 바에서 현재 선택된 텍스트 재생
  const playSelectedRate = (rate: number) => {
    if (!selectedSpeechText) {
      // 선택된 항목이 없으면 기본 텍스트 자동 지정
      if (activePart === 'part1' && currentStandardQ) {
        const full = currentStandardQ.sentences.map(s => s.en).join(' ');
        setSelectedItemId(`${currentStandardQ.id}-full`);
        setSelectedSpeechText(full);
        speakText(full, rate, `selected-${rate}`);
        return;
      }
      if (activePart === 'part4' && currentP4Set && currentP4Set.questions.length > 0) {
        const q = currentP4Set.questions[0];
        setSelectedItemId(`${q.qId}-prompt`);
        setSelectedSpeechText(q.question);
        speakText(q.question, rate, `selected-${rate}`);
        return;
      }
      if (currentStandardQ) {
        const txt = currentStandardQ.question || (currentStandardQ.sentences[0] ? currentStandardQ.sentences[0].en : '');
        if (txt) {
          setSelectedItemId(`${currentStandardQ.id}-prompt`);
          setSelectedSpeechText(txt);
          speakText(txt, rate, `selected-${rate}`);
          return;
        }
      }
    }
    if (selectedSpeechText) {
      speakText(selectedSpeechText, rate, `selected-${rate}`);
    }
  };

  // 2. 칸 선택 핸들러
  const handleSelectSpeech = (id: string, text: string) => {
    setSelectedItemId(id);
    setSelectedSpeechText(text);
  };

  // 2. 선택된 칸 구분 효과 클래스
  const getSelectableClass = (id: string) => {
    const isSelected = selectedItemId === id;
    return `cursor-pointer transition-all relative rounded-2xl ${
      isSelected
        ? 'ring-2 ring-[#0071E3] dark:ring-[#0A84FF] border-[#0071E3] dark:border-[#0A84FF] bg-[#0071E3]/8 dark:bg-[#0A84FF]/20 shadow-md -translate-y-0.5'
        : 'hover:border-[#0071E3]/40 dark:hover:border-white/20 hover:bg-[#0071E3]/[0.02] dark:hover:bg-white/[0.02]'
    }`;
  };

  // 5. Web Audio API를 이용한 단단한 Beep 신호음
  const playBeep = (freq = 1000, durationMs = 300) => {
    try {
      const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, ctx.currentTime);
      gain.gain.setValueAtTime(0.25, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + durationMs / 1000);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + durationMs / 1000);
    } catch {
      // AudioContext unavailable
    }
  };

  // 파트별 문항 필터링
  const activeQuestions = useMemo<StandardQuestion[]>(() => {
    if (activePart === 'part1') return masterData.part1;
    if (activePart === 'part2') return masterData.part2;
    if (activePart === 'part3') {
      if (part3TypeFilter === 'ALL') return masterData.part3;
      return masterData.part3.filter(q => q.typeId === part3TypeFilter);
    }
    if (activePart === 'part5') return masterData.part5;
    return [];
  }, [activePart, part3TypeFilter]);

  const activeP4Sets = useMemo<Part4Set[]>(() => {
    if (activePart !== 'part4') return [];
    if (part4TableTypeFilter === 'ALL') return masterData.part4;
    return masterData.part4.filter(s => s.tableTypeId === part4TableTypeFilter);
  }, [activePart, part4TableTypeFilter]);

  const currentStandardQ = activeQuestions[selectedIndex] || activeQuestions[0];
  const currentP4Set = activeP4Sets[selectedIndex] || activeP4Sets[0];

  // 타이머 기준 시간 계산
  const targetPrepTime = activePart === 'part4' ? (currentP4Set ? currentP4Set.prepTime : 45) : (currentStandardQ ? currentStandardQ.prepTime : 45);
  const targetRespTime = activePart === 'part4' ? 15 : (currentStandardQ ? currentStandardQ.responseTime : 45);

  // 문제나 파트 전환 시 타이머 리셋 & 기본 발음 항목 자동 선택
  useEffect(() => {
    if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    setTimerStatus('idle');
    setTimeLeft(targetPrepTime);

    // 기본 발음 항목 선택
    if (activePart === 'part1' && currentStandardQ) {
      const full = currentStandardQ.sentences.map(s => s.en).join(' ');
      setSelectedItemId(`${currentStandardQ.id}-full`);
      setSelectedSpeechText(full);
    } else if (activePart === 'part4' && currentP4Set && currentP4Set.questions.length > 0) {
      const q = currentP4Set.questions[0];
      setSelectedItemId(`${q.qId}-prompt`);
      setSelectedSpeechText(q.question);
    } else if (currentStandardQ) {
      if (currentStandardQ.question) {
        setSelectedItemId(`${currentStandardQ.id}-prompt`);
        setSelectedSpeechText(currentStandardQ.question);
      } else if (currentStandardQ.sentences.length > 0) {
        setSelectedItemId(`${currentStandardQ.id}-ms0`);
        setSelectedSpeechText(currentStandardQ.sentences[0].en);
      }
    }
  }, [activePart, selectedIndex, targetPrepTime, currentStandardQ, currentP4Set]);

  const startCbtTimer = () => {
    if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    setTimerStatus('prep');
    setTimeLeft(targetPrepTime);

    let currentSec = targetPrepTime;
    let mode: 'prep' | 'resp' = 'prep';

    timerIntervalRef.current = setInterval(() => {
      currentSec -= 1;
      if (currentSec <= 0) {
        if (mode === 'prep') {
          playBeep(1000, 350); // 준비 시간 종료 비프음
          mode = 'resp';
          currentSec = targetRespTime;
          setTimerStatus('resp');
          setTimeLeft(currentSec);
        } else {
          // 답변 시간 종료
          playBeep(1200, 450);
          if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
          setTimerStatus('done');
          setTimeLeft(0);
        }
      } else {
        setTimeLeft(currentSec);
      }
    }, 1000);
  };

  const pauseCbtTimer = () => {
    if (timerIntervalRef.current) {
      clearInterval(timerIntervalRef.current);
      timerIntervalRef.current = null;
    }
  };

  const resetCbtTimer = () => {
    if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    setTimerStatus('idle');
    setTimeLeft(targetPrepTime);
  };

  const handleTabChange = (part: ActivePart) => {
    stopSpeech();
    setActivePart(part);
    setSelectedIndex(0);
    setIsAnswerOpen(false);
    setP4AnswerOpenMap({});
    setP4QuestionVisibleMap({});
  };

  const toggleMemorized = (id: string) => {
    setMemorizedIds(prev => {
      const next = { ...prev };
      if (next[id]) delete next[id];
      else next[id] = true;
      localStorage.setItem('toeic_memorized_187', JSON.stringify(next));
      return next;
    });
  };

  const filteredVocabItems = useMemo(() => {
    const q = modalSearch.trim().toLowerCase();
    return magicData.items.filter(item => {
      if (modalPartFilter !== 'ALL' && String(item.part) !== modalPartFilter) return false;
      if (q) {
        return (
          item.en.toLowerCase().includes(q) ||
          item.ko.toLowerCase().includes(q) ||
          item.category.toLowerCase().includes(q) ||
          item.id.toLowerCase().includes(q) ||
          item.tip.toLowerCase().includes(q)
        );
      }
      return true;
    });
  }, [modalPartFilter, modalSearch]);

  const memorizedCount = Object.keys(memorizedIds).length;
  const totalItemsCount = activePart === 'part4' ? activeP4Sets.length : activeQuestions.length;
  const totalP4Questions = useMemo(() => {
    return masterData.part4.reduce((sum, s) => sum + s.questions.length, 0);
  }, []);

  return (
    <div className={`min-h-screen transition-colors duration-200 ${isDarkMode ? 'dark bg-[#000000] text-[#F5F5F7]' : 'bg-[#F5F5F7] text-[#1D1D1F]'} font-sans antialiased pb-36`}>
      {/* iOS 리퀴드 글래스 헤더 */}
      <header className="sticky top-0 z-40 bg-white/80 dark:bg-[#141416]/85 backdrop-blur-2xl border-b border-black/5 dark:border-white/10 shadow-sm transition-all">
        <div className="max-w-6xl mx-auto px-3 sm:px-4 py-2.5 sm:py-3.5 flex items-center justify-between gap-2 sm:gap-4">
          <div className="flex items-center gap-2 sm:gap-3 min-w-0">
            {/* 3. 다크모드 iOS 슬라이딩 스위치 토글 (상단 맨 왼쪽 ETS CBT MASTER 대신 배치) */}
            <button
              type="button"
              onClick={toggleDarkMode}
              className={`relative inline-flex h-7 w-14 sm:h-8 sm:w-16 shrink-0 cursor-pointer items-center rounded-full p-1 transition-all duration-300 ease-out focus:outline-none border shadow-inner ${
                isDarkMode
                  ? 'bg-[#0A84FF] border-[#0A84FF]/80 shadow-blue-900/30 ring-2 ring-[#0A84FF]/20'
                  : 'bg-[#E5E5EA] border-black/10 shadow-black/5'
              }`}
              title={isDarkMode ? '라이트 모드로 전환' : '다크 모드로 전환'}
              aria-label="다크 모드 전환"
            >
              <span className="absolute inset-0 flex items-center justify-between px-1.5 sm:px-2 text-[10px] sm:text-[11px] select-none pointer-events-none">
                <span className={`transition-opacity duration-200 ${isDarkMode ? 'opacity-85 text-white' : 'opacity-0'}`}>☀️</span>
                <span className={`transition-opacity duration-200 ${isDarkMode ? 'opacity-0' : 'opacity-55 text-slate-700'}`}>🌙</span>
              </span>
              <span
                className={`pointer-events-none flex h-5 w-5 sm:h-6 sm:w-6 transform items-center justify-center rounded-full bg-white shadow-md ring-0 transition duration-300 ease-out text-[11px] sm:text-xs ${
                  isDarkMode ? 'translate-x-7 sm:translate-x-8 text-[#0A84FF]' : 'translate-x-0 text-amber-500'
                }`}
              >
                {isDarkMode ? '🌙' : '☀️'}
              </span>
            </button>
            <h1 className="text-sm sm:text-lg font-bold tracking-tight text-[#1D1D1F] dark:text-[#F5F5F7] truncate">
              토익스피킹 기출 마스터
            </h1>
          </div>

          <div className="flex items-center gap-2 shrink-0">
            {/* 4. 오른쪽 상단에 단어장 배치 */}
            <button
              type="button"
              onClick={() => setIsVocabModalOpen(true)}
              className="inline-flex items-center gap-1.5 px-2.5 sm:px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-semibold bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20 dark:border-[#0A84FF]/30 hover:bg-[#0071E3]/20 transition-all hover:scale-105 shadow-sm whitespace-nowrap"
            >
              <span>📖</span>
              <span className="hidden sm:inline">시계토끼 만능문장 187</span>
              <span className="inline sm:hidden">만능문장</span>
            </button>
          </div>
        </div>

        {/* 세그먼트 컨트롤 탭 (Part 1~5) */}
        <div className="max-w-6xl mx-auto px-2 sm:px-4 pb-2.5 sm:pb-3">
          <div className="flex p-1 bg-black/5 dark:bg-white/10 rounded-full border border-black/5 dark:border-white/10 gap-1 overflow-x-auto no-scrollbar">
            {[
              { id: 'part1' as ActivePart, fullLabel: 'Part 1 지문 읽기', shortLabel: 'Part 1', count: String(masterData.part1.length) },
              { id: 'part2' as ActivePart, fullLabel: 'Part 2 사진 묘사', shortLabel: 'Part 2', count: String(masterData.part2.length) },
              { id: 'part3' as ActivePart, fullLabel: 'Part 3 질문 응답', shortLabel: 'Part 3', count: String(masterData.part3.length) },
              { id: 'part4' as ActivePart, fullLabel: 'Part 4 표 정보 안내', shortLabel: 'Part 4', count: `${masterData.part4.length}세트 (${totalP4Questions})` },
              { id: 'part5' as ActivePart, fullLabel: 'Part 5 의견 제시', shortLabel: 'Part 5', count: String(masterData.part5.length) }
            ].map(tab => {
              const isActive = activePart === tab.id;
              return (
                <button
                  key={tab.id}
                  type="button"
                  onClick={() => handleTabChange(tab.id)}
                  className={`flex-1 min-w-[72px] sm:min-w-[120px] py-1.5 sm:py-2 px-2 sm:px-3 rounded-full text-xs sm:text-sm font-semibold flex items-center justify-center gap-1.5 transition-all whitespace-nowrap ${
                    isActive
                      ? 'bg-white dark:bg-white/20 text-[#1D1D1F] dark:text-white shadow-sm font-bold'
                      : 'text-[#6E6E73] dark:text-[#8E8E93] hover:text-[#1D1D1F] dark:hover:text-white'
                  }`}
                >
                  <span className="hidden sm:inline">{tab.fullLabel}</span>
                  <span className="inline sm:hidden">{tab.shortLabel}</span>
                  <span
                    className={`text-[10px] sm:text-[11px] px-1.5 sm:px-2 py-0.5 rounded-full ${
                      isActive
                        ? 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/30 text-[#0071E3] dark:text-[#0A84FF]'
                        : 'bg-black/5 dark:bg-white/10 text-[#86868B] dark:text-[#8E8E93]'
                    }`}
                  >
                    {tab.count}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      </header>

      {/* 메인 콘텐츠 영역 */}
      <main className="max-w-4xl mx-auto px-3 sm:px-6 py-4 sm:py-8">
        {/* Part 3 유형 필터 칩 */}
        {activePart === 'part3' && (
          <div className="flex items-center gap-1.5 sm:gap-2 mb-6 p-1.5 sm:p-2 bg-white/70 dark:bg-[#1C1C1E]/75 backdrop-blur-md border border-black/5 dark:border-white/10 rounded-full shadow-xs overflow-x-auto no-scrollbar">
            <span className="text-xs font-bold text-[#6E6E73] dark:text-[#8E8E93] px-2.5 shrink-0 select-none">
              유형
            </span>
            {masterData.part3Types.map(t => {
              const isSelected = part3TypeFilter === t.id;
              return (
                <button
                  key={t.id}
                  type="button"
                  onClick={() => {
                    stopSpeech();
                    setPart3TypeFilter(t.id);
                    setSelectedIndex(0);
                    setIsAnswerOpen(false);
                  }}
                  className={`px-3 sm:px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-semibold border transition-all whitespace-nowrap shrink-0 ${
                    isSelected
                      ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3] dark:border-[#0A84FF] font-bold shadow-md shadow-blue-500/25 -translate-y-0.5'
                      : 'bg-white/90 dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-[#E5E5EA] border-black/10 dark:border-white/15 hover:border-[#0071E3]/40 hover:text-[#0071E3] dark:hover:text-white shadow-xs'
                  }`}
                >
                  {t.name}
                </button>
              );
            })}
          </div>
        )}

        {/* Part 4 표 속성별 필터 칩 */}
        {activePart === 'part4' && (
          <div className="flex items-center gap-1.5 sm:gap-2 mb-6 p-1.5 sm:p-2 bg-white/70 dark:bg-[#1C1C1E]/75 backdrop-blur-md border border-black/5 dark:border-white/10 rounded-full shadow-xs overflow-x-auto no-scrollbar">
            <span className="text-xs font-bold text-[#6E6E73] dark:text-[#8E8E93] px-2.5 shrink-0 select-none">
              표 속성
            </span>
            {masterData.part4TableTypes.map(t => {
              const isSelected = part4TableTypeFilter === t.id;
              return (
                <button
                  key={t.id}
                  type="button"
                  onClick={() => {
                    stopSpeech();
                    setPart4TableTypeFilter(t.id);
                    setSelectedIndex(0);
                    setP4AnswerOpenMap({});
                    setP4QuestionVisibleMap({});
                  }}
                  className={`px-3 sm:px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-semibold border transition-all whitespace-nowrap shrink-0 ${
                    isSelected
                      ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3] dark:border-[#0A84FF] font-bold shadow-md shadow-blue-500/25 -translate-y-0.5'
                      : 'bg-white/90 dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-[#E5E5EA] border-black/10 dark:border-white/15 hover:border-[#0071E3]/40 hover:text-[#0071E3] dark:hover:text-white shadow-xs'
                  }`}
                >
                  {t.name}
                </button>
              );
            })}
          </div>
        )}

        {/* Part 1 지문 읽기 뷰 */}
        {activePart === 'part1' && currentStandardQ && (
          <article className="bg-white/80 dark:bg-[#1C1C1E]/85 backdrop-blur-2xl border border-white/80 dark:border-white/10 rounded-2xl sm:rounded-3xl p-4 sm:p-8 shadow-sm">
            <div className="flex flex-col sm:flex-row items-stretch sm:items-start justify-between gap-3 sm:gap-4 pb-4 sm:pb-5 mb-5 sm:mb-6 border-b border-black/5 dark:border-white/10">
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 mb-2 flex-wrap">
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20">
                    {currentStandardQ.category}
                  </span>
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93]">
                    준비 45초 · 답변 45초
                  </span>
                </div>
                <h2 className="text-lg sm:text-2xl font-bold tracking-tight text-[#1D1D1F] dark:text-white truncate">
                  {currentStandardQ.qNum} — {currentStandardQ.topic}
                </h2>
              </div>

              <div className="flex items-center justify-between sm:justify-end gap-2 shrink-0 w-full sm:w-auto">
                <button
                  type="button"
                  disabled={selectedIndex === 0}
                  onClick={() => {
                    stopSpeech();
                    setSelectedIndex(i => Math.max(0, i - 1));
                  }}
                  className="flex-1 sm:flex-none px-3.5 py-1.5 rounded-full text-xs font-semibold border border-black/10 dark:border-white/15 bg-white/90 dark:bg-[#2C2C2E] hover:bg-white disabled:opacity-30 transition-all shadow-sm text-center"
                >
                  ← 이전
                </button>
                <button
                  type="button"
                  disabled={selectedIndex >= activeQuestions.length - 1}
                  onClick={() => {
                    stopSpeech();
                    setSelectedIndex(i => Math.min(activeQuestions.length - 1, i + 1));
                  }}
                  className="flex-1 sm:flex-none px-3.5 py-1.5 rounded-full text-xs font-semibold border border-black/10 dark:border-white/15 bg-white/90 dark:bg-[#2C2C2E] hover:bg-white disabled:opacity-30 transition-all shadow-sm text-center"
                >
                  다음 →
                </button>
              </div>
            </div>

            {/* 4. 전체 지문 제일 위 노출 (클릭 시 발음 선택) */}
            {(() => {
              const fullPassage = currentStandardQ.sentences.map(s => s.en).join(' ');
              const fullId = `${currentStandardQ.id}-full`;
              return (
                <div
                  onClick={() => handleSelectSpeech(fullId, fullPassage)}
                  className={`bg-white/95 dark:bg-[#26262A] border border-black/5 dark:border-white/10 rounded-2xl p-6 mb-7 shadow-sm ${getSelectableClass(fullId)}`}
                >
                  <div className="flex items-center justify-between gap-3 mb-3">
                    <span className="text-xs font-bold text-[#6E6E73] dark:text-[#8E8E93] tracking-wide uppercase">
                      전체 지문 (Full Passage) · 클릭하여 선택
                    </span>
                  </div>
                  <p className="text-lg sm:text-xl font-medium text-[#1D1D1F] dark:text-white leading-relaxed">
                    {fullPassage}
                  </p>
                </div>
              );
            })()}

            {/* 문장별 끊어 읽기 (클릭 시 발음 선택) */}
            <div>
              <h3 className="text-base font-bold text-[#1D1D1F] dark:text-white mb-3">
                문장별 끊어 읽기 (클릭하여 선택 후 하단에서 재생)
              </h3>
              <div className="space-y-3">
                {currentStandardQ.sentences.map((s, sIdx) => {
                  const sId = `${currentStandardQ.id}-s${sIdx}`;
                  return (
                    <div
                      key={sIdx}
                      onClick={() => handleSelectSpeech(sId, s.en)}
                      className={`p-4 rounded-2xl bg-white/70 dark:bg-[#26262A] border border-black/5 dark:border-white/10 flex flex-col sm:flex-row sm:items-start justify-between gap-3 ${getSelectableClass(sId)}`}
                    >
                      <div className="space-y-1">
                        <span className="inline-block text-[11px] font-bold px-2 py-0.5 rounded bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF]">
                          문장 {sIdx + 1}
                        </span>
                        <p className="text-base font-semibold text-[#1D1D1F] dark:text-white">{s.en}</p>
                        {s.chunking && (
                          <p className="text-xs font-mono text-[#0056B3] dark:text-[#409CFF] bg-[#0071E3]/5 dark:bg-[#0A84FF]/10 px-2.5 py-1 rounded-md inline-block">
                            {s.chunking}
                          </p>
                        )}
                        <p className="text-sm text-[#6E6E73] dark:text-[#8E8E93]">{s.ko}</p>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* 핵심 발음 어휘 (클릭 시 발음 선택) */}
            <div className="mt-7">
              <h3 className="text-base font-bold text-[#1D1D1F] dark:text-white mb-3">
                핵심 발음 어휘 (클릭하여 선택)
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                {currentStandardQ.vocabulary.map((v, vIdx) => {
                  const vId = `${currentStandardQ.id}-v${vIdx}`;
                  return (
                    <div
                      key={vIdx}
                      onClick={() => handleSelectSpeech(vId, v.word)}
                      className={`p-3 rounded-xl bg-white/70 dark:bg-[#26262A] border border-black/5 dark:border-white/10 flex items-center justify-between gap-2 ${getSelectableClass(vId)}`}
                    >
                      <div>
                        <div>
                          <span className="text-sm font-bold text-[#1D1D1F] dark:text-white">{v.word}</span>
                          <span className="text-xs font-mono text-[#0071E3] dark:text-[#0A84FF] ml-1.5">{v.ipa}</span>
                        </div>
                        <p className="text-xs text-[#6E6E73] dark:text-[#8E8E93] mt-0.5">
                          [{v.pos}] {v.meaning}
                        </p>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {currentStandardQ.readingTips && (
              <div className="mt-6 p-4 rounded-2xl bg-[#34C759]/10 border border-[#34C759]/20 text-sm text-[#166534] dark:text-[#4ADE80]">
                <strong>💡 Part 1 발음 팁:</strong> {currentStandardQ.readingTips}
              </div>
            )}

            {/* CBT 실전 디지털 타이머 */}
            <div className="mt-8 pt-6 border-t border-black/10 dark:border-white/10">
              <div className="p-4 sm:p-5 rounded-2xl bg-[#1D1D1F] dark:bg-[#242426] text-white shadow-lg flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 sm:gap-4 text-center sm:text-left">
                <div className="flex items-center gap-3 justify-center sm:justify-start">
                  <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10 flex items-center justify-center font-mono font-bold text-base sm:text-lg text-[#0071E3] dark:text-[#0A84FF] shrink-0">
                    ⏱
                  </div>
                  <div>
                    <div className="text-[11px] sm:text-xs font-bold text-[#86868B] tracking-wider uppercase">
                      CBT 실전 모의 타이머
                    </div>
                    <div className="text-xs sm:text-sm font-medium">
                      {timerStatus === 'idle' && '준비 45초 ➔ 삐(Beep) ➔ 답변 45초 자동 카운트'}
                      {timerStatus === 'prep' && '🟡 [준비 시간] 지문을 소리 내어 읽으며 준비하세요'}
                      {timerStatus === 'resp' && '🟢 [답변 시간] 실제 시험처럼 또박또박 답변하세요!'}
                      {timerStatus === 'done' && '✅ 답변 시간이 종료되었습니다!'}
                    </div>
                  </div>
                </div>

                <div className="flex items-center justify-center sm:justify-end gap-2.5 sm:gap-3">
                  <span className="font-mono text-2xl sm:text-3xl font-extrabold tracking-tight text-[#0071E3] dark:text-[#0A84FF] bg-white/5 px-3 sm:px-4 py-1 sm:py-1.5 rounded-xl border border-white/10">
                    {String(Math.floor(timeLeft / 60)).padStart(2, '0')}:
                    {String(timeLeft % 60).padStart(2, '0')}
                  </span>
                  <div className="flex items-center gap-1.5">
                    {timerStatus === 'idle' ? (
                      <button
                        type="button"
                        onClick={startCbtTimer}
                        className="px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-xs font-bold bg-[#0071E3] dark:bg-[#0A84FF] hover:bg-[#0077ED] text-white shadow-md transition-all whitespace-nowrap"
                      >
                        ▶ 시험 시작
                      </button>
                    ) : (
                      <>
                        <button
                          type="button"
                          onClick={pauseCbtTimer}
                          className="px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl text-xs font-semibold bg-white/10 hover:bg-white/20 text-white transition-all whitespace-nowrap"
                        >
                          ⏸ 일시정지
                        </button>
                        <button
                          type="button"
                          onClick={resetCbtTimer}
                          className="px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl text-xs font-semibold bg-white/10 hover:bg-white/20 text-[#FF453A] transition-all whitespace-nowrap"
                        >
                          ↺ 초기화
                        </button>
                      </>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </article>
        )}

        {/* Part 4 표 세트 뷰 */}
        {activePart === 'part4' && currentP4Set && (
          <article className="bg-white/80 dark:bg-[#1C1C1E]/85 backdrop-blur-2xl border border-white/80 dark:border-white/10 rounded-2xl sm:rounded-3xl p-4 sm:p-8 shadow-sm">
            <div className="flex flex-col sm:flex-row items-stretch sm:items-start justify-between gap-3 sm:gap-4 pb-4 sm:pb-5 mb-5 sm:mb-6 border-b border-black/5 dark:border-white/10">
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 mb-2 flex-wrap">
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20">
                    {currentP4Set.tableTypeBadge}
                  </span>
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93]">
                    표 읽기 45초 · 연계 문제 {currentP4Set.questions.length}문항
                  </span>
                </div>
                <h2 className="text-lg sm:text-2xl font-bold tracking-tight text-[#1D1D1F] dark:text-white truncate">
                  {currentP4Set.setNum} — {currentP4Set.topic}
                </h2>
              </div>

              <div className="flex items-center justify-between sm:justify-end gap-2 shrink-0 w-full sm:w-auto">
                <button
                  type="button"
                  disabled={selectedIndex === 0}
                  onClick={() => {
                    stopSpeech();
                    setSelectedIndex(i => Math.max(0, i - 1));
                    setP4AnswerOpenMap({});
                    setP4QuestionVisibleMap({});
                  }}
                  className="flex-1 sm:flex-none px-3.5 py-1.5 rounded-full text-xs font-semibold border border-black/10 dark:border-white/15 bg-white/90 dark:bg-[#2C2C2E] hover:bg-white disabled:opacity-30 transition-all shadow-sm text-center"
                >
                  ← 이전 표
                </button>
                <button
                  type="button"
                  disabled={selectedIndex >= activeP4Sets.length - 1}
                  onClick={() => {
                    stopSpeech();
                    setSelectedIndex(i => Math.min(activeP4Sets.length - 1, i + 1));
                    setP4AnswerOpenMap({});
                    setP4QuestionVisibleMap({});
                  }}
                  className="flex-1 sm:flex-none px-3.5 py-1.5 rounded-full text-xs font-semibold border border-black/10 dark:border-white/15 bg-white/90 dark:bg-[#2C2C2E] hover:bg-white disabled:opacity-30 transition-all shadow-sm text-center"
                >
                  다음 표 →
                </button>
              </div>
            </div>

            {/* 표(Schedule Table) */}
            <div className="border border-black/10 dark:border-white/10 rounded-2xl overflow-hidden bg-white dark:bg-[#1C1C1E] mb-7 shadow-sm">
              <div className="bg-[#1D1D1F] dark:bg-[#2C2C2E] text-white py-3.5 px-4 text-center font-bold text-base tracking-wide">
                {currentP4Set.scheduleTable.headerTitle}
              </div>
              <div className="bg-[#F8F8F9] dark:bg-[#242426] px-4 py-2.5 border-b border-black/5 dark:border-white/10 flex flex-wrap justify-center gap-3 sm:gap-4 text-xs text-[#6E6E73] dark:text-[#8E8E93]">
                {currentP4Set.scheduleTable.metaInfo.map((m, mIdx) => (
                  <span key={mIdx}>
                    <strong className="text-[#1D1D1F] dark:text-white">{m.label}:</strong> {m.value}
                  </span>
                ))}
              </div>
              <div className="overflow-x-auto">
                <table className="w-full min-w-[500px] text-xs sm:text-sm border-collapse">
                  <thead>
                    <tr className="bg-[#F2F2F4] dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-white text-left">
                      <th className="p-3 border-b border-black/5 dark:border-white/10">Time / Date</th>
                      <th className="p-3 border-b border-black/5 dark:border-white/10">Session / Person</th>
                      <th className="p-3 border-b border-black/5 dark:border-white/10">Topic / Experience</th>
                      <th className="p-3 border-b border-black/5 dark:border-white/10">Location / Mode</th>
                      <th className="p-3 border-b border-black/5 dark:border-white/10">Note / Speaker</th>
                    </tr>
                  </thead>
                  <tbody>
                    {currentP4Set.scheduleTable.rows.map((r, rIdx) => (
                      <tr key={rIdx} className="border-b border-black/5 dark:border-white/10 hover:bg-black/[0.01] dark:hover:bg-white/[0.02]">
                        <td className="p-3 font-bold">{r.date}</td>
                        <td className="p-3">{r.time}</td>
                        <td className="p-3 font-semibold">{r.event}</td>
                        <td className="p-3">{r.location}</td>
                        <td className="p-3 text-[#6E6E73] dark:text-[#8E8E93]">{r.note}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* 표 연계 문제 목록 */}
            <div>
              <h3 className="text-base font-bold text-[#1D1D1F] dark:text-white mb-4">
                표 연계 문제 (Questions {currentP4Set.questions.length}문항 순차 응답)
              </h3>
              <div className="space-y-6">
                {currentP4Set.questions.map(q => {
                  const isAnsOpen = !!p4AnswerOpenMap[q.qId];
                  const isQVisible = !!p4QuestionVisibleMap[q.qId];
                  const fullSentences = q.sentences.map(s => s.en).join(' ');
                  const qPromptId = `${q.qId}-prompt`;
                  const allAnsId = `${q.qId}-all`;

                  return (
                    <div
                      key={q.qId}
                      className="p-5 sm:p-6 rounded-2xl bg-white/90 dark:bg-[#26262A] border border-black/5 dark:border-white/10 shadow-sm space-y-4"
                    >
                      {/* LC 질문 영역 */}
                      <div className="p-4 rounded-xl bg-black/[0.02] dark:bg-white/[0.02] border border-black/5 dark:border-white/10">
                        <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                          <div className="flex items-center gap-2">
                            <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-[#1D1D1F] dark:bg-white text-white dark:text-[#1D1D1F]">
                              {q.qNum}
                            </span>
                            <span className="text-xs font-semibold text-[#86868B] dark:text-[#A1A1A6]">
                              🎧 실제 시험처럼 질문을 귀로 먼저 듣고 연습하세요
                            </span>
                          </div>
                          <div className="flex items-center gap-2">
                            {/* 질문 선택 버튼 */}
                            <button
                              type="button"
                              onClick={() => handleSelectSpeech(qPromptId, q.question)}
                              className={`px-3 sm:px-3.5 py-1 sm:py-1.5 rounded-full text-xs font-bold border transition-all ${
                                selectedItemId === qPromptId
                                  ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3] shadow-sm'
                                  : 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/20 hover:bg-[#0071E3]/20'
                              }`}
                            >
                              질문듣기
                            </button>
                            <button
                              type="button"
                              onClick={() =>
                                setP4QuestionVisibleMap(prev => ({
                                  ...prev,
                                  [q.qId]: !prev[q.qId]
                                }))
                              }
                              className={`px-3 py-1 rounded-full text-xs font-semibold border transition-all ${
                                isQVisible
                                  ? 'bg-black/5 dark:bg-white/10 text-[#1D1D1F] dark:text-white border-black/15'
                                  : 'bg-white dark:bg-[#2C2C2E] text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/30 hover:bg-[#0071E3]/5'
                              }`}
                            >
                              {isQVisible ? '질문 지문 접기 ▲' : '질문 지문 보기 ▼'}
                            </button>
                          </div>
                        </div>

                        {/* 질문 지문 및 한국어 해석 영역 (클릭 시 선택) */}
                        {isQVisible && (
                          <div
                            onClick={() => handleSelectSpeech(qPromptId, q.question)}
                            className={`mt-3 p-3.5 rounded-xl bg-white dark:bg-[#1C1C1E] border border-black/5 dark:border-white/10 space-y-1.5 animate-in fade-in duration-200 ${getSelectableClass(qPromptId)}`}
                          >
                            <p className="text-base font-bold text-[#1D1D1F] dark:text-white">{q.question}</p>
                            <p className="text-xs sm:text-sm text-[#0071E3] dark:text-[#0A84FF] font-medium">
                              <strong>해석:</strong> {q.questionKo}
                            </p>
                          </div>
                        )}
                      </div>

                      {/* 모범답안 토글 버튼 */}
                      <div className="flex items-center justify-between pt-1 border-t border-black/5 dark:border-white/10">
                        <button
                          type="button"
                          onClick={() => {
                            setP4AnswerOpenMap(prev => ({ ...prev, [q.qId]: !prev[q.qId] }));
                          }}
                          className={`w-full sm:w-auto px-5 py-2.5 sm:py-2 rounded-full text-sm sm:text-base font-bold border transition-all text-center justify-center shadow-xs ${
                            isAnsOpen
                              ? 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/30'
                              : 'bg-white dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-white border-black/10 dark:border-white/15 hover:border-black/20'
                          }`}
                        >
                          {isAnsOpen ? '모범답안 접기 ▲' : '모범답안 보기 ▼'}
                        </button>
                      </div>

                      {/* 모범답안 펼침 영역 */}
                      {isAnsOpen && (
                        <div className="mt-4 pt-4 border-t border-black/5 dark:border-white/10 space-y-4">
                          <div className="flex items-center justify-between gap-3 pb-2 border-b border-black/5 dark:border-white/10">
                            <span className="text-xs font-bold text-[#1D1D1F] dark:text-white">
                              문장별 모범답안 (클릭하여 선택)
                            </span>
                            <button
                              type="button"
                              onClick={() => handleSelectSpeech(allAnsId, fullSentences)}
                              className={`px-3 py-1 rounded-full text-xs font-semibold border transition-all ${
                                selectedItemId === allAnsId
                                  ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3]'
                                  : 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/20 hover:bg-[#0071E3]/20'
                              }`}
                            >
                              전체 모범답안 선택
                            </button>
                          </div>

                          {/* 문장별 모범답안 (클릭 시 선택) */}
                          <div className="space-y-2.5">
                            {q.sentences.map((s, sIdx) => {
                              const sId = `${q.qId}-ms${sIdx}`;
                              return (
                                <div
                                  key={sIdx}
                                  onClick={() => handleSelectSpeech(sId, s.en)}
                                  className={`p-3.5 rounded-xl bg-white/80 dark:bg-[#1C1C1E] border border-black/5 dark:border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-3 ${getSelectableClass(sId)}`}
                                >
                                  <div>
                                    {s.step && (
                                      <span className="text-[11px] font-bold px-2 py-0.5 rounded bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] inline-block mb-1">
                                        {s.step}
                                      </span>
                                    )}
                                    <p className="text-sm sm:text-base font-semibold text-[#1D1D1F] dark:text-white">
                                      {s.en}
                                    </p>
                                    <p className="text-xs sm:text-sm text-[#6E6E73] dark:text-[#8E8E93]">{s.ko}</p>
                                  </div>
                                </div>
                              );
                            })}
                          </div>

                          {/* 만능문장 */}
                          {q.magicSentences && q.magicSentences.length > 0 && (
                            <div className="space-y-2">
                              {q.magicSentences.map((m, mIdx) => {
                                const mId = `${q.qId}-mg${mIdx}`;
                                return (
                                  <div
                                    key={mIdx}
                                    onClick={() => handleSelectSpeech(mId, m.en)}
                                    className={`p-3 rounded-xl bg-[#FF9500]/10 border border-[#FF9500]/20 flex items-center justify-between gap-3 ${getSelectableClass(mId)}`}
                                  >
                                    <div>
                                      <p className="text-xs sm:text-sm font-bold text-[#92400E] dark:text-[#FBBF24]">
                                        {m.en}
                                      </p>
                                      <p className="text-xs text-[#B45309] dark:text-[#FCD34D]">{m.ko}</p>
                                      {m.tip && (
                                        <p className="text-[11px] text-[#D97706] mt-0.5">
                                          💡 {m.tip}
                                        </p>
                                      )}
                                    </div>
                                  </div>
                                );
                              })}
                            </div>
                          )}

                          {/* 어휘 */}
                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                            {q.vocabulary.map((v, vIdx) => {
                              const vId = `${q.qId}-vv${vIdx}`;
                              return (
                                <div
                                  key={vIdx}
                                  onClick={() => handleSelectSpeech(vId, v.word)}
                                  className={`p-2.5 rounded-lg bg-white/70 dark:bg-[#1C1C1E] border border-black/5 dark:border-white/10 flex items-center justify-between gap-2 ${getSelectableClass(vId)}`}
                                >
                                  <div>
                                    <span className="text-xs font-bold text-[#1D1D1F] dark:text-white">{v.word}</span>
                                    <span className="text-[11px] font-mono text-[#0071E3] dark:text-[#0A84FF] ml-1">
                                      {v.ipa}
                                    </span>
                                    <p className="text-[11px] text-[#6E6E73] dark:text-[#8E8E93]">
                                      [{v.pos}] {v.meaning}
                                    </p>
                                  </div>
                                </div>
                              );
                            })}
                          </div>

                          {q.explanation && (
                            <div className="p-3 rounded-xl bg-[#34C759]/10 border border-[#34C759]/20 text-xs sm:text-sm text-[#166534] dark:text-[#4ADE80]">
                              <strong>💡 답변 팁:</strong> {q.explanation}
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>

            {/* CBT 실전 모의 타이머 */}
            <div className="mt-8 pt-6 border-t border-black/10 dark:border-white/10">
              <div className="p-4 sm:p-5 rounded-2xl bg-[#1D1D1F] dark:bg-[#242426] text-white shadow-lg flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 sm:gap-4 text-center sm:text-left">
                <div className="flex items-center gap-3 justify-center sm:justify-start">
                  <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10 flex items-center justify-center font-mono font-bold text-base sm:text-lg text-[#0071E3] dark:text-[#0A84FF] shrink-0">
                    ⏱
                  </div>
                  <div>
                    <div className="text-[11px] sm:text-xs font-bold text-[#86868B] tracking-wider uppercase">
                      CBT 실전 모의 타이머
                    </div>
                    <div className="text-xs sm:text-sm font-medium">
                      {timerStatus === 'idle' && '표 분석 45초 ➔ 삐(Beep) ➔ 답변 15초 카운트'}
                      {timerStatus === 'prep' && '🟡 [표 분석] 표의 일정을 주의 깊게 스캔하세요'}
                      {timerStatus === 'resp' && '🟢 [답변 시간] 질문에 맞춰 침착하게 답변하세요!'}
                      {timerStatus === 'done' && '✅ 답변 시간이 종료되었습니다!'}
                    </div>
                  </div>
                </div>

                <div className="flex items-center justify-center sm:justify-end gap-2.5 sm:gap-3">
                  <span className="font-mono text-2xl sm:text-3xl font-extrabold tracking-tight text-[#0071E3] dark:text-[#0A84FF] bg-white/5 px-3 sm:px-4 py-1 sm:py-1.5 rounded-xl border border-white/10">
                    {String(Math.floor(timeLeft / 60)).padStart(2, '0')}:
                    {String(timeLeft % 60).padStart(2, '0')}
                  </span>
                  <div className="flex items-center gap-1.5">
                    {timerStatus === 'idle' ? (
                      <button
                        type="button"
                        onClick={startCbtTimer}
                        className="px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-xs font-bold bg-[#0071E3] dark:bg-[#0A84FF] hover:bg-[#0077ED] text-white shadow-md transition-all whitespace-nowrap"
                      >
                        ▶ 시험 시작
                      </button>
                    ) : (
                      <>
                        <button
                          type="button"
                          onClick={pauseCbtTimer}
                          className="px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl text-xs font-semibold bg-white/10 hover:bg-white/20 text-white transition-all whitespace-nowrap"
                        >
                          ⏸ 일시정지
                        </button>
                        <button
                          type="button"
                          onClick={resetCbtTimer}
                          className="px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl text-xs font-semibold bg-white/10 hover:bg-white/20 text-[#FF453A] transition-all whitespace-nowrap"
                        >
                          ↺ 초기화
                        </button>
                      </>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </article>
        )}

        {/* Part 2, Part 3, Part 5 표준 문제 뷰 */}
        {activePart !== 'part1' && activePart !== 'part4' && currentStandardQ && (
          <article className="bg-white/80 dark:bg-[#1C1C1E]/85 backdrop-blur-2xl border border-white/80 dark:border-white/10 rounded-2xl sm:rounded-3xl p-4 sm:p-8 shadow-sm">
            <div className="flex flex-col sm:flex-row items-stretch sm:items-start justify-between gap-3 sm:gap-4 pb-4 sm:pb-5 mb-5 sm:mb-6 border-b border-black/5 dark:border-white/10">
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 mb-2 flex-wrap">
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20">
                    {currentStandardQ.typeBadge || currentStandardQ.category}
                  </span>
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93]">
                    준비 {currentStandardQ.prepTime}초 · 답변 {currentStandardQ.responseTime}초
                  </span>
                </div>
                <h2 className="text-lg sm:text-2xl font-bold tracking-tight text-[#1D1D1F] dark:text-white truncate">
                  {currentStandardQ.qNum} — {currentStandardQ.topic}
                </h2>
              </div>

              <div className="flex items-center justify-between sm:justify-end gap-2 shrink-0 w-full sm:w-auto">
                <button
                  type="button"
                  disabled={selectedIndex === 0}
                  onClick={() => {
                    stopSpeech();
                    setSelectedIndex(i => Math.max(0, i - 1));
                    setIsAnswerOpen(false);
                  }}
                  className="flex-1 sm:flex-none px-3.5 py-1.5 rounded-full text-xs font-semibold border border-black/10 dark:border-white/15 bg-white/90 dark:bg-[#2C2C2E] hover:bg-white disabled:opacity-30 transition-all shadow-sm text-center"
                >
                  ← 이전
                </button>
                <button
                  type="button"
                  disabled={selectedIndex >= activeQuestions.length - 1}
                  onClick={() => {
                    stopSpeech();
                    setSelectedIndex(i => Math.min(activeQuestions.length - 1, i + 1));
                    setIsAnswerOpen(false);
                  }}
                  className="flex-1 sm:flex-none px-3.5 py-1.5 rounded-full text-xs font-semibold border border-black/10 dark:border-white/15 bg-white/90 dark:bg-[#2C2C2E] hover:bg-white disabled:opacity-30 transition-all shadow-sm text-center"
                >
                  다음 →
                </button>
              </div>
            </div>

            {/* Part 2 사진 (레터박스 없이 꽉 차게) */}
            {currentStandardQ.part === 2 && currentStandardQ.imageBase64 && (
              <div className="w-full rounded-2xl overflow-hidden mb-6 border border-black/10 dark:border-white/10 bg-black/5 shadow-md flex items-center justify-center max-h-[320px] sm:max-h-[540px]">
                <img
                  src={currentStandardQ.imageBase64}
                  alt={currentStandardQ.topic}
                  className="w-full h-auto max-h-[320px] sm:max-h-[540px] object-cover sm:object-contain rounded-2xl"
                />
              </div>
            )}

            {/* 질문 프롬프트 (클릭 시 선택) */}
            {currentStandardQ.question && (() => {
              const promptId = `${currentStandardQ.id}-prompt`;
              return (
                <div
                  onClick={() => handleSelectSpeech(promptId, currentStandardQ.question || '')}
                  className={`p-5 rounded-2xl bg-white/90 dark:bg-[#26262A] border border-black/5 dark:border-white/10 mb-6 shadow-sm ${getSelectableClass(promptId)}`}
                >
                  <div className="flex items-center justify-between gap-3 mb-2">
                    <span className="text-xs font-bold text-[#6E6E73] dark:text-[#8E8E93] tracking-wide uppercase">
                      QUESTION PROMPT · 클릭하여 선택
                    </span>
                  </div>
                  <p className="text-base sm:text-lg font-bold text-[#1D1D1F] dark:text-white">
                    {currentStandardQ.question}
                  </p>
                </div>
              );
            })()}

            {/* 모범답안 토글 버튼 */}
            <div className="flex items-center justify-between pt-1">
              <button
                type="button"
                onClick={() => setIsAnswerOpen(prev => !prev)}
                className={`w-full sm:w-auto px-5 py-3 sm:py-2.5 rounded-full text-sm sm:text-base font-bold border transition-all text-center justify-center shadow-xs ${
                  isAnswerOpen
                    ? 'bg-[#0071E3]/15 dark:bg-[#0A84FF]/25 text-[#0071E3] dark:text-[#64D2FF] border-[#0071E3]/40'
                    : 'bg-white dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-white border-black/10 dark:border-white/15 hover:border-black/20'
                }`}
              >
                {isAnswerOpen ? '모범답안 접기 ▲' : '모범답안 보기 ▼'}
              </button>
            </div>

            {/* 모범답안 펼침 영역 */}
            {isAnswerOpen && (() => {
              const fullModelAns = currentStandardQ.sentences.map(s => s.en).join(' ');
              const fullModelId = `${currentStandardQ.id}-all`;
              return (
                <div className="mt-5 pt-5 border-t border-black/5 dark:border-white/10 space-y-6">
                  {currentStandardQ.questionKo && (
                    <div className="p-3.5 rounded-xl bg-black/5 dark:bg-white/5 border-l-4 border-[#0071E3] dark:border-[#0A84FF] text-sm text-[#48484A] dark:text-[#A1A1A6]">
                      <strong>질문 해석:</strong> {currentStandardQ.questionKo}
                    </div>
                  )}

                  {/* 문장별 모범답안 */}
                  <div>
                    <div className="flex items-center justify-between gap-3 mb-3 pb-2 border-b border-black/5 dark:border-white/10">
                      <h3 className="text-base font-bold text-[#1D1D1F] dark:text-white">
                        문장별 모범답안 (클릭하여 선택 후 하단에서 재생)
                      </h3>
                      <button
                        type="button"
                        onClick={() => handleSelectSpeech(fullModelId, fullModelAns)}
                        className={`px-3 py-1 rounded-full text-xs font-semibold border transition-all ${
                          selectedItemId === fullModelId
                            ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3]'
                            : 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/20 hover:bg-[#0071E3]/20'
                        }`}
                      >
                        전체 모범답안 선택
                      </button>
                    </div>

                    <div className="space-y-2.5">
                      {currentStandardQ.sentences.map((s, sIdx) => {
                        const sId = `${currentStandardQ.id}-ms${sIdx}`;
                        return (
                          <div
                            key={sIdx}
                            onClick={() => handleSelectSpeech(sId, s.en)}
                            className={`p-4 rounded-2xl bg-white/70 dark:bg-[#26262A] border border-black/5 dark:border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-3 ${getSelectableClass(sId)}`}
                          >
                            <div>
                              {s.step && (
                                <span className="text-[11px] font-bold px-2 py-0.5 rounded bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] inline-block mb-1">
                                  {s.step}
                                </span>
                              )}
                              <p className="text-base font-semibold text-[#1D1D1F] dark:text-white">{s.en}</p>
                              <p className="text-sm text-[#6E6E73] dark:text-[#8E8E93] mt-0.5">{s.ko}</p>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>

                  {/* 쓰인 만능문장 */}
                  {currentStandardQ.magicSentences && currentStandardQ.magicSentences.length > 0 && (
                    <div>
                      <h3 className="text-base font-bold text-[#1D1D1F] dark:text-white mb-3">
                        적용된 만능문장 표현 (클릭하여 선택)
                      </h3>
                      <div className="space-y-2">
                        {currentStandardQ.magicSentences.map((m, mIdx) => {
                          const mId = `${currentStandardQ.id}-mg${mIdx}`;
                          return (
                            <div
                              key={mIdx}
                              onClick={() => handleSelectSpeech(mId, m.en)}
                              className={`p-3.5 rounded-2xl bg-[#FF9500]/10 border border-[#FF9500]/20 flex items-center justify-between gap-3 ${getSelectableClass(mId)}`}
                            >
                              <div>
                                <p className="text-sm font-bold text-[#92400E] dark:text-[#FBBF24]">{m.en}</p>
                                <p className="text-xs text-[#B45309] dark:text-[#FCD34D]">{m.ko}</p>
                                {m.tip && (
                                  <p className="text-xs text-[#D97706] mt-1">💡 {m.tip}</p>
                                )}
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  )}

                  {/* 핵심 어휘 */}
                  <div>
                    <h3 className="text-base font-bold text-[#1D1D1F] dark:text-white mb-3">
                      핵심 어휘 (클릭하여 선택)
                    </h3>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                      {currentStandardQ.vocabulary.map((v, vIdx) => {
                        const vId = `${currentStandardQ.id}-vv${vIdx}`;
                        return (
                          <div
                            key={vIdx}
                            onClick={() => handleSelectSpeech(vId, v.word)}
                            className={`p-3 rounded-xl bg-white/70 dark:bg-[#26262A] border border-black/5 dark:border-white/10 flex items-center justify-between gap-2 ${getSelectableClass(vId)}`}
                          >
                            <div>
                              <span className="text-sm font-bold text-[#1D1D1F] dark:text-white">{v.word}</span>
                              <span className="text-xs font-mono text-[#0071E3] dark:text-[#0A84FF] ml-1.5">{v.ipa}</span>
                              <p className="text-xs text-[#6E6E73] dark:text-[#8E8E93] mt-0.5">
                                [{v.pos}] {v.meaning}
                              </p>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>

                  {currentStandardQ.explanation && (
                    <div className="p-4 rounded-2xl bg-[#34C759]/10 border border-[#34C759]/20 text-sm text-[#166534] dark:text-[#4ADE80]">
                      <strong>💡 고득점 해설 전략:</strong> {currentStandardQ.explanation}
                    </div>
                  )}
                </div>
              );
            })()}

            {/* CBT 실전 디지털 타이머 */}
            <div className="mt-8 pt-6 border-t border-black/10 dark:border-white/10">
              <div className="p-4 sm:p-5 rounded-2xl bg-[#1D1D1F] dark:bg-[#242426] text-white shadow-lg flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 sm:gap-4 text-center sm:text-left">
                <div className="flex items-center gap-3 justify-center sm:justify-start">
                  <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10 flex items-center justify-center font-mono font-bold text-base sm:text-lg text-[#0071E3] dark:text-[#0A84FF] shrink-0">
                    ⏱
                  </div>
                  <div>
                    <div className="text-[11px] sm:text-xs font-bold text-[#86868B] tracking-wider uppercase">
                      CBT 실전 모의 타이머
                    </div>
                    <div className="text-xs sm:text-sm font-medium">
                      {timerStatus === 'idle' &&
                        `준비 ${targetPrepTime}초 ➔ 삐(Beep) ➔ 답변 ${targetRespTime}초 자동 카운트`}
                      {timerStatus === 'prep' && '🟡 [준비 시간] 키워드와 문장 구조를 머릿속으로 정리하세요'}
                      {timerStatus === 'resp' && '🟢 [답변 시간] 자신감 있는 톤으로 답변하세요!'}
                      {timerStatus === 'done' && '✅ 답변 시간이 종료되었습니다!'}
                    </div>
                  </div>
                </div>

                <div className="flex items-center justify-center sm:justify-end gap-2.5 sm:gap-3">
                  <span className="font-mono text-2xl sm:text-3xl font-extrabold tracking-tight text-[#0071E3] dark:text-[#0A84FF] bg-white/5 px-3 sm:px-4 py-1 sm:py-1.5 rounded-xl border border-white/10">
                    {String(Math.floor(timeLeft / 60)).padStart(2, '0')}:
                    {String(timeLeft % 60).padStart(2, '0')}
                  </span>
                  <div className="flex items-center gap-1.5">
                    {timerStatus === 'idle' ? (
                      <button
                        type="button"
                        onClick={startCbtTimer}
                        className="px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-xs font-bold bg-[#0071E3] dark:bg-[#0A84FF] hover:bg-[#0077ED] text-white shadow-md transition-all whitespace-nowrap"
                      >
                        ▶ 시험 시작
                      </button>
                    ) : (
                      <>
                        <button
                          type="button"
                          onClick={pauseCbtTimer}
                          className="px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl text-xs font-semibold bg-white/10 hover:bg-white/20 text-white transition-all whitespace-nowrap"
                        >
                          ⏸ 일시정지
                        </button>
                        <button
                          type="button"
                          onClick={resetCbtTimer}
                          className="px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl text-xs font-semibold bg-white/10 hover:bg-white/20 text-[#FF453A] transition-all whitespace-nowrap"
                        >
                          ↺ 초기화
                        </button>
                      </>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </article>
        )}
      </main>

      {/* 1 & 3. 하단 중앙 플로팅 바 (문항목록 | 이전 | 번호 | 다음 | 정지 | 1.0x | 0.75x 순서) */}
      <aside className="fixed bottom-[calc(16px+env(safe-area-inset-bottom,12px))] sm:bottom-9 left-1/2 -translate-x-1/2 z-40 bg-white/95 dark:bg-[#1C1C1E]/95 backdrop-blur-2xl border border-white/90 dark:border-white/15 shadow-2xl rounded-full px-2.5 sm:px-4 py-2 sm:py-2.5 flex items-center justify-between sm:justify-center gap-1.5 sm:gap-2.5 w-[calc(100%-16px)] max-w-xl sm:w-auto">
        <button
          type="button"
          onClick={() => setIsDrawerOpen(true)}
          className="px-2.5 sm:px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-bold text-[#1D1D1F] dark:text-[#F5F5F7] bg-black/5 dark:bg-white/10 hover:bg-black/10 dark:hover:bg-white/15 transition-all flex items-center gap-1 shadow-xs shrink-0"
        >
          <span>☰</span>
          <span className="hidden sm:inline"> 문항 목록</span>
          <span className="inline sm:hidden"> 목록</span>
        </button>

        <div className="h-4 w-px bg-black/10 dark:bg-white/15 shrink-0"></div>

        <button
          type="button"
          disabled={selectedIndex === 0}
          onClick={() => {
            stopSpeech();
            setSelectedIndex(i => Math.max(0, i - 1));
            setIsAnswerOpen(false);
            setP4AnswerOpenMap({});
            setP4QuestionVisibleMap({});
          }}
          className="px-2.5 sm:px-3 py-1.5 rounded-full text-xs sm:text-sm font-bold text-[#1D1D1F] dark:text-[#F5F5F7] hover:bg-black/5 dark:hover:bg-white/10 disabled:opacity-30 transition-all shrink-0"
        >
          <span className="hidden sm:inline">← 이전</span>
          <span className="inline sm:hidden">←</span>
        </button>

        <span className="text-xs sm:text-sm font-bold text-[#1D1D1F] dark:text-[#F5F5F7] px-1 font-mono shrink-0">
          <strong>{selectedIndex + 1}</strong> / {totalItemsCount}
        </span>

        <button
          type="button"
          disabled={selectedIndex >= totalItemsCount - 1}
          onClick={() => {
            stopSpeech();
            setSelectedIndex(i => Math.min(totalItemsCount - 1, i + 1));
            setIsAnswerOpen(false);
            setP4AnswerOpenMap({});
            setP4QuestionVisibleMap({});
          }}
          className="px-2.5 sm:px-3 py-1.5 rounded-full text-xs sm:text-sm font-bold text-[#0071E3] dark:text-[#0A84FF] hover:bg-[#0071E3]/10 disabled:opacity-30 transition-all shrink-0"
        >
          <span className="hidden sm:inline">다음 →</span>
          <span className="inline sm:hidden">→</span>
        </button>

        <div className="h-4 w-px bg-black/10 dark:bg-white/15 shrink-0"></div>

        {/* 1. 정지 버튼 */}
        <button
          type="button"
          onClick={stopSpeech}
          className={`px-2.5 sm:px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-bold border transition-all shrink-0 ${
            playingKey
              ? 'bg-[#FF3B30] text-white border-[#FF3B30] shadow-md animate-pulse'
              : 'bg-black/5 dark:bg-white/10 text-[#86868B] dark:text-[#A1A1A6] border-black/10 dark:border-white/15 hover:bg-black/10 hover:text-[#1D1D1F] dark:hover:text-white'
          }`}
          title="음성 정지"
        >
          <span>⏹</span>
          <span className="hidden sm:inline"> 정지</span>
        </button>

        {/* 1. 배속 토글 버튼 (1.0x, 0.75x) */}
        <button
          type="button"
          onClick={() => playSelectedRate(1.0)}
          className={`px-2.5 sm:px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-bold border transition-all shrink-0 ${
            playingKey === 'selected-1'
              ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3] shadow-md shadow-blue-500/30'
              : 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/20 hover:bg-[#0071E3]/20'
          }`}
          title="원어민 Daniel 1.0x 발음"
        >
          1.0x
        </button>
        <button
          type="button"
          onClick={() => playSelectedRate(0.75)}
          className={`px-2.5 sm:px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-bold border transition-all shrink-0 ${
            playingKey === 'selected-0.75'
              ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3] shadow-md shadow-blue-500/30'
              : 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/20 hover:bg-[#0071E3]/20'
          }`}
          title="원어민 Daniel 0.75x 느린 발음"
        >
          0.75x
        </button>
      </aside>

      {/* 문항 목록 리퀴드 글래스 사이드 드로어 */}
      {isDrawerOpen && (
        <div className="fixed inset-0 z-50 flex">
          <div
            className="fixed inset-0 bg-black/30 backdrop-blur-sm transition-opacity"
            onClick={() => setIsDrawerOpen(false)}
          ></div>
          <aside className="relative w-80 max-w-[85vw] bg-white/95 dark:bg-[#1C1C1E]/95 backdrop-blur-2xl border-r border-white/80 dark:border-white/10 shadow-2xl flex flex-col z-10 animate-in slide-in-from-left duration-200">
            <div className="p-5 border-b border-black/5 dark:border-white/10 flex items-center justify-between">
              <span className="text-base font-bold text-[#1D1D1F] dark:text-white">
                {activePart.toUpperCase()} 문항 목록 ({totalItemsCount})
              </span>
              <button
                type="button"
                onClick={() => setIsDrawerOpen(false)}
                className="w-7 h-7 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93] hover:text-[#1D1D1F] dark:hover:text-white font-bold flex items-center justify-center text-sm"
              >
                ✕
              </button>
            </div>
            <div className="flex-1 overflow-y-auto p-3 space-y-1.5">
              {activePart === 'part4'
                ? activeP4Sets.map((s, idx) => (
                    <button
                      key={s.id}
                      type="button"
                      onClick={() => {
                        stopSpeech();
                        setSelectedIndex(idx);
                        setP4AnswerOpenMap({});
                        setP4QuestionVisibleMap({});
                        setIsDrawerOpen(false);
                      }}
                      className={`w-full text-left p-3 rounded-xl border transition-all ${
                        idx === selectedIndex
                          ? 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 border-[#0071E3] dark:border-[#0A84FF] shadow-sm'
                          : 'bg-white/60 dark:bg-[#2C2C2E]/60 border-black/5 dark:border-white/10 hover:bg-white dark:hover:bg-[#2C2C2E]'
                      }`}
                    >
                      <div className="flex items-center justify-between gap-1 mb-1">
                        <strong className="text-xs text-[#1D1D1F] dark:text-white">{s.setNum}</strong>
                        <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF]">
                          {s.tableTypeBadge}
                        </span>
                      </div>
                      <p className="text-xs text-[#6E6E73] dark:text-[#8E8E93] line-clamp-2">{s.topic}</p>
                    </button>
                  ))
                : activeQuestions.map((q, idx) => (
                    <button
                      key={q.id}
                      type="button"
                      onClick={() => {
                        stopSpeech();
                        setSelectedIndex(idx);
                        setIsAnswerOpen(false);
                        setIsDrawerOpen(false);
                      }}
                      className={`w-full text-left p-3 rounded-xl border transition-all ${
                        idx === selectedIndex
                          ? 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 border-[#0071E3] dark:border-[#0A84FF] shadow-sm'
                          : 'bg-white/60 dark:bg-[#2C2C2E]/60 border-black/5 dark:border-white/10 hover:bg-white dark:hover:bg-[#2C2C2E]'
                      }`}
                    >
                      <div className="flex items-center justify-between gap-1 mb-1">
                        <strong className="text-xs text-[#1D1D1F] dark:text-white">{q.qNum}</strong>
                        <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF]">
                          {q.typeBadge || q.category}
                        </span>
                      </div>
                      <p className="text-xs text-[#6E6E73] dark:text-[#8E8E93] line-clamp-2">{q.topic}</p>
                    </button>
                  ))}
            </div>
          </aside>
        </div>
      )}

      {/* 시계토끼 만능문장 187 리퀴드 글래스 모달 */}
      {isVocabModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4">
          <div
            className="fixed inset-0 bg-black/40 backdrop-blur-md transition-opacity"
            onClick={() => setIsVocabModalOpen(false)}
          ></div>
          <div className="relative w-full max-w-4xl h-[92vh] sm:h-[85vh] bg-white/95 dark:bg-[#1C1C1E]/95 backdrop-blur-3xl border border-white/80 dark:border-white/15 rounded-2xl sm:rounded-3xl shadow-2xl flex flex-col overflow-hidden z-10 animate-in zoom-in-95 duration-200">
            <div className="p-3.5 sm:p-5 border-b border-black/5 dark:border-white/10 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
              <div className="flex items-center justify-between">
                <div>
                  <h2 className="text-base sm:text-lg font-bold text-[#1D1D1F] dark:text-white">
                    🐰 시계토끼 만능문장 187 단어장
                  </h2>
                  <p className="text-[11px] sm:text-xs text-[#6E6E73] dark:text-[#8E8E93]">
                    Part 2~5 구성 · 원어민 Daniel · 암기: <strong>{memorizedCount}</strong> / {magicData.items.length}개
                  </p>
                </div>
                <button
                  type="button"
                  onClick={() => setIsVocabModalOpen(false)}
                  className="sm:hidden w-8 h-8 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93] hover:text-[#1D1D1F] dark:hover:text-white font-bold flex items-center justify-center text-sm"
                >
                  ✕
                </button>
              </div>

              <div className="flex items-center gap-2">
                <input
                  type="search"
                  value={modalSearch}
                  onChange={e => setModalSearch(e.target.value)}
                  placeholder="영어 표현, 한국어 뜻 검색..."
                  className="px-3.5 py-1.5 rounded-full border border-black/10 dark:border-white/15 text-xs bg-white dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-white w-full sm:min-w-[200px] outline-none"
                />
                <button
                  type="button"
                  onClick={() => setIsVocabModalOpen(false)}
                  className="hidden sm:flex w-7 h-7 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93] hover:text-[#1D1D1F] dark:hover:text-white font-bold items-center justify-center text-sm"
                >
                  ✕
                </button>
              </div>
            </div>

            {/* 단어장 파트 필터 (Part 1 제외) */}
            <div className="px-3 sm:px-5 py-2 sm:py-2.5 border-b border-black/5 dark:border-white/10 flex flex-wrap gap-1.5 overflow-x-auto no-scrollbar">
              {[
                { id: 'ALL', label: `전체 (${magicData.items.length})` },
                { id: '2', label: 'Part 2 사진 (49)' },
                { id: '3', label: 'Part 3 질문 (47)' },
                { id: '4', label: 'Part 4 표 (38)' },
                { id: '5', label: 'Part 5 의견 (53)' }
              ].map(f => (
                <button
                  key={f.id}
                  type="button"
                  onClick={() => setModalPartFilter(f.id)}
                  className={`px-2.5 sm:px-3 py-1 rounded-full text-xs font-semibold border transition-all whitespace-nowrap ${
                    modalPartFilter === f.id
                      ? 'bg-[#1D1D1F] dark:bg-white text-white dark:text-[#1D1D1F] border-[#1D1D1F] dark:border-white'
                      : 'bg-white/70 dark:bg-[#2C2C2E] text-[#6E6E73] dark:text-[#8E8E93] border-black/10 dark:border-white/10 hover:border-black/20'
                  }`}
                >
                  {f.label}
                </button>
              ))}
            </div>

            <div className="flex-1 overflow-y-auto p-3 sm:p-5">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5 sm:gap-3">
                {filteredVocabItems.map(item => {
                  const isMem = !!memorizedIds[item.id];
                  return (
                    <div
                      key={item.id}
                      className={`p-4 rounded-2xl border flex flex-col justify-between gap-2.5 transition-all ${
                        isMem
                          ? 'bg-[#34C759]/10 border-[#34C759]/30'
                          : 'bg-white/80 dark:bg-[#242426] border-black/5 dark:border-white/10'
                      }`}
                    >
                      <div>
                        <div className="flex items-center justify-between gap-2 mb-2">
                          <div className="flex items-center gap-1.5">
                            <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-[#1D1D1F] dark:bg-white text-white dark:text-[#1D1D1F]">
                              Part {item.part}
                            </span>
                            <span className="text-xs font-bold text-[#0071E3] dark:text-[#0A84FF]">{item.id}</span>
                            <span className="text-xs font-medium text-[#86868B] dark:text-[#A1A1A6]">
                              {item.category}
                            </span>
                          </div>
                          <button
                            type="button"
                            onClick={() => toggleMemorized(item.id)}
                            className={`px-2.5 py-0.5 rounded-full text-[11px] font-semibold border transition-all ${
                              isMem
                                ? 'bg-[#34C759] text-white border-[#34C759]'
                                : 'bg-white dark:bg-[#2C2C2E] text-[#6E6E73] dark:text-[#8E8E93] border-black/10 dark:border-white/15'
                            }`}
                          >
                            {isMem ? '✓ 암기완료' : '암기 체크'}
                          </button>
                        </div>
                        <p className="text-base font-bold text-[#1D1D1F] dark:text-white leading-snug">{item.en}</p>
                        <p className="text-xs sm:text-sm text-[#6E6E73] dark:text-[#8E8E93] mt-1">{item.ko}</p>
                        {item.tip && (
                          <p className="text-xs text-[#FF9500] font-medium mt-1.5">
                            💡 {item.tip}
                          </p>
                        )}
                      </div>
                      <div className="flex justify-end pt-2 border-t border-black/5 dark:border-white/10 gap-2">
                        <button
                          type="button"
                          onClick={() => speakText(item.en, 1.0, `v-${item.id}-1`)}
                          className="px-2.5 py-1 rounded-full text-xs font-semibold bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20 hover:bg-[#0071E3]/20"
                        >
                          1.0x
                        </button>
                        <button
                          type="button"
                          onClick={() => speakText(item.en, 0.75, `v-${item.id}-075`)}
                          className="px-2.5 py-1 rounded-full text-xs font-semibold bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20 hover:bg-[#0071E3]/20"
                        >
                          0.75x
                        </button>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ToeicSpeakingApp;
