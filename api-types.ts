/**
 * ==============================================================================
 * 토익스피킹 API 규약 정의 (api-types.ts)
 * 확정된 백엔드(FastAPI) 엔티티 및 DTO 스펙
 * ==============================================================================
 */

export type ToeicPart = 'part2' | 'part3' | 'part4';

export interface VocabularyItem {
  word: string;
  ipa: string;
  pos: string;
  meaning: string;
  source?: '문제 필수' | '답변 핵심' | '사진 필수' | string;
}

export interface GrammarPoint {
  title: string;
  explanation: string;
}

export interface PhotoScene {
  category: string;
  locationEn: string;
  tags: string[];
}

export interface ScheduleTable {
  headerTitle: string;
  metaInfo: { label: string; value: string }[];
  rows: Record<string, string | boolean | number>[];
}

// ----------------------------------------------------
// Entity Models (DB Response)
// ----------------------------------------------------
export interface BaseToeicQuestion {
  id: number;
  setId: number;
  qNumber: string;
  prepTime: number;
  responseTime: number;
  question: string;
  questionTranslation: string;
  answer: string;
  answerTranslation: string;
  magicSentences: string[];
  scoreTip: string;
  vocabulary: VocabularyItem[];
  grammarPoints?: GrammarPoint[];
  createdAt: string;
  updatedAt: string;
}

export interface Part2QuestionResponse extends BaseToeicQuestion {
  part: 'part2';
  imageUrl: string;
  photoScene: PhotoScene;
  photoDescriptionKr?: string; // 사진 1:1 상황 팩트 해설
}

export interface Part3QuestionResponse extends BaseToeicQuestion {
  part: 'part3';
  keyPattern: string;
}

export interface Part4QuestionResponse extends BaseToeicQuestion {
  part: 'part4';
  scheduleTable: ScheduleTable;
  context?: string;       // 영문 전화 발화 상황 지문
  context_kr?: string;    // 발화 상황 한국어 번역
  setTitle?: string;
}

export type ToeicQuestionDetailResponse =
  | Part2QuestionResponse
  | Part3QuestionResponse
  | Part4QuestionResponse;

// ----------------------------------------------------
// Request DTOs
// ----------------------------------------------------
export interface CreateQuestionPayload {
  setId: number;
  part: ToeicPart;
  qNumber: string;
  prepTime: number;
  responseTime: number;
  question: string;
  questionTranslation: string;
  answer: string;
  answerTranslation: string;
  magicSentences?: string[];
  scoreTip: string;
  vocabulary?: VocabularyItem[];
  grammarPoints?: GrammarPoint[];

  // 파트별 선택/필수 필드
  imageUrl?: string;
  photoScene?: PhotoScene;
  keyPattern?: string;
  scheduleTable?: ScheduleTable;
}

export interface UpdateQuestionPayload {
  prepTime?: number;
  responseTime?: number;
  question?: string;
  questionTranslation?: string;
  answer?: string;
  answerTranslation?: string;
  magicSentences?: string[];
  scoreTip?: string;
  vocabulary?: VocabularyItem[];
  grammarPoints?: GrammarPoint[];
  imageUrl?: string;
  photoScene?: PhotoScene;
  keyPattern?: string;
  scheduleTable?: ScheduleTable;
}

export interface QuestionQueryParams {
  part?: ToeicPart;
  setId?: number;
  page?: number;
  limit?: number;
}

// ----------------------------------------------------
// API Response Wrappers
// ----------------------------------------------------
export interface PaginatedResponse<T> {
  total: number;
  page: number;
  limit: number;
  items: T[];
}

export type QuestionListApiResponse = PaginatedResponse<ToeicQuestionDetailResponse>;
