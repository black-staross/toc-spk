/**
 * ==============================================================================
 * FastAPI 백엔드 연동 클라이언트 서비스 (api.ts)
 * 
 * [주요 기능]
 * - Base URL 환경변수 (VITE_API_BASE_URL) 및 타임아웃 (10초) 제어
 * - HTTP 상태 코드 및 비정상 응답에 대한 표준화된 ApiError 클래스
 * - GET, POST, PUT, DELETE 메서드 추상화
 * ==============================================================================
 */

import {
  ToeicQuestionDetailResponse,
  QuestionListApiResponse,
  QuestionQueryParams,
  CreateQuestionPayload,
  UpdateQuestionPayload,
} from './api-types';

// 기본 API 서버 주소 (FastAPI 기본 포트 8000)
const API_BASE_URL =
  (typeof import.meta !== 'undefined' && import.meta.env?.VITE_API_BASE_URL) ||
  'http://localhost:8000/api/v1';

/**
 * 표준 API 에러 클래스 (UI 에러 바운더리 및 에러 상태 뷰어용)
 */
export class ApiError extends Error {
  status?: number;
  statusCodeText?: string;
  isNetworkError: boolean;
  endpoint: string;

  constructor(message: string, status?: number, endpoint: string = '', isNetworkError: boolean = false) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.endpoint = endpoint;
    this.isNetworkError = isNetworkError;

    if (status === 404) this.statusCodeText = '404 Not Found (문제를 찾을 수 없습니다)';
    else if (status === 500) this.statusCodeText = '500 Internal Server Error (서버 오류)';
    else if (status === 503) this.statusCodeText = '503 Service Unavailable (서버 점검 중)';
    else if (isNetworkError) this.statusCodeText = 'Network Connection Failed (서버 연결 불가)';
    else this.statusCodeText = `HTTP Status: ${status || 'Unknown'}`;
  }
}

/**
 * fetch 통신 래퍼 함수 (타임아웃 및 에러 파싱 내장)
 */
async function request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const url = `${API_BASE_URL}${endpoint}`;
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 10000); // 10초 타임아웃

  try {
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
        ...(options.headers || {}),
      },
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      let errorDetail = `서버 응답 오류 (HTTP ${response.status})`;
      try {
        const errorBody = await response.json();
        if (errorBody && errorBody.detail) {
          errorDetail = typeof errorBody.detail === 'string' ? errorBody.detail : JSON.stringify(errorBody.detail);
        }
      } catch {
        // JSON 파싱 불가 시 텍스트 본문 추출
        const rawText = await response.text();
        if (rawText) errorDetail = rawText;
      }
      throw new ApiError(errorDetail, response.status, endpoint, false);
    }

    // 204 No Content 대응
    if (response.status === 204) {
      return {} as T;
    }

    return await response.json();
  } catch (err: unknown) {
    clearTimeout(timeoutId);

    if (err instanceof ApiError) {
      throw err;
    }

    if (err instanceof DOMException && err.name === 'AbortError') {
      throw new ApiError('서버 응답 시간이 초과되었습니다 (10초 타임아웃).', 408, endpoint, true);
    }

    const networkMsg =
      `FastAPI 백엔드 서버(${API_BASE_URL})에 연결할 수 없습니다. 서버 실행 여부와 CORS 설정을 확인해 주세요.`;
    throw new ApiError(networkMsg, 0, endpoint, true);
  }
}

/**
 * 1. 문제 목록 조회 API (GET /questions)
 */
export async function getQuestions(params: QuestionQueryParams = {}): Promise<QuestionListApiResponse> {
  const query = new URLSearchParams();
  if (params.part) query.append('part', params.part);
  if (params.setId !== undefined) query.append('setId', String(params.setId));
  if (params.page !== undefined) query.append('page', String(params.page));
  if (params.limit !== undefined) query.append('limit', String(params.limit));

  const queryString = query.toString();
  const endpoint = `/questions${queryString ? `?${queryString}` : ''}`;
  return request<QuestionListApiResponse>(endpoint, { method: 'GET' });
}

/**
 * 2. 특정 문제 상세 조회 API (GET /questions/{id})
 */
export async function getQuestionById(id: number): Promise<ToeicQuestionDetailResponse> {
  return request<ToeicQuestionDetailResponse>(`/questions/${id}`, { method: 'GET' });
}

/**
 * 3. 신규 문제 등록 API (POST /questions)
 */
export async function createQuestion(payload: CreateQuestionPayload): Promise<ToeicQuestionDetailResponse> {
  return request<ToeicQuestionDetailResponse>('/questions', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

/**
 * 4. 문제 수정 API (PUT /questions/{id})
 */
export async function updateQuestion(id: number, payload: UpdateQuestionPayload): Promise<ToeicQuestionDetailResponse> {
  return request<ToeicQuestionDetailResponse>(`/questions/${id}`, {
    method: 'PUT',
    body: JSON.stringify(payload),
  });
}

/**
 * 5. 문제 삭제 API (DELETE /questions/{id})
 */
export async function deleteQuestion(id: number): Promise<void> {
  return request<void>(`/questions/${id}`, { method: 'DELETE' });
}
