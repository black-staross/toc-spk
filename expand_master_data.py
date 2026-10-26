import json

with open('data.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

p4_additional_sets = [
    {
        "setNumber": 6,
        "title": "Set 6: City Sightseeing Tour (도시 일일 관광 투어 일정표)",
        "topic": "Travel Tour Itinerary",
        "context": "Hello, this is Robert King. I am booked on tomorrow's City Sightseeing Tour. Could you answer a few questions about our itinerary?",
        "context_kr": "안녕하세요, 로버트 킹입니다. 내일 도시 관광 투어 예약자인데 일정표에 대해 몇 가지 질문드려도 될까요?",
        "table": {
            "headerTitle": "Grand City Sightseeing Tour - Daily Itinerary",
            "metaInfo": [
                {"label": "Departure Date", "value": "Wednesday, August 22"},
                {"label": "Meeting Point", "value": "Central Station Exit 3, Tour Bus Bay"}
            ],
            "rows": [
                {"time": "08:30 AM", "destination": "Meeting & Bus Boarding", "activity": "Attendance check & route guide", "guide": "Tour Leader Alex"},
                {"time": "09:30 AM - 11:30 AM", "destination": "Historic Castle Tour", "activity": "Guided walking tour", "guide": "Tour Leader Alex"},
                {"time": "12:00 PM - 01:30 PM", "destination": "Harbor Seafood Market", "activity": "Free time for lunch", "guide": "Self-guided"},
                {"time": "02:00 PM - 04:00 PM", "destination": "Modern Art Museum", "activity": "Exhibition viewing & souvenir shop", "guide": "Tour Leader Alex"}
            ]
        },
        "questions": [
            {
                "qNumber": "Question 8",
                "prepTime": 3,
                "responseTime": 15,
                "question": "Where is the meeting point for the tour,\nand what time do we meet?",
                "questionTranslation": "투어 집합 장소는 어디이고,\n몇 시에 모이나요?",
                "keyPattern": "Q8 집합 장소 및 시간",
                "answer": "The meeting point is at Central Station Exit 3 at the Tour Bus Bay,\nand you should meet at 8:30 AM for bus boarding.",
                "answerTranslation": "집합 장소는 중앙역 3번 출구 투어 버스 승강장이며,\n버스 탑승을 위해 오전 8시 30분까지 모이셔야 합니다.",
                "magicSentences": [
                    "The meeting point is [Location], and we meet at [Time]. (모이는 장소는 [장소]이며 [시간]에 모입니다)"
                ],
                "scoreTip": "상단 메타 정보의 Meeting Point와 첫 행의 08:30 AM을 결합하여 명확히 전달하세요.",
                "vocabulary": [
                    {"word": "meeting point", "ipa": "[ˈmiːtɪŋ pɔɪnt]", "pos": "명사구", "meaning": "집합 장소"},
                    {"word": "boarding", "ipa": "[ˈbɔːdɪŋ]", "pos": "명사", "meaning": "탑승"}
                ]
            },
            {
                "qNumber": "Question 9",
                "prepTime": 3,
                "responseTime": 15,
                "question": "Is lunch provided by the tour company at the Harbor Seafood Market?",
                "questionTranslation": "항구 수산시장에서 점심 식사가 여행사 측에서 제공되나요?",
                "keyPattern": "Q9 자유 시간 및 개별 식사 예외 정정",
                "answer": "No, I'm afraid that you have the wrong information.\nLunch is not provided by the company.\nActually, from 12:00 PM to 1:30 PM, you will have free time for self-guided lunch.",
                "answerTranslation": "아니요, 잘못 알고 계신 것 같습니다.\n회사에서 점심을 제공하지 않습니다.\n사실 12시부터 1시 30분까지 개별 식사를 위한 자유 시간입니다.",
                "magicSentences": [
                    "No, I'm afraid that you have the wrong information. Actually, you have free time. (아니요, 잘못 아셨습니다. 사실 자유 시간입니다)"
                ],
                "scoreTip": "표에서 'Free time for lunch (Self-guided)'로 표기된 항목을 짚어줍니다.",
                "vocabulary": [
                    {"word": "self-guided", "ipa": "[self ˈɡaɪdɪd]", "pos": "형용사", "meaning": "자유로운, 자율적인"},
                    {"word": "seafood", "ipa": "[ˈsiːfuːd]", "pos": "명사", "meaning": "해산물"}
                ]
            },
            {
                "qNumber": "Question 10",
                "prepTime": 3,
                "responseTime": 30,
                "question": "Can you give me all the details about the itinerary activities led by Tour Leader Alex?",
                "questionTranslation": "투어 리더 알렉스가 인솔하는 모든 일정 활동에 대해 말씀해 주시겠습니까?",
                "keyPattern": "Q10 특정 인솔자 세션 2개 나열",
                "answer": "Sure, there are two main tour activities led by Tour Leader Alex.\nFirst, from 9:30 AM to 11:30 AM, he will guide a walking tour at the Historic Castle.\nSecond, from 2:00 PM to 4:00 PM, he will lead the group to the Modern Art Museum for exhibition viewing and souvenir shopping.\nThese are the two guided activities by Alex.",
                "answerTranslation": "네, 투어 리더 알렉스가 인솔하는 주요 투어 활동은 2개입니다.\n첫째, 오전 9시 30분부터 11시 30분까지 역사적인 고성에서 도보 가이드 투어를 진행합니다.\n둘째, 오후 2시부터 4시까지 현대 미술관에서 전시 관람 및 기념품 쇼핑을 인솔합니다.\n이것이 알렉스가 안내하는 두 가지 활동입니다.",
                "magicSentences": [
                    "Sure, there are two activities led by [Guide]. (네, [가이드]가 이끄는 2가지 활동이 있습니다)"
                ],
                "scoreTip": "가이드 열에서 Alex가 적힌 9:30 AM 고성과 2:00 PM 미술관 2곳을 차례로 나열하세요.",
                "vocabulary": [
                    {"word": "historic castle", "ipa": "[hɪˈstɒrɪk ˈkɑːsl]", "pos": "명사구", "meaning": "유서 깊은 고성"},
                    {"word": "souvenir", "ipa": "[ˌsuːvəˈnɪə(r)]", "pos": "명사", "meaning": "기념품"}
                ]
            }
        ]
    },
    {
        "setNumber": 7,
        "title": "Set 7: Healthcare & Medical Seminar (의료 건강 세미나 일정표)",
        "topic": "Medical Seminar",
        "context": "Hello, this is Dr. William Clark. I am registered for the Healthcare Seminar on Friday and would like to confirm some details.",
        "context_kr": "안녕하세요, 윌리엄 클라크 박사입니다. 금요일 헬스케어 세미나 등록자인데 몇 가지 사항을 확인하고자 합니다.",
        "table": {
            "headerTitle": "Modern Healthcare & Wellness Seminar - Schedule",
            "metaInfo": [
                {"label": "Date", "value": "Friday, November 16"},
                {"label": "Location", "value": "City General Hospital, Auditorium A"}
            ],
            "rows": [
                {"time": "09:00 AM - 10:30 AM", "session": "Preventive Cardiology Trends", "speaker": "Dr. Susan Miller", "room": "Hall 1"},
                {"time": "11:00 AM - 12:30 PM", "session": "New Diabetes Treatment Protocols", "speaker": "Dr. Alan Green", "room": "Hall 2"},
                {"time": "02:00 PM - 03:30 PM", "session": "Hospital Telemedicine Systems", "speaker": "Dr. Susan Miller", "room": "Hall 1"},
                {"time": "04:00 PM - 05:00 PM", "session": "Patient Data Security Workshop", "speaker": "IT Director John Park", "room": "Lab 3"}
            ]
        },
        "questions": [
            {
                "qNumber": "Question 8",
                "prepTime": 3,
                "responseTime": 15,
                "question": "What is the date of the seminar,\nand where is it being held?",
                "questionTranslation": "세미나 날짜는 언제이고,\n어디서 열리나요?",
                "keyPattern": "Q8 세미나 일시 및 장소",
                "answer": "The seminar will be held on Friday, November 16th,\nat Auditorium A in City General Hospital.",
                "answerTranslation": "세미나는 11월 16일 금요일에 시립 종합병원 대강당 A에서 열립니다.",
                "magicSentences": [
                    "The seminar will be held on [Date] at [Location]. (세미나는 [날짜]에 [장소]에서 열립니다)"
                ],
                "scoreTip": "상단 정보의 날짜와 장소를 바로 읽어주세요.",
                "vocabulary": [
                    {"word": "auditorium", "ipa": "[ˌɔːdɪˈtɔːriəm]", "pos": "명사", "meaning": "강당, 대강의실"},
                    {"word": "preventive", "ipa": "[prɪˈventɪv]", "pos": "형용사", "meaning": "예방의, 예방을 위한"}
                ]
            },
            {
                "qNumber": "Question 9",
                "prepTime": 3,
                "responseTime": 15,
                "question": "I heard that the session on Diabetes Treatment starts at 2:00 PM.\nIs that correct?",
                "questionTranslation": "당뇨병 치료 세션이 오후 2시에 시작한다고 들었는데,\n맞나요?",
                "keyPattern": "Q9 오류 정정 공식 (#7)",
                "answer": "No, I'm afraid that you have the wrong information.\nActually, the session on Diabetes Treatment Protocols starts at 11:00 AM in Hall 2.",
                "answerTranslation": "아니요, 잘못 알고 계신 것 같습니다.\n사실 당뇨병 치료 프로토콜 세션은 오전 11시에 2번 홀에서 시작합니다.",
                "magicSentences": [
                    "No, I'm afraid that you have the wrong information. Actually, it starts at [Correct Time]. (아니요, 잘못 아셨습니다. 사실 [시간]에 시작합니다)"
                ],
                "scoreTip": "오후 2시가 아니라 오전 11시(11:00 AM)로 정정하세요.",
                "vocabulary": [
                    {"word": "protocol", "ipa": "[ˈprəʊtəkɒl]", "pos": "명사", "meaning": "치료 지침, 프로토콜"},
                    {"word": "treatment", "ipa": "[ˈtriːtmənt]", "pos": "명사", "meaning": "치료, 처치"}
                ]
            },
            {
                "qNumber": "Question 10",
                "prepTime": 3,
                "responseTime": 30,
                "question": "I would like to attend all sessions presented by Dr. Susan Miller.\nCould you give me all the details about her presentations?",
                "questionTranslation": "수잔 밀러 박사님이 발표하시는 모든 세션에 참석하고 싶습니다.\n그녀의 발표에 대한 모든 세부 사항을 알려주실 수 있나요?",
                "keyPattern": "Q10 공통 연사 2개 세션 나열",
                "answer": "Sure, there are two sessions presented by Dr. Susan Miller.\nFirst, from 9:00 AM to 10:30 AM, she will speak about Preventive Cardiology Trends in Hall 1.\nSecond, from 2:00 PM to 3:30 PM, she will lead a session on Hospital Telemedicine Systems in Hall 1.\nThese are the two sessions by Dr. Miller.",
                "answerTranslation": "네, 수잔 밀러 박사님이 발표하시는 두 개의 세션이 있습니다.\n첫째, 오전 9시부터 10시 30분까지 1번 홀에서 예방 심장학 트렌드에 대해 발표하십니다.\n둘째, 오후 2시부터 3시 30분까지 1번 홀에서 병원 원격 의료 시스템에 관한 세션을 진행하십니다.\n이것이 밀러 박사님의 두 세션입니다.",
                "magicSentences": [
                    "Sure, there are two sessions presented by [Name]. (네, [이름] 박사의 세션 2개가 있습니다)"
                ],
                "scoreTip": "Dr. Susan Miller의 두 세션 모두 Hall 1에서 열린다는 점과 시간을 조리 있게 설명하세요.",
                "vocabulary": [
                    {"word": "telemedicine", "ipa": "[ˌtelɪˈmedsn]", "pos": "명사", "meaning": "원격 의료"},
                    {"word": "cardiology", "ipa": "[ˌkɑːdiˈɒlədʒi]", "pos": "명사", "meaning": "심장학"}
                ]
            }
        ]
    },
    {
        "setNumber": 8,
        "title": "Set 8: Company Orientation Day (신입사원 온보딩 오리엔테이션)",
        "topic": "Onboarding Orientation Schedule",
        "context": "Hello, this is Jenny from Human Resources. I am calling to check the orientation schedule for our new employees this Monday.",
        "context_kr": "안녕하세요, 인사팀 제니입니다. 이번 주 월요일 신입사원 오리엔테이션 일정을 확인하고자 전화드렸습니다.",
        "table": {
            "headerTitle": "TechNova Corp - New Employee Orientation Agenda",
            "metaInfo": [
                {"label": "Date", "value": "Monday, March 5"},
                {"label": "Location", "value": "HQ Conference Hall (5th Floor)"}
            ],
            "rows": [
                {"time": "09:00 AM - 10:00 AM", "program": "CEO Welcome Speech & Company Vision", "presenter": "CEO Brian Scott", "venue": "Main Hall"},
                {"time": "10:30 AM - 12:00 PM", "program": "IT Setup & Security Guidelines", "presenter": "IT Manager Daniel Lee", "venue": "Lab 5"},
                {"time": "12:00 PM - 01:30 PM", "program": "Welcome Buffet Lunch", "presenter": "All Team Leaders", "venue": "Cafeteria"},
                {"time": "01:30 PM - 03:00 PM", "program": "HR Policies & Benefits Overview", "presenter": "HR Director Jenny Kim", "venue": "Main Hall"}
            ]
        },
        "questions": [
            {
                "qNumber": "Question 8",
                "prepTime": 3,
                "responseTime": 15,
                "question": "What is the first session of the orientation,\nand who will lead it?",
                "questionTranslation": "오리엔테이션의 첫 번째 세션은 무엇이고,\n누가 진행하나요?",
                "keyPattern": "Q8 첫 프로그램 및 발표자",
                "answer": "The first session is the CEO Welcome Speech and Company Vision,\nand it will be delivered by CEO Brian Scott at 9:00 AM in the Main Hall.",
                "answerTranslation": "첫 번째 세션은 대표이사 환영사 및 회사 비전 공유이며,\n오전 9시에 메인 홀에서 브라이언 스콧 대표가 진행합니다.",
                "magicSentences": [
                    "The first session is [Program], and it will be led by [Presenter]. (첫 세션은 [프로그램]이며 [발표자]가 진행합니다)"
                ],
                "scoreTip": "첫 행의 프로그램명과 발표자 CEO Brian Scott을 전달하세요.",
                "vocabulary": [
                    {"word": "orientation", "ipa": "[ˌɔːriənˈteɪʃn]", "pos": "명사", "meaning": "오리엔테이션, 예비 교육"},
                    {"word": "vision", "ipa": "[ˈvɪʒn]", "pos": "명사", "meaning": "비전, 미래상"}
                ]
            },
            {
                "qNumber": "Question 9",
                "prepTime": 3,
                "responseTime": 15,
                "question": "Is the IT Security Guidelines session scheduled to take place in the Main Hall?",
                "questionTranslation": "IT 보안 지침 세션이 메인 홀에서 열리는 것으로 예정되어 있나요?",
                "keyPattern": "Q9 장소 오류 정정 공식 (#7)",
                "answer": "No, I'm afraid that you have the wrong information.\nActually, the IT Setup and Security session will take place in Lab 5 on the 5th floor.",
                "answerTranslation": "아니요, 잘못 알고 계신 것 같습니다.\n사실 IT 세팅 및 보안 세션은 5층 5번 랩실에서 진행됩니다.",
                "magicSentences": [
                    "No, I'm afraid that you have the wrong information. Actually, it will take place in [Venue]. (아니요, 잘못 아셨습니다. 사실 [장소]에서 열립니다)"
                ],
                "scoreTip": "메인 홀이 아니라 Lab 5로 장소를 정정하세요.",
                "vocabulary": [
                    {"word": "guideline", "ipa": "[ˈɡaɪdlaɪn]", "pos": "명사", "meaning": "지침, 가이드라인"},
                    {"word": "venue", "ipa": "[ˈvenjuː]", "pos": "명사", "meaning": "개최 장소"}
                ]
            },
            {
                "qNumber": "Question 10",
                "prepTime": 3,
                "responseTime": 30,
                "question": "Could you tell me all the sessions scheduled to take place in the Main Hall?",
                "questionTranslation": "메인 홀에서 열리도록 예정된 모든 세션에 대해 말씀해 주시겠습니까?",
                "keyPattern": "Q10 동일 장소(Main Hall) 세션 2개 나열",
                "answer": "Sure, there are two sessions scheduled in the Main Hall.\nFirst, from 9:00 AM to 10:00 AM, there is the CEO Welcome Speech and Company Vision by CEO Brian Scott.\nSecond, from 1:30 PM to 3:00 PM, there is the HR Policies and Benefits Overview presented by HR Director Jenny Kim.\nThese are the two sessions in the Main Hall.",
                "answerTranslation": "네, 메인 홀에서 예정된 세션은 2개입니다.\n첫째, 오전 9시부터 10시까지 브라이언 스콧 대표의 환영사 및 비전 공유가 있습니다.\n둘째, 오후 1시 30분부터 3시까지 제니 킴 인사이사의 인사 정책 및 복지 개요 세션이 있습니다.\n이것이 메인 홀에서 진행되는 두 세션입니다.",
                "magicSentences": [
                    "Sure, there are two sessions scheduled in [Venue]. (네, [장소]에서 2개 세션이 예정되어 있습니다)"
                ],
                "scoreTip": "Venue 열에서 'Main Hall'로 표기된 9:00 AM과 1:30 PM 세션을 짝지어 나열합니다.",
                "vocabulary": [
                    {"word": "benefit", "ipa": "[ˈbenɪfɪt]", "pos": "명사", "meaning": "복리후생, 혜택"},
                    {"word": "policy", "ipa": "[ˈpɒləsi]", "pos": "명사", "meaning": "정책, 규정"}
                ]
            }
        ]
    }
]

master["part4"] = master["part4"] + p4_additional_sets
master["metadata"]["part3_count"] = len(master["part3"])
master["metadata"]["part4_count"] = sum(len(s["questions"]) for s in master["part4"])
master["metadata"]["part4_sets_count"] = len(master["part4"])

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print(f"Final Part 3 Count: {master['metadata']['part3_count']} questions (16 sets)")
print(f"Final Part 4 Count: {master['metadata']['part4_count']} questions ({master['metadata']['part4_sets_count']} sets)")
