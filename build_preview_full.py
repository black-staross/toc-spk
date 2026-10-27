import json

print("Rebuilding preview_react.html with all 3 user requirements updated...")

with open('data.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

p2_list = master.get('part2', [])
p3_list = master.get('part3', [])
p4_sets = master.get('part4', [])
p4_list = []
for s in p4_sets:
    sid = s.get('setNumber', 1)
    for idx, q in enumerate(s.get('questions', [])):
        p4_list.append({
            'id': q.get('id', sid * 10 + idx + 1),
            'part': 'part4',
            'setId': sid,
            'setNumber': sid,
            'setTitle': s.get('title', f'Set {sid}'),
            'qNumber': q.get('qNumber', q.get('questionNumber', f'Question {8 + idx}')),
            'prepTime': q.get('prepTime', 3),
            'responseTime': q.get('responseTime', 30 if idx == 2 else 15),
            'question': q.get('question', ''),
            'questionTranslation': q.get('questionTranslation', ''),
            'answer': q.get('answer', ''),
            'answerTranslation': q.get('answerTranslation', ''),
            'magicSentences': q.get('magicSentences', []),
            'scoreTip': q.get('scoreTip', ''),
            'vocabulary': q.get('vocabulary', []),
            'grammarPoints': q.get('grammarPoints', []),
            'scheduleTable': s.get('table', {}),
            'context': s.get('context', ''),
            'context_kr': s.get('context_kr', '')
        })

data_payload = {
    'part2': p2_list,
    'part3': p3_list,
    'part4': p4_list
}

data_json_str = json.dumps(data_payload, ensure_ascii=False)

html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>토익스피킹 파트 2, 3, 4 마스터 트레이너 | React & Tailwind Live Preview (High-Res Edition)</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Pretendard', '-apple-system', 'BlinkMacSystemFont', 'system-ui', 'Roboto', 'sans-serif'],
            mono: ['Inter', 'monospace'],
          },
          animation: {
            fadeIn: 'fadeIn 0.25s ease-in-out',
          },
          keyframes: {
            fadeIn: {
              '0%': { opacity: '0', transform: 'translateY(4px)' },
              '100%': { opacity: '1', transform: 'translateY(0)' },
            },
          },
        }
      }
    }
  </script>

  <!-- Google Fonts: Inter & Pretendard -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">

  <!-- React 18 & ReactDOM & Babel CDN -->
  <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

  <style>
    body {
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-800">
  <div id="root"></div>

  <script>
    window.TOEIC_FULL_DATA = __DATA_JSON_PLACEHOLDER__;
  </script>

  <!-- React App Script -->
  <script type="text/babel">
    const { useState, useEffect, useMemo, useCallback } = React;
    const FULL_DATA = window.TOEIC_FULL_DATA || { part2: [], part3: [], part4: [] };

    // [요청 3 반영] 시계토끼 핵심 공식을 만능족보 안에 모두 집약
    const CHEAT_FORMULAS = {
      part2: [
        { numberTag: 'P2-1', topic: '1단계: 장소 도입 (Location)', formulaEn: '"This is a picture taken at [a grocery store / an office / a park / indoors]."', formulaKo: '이 사진은 [마트/사무실/공원/실내]에서 찍힌 사진입니다.', extraTip: '시작 3초 안에 장소를 선언하여 발화 유창성 및 구조적 첫인상을 획득합니다.' },
        { numberTag: 'P2-2', topic: '2단계: 물건 집으려 손 뻗기 (초빈출)', formulaEn: '"He/She is reaching for an item on the shelf."', formulaKo: '그/그녀는 선반에 있는 물건을 집으려고 손을 뻗고 있습니다.', extraTip: '마트, 도서관, 서점, 옷가게 사진 필수 표현.' },
        { numberTag: 'P2-3', topic: '2단계: 결제 및 카드 건네기 / 받기', formulaEn: '"He is handing over a credit card, and she is receiving it with a smile."', formulaKo: '남성은 신용카드를 건네주고 있고, 여성은 미소 지으며 그것을 받고 있습니다.', extraTip: '계산대 및 프런트 데스크 대칭 동작 표현.' },
        { numberTag: 'P2-4', topic: '2단계: 전자기기 타이핑 및 통화하기', formulaEn: '"He is typing on a keyboard while talking on the phone."', formulaKo: '그는 전화 통화를 하면서 키보드를 타이핑하고 있습니다.', extraTip: 'while + ~ing 동시 동작 구문으로 고득점(IH) 확보.' },
        { numberTag: 'P2-5', topic: '3단계: 사물 진열 및 주차 (수동태)', formulaEn: '"Products are displayed on the shelves. / Cars are parked in the background."', formulaKo: '제품들이 선반에 진열되어 있습니다. / 배경에 차들이 주차되어 있습니다.', extraTip: '사람 묘사 후 사물 묘사 시 be + p.p. 수동태 적용.' },
        { numberTag: 'P2-6', topic: '4단계: 마무리 총평 공식 (Closing)', formulaEn: '"Overall, it seems like they are busy. / Overall, it seems like a peaceful day."', formulaKo: '전반적으로 그들은 바빠 보입니다. / 평화로운 날 같습니다.', extraTip: '남은 3~5초 동안 침묵 없이 감점 없이 깔끔하게 매듭짓기.' }
      ],
      part3: [
        { numberTag: '공식 1', topic: '스트레스 해소 & 기분 전환', formulaEn: '"It relieves my stress. I am stressed out these days, so I need this."', formulaKo: '스트레스를 풀어줍니다. 요즘 스트레스가 많아서 이게 필요해요.', extraTip: '취미, 운동, 음악, 영화, 외식 등 거의 모든 여가 질문에 적용 가능.' },
        { numberTag: '공식 2', topic: '시간 절약 & 바쁜 일상', formulaEn: '"It is faster, so I can save time. I have a busy daily routine."', formulaKo: '더 빨라서 시간을 아낄 수 있습니다. 저는 일상이 바빠요.', extraTip: '온라인 쇼핑, 지하철, 배달 음식, 모바일 뱅킹 단골 템플릿.' },
        { numberTag: '공식 3', topic: '비용 절약 & 빠듯한 예산', formulaEn: '"The price is reasonable, so I can save money. I have a tight budget."', formulaKo: '가격이 합리적이라 돈을 아낄 수 있습니다. 요즘 예산이 빠듯해요.', extraTip: '할인 행사, 대중교통 이용, 도서관, 가성비 제품 질문에 최적.' },
        { numberTag: '공식 4', topic: '유용한 정보 획득 & 후기', formulaEn: '"I can get a lot of useful information on the Internet and social media."', formulaKo: '인터넷과 SNS에서 많은 유용한 정보를 얻을 수 있습니다.', extraTip: '리뷰 읽기, 웹 검색, 스마트폰 앱 사용 질문에 100% 매칭.' },
        { numberTag: '공식 5', topic: '편리함 & 언제 어디서나', formulaEn: '"It is very convenient because I can do it anytime and anywhere."', formulaKo: '언제 어디서나 할 수 있어서 매우 편리합니다.', extraTip: 'OTT, 전자책, 스마트폰, 배송 서비스 질문에 적용.' },
        { numberTag: '공식 6', topic: '친구/가족과의 친목 & 추억', formulaEn: '"I can spend quality time with my friends and make good memories."', formulaKo: '친구들과 소중한 시간을 보내고 좋은 추억을 만들 수 있습니다.', extraTip: '카페, 여행, 콘서트, 맛집 외식 질문에 적용.' }
      ],
      part4: [
        { numberTag: 'Q8 공식', topic: '일정/장소 기본 안내 공식 (Q8 - 15초)', formulaEn: '"The [행사명] will be held on [날짜] at [시간] in [장소]."', formulaKo: '[행사]는 [날짜] [시간]에 [장소]에서 열릴 예정입니다.', extraTip: '전치사 짝꿍: on + 날짜, at + 시간, in + 장소.' },
        { numberTag: 'Q9 공식', topic: '오류 정정 및 취소 통보 공식 (Q9 - 15초)', formulaEn: '"No, actually, that information is not correct. It has been cancelled due to [이유]."', formulaKo: '아니요, 사실 그 정보는 맞지 않습니다. [이유]로 인해 취소되었습니다.', extraTip: '정중한 거절 표현(No, actually) 후 변경/취소 사실 명시 (취소선 확인).' },
        { numberTag: 'Q10 공식', topic: '복수 세션 순차 나열 공식 (Q10 - 30초)', formulaEn: '"Sure, there are two scheduled sessions. First, on [날짜] at [시간], ~ Second, on [날짜] at [시간], ~"', formulaKo: '물론입니다. 2개의 예정된 세션이 있습니다. 첫째로 ~, 둘째로 ~', extraTip: '도입 문장으로 시간을 벌고 First와 Second로 분할하여 안정적으로 30초 채우기.' }
      ]
    };

    function App() {
      const [currentPart, setCurrentPart] = useState('part3');
      const [selectedSetId, setSelectedSetId] = useState('all');
      const [currentIndex, setCurrentIndex] = useState(0);
      const [isAnswerVisible, setIsAnswerVisible] = useState(false);
      const [isExamMode, setIsExamMode] = useState(true);
      const [isCheatSheetOpen, setIsCheatSheetOpen] = useState(false);
      const [modalTab, setModalTab] = useState('part3');
      const [isP4ReadingActive, setIsP4ReadingActive] = useState(false);
      const [p4ReadingTime, setP4ReadingTime] = useState(45);
      const [speakingSentenceIndex, setSpeakingSentenceIndex] = useState(null);

      // 타이머 상태
      const [timerState, setTimerState] = useState({
        phase: 'idle',
        timeLeft: 3,
        totalDuration: 3,
        progressPercent: 0,
        isRunning: false
      });

      // 현재 선택된 파트의 전체 문제 목록
      const rawPartList = useMemo(() => {
        if (currentPart === 'part2') return FULL_DATA.part2 || [];
        if (currentPart === 'part3') return FULL_DATA.part3 || [];
        return FULL_DATA.part4 || [];
      }, [currentPart]);

      // 세트 필터링된 문제 목록
      const filteredQuestions = useMemo(() => {
        if (selectedSetId === 'all') return rawPartList;
        return rawPartList.filter(q => Number(q.setId || q.setNumber) === Number(selectedSetId));
      }, [rawPartList, selectedSetId]);

      // 사용 가능한 세트 번호 목록
      const availableSetIds = useMemo(() => {
        const s = new Set();
        rawPartList.forEach(q => s.add(Number(q.setId || q.setNumber || 1)));
        return Array.from(s).sort((a, b) => a - b);
      }, [rawPartList]);

      const activeQuestion = filteredQuestions[currentIndex] || filteredQuestions[0];

      // 음성 TTS 함수
      const speakText = (text, rate = 1.0, onEndCallback = null) => {
        if (!('speechSynthesis' in window)) return;
        window.speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(text);
        u.lang = 'en-US';
        u.rate = rate;
        const voices = window.speechSynthesis.getVoices();
        const preferred = voices.find(v => v.name.toLowerCase().includes('daniel')) || voices.find(v => v.lang.startsWith('en'));
        if (preferred) u.voice = preferred;
        u.onend = () => {
          setSpeakingSentenceIndex(null);
          if (onEndCallback) onEndCallback();
        };
        u.onerror = () => setSpeakingSentenceIndex(null);
        window.speechSynthesis.speak(u);
      };

      const handlePartSwitch = (p) => {
        if ('speechSynthesis' in window) window.speechSynthesis.cancel();
        setCurrentPart(p);
        setSelectedSetId('all');
        setCurrentIndex(0);
        setIsAnswerVisible(false);
        setIsP4ReadingActive(false);
        setP4ReadingTime(45);
        const prep = p === 'part2' ? 45 : 3;
        setTimerState({
          phase: 'idle',
          timeLeft: prep,
          totalDuration: prep,
          progressPercent: 0,
          isRunning: false
        });
      };

      const startTimer = () => {
        if (!activeQuestion) return;
        const prep = activeQuestion.prepTime || (currentPart === 'part2' ? 45 : 3);
        setTimerState({
          phase: 'prep',
          timeLeft: prep,
          totalDuration: prep,
          progressPercent: 0,
          isRunning: true
        });
      };

      // 타이머 이펙트
      useEffect(() => {
        let timer = null;
        if (timerState.isRunning && timerState.timeLeft > 0) {
          timer = setInterval(() => {
            setTimerState(prev => {
              const nextTime = prev.timeLeft - 1;
              const pct = ((prev.totalDuration - nextTime) / prev.totalDuration) * 100;
              return { ...prev, timeLeft: nextTime, progressPercent: Math.min(pct, 100) };
            });
          }, 1000);
        } else if (timerState.isRunning && timerState.timeLeft <= 0) {
          if (timerState.phase === 'prep') {
            const resp = activeQuestion?.responseTime || (currentPart === 'part2' ? 30 : 15);
            setTimerState({
              phase: 'response',
              timeLeft: resp,
              totalDuration: resp,
              progressPercent: 0,
              isRunning: true
            });
          } else {
            setTimerState(prev => ({ ...prev, phase: 'finished', isRunning: false, progressPercent: 100 }));
          }
        }
        return () => timer && clearInterval(timer);
      }, [timerState.isRunning, timerState.timeLeft, timerState.phase, activeQuestion, currentPart]);

      // Part 4 표 분석 타이머 이펙트
      useEffect(() => {
        let p4t = null;
        if (isP4ReadingActive && p4ReadingTime > 0) {
          p4t = setInterval(() => setP4ReadingTime(t => t - 1), 1000);
        } else if (isP4ReadingActive && p4ReadingTime <= 0) {
          setIsP4ReadingActive(false);
        }
        return () => p4t && clearInterval(p4t);
      }, [isP4ReadingActive, p4ReadingTime]);

      // [요청 3 반영] 파트 2, 3, 4 모두 정밀 문장 단위 분할
      const structuredSentences = useMemo(() => {
        if (!activeQuestion || !activeQuestion.answer) return [];
        let rawEn = activeQuestion.answer.split('\\n').map(s => s.trim()).filter(s => s.length > 0);
        let rawKo = (activeQuestion.answerTranslation || '').split('\\n').map(s => s.trim()).filter(s => s.length > 0);

        if (rawEn.length === 1 && rawEn[0].includes('.')) {
          const matchEn = rawEn[0].match(/[^.!?]+[.!?]+(\\s+|$)/g);
          if (matchEn && matchEn.length > 1) rawEn = matchEn.map(s => s.trim());
        }
        if (rawKo.length === 1 && rawKo[0].includes('.')) {
          const matchKo = rawKo[0].match(/[^.!?]+[.!?]+(\\s+|$)/g);
          if (matchKo && matchKo.length > 1) rawKo = matchKo.map(s => s.trim());
        }

        return rawEn.map((en, idx) => ({
          index: idx + 1,
          en,
          ko: rawKo[idx] || ''
        }));
      }, [activeQuestion]);

      // 키보드 단축키
      useEffect(() => {
        const handleKeyDown = (e) => {
          if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
          if (e.key === 'ArrowLeft' && currentIndex > 0) {
            e.preventDefault();
            setCurrentIndex(i => i - 1);
            setIsAnswerVisible(false);
          } else if (e.key === 'ArrowRight' && currentIndex < filteredQuestions.length - 1) {
            e.preventDefault();
            setCurrentIndex(i => i + 1);
            setIsAnswerVisible(false);
          } else if (e.code === 'Space') {
            e.preventDefault();
            setIsAnswerVisible(v => !v);
          } else if (e.key === '1' && activeQuestion) {
            e.preventDefault();
            speakText(activeQuestion.question, 1.0);
          } else if (e.key === '2' && activeQuestion) {
            e.preventDefault();
            speakText(activeQuestion.question, 0.75);
          } else if (e.key === 'Escape') {
            if ('speechSynthesis' in window) window.speechSynthesis.cancel();
            setIsCheatSheetOpen(false);
          }
        };
        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
      }, [currentIndex, filteredQuestions.length, activeQuestion]);

      if (!activeQuestion) return <div className="p-8 text-center font-bold">문제가 없습니다.</div>;

      return (
        <div className="min-h-screen bg-gradient-to-b from-slate-50 via-slate-100 to-slate-200 text-slate-800 antialiased pb-16">
          {/* Ambient Glow */}
          <div className="fixed -top-20 -left-20 w-80 h-80 bg-blue-500/10 rounded-full blur-3xl pointer-events-none -z-10" />
          <div className="fixed top-1/4 -right-20 w-80 h-80 bg-purple-500/10 rounded-full blur-3xl pointer-events-none -z-10" />

          <div className="w-full max-w-5xl mx-auto px-3.5 sm:px-6 lg:px-8 py-5 sm:py-7 flex flex-col gap-5 sm:gap-6">
            
            {/* 1. Bookmark Tabs */}
            <nav className="grid grid-cols-3 gap-2 sm:gap-4">
              <button
                onClick={() => handlePartSwitch('part2')}
                className={`flex items-center justify-center sm:justify-start gap-2 p-3 sm:p-4 rounded-2xl border transition-all ${
                  currentPart === 'part2'
                    ? 'bg-white/95 border-emerald-500 shadow-md ring-2 ring-emerald-500/20 translate-y-[-2px]'
                    : 'bg-white/60 hover:bg-white/90 border-slate-200 text-slate-600'
                }`}
              >
                <span className="text-xl sm:text-2xl">🖼️</span>
                <div className="flex flex-col text-left">
                  <span className={`text-xs sm:text-sm font-bold ${currentPart === 'part2' ? 'text-emerald-700' : 'text-slate-700'}`}>
                    PART 2 책갈피
                  </span>
                  <span className="hidden sm:inline text-xs text-slate-400">고화질 실사 사진 (26세트)</span>
                </div>
              </button>

              <button
                onClick={() => handlePartSwitch('part3')}
                className={`flex items-center justify-center sm:justify-start gap-2 p-3 sm:p-4 rounded-2xl border transition-all ${
                  currentPart === 'part3'
                    ? 'bg-white/95 border-blue-500 shadow-md ring-2 ring-blue-500/20 translate-y-[-2px]'
                    : 'bg-white/60 hover:bg-white/90 border-slate-200 text-slate-600'
                }`}
              >
                <span className="text-xl sm:text-2xl">🔖</span>
                <div className="flex flex-col text-left">
                  <span className={`text-xs sm:text-sm font-bold ${currentPart === 'part3' ? 'text-blue-700' : 'text-slate-700'}`}>
                    PART 3 책갈피
                  </span>
                  <span className="hidden sm:inline text-xs text-slate-400">일상 질문 (48문항/16세트)</span>
                </div>
              </button>

              <button
                onClick={() => handlePartSwitch('part4')}
                className={`flex items-center justify-center sm:justify-start gap-2 p-3 sm:p-4 rounded-2xl border transition-all ${
                  currentPart === 'part4'
                    ? 'bg-white/95 border-purple-500 shadow-md ring-2 ring-purple-500/20 translate-y-[-2px]'
                    : 'bg-white/60 hover:bg-white/90 border-slate-200 text-slate-600'
                }`}
              >
                <span className="text-xl sm:text-2xl">📑</span>
                <div className="flex flex-col text-left">
                  <span className={`text-xs sm:text-sm font-bold ${currentPart === 'part4' ? 'text-purple-700' : 'text-slate-700'}`}>
                    PART 4 책갈피
                  </span>
                  <span className="hidden sm:inline text-xs text-slate-400">표 보고 답하기 (24문항/8세트)</span>
                </div>
              </button>
            </nav>

            {/* 2. Glass Header */}
            <header className="bg-white/80 backdrop-blur-xl border border-white/80 rounded-3xl p-5 sm:p-6 shadow-xl flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
              <div className="flex flex-col gap-1">
                <div className="inline-flex items-center gap-2 bg-blue-50 border border-blue-200 text-blue-600 px-3 py-1 rounded-full text-xs font-semibold w-fit">
                  <span className="w-2 h-2 rounded-full bg-blue-500 animate-pulse" />
                  <span>Target: 120 ~ 140점 (IM3 - IH) · 전체 98개 기출 문항 마스터판</span>
                </div>
                <h1 className="text-xl sm:text-2xl lg:text-3xl font-extrabold tracking-tight text-slate-900 flex items-center gap-2">
                  <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">TOEIC Speaking</span>
                  <span>{currentPart === 'part2' ? 'Part 2 실전 트레이너' : currentPart === 'part3' ? 'Part 3 실전 트레이너' : 'Part 4 실전 트레이너'}</span>
                </h1>
                <p className="text-xs text-slate-500">
                  {currentPart === 'part2' && '기출 26개 고화질 실사 사진 · 45초 준비 / 30초 답변 · 문장별 개별 발음'}
                  {currentPart === 'part3' && '16개 테마 48개 전 문항 · 한글해석 블라인드 · 문장별 개별 발음'}
                  {currentPart === 'part4' && '8개 세트 24문항 전체 일정표 · 45초 표 분석 · 문의자 발화상황 연계'}
                </p>
              </div>

              <div className="flex items-center gap-2 w-full sm:w-auto">
                <div className="bg-white/90 border border-blue-200 rounded-2xl px-3 py-1.5 flex items-center gap-2 shadow-sm text-xs">
                  <span>👨‍💼</span>
                  <span className="font-bold">Daniel <strong className="text-blue-600 font-normal">(영국식)</strong></span>
                  <button onClick={() => speakText("Hello! Ready to practice every sentence separately?", 1.0)} className="text-[11px] bg-blue-50 text-blue-600 px-2 py-0.5 rounded-full font-bold">
                    ▶️
                  </button>
                </div>
                <button onClick={() => { setModalTab(currentPart); setIsCheatSheetOpen(true); }} className="px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold bg-purple-50 text-purple-700 border border-purple-200 active:scale-95 transition-all">
                  🐰 만능족보
                </button>
                <button onClick={() => setIsExamMode(!isExamMode)} className={`px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold border transition-all ${isExamMode ? 'bg-emerald-50 text-emerald-700 border-emerald-300' : 'bg-slate-100 text-slate-400 border-slate-200'}`}>
                  ⏱️ {isExamMode ? 'ON' : 'OFF'}
                </button>
              </div>
            </header>

            {/* 3. Toolbar (세트 셀렉터 + 이전/다음) */}
            <nav className="bg-white/80 backdrop-blur-xl border border-white/80 rounded-2xl p-3 sm:p-4 shadow-sm flex flex-col sm:flex-row items-center justify-between gap-3">
              <div className="flex items-center gap-2 w-full sm:w-auto">
                <label className="text-xs sm:text-sm font-bold text-slate-600 whitespace-nowrap">주제 세트:</label>
                <select
                  value={selectedSetId}
                  onChange={(e) => { setSelectedSetId(e.target.value); setCurrentIndex(0); setIsAnswerVisible(false); }}
                  className="flex-1 sm:w-64 bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 text-xs sm:text-sm font-semibold text-slate-700 outline-none cursor-pointer"
                >
                  <option value="all">전체 세트 (총 {rawPartList.length}문항)</option>
                  {availableSetIds.map(sid => (
                    <option key={sid} value={sid}>Set {sid} 문항</option>
                  ))}
                </select>
              </div>

              <div className="flex items-center justify-between sm:justify-center gap-3 w-full sm:w-auto">
                <div className="flex items-center gap-1.5 text-xs font-mono font-bold text-slate-700 bg-slate-100 px-3 py-1.5 rounded-xl">
                  <span>{currentIndex + 1}</span>
                  <span className="text-slate-400">/</span>
                  <span>{filteredQuestions.length}</span>
                </div>
                <div className="flex gap-1.5">
                  <button
                    onClick={() => { if (currentIndex > 0) { setCurrentIndex(i => i - 1); setIsAnswerVisible(false); } }}
                    disabled={currentIndex === 0}
                    className="px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold bg-white border border-slate-200 disabled:opacity-40 shadow-sm active:scale-95"
                  >
                    ← 이전
                  </button>
                  <button
                    onClick={() => { if (currentIndex < filteredQuestions.length - 1) { setCurrentIndex(i => i + 1); setIsAnswerVisible(false); } }}
                    disabled={currentIndex >= filteredQuestions.length - 1}
                    className="px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold bg-blue-600 text-white shadow-md disabled:opacity-40 active:scale-95"
                  >
                    다음 →
                  </button>
                </div>
              </div>
            </nav>

            {/* 4. Main Practice Card */}
            <main className="bg-white/85 backdrop-blur-2xl border border-white/90 rounded-3xl p-5 sm:p-8 shadow-2xl flex flex-col gap-6">
              
              {/* Meta Pills */}
              <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-100">
                <div className="flex items-center gap-2 flex-wrap">
                  <span className="text-xs font-extrabold px-3 py-1 rounded-full uppercase bg-blue-100 text-blue-800">
                    {currentPart.toUpperCase()}
                  </span>
                  <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-100 text-slate-600">
                    Set {activeQuestion.setId || activeQuestion.setNumber || 1}
                  </span>
                  <span className="text-xs font-bold px-2.5 py-1 rounded-full bg-slate-800 text-white font-mono">
                    {activeQuestion.qNumber || activeQuestion.questionNumber}
                  </span>
                  <span className="text-xs font-bold px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200">
                    답변 {activeQuestion.responseTime}초
                  </span>
                </div>
                {activeQuestion.keyPattern && (
                  <span className="text-xs bg-amber-50 text-amber-800 px-2.5 py-1 rounded-full border border-amber-200 font-semibold">
                    💡 {activeQuestion.keyPattern}
                  </span>
                )}
              </div>

              {/* [요청 1 반영] Part 2 고해상도 실제 시험 사진 뷰어 및 1:1 묘사 체크리스트 */}
              {currentPart === 'part2' && activeQuestion.imageUrl && (
                <div className="border border-slate-200 rounded-2xl overflow-hidden bg-slate-900/5 shadow-inner flex flex-col">
                  <div className="bg-slate-100 px-4 py-2 border-b border-slate-200 flex justify-between items-center text-xs font-semibold text-slate-600">
                    <span className="flex items-center gap-1.5 font-bold text-slate-800">📸 EXAM PHOTO SCENE</span>
                    <span className="bg-white px-2 py-0.5 rounded-full border border-slate-200 font-mono text-[11px] text-blue-700">{activeQuestion.photoScene?.locationEn || 'in the scene'}</span>
                  </div>
                  <div className="relative aspect-[16/9] max-h-[440px] bg-slate-900/10 flex items-center justify-center overflow-hidden">
                    <img
                      src={activeQuestion.imageUrl}
                      alt="Part 2 Realistic Photo"
                      className="w-full h-full object-cover transition-transform duration-500 hover:scale-[1.02]"
                    />
                    <div className="absolute bottom-2 right-2 bg-black/60 backdrop-blur-md text-white text-[10px] sm:text-xs px-2.5 py-1 rounded-md font-mono">
                      TOEIC Speaking Realistic Photo (Q3~Q4)
                    </div>
                  </div>

                  {/* 1:1 사진 상황 해설 및 핵심 묘사 키포인트 태그 */}
                  {activeQuestion.photoDescriptionKr && (
                    <div className="bg-white p-3.5 sm:p-4 border-t border-slate-200 flex flex-col gap-2.5">
                      <div className="flex items-start gap-2 text-xs sm:text-sm text-slate-700 leading-relaxed bg-slate-50 p-3 rounded-xl border border-slate-100">
                        <span className="text-base shrink-0">🔍</span>
                        <div>
                          <strong className="text-slate-900 font-bold block mb-0.5">사진 1:1 상황 팩트 해설:</strong>
                          <p className="text-slate-600 font-medium">{activeQuestion.photoDescriptionKr}</p>
                        </div>
                      </div>

                      {activeQuestion.photoScene?.tags && activeQuestion.photoScene.tags.length > 0 && (
                        <div className="flex flex-wrap gap-1.5 pt-1">
                          {activeQuestion.photoScene.tags.map((t, ti) => (
                            <span key={ti} className="text-[11px] sm:text-xs bg-emerald-50 text-emerald-800 border border-emerald-200 px-2.5 py-1 rounded-lg font-medium">
                              ✓ {t}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              )}

              {/* [요청 2 반영] Part 4 동적 컬럼 표 & 전체 일정표 + 전화 문의자 발화상황 완벽 복원 */}
              {currentPart === 'part4' && activeQuestion.scheduleTable && (
                <div className="border border-slate-200 rounded-2xl overflow-hidden shadow-sm flex flex-col gap-0">
                  <div className="bg-slate-800 text-white p-4 flex justify-between items-center">
                    <div>
                      <span className="text-[10px] text-blue-400 font-bold uppercase tracking-wider">Reference Schedule Table</span>
                      <h4 className="text-sm sm:text-base font-bold mt-0.5">{activeQuestion.scheduleTable.headerTitle || activeQuestion.setTitle}</h4>
                      {activeQuestion.scheduleTable.metaInfo && activeQuestion.scheduleTable.metaInfo.length > 0 && (
                        <div className="flex flex-wrap gap-2 mt-1.5">
                          {activeQuestion.scheduleTable.metaInfo.map((m, mi) => (
                            <span key={mi} className="text-[11px] bg-white/10 px-2 py-0.5 rounded">
                              <strong>{m.label}:</strong> {m.value}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                    <button
                      onClick={() => { setP4ReadingTime(45); setIsP4ReadingActive(!isP4ReadingActive); }}
                      className="px-3 py-1.5 rounded-xl text-xs font-bold bg-white/10 hover:bg-white/20 text-white border border-white/20 shrink-0"
                    >
                      ⏱️ {isP4ReadingActive ? `남은 시간: ${p4ReadingTime}초` : '45초 읽기'}
                    </button>
                  </div>

                  {/* 동적 컬럼 테이블 (모든 세트의 컬럼 누락 방지) */}
                  <div className="overflow-x-auto bg-white">
                    {(() => {
                      const rows = activeQuestion.scheduleTable.rows || [];
                      const colKeys = rows.length > 0 ? Object.keys(rows[0]).filter(k => k !== 'isCancelled') : ['time', 'event', 'location'];
                      return (
                        <table className="w-full text-left text-xs sm:text-sm border-collapse">
                          <thead className="bg-slate-100 border-b border-slate-200 text-slate-600">
                            <tr>
                              {colKeys.map(k => (
                                <th key={k} className="p-3 uppercase font-bold text-[11px]">{k}</th>
                              ))}
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-slate-100">
                            {rows.map((r, ri) => {
                              const isCancelled = Boolean(r.isCancelled || (r.activity && String(r.activity).includes('CANCEL')) || (r.status && String(r.status).includes('CANCEL')));
                              return (
                                <tr key={ri} className={isCancelled ? 'line-through text-slate-400 bg-rose-50/40' : 'hover:bg-slate-50'}>
                                  {colKeys.map(k => (
                                    <td key={k} className={`p-3 ${k === 'time' ? 'font-mono' : k === 'event' || k === 'topic' || k === 'program' ? 'font-bold text-blue-900' : ''}`}>
                                      {String(r[k] || '')}
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

                  {/* 전화 문의자 발화 상황 배너 */}
                  {activeQuestion.context && (
                    <div className="bg-amber-50/80 border-t border-amber-200 p-3.5 flex items-start gap-3">
                      <span className="text-lg">📞</span>
                      <div className="flex flex-col text-xs sm:text-sm">
                        <span className="font-bold text-amber-900">전화 문의자 / 발화 상황:</span>
                        <p className="text-amber-800 italic mt-0.5 font-medium">{activeQuestion.context}</p>
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Question Text Box */}
              <div className="flex flex-col gap-2">
                <div className="flex justify-between items-center">
                  <span className="text-xs font-black text-blue-600 tracking-wider uppercase">QUESTION</span>
                  <div className="flex gap-1.5">
                    <button onClick={() => speakText(activeQuestion.question, 1.0)} className="text-xs font-bold px-3 py-1 bg-white border border-slate-200 rounded-full hover:bg-blue-50 shadow-sm">
                      🔊 1.0x
                    </button>
                    <button onClick={() => speakText(activeQuestion.question, 0.75)} className="text-xs font-bold px-3 py-1 bg-white border border-slate-200 rounded-full hover:bg-amber-50 shadow-sm">
                      🐢 0.75x
                    </button>
                  </div>
                </div>
                <div className="bg-slate-50 border-l-4 border-blue-600 rounded-2xl p-4 sm:p-6 text-slate-900 font-semibold text-base sm:text-lg lg:text-xl leading-relaxed whitespace-pre-line shadow-inner">
                  {activeQuestion.question}
                </div>
              </div>

              {/* Timer Bar */}
              {isExamMode && (
                <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4 flex flex-col gap-2.5">
                  <div className="flex justify-between items-center">
                    <span className="text-xs font-extrabold uppercase px-2.5 py-0.5 rounded-full bg-slate-200 text-slate-700">
                      {timerState.phase === 'prep' ? '⏳ 준비 시간' : timerState.phase === 'response' ? '🎙️ 답변 시간' : '대기 중'}
                    </span>
                    <span className="text-2xl font-black font-mono text-blue-600">{timerState.timeLeft}s</span>
                  </div>
                  <div className="w-full h-2.5 bg-slate-200 rounded-full overflow-hidden">
                    <div className={`h-full transition-all ${timerState.phase === 'response' ? 'bg-emerald-500' : 'bg-amber-500'}`} style={{ width: `${timerState.progressPercent}%` }} />
                  </div>
                  <button onClick={startTimer} disabled={timerState.isRunning} className="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs sm:text-sm font-bold shadow-md disabled:opacity-50 active:scale-98 transition-all">
                    ▶️ 실전 카운트다운 시작
                  </button>
                </div>
              )}

              {/* Center Toggle Button */}
              <div className="flex justify-center">
                <button
                  onClick={() => setIsAnswerVisible(!isAnswerVisible)}
                  className="w-full sm:w-auto px-6 py-3 rounded-2xl text-xs sm:text-sm font-extrabold bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white shadow-lg active:scale-95 transition-all"
                >
                  {isAnswerVisible ? '🙈 모범답안 & 문제해석 접기' : '👁️ 모범답안 & 한국어 상세해설 보기 (Space)'}
                </button>
              </div>

              {/* Model Answer Drawer */}
              {isAnswerVisible && (
                <div className="flex flex-col gap-4 pt-4 border-t border-slate-200 animate-fadeIn">
                  {/* Korean Translation */}
                  <div className="bg-blue-50/80 border border-blue-200 rounded-2xl p-4 text-xs sm:text-sm text-blue-950 whitespace-pre-line leading-relaxed">
                    <span className="font-bold block mb-1 text-blue-900">💡 질문 한국어 상세 해설:</span>
                    {activeQuestion.questionTranslation}
                    {activeQuestion.context_kr && (
                      <div className="mt-2 pt-2 border-t border-blue-200 text-xs text-blue-800">
                        <strong>📞 전화 문의자 발화상황 번역:</strong> {activeQuestion.context_kr}
                      </div>
                    )}
                  </div>

                  {/* Model Answer Content Header */}
                  <div className="flex justify-between items-center">
                    <span className="text-xs font-black text-emerald-700 uppercase">MODEL ANSWER</span>
                    <button onClick={() => speakText(activeQuestion.answer, 1.0)} className="text-xs font-bold px-3 py-1 bg-emerald-50 text-emerald-700 border border-emerald-300 rounded-full">
                      🔊 답안 전체 듣기
                    </button>
                  </div>

                  {/* [요청 3 반영] 문장별 분할 뷰어 (파트 2, 3, 4 모두 개별 발음 버튼 제공) */}
                  <div className="flex flex-col gap-2.5">
                    {structuredSentences.map((sent) => (
                      <div
                        key={sent.index}
                        className="bg-slate-50 hover:bg-blue-50/40 border border-slate-200 rounded-2xl p-3.5 sm:p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 transition-colors"
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
                          <span className="text-xs sm:text-sm font-semibold text-slate-900 leading-relaxed">
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

                  {/* [요청 3 반영: 시계토끼 핵심문장 보라색 카드는 해설에서 완전히 제거됨] */}

                  {/* Vocabulary Chips */}
                  {activeQuestion.vocabulary && activeQuestion.vocabulary.length > 0 && (
                    <div className="bg-white border border-slate-200 rounded-2xl p-4">
                      <span className="text-xs font-bold block mb-2">📖 핵심 어휘 (클릭 시 원어민 발음 재생)</span>
                      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
                        {activeQuestion.vocabulary.map((v, i) => (
                          <div key={i} onClick={() => speakText(v.word, 0.9)} className="bg-slate-50 hover:bg-blue-50 p-2.5 rounded-xl border border-slate-200 flex justify-between items-center cursor-pointer text-xs">
                            <div>
                              <strong className="text-slate-800">{v.word}</strong> <span className="text-slate-400 font-mono">{v.ipa}</span>
                              <div className="text-[11px] text-slate-500">{v.meaning}</div>
                            </div>
                            <span className="text-slate-400">🔊</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Grammar Points */}
                  {activeQuestion.grammarPoints && activeQuestion.grammarPoints.length > 0 && (
                    <div className="bg-amber-50/70 border border-amber-200 rounded-2xl p-4 text-xs">
                      <span className="font-extrabold text-amber-900 block mb-1.5">💡 핵심 문법 및 구문 분석:</span>
                      <div className="flex flex-col gap-2">
                        {activeQuestion.grammarPoints.map((g, gIdx) => (
                          <div key={gIdx} className="bg-white/80 p-2.5 rounded-xl border border-amber-200/50">
                            <strong className="text-amber-900 block">{g.title}</strong>
                            <p className="text-slate-700 mt-0.5">{g.explanation}</p>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Score Tip */}
                  <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-4 text-xs text-emerald-950">
                    <strong className="text-emerald-900 block mb-0.5">🎯 120~140점 핵심 득점 전략:</strong>
                    {activeQuestion.scoreTip}
                  </div>
                </div>
              )}

            </main>

            {/* Footer */}
            <footer className="text-center text-xs text-slate-500 py-2">
              이번 주 토익스피킹 시험, 침묵 없이 만능문장으로 140점(IH) 달성하세요! 🏆
            </footer>

          </div>

          {/* [요청 3 반영] Modal: 시계토끼 만능문장 종합 족보집 (모든 파트 핵심 공식 총집합) */}
          {isCheatSheetOpen && (
            <div className="fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4">
              <div className="bg-white rounded-3xl w-full max-w-xl max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
                <div className="p-4 border-b border-slate-100 flex justify-between items-center bg-slate-50">
                  <h3 className="font-extrabold text-sm sm:text-base">🐰 시계토끼 만능문장 종합 족보집 (모든 파트 공식 집대성)</h3>
                  <button onClick={() => setIsCheatSheetOpen(false)} className="w-7 h-7 rounded-full bg-slate-200 text-xs font-bold">✕</button>
                </div>
                <div className="flex border-b border-slate-200 text-xs font-bold">
                  <button onClick={() => setModalTab('part2')} className={`flex-1 py-2.5 border-b-2 ${modalTab === 'part2' ? 'border-emerald-600 text-emerald-700 bg-emerald-50' : 'text-slate-500'}`}>Part 2 4단계 공식</button>
                  <button onClick={() => setModalTab('part3')} className={`flex-1 py-2.5 border-b-2 ${modalTab === 'part3' ? 'border-blue-600 text-blue-700 bg-blue-50' : 'text-slate-500'}`}>Part 3 7대 만능문장</button>
                  <button onClick={() => setModalTab('part4')} className={`flex-1 py-2.5 border-b-2 ${modalTab === 'part4' ? 'border-purple-600 text-purple-700 bg-purple-50' : 'text-slate-500'}`}>Part 4 Q8~Q10 응답 족보</button>
                </div>
                <div className="p-4 overflow-y-auto flex flex-col gap-2.5 text-xs">
                  {CHEAT_FORMULAS[modalTab].map((f, i) => (
                    <div key={i} className="bg-slate-50 p-3 rounded-xl border border-slate-200">
                      <div className="flex justify-between items-center">
                        <span className="font-bold text-blue-600">{f.topic}</span>
                        <span className="font-mono text-[10px] bg-slate-200 px-2 py-0.5 rounded font-bold">{f.numberTag}</span>
                      </div>
                      <p className="font-mono font-bold text-slate-900 mt-1">{f.formulaEn}</p>
                      <p className="text-slate-500 mt-0.5">{f.formulaKo}</p>
                      {f.extraTip && <p className="text-[11px] text-slate-400 mt-1">📌 {f.extraTip}</p>}
                    </div>
                  ))}
                </div>
                <div className="p-3 border-t border-slate-100 bg-slate-50 flex justify-end">
                  <button onClick={() => setIsCheatSheetOpen(false)} className="px-4 py-1.5 bg-slate-800 text-white rounded-xl text-xs font-bold">닫기</button>
                </div>
              </div>
            </div>
          )}

        </div>
      );
    }

    ReactDOM.createRoot(document.getElementById('root')).render(<App />);
  </script>
</body>
</html>
"""

final_html = html_content.replace('__DATA_JSON_PLACEHOLDER__', data_json_str)

with open('preview_react.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated preview_react.html (Size: {len(final_html):,} bytes)")
