import React, { useState, useEffect, useMemo, useRef } from 'react';
import masterDataRaw from './data/toeic_parts_master.json';
import magicDataRaw from './data/magic_187_vocab.json';
import vocabDataRaw from './data/toeic_essential_vocab.json';

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

interface EssentialVocabItem {
  id: string;
  word: string;
  ipa: string;
  pos: string;
  meaning: string;
  part: number;
  category: string;
  collocation?: string;
  example: string;
  exampleKo: string;
  tip?: string;
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

const cleanEnglishTopic = (topic: string): string => {
  if (!topic) return '';
  const match = topic.match(/\(([^)]+)\)/);
  if (match && /[a-zA-Z]/.test(match[1])) {
    return match[1].trim();
  }
  return topic.trim();
};

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

const vocabData = vocabDataRaw as {
  metadata: {
    title: string;
    totalCount?: number;
    total_count?: number;
  };
  items: EssentialVocabItem[];
};

type ActivePart = 'part1' | 'part2' | 'part3' | 'part4' | 'part5';
type ModalMainMode = 'magic' | 'vocab';

const playBeepAudio = (freq = 1000, durationMs = 300) => {
  try {
    const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = new AudioCtx();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, ctx.currentTime);
    gain.gain.setValueAtTime(0.15, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + durationMs / 1000);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + durationMs / 1000);
  } catch (e) {
    console.warn('Beep audio not supported or blocked:', e);
  }
};

interface CbtTimerCardProps {
  prepTime: number;
  responseTime: number;
  label?: string;
  defaultBadge?: string;
  timerId?: string;
  className?: string;
}

const CbtTimerCard: React.FC<CbtTimerCardProps> = ({
  prepTime,
  responseTime,
  label,
  defaultBadge,
  timerId = 'main',
  className,
}) => {
  const [stage, setStage] = useState<'standby' | 'prep' | 'response' | 'ended'>('standby');
  const [remaining, setRemaining] = useState<number>(prepTime > 0 ? prepTime : responseTime);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const intervalRef = useRef<any>(null);

  // 시간 설정이 바뀌면 초기화
  useEffect(() => {
    if (intervalRef.current) clearInterval(intervalRef.current);
    intervalRef.current = null;
    setIsRunning(false);
    setStage('standby');
    setRemaining(prepTime > 0 ? prepTime : responseTime);
    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current);
    };
  }, [prepTime, responseTime]);

  const toggleTimer = () => {
    if (isRunning && intervalRef.current) {
      // 일시정지
      clearInterval(intervalRef.current);
      intervalRef.current = null;
      setIsRunning(false);
      return;
    }

    // 시작 또는 재개
    let currentStage = stage;
    let currentRemaining = remaining;

    if (currentStage === 'standby' || currentStage === 'ended') {
      if (prepTime > 0) {
        currentStage = 'prep';
        currentRemaining = prepTime;
      } else {
        currentStage = 'response';
        currentRemaining = responseTime;
      }
      setStage(currentStage);
      setRemaining(currentRemaining);
    }

    setIsRunning(true);

    intervalRef.current = setInterval(() => {
      currentRemaining -= 1;
      if (currentRemaining <= 0) {
        if (currentStage === 'prep') {
          playBeepAudio(1000, 400); // 삐- 신호음
          if (responseTime > 0) {
            currentStage = 'response';
            currentRemaining = responseTime;
            setStage('response');
            setRemaining(currentRemaining);
          } else {
            // 준비 시간 전용 (예: 표 읽기 45초)
            playBeepAudio(587, 600); // 종료음
            if (intervalRef.current) clearInterval(intervalRef.current);
            intervalRef.current = null;
            setIsRunning(false);
            setStage('ended');
            setRemaining(0);
          }
        } else if (currentStage === 'response') {
          playBeepAudio(587, 600); // 종료음
          if (intervalRef.current) clearInterval(intervalRef.current);
          intervalRef.current = null;
          setIsRunning(false);
          setStage('ended');
          setRemaining(0);
        }
      } else {
        setRemaining(currentRemaining);
      }
    }, 1000);
  };

  const resetTimer = () => {
    if (intervalRef.current) clearInterval(intervalRef.current);
    intervalRef.current = null;
    setIsRunning(false);
    setStage('standby');
    setRemaining(prepTime > 0 ? prepTime : responseTime);
  };

  const initialBadge = defaultBadge || label || (responseTime === 0 ? '표 읽기 대기 중' : '타이머 대기 중');

  return (
    <div className={`cbt-timer-card ${className || ''}`} data-timer-id={timerId}>
      <div className="timer-top-line grid grid-cols-[1fr_auto_1fr] items-center gap-2 w-full">
        {/* 1. 상태 뱃지 (좌측 열) */}
        <div className="justify-self-start flex items-center min-w-0">
          {stage === 'prep' && (
            <div className="timer-stage-badge prep whitespace-nowrap">
              <span className="voice-dot" />
              준비 시간
            </div>
          )}
          {stage === 'response' && (
            <div className="timer-stage-badge response whitespace-nowrap">
              <span className="voice-dot" />
              답변 시간
            </div>
          )}
          {stage === 'ended' && (
            <div className="timer-stage-badge standby whitespace-nowrap">
              {responseTime === 0 ? '표 읽기 종료' : '답변 종료'}
            </div>
          )}
          {stage === 'standby' && (
            <div className="timer-stage-badge standby whitespace-nowrap">
              {initialBadge}
            </div>
          )}
        </div>

        {/* 2. 디지털 시계 (중앙 열: 100% 카드 정중앙 완벽 정렬) */}
        <div className="timer-digital-display justify-self-center text-center font-mono select-none">
          {String(Math.floor(remaining / 60)).padStart(2, '0')}:
          {String(remaining % 60).padStart(2, '0')}
        </div>

        {/* 3. 컨트롤 버튼 (우측 열: 시작/일시정지 토글 + 상시 노출 초기화 버튼) */}
        <div className="timer-btn-actions justify-self-end flex items-center gap-1.5 shrink-0">
          <button
            type="button"
            className="btn-timer-ctrl"
            onClick={toggleTimer}
            title={isRunning ? '일시정지' : stage === 'ended' ? '다시 시작' : '시작'}
            aria-label="타이머 시작/일시정지"
          >
            {isRunning ? '⏸' : stage === 'ended' ? '↺' : '▶'}
          </button>
          <button
            type="button"
            className="btn-timer-ctrl"
            onClick={resetTimer}
            title="초기화"
            aria-label="타이머 초기화"
          >
            ↺
          </button>
        </div>
      </div>
    </div>
  );
};

