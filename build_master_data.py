import json

# Load existing Part 3 data
with open('data.json', 'r', encoding='utf-8') as f:
    existing_p3 = json.load(f)

# Add Desserts Set (Set 16) from user's uploaded sample
desserts_set = [
    {
        "id": 46,
        "setNumber": 16,
        "setTitle": "Set 16: Desserts & Bakeries (디저트 & 베이커리)",
        "questionNumber": "Question 5",
        "prepTime": 3,
        "responseTime": 15,
        "question": "What kind of desserts do you enjoy eating the most,\nand how often do you eat them?",
        "questionTranslation": "어떤 종류의 디저트를 가장 즐겨 먹고,\n얼마나 자주 드시나요?",
        "keyPattern": "종류 + 빈도 공식 (기분 전환 만능문장)",
        "answer": "I enjoy eating chocolate cake the most,\nand I eat it about once or twice a week.\nIt relieves my stress and puts me in a good mood.",
        "answerTranslation": "저는 초콜릿 케이크를 가장 즐겨 먹고,\n일주일에 한두 번 정도 먹습니다.\n스트레스를 풀어주고 기분을 좋게 만들어 줍니다.",
        "magicSentences": [
            "It relieves my stress and puts me in a good mood. (스트레스를 풀어주고 기분을 좋게 해줍니다)"
        ],
        "scoreTip": "디저트 질문에는 'chocolate cake'나 'ice cream'을 말하고 만능문장 'relieves my stress'를 바로 붙이세요.",
        "vocabulary": [
            {"word": "dessert", "ipa": "[dɪˈzɜːt]", "pos": "명사", "meaning": "디저트, 후식"},
            {"word": "relieve stress", "ipa": "[rɪˈliːv stres]", "pos": "동사구", "meaning": "스트레스를 풀다"},
            {"word": "good mood", "ipa": "[ɡʊd muːd]", "pos": "명사구", "meaning": "좋은 기분, 상쾌한 상태"},
            {"word": "sweet", "ipa": "[swiːt]", "pos": "형용사", "meaning": "달콤한, 맛있는"}
        ]
    },
    {
        "id": 47,
        "setNumber": 16,
        "setTitle": "Set 16: Desserts & Bakeries (디저트 & 베이커리)",
        "questionNumber": "Question 6",
        "prepTime": 3,
        "responseTime": 15,
        "question": "When you buy desserts, do you prefer going to a bakery near your house or ordering online?\nWhy?",
        "questionTranslation": "디저트를 살 때 집 근처 베이커리에 가는 것을 선호하나요, 아니면 온라인으로 주문하는 것을 선호하나요?\n왜 그런가요?",
        "keyPattern": "선호도 비교 (시간 절약 & 신선함)",
        "answer": "I prefer going to a bakery near my house.\nBecause it is close, so it is faster and I can save time.\nAlso, the bread and pastries are very fresh.",
        "answerTranslation": "저는 집 근처 베이커리에 가는 것을 선호합니다.\n가까워서 더 빠르고 시간을 절약할 수 있기 때문입니다.\n또한 빵과 과자가 매우 신선합니다.",
        "magicSentences": [
            "It is close, so it is faster and I can save time. (가까워서 더 빠르고 시간을 절약할 수 있습니다)",
            "The items are very fresh. (제품이 매우 신선합니다)"
        ],
        "scoreTip": "집 근처 장소를 고르면 'close to my house' + 'save time' 만능문장으로 15초를 쉽게 채울 수 있습니다.",
        "vocabulary": [
            {"word": "bakery", "ipa": "[ˈbeɪkəri]", "pos": "명사", "meaning": "제과점, 빵집"},
            {"word": "pastry", "ipa": "[ˈpeɪstri]", "pos": "명사", "meaning": "페이스트리, 구운 과자"},
            {"word": "fresh", "ipa": "[freʃ]", "pos": "형용사", "meaning": "신선한, 갓 구운"},
            {"word": "save time", "ipa": "[seɪv taɪm]", "pos": "동사구", "meaning": "시간을 아끼다"}
        ]
    },
    {
        "id": 48,
        "setNumber": 16,
        "setTitle": "Set 16: Desserts & Bakeries (디저트 & 베이커리)",
        "questionNumber": "Question 7",
        "prepTime": 3,
        "responseTime": 30,
        "question": "If you had to serve dessert to guests, which one would you choose?\n(Cake / Fruit pie / Ice cream)",
        "questionTranslation": "손님에게 디저트를 대접해야 한다면 다음 중 무엇을 고르시겠습니까?\n(케이크 / 과일 파이 / 아이스크림)",
        "keyPattern": "선택형 30초 (인기 아이템 + 가성비 + 시간 절약)",
        "answer": "If I had to serve dessert to guests, I would choose cake.\nFirst of all, it is a very popular item, so people will love it.\nEveryone enjoys eating sweet cake at a party.\nIn addition, the price is reasonable and I can easily buy it at a nearby bakery, so I can save time.\nTherefore, cake is the best choice to serve to guests.",
        "answerTranslation": "손님들에게 디저트를 대접해야 한다면, 저는 케이크를 선택하겠습니다.\n우선 매우 인기 있는 품목이라 사람들이 아주 좋아할 것입니다.\n파티에서 달콤한 케이크를 먹는 것은 누구나 즐깁니다.\n게다가 가격이 합리적이고 근처 빵집에서 쉽게 살 수 있어 시간을 절약할 수 있습니다.\n그러므로 손님에게 대접하기에는 케이크가 최선의 선택입니다.",
        "magicSentences": [
            "It is a popular item, so people will love it. (인기 있는 품목이라 사람들이 좋아할 것입니다)",
            "The price is reasonable, so I can save money. (가격이 합리적이라 돈을 아낄 수 있습니다)",
            "I can save time. (시간을 절약할 수 있습니다)"
        ],
        "scoreTip": "선택형 30초는 'If I had to ~ I would choose [선택]'으로 서론을 열고, '인기 아이템(#37)' + '합리적 가격(#3)' + '시간 절약(#4)'을 결합하세요.",
        "vocabulary": [
            {"word": "serve", "ipa": "[sɜːv]", "pos": "동사", "meaning": "(음식을) 대접하다, 차려내다"},
            {"word": "guest", "ipa": "[ɡest]", "pos": "명사", "meaning": "손님, 하객"},
            {"word": "popular item", "ipa": "[ˈpɒpjələ ˈaɪtəm]", "pos": "명사구", "meaning": "대중적인 인기 품목"},
            {"word": "reasonable", "ipa": "[ˈriːznəbl]", "pos": "형용사", "meaning": "합리적인, 적당한"},
            {"word": "nearby", "ipa": "[ˌnɪəˈbaɪ]", "pos": "형용사/부사", "meaning": "인근의, 가까운 곳에"}
        ]
    }
]

