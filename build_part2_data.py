import json

print("Integrating Part 2 (Picture Description) into data.json...")

with open('data.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

# 14 Photo Questions with 120-140 Model Answers, Grammar Breakdown & Vocab
part2_photo_questions = [
    {
        "id": 1,
        "setNumber": 1,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 1: Grocery Store (식료품점/마트 장보기)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[식료품점/마트 장보기 사진] 마트 진열대 통로에 남녀 2명이 있는 사진. 오른쪽에는 긴 머리에 회색 셔츠를 입은 여성이 장바구니를 들고 선반의 물건을 집으려 손을 뻗고 있고, 왼쪽에는 짧은 머리에 흰 셔츠를 입은 남성이 쇼핑카트를 밀면서 전화 통화를 하고 있음. 배경의 선반에는 다양한 식료품들이 진열되어 있음.",
        "photoScene": {
            "category": "마트/식료품점",
            "locationEn": "at a grocery store",
            "visualSvg": "grocery",
            "tags": ["grocery store", "shopping cart", "reaching for an item", "shelves"]
        },
        "answer": "This is a picture taken at a grocery store.\nThere are two people in this picture.\nOn the right side of the picture, there is a woman. She has long hair and is wearing a gray shirt. She is carrying a shopping basket and reaching for an item.\nOn the left side of the picture, there is a man. He has short hair and is wearing a white shirt. He is pushing a shopping cart and talking on the phone.\nIn the background, I can see groceries on display on the shelves.",
        "answerTranslation": "이 사진은 식료품점에서 찍힌 사진입니다.\n사진에 두 명의 사람이 있습니다.\n사진 오른쪽에 한 여성이 있습니다. 그녀는 긴 머리에 회색 셔츠를 입고 있으며, 장바구니를 들고 물건을 집으려고 손을 뻗고 있습니다.\n사진 왼쪽에 한 남성이 있습니다. 그는 짧은 머리에 흰 셔츠를 입고 있으며, 쇼핑카트를 밀면서 전화 통화를 하고 있습니다.\n배경에는 선반 위에 진열된 식료품들이 보입니다.",
        "magicSentences": [
            "This is a picture taken at [장소]. (이 사진은 [장소]에서 찍힌 사진입니다)",
            "He/She is reaching for an item. (그/그녀는 물건을 향해 손을 뻗고 있습니다)",
            "He is pushing a cart. (그는 카트를 밀고 있습니다)",
            "I can see groceries on display. (진열된 식료품들을 볼 수 있습니다)"
        ],
        "grammarPoints": [
            {
                "title": "사진 묘사 1단계: 'This is a picture taken at/in [장소]' 과거분사 구문",
                "explanation": "사진 묘사 첫 문장의 절대 공식입니다. 'taken at/in'은 앞에 'which was'가 생략된 과거분사구로, 사진이 촬영된 장소를 나타낼 때 전치사 at(특정 시설/상점)이나 in(실내/지역)을 사용합니다."
            },
            {
                "title": "동작 묘사의 기본: 현재진행형 (be + -ing)",
                "explanation": "사진 속 인물의 동작은 100% 현재진행형(is pushing, is talking, is reaching)으로 묘사해야 합니다. 'pushes' 같은 단순 현재 시제를 쓰면 감점되므로 반드시 be동사 + -ing 형태를 유지하세요."
            },
            {
                "title": "사물 진열의 전치사구: 'on display on the shelves'",
                "explanation": "'진열 중인'을 나타내는 전치사구 'on display'와 선반 표면을 나타내는 'on the shelves'가 결합하여 배경 사물을 자연스럽게 완성합니다."
            }
        ],
        "vocabulary": [
            {"word": "grocery store", "ipa": "[ˈɡrəʊsəri stɔː(r)]", "pos": "명사", "meaning": "식료품점, 마트", "source": "사진 필수"},
            {"word": "shopping basket", "ipa": "[ˈʃɒpɪŋ ˈbɑːskɪt]", "pos": "명사", "meaning": "장바구니", "source": "사진 필수"},
            {"word": "reach for", "ipa": "[riːtʃ fɔː(r)]", "pos": "동사구", "meaning": "~을 집으려고 손을 뻗다", "source": "답변 핵심"},
            {"word": "push a cart", "ipa": "[pʊʃ ə kɑːt]", "pos": "동사구", "meaning": "카트를 밀다", "source": "답변 핵심"},
            {"word": "on display", "ipa": "[ɒn dɪˈspleɪ]", "pos": "형용사구", "meaning": "진열된, 전시된", "source": "답변 핵심"}
        ],
        "scoreTip": "인물 2명이 좌우에 나뉘어 있을 때는 ①장소 도입 ➡️ ②오른쪽 여성(외모/동작) ➡️ ③왼쪽 남성(외모/동작) ➡️ ④배경 사물의 4단계 공식으로 30초를 완벽하게 채울 수 있습니다."
    },
    {
        "id": 2,
        "setNumber": 2,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 2: Retail Store (상점 내 상품 확인 및 쇼핑)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[상점 내 상품 확인 사진] 매장 안에서 남녀 2명이 나란히 서 있는 사진. 가운데 금발 머리에 가죽 자켓과 청바지를 입은 여성이 물건을 들고 손가락으로 가리키고 있고, 그 옆의 갈색 머리에 검은색 셔츠와 청바지를 입은 남성이 태블릿 PC를 들고 여성을 바라보고 있음.",
        "photoScene": {
            "category": "상점/매장",
            "locationEn": "at a store",
            "visualSvg": "retail",
            "tags": ["retail store", "tablet PC", "pointing", "jeans"]
        },
        "answer": "This is a picture taken at a store.\nThere are two people in this picture.\nIn the middle of the picture, there is a woman. She has blonde hair, and she is wearing a leather jacket and jeans. She is holding an item and pointing at it.\nNext to her, there is a man. He has brown hair, and he is wearing a black shirt and jeans. He is holding a tablet PC and looking at the woman.\nOverall, it seems like they are shopping together.",
        "answerTranslation": "이 사진은 상점에서 찍힌 사진입니다.\n사진에 두 사람이 있습니다.\n사진 가운데에 한 여성이 있습니다. 그녀는 금발 머리에 가죽 자켓과 청바지를 입고 있으며, 물건을 들고 그것을 가리키고 있습니다.\n그녀 옆에는 한 남성이 있습니다. 그는 갈색 머리에 검은색 셔츠와 청바지를 입고 있으며, 태블릿 PC를 들고 여성을 바라보고 있습니다.\n전반적으로 함께 쇼핑 중인 것 같습니다.",
        "magicSentences": [
            "In the middle of the picture, there is [인물]. (사진 가운데에 [인물]이 있습니다)",
            "Next to her/him, there is [인물]. (그/그녀 옆에 [인물]이 있습니다)",
            "He/She is pointing at it. (그것을 손가락으로 가리키고 있습니다)",
            "Overall, it seems like S+V. (전반적으로 ~인 것 같습니다)"
        ],
        "grammarPoints": [
            {
                "title": "위치 연결 표현: 'Next to her/him'의 효율적 전개",
                "explanation": "두 인물이 나란히 서 있을 때 'On the left', 'On the right'를 반복하기보다 'In the middle ~'로 첫 사람을 잡은 뒤 'Next to her(그녀 옆에)'로 연결하면 표현의 다양성에서 높은 점수를 받습니다."
            },
            {
                "title": "착용 상태: 'be wearing' vs 동작 'put on'",
                "explanation": "옷을 이미 입고 있는 상태를 말할 때는 진행형 'is wearing'을 쓰며, 옷을 입는 동작을 나타내는 'is putting on'과 구별해야 합니다."
            },
            {
                "title": "마무리 총평: 'Overall, it seems like S+V'",
                "explanation": "사진 묘사의 마지막 3초는 전체적인 분위기나 상황 추측으로 마무리합니다. 'it seems like + 주어 + 동사'는 토익스피킹 파트 2에서 가장 안전하고 고급스러운 마무리 템플릿입니다."
            }
        ],
        "vocabulary": [
            {"word": "leather jacket", "ipa": "[ˈleðə ˈdʒækɪt]", "pos": "명사", "meaning": "가죽 자켓", "source": "사진 필수"},
            {"word": "tablet PC", "ipa": "[ˈtæblət ˌpiːˈsiː]", "pos": "명사", "meaning": "태블릿 PC", "source": "사진 필수"},
            {"word": "point at", "ipa": "[pɔɪnt æt]", "pos": "동사구", "meaning": "~을 가리키다", "source": "답변 핵심"},
            {"word": "look at", "ipa": "[lʊk æt]", "pos": "동사구", "meaning": "~을 바라보다", "source": "답변 핵심"},
            {"word": "overall", "ipa": "[ˌəʊvərˈɔːl]", "pos": "부사", "meaning": "전반적으로, 종합해서", "source": "답변 핵심"}
        ],
        "scoreTip": "가리키는 동작(pointing at it)과 태블릿을 쥐고 있는 동작(holding a tablet PC)을 명확하게 표현해 주면 고득점(130~140점 이상)을 안정적으로 확보할 수 있습니다."
    },
    {
        "id": 3,
        "setNumber": 3,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 3: Checkout Counter (계산대 신용카드 결제)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[상점/카페 계산대 결제 사진] 계산대에서 점원 1명과 손님 2명(총 3명)이 있는 사진. 오른쪽에는 앞치마를 입은 여성 점원이 카드 단말기를 들고 신용카드를 받고 있고, 왼쪽에는 남녀 고객 2명 중 남성이 미소 지으며 신용카드를 건네주고 있고 여성은 컵을 들고 점원을 바라보고 있음.",
        "photoScene": {
            "category": "계산대/결제",
            "locationEn": "at a store counter",
            "visualSvg": "checkout",
            "tags": ["cashier", "credit card", "handing over", "receiving"]
        },
        "answer": "This is a picture taken at a store.\nThere are three people in this picture.\nOn the right side of the picture, there is a woman who looks like a clerk. She is wearing an apron, and she is holding a card machine and receiving a credit card.\nOn the left side of the picture, there are two customers. One of them is a man, and he is smiling and handing over the credit card. The other is a woman, and she is holding a cup and looking at the clerk.",
        "answerTranslation": "이 사진은 상점에서 찍힌 사진입니다.\n사진에 세 사람이 있습니다.\n사진 오른쪽에 점원처럼 보이는 여성이 있습니다. 그녀는 앞치마를 입고 카드 단말기를 든 채 신용카드를 받고 있습니다.\n사진 왼쪽에는 두 명의 손님이 있습니다. 그중 한 명인 남성은 미소를 지으며 신용카드를 건네고 있고, 다른 한 명인 여성은 컵을 들고 점원을 바라보고 있습니다.",
        "magicSentences": [
            "He/She looks like a clerk. (점원처럼 보입니다)",
            "He is handing over a credit card. (신용카드를 건네주고 있습니다)",
            "She is receiving an item / credit card. (물건/신용카드를 건네받고 있습니다)",
            "One of them is ~ and the other is ~ (한 명은 ~이고 다른 한 명은 ~입니다)"
        ],
        "grammarPoints": [
            {
                "title": "주격 관계대명사: 'a woman who looks like a clerk'",
                "explanation": "인물의 직업이나 역할을 추측할 때 관계대명사절 'who looks like ~'(~처럼 보이는)을 활용하면 복문 구사 능력이 인정되어 가산점을 받습니다."
            },
            {
                "title": "결제 동작의 대칭쌍: 'handing over' vs 'receiving'",
                "explanation": "손님이 '건네다'는 handing over, 직원이 '받다'는 receiving으로 짝을 지어 대칭 동사로 표현하면 문장이 대단히 자연스럽습니다."
            },
            {
                "title": "두 대상의 특정 지칭: 'One of them ~ The other ~'",
                "explanation": "2명의 손님 중 첫 번째 사람을 언급할 때는 One of them, 나머지 한 명을 칭할 때는 정관사 the가 붙은 'The other'를 사용하는 것이 정확한 수일치 문법입니다."
            }
        ],
        "vocabulary": [
            {"word": "clerk", "ipa": "[klɑːk]", "pos": "명사", "meaning": "점원, 직원", "source": "사진 필수"},
            {"word": "apron", "ipa": "[ˈeɪprən]", "pos": "명사", "meaning": "앞치마", "source": "사진 필수"},
            {"word": "hand over", "ipa": "[hænd ˈəʊvə(r)]", "pos": "동사구", "meaning": "건네주다, 인도하다", "source": "답변 핵심"},
            {"word": "receive", "ipa": "[rɪˈsiːv]", "pos": "동사", "meaning": "받다, 수령하다", "source": "답변 핵심"},
            {"word": "credit card", "ipa": "[ˈkredɪt kɑːd]", "pos": "명사", "meaning": "신용카드", "source": "답변 핵심"}
        ],
        "scoreTip": "계산대 장면은 토익스피킹 파트 2에서 가장 많이 나오는 초빈출 유형입니다. 카드를 내미는 손님(handing over)과 받는 직원(receiving)을 확실하게 묘사하세요."
    },
    {
        "id": 4,
        "setNumber": 4,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 4: Hotel Front Desk (호텔 프런트 데스크 체크인)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[호텔 프런트 데스크 체크인 사진] 실내 카운터에서 직원 2명과 고객 1명(총 3명)이 있는 사진. 오른쪽 여성 고객이 손을 내밀어 열쇠(방 키)를 받고 있고, 맞은편 카운터의 여성 직원은 미소 지으며 열쇠를 건네주고 있으며, 그 옆의 남성 직원은 수화기를 들고 전화 통화를 하고 있음.",
        "photoScene": {
            "category": "호텔/프런트",
            "locationEn": "at a hotel front desk",
            "visualSvg": "hotel",
            "tags": ["hotel reception", "room key", "checking in", "counter"]
        },
        "answer": "This is a picture taken indoors at a hotel.\nThere are three people in this picture.\nOn the right side of the picture, there is a woman who looks like a customer. She is holding out her hand and receiving a key.\nIn front of her, there are two clerks standing at the counter. One of them is a woman, and she is smiling and handing over the key to the customer. The other is a man, and he is talking on the phone.\nOverall, it seems like a customer is checking in at a hotel.",
        "answerTranslation": "이 사진은 호텔 실내에서 찍힌 사진입니다.\n사진에 세 사람이 있습니다.\n사진 오른쪽에 고객처럼 보이는 여성이 손을 내밀어 열쇠를 받고 있습니다.\n그녀 앞 카운터에는 직원 두 명이 서 있습니다. 그중 여성 직원은 미소 지으며 고객에게 열쇠를 건네주고 있고, 남성 직원은 전화 통화를 하고 있습니다.\n전반적으로 고객이 호텔에서 체크인을 하고 있는 것 같습니다.",
        "magicSentences": [
            "This is a picture taken indoors. (이 사진은 실내에서 찍힌 사진입니다)",
            "They are standing at the counter. (카운터에 서 있습니다)",
            "She is holding out her hand. (손을 내밀고 있습니다)",
            "It seems like a customer is checking in. (고객이 체크인하는 것 같습니다)"
        ],
        "grammarPoints": [
            {
                "title": "대면 구도의 위치 전치사: 'In front of her / Across from her'",
                "explanation": "카운터를 사이에 두고 마주 보고 있을 때 'In front of her'(그녀 앞에) 또는 'Across from her'(그녀 맞은편에)를 쓰면 공간적 원근감이 생생하게 전달됩니다."
            },
            {
                "title": "동작의 연속: 분사구문 'smiling and handing over'",
                "explanation": "'is smiling and handing over'처럼 두 가지 긍정적인 행동을 등위접속사 and로 연결하여 자연스러운 표정과 행동을 동시에 표현합니다."
            }
        ],
        "vocabulary": [
            {"word": "reception desk", "ipa": "[rɪˈsepʃn desk]", "pos": "명사", "meaning": "접수대, 프런트", "source": "사진 필수"},
            {"word": "check in", "ipa": "[tʃek ɪn]", "pos": "동사구", "meaning": "체크인하다, 투숙 수속을 밟다", "source": "사진 필수"},
            {"word": "hold out one's hand", "ipa": "[həʊld aʊt wʌnz hænd]", "pos": "관용구", "meaning": "손을 내밀다", "source": "답변 핵심"},
            {"word": "hand over the key", "ipa": "[hænd ˈəʊvə ðə kiː]", "pos": "동사구", "meaning": "열쇠를 건네다", "source": "답변 핵심"}
        ],
        "scoreTip": "호텔 체크인 상황을 알아채고 마지막에 'checking in at a hotel'이라는 토익스피킹 핵심 상황 어휘를 넣어주면 가산점을 크게 받습니다."
    },
    {
        "id": 5,
        "setNumber": 5,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 5: Restaurant Dining (레스토랑 식사 및 대화)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[레스토랑 식사 및 대화 사진] 레스토랑 테이블에 남녀 2명이 마주 앉아 있는 사진. 왼쪽에는 긴 머리에 원피스를 입은 여성이 두 손을 모으고 미소 짓고 있으며, 오른쪽에는 갈색 머리에 흰 셔츠를 입은 남성이 테이블에 팔을 얹고 여성을 바라보고 있음. 두 사람 사이 테이블 위에는 와인잔과 병 등이 놓여 있음.",
        "photoScene": {
            "category": "식당/레스토랑",
            "locationEn": "at a restaurant",
            "visualSvg": "restaurant",
            "tags": ["restaurant", "wine glasses", "sitting at a table", "smiling"]
        },
        "answer": "This is a picture taken at a restaurant.\nThere are two people sitting at a table.\nOn the left side of the picture, there is a woman. She has long hair and is wearing a dress. She is smiling and holding her hands together.\nOn the right side of the picture, there is a man. He has brown hair and is wearing a white shirt. He is resting his arms on the table and looking at the woman.\nBetween them, there are wine glasses and a bottle on the table.",
        "answerTranslation": "이 사진은 레스토랑에서 찍힌 사진입니다.\n테이블에 두 사람이 앉아 있습니다.\n사진 왼쪽에 긴 머리에 원피스를 입은 여성이 미소 지으며 두 손을 모으고 있습니다.\n사진 오른쪽에는 갈색 머리에 흰 셔츠를 입은 남성이 테이블에 팔을 걸치고 여성을 바라보고 있습니다.\n두 사람 사이 테이블 위에는 와인잔들과 병이 있습니다.",
        "magicSentences": [
            "This is a picture taken at a restaurant. (레스토랑에서 찍힌 사진입니다)",
            "They are sitting at a table. (테이블에 앉아 있습니다)",
            "She is wearing a dress. (원피스를 입고 있습니다)",
            "Between them, there are [사물]. (그들 사이에 [사물]이 있습니다)"
        ],
        "grammarPoints": [
            {
                "title": "사물 위치 표현: 'Between them, there are ~'",
                "explanation": "두 사람 사이의 공간을 묘사할 때 'Between them'(그들 사이에)을 문두에 배치하고 유도부사 'there are + 복수명사'로 연결하는 세련된 구문입니다."
            },
            {
                "title": "착석 상태의 표현: 'sitting at a table'",
                "explanation": "테이블에 앉아 있을 때 전치사는 on이 아니라 'at a table'을 사용합니다. (의자에 앉는 것은 on a chair, 식탁에 마주 앉는 것은 at a table)"
            }
        ],
        "vocabulary": [
            {"word": "wine glass", "ipa": "[waɪn ɡlɑːs]", "pos": "명사", "meaning": "와인잔", "source": "사진 필수"},
            {"word": "hold hands together", "ipa": "[həʊld hændz təˈɡeðə]", "pos": "동사구", "meaning": "두 손을 모으다", "source": "답변 핵심"},
            {"word": "rest one's arms", "ipa": "[rest wʌnz ɑːmz]", "pos": "동사구", "meaning": "팔을 얹다, 걸치다", "source": "답변 핵심"},
            {"word": "between them", "ipa": "[bɪˈtwiːn ðem]", "pos": "전치사구", "meaning": "그들 사이에", "source": "답변 핵심"}
        ],
        "scoreTip": "식당 2인 테이블 사진에서는 ①장소 및 착석 ➡️ ②왼쪽 인물 ➡️ ③오른쪽 인물 ➡️ ④테이블 위 와인잔/병 사물 묘사로 진행하면 깔끔합니다."
    },
    {
        "id": 6,
        "setNumber": 6,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 6: Cafe Dessert & Menu (카페 메뉴 확인 및 디저트)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[카페 메뉴 확인 및 디저트 식사 사진] 카페 테이블에 남녀 2명이 앉아 있는 사진. 왼쪽 남성은 손목시계를 차고 메뉴판을 들고 보고 있으며, 오른쪽 여성은 머리를 하나로 묶고(포니테일) 포크를 든 채 케이크를 먹고 있음. 앞쪽 테이블 위에는 컵과 접시들이 놓여 있음.",
        "photoScene": {
            "category": "카페/디저트",
            "locationEn": "at a cafe",
            "visualSvg": "cafe",
            "tags": ["cafe", "menu", "eating cake", "ponytail"]
        },
        "answer": "This is a picture taken at a cafe.\nThere are two people sitting at a table.\nOn the left side of the picture, there is a man. He is wearing a watch, and he is holding a menu and looking at it.\nOn the right side of the picture, there is a woman with a ponytail. She is holding a fork and eating some cake.\nIn front of them, there are cups and dishes on the table.\nOverall, it seems like they are having a peaceful time.",
        "answerTranslation": "이 사진은 카페에서 찍힌 사진입니다.\n테이블에 두 사람이 앉아 있습니다.\n사진 왼쪽에 있는 남성은 시계를 차고 메뉴판을 들고 보고 있습니다.\n사진 오른쪽에 포니테일 머리를 한 여성은 포크를 들고 케이크를 먹고 있습니다.\n그들 앞 테이블 위에는 컵과 접시들이 놓여 있습니다.\n전반적으로 평화로운 시간을 보내고 있는 것 같습니다.",
        "magicSentences": [
            "This is a picture taken at a cafe. (카페에서 찍힌 사진입니다)",
            "He is looking at a menu. (메뉴판을 보고 있습니다)",
            "She is eating some food / cake. (음식/케이크를 먹고 있습니다)",
            "Overall, it seems like a peaceful day. (전반적으로 평화로운 날 같습니다)"
        ],
        "grammarPoints": [
            {
                "title": "외모 부가 수식: 'with a ponytail'",
                "explanation": "'a woman with a ponytail'처럼 전치사 with + 헤어스타일/특징을 활용하면 관계대명사를 쓰지 않고도 간결하고 세련되게 인물을 묘사할 수 있습니다."
            },
            {
                "title": "도구 수단 표현: 'holding a fork and eating'",
                "explanation": "포크를 들고 먹고 있는 복합 동작을 'holding ~ and eating ~'의 병렬 구조로 매끄럽게 연결합니다."
            }
        ],
        "vocabulary": [
            {"word": "ponytail", "ipa": "[ˈpəʊniteɪl]", "pos": "명사", "meaning": "포니테일 (하나로 묶은 머리)", "source": "사진 필수"},
            {"word": "menu", "ipa": "[ˈmenjuː]", "pos": "명사", "meaning": "메뉴판", "source": "사진 필수"},
            {"word": "dishes", "ipa": "[ˈdɪʃɪz]", "pos": "명사", "meaning": "접시들, 식기류", "source": "답변 핵심"},
            {"word": "peaceful time", "ipa": "[ˈpiːsfl taɪm]", "pos": "명사구", "meaning": "평화로운 시간", "source": "답변 핵심"}
        ],
        "scoreTip": "만능문장 #30(looking at a menu)과 #51(eating some food)을 각각 남녀에게 배정하고, 앞쪽 테이블 위 컵과 접시를 덧붙이면 30초가 정확하게 마무리됩니다."
    },
    {
        "id": 7,
        "setNumber": 7,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 7: Outdoor Park Walk (야외 거리/공원 통화 및 대화)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[야외 거리/공원 여성 대화 및 통화 사진] 야외에 여러 사람이 있는 사진. 가운데에 두 여성이 서 있는데, 한 여성은 팔에 가방을 걸치고 손짓을 하며 전화 통화를 하고 있고, 옆의 다른 여성은 친구를 바라보며 귀 기울여 듣고 있음. 그들 뒤쪽에는 한 여성이 벤치에 앉아 있고, 오른쪽 배경에는 푸른 잎이 무성한 나무들이 많음.",
        "photoScene": {
            "category": "야외/공원",
            "locationEn": "outdoors in a park",
            "visualSvg": "outdoor",
            "tags": ["outdoors", "hand gesture", "bench", "trees"]
        },
        "answer": "This is a picture taken outdoors.\nIn the middle of the picture, there are two women. One of them is carrying a bag on her arm, and she is talking on the phone while making a hand gesture.\nNext to her, there is another woman looking at her friend and listening to her.\nBehind them, a woman is sitting on a bench.\nOn the right side of the picture, I can see many green trees.\nOverall, it seems like a beautiful sunny day.",
        "answerTranslation": "이 사진은 야외에서 찍힌 사진입니다.\n사진 가운데에 두 여성이 있습니다. 한 명은 팔에 가방을 걸치고 손짓을 하며 전화 통화를 하고 있습니다.\n그녀 옆의 다른 여성은 친구를 바라보며 이야기를 듣고 있습니다.\n그들 뒤에는 한 여성이 벤치에 앉아 있고, 사진 오른쪽에는 푸른 나무들이 많이 보입니다.\n전반적으로 아름답고 화창한 날 같습니다.",
        "magicSentences": [
            "This is a picture taken outdoors. (야외에서 찍힌 사진입니다)",
            "She is talking on the phone while making a hand gesture. (손짓하며 전화 통화를 하고 있습니다)",
            "Behind them, someone is sitting on a bench. (그들 뒤에 벤치에 앉아 있습니다)",
            "Overall, it seems like a beautiful sunny day. (화창한 날인 것 같습니다)"
        ],
        "grammarPoints": [
            {
                "title": "동시 동작 접속사: 'while making a hand gesture'",
                "explanation": "'talking on the phone while making ~'처럼 while + 현재분사는 두 동작이 동시에 일어남을 나타내는 고득점(IH~AL) 핵심 구문입니다."
            },
            {
                "title": "배경 날씨 총평: 'Overall, it seems like a beautiful sunny day'",
                "explanation": "야외 사진에서는 날씨나 계절감(sunny day, peaceful day)을 언급하며 끝맺는 것이 가장 자연스럽습니다."
            }
        ],
        "vocabulary": [
            {"word": "hand gesture", "ipa": "[hænd ˈdʒestʃə(r)]", "pos": "명사", "meaning": "손짓, 제스처", "source": "사진 필수"},
            {"word": "carry a bag", "ipa": "[ˈkæri ə bæɡ]", "pos": "동사구", "meaning": "가방을 메다/들다", "source": "사진 필수"},
            {"word": "sit on a bench", "ipa": "[sɪt ɒn ə bentʃ]", "pos": "동사구", "meaning": "벤치에 앉다", "source": "답변 핵심"},
            {"word": "sunny day", "ipa": "[ˈsʌni deɪ]", "pos": "명사구", "meaning": "화창한 날", "source": "답변 핵심"}
        ],
        "scoreTip": "통화하며 손을 흔드는 동작은 'making a hand gesture'라는 표현을 쓰면 어휘력 평가에서 높은 가산점을 받습니다."
    },
    {
        "id": 8,
        "setNumber": 8,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 8: Park Trail & Geese (공원 산책로와 벤치 휴식)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[공원 산책로 및 벤치 휴식 사진] 공원에 여러 사람과 거위 2마리가 있는 사진. 왼쪽에는 니트 모자와 자켓을 입은 남성이 산책로를 따라 걸어가고 있어 뒷모습이 보이고, 가운데에는 두 사람이 벤치에 앉아 있는데 그중 한 여성이 다리를 꼬고 앉아 있음. 사진 앞쪽(전면)에는 거위 두 마리가 땅에서 무언가를 쪼아 먹고 있음.",
        "photoScene": {
            "category": "공원/자연",
            "locationEn": "at a park",
            "visualSvg": "park",
            "tags": ["park path", "walking", "crossing legs", "geese"]
        },
        "answer": "This is a picture taken at a park.\nOn the left side of the picture, there is a man walking along the path. I can see his back, and he is wearing a knitted cap and a jacket.\nIn the middle of the picture, two people are sitting on a bench, and one of them is crossing her legs.\nIn the foreground of the picture, there are two geese eating something on the ground.\nOverall, it seems like a peaceful day at the park.",
        "answerTranslation": "이 사진은 공원에서 찍힌 사진입니다.\n사진 왼쪽에는 산책로를 따라 걷고 있는 한 남성이 있습니다. 그의 뒷모습이 보이며 니트 모자와 자켓을 입고 있습니다.\n사진 가운데에는 두 사람이 벤치에 앉아 있고 그중 한 명은 다리를 꼬고 있습니다.\n사진 앞쪽(전면)에는 거위 두 마리가 땅에서 무언가를 먹고 있습니다.\n전반적으로 공원의 평화로운 날 같습니다.",
        "magicSentences": [
            "This is a picture taken at a park. (공원에서 찍힌 사진입니다)",
            "I can see his/her back. (그의 뒷모습이 보입니다)",
            "She is crossing her legs. (그녀는 다리를 꼬고 있습니다)",
            "In the foreground, there are [사물/동물]. (전면에 [사물/동물]이 있습니다)"
        ],
        "grammarPoints": [
            {
                "title": "전면(앞쪽) 위치 표현: 'In the foreground of the picture'",
                "explanation": "사진의 맨 앞쪽을 가리킬 때는 In the foreground, 맨 뒤쪽 배경은 In the background를 쓰는 것이 공간 묘사의 기본 원칙입니다."
            },
            {
                "title": "뒷모습 묘사: 'I can see his/her back'",
                "explanation": "얼굴이 안 보이고 걸어가는 뒷모습만 보일 때 당황하지 말고 'I can see his back'이라고 말해주면 감점 없이 깔끔하게 처리됩니다."
            }
        ],
        "vocabulary": [
            {"word": "knitted cap", "ipa": "[ˈnɪtɪd kæp]", "pos": "명사", "meaning": "니트 모자, 비니", "source": "사진 필수"},
            {"word": "walk along the path", "ipa": "[wɔːk əˈlɒŋ ðə pɑːθ]", "pos": "동사구", "meaning": "길을 따라 걷다", "source": "사진 필수"},
            {"word": "cross one's legs", "ipa": "[krɒs wʌnz leɡz]", "pos": "동사구", "meaning": "다리를 꼬다", "source": "답변 핵심"},
            {"word": "in the foreground", "ipa": "[ɪn ðə ˈfɔːɡraʊnd]", "pos": "전치사구", "meaning": "사진의 전면에, 앞쪽에", "source": "답변 핵심"}
        ],
        "scoreTip": "공원 사진에서 사람이 걷는 모습, 벤치에 앉아 쉬는 모습, 동물(새, 거위 등)을 앞뒤 원근감에 맞게 균형 있게 설명하세요."
    },
    {
        "id": 9,
        "setNumber": 9,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 9: Classic Library (오래된 도서관 서재 3인 학습)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[오래된 도서관/서재 3인 학습 사진] 고풍스러운 도서관(또는 서재)에 남성 2명과 여성 1명(총 3명)이 있는 사진. 왼쪽에는 한 남성이 소파에 앉아 노트에 무언가를 적고(필기하고) 있고, 가운데에는 다른 남성이 책상에서 노트북 화면을 바라보고 있으며 책상 위에 많은 책들이 쌓여 있음. 오른쪽에는 노란색 가디건과 체크무늬 치마를 입은 여성이 빼곡한 책장에서 책을 찾고 있음.",
        "photoScene": {
            "category": "도서관/학습",
            "locationEn": "in a library",
            "visualSvg": "library",
            "tags": ["library", "stacked books", "bookshelf", "cardigan"]
        },
        "answer": "I think this picture was taken in an old library.\nOn the left side of the picture, a man is writing something down in a note while sitting on a sofa.\nIn the middle of the picture, another man is looking at a laptop screen, and many books are stacked on the desk.\nOn the right side of the picture, it seems like a woman wearing a yellow cardigan is looking for a book in the bookshelf.\nOverall, it seems like a peaceful day.",
        "answerTranslation": "이 사진은 오래된 도서관에서 찍힌 것 같습니다.\n사진 왼쪽에서는 한 남성이 소파에 앉아 노트에 무언가를 적고 있습니다.\n사진 가운데에는 다른 남성이 노트북 화면을 보고 있으며, 책상 위에 많은 책들이 쌓여 있습니다.\n사진 오른쪽에는 노란색 가디건을 입은 여성이 책장에서 책을 찾고 있는 것처럼 보입니다.\n전반적으로 평화로운 분위기입니다.",
        "magicSentences": [
            "This picture was taken in an old library. (오래된 도서관에서 찍혔습니다)",
            "He is writing something down in a note. (노트에 무언가를 적고 있습니다)",
            "Many books are stacked on the desk. (많은 책이 책상 위에 쌓여 있습니다)",
            "She is looking for a book in the bookshelf. (책장에서 책을 찾고 있습니다)"
        ],
        "grammarPoints": [
            {
                "title": "사물 상태 수동태: 'are stacked on the desk'",
                "explanation": "책이나 박스 등이 쌓여 있는 모습을 묘사할 때는 수동태인 'are stacked'를 씁니다. 상태 수동태를 구사하면 토스 고득점 기준에 완벽히 부합합니다."
            },
            {
                "title": "복합 수식 분사: 'a woman wearing a yellow cardigan is looking for ~'",
                "explanation": "'현재분사구(wearing ~)'가 앞의 명사 woman을 수식하고, 문장의 본동사 'is looking for'가 이어지는 자연스러운 문장 확장 구문입니다."
            }
        ],
        "vocabulary": [
            {"word": "bookshelf", "ipa": "[ˈbʊkʃelf]", "pos": "명사", "meaning": "책장, 서가", "source": "사진 필수"},
            {"word": "write down", "ipa": "[raɪt daʊn]", "pos": "동사구", "meaning": "적다, 필기하다", "source": "답변 핵심"},
            {"word": "stacked", "ipa": "[stækt]", "pos": "형용사/과거분사", "meaning": "쌓여 있는", "source": "답변 핵심"},
            {"word": "look for", "ipa": "[lʊk fɔː(r)]", "pos": "동사구", "meaning": "~을 찾다", "source": "답변 핵심"}
        ],
        "scoreTip": "도서관/서점에서는 책을 찾는 사람(looking for a book)과 책상 위에 쌓인 책(books are stacked)을 함께 언급해 주는 것이 핵심입니다."
    },
    {
        "id": 10,
        "setNumber": 10,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 10: Classroom Handouts (강의실 유인물 배부 및 전달)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[소규모 강의실 유인물 배부 사진] 작은 교실(강의실)에서 교수로 보이는 남성과 학생들이 있는 사진. 왼쪽에 서 있는 남성이 학생들에게 유인물(프린트물)을 나눠주고 있고, 가운데에 앉아 있는 검정·보라·초록 배색 스웨트셔츠 차림의 남학생이 자기 뒤에 앉은 여학생에게 유인물을 건네주고 있음. 주변의 다른 학생들은 그들을 바라보고 있음.",
        "photoScene": {
            "category": "교실/수업",
            "locationEn": "in a small classroom",
            "visualSvg": "classroom",
            "tags": ["classroom", "distributing handouts", "passing paper", "students"]
        },
        "answer": "I think this is a picture of a small classroom.\nOn the left side of the picture, a man is distributing handouts to the students, and he seems like a professor.\nIn the middle of the picture, another man is passing a handout to a woman behind him. He is wearing a black and purple sweatshirt, and other students are looking at them.",
        "answerTranslation": "이 사진은 작은 교실 사진인 것 같습니다.\n사진 왼쪽에서는 한 남성이 학생들에게 유인물을 나눠주고 있는데, 교수님처럼 보입니다.\n사진 가운데에서는 다른 남성이 자신의 뒤에 있는 여성에게 유인물을 건네주고 있습니다. 그는 검은색과 보라색이 섞인 스웨트셔츠를 입고 있으며, 다른 학생들은 그들을 바라보고 있습니다.",
        "magicSentences": [
            "He is distributing handouts to the students. (학생들에게 유인물을 나눠주고 있습니다)",
            "He is passing a handout to a woman behind him. (뒤에 있는 여성에게 유인물을 건네주고 있습니다)",
            "He seems like a professor. (교수님처럼 보입니다)"
        ],
        "grammarPoints": [
            {
                "title": "배부 동사: 'distributing' vs 전달 동사 'passing/handing'",
                "explanation": "여러 사람에게 골고루 나누어줄 때는 distribute, 뒷사람에게 건넬 때는 pass 또는 hand over를 구분하여 쓰는 것이 어휘 점수의 차별화 포인트입니다."
            },
            {
                "title": "방향 전치사: 'to a woman behind him'",
                "explanation": "'behind him'(그의 뒤에 있는) 전치사구가 woman을 수식하여 인물 간의 앞뒤 위치 관계를 명쾌하게 드러냅니다."
            }
        ],
        "vocabulary": [
            {"word": "handout", "ipa": "[ˈhændaʊt]", "pos": "명사", "meaning": "유인물, 프린트물", "source": "사진 필수"},
            {"word": "distribute", "ipa": "[dɪˈstrɪbjuːt]", "pos": "동사", "meaning": "나누어주다, 배부하다", "source": "답변 핵심"},
            {"word": "pass", "ipa": "[pɑːs]", "pos": "동사", "meaning": "건네주다, 전달하다", "source": "답변 핵심"},
            {"word": "sweatshirt", "ipa": "[ˈswetʃɜːt]", "pos": "명사", "meaning": "맨투맨 셔츠, 스웨트셔츠", "source": "답변 핵심"}
        ],
        "scoreTip": "교실에서 프린트물을 나누어 주는 장면은 토익스피킹에서 주기적으로 출제되는 유형이므로 'distributing handouts' 표현을 꼭 외워두세요."
    },
    {
        "id": 11,
        "setNumber": 11,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 11: Office Lounge (오피스 라운지 정장 여성 3인)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[오피스 라운지 정장 차림 여성 3인 사진] 사무실 휴게실(라운지)에 정장을 입은 여성 3명이 서 있는 사진. 오른쪽 여성은 노트북을 두 손에 든 채 사용하고 있고, 왼쪽의 짧은 갈색 머리 여성은 창틀에 기대어 노트에 무언가를 적고 있으며, 가운데 검은색 정장을 입은 여성은 전화 통화를 하고 있음.",
        "photoScene": {
            "category": "사무실/오피스",
            "locationEn": "in an office lounge",
            "visualSvg": "office",
            "tags": ["office lounge", "formal suit", "leaning against", "laptop"]
        },
        "answer": "I think this is a picture of a staff lounge.\nOn the right side of the picture, a woman is using a laptop computer while holding it.\nOn the left side of the picture, another woman with short brown hair is writing something down in a note. She is leaning against the window frame.\nIn the middle of the picture, another woman wearing a black suit is talking on the phone.",
        "answerTranslation": "이 사진은 직원 라운지 사진인 것 같습니다.\n사진 오른쪽에서는 한 여성이 노트북을 손에 든 채 사용하고 있습니다.\n사진 왼쪽에서는 짧은 갈색 머리를 한 다른 여성이 노트에 무언가를 적고 있으며 창틀에 기대어 있습니다.\n사진 가운데에서는 검은색 정장을 입은 또 다른 여성이 전화 통화를 하고 있습니다.",
        "magicSentences": [
            "This is a picture of a staff lounge. (직원 라운지 사진입니다)",
            "She is using a laptop while holding it. (노트북을 든 채 사용하고 있습니다)",
            "She is leaning against the window frame. (창틀에 기대어 있습니다)",
            "She is wearing a black suit. (검은색 정장을 입고 있습니다)"
        ],
        "grammarPoints": [
            {
                "title": "벽/창틀에 기댐: 'leaning against [사물]'",
                "explanation": "벽이나 기둥, 창틀에 기대어 서 있는 자세는 반드시 전치사 against를 결합하여 'leaning against the wall / window frame'으로 표현합니다."
            },
            {
                "title": "동성 3인 지칭 테크닉: 'a woman ➡️ another woman ➡️ another woman'",
                "explanation": "모두 여성일 때는 'She'만 반복하면 혼동을 주므로 'a woman', 'another woman with short hair', 'the other woman'으로 주어를 분리합니다."
            }
        ],
        "vocabulary": [
            {"word": "staff lounge", "ipa": "[stɑːf laʊndʒ]", "pos": "명사", "meaning": "직원 휴게실, 라운지", "source": "사진 필수"},
            {"word": "lean against", "ipa": "[liːn əˈɡenst]", "pos": "동사구", "meaning": "~에 기대다", "source": "답변 핵심"},
            {"word": "window frame", "ipa": "[ˈwɪndəʊ freɪm]", "pos": "명사", "meaning": "창틀", "source": "답변 핵심"},
            {"word": "black suit", "ipa": "[blæk suːt]", "pos": "명사", "meaning": "검은색 정장", "source": "답변 핵심"}
        ],
        "scoreTip": "오피스 사진에서는 'formal clothes'나 'suit'라는 복장 어휘와 'leaning against'라는 자세 어휘를 구사하면 고급스러운 인상을 줍니다."
    },
    {
        "id": 12,
        "setNumber": 12,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 12: Device Multitasking (휴게실 3인 전자기기 사용)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[직원 휴게실 남녀 3인 전자기기 사용 사진] 실내 휴게실에 여성 2명과 남성 1명이 있는 사진. 오른쪽에는 줄무늬 셔츠를 입은 여성이 테이블에서 노트북으로 타이핑을 하고 있고, 왼쪽에는 다른 여성이 스마트폰을 들여다보고 있으며, 가운데 뒤쪽에는 한 남성이 노트북 화면을 보면서 전화 통화를 하고 있음.",
        "photoScene": {
            "category": "휴게실/기기",
            "locationEn": "in a staff room",
            "visualSvg": "devices",
            "tags": ["smartphone", "typing", "striped shirt", "multitasking"]
        },
        "answer": "I think this picture was taken in a staff lounge.\nOn the right side of the picture, a woman wearing a striped shirt is typing on a laptop computer. It seems like she is watching a video.\nOn the left side of the picture, another woman is looking at her smartphone.\nIn the middle of the picture, a man is talking on the phone while looking at a laptop screen.",
        "answerTranslation": "이 사진은 직원 휴게실에서 찍힌 것 같습니다.\n사진 오른쪽에는 줄무늬 셔츠를 입은 여성이 노트북으로 타이핑을 하고 있는데, 영상을 보고 있는 것처럼 보입니다.\n사진 왼쪽에는 다른 여성이 스마트폰을 보고 있습니다.\n사진 가운데에는 한 남성이 노트북 화면을 보면서 전화 통화를 하고 있습니다.",
        "magicSentences": [
            "She is typing on a laptop computer. (노트북으로 타이핑을 하고 있습니다)",
            "She is looking at her smartphone. (스마트폰을 들여다보고 있습니다)",
            "He is talking on the phone while looking at a screen. (화면을 보며 전화 통화를 하고 있습니다)"
        ],
        "grammarPoints": [
            {
                "title": "기기 조작의 전치사: 'typing on a laptop'",
                "explanation": "컴퓨터나 키보드로 타이핑할 때 전치사는 on을 쓰며 'typing on a keyboard / laptop'으로 표현합니다."
            },
            {
                "title": "패턴 복장 표현: 'a striped shirt'",
                "explanation": "줄무늬는 striped, 체크무늬는 checked 또는 plaid로 표현하여 인물의 시각적 특징을 디테일하게 강조합니다."
            }
        ],
        "vocabulary": [
            {"word": "striped shirt", "ipa": "[straɪpt ʃɜːt]", "pos": "명사", "meaning": "줄무늬 셔츠", "source": "사진 필수"},
            {"word": "typing on", "ipa": "[ˈtaɪpɪŋ ɒn]", "pos": "동사구", "meaning": "~에 타이핑하다", "source": "답변 핵심"},
            {"word": "smartphone", "ipa": "[ˈsmɑːtfəʊn]", "pos": "명사", "meaning": "스마트폰", "source": "사진 필수"},
            {"word": "multitasking", "ipa": "[ˌmʌltiˈtɑːskɪŋ]", "pos": "명사", "meaning": "다중 작업", "source": "답변 핵심"}
        ],
        "scoreTip": "각 인물이 사용하는 기기(laptop, smartphone, phone)를 명확히 구분하여 문장마다 하나씩 배분하면 4문장으로 완벽한 만점 묘사가 됩니다."
    },
    {
        "id": 13,
        "setNumber": 13,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 13: Outdoor Flea Market (야외 벼룩시장 중고 카메라 판매)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[야외 벼룩시장 중고 카메라 판매 사진] 야외 마켓 테이블 위에 다양한 종류의 중고 카메라들이 진열되어 있고, 상인과 손님이 테이블을 사이에 두고 서 있는 사진. 뒤쪽 배경에는 차들이 주차되어 있고 파라솔과 나무들이 보임.",
        "photoScene": {
            "category": "시장/마켓",
            "locationEn": "at an outdoor flea market",
            "visualSvg": "market",
            "tags": ["flea market", "cameras displayed", "parked cars", "parasol"]
        },
        "answer": "This is a picture taken outdoors at a flea market.\nIn the foreground of the picture, many kinds of used cameras are displayed on the table.\nAround the table, people are looking at the products and having a conversation.\nIn the background of the picture, some cars are parked, and I can see some trees and parasols.\nOverall, it seems like a peaceful day.",
        "answerTranslation": "이 사진은 야외 벼룩시장에서 찍힌 사진입니다.\n사진 앞쪽 테이블 위에는 여러 종류의 중고 카메라들이 진열되어 있습니다.\n테이블 주변에서는 사람들이 제품을 보며 대화를 나누고 있습니다.\n사진 배경에는 차들이 몇 대 주차되어 있고 나무와 파라솔도 보입니다.\n전반적으로 평화로운 날 같습니다.",
        "magicSentences": [
            "This is a picture taken outdoors at a flea market. (야외 벼룩시장에서 찍힌 사진입니다)",
            "Products are displayed on the table. (물품들이 테이블에 진열되어 있습니다)",
            "They are having a conversation. (대화를 나누고 있습니다)",
            "Cars are parked in the background. (배경에 차들이 주차되어 있습니다)"
        ],
        "grammarPoints": [
            {
                "title": "사물 중심 사진의 전개: 전면 사물 ➡️ 인물 행동 ➡️ 배경",
                "explanation": "인물보다 진열 상품이 주인공인 시장 사진에서는 'In the foreground ~ cameras are displayed'로 사물을 먼저 잡는 것이 정석입니다."
            },
            {
                "title": "차량 주차 상태: 'cars are parked'",
                "explanation": "자동차가 주차되어 있는 상태는 수동태 'are parked'를 쓰며, 주차장이나 길가 배경 사진의 필수 만능 표현입니다."
            }
        ],
        "vocabulary": [
            {"word": "flea market", "ipa": "[ˈfliː mɑːkɪt]", "pos": "명사", "meaning": "벼룩시장", "source": "사진 필수"},
            {"word": "used cameras", "ipa": "[juːzd ˈkæmərəz]", "pos": "명사", "meaning": "중고 카메라들", "source": "사진 필수"},
            {"word": "are parked", "ipa": "[ɑː pɑːkt]", "pos": "동사구(수동태)", "meaning": "주차되어 있다", "source": "답변 핵심"},
            {"word": "parasol", "ipa": "[ˈpærəsɒl]", "pos": "명사", "meaning": "파라솔, 차양", "source": "사진 필수"}
        ],
        "scoreTip": "사물 비중이 큰 야외 마켓에서는 수동태(are displayed, are parked)를 자연스럽게 활용하여 풍경을 입체적으로 묘사하세요."
    },
    {
        "id": 14,
        "setNumber": 14,
        "qNumber": "Question 3 / 4",
        "setTitle": "Set 14: Busy Cafe Counter (카페 카운터 주문 및 음료 제조)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": "[카페 카운터 주문 및 커피 제조 사진] 카페 카운터 주변에 5명의 사람이 있는 사진. 가운데 계산대에서는 회색 티셔츠를 입은 여성 직원이 태블릿을 이용해 정장 차림의 남성 고객에게서 주문을 받고 있고, 왼쪽 뒤편에서는 다른 남성 바리스타가 커피 머신으로 커피를 내리고 있음. 천장(사진 위쪽)에는 알록달록한 조명 여러 개가 매달려 있음.",
        "photoScene": {
            "category": "카페/카운터",
            "locationEn": "at a busy cafe counter",
            "visualSvg": "busycafe",
            "tags": ["taking an order", "making coffee", "colorful lights", "busy"]
        },
        "answer": "I think this picture was taken in a cafe.\nIn the middle of the picture, a woman wearing a gray t-shirt is taking an order from a man at the counter.\nOn the left side of the picture, it seems like another man is making some coffee.\nAt the top of the picture, many colorful lights are hanging from the ceiling.\nOverall, it seems like they are busy.",
        "answerTranslation": "이 사진은 카페에서 찍힌 것 같습니다.\n사진 가운데 카운터에서는 회색 티셔츠를 입은 여성이 한 남성으로부터 주문을 받고 있습니다.\n사진 왼쪽에서는 다른 남성이 커피를 만들고 있는 것처럼 보입니다.\n사진 위쪽 천장에는 알록달록한 조명 여러 개가 매달려 있습니다.\n전반적으로 바쁜 분위기입니다.",
        "magicSentences": [
            "This picture was taken in a cafe. (카페에서 찍혔습니다)",
            "She is taking an order from a customer. (고객에게서 주문을 받고 있습니다)",
            "He is making some coffee. (커피를 만들고 있습니다)",
            "Overall, it seems like they are busy. (전반적으로 바빠 보입니다)"
        ],
        "grammarPoints": [
            {
                "title": "주문 접수 핵심 구문: 'taking an order from [사람]'",
                "explanation": "주문을 '받다'는 take an order이며, 전치사 from을 붙여 'is taking an order from a customer'로 두 사람을 한 번에 엮어주는 고난도 압축 기법입니다."
            },
            {
                "title": "위치 천장 표현: 'At the top of the picture / hanging from the ceiling'",
                "explanation": "사진 윗부분을 칭할 때는 'At the top of the picture', 천장에 매달린 것은 'hanging from the ceiling'으로 표현하여 시선의 상하 이동을 보여줍니다."
            }
        ],
        "vocabulary": [
            {"word": "take an order", "ipa": "[teɪk ən ˈɔːdə(r)]", "pos": "동사구", "meaning": "주문을 받다", "source": "사진 필수"},
            {"word": "make coffee", "ipa": "[meɪk ˈkɒfi]", "pos": "동사구", "meaning": "커피를 내리다/만들다", "source": "답변 핵심"},
            {"word": "hang from the ceiling", "ipa": "[hæŋ frəm ðə ˈsiːlɪŋ]", "pos": "동사구", "meaning": "천장에 매달려 있다", "source": "사진 필수"},
            {"word": "busy", "ipa": "[ˈbɪzi]", "pos": "형용사", "meaning": "분주한, 바쁜", "source": "답변 핵심"}
        ],
        "scoreTip": "주문을 받는 직원과 손님을 따로 떼지 않고 'taking an order from a man'으로 한 문장에 묶으면 발화 시간을 크게 아낄 수 있습니다."
    }
]

master["part2"] = part2_photo_questions
master["metadata"]["part2_count"] = len(part2_photo_questions)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print(f"Successfully integrated Part 2: {len(part2_photo_questions)} photo sets into data.json!")