const CbtSubTimer = CbtTimerCard;

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

  // 만능문장 187 & 빈출 단어장 모달 상태
  const [isVocabModalOpen, setIsVocabModalOpen] = useState<boolean>(false);
  const [modalMainMode, setModalMainMode] = useState<ModalMainMode>('magic');
  const [modalPartFilter, setModalPartFilter] = useState<string>('2');
  const [modalSearch, setModalSearch] = useState<string>('');

  const [bookmarkedMagicIds, setBookmarkedMagicIds] = useState<Record<string, boolean>>(() => {
    try {
      const legacy = JSON.parse(localStorage.getItem('toeic_memorized_187') || '{}');
      return JSON.parse(localStorage.getItem('toeic_saved_magic_sentences') || JSON.stringify(legacy));
    } catch {
      return {};
    }
  });

  const [bookmarkedVocabIds, setBookmarkedVocabIds] = useState<Record<string, boolean>>(() => {
    try {
      return JSON.parse(localStorage.getItem('toeic_saved_vocab_words') || '{}');
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

  const speakMagicItem = (id: string, rate: number = 1.0) => {
    const item = magicData.items.find(it => it.id === id);
    if (item && item.en) {
      speakText(item.en, rate, `magic-${id}-${rate}`);
    }
  };

  const speakVocabItem = (id: string, rate: number = 1.0) => {
    const item = vocabData.items.find(it => it.id === id);
    if (item && item.word) {
      speakText(item.word, rate, `vocab-${id}-${rate}`);
    }
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

  // 2. 칸 선택 핸들러 (autoPlay=true면 클릭 시 즉시 1.0x 원어민 음성 재생)
  const handleSelectSpeech = (id: string, text: string, autoPlay: boolean = true) => {
    setSelectedItemId(id);
    setSelectedSpeechText(text);
    if (autoPlay && text) {
      speakText(text, 1.0, `select-${id}-1`);
    }
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

  // 문제나 파트 전환 시 기본 발음 항목 자동 선택
  useEffect(() => {
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

  const renderCbtTimerBlock = (label?: string) => (
    <CbtTimerCard
      key={`main-${activePart}-${selectedIndex}`}
      prepTime={targetPrepTime}
      responseTime={targetRespTime}
      label={label}
      defaultBadge={label || '타이머 대기 중'}
      timerId={`main-${activePart}-${selectedIndex}`}
    />
  );

  const handleTabChange = (part: ActivePart) => {
    stopSpeech();
    setActivePart(part);
    setSelectedIndex(0);
    setIsAnswerOpen(false);
    setP4AnswerOpenMap({});
    setP4QuestionVisibleMap({});
  };

  const PARTS_ORDER: ActivePart[] = ['part1', 'part2', 'part3', 'part4', 'part5'];

  const getPartCount = (part: ActivePart): number => {
    if (part === 'part1') return masterData.part1.length;
    if (part === 'part2') return masterData.part2.length;
    if (part === 'part3') {
      if (part3TypeFilter === 'ALL') return masterData.part3.length;
      return masterData.part3.filter(q => q.typeId === part3TypeFilter).length;
    }
    if (part === 'part4') {
      if (part4TableTypeFilter === 'ALL') return masterData.part4.length;
      return masterData.part4.filter(s => s.tableTypeId === part4TableTypeFilter).length;
    }
    if (part === 'part5') return masterData.part5.length;
    return 0;
  };

  const handleNext = () => {
    stopSpeech();
    setIsAnswerOpen(false);
    setP4AnswerOpenMap({});
    setP4QuestionVisibleMap({});

    if (selectedIndex < totalItemsCount - 1) {
      setSelectedIndex(selectedIndex + 1);
    } else {
      const pIdx = PARTS_ORDER.indexOf(activePart);
      if (pIdx < PARTS_ORDER.length - 1) {
        const nextPart = PARTS_ORDER[pIdx + 1];
        setActivePart(nextPart);
        setSelectedIndex(0);
      }
    }
  };

  const handlePrev = () => {
    stopSpeech();
    setIsAnswerOpen(false);
    setP4AnswerOpenMap({});
    setP4QuestionVisibleMap({});

    if (selectedIndex > 0) {
      setSelectedIndex(selectedIndex - 1);
    } else {
      const pIdx = PARTS_ORDER.indexOf(activePart);
      if (pIdx > 0) {
        const prevPart = PARTS_ORDER[pIdx - 1];
        const prevCount = getPartCount(prevPart);
        setActivePart(prevPart);
        setSelectedIndex(Math.max(0, prevCount - 1));
      }
    }
  };

  const toggleBookmark = (id: string, type: 'magic' | 'vocab') => {
    if (type === 'magic') {
      setBookmarkedMagicIds(prev => {
        const next = { ...prev };
        if (next[id]) delete next[id];
        else next[id] = true;
        localStorage.setItem('toeic_saved_magic_sentences', JSON.stringify(next));
        return next;
      });
    } else {
      setBookmarkedVocabIds(prev => {
        const next = { ...prev };
        if (next[id]) delete next[id];
        else next[id] = true;
        localStorage.setItem('toeic_saved_vocab_words', JSON.stringify(next));
        return next;
      });
    }
  };

  const filteredMagicItems = useMemo(() => {
    const q = modalSearch.trim().toLowerCase();
    return magicData.items.filter(item => {
      if (modalPartFilter === 'SAVED') {
        if (!bookmarkedMagicIds[item.id]) return false;
      } else if (modalPartFilter !== 'ALL' && String(item.part) !== modalPartFilter) {
        return false;
      }
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
  }, [modalPartFilter, modalSearch, bookmarkedMagicIds]);

  const filteredVocabItems = useMemo(() => {
    const q = modalSearch.trim().toLowerCase();
    return vocabData.items.filter(item => {
      if (modalPartFilter === 'SAVED') {
        if (!bookmarkedVocabIds[item.id]) return false;
      } else if (modalPartFilter !== 'ALL' && String(item.part) !== modalPartFilter) {
        return false;
      }
      if (q) {
        return (
          item.word.toLowerCase().includes(q) ||
          item.meaning.toLowerCase().includes(q) ||
          (item.ipa || '').toLowerCase().includes(q) ||
          item.category.toLowerCase().includes(q) ||
          item.id.toLowerCase().includes(q) ||
          (item.collocation || '').toLowerCase().includes(q) ||
          (item.example || '').toLowerCase().includes(q) ||
          (item.exampleKo || '').toLowerCase().includes(q) ||
          (item.tip || '').toLowerCase().includes(q)
        );
      }
      return true;
    });
  }, [modalPartFilter, modalSearch, bookmarkedVocabIds]);

  const savedMagicCount = Object.keys(bookmarkedMagicIds).length;
  const savedVocabCount = Object.keys(bookmarkedVocabIds).length;
  const totalItemsCount = activePart === 'part4' ? activeP4Sets.length : activeQuestions.length;
  const isFirstOfAll = activePart === 'part1' && selectedIndex === 0;
  const isLastOfAll = activePart === 'part5' && selectedIndex >= totalItemsCount - 1;
  const totalP4Questions = useMemo(() => {
    return masterData.part4.reduce((sum, s) => sum + s.questions.length, 0);
  }, []);

  return (
    <div className={`min-h-screen transition-colors duration-200 ${isDarkMode ? 'dark bg-[#0E0E11] text-[#F5F5F7]' : 'bg-[#EEF2F6] text-[#1D1D1F]'} font-sans antialiased flex flex-col items-center`}>
      {/* 5. 컴퓨터 & 태블릿에서도 모바일 화면 레이아웃으로 고정하는 앱 셸 */}
      <div className={`w-full max-w-[480px] min-h-screen ${isDarkMode ? 'bg-[#000000] border-x border-white/10 shadow-2xl' : 'bg-gradient-to-b from-white via-[#F5F5F7] to-[#EBEBF0] shadow-xl'} relative flex flex-col pb-48`}>
        {/* iOS 리퀴드 글래스 헤더 */}
        <header className="sticky top-0 z-40 bg-white/80 dark:bg-[#141416]/85 backdrop-blur-2xl border-b border-black/5 dark:border-white/10 shadow-sm transition-all">
          <div className="w-full px-3.5 py-3 flex items-center justify-between gap-2">
            <div className="flex items-center gap-2 min-w-0">
              <h1 className="text-sm sm:text-base font-extrabold tracking-tight text-[#1D1D1F] dark:text-[#F5F5F7] truncate">
                토익스피킹 기출 마스터
              </h1>
            </div>

          <div className="flex items-center gap-2 shrink-0">
            {/* 만능문장 187 & 빈출 단어장 모달 버튼 (이모티콘 없이 깔끔한 캡슐) */}
            <button
              type="button"
              onClick={() => setIsVocabModalOpen(true)}
              className="inline-flex items-center px-3 py-1.5 rounded-full text-xs font-bold bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20 dark:border-[#0A84FF]/30 hover:bg-[#0071E3] hover:text-white dark:hover:bg-[#0A84FF] dark:hover:text-white transition-all shadow-xs whitespace-nowrap"
            >
              <span>만능문장 & 단어장</span>
            </button>

            {/* 5. 다크모드 버튼 (제일 오른쪽 상단에 위치) */}
            <button
              type="button"
              onClick={toggleDarkMode}
              className="w-9 h-9 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl bg-[#F0F4F8] dark:bg-white/10 hover:bg-[#E4ECF4] dark:hover:bg-white/15 border border-[#0071E3]/15 dark:border-white/10 flex items-center justify-center text-[#1E293B] dark:text-[#FFD60A] transition-all duration-200 hover:scale-105 active:scale-95 shadow-xs shrink-0"
              title={isDarkMode ? '라이트 모드로 전환' : '다크 모드로 전환'}
              aria-label="다크 모드 전환"
            >
              {isDarkMode ? (
                <svg
                  className="w-4 h-4 sm:w-5 sm:h-5 transition-transform duration-300"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <circle cx="12" cy="12" r="5" />
                  <line x1="12" y1="1" x2="12" y2="3" />
                  <line x1="12" y1="21" x2="12" y2="23" />
                  <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" />
                  <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" />
                  <line x1="1" y1="12" x2="3" y2="12" />
                  <line x1="21" y1="12" x2="23" y2="12" />
                  <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" />
                  <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" />
                </svg>
              ) : (
                <svg
                  className="w-4 h-4 sm:w-5 sm:h-5 transition-transform duration-300"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
                </svg>
              )}
            </button>
          </div>
        </div>

        {/* 세그먼트 컨트롤 탭 (Part 1~5) */}
        <div className="max-w-6xl mx-auto px-2 sm:px-4 pb-2.5 sm:pb-3">
          <div className="flex p-1 bg-black/5 dark:bg-white/10 rounded-full border border-black/5 dark:border-white/10 gap-1 overflow-x-auto no-scrollbar">
            {[
              { id: 'part1' as ActivePart, label: 'Part 1', count: String(masterData.part1.length) },
              { id: 'part2' as ActivePart, label: 'Part 2', count: String(masterData.part2.length) },
              { id: 'part3' as ActivePart, label: 'Part 3', count: String(masterData.part3.length) },
              { id: 'part4' as ActivePart, label: 'Part 4', count: String(totalP4Questions) },
              { id: 'part5' as ActivePart, label: 'Part 5', count: String(masterData.part5.length) }
            ].map(tab => {
              const isActive = activePart === tab.id;
              return (
                <button
                  key={tab.id}
                  type="button"
                  onClick={() => handleTabChange(tab.id)}
                  className={`flex-1 min-w-[58px] sm:min-w-[80px] py-1.5 sm:py-2 px-2 sm:px-3 rounded-full text-xs sm:text-sm font-semibold flex items-center justify-center transition-all whitespace-nowrap ${
                    isActive
                      ? 'bg-white dark:bg-white/20 text-[#1D1D1F] dark:text-white shadow-sm font-bold'
                      : 'text-[#6E6E73] dark:text-[#8E8E93] hover:text-[#1D1D1F] dark:hover:text-white'
                  }`}
                >
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </div>
        </div>
      </header>

      {/* 메인 콘텐츠 영역 (모바일 고정 레이아웃) */}
      <main className="w-full max-w-[480px] mx-auto px-3 py-3">
        {/* Part 3 유형 세그먼트 탭 바 */}
        {activePart === 'part3' && (
          <div className="flex p-1 mb-6 bg-black/5 dark:bg-white/10 rounded-full border border-black/5 dark:border-white/10 gap-1 overflow-x-auto no-scrollbar">
            {masterData.part3Types.map(t => {
              const isSelected = part3TypeFilter === t.id;
              return (
                <button
                  key={t.id}
                  type="button"
                  role="tab"
                  onClick={() => {
                    stopSpeech();
                    setPart3TypeFilter(t.id);
                    setSelectedIndex(0);
                    setIsAnswerOpen(false);
                  }}
                  className={`flex-1 min-w-max py-2 px-3.5 rounded-full text-xs sm:text-sm font-semibold flex items-center justify-center transition-all whitespace-nowrap ${
                    isSelected
                      ? 'bg-white dark:bg-[#0A84FF] text-[#0071E3] dark:text-white shadow-sm font-bold'
                      : 'text-[#6E6E73] dark:text-[#AEAEB2] hover:text-[#1D1D1F] dark:hover:text-white'
                  }`}
                >
                  {t.name}
                </button>
              );
            })}
          </div>
        )}

        {/* Part 4 표 속성 세그먼트 탭 바 */}
        {activePart === 'part4' && (
          <div className="flex p-1 mb-6 bg-black/5 dark:bg-white/10 rounded-full border border-black/5 dark:border-white/10 gap-1 overflow-x-auto no-scrollbar">
            {masterData.part4TableTypes.map(t => {
              const isSelected = part4TableTypeFilter === t.id;
              return (
                <button
                  key={t.id}
                  type="button"
                  role="tab"
                  onClick={() => {
                    stopSpeech();
                    setPart4TableTypeFilter(t.id);
                    setSelectedIndex(0);
                    setP4AnswerOpenMap({});
                    setP4QuestionVisibleMap({});
                  }}
                  className={`flex-1 min-w-max py-2 px-3.5 rounded-full text-xs sm:text-sm font-semibold flex items-center justify-center transition-all whitespace-nowrap ${
                    isSelected
                      ? 'bg-white dark:bg-[#0A84FF] text-[#0071E3] dark:text-white shadow-sm font-bold'
                      : 'text-[#6E6E73] dark:text-[#AEAEB2] hover:text-[#1D1D1F] dark:hover:text-white'
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
                  <span className="text-xs font-bold px-2.5 py-0.5 rounded-full bg-[#1D1D1F] dark:bg-white text-white dark:text-[#1D1D1F]">
                    Q{selectedIndex + 1}
                  </span>
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93]">
                    준비 45초 · 답변 45초
                  </span>
                </div>
                <h2 className="text-base sm:text-lg font-bold tracking-tight text-[#1D1D1F] dark:text-white truncate">
                  {cleanEnglishTopic(currentStandardQ.topic)}
                </h2>
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
                  <p className="text-lg sm:text-xl font-medium text-[#1D1D1F] dark:text-white leading-relaxed">
                    {fullPassage}
                  </p>
                </div>
              );
            })()}

            {/* 5. 실제 CBT 타이머 (전체 지문 바로 밑에 배치) */}
            <div className="mb-7">
              {renderCbtTimerBlock('타이머 대기 중')}
            </div>

            {/* 문장별 끊어 읽기 (클릭 시 발음 선택) */}
            <div>
              <h3 className="text-base font-bold text-[#1D1D1F] dark:text-white mb-3">
                문장별 끊어 읽기
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
                핵심 발음 어휘
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
              <div className="mt-6 p-4 rounded-2xl bg-[#34C759]/10 border border-[#34C759]/20 text-sm text-[#166534] dark:text-[#4ADE80] flex flex-col gap-1.5">
                <div className="font-bold">💡 Part 1 발음 팁</div>
                <p className="leading-relaxed">{currentStandardQ.readingTips}</p>
              </div>
            )}
          </article>
        )}

        {/* Part 4 표 세트 뷰 */}
        {activePart === 'part4' && currentP4Set && (
          <article className="bg-white/80 dark:bg-[#1C1C1E]/85 backdrop-blur-2xl border border-white/80 dark:border-white/10 rounded-2xl sm:rounded-3xl p-4 sm:p-8 shadow-sm">
            <div className="flex flex-col sm:flex-row items-stretch sm:items-start justify-between gap-3 sm:gap-4 pb-4 sm:pb-5 mb-5 sm:mb-6 border-b border-black/5 dark:border-white/10">
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 mb-2 flex-wrap">
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93]">
                    표 읽기 45초
                  </span>
                </div>
                <h2 className="text-base sm:text-lg font-bold tracking-tight text-[#1D1D1F] dark:text-white truncate">
                  Set {selectedIndex + 1} — {cleanEnglishTopic(currentP4Set.topic)}
                </h2>
              </div>
            </div>

            {/* 표(Schedule Table) */}
            <div className="border border-black/10 dark:border-white/10 rounded-2xl overflow-hidden bg-white dark:bg-[#1C1C1E] mb-5 shadow-sm">
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

            {/* 일정표 밑: 준비 시간 45초 타이머 세팅 */}
            <div className="mb-5">
              <CbtSubTimer
                key={`p4-table-${selectedIndex}`}
                prepTime={45}
                responseTime={0}
                label="표 읽기 45초"
                defaultBadge="표 읽기 45초"
                timerId={`p4-table-${selectedIndex}`}
              />
            </div>

            {/* 3. 표 읽는 타이머 밑 구분선 */}
            <div className="border-t border-black/10 dark:border-white/10 my-6" />

            {/* 문제 카드 목록 (표 연계 문구 및 안내사항 삭제) */}
            <div>
              <div className="space-y-6">
                {currentP4Set.questions.map((q, qIdx) => {
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
                      {/* LC 질문 헤더 & 컨트롤 (1. Q1문항+질문듣기 통합 버튼 / 2. 질문보기 & 모범답안보기 우측 밀어서 배치) */}
                      <div className="p-3.5 sm:p-4 rounded-xl bg-black/[0.02] dark:bg-white/[0.02] border border-black/5 dark:border-white/10">
                        <div className="flex items-center justify-between gap-2 flex-wrap">
                          {/* 1. Q{qIdx + 1} 질문듣기 통합 버튼 (검은 배경 제거) */}
                          <button
                            type="button"
                            onClick={() => handleSelectSpeech(qPromptId, q.question)}
                            className={`h-[34px] px-3.5 rounded-full text-xs font-bold border inline-flex items-center justify-center transition-all shrink-0 ${
                              selectedItemId === qPromptId
                                ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3] shadow-sm'
                                : 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/20 hover:bg-[#0071E3]/20'
                            }`}
                          >
                            Q{qIdx + 1} 질문듣기
                          </button>

                          {/* 2. 질문 보기 & 모범답안 보기 우측 밀어서 배치 */}
                          <div className="flex items-center gap-1.5 shrink-0">
                            <button
                              type="button"
                              onClick={() =>
                                setP4QuestionVisibleMap(prev => ({
                                  ...prev,
                                  [q.qId]: !prev[q.qId]
                                }))
                              }
                              className={`h-[34px] px-3 sm:px-3.5 rounded-full text-xs font-bold border inline-flex items-center justify-center transition-all ${
                                isQVisible
                                  ? 'bg-black/5 dark:bg-white/10 text-[#1D1D1F] dark:text-white border-black/15'
                                  : 'bg-white dark:bg-[#2C2C2E] text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/30 hover:bg-[#0071E3]/5'
                              }`}
                            >
                              {isQVisible ? '질문 접기' : '질문 보기'}
                            </button>
                            <button
                              type="button"
                              onClick={() => {
                                setP4AnswerOpenMap(prev => ({ ...prev, [q.qId]: !prev[q.qId] }));
                              }}
                              className={`h-[34px] px-3 sm:px-3.5 rounded-full text-xs font-bold border inline-flex items-center justify-center transition-all ${
                                isAnsOpen
                                  ? 'bg-[#0071E3]/15 dark:bg-[#0A84FF]/25 text-[#0071E3] dark:text-[#64D2FF] border-[#0071E3]/40'
                                  : 'bg-white dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-white border-black/10 dark:border-white/15 hover:border-black/20'
                              }`}
                            >
                              {isAnsOpen ? '모범답안 접기' : '모범답안 보기'}
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

                      {/* 1. 파트 4 문제 타이머 (모범답안 위에 배치) */}
                      <div className="pt-1">
                        <CbtSubTimer
                          key={`p4-q-${q.qId}`}
                          prepTime={3}
                          responseTime={qIdx >= 2 ? 30 : 15}
                          label={qIdx >= 2 ? '답변 30초' : '답변 15초'}
                          defaultBadge={qIdx >= 2 ? '답변 30초' : '답변 15초'}
                          timerId={`p4-q-${q.qId}`}
                        />
                      </div>

                      {/* 모범답안 펼침 영역 */}
                      {isAnsOpen && (
                        <div className="mt-4 pt-4 border-t border-black/5 dark:border-white/10 space-y-4">
                          <div className="flex items-center justify-between gap-3 pb-2 border-b border-black/5 dark:border-white/10">
                            <span className="text-xs font-bold text-[#1D1D1F] dark:text-white">
                              문장별 모범답안
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

                          {/* 문장별 모범답안 */}
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
                              <h5 className="text-xs font-bold text-[#1D1D1F] dark:text-white">다른 만능문장 표현</h5>
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
                            <div className="p-3 rounded-xl bg-[#34C759]/10 border border-[#34C759]/20 text-xs sm:text-sm text-[#166534] dark:text-[#4ADE80] flex flex-col gap-1">
                              <div className="font-bold">💡 답변 팁</div>
                              <p className="leading-relaxed">{q.explanation}</p>
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  );
                })}
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
                  <span className="text-xs font-bold px-2.5 py-0.5 rounded-full bg-[#1D1D1F] dark:bg-white text-white dark:text-[#1D1D1F]">
                    Q{selectedIndex + 1}
                  </span>
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93]">
                    준비 {currentStandardQ.prepTime}초 · 답변 {currentStandardQ.responseTime}초
                  </span>
                </div>
                <h2 className="text-base sm:text-lg font-bold tracking-tight text-[#1D1D1F] dark:text-white truncate">
                  {cleanEnglishTopic(currentStandardQ.topic)}
                </h2>
              </div>
            </div>

            {/* Part 2 사진 (레터박스 없이 꽉 차게) */}
            {currentStandardQ.part === 2 && currentStandardQ.imageBase64 && (
              <div className="w-full rounded-2xl overflow-hidden mb-6 border border-black/10 dark:border-white/10 bg-black/5 shadow-md flex items-center justify-center max-h-[320px] sm:max-h-[540px]">
                <img
                  src={currentStandardQ.imageBase64}
                  alt={cleanEnglishTopic(currentStandardQ.topic)}
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
                  <p className="text-base sm:text-lg font-bold text-[#1D1D1F] dark:text-white">
                    {currentStandardQ.question}
                  </p>
                </div>
              );
            })()}

            {/* 5. CBT 타이머 (문제/질문 바로 밑에 배치) */}
            <div className="mb-6">
              {renderCbtTimerBlock()}
            </div>

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
                {isAnswerOpen ? '모범답안 접기' : '모범답안 보기'}
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
                        문장별 모범답안
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

                  {/* 2. 쓰인 만능문장 (적용된 만능문장 ➔ 다른 만능문장 표현으로 변경, 안내문구 제거) */}
                  {currentStandardQ.magicSentences && currentStandardQ.magicSentences.length > 0 && (
                    <div>
                      <h3 className="text-base font-bold text-[#1D1D1F] dark:text-white mb-3">
                        다른 만능문장 표현
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
                      핵심 어휘
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

                  {/* 4. 고득점 해설 전략: 밑으로 줄 바꿔서 내용 적기 */}
                  {currentStandardQ.explanation && (
                    <div className="p-4 rounded-2xl bg-[#34C759]/10 border border-[#34C759]/20 text-sm text-[#166534] dark:text-[#4ADE80] flex flex-col gap-1.5">
                      <div className="font-bold">💡 고득점 해설 전략</div>
                      <p className="leading-relaxed">{currentStandardQ.explanation}</p>
                    </div>
                  )}
                </div>
              );
            })()}
          </article>
        )}
      </main>

      {/* 하단 중앙 플로팅 바 (양옆: 이전/다음 화살표, 가운데: 문항목록 | 정지 | 1.0x | 0.75x) */}
      <aside className="fixed bottom-[calc(68px+env(safe-area-inset-bottom,16px))] sm:bottom-[84px] left-1/2 -translate-x-1/2 z-40 bg-white/95 dark:bg-[#1C1C1E]/95 backdrop-blur-2xl border border-white/90 dark:border-white/15 shadow-2xl rounded-full px-2 sm:px-3.5 py-1.5 sm:py-2 flex items-center justify-between sm:justify-center gap-1 sm:gap-2 w-auto max-w-[calc(100%-8px)]">
        {/* 1. 이전 문항 버튼 (양옆 배치: 맨 왼쪽) */}
        <button
          type="button"
          disabled={isFirstOfAll}
          onClick={handlePrev}
          className="w-[34px] h-[34px] sm:w-10 sm:h-10 rounded-full text-[#1D1D1F] dark:text-[#F5F5F7] hover:bg-black/5 dark:hover:bg-white/10 disabled:opacity-25 transition-all flex items-center justify-center shrink-0 cursor-pointer"
          title="이전 문항"
          aria-label="이전 문항"
        >
          <svg className="w-4 h-4 sm:w-5 sm:h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
        </button>

        {/* 2. 가운데 영역: 문항 목록 햄버거 버튼 */}
        <button
          type="button"
          onClick={() => setIsDrawerOpen(true)}
          className="w-[34px] h-[34px] sm:w-10 sm:h-10 rounded-full text-[#1D1D1F] dark:text-[#F5F5F7] bg-black/5 dark:bg-white/10 hover:bg-black/10 dark:hover:bg-white/15 transition-all flex items-center justify-center shrink-0 cursor-pointer"
          title="문항 목록"
          aria-label="문항 목록 열기"
        >
          <svg className="w-4 h-4 sm:w-5 sm:h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>

        {/* 3. 정지 버튼 */}
        <button
          type="button"
          onClick={stopSpeech}
          className={`w-[34px] h-[34px] sm:w-10 sm:h-10 rounded-full border transition-all flex items-center justify-center shrink-0 cursor-pointer ${
            playingKey
              ? 'bg-[#FF3B30] text-white border-[#FF3B30] shadow-md animate-pulse'
              : 'bg-[#FF3B30]/10 text-[#FF3B30] border-[#FF3B30]/25 hover:bg-[#FF3B30]/20'
          }`}
          title="발음 재생 정지"
          aria-label="발음 정지"
        >
          <svg className="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="currentColor">
            <rect x="6" y="5" width="4" height="14" rx="1.5"></rect>
            <rect x="14" y="5" width="4" height="14" rx="1.5"></rect>
          </svg>
        </button>

        {/* 4. 배속 토글 버튼 (1.0x, 0.75x) */}
        <button
          type="button"
          onClick={() => playSelectedRate(1.0)}
          className={`h-[34px] sm:h-10 min-w-[36px] sm:min-w-[48px] px-2 sm:px-3.5 inline-flex items-center justify-center rounded-full text-xs sm:text-sm font-bold border transition-all shrink-0 cursor-pointer ${
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
          className={`h-[34px] sm:h-10 min-w-[40px] sm:min-w-[48px] px-2 sm:px-3.5 inline-flex items-center justify-center rounded-full text-xs sm:text-sm font-bold border transition-all shrink-0 cursor-pointer ${
            playingKey === 'selected-0.75'
              ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3] shadow-md shadow-blue-500/30'
              : 'bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border-[#0071E3]/20 hover:bg-[#0071E3]/20'
          }`}
          title="원어민 Daniel 0.75x 느린 발음"
        >
          0.75x
        </button>

        {/* 5. 다음 문항 버튼 (양옆 배치: 맨 오른쪽) */}
        <button
          type="button"
          disabled={isLastOfAll}
          onClick={handleNext}
          className="w-[34px] h-[34px] sm:w-10 sm:h-10 rounded-full text-[#1D1D1F] dark:text-[#F5F5F7] hover:bg-black/5 dark:hover:bg-white/10 disabled:opacity-25 transition-all flex items-center justify-center shrink-0 cursor-pointer"
          title="다음 문항"
          aria-label="다음 문항"
        >
          <svg className="w-4 h-4 sm:w-5 sm:h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>
      </aside>
      </div>{/* /.mobile-app-shell */}

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
                        <strong className="text-xs text-[#1D1D1F] dark:text-white">Set {idx + 1}</strong>
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
                        <strong className="text-xs text-[#1D1D1F] dark:text-white">Q{idx + 1}</strong>
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

      {/* 만능문장 187 & 빈출 단어장 리퀴드 글래스 모달 */}
      {isVocabModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4">
          <div
            className="fixed inset-0 bg-black/40 backdrop-blur-md transition-opacity"
            onClick={() => setIsVocabModalOpen(false)}
          ></div>
          <div className="relative w-full max-w-[480px] h-[92vh] sm:h-[88vh] bg-white/95 dark:bg-[#1C1C1E]/95 backdrop-blur-3xl border border-white/80 dark:border-white/15 rounded-2xl sm:rounded-3xl shadow-2xl flex flex-col overflow-hidden z-10 animate-in zoom-in-95 duration-200">
            {/* 1. 모달 헤더 (알약 모드 토글 중앙 정렬 + iOS 리퀴드 글래스 X + 전체 너비 검색창) */}
            <div className="p-3.5 sm:p-5 border-b border-black/5 dark:border-white/10 flex flex-col gap-3 bg-white/70 dark:bg-[#1C1C1E]/70 backdrop-blur-2xl">
              {/* 1단: 가운데 정렬된 알약 토글 + 우측 리퀴드 글래스 X 닫기 버튼 */}
              <div className="relative flex items-center justify-center w-full min-h-[40px]">
                {/* 6. 중앙 정렬 알약 모드 토글 */}
                <div className="inline-flex p-1 bg-black/5 dark:bg-white/10 rounded-full border border-black/5 dark:border-white/10 gap-1 backdrop-blur-md">
                  <button
                    type="button"
                    onClick={() => {
                      setModalMainMode('magic');
                      setModalPartFilter('2');
                    }}
                    className={`py-1 sm:py-1.5 px-3 sm:px-4 rounded-full text-xs font-semibold transition-all whitespace-nowrap ${
                      modalMainMode === 'magic'
                        ? 'bg-white dark:bg-[#0A84FF] text-[#0071E3] dark:text-white shadow-xs font-bold'
                        : 'text-[#6E6E73] dark:text-[#8E8E93] hover:text-[#1D1D1F] dark:hover:text-white'
                    }`}
                  >
                    <span>만능문장 187</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setModalMainMode('vocab');
                      setModalPartFilter('1');
                    }}
                    className={`py-1 sm:py-1.5 px-3 sm:px-4 rounded-full text-xs font-semibold transition-all whitespace-nowrap ${
                      modalMainMode === 'vocab'
                        ? 'bg-white dark:bg-[#0A84FF] text-[#0071E3] dark:text-white shadow-xs font-bold'
                        : 'text-[#6E6E73] dark:text-[#8E8E93] hover:text-[#1D1D1F] dark:hover:text-white'
                    }`}
                  >
                    <span>빈출 단어장 120</span>
                  </button>
                </div>

                {/* 우측 고정 리퀴드 글래스 닫기(X) 버튼 */}
                <button
                  type="button"
                  onClick={() => setIsVocabModalOpen(false)}
                  className="absolute right-0 top-1/2 -translate-y-1/2 w-8 h-8 sm:w-9 sm:h-9 rounded-full bg-[rgba(118,118,128,0.14)] dark:bg-[rgba(118,118,128,0.28)] backdrop-blur-xl border border-white/60 dark:border-white/15 text-[#3C3C43] dark:text-[#EBEBF5] hover:bg-[rgba(118,118,128,0.24)] dark:hover:bg-[rgba(118,118,128,0.42)] flex items-center justify-center transition-all hover:scale-105 active:scale-95 shadow-sm"
                  aria-label="닫기"
                >
                  <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round">
                    <line x1="17" y1="7" x2="7" y2="17" />
                    <line x1="7" y1="7" x2="17" y2="17" />
                  </svg>
                </button>
              </div>

              {/* 2단: 전체 너비 검색창 */}
              <div className="relative w-full">
                <svg className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-[#8E8E93]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="11" cy="11" r="8" />
                  <line x1="21" y1="21" x2="16.65" y2="16.65" />
                </svg>
                <input
                  type="search"
                  value={modalSearch}
                  onChange={e => setModalSearch(e.target.value)}
                  placeholder="단어, 표현, 한국어 뜻 검색..."
                  className="w-full pl-10 pr-4 py-2 rounded-full border border-black/10 dark:border-white/15 text-xs sm:text-sm bg-white dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-white outline-none focus:border-[#0071E3] dark:focus:border-[#0A84FF] transition-all"
                />
              </div>
            </div>

            {/* 7. 파트 필터 세그먼트 컨트롤 탭: 좌측 북마크 버튼 분리 + 전체/저장됨 탭 제거 + 가운데 정렬(모바일 짤림 방지) */}
            <div className="px-3 sm:px-5 py-2.5 sm:py-3 border-b border-black/5 dark:border-white/10 bg-black/[0.02] dark:bg-white/[0.02] overflow-x-auto no-scrollbar">
              <div className="flex items-center justify-start sm:justify-center gap-2 min-w-max mx-auto px-1">
                {/* 7. 좌측 북마크 전용 버튼 */}
                <button
                  type="button"
                  onClick={() => {
                    if (modalPartFilter === 'SAVED') {
                      setModalPartFilter(modalMainMode === 'magic' ? '2' : '1');
                    } else {
                      setModalPartFilter('SAVED');
                    }
                  }}
                  className={`h-8 sm:h-9 px-2.5 sm:px-3 rounded-full text-xs font-bold border inline-flex items-center justify-center gap-1.5 transition-all shrink-0 ${
                    modalPartFilter === 'SAVED'
                      ? 'bg-[#0071E3] dark:bg-[#0A84FF] text-white border-[#0071E3] shadow-xs'
                      : 'bg-white dark:bg-[#2C2C2E] text-[#1D1D1F] dark:text-white border-black/10 dark:border-white/15 hover:border-black/20'
                  }`}
                  title="저장된 항목 보기"
                >
                  <svg
                    className="w-3.5 h-3.5"
                    viewBox="0 0 24 24"
                    fill={modalPartFilter === 'SAVED' ? 'currentColor' : 'none'}
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
                  </svg>
                  <span>저장됨</span>
                  <span
                    className={`text-[10px] px-1.5 py-0.5 rounded-full ${
                      modalPartFilter === 'SAVED'
                        ? 'bg-white/25 text-white'
                        : 'bg-black/5 dark:bg-white/10 text-[#6E6E73] dark:text-[#8E8E93]'
                    }`}
                  >
                    {modalMainMode === 'magic' ? savedMagicCount : savedVocabCount}
                  </span>
                </button>

                {/* 구분선 */}
                <div className="h-5 w-px bg-black/10 dark:bg-white/10 shrink-0" />

                {/* 파트 탭 목록 */}
                <div className="flex p-1 bg-black/5 dark:bg-white/10 rounded-full border border-black/5 dark:border-white/10 gap-1 shrink-0">
                  {(modalMainMode === 'magic'
                    ? [
                        { id: '2', name: 'Part 2', count: 49 },
                        { id: '3', name: 'Part 3', count: 47 },
                        { id: '4', name: 'Part 4', count: 38 },
                        { id: '5', name: 'Part 5', count: 53 }
                      ]
                    : [
                        { id: '1', name: 'Part 1', count: 24 },
                        { id: '2', name: 'Part 2', count: 24 },
                        { id: '3', name: 'Part 3', count: 24 },
                        { id: '4', name: 'Part 4', count: 24 },
                        { id: '5', name: 'Part 5', count: 24 }
                      ]
                  ).map(f => {
                    const isActive = modalPartFilter === f.id;
                    return (
                      <button
                        key={f.id}
                        type="button"
                        role="tab"
                        onClick={() => setModalPartFilter(f.id)}
                        className={`flex-1 min-w-max py-1.5 px-2.5 sm:px-3 rounded-full text-xs font-semibold flex items-center justify-center gap-1.5 transition-all whitespace-nowrap ${
                          isActive
                            ? 'bg-white dark:bg-[#0A84FF] text-[#0071E3] dark:text-white shadow-sm font-bold'
                            : 'text-[#6E6E73] dark:text-[#8E8E93] hover:text-[#1D1D1F] dark:hover:text-white'
                        }`}
                      >
                        <span>{f.name}</span>
                      </button>
                    );
                  })}
                </div>
              </div>
            </div>

            {/* 카드 목록 영역 */}
            <div className="flex-1 overflow-y-auto p-3 sm:p-5">
              {modalMainMode === 'magic' ? (
                /* 만능문장 카드 그리드 */
                filteredMagicItems.length === 0 ? (
                  <div className="text-center py-16 text-xs sm:text-sm text-[#86868B] dark:text-[#8E8E93]">
                    {modalPartFilter === 'SAVED'
                      ? '저장된 만능문장이 없습니다. 우측 상단 책갈피 아이콘을 눌러 저장해보세요.'
                      : '검색 결과가 없습니다.'}
                  </div>
                ) : (
                  <div className="grid grid-cols-1 gap-3 sm:gap-3.5">
                    {filteredMagicItems.map(item => {
                      const isSaved = !!bookmarkedMagicIds[item.id];
                      return (
                        <div
                          key={item.id}
                          className="p-4 sm:p-4.5 rounded-2xl border flex flex-col justify-between gap-2.5 transition-all bg-white/90 dark:bg-[#242426] border-black/5 dark:border-white/10"
                        >
                          {/* 본문 문장과 북마크 버튼을 같은 줄(같은 선상)에 배치 */}
                          <div className="flex items-start justify-between gap-2.5 w-full">
                            <div className="flex items-start gap-2.5 flex-1 min-w-0">
                              <button
                                type="button"
                                onClick={() => speakMagicItem(item.id, 1.0)}
                                className="w-7 h-7 sm:w-8 sm:h-8 rounded-full shrink-0 flex items-center justify-center bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20 hover:bg-[#0071E3]/25 active:scale-95 transition-all mt-0.5"
                                title="발음 듣기"
                                aria-label="발음 듣기"
                              >
                                <svg
                                  className="w-3.5 h-3.5 sm:w-4 sm:h-4"
                                  viewBox="0 0 24 24"
                                  fill="none"
                                  stroke="currentColor"
                                  strokeWidth="2"
                                  strokeLinecap="round"
                                  strokeLinejoin="round"
                                >
                                  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" />
                                  <path d="M15.54 8.46a5 5 0 0 1 0 7.07" />
                                </svg>
                              </button>
                              <div className="flex-1 min-w-0">
                                <p className="text-base sm:text-[16.5px] font-bold text-[#1D1D1F] dark:text-white leading-snug">
                                  {item.en}
                                </p>
                                <p className="text-xs sm:text-sm text-[#6E6E73] dark:text-[#8E8E93] mt-1.5 leading-relaxed">
                                  {item.ko}
                                </p>
                              </div>
                            </div>

                            {/* 우측 상단 북마크 저장 버튼 (스피커/문장과 같은 선상) */}
                            <button
                              type="button"
                              onClick={() => toggleBookmark(item.id, 'magic')}
                              className={`w-7 h-7 sm:w-8 sm:h-8 rounded-full shrink-0 flex items-center justify-center transition-all ${
                                isSaved
                                  ? 'bg-[#0071E3]/15 dark:bg-[#0A84FF]/25 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/30 scale-105'
                                  : 'bg-black/5 dark:bg-white/10 text-[#86868B] dark:text-[#8E8E93] hover:text-[#0071E3] dark:hover:text-[#0A84FF]'
                              }`}
                              title={isSaved ? '저장 해제' : '저장'}
                              aria-label="저장"
                            >
                              <svg
                                className="w-3.5 h-3.5 sm:w-4 sm:h-4"
                                viewBox="0 0 24 24"
                                fill={isSaved ? 'currentColor' : 'none'}
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round"
                              >
                                <path d="M19 21l-7-4.5L5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
                              </svg>
                            </button>
                          </div>

                          {item.tip && (
                            <div className="mt-1 p-2 rounded-xl bg-[#FF9500]/10 dark:bg-[#FF9500]/15 border border-[#FF9500]/25 text-xs text-[#B26200] dark:text-[#FFB340]">
                              <span className="font-bold">💡 만능 팁:</span> {item.tip}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )
              ) : (
                /* 기출 빈출 단어장 그리드 (3. 인터넷 사전/단어장 프리미엄 레이아웃) */
                filteredVocabItems.length === 0 ? (
                  <div className="text-center py-16 text-xs sm:text-sm text-[#86868B] dark:text-[#8E8E93]">
                    {modalPartFilter === 'SAVED'
                      ? '저장된 단어가 없습니다. 우측 상단 책갈피 아이콘을 눌러 저장해보세요.'
                      : '검색 결과가 없습니다.'}
                  </div>
                ) : (
                  <div className="grid grid-cols-1 gap-3 sm:gap-3.5">
                    {filteredVocabItems.map(item => {
                      const isSaved = !!bookmarkedVocabIds[item.id];
                      return (
                        <div
                          key={item.id}
                          className="p-4 sm:p-4.5 rounded-2xl border flex flex-col justify-between gap-2.5 transition-all bg-white/90 dark:bg-[#242426] border-black/5 dark:border-white/10"
                        >
                          {/* 표제어/스피커와 북마크 버튼을 같은 줄(같은 선상)에 배치 */}
                          <div className="flex items-center justify-between gap-2.5 w-full">
                            <div className="flex items-center gap-2 sm:gap-2.5 flex-wrap flex-1 min-w-0">
                              <button
                                type="button"
                                onClick={() => speakVocabItem(item.id, 1.0)}
                                className="w-7 h-7 sm:w-8 sm:h-8 rounded-full shrink-0 flex items-center justify-center bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/20 hover:bg-[#0071E3]/25 active:scale-95 transition-all"
                                title="발음 듣기"
                                aria-label="발음 듣기"
                              >
                                <svg
                                  className="w-3.5 h-3.5 sm:w-4 sm:h-4"
                                  viewBox="0 0 24 24"
                                  fill="none"
                                  stroke="currentColor"
                                  strokeWidth="2"
                                  strokeLinecap="round"
                                  strokeLinejoin="round"
                                >
                                  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" />
                                  <path d="M15.54 8.46a5 5 0 0 1 0 7.07" />
                                </svg>
                              </button>
                              <h3 className="text-xl font-extrabold text-[#1D1D1F] dark:text-white tracking-tight">
                                {item.word}
                              </h3>
                              <span className="text-xs font-mono text-[#0071E3] dark:text-[#0A84FF] font-semibold">
                                {item.ipa}
                              </span>
                              <span className="text-[11px] font-bold px-1.5 py-0.5 rounded bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF]">
                                {item.pos}
                              </span>
                            </div>

                            {/* 우측 상단 북마크 저장 버튼 (단어/스피커와 같은 선상) */}
                            <button
                              type="button"
                              onClick={() => toggleBookmark(item.id, 'vocab')}
                              className={`w-7 h-7 sm:w-8 sm:h-8 rounded-full shrink-0 flex items-center justify-center transition-all ${
                                isSaved
                                  ? 'bg-[#0071E3]/15 dark:bg-[#0A84FF]/25 text-[#0071E3] dark:text-[#0A84FF] border border-[#0071E3]/30 scale-105'
                                  : 'bg-black/5 dark:bg-white/10 text-[#86868B] dark:text-[#8E8E93] hover:text-[#0071E3] dark:hover:text-[#0A84FF]'
                              }`}
                              title={isSaved ? '저장 해제' : '저장'}
                              aria-label="저장"
                            >
                              <svg
                                className="w-3.5 h-3.5 sm:w-4 sm:h-4"
                                viewBox="0 0 24 24"
                                fill={isSaved ? 'currentColor' : 'none'}
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round"
                              >
                                <path d="M19 21l-7-4.5L5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
                              </svg>
                            </button>
                          </div>

                          {/* 3. 핵심 뜻 */}
                          <p className="text-[15.5px] font-bold text-[#1D1D1F] dark:text-white mt-1 leading-snug">
                            {item.meaning}
                          </p>

                            {/* 4. 자주 쓰이는 표현 (연어구) */}
                            {item.collocation && (
                              <div className="mt-2.5 flex items-center gap-2 p-2 rounded-xl bg-[#0071E3]/5 dark:bg-[#0A84FF]/10 border border-[#0071E3]/15 dark:border-[#0A84FF]/20 text-xs">
                                <span className="font-bold text-[10.5px] px-1.5 py-0.5 rounded bg-[#0071E3]/10 dark:bg-[#0A84FF]/20 text-[#0071E3] dark:text-[#0A84FF] whitespace-nowrap">
                                  자주 쓰이는 표현
                                </span>
                                <span className="text-[#1D1D1F] dark:text-[#F5F5F7] font-bold tracking-tight">
                                  {item.collocation}
                                </span>
                              </div>
                            )}

                            {/* 5. 실전 기출 예문 */}
                            {item.example && (
                              <div className="mt-2.5 p-2.5 rounded-r-xl border-l-[3px] border-[#0071E3] dark:border-[#0A84FF] bg-black/[0.02] dark:bg-white/[0.03] text-xs">
                                <p className="text-[#1D1D1F] dark:text-[#F5F5F7] font-semibold leading-relaxed">
                                  "{item.example}"
                                </p>
                                <p className="text-[#6E6E73] dark:text-[#8E8E93] mt-1">
                                  {item.exampleKo}
                                </p>
                              </div>
                            )}

                            {/* 6. 출제 포인트 및 팁 */}
                            {item.tip && (
                              <div className="mt-2.5 p-2 rounded-xl bg-[#FF9500]/10 dark:bg-[#FF9500]/15 border border-[#FF9500]/25 text-xs text-[#B26200] dark:text-[#FFB340]">
                                <span className="font-bold">💡 기출 팁:</span> {item.tip}
                              </div>
                            )}
                        </div>
                      );
                    })}
                  </div>
                )
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ToeicSpeakingApp;