part3_data = existing_p3 + desserts_set

# Part 4 Datasets: 10 Comprehensive High-Frequency Exam Sets
part4_sets = [
    {
        "setNumber": 1,
        "title": "Set 1: Museum Event Schedule (박물관 5월 행사 일정표)",
        "topic": "Museum Event Schedule",
        "context": "Hello, this is Green Library Museum. I am calling to inquire about the upcoming May events schedule. Could you please answer a few questions?",
        "context_kr": "안녕하세요, 그린 박물관입니다. 다가오는 5월 행사 일정에 대해 문의드리고자 전화드렸습니다. 몇 가지 질문에 답해주실 수 있나요?",
        "table": {
            "headerTitle": "Green Library Museum - May Event Schedule",
            "metaInfo": [
                {"label": "Location", "value": "Main Exhibition Hall & Conference Room B"},
                {"label": "Admission", "value": "Free for museum members ($10 for non-members)"}
            ],
            "rows": [
                {"date": "May 5", "time": "10:00 AM", "event": "New Collection Introduction", "location": "Room 101", "note": "Led by Curator David Smith"},
                {"date": "May 12", "time": "2:00 PM", "event": "Historic Preservation Lecture", "location": "Conf. Room B", "note": "Guest Speaker Dr. Emily Brown"},
                {"date": "May 19", "time": "11:00 AM", "event": "Kids Art Workshop", "location": "Outdoor Plaza", "note": "Pre-registration required"},
                {"date": "May 26", "time": "3:00 PM", "event": "Ancient Sculpture Seminar", "location": "Conf. Room B", "note": "Led by Dr. Emily Brown"}
            ]
        },
        "questions": [
            {
                "qNumber": "Question 8",
                "prepTime": 3,
                "responseTime": 15,
                "question": "What is the first event scheduled in May,\nand where will it be held?",
                "questionTranslation": "5월에 예정된 첫 번째 행사는 무엇이고,\n어디서 열리나요?",
                "keyPattern": "Q8 기본 정보 확인 공식 (일시 + 장소)",
                "answer": "The first event is the New Collection Introduction,\nand it will be held in Room 101 at 10:00 AM on May 5th.",
                "answerTranslation": "첫 번째 행사는 '새로운 컬렉션 소개'이며,\n5월 5일 오전 10시에 101호실에서 열릴 예정입니다.",
                "magicSentences": [
                    "The [Event] will be held in [Location] at [Time] on [Date]. (행사는 [일시]에 [장소]에서 열립니다)"
                ],
                "scoreTip": "표 맨 위 첫 번째 항목을 읽어주면 됩니다. 'The first event is [행사], and it will be held in [장소]' 공식을 쓰세요.",
                "vocabulary": [
                    {"word": "scheduled", "ipa": "[ˈskedʒuːld]", "pos": "형용사", "meaning": "예정된"},
                    {"word": "exhibition", "ipa": "[ˌeksɪˈbɪʃn]", "pos": "명사", "meaning": "전시회, 전람회"},
                    {"word": "introduction", "ipa": "[ˌɪntrəˈdʌkʃn]", "pos": "명사", "meaning": "소개, 도입"}
                ]
            },
            {
                "qNumber": "Question 9",
                "prepTime": 3,
                "responseTime": 15,
                "question": "If I remember correctly, the lecture on historic preservation is scheduled to start at 5:00 PM.\nIs that correct?",
                "questionTranslation": "제가 기억하기로는 역사 보존 강연이 오후 5시에 시작하는 것으로 예정되어 있는데,\n맞습니까?",
                "keyPattern": "Q9 오류 정정 만능 공식 (#7)",
                "answer": "No, I'm afraid that you have the wrong information.\nActually, the lecture on historic preservation is scheduled to start at 2:00 PM in Conference Room B.",
                "answerTranslation": "아니요, 잘못된 정보를 알고 계신 것 같습니다.\n사실 역사 보존에 관한 강연은 회의실 B에서 오후 2시에 시작할 예정입니다.",
                "magicSentences": [
                    "No, I'm afraid that you have the wrong information. Actually, [올바른 정보]. (아니요, 잘못 알고 계십니다. 사실은 ~입니다)"
                ],
                "scoreTip": "Q9 90% 이상 출제되는 오류 정정 문제입니다. 'No, I'm afraid that you have the wrong information. Actually, ~'를 입에 달고 계세요!",
                "vocabulary": [
                    {"word": "historic preservation", "ipa": "[hɪˈstɒrɪk ˌprezəˈveɪʃn]", "pos": "명사구", "meaning": "역사적 보존"},
                    {"word": "wrong information", "ipa": "[rɒŋ ˌɪnfəˈmeɪʃn]", "pos": "명사구", "meaning": "잘못된 정보"},
                    {"word": "conference room", "ipa": "[ˈkɒnfərəns ruːm]", "pos": "명사구", "meaning": "회의실"}
                ]
            },
            {
                "qNumber": "Question 10",
                "prepTime": 3,
                "responseTime": 30,
                "question": "I would love to attend all sessions led by Dr. Emily Brown.\nCould you tell me all the details about her events?",
                "questionTranslation": "에밀리 브라운 박사님이 진행하는 모든 세션에 참석하고 싶습니다.\n그녀의 행사에 대한 모든 세부 사항을 말씀해 주시겠습니까?",
                "keyPattern": "Q10 다중 나열 만능 공식 (Sure, there are two scheduled sessions)",
                "answer": "Sure, there are two scheduled sessions led by Dr. Emily Brown.\nFirst, on May 12th at 2:00 PM, she will lead a Historic Preservation Lecture in Conference Room B.\nSecond, on May 26th at 3:00 PM, she will conduct an Ancient Sculpture Seminar in the same room.\nThese are the two sessions she will lead.",
                "answerTranslation": "네, 에밀리 브라운 박사님이 진행하는 두 개의 세션이 예정되어 있습니다.\n첫째, 5월 12일 오후 2시에 회의실 B에서 역사 보존 강연을 진행하십니다.\n둘째, 5월 26일 오후 3시에 같은 회의실에서 고대 조각 세미나를 진행하십니다.\n이것이 그녀가 진행할 두 세션입니다.",
                "magicSentences": [
                    "Sure, there are two scheduled sessions. (네, 2개의 세션이 예정되어 있습니다)",
                    "First, on [Date] at [Time], there will be [Event]. (첫째, [일시]에 [행사]가 있습니다)",
                    "Second, on [Date] at [Time], there will be [Event]. (둘째, [일시]에 [행사]가 있습니다)"
                ],
                "scoreTip": "공통 발표자(Dr. Emily Brown)가 맡은 2개 세션을 차례로 'First, on [날짜] at [시간], ~ Second, on [날짜] at [시간], ~'로 나열하면 30초 만점입니다.",
                "vocabulary": [
                    {"word": "ancient sculpture", "ipa": "[ˈeɪnʃənt ˈskʌlptʃə(r)]", "pos": "명사구", "meaning": "고대 조각품"},
                    {"word": "seminar", "ipa": "[ˈsemɪnɑː(r)]", "pos": "명사", "meaning": "세미나, 연구 집회"},
                    {"word": "conduct", "ipa": "[kənˈdʌkt]", "pos": "동사", "meaning": "(행사/연구 등을) 진행하다, 지휘하다"}
                ]
            }
        ]
    },
    {
        "setNumber": 2,
        "title": "Set 2: Global Marketing Conference (글로벌 마케팅 컨퍼런스)",
        "topic": "Business Conference Program",
        "context": "Hello, this is David Clark from Nexus Media. I am attending the Global Marketing Conference next Monday and have a few questions about the agenda.",
        "context_kr": "안녕하세요, 넥서스 미디어의 데이비드 클라크입니다. 다음 주 월요일 글로벌 마케팅 컨퍼런스에 참석하는데 일정표에 관해 질문이 있습니다.",
        "table": {
            "headerTitle": "Annual Global Marketing Conference - Program Agenda",
            "metaInfo": [
                {"label": "Date", "value": "Monday, October 15"},
                {"label": "Venue", "value": "Grand Hyatt Hotel, Ballroom 2"}
            ],
            "rows": [
                {"time": "09:00 AM - 10:00 AM", "event": "Registration & Welcome Coffee", "speaker": "Staff Members", "room": "Foyer"},
                {"time": "10:00 AM - 11:30 AM", "event": "Keynote: AI in Digital Advertising", "speaker": "Sarah Jenkins", "room": "Main Hall"},
                {"time": "01:30 PM - 03:00 PM", "event": "Social Media Growth Strategies", "speaker": "Michael Chang", "room": "Room A"},
                {"time": "03:30 PM - 05:00 PM", "event": "Customer Data Protection & Ethics", "speaker": "Sarah Jenkins", "room": "Room B"}
            ]
        },
        "questions": [
            {
                "qNumber": "Question 8",
                "prepTime": 3,
                "responseTime": 15,
                "question": "What time does the conference start,\nand what is the first program?",
                "questionTranslation": "컨퍼런스는 몇 시에 시작하고,\n첫 번째 프로그램은 무엇인가요?",
                "keyPattern": "Q8 시작 시간 및 첫 프로그램",
                "answer": "The conference will start at 9:00 AM with Registration and Welcome Coffee in the Foyer.",
                "answerTranslation": "컨퍼런스는 오전 9시에 포비어에서 등록 및 환영 커피 세션으로 시작됩니다.",
                "magicSentences": [
                    "It will start at [Time] with [Event] in [Room]. ([장소]에서 [시간]에 [행사]로 시작합니다)"
                ],
                "scoreTip": "표 첫 줄을 보고 'It will start at [시간] with [세션]'으로 간결하고 정확하게 답하세요.",
                "vocabulary": [
                    {"word": "registration", "ipa": "[ˌredʒɪˈstreɪʃn]", "pos": "명사", "meaning": "등록, 접수"},
                    {"word": "agenda", "ipa": "[əˈdʒendə]", "pos": "명사", "meaning": "일정표, 의제"},
                    {"word": "keynote speech", "ipa": "[ˈkiːnəʊt spiːtʃ]", "pos": "명사구", "meaning": "기조 연설"}
                ]
            },
            {
                "qNumber": "Question 9",
                "prepTime": 3,
                "responseTime": 15,
                "question": "I heard that the afternoon session on Social Media Growth will be led by Sarah Jenkins.\nIs that right?",
                "questionTranslation": "소셜 미디어 성장에 관한 오후 세션은 사라 젠킨스 씨가 진행한다고 들었는데,\n맞나요?",
                "keyPattern": "Q9 오류 정정 공식 (#7)",
                "answer": "No, I'm afraid that you have the wrong information.\nActually, the session on Social Media Growth Strategies will be led by Michael Chang, not Sarah Jenkins.",
                "answerTranslation": "아니요, 잘못 알고 계신 것 같습니다.\n사실 소셜 미디어 성장 전략 세션은 사라 젠킨스가 아니라 마이클 장 씨가 진행합니다.",
                "magicSentences": [
                    "No, I'm afraid that you have the wrong information. Actually, it will be led by [Correct Speaker]. (아니요, 잘못 아셨습니다. 사실은 [발표자]가 진행합니다)"
                ],
                "scoreTip": "발표자가 틀린 전형적 오류 문제입니다. 마이클 장으로 정정해 주세요.",
                "vocabulary": [
                    {"word": "growth strategy", "ipa": "[ɡrəʊθ ˈstrætədʒi]", "pos": "명사구", "meaning": "성장 전략"},
                    {"word": "lead a session", "ipa": "[liːd ə ˈseʃn]", "pos": "동사구", "meaning": "세션을 이끌다, 진행하다"}
                ]
            },
            {
                "qNumber": "Question 10",
                "prepTime": 3,
                "responseTime": 30,
                "question": "Could you please give me all the information about the presentations by Sarah Jenkins?",
                "questionTranslation": "사라 젠킨스 씨가 하는 발표에 대한 모든 정보를 말씀해 주시겠습니까?",
                "keyPattern": "Q10 공통 발표자 2개 세션 나열",
                "answer": "Sure, there are two presentations by Sarah Jenkins scheduled on that day.\nFirst, from 10:00 AM to 11:30 AM, she will deliver the Keynote speech on AI in Digital Advertising in the Main Hall.\nSecond, from 3:30 PM to 5:00 PM, she will lead a session on Customer Data Protection and Ethics in Room B.\nThese are all the details of her presentations.",
                "answerTranslation": "네, 그날 사라 젠킨스 씨의 발표는 2개가 예정되어 있습니다.\n첫째, 오전 10시부터 11시 30분까지 메인 홀에서 '디지털 광고에서의 AI' 기조연설을 하십니다.\n둘째, 오후 3시 30분부터 5시까지 B룸에서 '고객 데이터 보호와 윤리' 세션을 진행하십니다.\n이것이 그녀의 발표에 대한 모든 세부 사항입니다.",
                "magicSentences": [
                    "Sure, there are two presentations scheduled. (네, 2개의 발표가 예정되어 있습니다)",
                    "First, from [Time] to [Time], she will [Event]. (첫째, [시간]부터 [시간]까지 [행사]를 하십니다)",
                    "Second, from [Time] to [Time], she will [Event]. (둘째, [시간]부터 [시간]까지 [행사]를 하십니다)"
                ],
                "scoreTip": "두 세션의 시간, 세션명, 장소(Room)를 차례로 명확한 발음으로 읽어줍니다.",
                "vocabulary": [
                    {"word": "deliver a speech", "ipa": "[dɪˈlɪvə(r) ə spiːtʃ]", "pos": "동사구", "meaning": "연설을 하다"},
                    {"word": "ethics", "ipa": "[ˈeθɪks]", "pos": "명사", "meaning": "윤리, 도덕"},
                    {"word": "protection", "ipa": "[prəˈtekʃn]", "pos": "명사", "meaning": "보호, 보안"}
                ]
            }
        ]
    },
    {
        "setNumber": 3,
        "title": "Set 3: Job Interview Schedule (신입 사원 면접 일정표)",
        "topic": "Interview Schedule",
        "context": "Hello, this is Brenda Vance from the HR department. I need to review today's interview schedule for the Graphic Designer position. Could you answer some questions?",
        "context_kr": "안녕하세요, 인사부의 브렌다 밴스입니다. 오늘 그래픽 디자이너 직무 면접 일정을 검토해야 합니다. 몇 가지 질문에 답해주시겠어요?",
        "table": {
            "headerTitle": "Creative Studio - Interview Schedule for Graphic Designer",
            "metaInfo": [
                {"label": "Date", "value": "Thursday, November 8"},
                {"label": "Interview Room", "value": "Meeting Room 302"}
            ],
            "rows": [
                {"time": "09:30 AM", "applicant": "Kevin Miller", "experience": "3 years at Alpha Corp", "status": "In-person interview"},
                {"time": "11:00 AM", "applicant": "Lisa Wong", "experience": "Entry level (Recent graduate)", "status": "In-person interview"},
                {"time": "02:00 PM", "applicant": "James Anderson", "experience": "5 years at Design Lab", "status": "Online Video (Zoom)"},
                {"time": "03:30 PM", "applicant": "Rachel Green", "experience": "4 years at Brand Inc.", "status": "In-person interview"}
            ]
        },
        "questions": [
            {
                "qNumber": "Question 8",
                "prepTime": 3,
                "responseTime": 15,
                "question": "Where will the interviews be held,\nand who is the first candidate?",
                "questionTranslation": "면접은 어디서 진행되고,\n첫 번째 지원자는 누구인가요?",
                "keyPattern": "Q8 장소 및 첫 번째 지원자",
                "answer": "The interviews will be held in Meeting Room 302,\nand the first candidate is Kevin Miller at 9:30 AM.",
                "answerTranslation": "면접은 302호 회의실에서 진행되며,\n첫 번째 지원자는 오전 9시 30분의 케빈 밀러 씨입니다.",
                "magicSentences": [
                    "The interviews will be held in [Room], and the first candidate is [Name]. (면접은 [장소]에서 열리며 첫 후보자는 [이름]입니다)"
                ],
                "scoreTip": "상단 메타 정보의 Meeting Room 302와 첫 지원자 Kevin Miller를 묶어 대답하세요.",
                "vocabulary": [
                    {"word": "candidate", "ipa": "[ˈkændɪdət]", "pos": "명사", "meaning": "후보자, 지원자"},
                    {"word": "applicant", "ipa": "[ˈæplɪkənt]", "pos": "명사", "meaning": "지원자"},
                    {"word": "in-person", "ipa": "[ɪn ˈpɜːsn]", "pos": "형용사/부사", "meaning": "직접 대면의"}
                ]
            },
            {
                "qNumber": "Question 9",
                "prepTime": 3,
                "responseTime": 15,
                "question": "Are all candidates required to attend the interview in person at the office?",
                "questionTranslation": "모든 지원자가 사무실로 직접 대면 면접에 와야 하나요?",
                "keyPattern": "Q9 온라인 화상 면접 예외 확인",
                "answer": "No, not all of them.\nActually, James Anderson's interview at 2:00 PM will be conducted online via Zoom.",
                "answerTranslation": "아니요, 모두가 그렇지는 않습니다.\n사실 오후 2시의 제임스 앤더슨 씨 면접은 줌(Zoom)을 통해 온라인으로 진행됩니다.",
                "magicSentences": [
                    "No, actually [Name]'s interview will be conducted online via [Platform]. (아니요, 사실 [이름]의 면접은 온라인으로 진행됩니다)"
                ],
                "scoreTip": "표에서 유일하게 'Online Video (Zoom)'으로 표기된 예외 지원자(James Anderson)를 짚어줍니다.",
                "vocabulary": [
                    {"word": "conduct online", "ipa": "[kənˈdʌkt ˈɒnlaɪn]", "pos": "동사구", "meaning": "온라인으로 진행하다"},
                    {"word": "recent graduate", "ipa": "[ˈriːsnt ˈɡrædʒuət]", "pos": "명사구", "meaning": "최근 졸업생, 신입"}
                ]
            },
            {
                "qNumber": "Question 10",
                "prepTime": 3,
                "responseTime": 30,
                "question": "Could you tell me all the details about the candidates who have more than 3 years of work experience?",
                "questionTranslation": "3년 이상의 경력을 가진 지원자들에 대한 모든 세부 사항을 말씀해 주시겠습니까?",
                "keyPattern": "Q10 조건 만족 지원자 2명 나열",
                "answer": "Sure, there are two candidates with more than three years of experience.\nFirst, at 2:00 PM, James Anderson has 5 years of experience at Design Lab, and his interview is via Zoom.\nSecond, at 3:30 PM, Rachel Green has 4 years of experience at Brand Inc., and her interview is in-person.\nThese are the two experienced candidates.",
                "answerTranslation": "네, 3년 이상의 경력을 가진 지원자는 두 명입니다.\n첫째, 오후 2시 제임스 앤더슨 씨는 디자인 랩에서 5년 경력이 있으며 줌으로 면접을 봅니다.\n둘째, 오후 3시 30분 레이첼 그린 씨는 브랜드사에서 4년 경력이 있으며 대면 면접입니다.\n이 두 명이 경력직 지원자입니다.",
                "magicSentences": [
                    "Sure, there are two candidates who meet that condition. (네, 그 조건을 만족하는 두 지원자가 있습니다)"
                ],
                "scoreTip": "'more than 3 years'이므로 3년(Kevin Miller)은 제외되고 5년(James)과 4년(Rachel) 2명을 나열해야 합니다! 조건 주의!",
                "vocabulary": [
                    {"word": "work experience", "ipa": "[wɜːk ɪkˈspɪəriəns]", "pos": "명사구", "meaning": "근무 경력"},
                    {"word": "entry level", "ipa": "[ˈentri ˈlevl]", "pos": "명사/형용사", "meaning": "신입, 초급의"}
                ]
            }
        ]
    },
    {
        "setNumber": 4,
        "title": "Set 4: Employee Training Workshop (사내 직원 직무 연수 워크숍)",
        "topic": "Workshop Agenda",
        "context": "Hello, this is Tom Harris from the Sales Team. I have some questions regarding the upcoming Employee Training Workshop next Friday.",
        "context_kr": "안녕하세요, 영업팀의 톰 해리스입니다. 다음 주 금요일 직원 직무 교육 워크숍에 관해 질문이 있습니다.",
        "table": {
            "headerTitle": "SkillUp Training - Annual Professional Development Workshop",
            "metaInfo": [
                {"label": "Date", "value": "Friday, September 21"},
                {"label": "Location", "value": "Training Center, 4th Floor"}
            ],
            "rows": [
                {"time": "09:00 AM - 10:30 AM", "topic": "Effective Business Communication", "instructor": "Kelly Jones", "cost": "Free"},
                {"time": "11:00 AM - 12:30 PM", "topic": "Project Management Software", "instructor": "Robert Miller", "cost": "$25 (Materials fee)"},
                {"time": "02:00 PM - 03:30 PM", "topic": "Advanced Excel & Data Analytics", "instructor": "Robert Miller", "cost": "$30 (Software license)"},
                {"time": "04:00 PM - 05:00 PM", "topic": "Stress Management at Workplace", "instructor": "Kelly Jones", "cost": "Free"}
            ]
        },
        "questions": [
            {
                "qNumber": "Question 8",
                "prepTime": 3,
                "responseTime": 15,
                "question": "Where is the workshop taking place,\nand is the first session free of charge?",
                "questionTranslation": "워크숍은 어디서 열리고,\n첫 번째 세션은 무료인가요?",
                "keyPattern": "Q8 장소 및 첫 세션 비용",
                "answer": "The workshop will take place on the 4th Floor of the Training Center,\nand yes, the first session on Business Communication is completely free of charge.",
                "answerTranslation": "워크숍은 교육 센터 4층에서 열리며,\n네, 비즈니스 커뮤니케이션에 관한 첫 번째 세션은 전액 무료입니다.",
                "magicSentences": [
                    "The workshop will take place on [Location], and yes, it is free of charge. (워크숍은 [장소]에서 열리며, 네 무료입니다)"
                ],
                "scoreTip": "장소(4th Floor)와 첫 세션 비용(Free)을 명쾌하게 답변하세요.",
                "vocabulary": [
                    {"word": "take place", "ipa": "[teɪk pleɪs]", "pos": "동사구", "meaning": "열리다, 개최되다"},
                    {"word": "free of charge", "ipa": "[friː əv tʃɑːdʒ]", "pos": "부사구", "meaning": "무료로"}
                ]
            },
            {
                "qNumber": "Question 9",
                "prepTime": 3,
                "responseTime": 15,
                "question": "I heard that the afternoon session on Advanced Excel starts at 3:00 PM.\nIs that correct?",
                "questionTranslation": "고급 엑셀 오후 세션이 오후 3시에 시작한다고 들었는데,\n맞습니까?",
                "keyPattern": "Q9 오류 정정 공식 (#7)",
                "answer": "No, I'm afraid that you have the wrong information.\nActually, the Advanced Excel session starts at 2:00 PM, and it will run until 3:30 PM.",
                "answerTranslation": "아니요, 잘못 알고 계신 것 같습니다.\n사실 고급 엑셀 세션은 오후 2시에 시작해서 3시 30분까지 진행됩니다.",
                "magicSentences": [
                    "No, I'm afraid that you have the wrong information. Actually, it starts at [Correct Time]. (아니요, 잘못 아셨습니다. 사실은 [시간]에 시작합니다)"
                ],
                "scoreTip": "오후 3시가 아니라 2시(2:00 PM)에 시작한다고 정정합니다.",
                "vocabulary": [
                    {"word": "run until", "ipa": "[rʌn ənˈtɪl]", "pos": "동사구", "meaning": "~까지 진행되다/이어지다"},
                    {"word": "data analytics", "ipa": "[ˈdeɪtə ˌænəˈlɪtɪks]", "pos": "명사구", "meaning": "데이터 분석"}
                ]
            },
            {
                "qNumber": "Question 10",
                "prepTime": 3,
                "responseTime": 30,
                "question": "Can you give me all the information about the workshops taught by Robert Miller?",
                "questionTranslation": "로버트 밀러 강사가 가르치는 워크숍에 대한 모든 정보를 알려주실 수 있나요?",
                "keyPattern": "Q10 공통 강사 세션 2개 나열",
                "answer": "Sure, there are two workshops instructed by Robert Miller.\nFirst, from 11:00 AM to 12:30 PM, he will teach Project Management Software, which has a materials fee of $25.\nSecond, from 2:00 PM to 3:30 PM, he will instruct Advanced Excel and Data Analytics, which costs $30 for software licenses.\nThese are the two sessions led by him.",
                "answerTranslation": "네, 로버트 밀러 강사가 진행하는 워크숍은 2개입니다.\n첫째, 오전 11시부터 12시 30분까지 프로젝트 관리 소프트웨어를 가르치며 교재비 25달러가 있습니다.\n둘째, 오후 2시부터 3시 30분까지 고급 엑셀 및 데이터 분석을 가르치며 소프트웨어 라이선스 비용 30달러가 듭니다.\n이것이 그가 진행하는 두 세션입니다.",
                "magicSentences": [
                    "Sure, there are two workshops instructed by [Name]. (네, [이름] 강사의 워크숍 2개가 있습니다)"
                ],
                "scoreTip": "시간, 주제, 비용($25, $30)까지 모두 표에 나와 있으므로 꼼꼼하게 언급해주면 고득점을 받습니다.",
                "vocabulary": [
                    {"word": "instruct", "ipa": "[ɪnˈstrʌkt]", "pos": "동사", "meaning": "가르치다, 교육하다"},
                    {"word": "materials fee", "ipa": "[məˈtɪəriəlz fiː]", "pos": "명사구", "meaning": "재료비, 교재비"}
                ]
            }
        ]
    },
    {
        "setNumber": 5,
        "title": "Set 5: City Community Festival (지역 주민 커뮤니티 축제)",
        "topic": "Community Festival Schedule",
        "context": "Hello, this is Sarah Connor from the neighborhood association. I want to ask about the upcoming Springfield City Festival schedule this Saturday.",
        "context_kr": "안녕하세요, 주민회의 사라 코너입니다. 이번 주 토요일 스프링필드 도시 축제 일정에 대해 문의드립니다.",
        "table": {
            "headerTitle": "Springfield City Summer Festival - Event Program",
            "metaInfo": [
                {"label": "Date", "value": "Saturday, July 14"},
                {"label": "Main Stage", "value": "Centennial Community Park"}
            ],
            "rows": [
                {"time": "10:00 AM", "event": "Opening Parade & Marching Band", "location": "Main Street to Park", "target": "All citizens"},
                {"time": "01:00 PM", "event": "Local Food Cooking Contest", "location": "Food Tent A", "target": "Adult participants"},
                {"time": "03:30 PM", "event": "Kids Magic & Puppet Show", "location": "Activity Tent B", "target": "Children and families"},
                {"time": "07:00 PM", "event": "Live Fireworks & Rock Concert", "location": "Main Stage", "target": "All citizens"}
            ]
        },
        "questions": [
            {
                "qNumber": "Question 8",
                "prepTime": 3,
                "responseTime": 15,
                "question": "What is the date of the festival,\nand where does the opening parade take place?",
                "questionTranslation": "축제 날짜는 언제이고,\n개막 퍼레이드는 어디서 열리나요?",
                "keyPattern": "Q8 축제 날짜 및 퍼레이드 장소",
                "answer": "The festival will be held on Saturday, July 14th,\nand the opening parade will take place from Main Street to the park at 10:00 AM.",
                "answerTranslation": "축제는 7월 14일 토요일에 열리며,\n개막 퍼레이드는 오전 10시에 메인 스트리트에서 공원까지 진행됩니다.",
                "magicSentences": [
                    "The festival will be held on [Date], and the parade will take place at [Location]. (축제는 [날짜]에 열리며 퍼레이드는 [장소]에서 열립니다)"
                ],
                "scoreTip": "날짜와 장소(From Main Street to Park)를 또렷하게 전달하세요.",
                "vocabulary": [
                    {"word": "parade", "ipa": "[pəˈreɪd]", "pos": "명사", "meaning": "퍼레이드, 행진"},
                    {"word": "centennial", "ipa": "[senˈteniəl]", "pos": "형용사/명사", "meaning": "100주년의"}
                ]
            },
            {
                "qNumber": "Question 9",
                "prepTime": 3,
                "responseTime": 15,
                "question": "Is the Kids Magic and Puppet Show scheduled in the evening after 6:00 PM?",
                "questionTranslation": "어린이 마술 및 인형극 쇼는 오후 6시 이후 저녁 시간으로 예정되어 있나요?",
                "keyPattern": "Q9 오류 정정 공식 (#7)",
                "answer": "No, I'm afraid that you have the wrong information.\nActually, the Kids Magic and Puppet Show is scheduled in the afternoon at 3:30 PM in Activity Tent B.",
                "answerTranslation": "아니요, 잘못 알고 계신 것 같습니다.\n사실 어린이 마술 및 인형극 쇼는 오후 3시 30분에 활동 텐트 B에서 열릴 예정입니다.",
                "magicSentences": [
                    "No, I'm afraid that you have the wrong information. Actually, it is scheduled at [Correct Time]. (아니요, 잘못 아셨습니다. 사실 [시간]에 열립니다)"
                ],
                "scoreTip": "저녁이 아니라 오후 3시 30분(3:30 PM)임을 짚어줍니다.",
                "vocabulary": [
                    {"word": "puppet show", "ipa": "[ˈpʌpɪt ʃəʊ]", "pos": "명사구", "meaning": "인형극"},
                    {"word": "scheduled", "ipa": "[ˈskedʒuːld]", "pos": "형용사", "meaning": "예정된"}
                ]
            },
            {
                "qNumber": "Question 10",
                "prepTime": 3,
                "responseTime": 30,
                "question": "Can you tell me all the events that are suitable for all citizens to enjoy together?",
                "questionTranslation": "모든 시민이 다 함께 즐기기에 적합한 모든 행사를 말씀해 주시겠습니까?",
                "keyPattern": "Q10 대상자 조건(All citizens) 2개 행사 나열",
                "answer": "Sure, there are two events targeted for all citizens.\nFirst, at 10:00 AM, there is the Opening Parade and Marching Band starting from Main Street to the park.\nSecond, at 7:00 PM, there is the Live Fireworks and Rock Concert at the Main Stage.\nThese are the two events for all citizens.",
                "answerTranslation": "네, 모든 시민을 대상으로 하는 행사는 두 개가 있습니다.\n첫째, 오전 10시에 메인 스트리트에서 공원까지 이어지는 개막 퍼레이드와 마칭 밴드가 있습니다.\n둘째, 오후 7시에 메인 무대에서 열리는 라이브 불꽃놀이와 록 콘서트가 있습니다.\n이것이 모든 시민을 위한 두 행사입니다.",
                "magicSentences": [
                    "Sure, there are two events targeted for all citizens. (네, 모든 시민을 위한 2개의 행사가 있습니다)"
                ],
                "scoreTip": "Target 열에서 'All citizens'로 표기된 10:00 AM 퍼레이드와 7:00 PM 불꽃놀이를 짝지어 설명하세요.",
                "vocabulary": [
                    {"word": "suitable", "ipa": "[ˈsuːtəbl]", "pos": "형용사", "meaning": "적합한, 알맞은"},
                    {"word": "fireworks", "ipa": "[ˈfaɪəwɜːks]", "pos": "명사", "meaning": "불꽃놀이"}
                ]
            }
        ]
    }
]

# Combined Master Dictionary
master_data = {
    "metadata": {
        "part3_count": len(part3_data),
        "part4_count": sum(len(s["questions"]) for s in part4_sets),
        "part4_sets_count": len(part4_sets)
    },
    "part3": part3_data,
    "part4": part4_sets
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print("data.json successfully written with Part 3 and Part 4 master datasets!")
print(f"Part 3 questions: {len(part3_data)}")
print(f"Part 4 sets: {len(part4_sets)}, Part 4 questions: {sum(len(s['questions']) for s in part4_sets)}")
