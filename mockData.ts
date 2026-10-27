/**
 * ==============================================================================
 * 토익스피킹 실전 트레이너 - 완성형 Mock Data (mockData.ts)
 * 
 * [목적]
 * - 백엔드 API 연동 전 UI/UX 검증을 위한 신뢰성 있는 실전 모의 데이터 제공
 * - types.ts 인터페이스 규약 준수
 * ==============================================================================
 */

import {
  UserStudyProfile,
  Part2Question,
  Part3Question,
  Part4Set,
  CheatFormula,
} from './types';

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

// 2. Part 2 사진 묘사 Mock Data (대표 세트 2개)
export const MOCK_PART2_QUESTIONS: Part2Question[] = [
  {
    id: 101,
    part: 'part2',
    setId: 1,
    setNumber: 1,
    qNumber: 'Question 3',
    questionNumber: 'Question 3',
    setTitle: 'Set 1: An Office (사무실 2인 업무)',
    prepTime: 45,
    responseTime: 30,
    question: 'Describe the picture on your screen in as much detail as you can.',
    questionTranslation: '화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.',
    photoDescriptionKr: '밝은 오피스에서 두 남성이 나란히 앉아 컴퓨터 작업을 하고 있는 모습입니다. 앞쪽 남성은 안경과 회색 티셔츠를 입고 키보드를 타이핑 중이며, 뒤쪽 남성은 검은 셔츠를 입고 화면을 보고 있습니다.',
    photoScene: {
      category: 'an office',
      locationEn: 'in a modern office',
      tags: [
        '장소: 사무실 (in an office)',
        '전면 남성: 안경 착용 & 키보드 타이핑 (typing on a keyboard)',
        '동료 남성: 나란히 앉아 화면 응시 (working next to him)',
        '주변 사물: 책상 위 스마트폰과 화분 (smartphone and potted plant)'
      ]
    },
    imageUrl: 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80',
    answer: 'This is a picture taken in an office.\nIn the foreground, there is a man wearing glasses and a gray shirt. He is typing on a keyboard while looking at the monitor.\nNext to him, another man is working on his laptop.\nIn the background, large windows let in plenty of natural sunlight.\nOverall, it seems like they are concentrating on their work.',
    answerTranslation: '이 사진은 사무실에서 찍힌 사진입니다.\n앞쪽에는 안경과 회색 셔츠를 입은 남성이 있습니다. 그는 모니터를 보며 키보드로 타이핑하고 있습니다.\n그 옆에는 다른 남성이 노트북으로 작업하고 있습니다.\n배경에는 큰 창문으로 자연광이 쏟아져 들어오고 있습니다.\n전반적으로 그들은 업무에 집중하고 있는 것 같습니다.',
    magicSentences: [
      'This is a picture taken in an office.',
      'He is typing on a keyboard while looking at the monitor.',
      'Overall, it seems like they are concentrating on their work.'
    ],
    scoreTip: '4단계 시계토끼 공식(장소 도입 → 중심 인물 동작 → 주변 사물 → 마무리 총평)을 지키면 30초 안에 무조건 IH를 확보할 수 있습니다.',
    vocabulary: [
      { word: 'concentrate on', ipa: '[ˈkɒnsntreɪt ɒn]', pos: '동사구', meaning: '~에 집중하다', source: '답변 핵심' },
      { word: 'foreground', ipa: '[ˈfɔːɡraʊnd]', pos: '명사', meaning: '(사진 등의) 전경, 앞쪽', source: '사진 필수' },
      { word: 'natural sunlight', ipa: '[ˈnætʃrəl ˈsʌnlaɪt]', pos: '명사구', meaning: '자연 채광', source: '답변 핵심' }
    ],
    grammarPoints: [
      {
        title: '동시 동작 묘사: while + ~ing',
        explanation: 'He is typing on a keyboard while looking at the monitor처럼 while 뒤에 분사(~ing)를 붙이면 문장이 풍부해져 고득점(IH)을 받습니다.'
      }
    ]
  },
  {
    id: 102,
    part: 'part2',
    setId: 2,
    setNumber: 2,
    qNumber: 'Question 4',
    questionNumber: 'Question 4',
    setTitle: 'Set 2: A Supermarket (마트 계산대 풍경)',
    prepTime: 45,
    responseTime: 30,
    question: 'Describe the picture on your screen in as much detail as you can.',
    questionTranslation: '화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.',
    photoDescriptionKr: '슈퍼마켓 계산대에서 고객이 신용카드를 건네고 캐셔가 이를 받는 모습, 카트에는 신선한 식료품이 담겨 있습니다.',
    photoScene: {
      category: 'a supermarket',
      locationEn: 'at a checkout counter in a supermarket',
      tags: [
        '장소: 슈퍼마켓 계산대 (at a checkout counter)',
        '고객: 카드 건네기 (handing over a credit card)',
        '캐셔: 유니폼 착용 & 카드 수령 (receiving the card)',
        '사물: 식료품 카트 (a shopping cart with groceries)'
      ]
    },
    imageUrl: 'https://images.unsplash.com/photo-1578916171728-46686eac8d58?auto=format&fit=crop&w=1200&q=80',
    answer: 'This is a picture taken at a supermarket checkout counter.\nIn the middle, a customer is handing over a credit card to the cashier, and the cashier is smiling.\nOn the conveyor belt, various grocery items are placed.\nIn the background, shelves are fully stocked with packaged goods.\nOverall, it looks like a typical busy shopping day.',
    answerTranslation: '이 사진은 슈퍼마켓 계산대에서 찍힌 사진입니다.\n가운데에는 한 고객이 캐셔에게 신용카드를 건네고 있고 캐셔는 미소 짓고 있습니다.\n컨베이어 벨트 위에는 다양한 식료품이 놓여 있습니다.\n배경에는 선반에 포장 상품들이 가득 채워져 있습니다.\n전반적으로 전형적인 바쁜 쇼핑 날 같습니다.',
    magicSentences: [
      'This is a picture taken at a supermarket checkout counter.',
      'He is handing over a credit card, and she is receiving it.',
      'Overall, it looks like a typical busy shopping day.'
    ],
    scoreTip: '손동작 묘사(handing over / reaching for)는 파트 2 최고 빈출 표현입니다. 주어와 동작을 일치시키세요.',
    vocabulary: [
      { word: 'checkout counter', ipa: '[ˈtʃekaʊt ˈkaʊntə(r)]', pos: '명사', meaning: '계산대', source: '사진 필수' },
      { word: 'hand over', ipa: '[hænd ˈəʊvə(r)]', pos: '동사구', meaning: '건네주다', source: '사진 필수' },
      { word: 'stocked with', ipa: '[stɒkt wɪð]', pos: '형용사구', meaning: '~로 가득 찬', source: '답변 핵심' }
    ]
  }
];

