/**
 * ==============================================================================
 * 토익스피킹 파트 2, 3, 4 실전 트레이너 - TypeScript 인터페이스 규약 (types.ts)
 * 
 * [목적]
 * - 프론트엔드 UI 컴포넌트의 상태(State) 및 Props 타입 안정성 확보
 * - 추후 백엔드 REST API / GraphQL 서버 연동 시 DTO 규약으로 1:1 매핑 가능
 * ==============================================================================
 */

// 1. 공통 학습 파트 구분
export type ToeicPart = 'part2' | 'part3' | 'part4';

// 2. 어휘 및 발음기호(IPA) 데이터 모델
export interface VocabularyItem {
  id?: string | number;
  word: string;         // 영단어/숙어 (e.g., "online", "reach for")
  ipa: string;          // 국제 음성 기호 (e.g., "[ˌɒnˈlaɪn]")
  pos: string;          // 품사 (e.g., "형용사", "동사구")
  meaning: string;      // 한국어 번역 의미
  source?: '문제 필수' | '답변 핵심' | '사진 필수' | string; // 출처 라벨
}

// 3. 핵심 문법 및 구문 분석 데이터 모델
export interface GrammarPoint {
  id?: string | number;
  title: string;        // 문법 포인트 제목 (e.g., "구문 핵심: 'The last time S+V was ~'")
  explanation: string;  // 상세 설명 및 감점 방지 팁
}

// 4. 문장 단위 구조화 모델 (답안 내 한 문장씩 읽기/학습 지원)
export interface StructuredSentence {
  index: number;
  en: string;           // 영어 문장
  ko: string;           // 한국어 대역 문장
  highlightPhrases?: string[]; // 강조 만능 문장 패턴
}

// 5. Part 2 전용: 사진 묘사 장면(Scene) 메타데이터
export interface Part2PhotoScene {
  category: string;     // 장면 카테고리 (e.g., "an office", "grocery store")
  locationEn: string;   // 영문 장소 표현 (e.g., "in an office", "at a cafe")
  tags: string[];       // 묘사 키포인트 태그 목록
}

// 6. Part 2 문항 인터페이스
export interface Part2Question {
  id: number;
  part: 'part2';
  setId: number;
  setNumber: number;
  qNumber: string;              // e.g., "Question 3 / 4"
  questionNumber: string;
  setTitle: string;             // e.g., "Set 1: An Office (사무실 업무 사진)"
  prepTime: number;             // 준비시간 (초, 기본 45)
  responseTime: number;         // 답변시간 (초, 기본 30)
  question: string;             // 지시문 (Describe the picture...)
  questionTranslation: string;  // 지시문 한국어 번역
  photoDescriptionKr: string;   // 사진 상세 한국어 묘사 가이드
  photoScene: Part2PhotoScene;  // 사진 분석 세부 요소
  imageUrl: string;             // 이미지 URL (Base64 또는 CDN 링크)
  answer: string;               // 4단계 만능공식 모범답안
  answerTranslation: string;    // 모범답안 한국어 번역
  magicSentences: string[];     // 적용된 시계토끼 만능문장
  scoreTip: string;             // 120~140점 목표 달성 팁
  vocabulary: VocabularyItem[]; // 문항 연계 어휘 목록
  grammarPoints?: GrammarPoint[];// 문법 분석
}

// 7. Part 3 문항 인터페이스 (일상 대화 질문 응답)
export interface Part3Question {
  id: number;
  part: 'part3';
  setId: number;
  setNumber: number;
  qNumber: string;              // e.g., "Question 5", "Question 6", "Question 7"
  questionNumber: string;
  setTitle: string;             // e.g., "Set 1: Online Shopping (온라인 쇼핑)"
  prepTime: number;             // 준비시간 (초, 기본 3)
  responseTime: number;         // 답변시간 (초, 15 또는 30)
  question: string;             // 실제 시험 영어 지문
  questionTranslation: string;  // 질문 한국어 번역
  keyPattern: string;           // 패턴 공식 (e.g., "When + What 의문사 공식")
  answer: string;               // 모범 답안 (개행 구분)
  answerTranslation: string;    // 답안 한국어 번역
  magicSentences: string[];     // 만능문장 하이라이트
  scoreTip: string;             // 120~140점 핵심 전략
  vocabulary: VocabularyItem[]; // 주요 어휘
  grammarPoints?: GrammarPoint[];// 문법 분석
}

