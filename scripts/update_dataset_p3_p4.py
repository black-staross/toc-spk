#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/update_dataset_p3_p4.py
- Part 3: 5개 유형 × 6문제 = 총 30문제로 보충 (최신 2026 기출 5문제 추가)
- Part 3 문항 번호: 'Part 3 - #01 (Q5)' 형식에서 '(Q5)'를 떼고 'Part 3 - #01' ~ 'Part 3 - #30'으로 다른 파트와 동일하게 #번호만 남김
- Part 4: 8개 표 세트 × 4문제 = 총 32문제로 보충 (병원 세미나, 해외 출장 여정표, 피트니스 센터 강습표 등 3개 세트 12문제 신규 추가)
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def run_update():
    # 1. 새 Part 3 데이터 생성
    # 기존 data/toeic_parts_master.json을 읽어서 Part 3 기존 25문제를 가져오고,
    # 번호 양식을 Part 3 - #01로 변경한 뒤 각 유형별 6번째 문제를 추가한다.
    master_path = ROOT / "data" / "toeic_parts_master.json"
    with open(master_path, "r", encoding="utf-8") as f:
        master = json.load(f)

    old_p3 = master.get("part3", [])
    
    # 유형별 분리
    t1_items = [q for q in old_p3 if q["typeId"] == "p3-t1"]
    t2_items = [q for q in old_p3 if q["typeId"] == "p3-t2"]
    t3_items = [q for q in old_p3 if q["typeId"] == "p3-t3"]
    t4_items = [q for q in old_p3 if q["typeId"] == "p3-t4"]
    t5_items = [q for q in old_p3 if q["typeId"] == "p3-t5"]

    # 1) 유형 1 신규 문제: 스마트폰 앱 다운로드 및 어학 공부 (#06)
    new_q_t1 = {
        "id": "p3-06",
        "part": 3,
        "qNum": "Part 3 - #06",
        "typeId": "p3-t1",
        "typeName": "유형 1: 시점·최근 경험 (When / Past)",
        "typeBadge": "유형 1 · 시점·최근 경험",
        "topic": "모바일 앱 최근 다운로드 경험 (Mobile Application)",
        "prepTime": 3,
        "responseTime": 15,
        "question": "When was the last time you downloaded a new app on your smartphone, and what kind of app was it?",
        "questionKo": "스마트폰에 새로운 앱을 마지막으로 다운로드한 것이 언제였고, 어떤 종류의 앱이었나요?",
        "sentences": [
            {"step": "1. 과거 시점 제시", "en": "The last time I downloaded a new app on my smartphone was just a few days ago.", "ko": "제가 스마트폰에 새로운 앱을 마지막으로 다운로드한 것은 불과 며칠 전이었습니다."},
            {"step": "2. 구체적 종류", "en": "It was a language learning application to practice everyday English speaking.", "ko": "일상 영어 회화를 연습하기 위한 어학 학습 애플리케이션이었습니다."},
            {"step": "3. 사용 소감", "en": "It is very user-friendly, and I use it every day to improve my skills.", "ko": "사용하기 매우 편리해서 실력을 키우기 위해 매일 사용하고 있습니다."}
        ],
        "magicSentences": [
            {"en": "The last time I downloaded a new app was just a few days ago.", "ko": "마지막으로 새 앱을 다운로드한 것은 며칠 전이었습니다.", "tip": "When was the last time 질문을 주어+was a few days ago로 즉각 대응"},
            {"en": "It is very convenient and user-friendly.", "ko": "매우 편리하고 사용하기 쉽습니다.", "tip": "시계토끼 만능 #055 (앱/디지털 서비스 만족도 공식)"}
        ],
        "vocabulary": [
            {"word": "download", "ipa": "[ˌdaʊnˈloʊd]", "pos": "동사", "meaning": "다운로드하다"},
            {"word": "application", "ipa": "[ˌæplɪˈkeɪʃn]", "pos": "명사", "meaning": "응용 프로그램, 앱"},
            {"word": "user-friendly", "ipa": "[ˌjuːzər ˈfrendli]", "pos": "형용사", "meaning": "사용하기 편리한"}
        ],
        "explanation": "질문의 'When was the last time you downloaded ~'를 그대로 'The last time I downloaded a new app was just a few days ago'로 받아치고, language learning app과 user-friendly를 활용해 15초를 채우세요."
    }

    # 2) 유형 2 신규 문제: 스터디 카페/도서관 방문 빈도 및 동행인 (#12)
    new_q_t2 = {
        "id": "p3-12",
        "part": 3,
        "qNum": "Part 3 - #12",
        "typeId": "p3-t2",
        "typeName": "유형 2: 빈도·장소·동행인 (How often / Where / Who)",
        "typeBadge": "유형 2 · 빈도·장소·동행인",
        "topic": "도서관·스터디 카페 방문 빈도 및 동행인 (Study Cafe / Library)",
        "prepTime": 3,
        "responseTime": 15,
        "question": "How often do you go to a study cafe or a library, and who do you usually go with?",
        "questionKo": "스터디 카페나 도서관에 얼마나 자주 가며, 보통 누구와 함께 가나요?",
        "sentences": [
            {"step": "1. 빈도 제시", "en": "I usually go to a study cafe about twice a week.", "ko": "저는 보통 일주일에 두 번 정도 스터디 카페에 갑니다."},
            {"step": "2. 동행인 제시", "en": "Most of the time, I go there alone because it helps me concentrate better on my studies.", "ko": "학업에 더 잘 집중할 수 있기 때문에 대부분의 경우 혼자 갑니다."},
            {"step": "3. 환경 만족도", "en": "The study atmosphere is quiet and provides high-speed Wi-Fi.", "ko": "학습 분위기가 조용하고 초고속 와이파이를 제공합니다."}
        ],
        "magicSentences": [
            {"en": "I usually go there about twice a week.", "ko": "저는 보통 일주일에 두 번 정도 그곳에 갑니다.", "tip": "시계토끼 만능 #074 (주 2회 빈도 공식)"},
            {"en": "I go there alone to focus better on my work.", "ko": "집중을 더 잘하기 위해 혼자 갑니다.", "tip": "시계토끼 만능 #078 (혼자 방문하는 이유)"}
        ],
        "vocabulary": [
            {"word": "study cafe", "ipa": "[ˈstʌdi kæˈfeɪ]", "pos": "명사", "meaning": "스터디 카페"},
            {"word": "concentrate on", "ipa": "[ˈkɑːnsntreɪt ɑːn]", "pos": "숙어", "meaning": "~에 집중하다"},
            {"word": "atmosphere", "ipa": "[ˈætməsfɪr]", "pos": "명사", "meaning": "분위기"}
        ],
        "explanation": "빈도는 twice a week, 동행인은 alone(혼자)으로 설정하고 concentrate better를 이유로 대면 깔끔하게 답변할 수 있습니다."
    }

    # 3) 유형 3 신규 문제: 영화/드라마 추천 정보 검색 (친구 추천 vs 온라인 리뷰) (#18)
    new_q_t3 = {
        "id": "p3-18",
        "part": 3,
        "qNum": "Part 3 - #18",
        "typeId": "p3-t3",
        "typeName": "유형 3: 양자택일 선호도·찬반 (Preference / Agree or Disagree)",
        "typeBadge": "유형 3 · 양자택일·찬반",
        "topic": "영화/드라마 선택 시 친구 추천 vs 온라인 리뷰 선호도 (Movie Recommendations)",
        "prepTime": 3,
        "responseTime": 15,
        "question": "When choosing a movie or TV show to watch, do you prefer asking friends for recommendations or reading online reviews? Why?",
        "questionKo": "볼 영화나 TV 프로그램을 고를 때 친구에게 추천을 부탁하는 것과 온라인 리뷰를 읽는 것 중 어느 쪽을 더 선호하나요? 왜 그런가요?",
        "sentences": [
            {"step": "1. 선호 입장 제시", "en": "I prefer reading online reviews rather than asking friends for recommendations.", "ko": "저는 친구에게 추천을 부탁하는 것보다 온라인 리뷰를 읽는 것을 더 선호합니다."},
            {"step": "2. 이유 1 (다양성)", "en": "This is because online reviews provide a wide variety of honest opinions from many viewers.", "ko": "온라인 리뷰는 많은 시청자들로부터 다양한 솔직한 의견을 제공하기 때문입니다."},
            {"step": "3. 이유 2 (편의성)", "en": "Also, I can check ratings quickly on my smartphone anytime, anywhere.", "ko": "또한 언제 어디서나 스마트폰으로 평점을 빠르게 확인할 수 있습니다."}
        ],
        "magicSentences": [
            {"en": "I prefer reading online reviews because it is more reliable.", "ko": "더 신뢰할 수 있기 때문에 온라인 리뷰를 선호합니다.", "tip": "시계토끼 만능 #083 (선호 이유 공식)"},
            {"en": "I can check ratings anytime and anywhere on my smartphone.", "ko": "스마트폰으로 언제 어디서든 평점을 확인할 수 있습니다.", "tip": "시계토끼 만능 #086 (접근성 편의 공식)"}
        ],
        "vocabulary": [
            {"word": "recommendation", "ipa": "[ˌrekəmenˈdeɪʃn]", "pos": "명사", "meaning": "추천"},
            {"word": "honest opinion", "ipa": "[ˈɑːnɪst əˈpɪnjən]", "pos": "명사구", "meaning": "솔직한 의견"},
            {"word": "ratings", "ipa": "[ˈreɪtɪŋz]", "pos": "명사", "meaning": "평점, 시청률"}
        ],
        "explanation": "I prefer A rather than B 구문을 활용하여 빠르게 선호를 밝히고, 다양성(wide variety of opinions)과 언제 어디서나 확인 가능한 편의성을 제시하세요."
    }

    # 4) 유형 4 신규 문제: 전자기기 구매 시 최우선 고려 요소 (30초) (#24)
    new_q_t4 = {
        "id": "p3-24",
        "part": 3,
        "qNum": "Part 3 - #24",
        "typeId": "p3-t4",
        "typeName": "유형 4: 3자택일 최적 선택 (Best Option out of Three)",
        "typeBadge": "유형 4 · 3자택일 선택",
        "topic": "노트북/태블릿 구매 시 가장 중요한 고려 요소 (Buying a Laptop or Tablet)",
        "prepTime": 3,
        "responseTime": 30,
        "question": "When purchasing a new laptop or tablet, which of the following is most important to you: Brand reputation, Battery life, or Price? Why?",
        "questionKo": "새 노트북이나 태블릿을 구매할 때 브랜드 평판, 배터리 수명, 가격 중 어느 것이 가장 중요한가요? 왜 그런가요?",
        "sentences": [
            {"step": "1. 서론 (선택 제시)", "en": "When purchasing a new laptop or tablet, battery life is the most important factor to me.", "ko": "새 노트북이나 태블릿을 구매할 때 저에게는 배터리 수명이 가장 중요한 요소입니다."},
            {"step": "2. 이유 1 (휴대성)", "en": "First of all, I often carry my device to cafes, libraries, and outside meetings.", "ko": "우선, 저는 카페, 도서관, 외부 회의에 기기를 자주 가지고 다닙니다."},
            {"step": "3. 세부 부연", "en": "If the battery lasts all day long, I don't need to carry a heavy charger or look for power outlets.", "ko": "배터리가 하루 종일 지속된다면 무거운 충전기를 들고 다니거나 콘센트를 찾을 필요가 없습니다."},
            {"step": "4. 이유 2 (작업 연속성)", "en": "In addition, long battery life allows me to work continuously without any interruptions during long travels.", "ko": "게다가 긴 배터리 수명은 장거리 이동 중에도 끊김 없이 지속적으로 작업할 수 있게 해줍니다."},
            {"step": "5. 결론", "en": "Therefore, battery life is definitely my top priority.", "ko": "따라서 배터리 수명이 단연코 저의 최우선 순위입니다."}
        ],
        "magicSentences": [
            {"en": "Battery life is the most important factor to me.", "ko": "배터리 수명이 저에게 가장 중요한 요소입니다.", "tip": "시계토끼 만능 #089 (최우선 순위 공식)"},
            {"en": "I don't need to carry a heavy charger or look for power outlets.", "ko": "무거운 충전기를 들거나 콘센트를 찾을 필요가 없습니다.", "tip": "전자기기 배터리 만능 근거"},
            {"en": "Therefore, it is definitely my top priority.", "ko": "따라서 그것이 단연 저의 최우선 순위입니다.", "tip": "시계토끼 만능 #095 (30초 결론 공식)"}
        ],
        "vocabulary": [
            {"word": "battery life", "ipa": "[ˈbætəri laɪf]", "pos": "명사", "meaning": "배터리 수명"},
            {"word": "power outlet", "ipa": "[ˈpaʊər ˈaʊtlet]", "pos": "명사", "meaning": "전원 콘센트"},
            {"word": "interruption", "ipa": "[ˌɪntəˈrʌpʃn]", "pos": "명사", "meaning": "중단, 방해"},
            {"word": "top priority", "ipa": "[tɑːp praɪˈɔːrəti]", "pos": "명사", "meaning": "최우선 순위"}
        ],
        "explanation": "30초 답변이므로 서론(1문장) + 첫째 이유 및 부연(2문장) + 둘째 이유(1문장) + 결론(1문장)의 5문장 템플릿으로 안정적인 답변을 완성하세요."
    }

    # 5) 유형 5 신규 문제: 온라인 신선 식료품 배달 서비스의 장점 (30초) (#30)
    new_q_t5 = {
        "id": "p3-30",
        "part": 3,
        "qNum": "Part 3 - #30",
        "typeId": "p3-t5",
        "typeName": "유형 5: 장단점·중요 이유 (Advantages / Importance)",
        "typeBadge": "유형 5 · 장단점·이유",
        "topic": "온라인 신선 식료품 배달 서비스의 장점 (Online Grocery Delivery)",
        "prepTime": 3,
        "responseTime": 30,
        "question": "What are the advantages of using online grocery delivery services compared to visiting a local supermarket?",
        "questionKo": "동네 슈퍼마켓을 직접 방문하는 것과 비교했을 때 온라인 식료품 배달 서비스를 이용하는 것의 장점은 무엇인가요?",
        "sentences": [
            {"step": "1. 서론 (장점 개수)", "en": "There are several great advantages of using online grocery delivery services.", "ko": "온라인 식료품 배달 서비스를 이용하는 데는 몇 가지 큰 장점이 있습니다."},
            {"step": "2. 장점 1 (시간/노력 절약)", "en": "First, it saves a tremendous amount of time and effort.", "ko": "첫째, 엄청난 시간과 노력을 절약해 줍니다."},
            {"step": "3. 세부 부연", "en": "Instead of driving through heavy traffic and waiting in long checkout lines, I can order fresh food with just a few clicks.", "ko": "복잡한 교통을 뚫고 운전하거나 긴 계산대 줄을 서는 대신 몇 번의 클릭만으로 신선한 음식을 주문할 수 있습니다."},
            {"step": "4. 장점 2 (무거운 짐 배송)", "en": "Second, heavy items like bottled water, rice, and detergents are delivered right to my front door.", "ko": "둘째, 생수, 쌀, 세제 같은 무거운 물품들이 현관문 앞까지 바로 배송됩니다."},
            {"step": "5. 결론", "en": "For these reasons, online grocery shopping makes our daily lives much more convenient.", "ko": "이러한 이유들로 온라인 식료품 쇼핑은 일상생활을 훨씬 더 편리하게 만들어 줍니다."}
        ],
        "magicSentences": [
            {"en": "First, it saves a tremendous amount of time and effort.", "ko": "첫째, 엄청난 시간과 노력을 절약해 줍니다.", "tip": "시계토끼 만능 #091 (시간/비용 절약 공식)"},
            {"en": "Heavy items are delivered right to my front door.", "ko": "무거운 물품들이 현관문 앞까지 배송됩니다.", "tip": "배달 서비스 만능 근거"},
            {"en": "It makes our daily lives much more convenient.", "ko": "일상생활을 훨씬 더 편리하게 만듭니다.", "tip": "시계토끼 만능 #096 (삶의 질 향상 결론)"}
        ],
        "vocabulary": [
            {"word": "grocery delivery", "ipa": "[ˈɡroʊsəri dɪˈlɪvəri]", "pos": "명사", "meaning": "식료품 배달"},
            {"word": "tremendous", "ipa": "[trəˈmendəs]", "pos": "형용사", "meaning": "엄청난, 대단한"},
            {"word": "detergent", "ipa": "[dɪˈtɜːrdʒənt]", "pos": "명사", "meaning": "세제"},
            {"word": "checkout line", "ipa": "[ˈtʃekaʊt laɪn]", "pos": "명사", "meaning": "계산대 대기열"}
        ],
        "explanation": "시간 절약(saves time)과 무거운 짐 운반 부담 해소(delivered to front door) 두 가지 명확한 장점을 대조하면 30초 고득점을 받을 수 있습니다."
    }

    # 번호 부여: (Q5), (Q6) 떼고 다른 파트처럼 Part 3 - #01 ~ #30 순차 부여
    all_p3_raw = (
        t1_items + [new_q_t1] +
        t2_items + [new_q_t2] +
        t3_items + [new_q_t3] +
        t4_items + [new_q_t4] +
        t5_items + [new_q_t5]
    )

    p3_final = []
    for idx, q in enumerate(all_p3_raw, start=1):
        clean_q = dict(q)
        clean_q["id"] = f"p3-{idx:02d}"
        clean_q["qNum"] = f"Part 3 - #{idx:02d}"  # #번호만 깔끔하게 유지!
        p3_final.append(clean_q)

    # 2. 새 Part 4 데이터 생성 (8개 세트 × 4문제 = 총 32문제)
    # 기존 5개 세트 가져오기
    old_p4_sets = master.get("part4", [])

    # 신규 세트 6: 병원·의료 건강 워크숍 (4문항)
    t_medical = {
        "headerTitle": "Metro Community Health Center - Autumn Wellness Workshops & Screenings",
        "metaInfo": [
            {"label": "Date & Venue", "value": "November 25 / Community Health Center, 2nd Floor Auditorium"},
            {"label": "Cost & Registration", "value": "Free admission for all local residents (Pre-registration required for screenings)"}
        ],
        "rows": [
            {"date": "09:30 AM", "time": "Session 1", "event": "Cardiovascular Health & Exercise", "location": "Room 201", "note": "Instructor: Dr. Robert Kim"},
            {"date": "11:00 AM", "time": "Session 2", "event": "Nutrition & Balanced Meal Planning", "location": "Room 203", "note": "Instructor: Lisa Wong (Changed from Dr. Robert Kim)"},
            {"date": "01:30 PM", "time": "Session 3", "event": "Stress Management & Meditation", "location": "Quiet Lounge", "note": "Instructor: Helen Vance"},
            {"date": "03:30 PM", "time": "Session 4", "event": "Free Blood Pressure & Glucose Screening", "location": "Clinic B", "note": "Instructor: Dr. Robert Kim & Staff"}
        ]
    }
    set6 = {
        "id": "p4-set6",
        "part": 4,
        "setNum": "Part 4 - Set 6",
        "tableTypeId": "table-medical",
        "tableTypeName": "병원·건강 세미나",
        "tableTypeBadge": "건강 세미나표",
        "topic": "Metro Community Health Center - Free Wellness Workshops & Screenings",
        "prepTime": 45,
        "scheduleTable": t_medical,
        "questions": [
            {
                "qId": "p4-s6-q8",
                "qNum": "Question 8",
                "topic": "행사 개최 일시·장소 및 첫 세션 시작 시각",
                "prepTime": 3,
                "responseTime": 15,
                "question": "When and where will the Autumn Wellness Workshops be held, and what time does the first session start?",
                "questionKo": "가을 웰니스 워크숍은 언제 어디서 열리며, 첫 번째 세션은 몇 시에 시작하나요?",
                "sentences": [
                    {"step": "1. 일시 및 장소 안내", "en": "The Autumn Wellness Workshops will be held on November 25th at the 2nd Floor Auditorium in the Community Health Center.", "ko": "가을 웰니스 워크숍은 11월 25일에 지역 보건 센터 2층 강당에서 열릴 예정입니다."},
                    {"step": "2. 첫 세션 시작 시각", "en": "Also, the first session on Cardiovascular Health and Exercise starts at 9:30 AM in Room 201.", "ko": "또한 심혈관 건강 및 운동에 관한 첫 번째 세션은 201호에서 오전 9시 30분에 시작합니다."}
                ],
                "magicSentences": [
                    {"en": "It will be held on November 25th in the 2nd Floor Auditorium.", "ko": "11월 25일 2층 강당에서 열립니다.", "tip": "시계토끼 만능 #097 & #099 (개최 일시 장소 공식)"},
                    {"en": "The first session starts at 9:30 AM in Room 201.", "ko": "첫 세션은 201호에서 오전 9시 30분에 시작합니다.", "tip": "시계토끼 만능 #106 (시작 시각 안내)"}
                ],
                "vocabulary": [
                    {"word": "auditorium", "ipa": "[ˌɔːdɪˈtɔːriəm]", "pos": "명사", "meaning": "강당"},
                    {"word": "cardiovascular", "ipa": "[ˌkɑːrdioʊˈvæskjələr]", "pos": "형용사", "meaning": "심혈관의"}
                ],
                "explanation": "표 상단의 개최 일시(November 25th), 장소(2nd Floor Auditorium), 첫 세션 시각(9:30 AM in Room 201)을 답변하세요."
            },
            {
                "qId": "p4-s6-q9",
                "qNum": "Question 9",
                "topic": "오전 11시 영양 식단 세션 강사 변경 오류 정정",
                "prepTime": 3,
                "responseTime": 15,
                "question": "I heard that Dr. Robert Kim will be teaching the Nutrition and Balanced Meal Planning session at 11:00 AM. Is that correct?",
                "questionKo": "오전 11시에 있는 영양 및 균형 잡힌 식단 계획 세션을 로버트 킴 박사가 가르친다고 들었습니다. 맞나요?",
                "sentences": [
                    {"step": "1. 오류 정정 표현", "en": "No, I'm afraid that is not correct.", "ko": "아니요, 유감스럽지만 그것은 사실이 아닙니다."},
                    {"step": "2. 변경된 강사 안내", "en": "Although Dr. Robert Kim was originally scheduled, the instructor has been changed to Lisa Wong.", "ko": "원래는 로버트 킴 박사로 예정되어 있었지만, 강사가 리사 웡으로 변경되었습니다."},
                    {"step": "3. 장소 및 시간 확인", "en": "The session will still take place at 11:00 AM in Room 203.", "ko": "세션은 여전히 203호에서 오전 11시에 진행됩니다."}
                ],
                "magicSentences": [
                    {"en": "No, that is not correct. The instructor has been changed to Lisa Wong.", "ko": "아니요, 그렇지 않습니다. 강사가 리사 웡으로 변경되었습니다.", "tip": "시계토끼 만능 #118 (강사 변경 오류 정정)"}
                ],
                "vocabulary": [
                    {"word": "originally", "ipa": "[əˈrɪdʒənəli]", "pos": "부사", "meaning": "원래는"},
                    {"word": "meal planning", "ipa": "[miːl ˈplænɪŋ]", "pos": "명사", "meaning": "식단 계획"}
                ],
                "explanation": "비고란에 적힌 '(Changed from Dr. Robert Kim)'을 파악하여 Lisa Wong으로 강사가 변경되었음을 명확히 정정하세요."
            },
            {
                "qId": "p4-s6-q10",
                "qNum": "Question 10",
                "topic": "로버트 킴(Dr. Robert Kim) 박사가 진행하는 모든 세션 2가지 상세 안내",
                "prepTime": 3,
                "responseTime": 30,
                "question": "I would like to attend all programs led by Dr. Robert Kim. Could you give me all the details about his sessions?",
                "questionKo": "로버트 킴 박사가 이끄는 모든 프로그램에 참석하고 싶습니다. 그가 진행하는 세션의 모든 세부 사항을 알려주시겠어요?",
                "sentences": [
                    {"step": "1. 총 개수 안내", "en": "Sure! There are two programs led by Dr. Robert Kim on November 25th.", "ko": "물론입니다! 11월 25일에 로버트 킴 박사가 이끄는 프로그램이 두 개 있습니다."},
                    {"step": "2. 첫 번째 프로그램", "en": "First, from 9:30 AM, he will conduct Session 1 on Cardiovascular Health and Exercise in Room 201.", "ko": "첫째, 오전 9시 30분부터 201호에서 심혈관 건강 및 운동에 관한 세션 1을 진행합니다."},
                    {"step": "3. 두 번째 프로그램", "en": "Second, at 3:30 PM, he and his staff will provide Free Blood Pressure and Glucose Screening in Clinic B.", "ko": "둘째, 오후 3시 30분에는 클리닉 B에서 그와 스태프들이 무료 혈압 및 혈당 검진을 제공합니다."}
                ],
                "magicSentences": [
                    {"en": "There are two programs led by Dr. Robert Kim.", "ko": "로버트 킴 박사가 이끄는 프로그램이 두 개 있습니다.", "tip": "시계토끼 만능 #129 (총 2개 프로그램 오프닝)"},
                    {"en": "First, at 9:30 AM... Second, at 3:30 PM...", "ko": "첫째 9:30에는... 둘째 3:30에는...", "tip": "시계토끼 만능 #131 (시간 순차 전개 공식)"}
                ],
                "vocabulary": [
                    {"word": "conduct", "ipa": "[kənˈdʌkt]", "pos": "동사", "meaning": "진행하다, 실시하다"},
                    {"word": "glucose screening", "ipa": "[ˈɡluːkoʊs ˈskriːnɪŋ]", "pos": "명사", "meaning": "혈당 검진"}
                ],
                "explanation": "오전 11시 세션은 Lisa Wong으로 바뀌었으므로 제외하고, 오전 9:30 세션 1과 오후 3:30 무료 검진 세션 4 두 가지만 정확히 설명하세요."
            },
            {
                "qId": "p4-s6-q-extra",
                "qNum": "추가 문제 (사전 등록 규정)",
                "topic": "입장료 및 무료 건강 검진 사전 등록 필수 규정",
                "prepTime": 3,
                "responseTime": 15,
                "question": "How much is the admission fee for the workshops, and is there any special registration requirement for the health screening?",
                "questionKo": "워크숍 입장료는 얼마이며, 건강 검진에 대한 특별한 등록 요구사항이 있나요?",
                "sentences": [
                    {"step": "1. 입장료 안내", "en": "Admission is completely free for all local residents.", "ko": "입장료는 모든 지역 주민에게 완전 무료입니다."},
                    {"step": "2. 사전 등록 필수 안내", "en": "However, please keep in mind that pre-registration is required for the free health screening in Clinic B.", "ko": "하지만 클리닉 B에서 진행되는 무료 건강 검진은 사전 등록이 필수라는 점을 명심해 주시기 바랍니다."}
                ],
                "magicSentences": [
                    {"en": "Admission is completely free for all local residents.", "ko": "모든 지역 주민에게 입장료는 완전 무료입니다.", "tip": "시계토끼 만능 #122 (무료 입장 공식)"},
                    {"en": "Pre-registration is required for the health screening.", "ko": "건강 검진은 사전 등록이 필수입니다.", "tip": "시계토끼 만능 #127 (사전 등록 필수 공식)"}
                ],
                "vocabulary": [
                    {"word": "local residents", "ipa": "[ˈloʊkl ˈrezɪdənts]", "pos": "명사", "meaning": "지역 주민들"},
                    {"word": "keep in mind", "ipa": "[kiːp ɪn maɪnd]", "pos": "숙어", "meaning": "명심하다, 유념하다"}
                ],
                "explanation": "상단의 'Free admission for all local residents'와 'Pre-registration required for screenings' 두 가지 정보를 전달하세요."
            }
        ]
    }

    # 신규 세트 7: 해외 출장 비행 및 회의 일정표 (4문항)
    t_itinerary = {
        "headerTitle": "David Miller - 3-Day Business Trip Itinerary to Singapore",
        "metaInfo": [
            {"label": "Traveler & Team", "value": "David Miller / Global Sales & Partnership Division"},
            {"label": "Hotel & Transfer", "value": "Marina Grand Hotel, Singapore (Complimentary Airport Shuttle Provided)"}
        ],
        "rows": [
            {"date": "Dec 8 / 09:15 AM", "time": "Flight SQ 601", "event": "Incheon (ICN) to Singapore (SIN)", "location": "Terminal 3", "note": "Arrives at 2:45 PM / Non-stop"},
            {"date": "Dec 8 / 04:30 PM", "time": "Meeting 1", "event": "Welcome Briefing & Contract Review", "location": "Apex Asia HQ", "note": "With Director Alan Tan"},
            {"date": "Dec 9 / 10:00 AM", "time": "Meeting 2", "event": "Product Demonstration & QA Session", "location": "Tech Park Hall 4", "note": "With Engineering Team"},
            {"date": "Dec 9 / 02:00 PM", "time": "Site Visit", "event": "Automated Logistics Center Tour", "location": "Port Terminal", "note": "Cancelled - Replaced by Executive Dinner at 6:30 PM"}
        ]
    }
    set7 = {
        "id": "p4-set7",
        "part": 4,
        "setNum": "Part 4 - Set 7",
        "tableTypeId": "table-itinerary",
        "tableTypeName": "비행·출장 여정표",
        "tableTypeBadge": "출장 여정표",
        "topic": "David Miller - 3-Day Business Trip Itinerary to Singapore",
        "prepTime": 45,
        "scheduleTable": t_itinerary,
        "questions": [
            {
                "qId": "p4-s7-q8",
                "qNum": "Question 8",
                "topic": "출발 항공편 편명 및 싱가포르 현지 도착 시각",
                "prepTime": 3,
                "responseTime": 15,
                "question": "What is David Miller's flight number to Singapore, and what time will he arrive in Singapore?",
                "questionKo": "데이비드 밀러의 싱가포르행 항공편 편명은 무엇이며, 싱가포르에 몇 시에 도착하나요?",
                "sentences": [
                    {"step": "1. 항공편명 및 출발", "en": "His flight number is Flight SQ 601, departing at 9:15 AM on December 8th from Terminal 3.", "ko": "그의 항공편은 SQ 601편으로, 12월 8일 오전 9시 15분에 3번 터미널에서 출발합니다."},
                    {"step": "2. 현지 도착 시각", "en": "He will arrive in Singapore at 2:45 PM on the same day on a non-stop flight.", "ko": "그는 같은 날 오후 2시 45분에 직항편으로 싱가포르에 도착할 예정입니다."}
                ],
                "magicSentences": [
                    {"en": "His flight number is SQ 601, and he will arrive at 2:45 PM.", "ko": "항공편은 SQ 601편이며, 오후 2시 45분에 도착합니다.", "tip": "항공 일정표 도착 시각 공식"}
                ],
                "vocabulary": [
                    {"word": "flight number", "ipa": "[flaɪt ˈnʌmbər]", "pos": "명사", "meaning": "항공편 번호"},
                    {"word": "non-stop flight", "ipa": "[ˌnɑːn ˈstɑːp flaɪt]", "pos": "명사", "meaning": "직항편"}
                ],
                "explanation": "첫 번째 행의 Flight SQ 601과 비고란의 'Arrives at 2:45 PM'을 명확히 읽어주세요."
            },
            {
                "qId": "p4-s7-q9",
                "qNum": "Question 9",
                "topic": "12월 9일 물류센터 투어 취소 및 만찬 대체 정정",
                "prepTime": 3,
                "responseTime": 15,
                "question": "I would like to accompany David on the Automated Logistics Center Tour on December 9th at 2:00 PM. Is that tour still happening?",
                "questionKo": "12월 9일 오후 2시에 데이비드와 함께 자동화 물류센터 투어에 동행하고 싶습니다. 그 투어가 여전히 진행되나요?",
                "sentences": [
                    {"step": "1. 취소 사실 안내", "en": "No, I'm afraid that tour is not happening.", "ko": "아니요, 유감스럽지만 그 투어는 진행되지 않습니다."},
                    {"step": "2. 취소 및 대체 일정 설명", "en": "The Automated Logistics Center Tour at 2:00 PM has been cancelled.", "ko": "오후 2시의 자동화 물류센터 투어는 취소되었습니다."},
                    {"step": "3. 대체 프로그램 안내", "en": "Instead, it has been replaced by an Executive Dinner at 6:30 PM.", "ko": "대신 오후 6시 30분의 경영진 만찬으로 대체되었습니다."}
                ],
                "magicSentences": [
                    {"en": "Unfortunately, that tour has been cancelled.", "ko": "안타깝게도 그 투어는 취소되었습니다.", "tip": "시계토끼 만능 #117 (취소 안내 수동태)"},
                    {"en": "Instead, it has been replaced by an Executive Dinner at 6:30 PM.", "ko": "대신 오후 6시 30분 경영진 만찬으로 대체되었습니다.", "tip": "시계토끼 만능 #120 (대체 일정 공식)"}
                ],
                "vocabulary": [
                    {"word": "logistics center", "ipa": "[ləˈdʒɪstɪks ˈsentər]", "pos": "명사", "meaning": "물류 센터"},
                    {"word": "executive dinner", "ipa": "[ɪɡˈzekjətɪv ˈdɪnər]", "pos": "명사", "meaning": "경영진/임원 만찬"}
                ],
                "explanation": "표 마지막 행의 'Cancelled - Replaced by Executive Dinner at 6:30 PM'을 설명하세요."
            },
            {
                "qId": "p4-s7-q10",
                "qNum": "Question 10",
                "topic": "첫째 날인 12월 8일에 예정된 모든 일정 상세 안내",
                "prepTime": 3,
                "responseTime": 30,
                "question": "Can you give me all the details about David Miller's schedule on the first day, December 8th?",
                "questionKo": "첫째 날인 12월 8일에 있는 데이비드 밀러의 모든 일정 세부 사항을 알려주시겠어요?",
                "sentences": [
                    {"step": "1. 총 개수 안내", "en": "Sure! There are two major schedules planned on December 8th.", "ko": "물론입니다! 12월 8일에는 두 개의 주요 일정이 계획되어 있습니다."},
                    {"step": "2. 첫 번째 일정 (비행)", "en": "First, at 9:15 AM, he will take Flight SQ 601 from Terminal 3 to Singapore and arrive at 2:45 PM.", "ko": "첫째, 오전 9시 15분에 3번 터미널에서 싱가포르행 SQ 601편에 탑승하여 오후 2시 45분에 도착합니다."},
                    {"step": "3. 두 번째 일정 (회의)", "en": "Second, at 4:30 PM, he has Meeting 1 for the Welcome Briefing and Contract Review with Director Alan Tan at Apex Asia HQ.", "ko": "둘째, 오후 4시 30분에는 아펙스 아시아 본사에서 앨런 탄 이사와 환영 브리핑 및 계약 검토를 위한 회의 1이 있습니다."}
                ],
                "magicSentences": [
                    {"en": "There are two major schedules planned on December 8th.", "ko": "12월 8일에 두 개의 주요 일정이 잡혀 있습니다.", "tip": "시계토끼 만능 #129 (날짜별 일정 요약)"},
                    {"en": "First, he will take Flight SQ 601... Second, at 4:30 PM...", "ko": "첫째 비행기를 탑승하고... 둘째 4:30에는...", "tip": "시계토끼 만능 #131 (시간순 나열)"}
                ],
                "vocabulary": [
                    {"word": "briefing", "ipa": "[ˈbriːfɪŋ]", "pos": "명사", "meaning": "요약 보고, 브리핑"},
                    {"word": "contract review", "ipa": "[ˈkɑːntrækt rɪˈvjuː]", "pos": "명사", "meaning": "계약서 검토"}
                ],
                "explanation": "12월 8일 행 두 개(Flight SQ 601 이동과 4:30 PM 계약 검토 회의)를 차례대로 요약 설명하세요."
            },
            {
                "qId": "p4-s7-q-extra",
                "qNum": "추가 문제 (호텔 및 셔틀)",
                "topic": "숙소 호텔 및 무료 공항 셔틀 제공 여부 안내",
                "prepTime": 3,
                "responseTime": 15,
                "question": "Where will David Miller be staying in Singapore, and does the hotel provide transportation from the airport?",
                "questionKo": "데이비드 밀러는 싱가포르에서 어디에 머무르며, 호텔에서 공항 교통편을 제공하나요?",
                "sentences": [
                    {"step": "1. 숙소 이름 안내", "en": "He will be staying at the Marina Grand Hotel in Singapore.", "ko": "그는 싱가포르의 마리나 그랜드 호텔에 투숙할 예정입니다."},
                    {"step": "2. 무료 셔틀 제공 안내", "en": "Also, the hotel provides a complimentary airport shuttle service for all guests.", "ko": "또한 호텔에서는 모든 투숙객에게 무료 공항 셔틀버스 서비스를 제공합니다."}
                ],
                "magicSentences": [
                    {"en": "He will be staying at the Marina Grand Hotel.", "ko": "그는 마리나 그랜드 호텔에 머물 예정입니다.", "tip": "숙소 안내 공식"},
                    {"en": "The hotel provides a complimentary airport shuttle.", "ko": "호텔에서 무료 공항 셔틀을 제공합니다.", "tip": "시계토끼 만능 #125 (무료 편의시설 안내)"}
                ],
                "vocabulary": [
                    {"word": "complimentary", "ipa": "[ˌkɑːmplɪˈmentri]", "pos": "형용사", "meaning": "무료의"},
                    {"word": "airport shuttle", "ipa": "[ˈerpɔːrt ˈʃʌtl]", "pos": "명사", "meaning": "공항 셔틀버스"}
                ],
                "explanation": "상단 Hotel & Transfer의 'Marina Grand Hotel'과 'Complimentary Airport Shuttle Provided'를 완전한 문장으로 답변하세요."
            }
        ]
    }

    # 신규 세트 8: 스포츠·피트니스 센터 강습표 (4문항)
    t_fitness = {
        "headerTitle": "City Sports Complex - Autumn Fitness & Aquatics Class Schedule",
        "metaInfo": [
            {"label": "Facility Location", "value": "Central District Sports Arena (Near City Hall Station Exit 2)"},
            {"label": "Tuition & Discount", "value": "$70 per month (20% discount for students / Locker fee: $10)"}
        ],
        "rows": [
            {"date": "Mon & Wed", "time": "07:00 AM", "event": "Morning Yoga & Stretching", "location": "Studio A", "note": "Instructor: Chloe Bennett"},
            {"date": "Tue & Thu", "time": "06:30 PM", "event": "Intermediate Swimming Stroke", "location": "Pool Lane 3-4", "note": "Instructor: Mark Davies"},
            {"date": "Friday", "time": "08:00 PM", "event": "High-Intensity Interval Training (HIIT)", "location": "Main Gym", "note": "Instructor: Mark Davies"},
            {"date": "Saturday", "time": "10:00 AM", "event": "Weekend Pilates for Beginners", "location": "Studio B", "note": "Instructor: Chloe Bennett"}
        ]
    }
    set8 = {
        "id": "p4-set8",
        "part": 4,
        "setNum": "Part 4 - Set 8",
        "tableTypeId": "table-fitness",
        "tableTypeName": "스포츠·피트니스 강습",
        "tableTypeBadge": "피트니스 강습표",
        "topic": "City Sports Complex - Autumn Fitness & Swimming Class Schedule",
        "prepTime": 45,
        "scheduleTable": t_fitness,
        "questions": [
            {
                "qId": "p4-s8-q8",
                "qNum": "Question 8",
                "topic": "중급 수영 강습 요일, 시간 및 장소 안내",
                "prepTime": 3,
                "responseTime": 15,
                "question": "On which days is the Intermediate Swimming Stroke class held, and what time does it start?",
                "questionKo": "중급 수영 영법 강습은 무슨 요일에 열리며, 몇 시에 시작하나요?",
                "sentences": [
                    {"step": "1. 요일 및 시간 안내", "en": "The Intermediate Swimming Stroke class is held on Tuesdays and Thursdays at 6:30 PM.", "ko": "중급 수영 영법 강습은 화요일과 목요일 오후 6시 30분에 열립니다."},
                    {"step": "2. 장소 및 강사 안내", "en": "It takes place in Pool Lane 3 and 4, taught by Mark Davies.", "ko": "수영장 3~4번 레인에서 진행되며 마크 데이비스 강사가 지도합니다."}
                ],
                "magicSentences": [
                    {"en": "It is held on Tuesdays and Thursdays at 6:30 PM.", "ko": "화요일과 목요일 오후 6시 30분에 열립니다.", "tip": "시계토끼 만능 #103 & #106 (요일 시간 공식)"}
                ],
                "vocabulary": [
                    {"word": "intermediate", "ipa": "[ˌɪntərˈmiːdiət]", "pos": "형용사", "meaning": "중급의"},
                    {"word": "swimming stroke", "ipa": "[ˈswɪmɪŋ stroʊk]", "pos": "명사", "meaning": "수영 영법"}
                ],
                "explanation": "두 번째 행의 'Tue & Thu', '06:30 PM', 'Pool Lane 3-4'를 완전한 문장으로 답변하세요."
            },
            {
                "qId": "p4-s8-q9",
                "qNum": "Question 9",
                "topic": "금요일 HIIT 강습 시간 오류 정정",
                "prepTime": 3,
                "responseTime": 15,
                "question": "I would like to join the Friday High-Intensity Interval Training class. Does it start at 6:00 PM?",
                "questionKo": "금요일 고강도 인터벌 트레이닝(HIIT) 수업에 참여하고 싶습니다. 오후 6시에 시작하나요?",
                "sentences": [
                    {"step": "1. 시간 오류 정정", "en": "No, I'm afraid that is not correct.", "ko": "아니요, 유감스럽지만 그것은 맞지 않습니다."},
                    {"step": "2. 정확한 시작 시각 안내", "en": "The Friday High-Intensity Interval Training class starts at 8:00 PM, not 6:00 PM.", "ko": "금요일 고강도 인터벌 트레이닝 수업은 오후 6시가 아니라 오후 8시에 시작합니다."},
                    {"step": "3. 장소 확인", "en": "It will take place in the Main Gym with instructor Mark Davies.", "ko": "메인 체육관에서 마크 데이비스 강사와 함께 진행될 예정입니다."}
                ],
                "magicSentences": [
                    {"en": "No, that is not correct. It starts at 8:00 PM, not 6:00 PM.", "ko": "아니요, 그렇지 않습니다. 6시가 아니라 8시에 시작합니다.", "tip": "시계토끼 만능 #114 (시각 정정 공식)"}
                ],
                "vocabulary": [
                    {"word": "high-intensity", "ipa": "[haɪ ɪnˈtensəti]", "pos": "형용사", "meaning": "고강도의"},
                    {"word": "interval training", "ipa": "[ˈɪntərvl ˈtreɪnɪŋ]", "pos": "명사", "meaning": "인터벌 훈련"}
                ],
                "explanation": "표 세 번째 행의 Friday 수업 시간은 08:00 PM이므로 시간을 올바르게 정정하세요."
            },
            {
                "qId": "p4-s8-q10",
                "qNum": "Question 10",
                "topic": "클로이 베넷(Chloe Bennett) 강사가 지도하는 모든 강습 2가지 상세 안내",
                "prepTime": 3,
                "responseTime": 30,
                "question": "I am a big fan of Chloe Bennett's fitness classes. Could you tell me all the classes she will be teaching?",
                "questionKo": "저는 클로이 베넷 강사의 피트니스 수업 팬입니다. 그녀가 지도할 모든 강습을 알려주실 수 있나요?",
                "sentences": [
                    {"step": "1. 총 개수 안내", "en": "Sure! There are two classes taught by Chloe Bennett.", "ko": "물론입니다! 클로이 베넷이 가르치는 수업은 두 개가 있습니다."},
                    {"step": "2. 첫 번째 강습 (평일 요가)", "en": "First, on Mondays and Wednesdays at 7:00 AM, she teaches Morning Yoga and Stretching in Studio A.", "ko": "첫째, 월요일과 수요일 오전 7시에 스튜디오 A에서 아침 요가 및 스트레칭을 가르칩니다."},
                    {"step": "3. 두 번째 강습 (주말 필라테스)", "en": "Second, on Saturdays at 10:00 AM, she leads Weekend Pilates for Beginners in Studio B.", "ko": "둘째, 토요일 오전 10시에는 스튜디오 B에서 초보자를 위한 주말 필라테스를 진행합니다."}
                ],
                "magicSentences": [
                    {"en": "There are two classes taught by Chloe Bennett.", "ko": "클로이 베넷이 지도하는 수업이 두 개 있습니다.", "tip": "시계토끼 만능 #129 (강사별 강습 요약)"},
                    {"en": "First, on Mondays and Wednesdays... Second, on Saturdays...", "ko": "첫째 월수에는... 둘째 토요일에는...", "tip": "시계토끼 만능 #131 (요일 순차 안내)"}
                ],
                "vocabulary": [
                    {"word": "stretching", "ipa": "[ˈstretʃɪŋ]", "pos": "명사", "meaning": "스트레칭"},
                    {"word": "beginners", "ipa": "[bɪˈɡɪnərz]", "pos": "명사", "meaning": "초보자들"}
                ],
                "explanation": "첫 번째 행(월수 아침 요가)과 네 번째 행(토요일 오전 초보자 필라테스) 두 수업의 요일, 시간, 스튜디오를 차례로 설명하세요."
            },
            {
                "qId": "p4-s8-q-extra",
                "qNum": "추가 문제 (수강료 및 할인)",
                "topic": "월 수강료, 학생 할인 혜택 및 락커 이용료 안내",
                "prepTime": 3,
                "responseTime": 15,
                "question": "How much is the monthly tuition fee, and is there any discount available for students?",
                "questionKo": "월 수강료는 얼마이며, 학생을 위한 할인 혜택이 있나요?",
                "sentences": [
                    {"step": "1. 수강료 및 학생 할인 안내", "en": "The monthly tuition is $70, and students can receive a 20% discount.", "ko": "월 수강료는 70달러이며, 학생은 20% 할인을 받을 수 있습니다."},
                    {"step": "2. 락커 이용료 추가 안내", "en": "Also, an optional personal locker is available for an additional fee of $10 per month.", "ko": "또한 개인 락커는 월 10달러의 추가 비용으로 이용하실 수 있습니다."}
                ],
                "magicSentences": [
                    {"en": "The monthly tuition is 70 dollars, and students receive a 20% discount.", "ko": "월 수강료는 70달러이며 학생은 20% 할인을 받습니다.", "tip": "시계토끼 만능 #123 (수강료 및 할인 공식)"}
                ],
                "vocabulary": [
                    {"word": "tuition", "ipa": "[tuˈɪʃn]", "pos": "명사", "meaning": "수강료"},
                    {"word": "personal locker", "ipa": "[ˈpɜːrsənl ˈlɑːkər]", "pos": "명사", "meaning": "개인 사물함"}
                ],
                "explanation": "상단의 '$70 per month', '20% discount for students', 'Locker fee: $10'을 완전한 문장으로 설명하세요."
            }
        ]
    }

    all_p4_sets = old_p4_sets + [set6, set7, set8]

    # 마스터 데이터 조합
    total_p4_q = sum(len(s["questions"]) for s in all_p4_sets)

    new_master = dict(master)
    new_master["counts"]["part3"] = len(p3_final)
    new_master["counts"]["part4"] = total_p4_q
    new_master["counts"]["totalQuestions"] = (
        len(new_master["part1"]) +
        len(new_master["part2"]) +
        len(p3_final) +
        total_p4_q +
        len(new_master["part5"])
    )

    new_master["part3Types"] = [
        {"id": "ALL", "name": f"전체 유형 ({len(p3_final)}문항)"},
        {"id": "p3-t1", "name": "유형 1: 시점·최근 경험 (6문항)"},
        {"id": "p3-t2", "name": "유형 2: 빈도·장소·동행인 (6문항)"},
        {"id": "p3-t3", "name": "유형 3: 양자택일 선호도·찬반 (6문항)"},
        {"id": "p3-t4", "name": "유형 4: 3자택일 최적 선택 (6문항)"},
        {"id": "p3-t5", "name": "유형 5: 장단점·중요 이유 (6문항)"}
    ]

    new_master["part4TableTypes"] = [
        {"id": "ALL", "name": f"전체 표 속성 ({len(all_p4_sets)}개 세트 · {total_p4_q}문항)"},
        {"id": "table-conf", "name": "컨퍼런스·학술 심포지엄"},
        {"id": "table-museum", "name": "박물관 전시·문화 강연"},
        {"id": "table-training", "name": "사내 직원 연수·워크숍"},
        {"id": "table-tour", "name": "여행·시티 투어 여정표"},
        {"id": "table-interview", "name": "인사 채용 면접·이력 요약"},
        {"id": "table-medical", "name": "병원·건강 세미나 일정표"},
        {"id": "table-itinerary", "name": "비행·해외 출장 일정표"},
        {"id": "table-fitness", "name": "스포츠·피트니스 강습표"}
    ]

    new_master["part3"] = p3_final
    new_master["part4"] = all_p4_sets

    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(new_master, f, ensure_ascii=False, indent=2)

    print(f"✅ data/toeic_parts_master.json 갱신 완료!")
    print(f"   - Part 3 문항 수: {len(p3_final)} (5개 유형 × 6문제 = 총 30문제)")
    print(f"   - Part 3 번호 형식: {p3_final[0]['qNum']} ~ {p3_final[-1]['qNum']} (깔끔한 #번호만 유지)")
    print(f"   - Part 4 세트 수: {len(all_p4_sets)}개 세트 (총 {total_p4_q}문제 보충)")
    print(f"   - 전체 문항 수: {new_master['counts']['totalQuestions']}문항")

if __name__ == "__main__":
    run_update()