// 3. Part 3 일상 질문 Mock Data (온라인 쇼핑, 대중교통 등 3개 문항)
export const MOCK_PART3_QUESTIONS: Part3Question[] = [
  {
    id: 201,
    part: 'part3',
    setId: 1,
    setNumber: 1,
    qNumber: 'Question 5',
    questionNumber: 'Question 5',
    setTitle: 'Set 1: Online Shopping (온라인 쇼핑)',
    prepTime: 3,
    responseTime: 15,
    question: 'When was the last time you bought clothes online,\nand what did you buy?',
    questionTranslation: '마지막으로 온라인에서 옷을 구매한 것은 언제이고,\n무엇을 샀나요?',
    keyPattern: 'When + What 의문사 공식 (질문 그대로 과거형으로 받아치기)',
    answer: 'The last time I bought clothes online was last week, and I bought a black T-shirt.\n\nIt was very convenient and comfortable.',
    answerTranslation: '마지막으로 온라인에서 옷을 산 것은 지난주였고, 검은색 티셔츠를 샀습니다.\n\n매우 편리하고 편했습니다.',
    magicSentences: [
      'It is very convenient and comfortable. (매우 편리하고 편합니다)'
    ],
    scoreTip: 'The last time I bought clothes online was [시간], and I bought [물건]. 질문을 주어로 받아치고 만능문장 하나만 붙이면 15초가 완성됩니다.',
    vocabulary: [
      { word: 'online', ipa: '[ˌɒnˈlaɪn]', pos: '형용사/부사', meaning: '온라인의, 인터넷상의', source: '문제 필수' },
      { word: 'the last time', ipa: '[ðə lɑːst taɪm]', pos: '명사구', meaning: '마지막으로 ~한 때', source: '문제 필수' },
      { word: 'convenient', ipa: '[kənˈviːniənt]', pos: '형용사', meaning: '편리한, 간편한', source: '답변 핵심' },
      { word: 'comfortable', ipa: '[ˈkʌmftəbl]', pos: '형용사', meaning: '편안한, 안락한', source: '답변 핵심' }
    ],
    grammarPoints: [
      {
        title: "구문 핵심: 'The last time S+V was ~'의 주어-동사 구조",
        explanation: "‘The last time I ~’ 전체가 문장의 주어(명사구) 역할을 하므로, 뒤에 반드시 본동사 'was'가 와야 완전한 문장이 됩니다. (was를 빠뜨리면 문장 불완전으로 감점)"
      },
      {
        title: '시제 일치: 과거 의문문에 대한 과거형 답변',
        explanation: "질문에서 'When was the last time ~'로 과거 시제를 물었으므로, 답변의 동사도 반드시 bought와 was로 일치시켜야 합니다."
      }
    ]
  },
  {
    id: 202,
    part: 'part3',
    setId: 1,
    setNumber: 1,
    qNumber: 'Question 6',
    questionNumber: 'Question 6',
    setTitle: 'Set 1: Online Shopping (온라인 쇼핑)',
    prepTime: 3,
    responseTime: 15,
    question: 'Do you usually read customer reviews before buying products online?\nWhy or why not?',
    questionTranslation: '온라인으로 물건을 사기 전에 보통 고객 리뷰를 읽나요?\n왜 그런가요?',
    keyPattern: 'Yes/No + 이유 (정보 획득 만능문장)',
    answer: 'Yes, I usually read customer reviews before buying products online.\n\nBecause I can get a lot of useful information, and it helps me make a good choice.',
    answerTranslation: '네, 저는 온라인으로 제품을 구매하기 전에 보통 고객 리뷰를 읽습니다.\n\n유용한 정보를 많이 얻을 수 있고, 좋은 선택을 하도록 도와주기 때문입니다.',
    magicSentences: [
      'I can get a lot of useful information. (많은 유용한 정보를 얻을 수 있습니다)'
    ],
    scoreTip: "온라인/인터넷 관련 질문에는 무조건 'I can get a lot of useful information' 만능문장을 사용하세요.",
    vocabulary: [
      { word: 'customer review', ipa: '[ˈkʌstəmə rɪˈvjuː]', pos: '명사구', meaning: '고객 후기, 리뷰', source: '문제 필수' },
      { word: 'useful', ipa: '[ˈjuːsfl]', pos: '형용사', meaning: '유용한, 도움되는', source: '답변 핵심' },
      { word: 'make a choice', ipa: '[meɪk ə tʃɔɪs]', pos: '동사구', meaning: '선택을 하다', source: '답변 핵심' }
    ]
  },
  {
    id: 203,
    part: 'part3',
    setId: 1,
    setNumber: 1,
    qNumber: 'Question 7',
    questionNumber: 'Question 7',
    setTitle: 'Set 1: Online Shopping (온라인 쇼핑)',
    prepTime: 3,
    responseTime: 30,
    question: 'What are the advantages of shopping online compared to in-store shopping?\nGive specific reasons.',
    questionTranslation: '오프라인 매장 쇼핑과 비교했을 때 온라인 쇼핑의 장점은 무엇인가요?\n구체적인 이유를 드세요.',
    keyPattern: '장점 비교 30초 공식 (시간 절약 + 가격 할인 만능문장 2단 결합)',
    answer: 'There are several advantages of shopping online.\n\nFirst, it is much faster, so I can save time. I have a busy daily schedule, so I can order products anytime.\n\nSecond, the prices are cheaper, so I can save money. Online stores offer many discount coupons.\n\nFor these reasons, I prefer online shopping.',
    answerTranslation: '온라인 쇼핑에는 몇 가지 장점이 있습니다.\n\n첫째로, 훨씬 빨라서 시간을 아낄 수 있습니다. 저는 일상 스케줄이 바쁜데 언제든 주문할 수 있습니다.\n\n둘째로, 가격이 더 저렴해서 돈을 절약할 수 있습니다. 온라인 매장은 할인 쿠폰을 많이 제공합니다.\n\n이러한 이유로 저는 온라인 쇼핑을 선호합니다.',
    magicSentences: [
      'It is faster, so I can save time. I have a busy daily routine.',
      'The price is reasonable, so I can save money. I have a tight budget.'
    ],
    scoreTip: '30초 질문(Q7)은 첫째 이유(시간 절약) + 둘째 이유(비용 절약) 만능문장 2개를 이어붙이고 마무리 문장(For these reasons~)을 넣으면 만점입니다.',
    vocabulary: [
      { word: 'advantage', ipa: '[ədˈvɑːntɪdʒ]', pos: '명사', meaning: '이점, 장점', source: '문제 필수' },
      { word: 'save time', ipa: '[seɪv taɪm]', pos: '동사구', meaning: '시간을 아끼다', source: '답변 핵심' },
      { word: 'tight budget', ipa: '[taɪt ˈbʌdʒɪt]', pos: '명사구', meaning: '빠듯한 예산', source: '답변 핵심' }
    ]
  }
];

