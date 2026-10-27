/**
 * ==============================================================================
 * 토익스피킹 실전 마스터 데이터셋 (mockData.ts)
 * 
 * [데이터 구성]
 * - Part 2 사진 묘사: 총 26세트 (고화질 실사 사진 및 4단계 묘사 공식)
 * - Part 3 일상 질문: 총 48문항 (16개 테마 세트 x 3문항)
 * - Part 4 표 분석: 총 24문항 (8개 세트 x 3문항, 동적 컬럼 & 전화 문의자 상황 탑재)
 * - 총 98개 실전 기출 문항 및 어휘/IPA/문법분석 100% 탑재
 * - 시계토끼 종합 만능족보집 대폭 보강
 * ==============================================================================
 */

import masterRawData from './data.json';
import {
  ToeicQuestionDetailResponse,
  Part2QuestionResponse,
  Part3QuestionResponse,
  Part4QuestionResponse,
  UserStudyProfile,
  CheatFormula
} from './api-types';

// 1. 사용자 학습 정보 Mock Data
export const MOCK_USER_PROFILE: UserStudyProfile = {
  userId: 'user_toeic_778',
  userName: '박상현',
  targetScore: '120 ~ 140점 (IM3 - IH)',
  currentLevel: 'IM2 (110점)',
  dDayText: '이번 주 일요일 시험 D-5',
  studyStreakDays: 7,
  completedQuestionsCount: 18,
  bookmarkedQuestionIds: [1, 2, 5],
};

// 2. Part 2 전체 26문항 (고화질 실사 사진 매핑)
export const MOCK_PART2_QUESTIONS: Part2QuestionResponse[] = (masterRawData.part2 || []).map((q: any) => ({
  id: q.id || q.setId || 100,
  part: 'part2' as const,
  setId: q.setId || q.setNumber || 1,
  qNumber: q.qNumber || q.questionNumber || 'Question 3',
  prepTime: q.prepTime || 45,
  responseTime: q.responseTime || 30,
  question: q.question || 'Describe the picture on your screen in as much detail as you can.',
  questionTranslation: q.questionTranslation || '화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.',
  imageUrl: q.imageUrl,
  photoScene: q.photoScene || {
    category: 'photo',
    locationEn: 'in the picture',
    tags: ['장소 묘사', '인물 동작', '배경 및 사물']
  },
  photoDescriptionKr: q.photoDescriptionKr || '',
  answer: q.answer || '',
  answerTranslation: q.answerTranslation || '',
  magicSentences: q.magicSentences || [],
  scoreTip: q.scoreTip || '4단계 시계토끼 공식(장소 → 중심 인물 → 주변 → 마무리 총평)으로 30초를 완성하세요.',
  vocabulary: q.vocabulary || [],
  grammarPoints: q.grammarPoints || [],
  createdAt: new Date().toISOString(),
  updatedAt: new Date().toISOString(),
}));

// 3. Part 3 전체 48문항 (16개 테마 세트)
export const MOCK_PART3_QUESTIONS: Part3QuestionResponse[] = (masterRawData.part3 || []).map((q: any) => ({
  id: q.id,
  part: 'part3' as const,
  setId: q.setId || q.setNumber || 1,
  qNumber: q.qNumber || q.questionNumber || 'Question 5',
  prepTime: q.prepTime || 3,
  responseTime: q.responseTime || 15,
  question: q.question || '',
  questionTranslation: q.questionTranslation || '',
  keyPattern: q.keyPattern || '의문사 패턴 공식',
  answer: q.answer || '',
  answerTranslation: q.answerTranslation || '',
  magicSentences: q.magicSentences || [],
  scoreTip: q.scoreTip || '질문을 주어로 받아치고 만능문장을 붙여 15초/30초를 채우세요.',
  vocabulary: q.vocabulary || [],
  grammarPoints: q.grammarPoints || [],
  createdAt: new Date().toISOString(),
  updatedAt: new Date().toISOString(),
}));

// 4. Part 4 전체 24문항 (8개 세트 x 3문항, context 및 table 동적 완벽 매핑)
export const MOCK_PART4_SETS: any[] = masterRawData.part4 || [];