// 8. Part 4 전용: 제공된 정보(표/일정표) 데이터 모델
export interface ScheduleTableMeta {
  label: string;                // e.g., "Location", "Admission", "Date"
  value: string;
}

export interface ScheduleTable {
  headerTitle: string;          // 표 상단 타이틀
  metaInfo: ScheduleTableMeta[];// 표 부가 정보
  rows: Record<string, string | boolean | number>[]; // 행 데이터 (동적 컬럼 지원)
}

// 8-1. Part 4 세트 내 개별 질문 인터페이스
export interface Part4QuestionItem {
  id?: number;
  qNumber: string;              // e.g., "Question 8", "Question 9", "Question 10"
  questionNumber?: string;
  prepTime: number;             // 준비시간 (초, 기본 3)
  responseTime: number;         // 답변시간 (초, Q8/Q9: 15초, Q10: 30초)
  question: string;             // 질문 영어 지문
  questionTranslation: string;  // 질문 한국어 번역
  keyPattern: string;           // 답변 패턴
  answer: string;               // 모범답안
  answerTranslation: string;    // 모범답안 번역
  magicSentences: string[];     // 만능문장
  scoreTip: string;             // 고득점 팁
  vocabulary: VocabularyItem[]; // 어휘
  grammarPoints?: GrammarPoint[];// 문법
}

// 8-2. Part 4 복합 세트 인터페이스 (표 1개 + 질문 3개)
export interface Part4Set {
  setNumber: number;
  title: string;                // e.g., "Set 1: Museum Event Schedule"
  topic: string;                // 주제명
  context: string;              // 전화 발화 상황 영문 지문
  context_kr: string;           // 발화 상황 한국어 번역
  table: ScheduleTable;         // 스케줄 표
  questions: Part4QuestionItem[];
}

// 8-3. UI 렌더링 시 일관된 플랫 구조로 평탄화된 Part 4 문항 인터페이스
export interface Part4FlattenedQuestion extends Part4QuestionItem {
  id: number;
  part: 'part4';
  setId: number;
  setNumber: number;
  setTitle: string;
  topic: string;
  context: string;
  context_kr: string;
  table: ScheduleTable;
  qIndexInSet: number;          // 1, 2, 3 (세트 내 몇 번째 질문인지)
}

// 9. 통합 문제 유니온 타입 (Part 2, Part 3, Part 4)
export type AnyToeicQuestion = Part2Question | Part3Question | Part4FlattenedQuestion;

// 10. 만능문장 치트시트 공식 모델
export interface CheatFormula {
  id: string;
  numberTag: string;            // e.g., "공식 1", "P2-1"
  topic: string;                // 주제 (e.g., "스트레스 해소", "장소 도입")
  formulaEn: string;            // 영문 공식
  formulaKo: string;            // 한국어 해석
  extraTip?: string;            // 적용 주제 및 변형 표현
}

// 11. 사용자 프로필 및 학습 진행 상태 모델 (User & Session Info)
export interface UserStudyProfile {
  userId: string;
  userName: string;
  avatarUrl?: string;
  targetScore: string;          // e.g., "120~140점 (IM3 - IH)"
  currentLevel: string;         // e.g., "IM2"
  dDayText: string;             // e.g., "이번 주 일요일 시험 D-5"
  studyStreakDays: number;      // 연속 학습일 (e.g., 7)
  completedQuestionsCount: number;
  bookmarkedQuestionIds: number[];
}

// 12. 전체 마스터 데이터셋 응답 규약 (API 응답 DTO)
export interface MasterToeicDataResponse {
  metadata: {
    version?: string;
    part2_count: number;
    part3_count: number;
    part4_count: number;
    part4_sets_count: number;
  };
  part2: Part2Question[];
  part3: Part3Question[];
  part4: Part4Set[];
  cheatSheets: {
    part2: CheatFormula[];
    part3: CheatFormula[];
    part4: CheatFormula[];
  };
}

// 13. UI 컴포넌트 내부 타이머 상태
export interface TimerState {
  phase: 'idle' | 'prep' | 'response' | 'finished';
  timeLeft: number;
  totalDuration: number;
  progressPercent: number;
  isRunning: boolean;
}
