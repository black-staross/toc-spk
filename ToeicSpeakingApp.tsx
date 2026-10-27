import React, { useState, useEffect, useMemo, useCallback } from 'react';
import {
  ToeicPart,
  ToeicQuestionDetailResponse,
  Part2QuestionResponse,
  Part3QuestionResponse,
  Part4QuestionResponse,
  QuestionQueryParams,
} from './api-types';
import { getQuestions, ApiError } from './api';
import {
  MOCK_USER_PROFILE,
  FULL_MASTER_QUESTIONS,
  MOCK_CHEAT_SHEETS,
} from './mockData';

// 백엔드 FastAPI 서버 미구동 상태에서도 전체 98개 문항을 완벽 학습할 수 있는 Fallback 데이터셋
const FALLBACK_MOCK_DATA: ToeicQuestionDetailResponse[] = FULL_MASTER_QUESTIONS;

interface ExamTimerState {
  phase: 'idle' | 'prep' | 'response' | 'finished';
  timeLeft: number;
  totalDuration: number;
  progressPercent: number;
  isRunning: boolean;
}

export const ToeicSpeakingApp: React.FC = () => {
  // ----------------------------------------------------------------------------
  // 1. 상태 관리
  // ----------------------------------------------------------------------------
  const [currentPart, setCurrentPart] = useState<ToeicPart>('part3');
  const [selectedSetId, setSelectedSetId] = useState<number | 'all'>('all');
  const [questions, setQuestions] = useState<ToeicQuestionDetailResponse[]>([]);
  const [currentIndex, setCurrentIndex] = useState<number>(0);

  // 로딩 & 에러 & 오프라인 폴백 상태
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [apiError, setApiError] = useState<ApiError | null>(null);
  const [isUsingFallback, setIsUsingFallback] = useState<boolean>(false);

  // UI 인터랙션 상태
  const [isAnswerVisible, setIsAnswerVisible] = useState<boolean>(false);
  const [isExamMode, setIsExamMode] = useState<boolean>(true);
  const [isCheatSheetOpen, setIsCheatSheetOpen] = useState<boolean>(false);
  const [modalTab, setModalTab] = useState<ToeicPart>('part3');

  // 오디오 발음 재생(TTS) 상태
  const [speakingSentenceIndex, setSpeakingSentenceIndex] = useState<number | null>(null);

  // 실전 타이머 상태
  const [timerState, setTimerState] = useState<ExamTimerState>({
    phase: 'idle',
    timeLeft: 3,
    totalDuration: 3,
    progressPercent: 0,
    isRunning: false,
  });

  // Part 4 전용 45초 표 읽기 실전 타이머 상태
  const [p4ReadingTime, setP4ReadingTime] = useState<number>(45);
  const [isP4ReadingActive, setIsP4ReadingActive] = useState<boolean>(false);

  // ----------------------------------------------------------------------------
  // 2. 실제 FastAPI 서버 데이터 로딩 로직 (fetch/axios)
  // ----------------------------------------------------------------------------
  const fetchQuestionsFromApi = useCallback(
    async (targetPart: ToeicPart, targetSetId: number | 'all') => {
      setIsLoading(true);
      setApiError(null);

      const params: QuestionQueryParams = {
        part: targetPart,
        limit: 100,
      };
      if (targetSetId !== 'all') {
        params.setId = targetSetId;
      }

      try {
        const response = await getQuestions(params);
        setQuestions(response.items);
        setCurrentIndex(0);
        setIsUsingFallback(false);
      } catch (err: unknown) {
        if (err instanceof ApiError) {
          setApiError(err);
        } else {
          setApiError(new ApiError('알 수 없는 오류가 발생했습니다.', 500));
        }
      } finally {
        setIsLoading(false);
      }
    },
    []
  );

  useEffect(() => {
    if (!isUsingFallback) {
      fetchQuestionsFromApi(currentPart, selectedSetId);
    } else {
      let filtered = FALLBACK_MOCK_DATA.filter((q) => q.part === currentPart);
      if (selectedSetId !== 'all') {
        filtered = filtered.filter((q) => q.setId === selectedSetId);
      }
      setQuestions(filtered);
      setCurrentIndex(0);
      setIsLoading(false);
    }
  }, [currentPart, selectedSetId, isUsingFallback, fetchQuestionsFromApi]);

  const handleEnableFallbackMock = () => {
    setIsUsingFallback(true);
    setApiError(null);
    setIsLoading(true);
    setTimeout(() => {
      let filtered = FALLBACK_MOCK_DATA.filter((q) => q.part === currentPart);
      if (selectedSetId !== 'all') {
        filtered = filtered.filter((q) => q.setId === selectedSetId);
      }
      setQuestions(filtered);
      setCurrentIndex(0);
      setIsLoading(false);
    }, 200);
  };

  const activeQuestion: ToeicQuestionDetailResponse | undefined = questions[currentIndex];

  const availableSetIds = useMemo(() => {
    const setSet = new Set<number>();
    const pool = isUsingFallback
      ? FALLBACK_MOCK_DATA.filter((q) => q.part === currentPart)
      : questions;
    pool.forEach((q) => setSet.add(q.setId));
    return Array.from(setSet).sort((a, b) => a - b);
  }, [questions, isUsingFallback, currentPart]);

  // ----------------------------------------------------------------------------
  // 3. Web Speech API (TTS) 로직 (Daniel 음성 지향)
  // ----------------------------------------------------------------------------
  const stopSpeech = useCallback(() => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    setSpeakingSentenceIndex(null);
  }, []);

  const speakText = useCallback(
    (text: string, rate: number = 1.0, onEndCallback?: () => void) => {
      if (!('speechSynthesis' in window)) {
        alert('현재 브라우저 환경에서 음성 합성을 지원하지 않습니다.');
        return;
      }
      stopSpeech();

      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = rate;

      const voices = window.speechSynthesis.getVoices();
      const preferred =
        voices.find((v) => v.name.toLowerCase().includes('daniel')) ||
        voices.find((v) => v.lang.startsWith('en') && (v.name.includes('Male') || v.name.includes('Eddy'))) ||
        voices.find((v) => v.lang.startsWith('en'));

      if (preferred) utterance.voice = preferred;

      utterance.onend = () => {
        setSpeakingSentenceIndex(null);
        if (onEndCallback) onEndCallback();
      };
      utterance.onerror = () => setSpeakingSentenceIndex(null);

      window.speechSynthesis.speak(utterance);
    },
    [stopSpeech]
  );

  // ----------------------------------------------------------------------------
  // 4. 문제 전환 및 실전 타이머
  // ----------------------------------------------------------------------------
  const resetTimer = useCallback(() => {
    const prep = activeQuestion?.prepTime || (currentPart === 'part2' ? 45 : 3);
    setTimerState({
      phase: 'idle',
      timeLeft: prep,
      totalDuration: prep,
      progressPercent: 0,
      isRunning: false,
    });
  }, [activeQuestion, currentPart]);

  const handlePartSwitch = (part: ToeicPart) => {
    stopSpeech();
    setCurrentPart(part);
    setSelectedSetId('all');
    setCurrentIndex(0);
    setIsAnswerVisible(false);
    resetTimer();
    setIsP4ReadingActive(false);
    setP4ReadingTime(45);
  };

  const handlePrevQuestion = () => {
    if (currentIndex > 0) {
      stopSpeech();
      setCurrentIndex((prev) => prev - 1);
      setIsAnswerVisible(false);
      resetTimer();
    }
  };

  const handleNextQuestion = () => {
    if (currentIndex < questions.length - 1) {
      stopSpeech();
      setCurrentIndex((prev) => prev + 1);
      setIsAnswerVisible(false);
      resetTimer();
    }
  };

  const startExamTimer = () => {
    if (!activeQuestion) return;
    const prepTime = activeQuestion.prepTime || (currentPart === 'part2' ? 45 : 3);
    setTimerState({
      phase: 'prep',
      timeLeft: prepTime,
      totalDuration: prepTime,
      progressPercent: 0,
      isRunning: true,
    });
  };

  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;
    if (timerState.isRunning && timerState.timeLeft > 0) {
      interval = setInterval(() => {
        setTimerState((prev) => {
          const nextTime = prev.timeLeft - 1;
          const pct = ((prev.totalDuration - nextTime) / prev.totalDuration) * 100;
          return {
            ...prev,
            timeLeft: nextTime,
            progressPercent: Math.min(pct, 100),
          };
        });
      }, 1000);
    } else if (timerState.isRunning && timerState.timeLeft <= 0) {
      if (timerState.phase === 'prep') {
        const responseTime = activeQuestion?.responseTime || (currentPart === 'part2' ? 30 : 15);
        try {
          const ctx = new (window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext)();
          const osc = ctx.createOscillator();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(880, ctx.currentTime);
          osc.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.3);
        } catch {
          // Web Audio 제한 시 무시
        }

        setTimerState({
          phase: 'response',
          timeLeft: responseTime,
          totalDuration: responseTime,
          progressPercent: 0,
          isRunning: true,
        });
      } else if (timerState.phase === 'response') {
        setTimerState((prev) => ({
          ...prev,
          phase: 'finished',
          isRunning: false,
          progressPercent: 100,
        }));
      }
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [timerState.isRunning, timerState.timeLeft, timerState.phase, activeQuestion, currentPart]);

  useEffect(() => {
    let p4Interval: NodeJS.Timeout | null = null;
    if (isP4ReadingActive && p4ReadingTime > 0) {
      p4Interval = setInterval(() => {
        setP4ReadingTime((prev) => prev - 1);
      }, 1000);
    } else if (isP4ReadingActive && p4ReadingTime <= 0) {
      setIsP4ReadingActive(false);
    }
    return () => {
      if (p4Interval) clearInterval(p4Interval);
    };
  }, [isP4ReadingActive, p4ReadingTime]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement || e.target instanceof HTMLSelectElement) return;

      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        handlePrevQuestion();
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        handleNextQuestion();
      } else if (e.code === 'Space') {
        e.preventDefault();
        setIsAnswerVisible((prev) => !prev);
      } else if (e.key === '1' && activeQuestion) {
        e.preventDefault();
        speakText(activeQuestion.question, 1.0);
      } else if (e.key === '2' && activeQuestion) {
        e.preventDefault();
        speakText(activeQuestion.question, 0.75);
      } else if (e.key === 'Escape') {
        stopSpeech();
        setIsCheatSheetOpen(false);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  });

  // [요청 3 반영] 파트 2, 3, 4 모두 정교한 문장 단위 분할 (줄바꿈 또는 마침표/물음표/느낌표 기준)
  const structuredSentences = useMemo(() => {
    if (!activeQuestion) return [];
    
    // 줄바꿈으로 먼저 나누고, 단일 긴 줄인 경우 문장 부호로 재분할
    let rawEn = activeQuestion.answer.split('\n').map(s => s.trim()).filter(s => s.length > 0);
    let rawKo = activeQuestion.answerTranslation.split('\n').map(s => s.trim()).filter(s => s.length > 0);

    if (rawEn.length === 1 && rawEn[0].includes('.')) {
      const matchEn = rawEn[0].match(/[^.!?]+[.!?]+(\s+|$)/g);
      if (matchEn && matchEn.length > 1) {
        rawEn = matchEn.map(s => s.trim());
      }
    }
    if (rawKo.length === 1 && rawKo[0].includes('.')) {
      const matchKo = rawKo[0].match(/[^.!?]+[.!?]+(\s+|$)/g);
      if (matchKo && matchKo.length > 1) {
        rawKo = matchKo.map(s => s.trim());
      }
    }

    return rawEn.map((en, idx) => ({
      index: idx + 1,
      en,
      ko: rawKo[idx] || '',
    }));
  }, [activeQuestion]);

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 via-slate-100 to-slate-200 text-slate-800 antialiased font-sans pb-16">
      {/* Ambient Blur Orbs */}
      <div className="fixed -top-24 -left-24 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl pointer-events-none -z-10" />
      <div className="fixed top-1/4 -right-24 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl pointer-events-none -z-10" />
      <div className="fixed -bottom-24 left-1/3 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none -z-10" />

      {/* Main Viewport */}
      <div className="w-full max-w-5xl mx-auto px-3.5 sm:px-6 lg:px-8 py-4 sm:py-6 lg:py-8 flex flex-col gap-5 sm:gap-6">
        
        {/* =======================================================================
            TOP BOOKMARK TABS (Part 2, Part 3, Part 4)
            ======================================================================= */}
        <nav aria-label="토익스피킹 파트 선택" className="grid grid-cols-3 gap-2 sm:gap-3 lg:gap-4">
          <button
            onClick={() => handlePartSwitch('part2')}
            className={`relative flex items-center justify-center sm:justify-start gap-2 sm:gap-3 p-3 sm:p-4 rounded-2xl border transition-all duration-300 text-left ${
              currentPart === 'part2'
                ? 'bg-white/95 border-emerald-500/60 shadow-lg shadow-emerald-500/10 ring-2 ring-emerald-500/20 translate-y-[-2px]'
                : 'bg-white/60 hover:bg-white/90 border-slate-200 hover:border-slate-300 shadow-sm opacity-80 hover:opacity-100'
            }`}
          >
            <span className="text-xl sm:text-2xl">🖼️</span>
            <div className="flex flex-col">
              <span className={`text-xs sm:text-sm font-bold tracking-tight ${currentPart === 'part2' ? 'text-emerald-700' : 'text-slate-700'}`}>
                PART 2 책갈피
              </span>
              <span className="hidden sm:inline text-xs text-slate-500 truncate">고화질 사진 묘사 (26세트)</span>
            </div>
          </button>

          <button
            onClick={() => handlePartSwitch('part3')}
            className={`relative flex items-center justify-center sm:justify-start gap-2 sm:gap-3 p-3 sm:p-4 rounded-2xl border transition-all duration-300 text-left ${
              currentPart === 'part3'
                ? 'bg-white/95 border-blue-500/60 shadow-lg shadow-blue-500/10 ring-2 ring-blue-500/20 translate-y-[-2px]'
                : 'bg-white/60 hover:bg-white/90 border-slate-200 hover:border-slate-300 shadow-sm opacity-80 hover:opacity-100'
            }`}
          >
            <span className="text-xl sm:text-2xl">🔖</span>
            <div className="flex flex-col">
              <span className={`text-xs sm:text-sm font-bold tracking-tight ${currentPart === 'part3' ? 'text-blue-700' : 'text-slate-700'}`}>
                PART 3 책갈피
              </span>
              <span className="hidden sm:inline text-xs text-slate-500 truncate">일상 질문 답하기 (48문항)</span>
            </div>
          </button>

          <button
            onClick={() => handlePartSwitch('part4')}
            className={`relative flex items-center justify-center sm:justify-start gap-2 sm:gap-3 p-3 sm:p-4 rounded-2xl border transition-all duration-300 text-left ${
              currentPart === 'part4'
                ? 'bg-white/95 border-purple-500/60 shadow-lg shadow-purple-500/10 ring-2 ring-purple-500/20 translate-y-[-2px]'
                : 'bg-white/60 hover:bg-white/90 border-slate-200 hover:border-slate-300 shadow-sm opacity-80 hover:opacity-100'
            }`}
          >
            <span className="text-xl sm:text-2xl">📑</span>
            <div className="flex flex-col">
              <span className={`text-xs sm:text-sm font-bold tracking-tight ${currentPart === 'part4' ? 'text-purple-700' : 'text-slate-700'}`}>
                PART 4 책갈피
              </span>
              <span className="hidden sm:inline text-xs text-slate-500 truncate">표/일정표 보고 답하기 (24문항)</span>
            </div>
          </button>
        </nav>

        {/* =======================================================================
            APPLE GLASS HEADER
            ======================================================================= */}
        <header className="bg-white/80 backdrop-blur-xl border border-white/80 rounded-2xl sm:rounded-3xl p-4 sm:p-6 shadow-xl shadow-slate-200/50 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <div className="flex flex-col gap-1.5">
            <div className="inline-flex items-center gap-2 bg-blue-50 border border-blue-200/60 text-blue-600 px-3 py-1 rounded-full text-xs font-semibold w-fit">
              <span className="w-2 h-2 rounded-full bg-blue-500 animate-pulse" />
              <span>Target: {MOCK_USER_PROFILE.targetScore} · 실전 마스터판 (98문항 전체)</span>
            </div>
            <h1 className="text-xl sm:text-2xl lg:text-3xl font-extrabold tracking-tight text-slate-900 flex items-center gap-2 flex-wrap">
              <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
                TOEIC Speaking
              </span>
              <span>
                {currentPart === 'part2' && 'Part 2 실전 트레이너'}
                {currentPart === 'part3' && 'Part 3 실전 트레이너'}
                {currentPart === 'part4' && 'Part 4 실전 트레이너'}
              </span>
            </h1>
            <p className="text-xs sm:text-sm text-slate-500">
              {currentPart === 'part2' && '기출 26개 고화질 실사 사진 · 45초 준비 / 30초 답변 · 문장별 개별 발음'}
              {currentPart === 'part3' && '16개 테마 48개 전 문항 · 한글해석 블라인드 · 문장별 개별 발음'}
              {currentPart === 'part4' && '8개 세트 24문항 전체 일정표 · 45초 표 읽기 · 문의자 발화상황 연계'}
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full md:w-auto">
            {/* Daniel Voice Capsule */}
            <div className="bg-white/90 border border-blue-200/80 rounded-2xl px-3.5 py-2 flex items-center justify-between sm:justify-start gap-3 shadow-sm">
              <div className="flex items-center gap-2">
                <span className="text-xl">👨‍💼</span>
                <div className="flex flex-col text-left">
                  <span className="text-xs font-bold text-slate-800">
                    전담 음성: <strong className="text-blue-600 font-mono">Daniel</strong>
                  </span>
                  <span className="text-[10px] text-slate-500">영국식 표준 발음</span>
                </div>
              </div>
              <button
                onClick={() => speakText("Hello! I am Daniel, your dedicated British voice coach.", 1.0)}
                className="text-xs font-semibold bg-blue-50 hover:bg-blue-600 hover:text-white text-blue-600 px-2.5 py-1 rounded-full transition-all border border-blue-200"
              >
                ▶️ 샘플
              </button>
            </div>

            {/* Modal & Timer Toggles */}
            <div className="flex items-center gap-2">
              <button
                onClick={() => {
                  setModalTab(currentPart);
                  setIsCheatSheetOpen(true);
                }}
                className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold bg-purple-50 hover:bg-purple-100 text-purple-700 border border-purple-200/80 transition-all active:scale-95"
              >
                <span>🐰</span>
                <span>만능문장 족보집</span>
              </button>
              <button
                onClick={() => setIsExamMode(!isExamMode)}
                className={`flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold border transition-all active:scale-95 ${
                  isExamMode
                    ? 'bg-emerald-50 text-emerald-700 border-emerald-300'
                    : 'bg-slate-100 text-slate-500 border-slate-300'
                }`}
              >
                <span>⏱️</span>
                <span>타이머: <strong>{isExamMode ? 'ON' : 'OFF'}</strong></span>
              </button>
            </div>
          </div>
        </header>

        {/* =======================================================================
            TOOLBAR
            ======================================================================= */}
        <nav aria-label="문항 제어 툴바" className="bg-white/80 backdrop-blur-xl border border-white/80 rounded-2xl p-3 sm:p-4 shadow-sm flex flex-col sm:flex-row items-center justify-between gap-3 sm:gap-4">
          <div className="flex items-center gap-2 w-full sm:w-auto">
            <label htmlFor="setFilterSelect" className="text-xs sm:text-sm font-bold text-slate-600 whitespace-nowrap">
              세트 필터:
            </label>
            <select
              id="setFilterSelect"
              value={selectedSetId}
              onChange={(e) => {
                const val = e.target.value === 'all' ? 'all' : Number(e.target.value);
                setSelectedSetId(val);
                setCurrentIndex(0);
                setIsAnswerVisible(false);
                resetTimer();
              }}
              className="flex-1 sm:w-60 bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 text-xs sm:text-sm font-semibold text-slate-700 outline-none cursor-pointer"
            >
              <option value="all">전체 세트 (총 {questions.length}문항)</option>
              {availableSetIds.map((sid) => (
                <option key={sid} value={sid}>
                  Set {sid} 문항
                </option>
              ))}
            </select>

            {isUsingFallback && (
              <span className="text-[11px] font-bold bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full border border-amber-300 whitespace-nowrap">
                오프라인 마스터 모드
              </span>
            )}
          </div>

          <div className="flex items-center gap-3 w-full sm:w-auto justify-between sm:justify-center">
            {/* Counter & Progress */}
            <div className="flex flex-col items-center gap-1 min-w-[90px]">
              <span className="text-xs sm:text-sm font-bold font-mono text-slate-700">
                {questions.length > 0 ? currentIndex + 1 : 0} <span className="text-slate-400">/</span> {questions.length}
              </span>
              <div className="w-24 sm:w-28 h-1.5 bg-slate-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-blue-500 to-indigo-600 transition-all duration-300"
                  style={{
                    width: questions.length > 0 ? `${((currentIndex + 1) / questions.length) * 100}%` : '0%',
                  }}
                />
              </div>
            </div>

            {/* Navigation Buttons */}
            <div className="flex items-center gap-1.5">
              <button
                onClick={handlePrevQuestion}
                disabled={currentIndex === 0 || isLoading}
                className="inline-flex items-center gap-1 px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 disabled:opacity-40 disabled:cursor-not-allowed transition-all active:scale-95 shadow-sm"
              >
                <span>←</span>
                <span className="hidden sm:inline">이전</span>
              </button>
              <button
                onClick={handleNextQuestion}
                disabled={currentIndex >= questions.length - 1 || isLoading}
                className="inline-flex items-center gap-1 px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold bg-blue-600 hover:bg-blue-700 text-white disabled:opacity-40 disabled:cursor-not-allowed transition-all active:scale-95 shadow-md shadow-blue-500/20"
              >
                <span className="hidden sm:inline">다음</span>
                <span>→</span>
              </button>
            </div>
          </div>
        </nav>

        {/* =======================================================================
            MAIN CARD VIEWPORT
            ======================================================================= */}
        {isLoading ? (
          /* Skeleton */
          <main aria-busy="true" className="bg-white/85 backdrop-blur-2xl border border-white/90 rounded-3xl p-6 sm:p-10 shadow-2xl animate-pulse flex flex-col gap-6">
            <div className="h-6 w-36 bg-slate-200 rounded-full" />
            <div className="w-full aspect-[16/9] max-h-[360px] bg-slate-200/80 rounded-2xl flex items-center justify-center text-slate-400 font-bold">
              📸 고화질 시험 사진 로딩 중...
            </div>
            <div className="h-20 bg-slate-100 rounded-2xl" />
          </main>
        ) : apiError ? (
          /* Error State with Fallback */
          <main className="bg-white/90 backdrop-blur-2xl border border-rose-200 rounded-3xl p-8 sm:p-12 shadow-xl flex flex-col items-center text-center gap-4 animate-fadeIn">
            <div className="w-16 h-16 rounded-3xl bg-rose-100 text-rose-600 flex items-center justify-center text-3xl">
              ⚠️
            </div>
            <h3 className="text-xl font-extrabold text-slate-900">서버 통신 오류</h3>
            <p className="text-xs sm:text-sm text-slate-600 max-w-md leading-relaxed">{apiError.message}</p>
            <div className="flex gap-3 mt-2">
              <button
                onClick={() => fetchQuestionsFromApi(currentPart, selectedSetId)}
                className="px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-blue-600 hover:bg-blue-700 text-white shadow-md active:scale-95"
              >
                🔄 재연결 시도
              </button>
              <button
                onClick={handleEnableFallbackMock}
                className="px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-slate-800 hover:bg-slate-900 text-white shadow-md active:scale-95"
              >
                📦 98문항 전체 오프라인 모드
              </button>
            </div>
          </main>
        ) : !activeQuestion ? (
          <main className="bg-white/90 rounded-3xl p-12 text-center border border-slate-200 shadow-sm">
            <p className="font-bold text-slate-700">등록된 문제가 없습니다.</p>
          </main>
        ) : (
          <main className="bg-white/85 backdrop-blur-2xl border border-white/90 rounded-2xl sm:rounded-3xl p-4 sm:p-7 lg:p-9 shadow-2xl shadow-slate-300/40 flex flex-col gap-6">
            
            {/* Top Meta Pill Header */}
            <div className="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-slate-100">
              <div className="flex flex-wrap items-center gap-2">
                <span className={`text-[11px] sm:text-xs font-extrabold px-3 py-1 rounded-full uppercase tracking-wider ${
                  currentPart === 'part2' ? 'bg-emerald-100 text-emerald-800' :
                  currentPart === 'part3' ? 'bg-blue-100 text-blue-800' : 'bg-purple-100 text-purple-800'
                }`}>
                  {currentPart.toUpperCase()}
                </span>
                <span className="text-[11px] sm:text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-100 text-slate-600">
                  Set {activeQuestion.setId}
                </span>
                <span className="text-[11px] sm:text-xs font-bold font-mono px-2.5 py-1 rounded-full bg-slate-800 text-white">
                  {activeQuestion.qNumber}
                </span>
                <span className="text-[11px] sm:text-xs font-bold px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200">
                  답변 {activeQuestion.responseTime}초
                </span>
              </div>
              <div className="text-xs font-semibold text-slate-500">
                {'keyPattern' in activeQuestion && (
                  <span className="inline-flex items-center gap-1 bg-amber-50 text-amber-800 border border-amber-200 px-2.5 py-0.5 rounded-full">
                    💡 {(activeQuestion as Part3QuestionResponse).keyPattern}
                  </span>
                )}
              </div>
            </div>

            {/* ===================================================================
                [요청 1 반영] PART 2 전용: 고화질 실사 시험 사진 뷰어 프레임
                =================================================================== */}
            {activeQuestion.part === 'part2' && 'photoScene' in activeQuestion && (
              <section aria-label="Part 2 사진 뷰어" className="flex flex-col gap-3">
                <div className="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-3.5 flex items-start gap-3">
                  <span className="text-xs font-extrabold bg-emerald-600 text-white px-2 py-0.5 rounded-md">
                    DIRECTIONS
                  </span>
                  <p className="text-xs sm:text-sm text-emerald-900 leading-relaxed">
                    In this part, you will describe the picture on your screen in as much detail as you can. You will have <strong>45 seconds</strong> to prepare, then <strong>30 seconds</strong> to speak. (Questions 3-4)
                  </p>
                </div>

                <div className="border border-slate-200 rounded-2xl overflow-hidden bg-slate-900/5 shadow-inner flex flex-col">
                  <div className="bg-slate-100 px-4 py-2 border-b border-slate-200 flex items-center justify-between text-xs">
                    <span className="font-bold text-slate-700">📸 EXAM PHOTO SCENE</span>
                    <span className="text-slate-500 font-medium font-mono text-[11px] bg-white px-2 py-0.5 rounded-full border border-slate-200">
                      {(activeQuestion as Part2QuestionResponse).photoScene?.locationEn}
                    </span>
                  </div>
                  <div className="relative aspect-[16/10] sm:aspect-[16/9] w-full max-h-[460px] overflow-hidden bg-slate-900/10 flex items-center justify-center">
                    <img
                      src={(activeQuestion as Part2QuestionResponse).imageUrl}
                      alt="Part 2 Realistic Exam Scene"
                      className="w-full h-full object-cover transition-transform duration-500 hover:scale-[1.02]"
                      loading="lazy"
                    />
                    <div className="absolute bottom-2 right-2 bg-black/60 backdrop-blur-md text-white text-[10px] sm:text-xs px-2.5 py-1 rounded-md font-mono">
                      TOEIC Speaking Realistic Photo (Q3~Q4)
                    </div>
                  </div>

                  {/* 1:1 사진 상황 해설 및 핵심 묘사 키포인트 태그 */}
                  {(activeQuestion as Part2QuestionResponse).photoDescriptionKr && (
                    <div className="bg-white p-3.5 sm:p-4 border-t border-slate-200 flex flex-col gap-2.5">
                      <div className="flex items-start gap-2 text-xs sm:text-sm text-slate-700 leading-relaxed bg-slate-50 p-3 rounded-xl border border-slate-100">
                        <span className="text-base shrink-0">🔍</span>
                        <div>
                          <strong className="text-slate-900 font-bold block mb-0.5">사진 1:1 상황 팩트 해설:</strong>
                          <p className="text-slate-600 font-medium">{(activeQuestion as Part2QuestionResponse).photoDescriptionKr}</p>
                        </div>
                      </div>

                      {(activeQuestion as Part2QuestionResponse).photoScene?.tags && (activeQuestion as Part2QuestionResponse).photoScene.tags.length > 0 && (
                        <div className="flex flex-wrap gap-1.5 pt-1">
                          {(activeQuestion as Part2QuestionResponse).photoScene.tags.map((t, ti) => (
                            <span key={ti} className="text-[11px] sm:text-xs bg-emerald-50 text-emerald-800 border border-emerald-200 px-2.5 py-1 rounded-lg font-medium">
                              ✓ {t}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              </section>
            )}

            {/* ===================================================================
                [요청 2 반영] PART 4 전용: 동적 컬럼 표 & 누락 없는 전체 일정표 + Caller Context
                =================================================================== */}
            {activeQuestion.part === 'part4' && 'scheduleTable' in activeQuestion && (
              <section aria-label="Part 4 일정표" className="flex flex-col gap-4">
                <div className="bg-purple-50/80 border border-purple-200 rounded-2xl p-3 sm:p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                  <div className="flex items-start gap-2">
                    <span className="text-xs font-extrabold bg-purple-600 text-white px-2 py-0.5 rounded-md">
                      DIRECTIONS
                    </span>
                    <span className="text-xs sm:text-sm text-purple-900">
                      Questions 8-10 are based on the schedule below. (45s to read)
                    </span>
                  </div>
                  <button
                    onClick={() => {
                      setP4ReadingTime(45);
                      setIsP4ReadingActive(!isP4ReadingActive);
                    }}
                    className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold border transition-all ${
                      isP4ReadingActive
                        ? 'bg-rose-500 text-white border-rose-600 animate-pulse'
                        : 'bg-white text-purple-700 border-purple-300 hover:bg-purple-100'
                    }`}
                  >
                    <span>⏱️</span>
                    <span>{isP4ReadingActive ? `표 읽기 남음: ${p4ReadingTime}초` : '45초 표 읽기 실전 타이머'}</span>
                  </button>
                </div>

                {/* Schedule Table (동적 컬럼 렌더링으로 모든 세트의 누락 방지) */}
                <div className="border border-slate-200/90 rounded-2xl overflow-hidden bg-white shadow-sm">
                  <div className="bg-gradient-to-r from-slate-800 to-slate-900 text-white p-4">
                    <span className="text-[10px] font-extrabold tracking-widest text-blue-400 uppercase">
                      REFERENCE DOCUMENT
                    </span>
                    <h3 className="text-base sm:text-lg font-bold mt-0.5">
                      {(activeQuestion as Part4QuestionResponse).scheduleTable?.headerTitle || (activeQuestion as any).setTitle}
                    </h3>
                    <div className="flex flex-wrap gap-2 mt-2">
                      {(activeQuestion as Part4QuestionResponse).scheduleTable?.metaInfo?.map((meta, i) => (
                        <span key={i} className="text-xs bg-white/10 px-2 py-0.5 rounded-md">
                          <strong>{meta.label}:</strong> {meta.value}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* 동적 컬럼 테이블 */}
                  <div className="overflow-x-auto">
                    {(() => {
                      const rows = (activeQuestion as Part4QuestionResponse).scheduleTable?.rows || [];
                      const colKeys = rows.length > 0 ? Object.keys(rows[0]).filter(k => k !== 'isCancelled') : ['time', 'event', 'location'];
                      return (
                        <table className="w-full text-left text-xs sm:text-sm border-collapse">
                          <thead>
                            <tr className="bg-slate-100 text-slate-600 uppercase font-bold text-[11px] border-b border-slate-200">
                              {colKeys.map((k) => (
                                <th key={k} className="p-3 capitalize">{k}</th>
                              ))}
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-slate-100">
                            {rows.map((row: any, rIdx: number) => {
                              const isCancelled = Boolean(row.isCancelled || (row.activity && String(row.activity).includes('CANCEL')) || (row.status && String(row.status).includes('CANCEL')));
                              return (
                                <tr
                                  key={rIdx}
                                  className={`hover:bg-slate-50 transition-colors ${
                                    isCancelled ? 'line-through text-slate-400 bg-rose-50/30' : 'text-slate-800'
                                  }`}
                                >
                                  {colKeys.map((k) => (
                                    <td key={k} className={`p-3 ${k === 'time' ? 'font-mono' : k === 'event' || k === 'topic' || k === 'program' ? 'font-bold text-blue-900' : ''}`}>
                                      {String(row[k] || '')}
                                    </td>
                                  ))}
                                </tr>
                              );
                            })}
                          </tbody>
                        </table>
                      );
                    })()}
                  </div>

                  {/* Caller Context Box (전화 문의자 상황) */}
                  {(activeQuestion as Part4QuestionResponse).context && (
                    <div className="bg-amber-50/70 border-t border-amber-200/80 p-3.5 flex items-start gap-3">
                      <span className="text-lg">📞</span>
                      <div className="flex flex-col text-xs sm:text-sm">
                        <span className="font-bold text-amber-900">전화 문의자 / 발화 상황:</span>
                        <p className="text-amber-800 italic mt-0.5 font-medium">{(activeQuestion as Part4QuestionResponse).context}</p>
                      </div>
                    </div>
                  )}
                </div>
              </section>
            )}

            {/* 영어 질문 지문 섹션 */}
            <section aria-label="시험 질문 영역" className="flex flex-col gap-3">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-black tracking-wider text-blue-600 uppercase">
                    QUESTION
                  </span>
                  <span className="text-[11px] text-slate-400">
                    ※ 실제 시험 환경: 한글 해석은 숨겨지며, 모범답안 토글 시 표시됩니다.
                  </span>
                </div>
                
                {/* TTS Controls */}
                <div className="flex items-center gap-1.5">
                  <button
                    onClick={() => speakText(activeQuestion.question, 1.0)}
                    className="inline-flex items-center gap-1 text-xs font-bold px-3 py-1.5 rounded-full bg-white hover:bg-blue-50 text-slate-700 hover:text-blue-600 border border-slate-200 shadow-sm transition-all active:scale-95"
                  >
                    <span>🔊 Daniel 1.0x</span>
                  </button>
                  <button
                    onClick={() => speakText(activeQuestion.question, 0.75)}
                    className="inline-flex items-center gap-1 text-xs font-bold px-3 py-1.5 rounded-full bg-white hover:bg-amber-50 text-slate-700 hover:text-amber-600 border border-slate-200 shadow-sm transition-all active:scale-95"
                  >
                    <span>🐢 느리게 0.75x</span>
                  </button>
                  <button
                    onClick={stopSpeech}
                    className="inline-flex items-center gap-1 text-xs font-bold px-2.5 py-1.5 rounded-full bg-rose-50 hover:bg-rose-100 text-rose-600 border border-rose-200 transition-all active:scale-95"
                  >
                    <span>⏹️</span>
                  </button>
                </div>
              </div>

              {/* 영문 질문 텍스트 */}
              <div className="bg-slate-50 border-l-4 border-blue-600 rounded-2xl p-4 sm:p-6 text-slate-900 shadow-inner">
                <p className="text-base sm:text-lg lg:text-xl font-semibold leading-relaxed whitespace-pre-line tracking-tight font-sans">
                  {activeQuestion.question}
                </p>
              </div>
            </section>

            {/* 실전 준비 / 답변 타이머 바 */}
            {isExamMode && (
              <section aria-label="실전 시험 타이머" className="bg-slate-50 border border-slate-200/80 rounded-2xl p-4 flex flex-col gap-3">
                <div className="flex items-center justify-between">
                  <span className={`text-xs font-extrabold uppercase px-2.5 py-0.5 rounded-full ${
                    timerState.phase === 'prep' ? 'bg-amber-100 text-amber-800' :
                    timerState.phase === 'response' ? 'bg-emerald-100 text-emerald-800' :
                    timerState.phase === 'finished' ? 'bg-slate-200 text-slate-600' :
                    'bg-slate-100 text-slate-600'
                  }`}>
                    {timerState.phase === 'prep' && '⏳ 준비 시간 (Preparation)'}
                    {timerState.phase === 'response' && '🎙️ 답변 시간 (Speaking)'}
                    {timerState.phase === 'finished' && '🏁 답변 완료'}
                    {timerState.phase === 'idle' && '대기 중 (준비시간: ' + activeQuestion.prepTime + '초)'}
                  </span>
                  <div className="flex items-baseline gap-1 font-mono">
                    <span className="text-2xl sm:text-3xl font-extrabold text-blue-600">
                      {timerState.timeLeft}
                    </span>
                    <span className="text-xs text-slate-400 font-bold">초</span>
                  </div>
                </div>

                <div className="w-full h-2.5 bg-slate-200 rounded-full overflow-hidden">
                  <div
                    className={`h-full transition-all duration-200 ${
                      timerState.phase === 'response' ? 'bg-emerald-500' : 'bg-amber-500'
                    }`}
                    style={{ width: `${timerState.progressPercent}%` }}
                  />
                </div>

                <div className="flex gap-2">
                  <button
                    onClick={startExamTimer}
                    disabled={timerState.isRunning}
                    className="flex-1 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-emerald-600 hover:bg-emerald-700 text-white shadow-md shadow-emerald-500/20 disabled:opacity-50 disabled:cursor-not-allowed transition-all active:scale-98 flex items-center justify-center gap-1.5"
                  >
                    <span>▶️</span>
                    <span>실전 카운트다운 시작</span>
                  </button>
                  {timerState.phase !== 'idle' && (
                    <button
                      onClick={resetTimer}
                      className="px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-white border border-slate-200 text-slate-600 hover:bg-slate-100 transition-all"
                    >
                      리셋
                    </button>
                  )}
                </div>
              </section>
            )}

            {/* 모범답안 토글 버튼 (Space 단축키 연동) */}
            <div className="flex justify-center py-1">
              <button
                onClick={() => setIsAnswerVisible(!isAnswerVisible)}
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-2xl text-xs sm:text-sm font-extrabold bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white shadow-lg shadow-indigo-500/25 hover:shadow-indigo-500/40 hover:scale-[1.01] active:scale-98 transition-all"
                aria-expanded={isAnswerVisible}
              >
                <span>{isAnswerVisible ? '🙈' : '👁️'}</span>
                <span>{isAnswerVisible ? '모범답안 & 문제해석 접기' : '모범답안 & 한국어 상세해설 보기'}</span>
                <span className="ml-2 text-[10px] font-mono bg-white/20 px-2 py-0.5 rounded-md">
                  Space
                </span>
              </button>
            </div>

            {/* 모범답안 상세 해설 영역 */}
            {isAnswerVisible && (
              <section aria-label="모범답안 및 해설" className="flex flex-col gap-5 pt-4 border-t border-slate-200 animate-fadeIn">
                
                {/* 질문 번역 & 발화 상황 번역 */}
                <div className="bg-blue-50/80 border border-blue-200/80 rounded-2xl p-4 flex flex-col gap-1.5">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-blue-900">💡 질문 한국어 상세 해설:</span>
                    <span className="text-[11px] text-blue-600 font-medium">모범답안과 매칭하여 학습하세요</span>
                  </div>
                  <p className="text-xs sm:text-sm text-blue-950 font-medium whitespace-pre-line leading-relaxed">
                    {activeQuestion.questionTranslation}
                  </p>
                  {(activeQuestion as Part4QuestionResponse).context_kr && (
                    <div className="mt-2 pt-2 border-t border-blue-200 text-xs text-blue-800">
                      <strong>📞 전화 문의자 발화상황 번역:</strong> {(activeQuestion as Part4QuestionResponse).context_kr}
                    </div>
                  )}
                </div>

                {/* 답안 헤더 */}
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-black tracking-wider text-emerald-700 uppercase">
                      MODEL ANSWER
                    </span>
                    <span className="text-[11px] font-bold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full">
                      120~140점 (IM3~IH) 완벽 커버
                    </span>
                  </div>

                  <div className="flex items-center gap-1.5">
                    <button
                      onClick={() => speakText(activeQuestion.answer, 1.0)}
                      className="inline-flex items-center gap-1 text-xs font-bold px-3 py-1.5 rounded-full bg-emerald-50 hover:bg-emerald-600 hover:text-white text-emerald-700 border border-emerald-300 transition-all active:scale-95 shadow-sm"
                    >
                      <span>🔊 전체 1.0x</span>
                    </button>
                    <button
                      onClick={() => speakText(activeQuestion.answer, 0.75)}
                      className="inline-flex items-center gap-1 text-xs font-bold px-3 py-1.5 rounded-full bg-amber-50 hover:bg-amber-600 hover:text-white text-amber-700 border border-amber-300 transition-all active:scale-95 shadow-sm"
                    >
                      <span>🐢 느리게 0.75x</span>
                    </button>
                  </div>
                </div>

                {/* =================================================================
                    [요청 3 반영] 문장별 분할 뷰어 (파트 2, 3, 4 모두 개별 발음 버튼 제공)
                    ================================================================= */}
                <div className="flex flex-col gap-2.5">
                  {structuredSentences.map((sent) => (
                    <div
                      key={sent.index}
                      className="bg-slate-50/90 hover:bg-blue-50/40 border border-slate-200/80 rounded-2xl p-3.5 sm:p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 transition-colors"
                    >
                      <div className="flex flex-col gap-1 flex-1">
                        {currentPart === 'part2' && (
                          <div className="mb-0.5">
                            <span className="text-[10px] sm:text-[11px] font-extrabold px-2 py-0.5 rounded-md bg-purple-50 text-purple-700 border border-purple-200 inline-block">
                              {sent.index === 0 && '🐰 1단계: 장소 도입 (This is a picture taken in...)'}
                              {sent.index === 1 && '👤 2단계: 중심 인물/피사체 동작 (In the center/foreground...)'}
                              {sent.index === 2 && '🔍 3단계: 세부 사물/주변 인물 (Next to / On the table...)'}
                              {sent.index === 3 && (structuredSentences.length > 4 ? '🏙️ 3단계: 배경/환경 (In the background...)' : '✨ 4단계: 마무리 및 총평 (Overall, it seems...')}
                              {sent.index >= 4 && '✨ 4단계: 마무리 및 총평 (Overall, it seems...)'}
                            </span>
                          </div>
                        )}
                        <span className="text-xs sm:text-sm font-semibold text-slate-900 leading-relaxed font-sans">
                          {sent.en}
                        </span>
                        <span className="text-xs text-slate-500 font-medium">
                          {sent.ko}
                        </span>
                      </div>
                      <button
                        onClick={() => {
                          setSpeakingSentenceIndex(sent.index);
                          speakText(sent.en, 1.0, () => setSpeakingSentenceIndex(null));
                        }}
                        className={`inline-flex items-center gap-1 text-xs font-bold px-3 py-1.5 rounded-full border transition-all shrink-0 ${
                          speakingSentenceIndex === sent.index
                            ? 'bg-blue-600 text-white border-blue-600 animate-pulse'
                            : 'bg-white text-slate-700 border-slate-200 hover:border-blue-400 hover:text-blue-600 shadow-sm active:scale-95'
                        }`}
                        title="이 문장만 개별 발음 듣기"
                      >
                        <span>🔊</span>
                        <span>문장듣기</span>
                      </button>
                    </div>
                  ))}
                </div>

                {/* [요청 3 반영: 시계토끼 핵심문장 보라색 카드는 해설에서 제거하고 상단 만능문장 족보집 모달 안에 모두 통합] */}

                {/* 어휘 & 발음기호 */}
                {activeQuestion.vocabulary && activeQuestion.vocabulary.length > 0 && (
                  <div className="bg-white border border-slate-200 rounded-2xl p-4 flex flex-col gap-3">
                    <div className="flex items-center gap-2">
                      <span className="text-base">📖</span>
                      <span className="text-xs sm:text-sm font-bold text-slate-800">
                        핵심 어휘 및 IPA 발음기호 (단어 클릭 시 원어민 음성 재생)
                      </span>
                    </div>
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
                      {activeQuestion.vocabulary.map((vocab, vIdx) => (
                        <div
                          key={vIdx}
                          onClick={() => speakText(vocab.word, 0.9)}
                          className="group bg-slate-50 hover:bg-blue-50/60 border border-slate-200/80 hover:border-blue-300 rounded-xl p-2.5 flex items-center justify-between cursor-pointer transition-all"
                        >
                          <div className="flex flex-col">
                            <div className="flex items-center gap-1.5">
                              <span className="text-xs sm:text-sm font-bold text-slate-800 group-hover:text-blue-600">
                                {vocab.word}
                              </span>
                              <span className="text-[10px] text-slate-400 font-mono">
                                {vocab.ipa}
                              </span>
                            </div>
                            <span className="text-[11px] text-slate-500 mt-0.5">
                              {vocab.meaning}
                            </span>
                          </div>
                          <span className="text-slate-400 group-hover:text-blue-600 text-xs transition-colors">
                            🔊
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* 문법 포인트 */}
                {activeQuestion.grammarPoints && activeQuestion.grammarPoints.length > 0 && (
                  <div className="bg-amber-50/60 border border-amber-200/70 rounded-2xl p-4 flex flex-col gap-2.5">
                    <div className="flex items-center gap-2">
                      <span className="text-base">💡</span>
                      <span className="text-xs sm:text-sm font-bold text-amber-900">
                        핵심 문법 및 감점 방지 구문 분석 (Grammar Points)
                      </span>
                    </div>
                    <div className="flex flex-col gap-2">
                      {activeQuestion.grammarPoints.map((gp, gIdx) => (
                        <div key={gIdx} className="bg-white/80 rounded-xl p-3 border border-amber-200/50 flex flex-col gap-1">
                          <span className="text-xs font-bold text-amber-900">{gp.title}</span>
                          <p className="text-xs text-slate-700 leading-relaxed">{gp.explanation}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* 120-140점 전략 팁 */}
                <div className="bg-emerald-50/60 border border-emerald-200/80 rounded-2xl p-4 flex items-start gap-3">
                  <span className="text-xl">🎯</span>
                  <div className="flex flex-col text-xs sm:text-sm">
                    <span className="font-extrabold text-emerald-900">120~140점(IM3~IH) 확보 핵심 전략:</span>
                    <p className="text-emerald-900 mt-1 leading-relaxed font-medium">{activeQuestion.scoreTip}</p>
                  </div>
                </div>

              </section>
            )}

          </main>
        )}

        {/* =======================================================================
            FOOTER (단축키 가이드)
            ======================================================================= */}
        <footer className="bg-white/60 backdrop-blur-md border border-white/60 rounded-2xl p-4 flex flex-col items-center gap-3 text-center text-xs text-slate-500">
          <div className="flex flex-wrap items-center justify-center gap-1.5 sm:gap-2">
            <span className="inline-flex items-center gap-1 bg-white border border-slate-200 px-2 py-0.5 rounded-md font-mono text-[11px]">
              <kbd className="font-bold">←</kbd> 이전
            </span>
            <span className="inline-flex items-center gap-1 bg-white border border-slate-200 px-2 py-0.5 rounded-md font-mono text-[11px]">
              <kbd className="font-bold">→</kbd> 다음
            </span>
            <span className="inline-flex items-center gap-1 bg-white border border-slate-200 px-2 py-0.5 rounded-md font-mono text-[11px]">
              <kbd className="font-bold">Space</kbd> 답안 토글
            </span>
            <span className="inline-flex items-center gap-1 bg-white border border-slate-200 px-2 py-0.5 rounded-md font-mono text-[11px]">
              <kbd className="font-bold">1</kbd> 1.0x
            </span>
            <span className="inline-flex items-center gap-1 bg-white border border-slate-200 px-2 py-0.5 rounded-md font-mono text-[11px]">
              <kbd className="font-bold">2</kbd> 0.75x
            </span>
            <span className="inline-flex items-center gap-1 bg-white border border-slate-200 px-2 py-0.5 rounded-md font-mono text-[11px]">
              <kbd className="font-bold">Esc</kbd> 정지/닫기
            </span>
          </div>
          <p className="font-medium text-slate-600">
            {MOCK_USER_PROFILE.dDayText} · 침묵 없이 만능문장으로 140점(IH) 달성하세요! 🏆
          </p>
        </footer>

      </div>

      {/* =========================================================================
          [요청 3 반영] MODAL: 시계토끼 만능문장 종합 족보집 (모든 파트 핵심 공식 총집합)
          ========================================================================= */}
      {isCheatSheetOpen && (
        <div className="fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-3.5 sm:p-6 animate-fadeIn">
          <div className="bg-white rounded-3xl w-full max-w-2xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden border border-slate-200">
            <div className="p-4 sm:p-5 border-b border-slate-100 flex items-center justify-between bg-slate-50">
              <div className="flex items-center gap-2">
                <span className="text-2xl">🐰</span>
                <h3 className="text-base sm:text-lg font-extrabold text-slate-800">
                  시계토끼 만능문장 종합 족보집 (모든 파트 공식 집대성)
                </h3>
              </div>
              <button
                onClick={() => setIsCheatSheetOpen(false)}
                className="w-8 h-8 rounded-full bg-slate-200/70 hover:bg-slate-300 text-slate-600 flex items-center justify-center font-bold text-sm transition-colors"
                aria-label="닫기"
              >
                ✕
              </button>
            </div>

            <div className="flex border-b border-slate-200 bg-white">
              <button
                onClick={() => setModalTab('part2')}
                className={`flex-1 py-3 text-xs sm:text-sm font-bold border-b-2 transition-colors ${
                  modalTab === 'part2'
                    ? 'border-emerald-600 text-emerald-700 bg-emerald-50/50'
                    : 'border-transparent text-slate-500 hover:text-slate-700'
                }`}
              >
                🖼️ PART 2 4단계 묘사 공식
              </button>
              <button
                onClick={() => setModalTab('part3')}
                className={`flex-1 py-3 text-xs sm:text-sm font-bold border-b-2 transition-colors ${
                  modalTab === 'part3'
                    ? 'border-blue-600 text-blue-700 bg-blue-50/50'
                    : 'border-transparent text-slate-500 hover:text-slate-700'
                }`}
              >
                🔖 PART 3 만능문장 7대 공식
              </button>
              <button
                onClick={() => setModalTab('part4')}
                className={`flex-1 py-3 text-xs sm:text-sm font-bold border-b-2 transition-colors ${
                  modalTab === 'part4'
                    ? 'border-purple-600 text-purple-700 bg-purple-50/50'
                    : 'border-transparent text-slate-500 hover:text-slate-700'
                }`}
              >
                📑 PART 4 Q8~Q10 응답 족보
              </button>
            </div>

            <div className="p-4 sm:p-6 overflow-y-auto flex flex-col gap-3.5">
              <div className="bg-blue-50 border border-blue-200 rounded-2xl p-3 text-xs text-blue-900 leading-relaxed">
                💡 <strong>시험장 팁:</strong> 어떤 돌발 질문이 나와도 당황하지 말고 질문을 주어로 받아친 후 아래 만능문장 1~2개를 붙이면 120~140점이 완성됩니다.
              </div>

              {MOCK_CHEAT_SHEETS[modalTab].map((formula) => (
                <div
                  key={formula.id}
                  className="bg-slate-50 border border-slate-200/80 rounded-2xl p-4 flex flex-col gap-1.5"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-blue-600">{formula.topic}</span>
                    <span className="text-[10px] font-mono font-bold bg-slate-200 text-slate-700 px-2 py-0.5 rounded-full">
                      {formula.numberTag}
                    </span>
                  </div>
                  <p className="text-xs sm:text-sm font-bold text-slate-900 font-mono mt-0.5">
                    {formula.formulaEn}
                  </p>
                  <p className="text-xs text-slate-600 font-medium">{formula.formulaKo}</p>
                  {formula.extraTip && (
                    <span className="text-[11px] text-slate-400 mt-1">
                      📌 {formula.extraTip}
                    </span>
                  )}
                </div>
              ))}
            </div>

            <div className="p-4 border-t border-slate-100 bg-slate-50 flex justify-end">
              <button
                onClick={() => setIsCheatSheetOpen(false)}
                className="px-5 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-900 text-white transition-all"
              >
                닫기 (Esc)
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ToeicSpeakingApp;