// 4. Part 4 제공된 정보(표) 보고 답하기 Mock Data
export const MOCK_PART4_SETS: Part4Set[] = [
  {
    setNumber: 1,
    title: 'Set 1: Museum Event Schedule (박물관 5월 행사 일정표)',
    topic: 'Museum Event Schedule',
    context: 'Hello, this is Green Library Museum. I am calling to inquire about the upcoming May events schedule. Could you please answer a few questions?',
    context_kr: '안녕하세요, 그린 박물관입니다. 다가오는 5월 행사 일정에 대해 문의드리고자 전화드렸습니다. 몇 가지 질문에 답해주실 수 있나요?',
    table: {
      headerTitle: 'Green Library Museum - May Event Schedule',
      metaInfo: [
        { label: 'Location', value: 'Main Exhibition Hall & Conference Room B' },
        { label: 'Admission', value: 'Free for museum members ($10 for non-members)' }
      ],
      rows: [
        {
          date: 'May 5',
          time: '10:00 AM',
          event: 'New Collection Introduction',
          location: 'Room 101',
          note: 'Led by Curator David Smith'
        },
        {
          date: 'May 12',
          time: '2:00 PM',
          event: 'Historic Preservation Lecture',
          location: 'Conf. Room B',
          note: 'Guest Speaker Dr. Emily Brown'
        },
        {
          date: 'May 19',
          time: '11:00 AM',
          event: 'Kids Art Workshop (CANCELLED)',
          location: 'Outdoor Plaza',
          note: 'Cancelled due to renovation',
          isCancelled: true
        },
        {
          date: 'May 26',
          time: '3:00 PM',
          event: 'Ancient Sculpture Seminar',
          location: 'Conf. Room B',
          note: 'Led by Dr. Emily Brown'
        }
      ]
    },
    questions: [
      {
        id: 301,
        qNumber: 'Question 8',
        questionNumber: 'Question 8',
        prepTime: 3,
        responseTime: 15,
        question: 'When is the first event scheduled, and what is the event about?',
        questionTranslation: '첫 번째 행사는 언제로 예정되어 있고, 무슨 행사인가요?',
        keyPattern: '첫 행사 일시 + 명칭 응답 공식',
        answer: 'The first event, the New Collection Introduction, will be held on May 5th at 10:00 AM in Room 101.',
        answerTranslation: '첫 번째 행사인 신규 소장품 소개는 5월 5일 오전 10시 101호에서 열릴 예정입니다.',
        magicSentences: [
          'It will be held on [날짜] at [시간].'
        ],
        scoreTip: '행사 안내 시 수동태 전치사 공식(on + 날짜, at + 시간, in + 장소)을 정확하게 지키세요.',
        vocabulary: [
          { word: 'be held on', ipa: '[bi held ɒn]', pos: '동사구', meaning: '~에 개최되다', source: '답변 핵심' },
          { word: 'curator', ipa: '[kjʊˈreɪtə(r)]', pos: '명사', meaning: '큐레이터, 관리인', source: '문제 필수' }
        ]
      },
      {
        id: 302,
        qNumber: 'Question 9',
        questionNumber: 'Question 9',
        prepTime: 3,
        responseTime: 15,
        question: "I heard the Kids Art Workshop is scheduled for May 19th. Is that correct?",
        questionTranslation: '어린이 미술 워크숍이 5월 19일로 예정되어 있다고 들었는데, 맞나요? (취소 여부 확인)',
        keyPattern: '취소/오류 정정 공식 (No, actually~)',
        answer: 'No, actually, that information is not correct.\nThe Kids Art Workshop on May 19th has been cancelled due to renovation.',
        answerTranslation: '아니요, 사실 그 정보는 맞지 않습니다.\n5월 19일 어린이 미술 워크숍은 보수 공사로 인해 취소되었습니다.',
        magicSentences: [
          'No, actually, that information is not correct. It has been cancelled.'
        ],
        scoreTip: '파트 4의 Q9는 80% 확률로 잘못된 정보를 묻는 취소/변경 문제입니다. 당황하지 말고 정중히 바로잡아 주세요.',
        vocabulary: [
          { word: 'cancel', ipa: '[ˈkænsl]', pos: '동사', meaning: '취소하다', source: '문제 필수' },
          { word: 'due to', ipa: '[djuː tu]', pos: '전치사구', meaning: '~때문에', source: '답변 핵심' }
        ]
      },
      {
        id: 303,
        qNumber: 'Question 10',
        questionNumber: 'Question 10',
        prepTime: 3,
        responseTime: 30,
        question: 'I would like to know all the sessions led by Dr. Emily Brown. Could you give me all the details?',
        questionTranslation: 'Emily Brown 박사님이 진행하는 모든 세션을 알고 싶습니다. 세부 일정을 모두 알려주실 수 있나요?',
        keyPattern: '특정 인물 2개 세션 나열 공식 (Sure, there are two scheduled sessions~)',
        answer: 'Sure. There are two scheduled sessions led by Dr. Emily Brown.\n\nFirst, on May 12th at 2:00 PM, she will lead the Historic Preservation Lecture in Conference Room B.\n\nSecond, on May 26th at 3:00 PM, she will give the Ancient Sculpture Seminar in Conference Room B.',
        answerTranslation: '물론입니다. Emily Brown 박사님이 진행하는 세션은 두 개가 예정되어 있습니다.\n\n첫째로, 5월 12일 오후 2시에 회의실 B에서 역사 보존 강의를 진행하실 것입니다.\n\n둘째로, 5월 26일 오후 3시에 회의실 B에서 고대 조각 세미나를 진행하실 것입니다.',
        magicSentences: [
          'Sure, there are two scheduled sessions.',
          'First, on [날짜] at [시간], S + will + V.',
          'Second, on [날짜] at [시간], S + will + V.'
        ],
        scoreTip: 'Q10은 표에서 특정 강사나 주제를 찾아 2개를 또박또박 30초 동안 설명하면 고득점을 받습니다.',
        vocabulary: [
          { word: 'preservation', ipa: '[ˌprezəˈveɪʃn]', pos: '명사', meaning: '보존, 보호', source: '답변 핵심' },
          { word: 'sculpture', ipa: '[ˈskʌlptʃə(r)]', pos: '명사', meaning: '조각상, 조각', source: '문제 필수' }
        ]
      }
    ]
  }
];