export const MOCK_PART4_QUESTIONS: Part4QuestionResponse[] = MOCK_PART4_SETS.flatMap((set: any) =>
  (set.questions || []).map((q: any, idx: number) => ({
    id: q.id || set.setNumber * 10 + (idx + 1),
    part: 'part4' as const,
    setId: set.setNumber,
    setTitle: set.title,
    qNumber: q.qNumber || q.questionNumber || `Question ${8 + idx}`,
    prepTime: q.prepTime || 3,
    responseTime: q.responseTime || (idx === 2 ? 30 : 15),
    question: q.question || '',
    questionTranslation: q.questionTranslation || '',
    answer: q.answer || '',
    answerTranslation: q.answerTranslation || '',
    magicSentences: q.magicSentences || [],
    scoreTip: q.scoreTip || '표에 제공된 정보를 정확한 전치사(on + 날짜, at + 시간, in + 장소)와 함께 응답하세요.',
    vocabulary: q.vocabulary || [],
    grammarPoints: q.grammarPoints || [],
    scheduleTable: set.table || { headerTitle: set.title, metaInfo: [], rows: [] },
    context: set.context || '',
    context_kr: set.context_kr || '',
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  }))
);

// 5. 전체 98개 문항 통합 배열
export const FULL_MASTER_QUESTIONS: ToeicQuestionDetailResponse[] = [
  ...MOCK_PART2_QUESTIONS,
  ...MOCK_PART3_QUESTIONS,
  ...MOCK_PART4_QUESTIONS,
];

