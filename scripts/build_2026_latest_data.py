#!/usr/bin/env python3
"""
scripts/build_2026_latest_data.py
2026년 9월, 10월, 11월 극최신 토익스피킹 기출 복원 모의고사 3종 데이터 빌더
"""

import json
import os

LATEST_2026_DATA = [
    # =========================================================================
    # [2026년 11월 극최신 기출] 그웬 토익스피킹 복원 모의고사 (HITVVr0g-Go)
    # =========================================================================
    {
        "id": 20261101,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 22,
        "part": 1,
        "qNumber": "Question 1",
        "title": "Part 1 지문 읽기 (쇼핑몰 안내 방송)",
        "prep_time": 45,
        "response_time": 45,
        "question_text": "Welcome to the grand reopening of Westlake Shopping Pavilion. We have completely renovated our interior to offer you a brighter and more convenient shopping atmosphere. Please visit our newly opened organic cafe on the second floor for fresh pastries, smoothies, and artisan coffee. Don't forget that special discounts will be offered throughout this weekend.",
        "question_translation": "웨스트레이크 쇼핑 파빌리온의 그랜드 리오프닝에 오신 것을 환영합니다. 더욱 밝고 편리한 쇼핑 분위기를 제공해 드리고자 내부를 완전히 리모델링했습니다. 2층에 새로 오픈한 유기농 카페에 방문하시어 신선한 페이스트리, 스무디, 그리고 수제 커피를 즐겨보세요. 이번 주말 동안 특별 할인이 제공된다는 점을 잊지 마세요.",
        "model_answer": "Welcome to the grand reopening of Westlake Shopping Pavilion. We have completely renovated our interior to offer you a brighter and more convenient shopping atmosphere. Please visit our newly opened organic cafe on the second floor for fresh pastries, smoothies, and artisan coffee. Don't forget that special discounts will be offered throughout this weekend.",
        "score_tip": "pastries, smoothies, and artisan coffee의 병렬 구조에서 A↗, B↗, and C↘ 억양을 명확히 살리고 renovated, atmosphere의 강세를 주의하세요.",
        "vocabulary": [
            {"word": "renovate", "ipa": "[ˈrenəveɪt]", "meaning": "개조하다, 보수하다"},
            {"word": "atmosphere", "ipa": "[ˈætməsfɪər]", "meaning": "분위기, 환경"},
            {"word": "artisan", "ipa": "[ˌɑːrtəˈzæn]", "meaning": "장인의, 수제의"}
        ]
    },
    {
        "id": 20261102,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 223,
        "part": 2,
        "qNumber": "Question 3",
        "title": "Part 2 사진 묘사 (도심 자전거 도로와 보행자들)",
        "prep_time": 45,
        "response_time": 30,
        "image_url": "toeic_part2_images/part2_q01_photo.jpg",
        "question_text": "Describe the picture on your screen in as much detail as you can.",
        "question_translation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "model_answer": "This picture was taken outdoors on a busy city street. In the center, a woman wearing a helmet is riding a bicycle along the bike lane. On the sidewalk to the right, several pedestrians are walking while carrying backpacks. In the background, tall modern office buildings and lush green trees line the street under a clear blue sky. Overall, the atmosphere seems active and peaceful.",
        "score_tip": "장소 도입 ➔ 중심 인물(자전거 타는 여성) ➔ 주변 보행자 ➔ 배경 건물 순서로 30초 안에 4문장으로 깔끔하게 끊어 말하세요.",
        "vocabulary": [
            {"word": "pedestrian", "ipa": "[pəˈdestriən]", "meaning": "보행자"},
            {"word": "bike lane", "ipa": "[baɪk leɪn]", "meaning": "자전거 전용 도로"},
            {"word": "lush", "ipa": "[lʌʃ]", "meaning": "푸르고 무성한"}
        ]
    },
    {
        "id": 20261103,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 416,
        "part": 3,
        "qNumber": "Question 5",
        "title": "Part 3 일상 질문 (간식 섭취 빈도 및 종류)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Imagine that an English newspaper company is conducting research for an article about people's snacking habits and preferences.",
        "question_text": "How often do you eat snacks? What kinds of snacks do you usually eat?",
        "question_translation": "얼마나 자주 간식을 드시나요? 주로 어떤 종류의 간식을 드시나요?",
        "model_answer": "I usually eat snacks once or twice a day, mostly in the afternoon. I prefer light and healthy snacks like fresh fruits, almonds, or yogurt because they give me quick energy without feeling heavy.",
        "score_tip": "I usually eat snacks [빈도], and I like to eat [종류] because [이유]. 질문의 시제와 단어를 그대로 받아쳐 시작하세요.",
        "vocabulary": [
            {"word": "snacking habits", "ipa": "[ˈsnækɪŋ ˈhæbɪts]", "meaning": "간식 섭취 습관"},
            {"word": "preference", "ipa": "[ˈprefrəns]", "meaning": "선호, 기호"}
        ]
    },
    {
        "id": 20261104,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 457,
        "part": 3,
        "qNumber": "Question 6",
        "title": "Part 3 일상 질문 (영화 볼 때 간식 먹기)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Imagine that an English newspaper company is conducting research for an article about people's snacking habits and preferences.",
        "question_text": "Do you like eating snacks while watching a movie? Why or why not?",
        "question_translation": "영화를 볼 때 간식 먹는 것을 좋아하시나요? 왜 그런가요?",
        "model_answer": "Yes, I really enjoy eating snacks while watching a movie. Having popcorn or chips makes the movie-watching experience much more fun and exciting, especially when I am with friends.",
        "score_tip": "Yes, I really enjoy ~ 로 바로 답변을 내놓고 감각적인 이유(more fun and exciting)를 덧붙이세요.",
        "vocabulary": [
            {"word": "movie-watching experience", "ipa": "[ˈmuːvi ˈwɑːtʃɪŋ ɪkˈspɪriəns]", "meaning": "영화 관람 경험"}
        ]
    },
    {
        "id": 20261105,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 495,
        "part": 3,
        "qNumber": "Question 7",
        "title": "Part 3 일상 질문 (간식 구매 vs 직접 만들기)",
        "prep_time": 3,
        "response_time": 30,
        "context": "Imagine that an English newspaper company is conducting research for an article about people's snacking habits and preferences.",
        "question_text": "Do you prefer buying snacks or making your own? Why?",
        "question_translation": "간식을 사서 먹는 것과 직접 만들어 먹는 것 중 어느 쪽을 선호하시나요? 왜 그런가요?",
        "model_answer": "I definitely prefer buying snacks rather than making my own. First of all, it is much more convenient and saves a lot of time because I have a busy daily schedule. Also, convenience stores and bakeries offer a huge variety of delicious snacks that are hard to make at home. Therefore, buying snacks is the best option for me.",
        "score_tip": "30초 문항은 서론(I prefer buying) ➔ First of all(시간 절약) ➔ Also(다양한 종류) ➔ Therefore(결론) 4단계 구조로 전개하세요.",
        "vocabulary": [
            {"word": "convenient", "ipa": "[kənˈviːniənt]", "meaning": "편리한, 간편한"},
            {"word": "a variety of", "ipa": "[ə vəˈraɪəti əv]", "meaning": "다양한"}
        ]
    },
    {
        "id": 20261106,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 611,
        "part": 4,
        "qNumber": "Question 8",
        "title": "Part 4 표 분석 (Brookfield 11월 마지막 행사)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Hello, my name is Harry Wilson and I'm interested in attending some community events in Brookfield this November. I recently heard about the city's cultural events calendar, but I haven't had a chance to look at it yet. Could you please answer a few questions for me?",
        "table_title": "Brookfield November Cultural Events Calendar",
        "question_text": "What is the last event scheduled for November? When and where will it take place?",
        "question_translation": "11월에 예정된 마지막 행사는 무엇인가요? 언제, 어디서 열리나요?",
        "model_answer": "The last event scheduled for November is the Winter Lights Ceremony. It will take place on Saturday, November 28th, from 6:00 PM to 8:30 PM at Brookfield Central Square.",
        "score_tip": "The last event scheduled is [행사명]. It will be held on [날짜] at [장소]. 전치사 on과 at을 정확히 구사하세요.",
        "vocabulary": [
            {"word": "take place", "ipa": "[teɪk pleɪs]", "meaning": "개최되다, 열리다"}
        ]
    },
    {
        "id": 20261107,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 639,
        "part": 4,
        "qNumber": "Question 9",
        "title": "Part 4 표 분석 (오류 정정: 공예 페어 날짜 확인)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Hello, my name is Harry Wilson and I'm interested in attending some community events in Brookfield this November.",
        "table_title": "Brookfield November Cultural Events Calendar",
        "question_text": "I was told that the autumn food and craft fair will be held on November 12th. Is that correct?",
        "question_translation": "가을 음식 및 공예 페어가 11월 12일에 열린다고 들었는데, 맞나요?",
        "model_answer": "I'm afraid you have the incorrect information. The Autumn Food and Craft Fair is actually scheduled for Sunday, November 15th, from 10:00 AM to 4:00 PM at Riverside Community Center.",
        "score_tip": "Question 9의 대표적인 오류 정정 공식인 'I'm afraid that's not correct. Actually, ~'를 활용하세요.",
        "vocabulary": [
            {"word": "I'm afraid that", "ipa": "[aɪm əˈfreɪd ðæt]", "meaning": "유감스럽게도 ~입니다 (정중한 거절/정정)"}
        ]
    },
    {
        "id": 20261108,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 681,
        "part": 4,
        "qNumber": "Question 10",
        "title": "Part 4 표 분석 (음악 관련 모든 세션 안내)",
        "prep_time": 3,
        "response_time": 30,
        "context": "Hello, my name is Harry Wilson and I'm interested in attending some community events in Brookfield this November.",
        "table_title": "Brookfield November Cultural Events Calendar",
        "question_text": "I'm particularly interested in music. Could you please tell me about all the music related events scheduled for November?",
        "question_translation": "제가 음악에 특별히 관심이 많은데요. 11월에 예정된 모든 음악 관련 행사에 대해 말씀해 주시겠어요?",
        "model_answer": "Sure, there are two music-related events scheduled. First, on Friday, November 6th, there will be a Classical String Quartet Concert at the Symphony Hall from 7:00 PM. Second, on Friday, November 20th, a Jazz in the Park Festival is scheduled at the Waterfront Pavilion starting at 5:00 PM.",
        "score_tip": "30초 문항은 'Sure, there are two scheduled events.'로 시작하고 First, on [날짜] ~, Second, on [날짜] ~ 로 2개를 차례로 설명하세요.",
        "vocabulary": [
            {"word": "particularly", "ipa": "[pərˈtɪkjələrli]", "meaning": "특히, 유독"}
        ]
    },
    {
        "id": 20261109,
        "exam_date": "2026년 11월",
        "source_title": "2026년 11월 토익스피킹 최신 시험 복원 모의고사 (그웬)",
        "youtube_video_id": "HITVVr0g-Go",
        "youtube_timestamp": 737,
        "part": 5,
        "qNumber": "Question 11",
        "title": "Part 5 의견 제시 (투어 가이드의 지역 역사/문화 지식 중요성)",
        "prep_time": 45,
        "response_time": 60,
        "question_text": "Do you agree or disagree that having extensive knowledge about local history and culture is important for being a good tour guide? Why or why not? Give specific reasons and examples to support your opinion.",
        "question_translation": "훌륭한 관광 가이드가 되기 위해 지역의 역사와 문화에 대한 광범위한 지식을 갖추는 것이 중요하다는 의견에 동의하십니까, 아니면 반대하십니까? 구체적인 이유와 사례를 들어 의견을 뒷받침하세요.",
        "model_answer": "I strongly agree that having extensive knowledge about local history and culture is essential for being a good tour guide. First of all, tourists visit new places to learn authentic stories and historical context behind famous landmarks. When a tour guide can explain interesting historical facts in detail, it makes the travel experience much more meaningful and memorable. Second, knowledgeable guides can answer unexpected questions from tourists with confidence, which builds great trust and satisfaction. In my own experience, when I visited Rome, the local guide shared fascinating historical anecdotes about the Colosseum, which made the trip unforgettable. For these reasons, I believe comprehensive cultural knowledge is the most crucial quality for a guide.",
        "score_tip": "서론(I strongly agree) ➔ 근거1(관광객의 진정한 학습 니즈) ➔ 근거2(신뢰와 만족도) ➔ 개인 경험(Rome 여행 사례) ➔ 결론(For these reasons)의 60초 만점 템플릿입니다.",
        "vocabulary": [
            {"word": "extensive knowledge", "ipa": "[ɪkˈstensɪv ˈnɑːlɪdʒ]", "meaning": "광범위한 지식"},
            {"word": "authentic", "ipa": "[ɔːˈθentɪk]", "meaning": "진정한, 진짜의"},
            {"word": "anecdote", "ipa": "[ˈænɪkdoʊt]", "meaning": "일화, 비하인드 스토리"}
        ]
    },

    # =========================================================================
    # [2026년 10월 극최신 기출] 지나쌤 최신 기출 반영 모의고사 20 (Vk6-5HyWI_Y)
    # =========================================================================
    {
        "id": 20261001,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 5,
        "part": 1,
        "qNumber": "Question 1",
        "title": "Part 1 지문 읽기 (사내 직원 교육 공지)",
        "prep_time": 45,
        "response_time": 45,
        "question_text": "Good morning, team. Before we begin today's orientation, please ensure that you have signed the attendance sheet at the front desk. Our training program will cover workplace safety, communication protocols, and new software tools. We expect everyone to participate actively throughout the session.",
        "question_translation": "좋은 아침입니다, 팀원 여러분. 오늘 오리엔테이션을 시작하기에 앞서 안내 데스크의 출석부에 서명하셨는지 확인해 주시기 바랍니다. 교육 프로그램에서는 직장 안전, 커뮤니케이션 프로토콜, 그리고 새로운 소프트웨어 툴을 다룰 예정입니다. 모든 분들이 적극적으로 참여해 주시기를 기대합니다.",
        "model_answer": "Good morning, team. Before we begin today's orientation, please ensure that you have signed the attendance sheet at the front desk. Our training program will cover workplace safety, communication protocols, and new software tools. We expect everyone to participate actively throughout the session.",
        "score_tip": "safety, protocols, and new software tools 병렬 구문의 억양 및 orientation의 첫 음절 발음에 주의하세요.",
        "vocabulary": [
            {"word": "orientation", "ipa": "[ˌɔːriənˈteɪʃn]", "meaning": "오리엔테이션, 교육"},
            {"word": "attendance sheet", "ipa": "[əˈtendəns ʃiːt]", "meaning": "출석부"},
            {"word": "protocol", "ipa": "[ˈproʊtəkɑːl]", "meaning": "규약, 행동 수칙"}
        ]
    },
    {
        "id": 20261002,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 236,
        "part": 2,
        "qNumber": "Question 3",
        "title": "Part 2 사진 묘사 (서점/매장 선반 앞 인물들)",
        "prep_time": 45,
        "response_time": 30,
        "image_url": "toeic_part2_images/part2_q03_photo.jpg",
        "question_text": "Describe the picture on your screen in as much detail as you can.",
        "question_translation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "model_answer": "This picture was taken indoors at a bookstore or library. In the foreground, a woman wearing glasses is reaching for a book on a wooden shelf. On the other side, a man is looking at documents while holding a coffee cup. In the background, tall bookshelves filled with various books are neatly arranged. Overall, the scene looks quiet and studious.",
        "score_tip": "초빈출 손동작 'reaching for an item on the shelf' 표현을 정확히 적용하세요.",
        "vocabulary": [
            {"word": "reach for", "ipa": "[riːtʃ fɔːr]", "meaning": "~을 향해 손을 뻗다"},
            {"word": "neatly arranged", "ipa": "[ˈniːtli əˈreɪndʒd]", "meaning": "깔끔하게 정돈된"},
            {"word": "studious", "ipa": "[ˈstuːdiəs]", "meaning": "학구적인, 차분한"}
        ]
    },
    {
        "id": 20261003,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 426,
        "part": 3,
        "qNumber": "Question 5",
        "title": "Part 3 일상 질문 (음악 감상 시간대: 아침 vs 밤)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Imagine that a magazine is conducting an interview about listening to music.",
        "question_text": "Do you usually listen to music in the morning or at night? Choose one of the options provided and explain why you chose it.",
        "question_translation": "보통 아침과 밤 중 언제 음악을 들으시나요? 보기 중 하나를 선택하고 이유를 설명하세요.",
        "model_answer": "I usually listen to music at night before going to bed. Listening to calm acoustic music helps me unwind after a long busy day and fall asleep much faster.",
        "score_tip": "I usually listen to music at night because ~ 로 시작해 'unwind(긴장을 풀다)' 표현을 활용하세요.",
        "vocabulary": [
            {"word": "unwind", "ipa": "[ˌʌnˈwaɪnd]", "meaning": "긴장을 풀다, 휴식하다"}
        ]
    },
    {
        "id": 20261004,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 473,
        "part": 3,
        "qNumber": "Question 6",
        "title": "Part 3 일상 질문 (혼자 음악 듣기 vs 다른 사람과 듣기)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Imagine that a magazine is conducting an interview about listening to music.",
        "question_text": "Which is more enjoyable for you? Listening to music by yourself or listening to music with others? Choose one of the options provided and explain why you chose it.",
        "question_translation": "혼자 음악을 듣는 것과 다른 사람들과 함께 듣는 것 중 어느 쪽이 더 즐거우신가요?",
        "model_answer": "Listening to music by myself is much more enjoyable for me. When I listen alone with headphones, I can completely focus on my favorite tracks without any interruptions.",
        "score_tip": "Listening to music by myself is more enjoyable because I can focus on my favorite tracks without interruptions.",
        "vocabulary": [
            {"word": "interruption", "ipa": "[ˌɪntəˈrʌpʃn]", "meaning": "방해, 중단"}
        ]
    },
    {
        "id": 20261005,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 504,
        "part": 3,
        "qNumber": "Question 7",
        "title": "Part 3 일상 질문 (파티에 가장 적합한 음악 장르: Pop, Classical, Jazz)",
        "prep_time": 3,
        "response_time": 30,
        "context": "Imagine that a magazine is conducting an interview about listening to music.",
        "question_text": "Which type of music do you think is best for a party and why? pop music, classical music, or jazz music.",
        "question_translation": "파티에 가장 좋은 음악 장르는 무엇이라고 생각하시나요? 팝, 클래식, 재즈 중 선택하고 이유를 설명하세요.",
        "model_answer": "I definitely think pop music is the best choice for a party. First, pop songs have upbeat rhythms and catchy melodies that make people feel excited and energetic. Second, most people know the lyrics to popular songs, so everyone can sing along and dance together. On the other hand, classical music is too quiet and serious for a party atmosphere. Therefore, pop music is perfect for making a lively party.",
        "score_tip": "선택지 중 Pop을 고르고 'upbeat rhythms', 'catchy melodies', 'sing along' 3대 표현으로 30초를 완성하세요.",
        "vocabulary": [
            {"word": "upbeat", "ipa": "[ˈʌpbiːt]", "meaning": "경쾌한, 활기찬"},
            {"word": "catchy", "ipa": "[ˈkætʃi]", "meaning": "기억하기 쉬운, 귀에 쏙 들어오는"},
            {"word": "sing along", "ipa": "[sɪŋ əˈlɔːŋ]", "meaning": "함께 따라 부르다"}
        ]
    },
    {
        "id": 20261006,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 637,
        "part": 4,
        "qNumber": "Question 8",
        "title": "Part 4 표 분석 (Steven Chiu의 첫 번째 일정)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Hi, I'm Steven Chiu. I'm calling to check my schedule for July 21st. I have a few questions about my schedule.",
        "table_title": "Steven Chiu's Daily Itinerary - Tuesday, July 21st",
        "question_text": "What is the first thing on my schedule and what time does it start?",
        "question_translation": "제 일정에서 첫 번째 일정이 무엇이고 몇 시에 시작하나요?",
        "model_answer": "The first thing on your schedule is a Department Status Meeting with team managers. It starts at 9:00 AM in Conference Room B.",
        "score_tip": "The first item on your schedule is [일정명]. It starts at [시간] in [장소].",
        "vocabulary": [
            {"word": "status meeting", "ipa": "[ˈsteɪtəs ˈmiːtɪŋ]", "meaning": "현황 보고 회의"}
        ]
    },
    {
        "id": 20261007,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 670,
        "part": 4,
        "qNumber": "Question 9",
        "title": "Part 4 표 분석 (서비스 전략 회의 시간 확인)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Hi, I'm Steven Chiu. I'm calling to check my schedule for July 21st.",
        "table_title": "Steven Chiu's Daily Itinerary - Tuesday, July 21st",
        "question_text": "I believe I have a meeting about service strategies. Can you tell me what time it will be?",
        "question_translation": "서비스 전략에 관한 회의가 있는 것으로 알고 있는데, 몇 시에 있나요?",
        "model_answer": "Yes, you have a Service Strategy Review meeting. It is scheduled from 1:30 PM to 2:30 PM in Meeting Room 3.",
        "score_tip": "시간 범위를 말할 때 'It is scheduled from [시작] to [종료]' 구문을 사용하세요.",
        "vocabulary": [
            {"word": "strategy", "ipa": "[ˈstrætədʒi]", "meaning": "전략"}
        ]
    },
    {
        "id": 20261008,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 716,
        "part": 4,
        "qNumber": "Question 10",
        "title": "Part 4 표 분석 (고객 피드백 관련 모든 일정)",
        "prep_time": 3,
        "response_time": 30,
        "context": "Hi, I'm Steven Chiu. I'm calling to check my schedule for July 21st.",
        "table_title": "Steven Chiu's Daily Itinerary - Tuesday, July 21st",
        "question_text": "Could you tell me everything on my schedule related to customer feedback?",
        "question_translation": "제 일정 중에서 고객 피드백과 관련된 모든 일정을 말씀해 주시겠어요?",
        "model_answer": "Sure, there are two scheduled sessions related to customer feedback. First, at 11:00 AM, you will attend a presentation on Customer Feedback Analysis led by Jessica Taylor. Second, at 3:30 PM, you have an Action Plan Discussion on Customer Survey Results with the support team.",
        "score_tip": "공통 키워드(Customer Feedback / Customer Survey)를 담은 2개 일정을 정확히 골라내어 First ~, Second ~ 로 답변하세요.",
        "vocabulary": [
            {"word": "feedback analysis", "ipa": "[ˈfiːdbæk əˈnæləsɪs]", "meaning": "피드백 분석"}
        ]
    },
    {
        "id": 20261009,
        "exam_date": "2026년 10월",
        "source_title": "2026년 10월 토익스피킹 최신 기출 반영 모의고사 20 (지나쌤)",
        "youtube_video_id": "Vk6-5HyWI_Y",
        "youtube_timestamp": 767,
        "part": 5,
        "qNumber": "Question 11",
        "title": "Part 5 의견 제시 (스마트폰 때문에 자녀 양육이 더 어려워졌는가?)",
        "prep_time": 45,
        "response_time": 60,
        "question_text": "Do you agree or disagree with the following statement? It has become more difficult for parents to raise their children because of smartphones. Give reasons or examples to support your opinion.",
        "question_translation": "다음 주장에 동의하십니까, 아니면 반대하십니까? 스마트폰 때문에 부모들이 자녀를 양육하기가 더 어려워졌다. 구체적인 이유와 사례를 들어 의견을 뒷받침하세요.",
        "model_answer": "I strongly agree with the statement that it has become much harder for parents to raise children because of smartphones. First, excessive smartphone usage causes digital addiction and distracts children from their studies and healthy physical activities. Parents constantly have to monitor screen time and struggle with their kids over phone rules. Second, smartphones expose young children to unfiltered online content, cyberbullying, and inappropriate social media trends, creating severe safety concerns that parents didn't face in the past. For instance, my cousin spends hours on short-form videos every evening, and her parents find it exhausting to manage her daily routines. For these reasons, smartphones have undeniably made modern parenting far more challenging.",
        "score_tip": "현대 부모들의 2대 고민인 'Screen time & study distraction'과 'Safety & social media exposure'를 논리적으로 전개하세요.",
        "vocabulary": [
            {"word": "excessive usage", "ipa": "[ɪkˈsesɪv ˈjuːsɪdʒ]", "meaning": "과도한 사용"},
            {"word": "parenting", "ipa": "[ˈperəntɪŋ]", "meaning": "육아, 부모의 양육"}
        ]
    },

    # =========================================================================
    # [2026년 9월 극최신 기출] 토오미 극최신 모의고사 #28 (UgazFDbahuI)
    # =========================================================================
    {
        "id": 20260901,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 9,
        "part": 1,
        "qNumber": "Question 1",
        "title": "Part 1 지문 읽기 (자연사 박물관 특별전 안내)",
        "prep_time": 45,
        "response_time": 45,
        "question_text": "Attention visitors. The Natural History Museum will close in fifteen minutes. Before leaving, please return all audio guides to the visitor information desk in the main lobby. If you purchased items from our gift shop, make sure to keep your receipts for validation. We thank you for visiting today, and we hope to see you again soon.",
        "question_translation": "방문객 여러분께 안내 말씀드립니다. 자연사 박물관은 15분 후에 문을 닫습니다. 나가시기 전에 메인 로비의 안내 데스크에 오디오 가이드를 모두 반납해 주시기 바랍니다. 기념품점에서 물품을 구매하셨다면 주차 확인을 위해 영수증을 소지하시기 바랍니다. 오늘 방문해 주셔서 감사드리며, 곧 다시 뵙기를 기대합니다.",
        "model_answer": "Attention visitors. The Natural History Museum will close in fifteen minutes. Before leaving, please return all audio guides to the visitor information desk in the main lobby. If you purchased items from our gift shop, make sure to keep your receipts for validation. We thank you for visiting today, and we hope to see you again soon.",
        "score_tip": "audio guides, visitor information desk, receipts의 복수형 -s 발음과 validation의 강세를 명확히 살리세요.",
        "vocabulary": [
            {"word": "validation", "ipa": "[ˌvælɪˈdeɪʃn]", "meaning": "유효성 확인, (주차권) 승인"},
            {"word": "receipt", "ipa": "[rɪˈsiːt]", "meaning": "영수증"}
        ]
    },
    {
        "id": 20260902,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 225,
        "part": 2,
        "qNumber": "Question 3",
        "title": "Part 2 사진 묘사 (야외 카페 테라스의 고객들)",
        "prep_time": 45,
        "response_time": 30,
        "image_url": "toeic_part2_images/part2_q05_photo.jpg",
        "question_text": "Describe the picture on your screen in as much detail as you can.",
        "question_translation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "model_answer": "This is a picture taken at an outdoor cafe terrace on a sunny day. In the middle of the picture, two people are sitting across from each other at a small table, talking pleasantly while drinking iced coffee. In the background, green parasols and brick buildings are visible along the street. Overall, the atmosphere seems very relaxed and peaceful.",
        "score_tip": "시계토끼 4단계 공식(장소 ➔ 중심 인물 대화/음료 ➔ 배경 파라솔 ➔ 총평)으로 30초를 완성하세요.",
        "vocabulary": [
            {"word": "across from each other", "ipa": "[əˈkrɔːs frəm iːtʃ ˈʌðər]", "meaning": "서로 마주보고"},
            {"word": "parasol", "ipa": "[ˈpærəsɔːl]", "meaning": "차양, 파라솔"}
        ]
    },
    {
        "id": 20260903,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 432,
        "part": 3,
        "qNumber": "Question 5",
        "title": "Part 3 일상 질문 (야외 요리 즐기는지 여부 및 이유)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Imagine a cooking magazine is conducting research in your area. You have agreed to participate in a telephone interview about cooking outdoors.",
        "question_text": "Do you enjoy cooking outdoors? Why or why not?",
        "question_translation": "야외에서 요리하는 것을 즐기시나요? 왜 그런가요?",
        "model_answer": "Yes, I really enjoy cooking outdoors, especially barbecuing with my family in the backyard. Cooking in fresh air makes the food taste much better and creates fun memories.",
        "score_tip": "Yes, I really enjoy cooking outdoors because it creates fun memories with my family.",
        "vocabulary": [
            {"word": "cooking outdoors", "ipa": "[ˈkʊkɪŋ ˌaʊtˈdɔːrz]", "meaning": "야외 요리"}
        ]
    },
    {
        "id": 20260904,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 475,
        "part": 3,
        "qNumber": "Question 6",
        "title": "Part 3 일상 질문 (가장 맛있었던 야외 요리와 마지막으로 먹은 시점)",
        "prep_time": 3,
        "response_time": 15,
        "context": "Imagine a cooking magazine is conducting research in your area. You have agreed to participate in a telephone interview about cooking outdoors.",
        "question_text": "What is the most delicious food you have cooked outdoors and when was the last time you had it?",
        "question_translation": "야외에서 요리했던 가장 맛있는 음식은 무엇이며, 마지막으로 먹은 것은 언제인가요?",
        "model_answer": "The most delicious food I have cooked outdoors was grilled steak, and the last time I had it was last month during a weekend camping trip with my close friends.",
        "score_tip": "The most delicious food was [음식], and the last time was [시간]. 의문사 2개(What + When)를 모두 답변하세요.",
        "vocabulary": [
            {"word": "grilled steak", "ipa": "[ɡrɪld steɪk]", "meaning": "직화 구이 스테이크"}
        ]
    },
    {
        "id": 20260905,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 510,
        "part": 3,
        "qNumber": "Question 7",
        "title": "Part 3 일상 질문 (실내 요리 vs 야외 요리 중 더 쉬운 것)",
        "prep_time": 3,
        "response_time": 30,
        "context": "Imagine a cooking magazine is conducting research in your area. You have agreed to participate in a telephone interview about cooking outdoors.",
        "question_text": "Which do you think is easier, cooking indoors or cooking outdoors?",
        "question_translation": "실내 요리와 야외 요리 중 어느 쪽이 더 쉽다고 생각하시나요?",
        "model_answer": "I believe cooking indoors is much easier than cooking outdoors for several reasons. First, inside a kitchen, all cooking utensils, running water, and spices are readily accessible, so food preparation is fast. Second, indoor cooking is completely unaffected by bad weather conditions such as strong wind or rain. On the contrary, cooking outdoors requires carrying heavy equipment and cleaning up is very difficult. Therefore, cooking indoors is definitely much simpler and more convenient.",
        "score_tip": "실내 요리가 더 쉬운 이유(접근성 running water/utensils + 날씨 제약 없음) 2가지를 명확히 제시하세요.",
        "vocabulary": [
            {"word": "utensil", "ipa": "[juːˈtensl]", "meaning": "조리 도구, 기구"},
            {"word": "readily accessible", "ipa": "[ˈredɪli əkˈsesəbl]", "meaning": "손쉽게 접근 가능한"}
        ]
    },
    {
        "id": 20260906,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 645,
        "part": 4,
        "qNumber": "Question 8",
        "title": "Part 4 표 분석 (수영 코치 컨퍼런스 개최 날짜와 등록 시작 시간)",
        "prep_time": 3,
        "response_time": 15,
        "context": "I'm planning to attend the Swimming Coaches Association annual conference. I haven't received the schedule yet, so I'd like to ask you a few questions.",
        "table_title": "Swimming Coaches Association Annual Conference",
        "question_text": "What date will the conference be held? And what time does registration begin?",
        "question_translation": "컨퍼런스는 몇 월 며칠에 열리나요? 그리고 등록은 몇 시에 시작하나요?",
        "model_answer": "The conference will be held on Saturday, September 19th, and registration begins at 8:30 AM in the Grand Ballroom Lobby.",
        "score_tip": "날짜와 시간을 각각 전치사 on과 at으로 정확히 명시하세요.",
        "vocabulary": [
            {"word": "annual conference", "ipa": "[ˈænjuəl ˈkɑːnfərəns]", "meaning": "연례 컨퍼런스/총회"}
        ]
    },
    {
        "id": 20260907,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 677,
        "part": 4,
        "qNumber": "Question 9",
        "title": "Part 4 표 분석 (오류 정정: Henry Patton과의 점심 식사 여부)",
        "prep_time": 3,
        "response_time": 15,
        "context": "I'm planning to attend the Swimming Coaches Association annual conference.",
        "table_title": "Swimming Coaches Association Annual Conference",
        "question_text": "I understand that we'll have lunch with Henry Patton. Could you confirm that for me?",
        "question_translation": "헨리 패튼 씨와 점심 식사를 하는 것으로 알고 있는데, 확인해 주시겠어요?",
        "model_answer": "No, I'm afraid that's incorrect. Lunch will be a buffet for all participants from 12:00 PM to 1:00 PM, and Henry Patton will give a keynote lecture at 1:30 PM.",
        "score_tip": "'No, I'm afraid that's incorrect.'로 시작해 실제 오찬 형식과 헨리 패튼의 강연 시간을 정정해 주세요.",
        "vocabulary": [
            {"word": "keynote lecture", "ipa": "[ˈkiːnoʊt ˈlektʃər]", "meaning": "기조 강연"}
        ]
    },
    {
        "id": 20260908,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 720,
        "part": 4,
        "qNumber": "Question 10",
        "title": "Part 4 표 분석 (초보 수영자 세션 전체 안내)",
        "prep_time": 3,
        "response_time": 30,
        "context": "I'm planning to attend the Swimming Coaches Association annual conference.",
        "table_title": "Swimming Coaches Association Annual Conference",
        "question_text": "I teach beginning swimmers. Could you give me all the information about the sessions that specifically deal with beginners?",
        "question_translation": "제가 초보 수영자들을 가르치고 있는데요. 초보자를 구체적으로 다루는 세션들에 대한 모든 정보를 주시겠어요?",
        "model_answer": "Sure, there are two sessions specifically designed for beginners. First, from 10:00 AM to 11:30 AM, there is a workshop titled 'Basic Breathing Techniques for Beginners' led by Coach Sarah Miller. Second, from 3:00 PM to 4:30 PM, you can attend 'Building Confidence in the Water' presented by David Evans.",
        "score_tip": "초보자 키워드(Beginners / Building Confidence)가 포함된 2개 세션의 시간, 제목, 발표자를 순서대로 안내하세요.",
        "vocabulary": [
            {"word": "specifically deal with", "ipa": "[spəˈsɪfɪkli diːl wɪð]", "meaning": "구체적으로 ~을 다루다"}
        ]
    },
    {
        "id": 20260909,
        "exam_date": "2026년 9월",
        "source_title": "2026년 9월 극최신 모의고사 #28 (토오미)",
        "youtube_video_id": "UgazFDbahuI",
        "youtube_timestamp": 780,
        "part": 5,
        "qNumber": "Question 11",
        "title": "Part 5 의견 제시 (마감 직전까지 과제를 미루는 학생이 좋은 성과를 낼 수 있는가?)",
        "prep_time": 45,
        "response_time": 60,
        "question_text": "Do you think it is possible for students to do well on their schoolwork if they don't start working on it until right before the deadline? Why or why not?",
        "question_translation": "학생들이 마감 직전까지 과제를 시작하지 않더라도 학교 공부를 잘하는 것이 가능하다고 생각하십니까? 왜 그런가요?",
        "model_answer": "I do not think it is possible for students to consistently do well on their schoolwork if they procrastinate until the last minute. First of all, high-quality academic work requires deep research, careful revisions, and critical thinking, which simply cannot be rushed in a few hours. Working under intense time pressure inevitably leads to careless mistakes and shallow content. Second, leaving assignments until right before the deadline causes extreme stress and sleep deprivation, which negatively impacts a student's mental clarity and physical health. When I was in university, I once tried writing a research paper the night before it was due. Because I lacked time to proofread, I received a very poor grade. Therefore, starting early and managing time properly is essential for academic success.",
        "score_tip": "벼락치기(procrastinate)가 불가능한 이유(품질 저하/실수 + 스트레스/수면 부족) 2가지와 대학 시절 반면교사 경험을 풍부하게 전달하세요.",
        "vocabulary": [
            {"word": "procrastinate", "ipa": "[prəˈkræstɪneɪt]", "meaning": "미루다, 늑장부리다"},
            {"word": "sleep deprivation", "ipa": "[sliːp ˌdeprɪˈveɪʃn]", "meaning": "수면 부족, 수면 박탈"},
            {"word": "proofread", "ipa": "[ˈpruːfriːd]", "meaning": "교정하다, 검토하다"}
        ]
    }
]

def main():
    os.makedirs("data", exist_ok=True)
    out_path = "data/toeic_data.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(LATEST_2026_DATA, f, ensure_ascii=False, indent=2)
    print(f"✅ 총 {len(LATEST_2026_DATA)}개의 2026년 9~11월 최신 기출 문항이 '{out_path}'에 저장되었습니다.")

if __name__ == "__main__":
    main()