// 5. 시계토끼 만능문장 족보집 Mock Data
export const MOCK_CHEAT_SHEETS: {
  part2: CheatFormula[];
  part3: CheatFormula[];
  part4: CheatFormula[];
} = {
  part2: [
    {
      id: 'p2_1',
      numberTag: 'P2-1',
      topic: '장소 도입 공식 (Location)',
      formulaEn: '"This is a picture taken at [a grocery store / an office / a park / indoors]."',
      formulaKo: '이 사진은 [마트/사무실/공원/실내]에서 찍힌 사진입니다.',
      extraTip: '시작 3초 안에 장소를 선언하여 발화 유창성 및 구조적 첫인상을 획득합니다.'
    },
    {
      id: 'p2_2',
      numberTag: 'P2-2',
      topic: '물건 집으려 손 뻗기 (초빈출 손동작)',
      formulaEn: '"He/She is reaching for an item on the shelf."',
      formulaKo: '그/그녀는 선반에 있는 물건을 집으려고 손을 뻗고 있습니다.',
      extraTip: '마트, 도서관, 서점, 옷가게 사진 필수 표현.'
    },
    {
      id: 'p2_3',
      numberTag: 'P2-3',
      topic: '결제 및 카드 건네기/받기',
      formulaEn: '"He is handing over a credit card, and she is receiving it with a smile."',
      formulaKo: '남성은 신용카드를 건네주고 있고, 여성은 미소 지으며 그것을 받고 있습니다.',
      extraTip: '계산대 및 프런트 데스크 대칭 동작 표현.'
    },
    {
      id: 'p2_4',
      numberTag: 'P2-4',
      topic: '사물 진열 및 수동태 묘사',
      formulaEn: '"Products are displayed on the shelves. / Cars are parked in the background."',
      formulaKo: '제품들이 선반에 진열되어 있습니다. / 배경에 차들이 주차되어 있습니다.',
      extraTip: '사람 묘사 후 사물 묘사 시 be + p.p. 수동태 적용.'
    },
    {
      id: 'p2_5',
      numberTag: 'P2-5',
      topic: '마무리 총평 공식 (Closing)',
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
    }
  ],
  part4: [
    {
      id: 'p4_1',
      numberTag: '응답 1',
      topic: '일정/장소 안내 공식 (Q8)',
      formulaEn: '"The [행사명] will be held on [날짜] at [시간] in [장소]."',
      formulaKo: '[행사]는 [날짜] [시간]에 [장소]에서 열릴 예정입니다.',
      extraTip: '전치사 짝꿍: on + 날짜, at + 시간, in + 장소.'
    },
    {
      id: 'p4_2',
      numberTag: '응답 2',
      topic: '오류 정정 및 취소 통보 공식 (Q9)',
      formulaEn: '"No, actually, that information is not correct. It has been cancelled due to [이유]."',
      formulaKo: '아니요, 사실 그 정보는 맞지 않습니다. [이유]로 인해 취소되었습니다.',
      extraTip: '정중한 거절 표현(No, actually) 후 변경/취소 사실 명시.'
    },
    {
      id: 'p4_3',
      numberTag: '응답 3',
      topic: '복수 세션 순차 안내 공식 (Q10)',
      formulaEn: '"Sure, there are two scheduled sessions. First, ~ Second, ~"',
      formulaKo: '물론입니다. 2개의 예정된 세션이 있습니다. 첫째로 ~, 둘째로 ~',
      extraTip: '도입 문장으로 시간을 벌고 First와 Second로 분할하여 안정적으로 30초 채우기.'
    }
  ]
};