// 6. 시계토끼 만능문장 종합 족보집 (모든 핵심 공식 집중 집약)
export const MOCK_CHEAT_SHEETS: {
  part2: CheatFormula[];
  part3: CheatFormula[];
  part4: CheatFormula[];
} = {
  part2: [
    {
      id: 'p2_1',
      numberTag: 'P2-1',
      topic: '1단계: 장소 도입 공식 (Location)',
      formulaEn: '"This is a picture taken at [a grocery store / an office / a park / indoors]."',
      formulaKo: '이 사진은 [마트/사무실/공원/실내]에서 찍힌 사진입니다.',
      extraTip: '시작 3초 안에 장소를 선언하여 발화 유창성 및 구조적 첫인상을 획득합니다.'
    },
    {
      id: 'p2_2',
      numberTag: 'P2-2',
      topic: '2단계: 손 뻗기 동작 (초빈출 손동작)',
      formulaEn: '"He/She is reaching for an item on the shelf."',
      formulaKo: '그/그녀는 선반에 있는 물건을 집으려고 손을 뻗고 있습니다.',
      extraTip: '마트, 도서관, 서점, 옷가게 사진 필수 표현.'
    },
    {
      id: 'p2_3',
      numberTag: 'P2-3',
      topic: '2단계: 결제 및 카드 건네기 / 받기',
      formulaEn: '"He is handing over a credit card, and she is receiving it with a smile."',
      formulaKo: '남성은 신용카드를 건네주고 있고, 여성은 미소 지으며 그것을 받고 있습니다.',
      extraTip: '계산대 및 프런트 데스크 대칭 동작 표현.'
    },
    {
      id: 'p2_4',
      numberTag: 'P2-4',
      topic: '2단계: 전자기기 타이핑 및 통화하기',
      formulaEn: '"He is typing on a keyboard while talking on the phone."',
      formulaKo: '그는 전화 통화를 하면서 키보드를 타이핑하고 있습니다.',
      extraTip: 'while + ~ing 동시 동작 구문으로 고득점(IH) 확보.'
    },
    {
      id: 'p2_5',
      numberTag: 'P2-5',
      topic: '3단계: 사물 진열 및 주차 (수동태 묘사)',
      formulaEn: '"Products are displayed on the shelves. / Cars are parked in the background."',
      formulaKo: '제품들이 선반에 진열되어 있습니다. / 배경에 차들이 주차되어 있습니다.',
      extraTip: '사람 묘사 후 사물 묘사 시 be + p.p. 수동태 적용.'
    },
    {
      id: 'p2_6',
      numberTag: 'P2-6',
      topic: '4단계: 마무리 총평 공식 (Closing)',
      formulaEn: '"Overall, it seems like they are busy. / Overall, it seems like a peaceful day."',
      formulaKo: '전반적으로 그들은 바빠 보입니다. / 평화로운 날 같습니다.',
      extraTip: '남은 3~5초 동안 침묵 없이 감점 없이 깔끔하게 매듭짓기.'
    }
  ],
  part3: [
    {
      id: 'p3_1',
      numberTag: '공식 1',
      topic: '스트레스 해소 & 기분 전환',
      formulaEn: '"It relieves my stress. I am stressed out these days, so I need this."',
      formulaKo: '스트레스를 풀어줍니다. 요즘 스트레스가 많아서 이게 필요해요.',
      extraTip: '취미, 운동, 음악, 영화, 외식 등 거의 모든 여가 질문에 적용 가능.'
    },
    {
      id: 'p3_2',
      numberTag: '공식 2',
      topic: '시간 절약 & 바쁜 일상',
      formulaEn: '"It is faster, so I can save time. I have a busy daily routine."',
      formulaKo: '더 빨라서 시간을 아낄 수 있습니다. 저는 일상이 바빠요.',
      extraTip: '온라인 쇼핑, 지하철, 배달 음식, 모바일 뱅킹 단골 템플릿.'
    },
    {
      id: 'p3_3',
      numberTag: '공식 3',
      topic: '비용 절약 & 빠듯한 예산',
      formulaEn: '"The price is reasonable, so I can save money. I have a tight budget."',
      formulaKo: '가격이 합리적이라 돈을 아낄 수 있습니다. 요즘 예산이 빠듯해요.',
      extraTip: '할인 행사, 대중교통 이용, 도서관, 가성비 제품 질문에 최적.'
    },
    {
      id: 'p3_4',
      numberTag: '공식 4',
      topic: '유용한 정보 획득 & 솔직 후기',
      formulaEn: '"I can get a lot of useful information on the Internet and social media."',
      formulaKo: '인터넷과 SNS에서 많은 유용한 정보를 얻을 수 있습니다.',
      extraTip: '리뷰 읽기, 웹 검색, 스마트폰 앱 사용 질문에 100% 매칭.'
    },
    {
      id: 'p3_5',
      numberTag: '공식 5',
      topic: '편리함 & 언제 어디서나',
      formulaEn: '"It is very convenient because I can do it anytime and anywhere."',
      formulaKo: '언제 어디서나 할 수 있어서 매우 편리합니다.',
      extraTip: 'OTT, 전자책, 스마트폰, 배송 서비스 질문에 적용.'
    },
    {
      id: 'p3_6',
      numberTag: '공식 6',
      topic: '친구/가족과의 친목 & 추억 만들기',
      formulaEn: '"I can spend quality time with my friends and make good memories."',
      formulaKo: '친구들과 소중한 시간을 보내고 좋은 추억을 만들 수 있습니다.',
      extraTip: '카페, 여행, 콘서트, 맛집 외식, 영화관 질문에 적용.'
    },
    {
      id: 'p3_7',
      numberTag: '공식 7',
      topic: '건강 증진 & 체력 유지',
      formulaEn: '"It is good for my health, and it helps me stay healthy and active."',
      formulaKo: '건강에 좋고, 건강하고 활동적으로 지내는 데 도움이 됩니다.',
      extraTip: '운동, 산책, 신선한 식료품, 집밥 요리 질문에 적용.'
    }
  ],
  part4: [
    {
      id: 'p4_1',
      numberTag: 'Q8 공식',
      topic: '일정/장소 기본 안내 공식 (Q8 - 15초)',
      formulaEn: '"The [행사명] will be held on [날짜] at [시간] in [장소]."',
      formulaKo: '[행사]는 [날짜] [시간]에 [장소]에서 열릴 예정입니다.',
      extraTip: '전치사 짝꿍: on + 날짜, at + 시간, in + 장소.'
    },
    {
      id: 'p4_2',
      numberTag: 'Q9 공식',
      topic: '오류 정정 및 취소 통보 공식 (Q9 - 15초)',
      formulaEn: '"No, actually, that information is not correct. It has been cancelled due to [이유]."',
      formulaKo: '아니요, 사실 그 정보는 맞지 않습니다. [이유]로 인해 취소되었습니다.',
      extraTip: '정중한 거절 표현(No, actually) 후 변경/취소 사실 명시 (취소선 행 확인).'
    },
    {
      id: 'p4_3',
      numberTag: 'Q10 공식',
      topic: '복수 세션 순차 나열 공식 (Q10 - 30초)',
      formulaEn: '"Sure, there are two scheduled sessions. First, on [날짜] at [시간], ~ Second, on [날짜] at [시간], ~"',
      formulaKo: '물론입니다. 2개의 예정된 세션이 있습니다. 첫째로 ~, 둘째로 ~',
      extraTip: '도입 문장으로 시간을 벌고 First와 Second로 분할하여 안정적으로 30초 채우기.'
    }
  ]
};
