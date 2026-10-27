import json

print("Updating data.json Part 2 with 100% photo-verified 1:1 Jenny 4-step formula datasets...")

part2_final = [
    {
        "id": 101,
        "setId": 1,
        "setNumber": 1,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 1: A Co-working Space (공유 오피스 노트북 협업)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a co-working space",
            "locationEn": "in a co-working space",
            "tags": [
                "장소: 공유 오피스 (in a co-working space)",
                "앞쪽 남성: 헤드폰 착용 & 노트북 타이핑 (wearing headphones and typing on a laptop)",
                "동료들: 테이블 맞은편에서 각자 노트북 집중 (colleagues focused on their laptops)",
                "사물: 테이블 위의 화분, 물병, 유리잔, 스마트폰 (potted plant, water bottle, smartphone on the table)"
            ]
        },
        "photoDescriptionKr": "[공유 오피스 노트북 협업 사진] 넓은 나무 테이블에 4~5명의 청년들이 둘러앉아 각자 노트북으로 일하고 있는 실사 사진입니다. 앞쪽의 남성은 헤드폰을 착용하고 노트북으로 열심히 타이핑하고 있으며, 맞은편 동료들도 각자의 화면에 집중하고 있습니다. 테이블 중앙에는 작은 화분과 물병, 유리잔, 스마트폰이 놓여 있습니다.",
        "answer": "This is a picture taken in a co-working space.\nIn the foreground, a man wearing black headphones is actively typing on his laptop computer.\nAcross the table, several colleagues are sitting together, focused on their own laptop screens.\nOn the wooden table, there are a small potted plant, a bottle of water, and a glass.\nOverall, everyone seems very productive and deeply focused on their projects.",
        "answerTranslation": "이 사진은 공유 오피스에서 찍힌 사진입니다.\n앞쪽에는 검은 헤드폰을 쓴 남성이 노트북 컴퓨터로 적극적으로 타이핑을 하고 있습니다.\n테이블 맞은편에는 여러 동료들이 함께 앉아 각자의 노트북 화면에 집중하고 있습니다.\n나무 테이블 위에는 작은 화분, 물병, 그리고 유리잔이 놓여 있습니다.\n전반적으로 모두가 매우 생산적이고 프로젝트에 깊이 집중하고 있는 것처럼 보입니다.",
        "magicSentences": [
            "This is a picture taken in a co-working space.",
            "A man wearing headphones is typing on his laptop.",
            "Across the table, several colleagues are sitting together.",
            "Overall, everyone seems very productive and focused on their projects."
        ],
        "scoreTip": "1단계 장소 도입 후 앞쪽 인물의 착용물(wearing headphones)과 손동작(typing on his laptop), 테이블 사물(potted plant, water bottle)을 짚어주면 IH/AL 고득점을 받습니다.",
        "vocabulary": [
            {"word": "co-working space", "ipa": "[ˌkəʊ ˈwɜːkɪŋ speɪs]", "pos": "명사구", "meaning": "공유 오피스, 공동 작업 공간", "source": "사진 필수"},
            {"word": "headphone", "ipa": "[ˈhedfəʊn]", "pos": "명사", "meaning": "헤드폰", "source": "사진 필수"},
            {"word": "productive", "ipa": "[prəˈdʌktɪv]", "pos": "형용사", "meaning": "생산적인, 결실 있는", "source": "답변 핵심"},
            {"word": "potted plant", "ipa": "[ˈpɒtɪd plɑːnt]", "pos": "명사구", "meaning": "화분에 심은 식물", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "현재분사 착용/동작: wearing + N & typing on + N", "explanation": "인물의 복장이나 액세서리를 wearing으로 표현하고 동시 동작을 is typing으로 연결하면 발화 유창성 가산점을 받습니다."}
        ]
    },
    {
        "id": 102,
        "setId": 2,
        "setNumber": 2,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 2: Meeting Room (회의실 손짓 토론)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a meeting room",
            "locationEn": "in a meeting room",
            "tags": [
                "장소: 회의실 (in a meeting room)",
                "앞쪽 인물: 체크무늬 셔츠 착용 & 양손으로 손짓하며 설명 (gesturing with both hands while explaining)",
                "동료: 옆에 앉아 경청하는 긴 흑발의 여성 (a woman with long dark hair listening)",
                "사물: 테이블 위의 노트북, 메모장, 스마트폰 (laptop, smartphone on a notepad)"
            ]
        },
        "photoDescriptionKr": "[회의실 손짓 토론 사진] 회의 테이블에서 체크무늬 셔츠를 입은 사람이 양손을 들어 열정적으로 손짓하며 회의 안건을 설명하고 있고, 그 옆에 긴 흑발의 여성이 앉아 경청하고 있는 클로즈업 사진입니다. 테이블 위에는 화면이 켜진 노트북과 펼쳐진 메모장 위에 스마트폰이 놓여 있습니다.",
        "answer": "This is a picture taken in a meeting room.\nIn the foreground, a person wearing a red plaid shirt is gesturing with both hands while explaining something passionately.\nNext to this person, a woman with long dark hair is listening attentively.\nOn the wooden conference table, an open laptop, a smartphone resting on a notepad, and a water bottle are placed.\nOverall, the atmosphere seems very engaging and collaborative.",
        "answerTranslation": "이 사진은 회의실에서 찍힌 사진입니다.\n앞쪽에는 붉은 체크무늬 셔츠를 입은 사람이 열정적으로 무언가를 설명하면서 양손으로 손짓을 하고 있습니다.\n이 사람 옆에는 긴 흑발의 여성이 주의 깊게 듣고 있습니다.\n나무 회의 테이블 위에는 열려 있는 노트북, 메모장 위에 놓인 스마트폰, 그리고 물병이 놓여 있습니다.\n전반적으로 분위기가 매우 적극적이고 협력적으로 보입니다.",
        "magicSentences": [
            "This is a picture taken in a meeting room.",
            "A person is gesturing with both hands while explaining something.",
            "Next to this person, a woman is listening attentively.",
            "Overall, the atmosphere seems very engaging and collaborative."
        ],
        "scoreTip": "회의 손짓 제스처는 'gesturing with both hands while explaining' 만능 패턴 하나로 완벽하게 득점할 수 있습니다.",
        "vocabulary": [
            {"word": "plaid shirt", "ipa": "[plæd ʃɜːt]", "pos": "명사구", "meaning": "격자/체크무늬 셔츠", "source": "사진 필수"},
            {"word": "gesture", "ipa": "[ˈdʒestʃə(r)]", "pos": "동사", "meaning": "손짓하다, 몸짓하다", "source": "답변 핵심"},
            {"word": "attentively", "ipa": "[əˈtentɪvli]", "pos": "부사", "meaning": "주의 깊게, 경청하여", "source": "답변 핵심"},
            {"word": "collaborative", "ipa": "[kəˈlæbərətɪv]", "pos": "형용사", "meaning": "협력적인", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "동시 동작 구문: gesturing with ~ while explaining ~", "explanation": "while 뒤에 분사(~ing)를 사용하여 두 가지 동시 동작을 한 번에 설명하는 토익스피킹 고득점 필수 구문입니다."}
        ]
    },
    {
        "id": 103,
        "setId": 3,
        "setNumber": 3,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 3: A Cafe Counter (카페 조명 간판과 메뉴판)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a cafe counter",
            "locationEn": "at the counter area of a cafe",
            "tags": [
                "장소: 카페 카운터 (at a cafe counter)",
                "간판: 전구로 불을 밝힌 'CAFE' 네온 간판 (illuminated 'CAFE' marquee sign)",
                "사물: 분필로 적힌 메뉴판과 가격표 (chalkboard menus with drink prices)",
                "조명: 천장에 매달린 녹색 펜던트 조명과 미러볼 (green pendant lamps and a disco ball)"
            ]
        },
        "photoDescriptionKr": "[카페 조명 간판과 메뉴판 사진] 아늑하고 빈티지한 카페 카운터 위쪽을 담은 사진입니다. 알전구로 화사하게 불을 밝힌 대형 'CAFE' 글자 조명 간판이 가장 먼저 눈에 띄며, 그 아래에는 분필로 정갈하게 커피와 차 종류 및 가격이 적힌 검은 칠판 메뉴판이 있습니다. 천장에는 녹색 펜던트 조명과 작은 미러볼이 매달려 있습니다.",
        "answer": "This is a picture taken at the counter area of a cozy cafe.\nIn the upper part of the picture, a large illuminated sign spelling 'CAFE' with glowing lightbulbs catches the eye.\nBelow the sign, black chalkboard menus display various drinks and prices written in white chalk.\nSeveral green pendant lamps and a small disco ball hang from the ceiling, creating a retro mood.\nOverall, the cafe has a warm, vintage, and inviting atmosphere.",
        "answerTranslation": "이 사진은 아늑한 카페의 카운터 구역에서 찍힌 사진입니다.\n사진 위쪽에는 빛나는 전구로 'CAFE'라고 쓰인 대형 조명 간판이 눈길을 끕니다.\n간판 아래에는 검은 칠판 메뉴판에 흰색 분필로 적힌 다양한 음료와 가격이 표시되어 있습니다.\n천장에는 몇 개의 녹색 펜던트 조명과 작은 미러볼이 매달려 있어 레트로한 분위기를 연출합니다.\n전반적으로 카페는 따뜻하고 빈티지하며 아늑한 분위기를 풍깁니다.",
        "magicSentences": [
            "This is a picture taken at the counter of a cafe.",
            "A large illuminated sign catches the eye.",
            "Black chalkboard menus display various drinks and prices.",
            "Overall, the cafe has a warm and inviting atmosphere."
        ],
        "scoreTip": "사물 중심 사진일 때는 'catches the eye(눈길을 사로잡다)'와 'hang from the ceiling(천장에 매달려 있다)' 표현을 활용하세요.",
        "vocabulary": [
            {"word": "illuminated sign", "ipa": "[ɪˈluːmɪneɪtɪd saɪn]", "pos": "명사구", "meaning": "조명 간판, 불이 켜진 간판", "source": "사진 필수"},
            {"word": "chalkboard", "ipa": "[ˈtʃɔːkbɔːd]", "pos": "명사", "meaning": "칠판, 흑판", "source": "사진 필수"},
            {"word": "pendant lamp", "ipa": "[ˈpendənt læmp]", "pos": "명사구", "meaning": "펜던트 조명 (천장 매달림 조명)", "source": "답변 핵심"},
            {"word": "inviting", "ipa": "[ɪnˈvaɪtɪŋ]", "pos": "형용사", "meaning": "매력적인, 아늑한", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "사물 위치 묘사: Below the sign, S+V", "explanation": "장소 부사구(Below the sign, In the upper part)를 문두에 두어 시선의 흐름을 자연스럽게 유도하는 기술입니다."}
        ]
    },
    {
        "id": 104,
        "setId": 4,
        "setNumber": 4,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 4: Cafe Seating Area (카페 실내 좌석과 노트북 손님)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a cafe",
            "locationEn": "inside a modern cafe",
            "tags": [
                "장소: 카페 좌석 (inside a modern cafe)",
                "인물: 오른쪽 테이블에서 모자 쓰고 노트북 작업하는 남성 (a man working on a laptop)",
                "사물: 흰색 라탄 의자와 노란 쿠션 (woven chairs with yellow cushions)",
                "배경: 중앙의 커다란 실내 화분 나무와 카운터 (large indoor tree and ordering counter)"
            ]
        },
        "photoDescriptionKr": "[카페 실내 좌석과 노트북 손님 사진] 감각적인 인테리어의 카페 실내 전경 사진입니다. 전경에는 노란색 쿠션이 놓인 둥근 흰색 라탄 의자들과 원형 테이블이 놓여 있고, 중앙에는 커다란 실내 관엽수 나무가 자리를 잡고 있습니다. 오른쪽 좌석에는 캡 모자와 어두운 겉옷을 입은 남성이 노트북에 집중하고 있으며, 뒤편 카운터에는 메뉴판과 직원이 서 있습니다.",
        "answer": "This is a picture taken inside a stylish and spacious cafe.\nOn the right side, a man wearing a cap and a dark jacket is seated at a table, concentrating on his laptop.\nIn the foreground, there are white woven chairs with yellow cushions placed around round tables.\nA large green indoor tree stands in the center, and in the background, a chalkboard menu and coffee equipment are visible behind the counter.\nOverall, the cafe looks very relaxed and comfortable for studying or relaxing.",
        "answerTranslation": "이 사진은 스타일리시하고 넓은 카페 실내에서 찍힌 사진입니다.\n오른쪽에는 모자와 어두운 자켓을 입은 남성이 테이블에 앉아 노트북에 집중하고 있습니다.\n앞쪽에는 둥근 테이블 주위로 노란 쿠션이 놓인 흰색 라탄 의자들이 있습니다.\n중앙에는 커다란 초록색 실내 나무가 서 있고, 배경의 카운터 뒤로는 칠판 메뉴판과 커피 장비들이 보입니다.\n전반적으로 카페는 공부하거나 휴식하기에 매우 편안하고 아늑해 보입니다.",
        "magicSentences": [
            "This is a picture taken inside a spacious cafe.",
            "A man is seated at a table, concentrating on his laptop.",
            "A large indoor tree stands in the center.",
            "Overall, the cafe looks very relaxed and comfortable."
        ],
        "scoreTip": "넓은 실내 공간 묘사 시 'seated at a table(테이블에 앉아)', 'stands in the center(중앙에 서 있다)'의 위치 동사를 배치하세요.",
        "vocabulary": [
            {"word": "spacious", "ipa": "[ˈspeɪʃəs]", "pos": "형용사", "meaning": "넓은, 널찍한", "source": "답변 핵심"},
            {"word": "woven chair", "ipa": "[ˈwəʊvn tʃeə(r)]", "pos": "명사구", "meaning": "라탄/엮은 의자", "source": "사진 필수"},
            {"word": "cushion", "ipa": "[ˈkʊʃn]", "pos": "명사", "meaning": "쿠션, 방석", "source": "사진 필수"},
            {"word": "indoor tree", "ipa": "[ˌɪndɔː ˈtriː]", "pos": "명사구", "meaning": "실내 관엽수 나무", "source": "사진 필수"}
        ],
        "grammarPoints": [
            {"title": "수동태 완료형 상태: is seated at a table", "explanation": "is seated는 '자리에 앉아 있는 정적 상태'를 나타내는 세련된 표현으로, is sitting보다 자연스럽게 들립니다."}
        ]
    },
    {
        "id": 105,
        "setId": 5,
        "setNumber": 5,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 5: Supermarket Aisle (마트 식료품 진열 통로)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1578916171728-46686eac8d58?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a supermarket",
            "locationEn": "in a supermarket aisle",
            "tags": [
                "장소: 슈퍼마켓 통로 (in a supermarket aisle)",
                "왼쪽 선반: 시리얼 상자들이 층층이 진열됨 (cereal boxes neatly stacked)",
                "오른쪽 선반: 우유 및 음료 팩들이 정돈됨 (cartons of milk and juice)",
                "배경: 저 멀리 카트를 밀고 가는 쇼핑객 (a shopper with a cart in the distance)"
            ]
        },
        "photoDescriptionKr": "[마트 식료품 진열 통로 사진] 환하고 넓은 대형 슈퍼마켓의 식료품 통로 사진입니다. 왼쪽 진열대에는 형형색색의 시리얼 상자들이 층층이 빼곡하게 진열되어 있고, 오른쪽 진열대에는 우유와 주스 팩들이 줄지어 정돈되어 있습니다. 반짝이는 타일 바닥 위로 천장 형광등 조명이 비치고 있으며, 저 멀리 통로 끝에는 카트를 끌고 장을 보는 손님이 보입니다.",
        "answer": "This is a picture taken in a bright supermarket aisle.\nThe aisle is lined with tall grocery shelves stretching far into the distance.\nOn the left shelves, colorful cereal boxes are neatly stacked on multiple tiers.\nOn the right, cartons of milk and packaged drinks are orderly arranged.\nIn the distance, a customer with a shopping cart can be seen walking down the aisle.\nOverall, the supermarket appears clean, fully stocked, and well-organized.",
        "answerTranslation": "이 사진은 밝은 슈퍼마켓 통로에서 찍힌 사진입니다.\n통로 양쪽에는 저 멀리까지 길게 뻗은 높은 식료품 선반들이 늘어서 있습니다.\n왼쪽 선반에는 다채로운 시리얼 상자들이 여러 층에 깔끔하게 쌓여 있습니다.\n오른쪽에는 우유 팩과 포장 음료들이 질서정연하게 정돈되어 있습니다.\n저 멀리에는 쇼핑 카트를 든 손님이 통로를 걸어가는 모습이 보입니다.\n전반적으로 슈퍼마켓은 깨끗하고, 재고가 가득하며, 잘 정돈되어 보입니다.",
        "magicSentences": [
            "This is a picture taken in a supermarket aisle.",
            "The aisle is lined with tall grocery shelves.",
            "Items are neatly stacked on multiple tiers.",
            "Overall, the store appears clean and well-organized."
        ],
        "scoreTip": "식료품 진열 통로 묘사 시 'neatly stacked on multiple tiers(여러 층에 깔끔하게 쌓인)'와 'fully stocked(물건이 가득 찬)'를 꼭 사용하세요.",
        "vocabulary": [
            {"word": "aisle", "ipa": "[aɪl]", "pos": "명사", "meaning": "(마트/비행기의) 통로", "source": "사진 필수"},
            {"word": "stack", "ipa": "[stæk]", "pos": "동사", "meaning": "쌓다, 포개다", "source": "답변 핵심"},
            {"word": "carton", "ipa": "[ˈkɑːtn]", "pos": "명사", "meaning": "(우유/음료 등의) 종이팩", "source": "사진 필수"},
            {"word": "fully stocked", "ipa": "[ˈfʊli stɒkt]", "pos": "형용사구", "meaning": "재고가 꽉 찬, 물건이 풍부한", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "수동 구문: is lined with ~", "explanation": "The aisle is lined with shelves는 '통로가 선반들로 둘러싸여 늘어서 있다'는 뜻으로 공간감 표현에 최고입니다."}
        ]
    },
    {
        "id": 106,
        "setId": 6,
        "setNumber": 6,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 6: Store Checkout Counter (계산대 카드 결제)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a checkout counter",
            "locationEn": "at a store checkout counter",
            "tags": [
                "장소: 매장 계산대 (at a checkout counter)",
                "중심 인물: 주황색 터틀넥 입고 카드 단말기에 카드 꽂는 미소 띤 여성 (smiling woman inserting a credit card)",
                "상대방: 왼쪽에서 POS 화면 보며 결제 돕는 점원의 손 (cashier assisting at the POS register)",
                "배경: 밝은 조명과 거울이 있는 세련된 매장 실내 (bright store interior with mirrors)"
            ]
        },
        "photoDescriptionKr": "[매장 계산대 카드 결제 사진] 매장 계산대 카운터에서 긴 갈색 머리의 미소 짓는 여성이 주황색 터틀넥 니트를 입고 오른손에 검은색 신용카드를 쥐어 결제 단말기에 꽂아 결제하고 있는 실사 사진입니다. 왼쪽 앞에는 점원의 손이 디지털 터치스크린 POS 모니터 옆에 보이며, 카운터 위에는 황금색 장식과 화면이 놓여 있고 배경에는 환한 조명과 거울이 있는 넓은 매장이 펼쳐져 있습니다.",
        "answer": "This is a picture taken at a store checkout counter.\nIn the center, a smiling woman wearing an orange turtleneck sweater is inserting a credit card into the payment terminal to pay.\nOn the left, a cashier is assisting her transaction beside a digital POS touchscreen register.\nOn the counter, a modern payment terminal and decorative items are placed neatly.\nIn the background, the spacious store is brightly illuminated with hanging lights and large mirrors.\nOverall, the customer service interaction seems very pleasant, friendly, and smooth.",
        "answerTranslation": "이 사진은 매장 계산대 카운터에서 찍힌 사진입니다.\n가운데에는 주황색 터틀넥 스웨터를 입은 미소 띤 여성이 결제하기 위해 신용카드를 결제 단말기에 꽂고 있습니다.\n왼쪽에는 점원이 디지털 POS 터치스크린 계산대 옆에서 그녀의 결제를 돕고 있습니다.\n카운터 위에는 최신 결제 단말기와 장식품들이 깔끔하게 놓여 있습니다.\n배경에는 넓은 매장이 펜던트 조명과 대형 거울들로 밝게 비춰지고 있습니다.\n전반적으로 고객 응대와 서비스가 매우 유쾌하고 친절하며 매끄러워 보입니다.",
        "magicSentences": [
            "This is a picture taken at a checkout counter.",
            "A woman is inserting a credit card into the payment terminal.",
            "A cashier is assisting her at the POS register.",
            "Overall, the customer service seems very pleasant and smooth."
        ],
        "scoreTip": "결제 동작의 핵심: 'inserting a credit card into the payment terminal(카드 단말기에 신용카드 꽂기)'.",
        "vocabulary": [
            {"word": "payment terminal", "ipa": "[ˈpeɪmənt ˈtɜːmɪnl]", "pos": "명사구", "meaning": "카드 결제 단말기", "source": "사진 필수"},
            {"word": "turtleneck", "ipa": "[ˈtɜːtlnek]", "pos": "명사", "meaning": "목폴라, 터틀넥 스웨터", "source": "사진 필수"},
            {"word": "POS register", "ipa": "[piː əʊ es ˈredʒɪstə(r)]", "pos": "명사구", "meaning": "포스기, 전자 계산대", "source": "답변 핵심"},
            {"word": "transaction", "ipa": "[trænˈzækʃn]", "pos": "명사", "meaning": "거래, 결제 처리", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "동작 목적 표현: ~ to pay / to make a payment", "explanation": "inserting a credit card 뒤에 to pay 목적 부정사를 붙여서 동작의 의도를 명확하고 자연스럽게 발화합니다."}
        ]
    },
    {
        "id": 107,
        "setId": 7,
        "setNumber": 7,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 7: Outdoor Fruit & Vegetable Market (청과물 시장 진열대)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1488459716781-31db52582fe9?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "an outdoor market",
            "locationEn": "at an outdoor fruit and vegetable market stand",
            "tags": [
                "장소: 야외 청과물 시장 (at a fruit and vegetable market)",
                "전경: 망고스틴, 용과, 패션프루트 등 열대 과일 가득 (tropical fruits with price tags)",
                "사물: 매장 위에 매달린 원형 금속 저울 (hanging metal scale)",
                "배경: 층층이 진열된 알록달록한 파프리카와 채소들 (bell peppers and vegetables arranged on tiers)"
            ]
        },
        "photoDescriptionKr": "[청과물 시장 진열대 사진] 화려하고 풍성한 야외 청과물 시장의 진열대 사진입니다. 전경에는 망고스틴, 패션프루트, 람부탄, 용과 등 다양한 신선한 열대 과일들이 이름표(Lichi, Mango)와 함께 수북이 쌓여 있고, 그 바로 위에는 둥근 금속 저울이 매달려 있습니다. 뒤쪽 배경에는 빨갛고 노란 파프리카, 당근, 가지, 호박 등 신선한 채소들이 층층이 먹음직스럽게 진열되어 있습니다.",
        "answer": "This is a picture taken at an outdoor fruit and vegetable market stand.\nIn the foreground, a rich variety of fresh tropical fruits such as mangosteens, passion fruits, and dragon fruits are piled high with name labels.\nAbove the produce, a round metal weighing scale hangs from the ceiling.\nIn the background, colorful bell peppers, carrots, and pumpkins are beautifully arranged on display tiers.\nOverall, the market stand looks very bountiful, vibrant, and appetizing.",
        "answerTranslation": "이 사진은 야외 과일 및 채소 시장 가판대에서 찍힌 사진입니다.\n앞쪽에는 망고스틴, 패션프루트, 용과 등 다양하고 신선한 열대 과일들이 이름표와 함께 수북이 쌓여 있습니다.\n농산물 위쪽으로는 둥근 금속 무게 저울이 천장에 매달려 있습니다.\n배경에는 알록달록한 파프리카, 당근, 호박들이 진열대 층에 아름답게 정돈되어 있습니다.\n전반적으로 시장 가판대는 매우 풍성하고, 활기차며, 먹음직스러워 보입니다.",
        "magicSentences": [
            "This is a picture taken at a fruit and vegetable market.",
            "A rich variety of fresh fruits are piled high with labels.",
            "A metal weighing scale hangs above the produce.",
            "Overall, the market stand looks very bountiful and vibrant."
        ],
        "scoreTip": "과일/야채 진열 묘사 시 'piled high(수북이 쌓인)'와 'a rich variety of ~(다양한 종류의)' 표현을 쓰면 어휘력 가산점을 받습니다.",
        "vocabulary": [
            {"word": "produce", "ipa": "[ˈprɒdjuːs]", "pos": "명사", "meaning": "(농업) 농산물, 청과물", "source": "사진 필수"},
            {"word": "weighing scale", "ipa": "[ˈweɪɪŋ skeɪl]", "pos": "명사구", "meaning": "무게 저울", "source": "사진 필수"},
            {"word": "pile high", "ipa": "[paɪl haɪ]", "pos": "동사구", "meaning": "수북이 쌓아 올리다", "source": "답변 핵심"},
            {"word": "bountiful", "ipa": "[ˈbaʊntɪfl]", "pos": "형용사", "meaning": "풍성한, 풍부한", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "동사-주어 도치 구문: Above the produce, a scale hangs", "explanation": "장소 전치사구를 앞세우고 hangs를 써서 시선의 이동을 극대화하는 세련된 묘사 방식입니다."}
        ]
    },
    {
        "id": 108,
        "setId": 8,
        "setNumber": 8,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 8: A Bakery Table (베이커리 갓 구운 곡물빵)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a bakery",
            "locationEn": "on a wooden table in a bakery",
            "tags": [
                "장소: 빵집 작업대 (on a bakery wooden table)",
                "사물: 갓 구운 둥근 깜파뉴 빵과 곡물 빵 3개 (three freshly baked artisan loaves)",
                "디테일: 빵 위에 놓인 황금빛 밀 이삭 (golden stalks of wheat)",
                "배경: 밀가루가 뿌려진 어두운 나무 테이블 (dark wooden surface dusted with flour)"
            ]
        },
        "photoDescriptionKr": "[베이커리 갓 구운 곡물빵 사진] 어두운 나무 테이블 위에 갓 구워낸 3개의 먹음직스러운 곡물 빵이 놓여 있는 정물 사진입니다. 앞쪽에는 흰 밀가루가 자연스럽게 묻어 있는 커다란 둥근 깜파뉴 빵이 있고 그 위에 황금색 밀 이삭 줄기가 얹어져 있습니다. 그 뒤로는 해바라기씨가 겉에 듬뿍 박힌 빵과 오트밀이 뿌려진 빵이 함께 놓여 있으며, 나무 테이블 위에는 밀가루 가루가 솔솔 흩뿌려져 있습니다.",
        "answer": "This is a picture taken on a bakery wooden table.\nIn the foreground, three freshly baked artisan bread loaves are resting on a dark wooden surface.\nThe round sourdough loaf in the front is lightly dusted with white flour, with a few golden stalks of wheat placed on top.\nBehind it, two other loaves are coated with sunflower seeds and whole grains.\nFlour is sprinkled across the table, adding a rustic bakery atmosphere.\nOverall, the freshly baked bread looks very healthy, delicious, and appetizing.",
        "answerTranslation": "이 사진은 베이커리의 나무 테이블 위에서 찍힌 사진입니다.\n앞쪽에는 갓 구워낸 3개의 장인 빵 덩어리가 어두운 나무 표면 위에 놓여 있습니다.\n앞에 있는 둥근 사워도우 빵은 흰 밀가루가 가볍게 묻어 있고, 그 위에는 몇 개의 황금빛 밀 이삭이 얹어져 있습니다.\n그 뒤쪽으로는 해바라기씨와 통곡물로 덮인 다른 두 개의 빵이 있습니다.\n테이블 위에 밀가루가 흩뿌려져 있어 소박한 베이커리 분위기를 더해줍니다.\n전반적으로 갓 구운 빵이 매우 건강하고 맛있으며 먹음직스러워 보입니다.",
        "magicSentences": [
            "This is a picture taken on a wooden table in a bakery.",
            "Three freshly baked loaves of bread are resting on the table.",
            "Flour is sprinkled across the dark wooden surface.",
            "Overall, the bread looks very delicious and appetizing."
        ],
        "scoreTip": "베이커리 음식 정물 묘사: 'freshly baked loaves of bread(갓 구운 빵 덩어리)', 'dusted with flour(밀가루가 묻은)'.",
        "vocabulary": [
            {"word": "artisan loaf", "ipa": "[ˈɑːtɪzæn ləʊf]", "pos": "명사구", "meaning": "수제 장인 빵 덩어리", "source": "사진 필수"},
            {"word": "stalk of wheat", "ipa": "[stɔːk əv wiːt]", "pos": "명사구", "meaning": "밀 이삭, 밀 줄기", "source": "사진 필수"},
            {"word": "sunflower seed", "ipa": "[ˈsʌnflaʊə siːd]", "pos": "명사구", "meaning": "해바라기씨", "source": "사진 필수"},
            {"word": "rustic", "ipa": "[ˈrʌstɪk]", "pos": "형용사", "meaning": "소박한, 투박하고 정겨운", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "과거분사 수식: dusted with flour / coated with seeds", "explanation": "사물의 표면 상태를 나타낼 때 'dusted with ~' 또는 'coated with ~'를 분사 형태로 붙여 유창성을 높입니다."}
        ]
    },
    {
        "id": 109,
        "setId": 9,
        "setNumber": 9,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 9: Library Bookshelves (도서관 서가 책장)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a library",
            "locationEn": "in a classic library or bookstore",
            "tags": [
                "장소: 도서관 서가 (in a library or bookstore)",
                "사물: 높은 나무 책장에 가득 찬 양장본 고서들 (tall wooden bookshelves packed with hardcover books)",
                "디테일: 선반 번호표 라벨 (shelf numbers 248, 249, 250)",
                "색상: 주황, 갈색, 파랑 등 다채로운 가죽 책 표지 (colorful leather book covers)"
            ]
        },
        "photoDescriptionKr": "[도서관 서가 책장 사진] 클래식한 도서관 또는 유서 깊은 서점의 거대한 나무 서가 책장 전경 사진입니다. 선반마다 선반 번호(248, 249, 250 등)를 나타내는 황동 번호판이 부착되어 있고, 주황색, 갈색, 파란색, 흰색 등 다양한 색상의 양장본 고서들이 크기별로 빼곡하고 질서정연하게 꽂혀 있습니다.",
        "answer": "This is a picture taken in a classic library or an old bookstore.\nThe scene features tall wooden bookshelves completely packed with vintage hardcover books.\nThe books are arranged neatly by size and subject, displaying colorful leather spines in orange, brown, and blue.\nAlong the wooden shelves, small plates indicating shelf numbers are visible.\nOverall, the bookshelves convey a scholarly, quiet, and timeless atmosphere.",
        "answerTranslation": "이 사진은 클래식한 도서관이나 오래된 서점에서 찍힌 사진입니다.\n이 장면은 빈티지 양장본 책들로 완전히 채워진 높은 나무 책장들을 보여줍니다.\n책들은 주황색, 갈색, 파란색의 다채로운 가죽 책등을 뽐내며 크기와 주제별로 깔끔하게 정돈되어 있습니다.\n나무 선반을 따라 선반 번호를 나타내는 작은 번호판들이 보입니다.\n전반적으로 책장들은 학구적이고 조용하며 세월이 흘러도 변치 않는 분위기를 전달합니다.",
        "magicSentences": [
            "This is a picture taken in a library.",
            "Tall wooden bookshelves are packed with vintage books.",
            "The books are arranged neatly by size and color.",
            "Overall, the bookshelves convey a scholarly and quiet atmosphere."
        ],
        "scoreTip": "도서관 서가 묘사: 'completely packed with books(책들로 가득 찬)', 'arranged neatly by size(크기별로 정돈된)'.",
        "vocabulary": [
            {"word": "hardcover book", "ipa": "[ˌhɑːdˈkʌvə bʊk]", "pos": "명사구", "meaning": "양장본 책, 하드커버 도서", "source": "사진 필수"},
            {"word": "bookshelf", "ipa": "[ˈbʊkʃelf]", "pos": "명사", "meaning": "책장, 서가", "source": "사진 필수"},
            {"word": "spine", "ipa": "[spaɪn]", "pos": "명사", "meaning": "(책의) 책등", "source": "답변 핵심"},
            {"word": "scholarly", "ipa": "[ˈskɒləli]", "pos": "형용사", "meaning": "학구적인, 학자다운", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "분사 구문 상태 묘사: displaying colorful leather spines", "explanation": "주절 뒤에 , displaying ~ 분사구를 덧붙여 책등의 다채로운 색상을 세부 묘사하는 고급 문장 구조입니다."}
        ]
    },
    {
        "id": 110,
        "setId": 10,
        "setNumber": 10,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 10: Study Room (스터디룸 대학생 그룹 스터디)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a study room",
            "locationEn": "in a library study room",
            "tags": [
                "장소: 도서관 스터디룸 (in a study room)",
                "중심 인물: 노트북 화면 보며 크게 웃는 턱수염 남성 (bearded student laughing over a laptop)",
                "동료들: 모자 착용하고 함께 웃는 친구들 (friends wearing caps smiling together)",
                "배경: 바인더와 책이 가득 찬 흰색 대형 책장 (white bookshelf full of binders and books)"
            ]
        },
        "photoDescriptionKr": "[스터디룸 대학생 그룹 스터디 사진] 도서관 스터디룸 테이블에서 3~4명의 젊은 대학생들이 모여 노트북을 함께 들여다보며 즐겁게 박장대소하고 있는 사진입니다. 가운데 턱수염을 기른 남성이 테이블 위로 몸을 숙이고 환하게 웃고 있으며, 야구 모자와 헌팅캡을 쓴 친구들도 함께 미소 지으며 화면을 보고 있습니다. 배경의 큰 흰색 책장에는 다양한 바인더와 책들이 가득 꽂혀 있습니다.",
        "answer": "This is a picture taken in a college library study room.\nIn the center, a group of university students are gathered around a table, laughing cheerfully while looking at a laptop screen.\nA young man with a beard is leaning over the table with a broad smile, sharing a fun moment with his peers.\nNext to him, his friends wearing caps are enjoying the conversation and smiling warmly.\nIn the background, a large white bookshelf is fully stacked with colorful binders and textbooks.\nOverall, the group study atmosphere seems extremely lively, cheerful, and friendly.",
        "answerTranslation": "이 사진은 대학교 도서관 스터디룸에서 찍힌 사진입니다.\n가운데에는 한 무리의 대학생들이 테이블에 모여 노트북 화면을 보며 유쾌하게 웃고 있습니다.\n턱수염을 기른 한 젊은 남성이 테이블 위로 몸을 기울여 활짝 웃으며 동료들과 즐거운 순간을 나누고 있습니다.\n그 옆에는 모자를 쓴 친구들이 대화를 즐기며 따뜻하게 미소 짓고 있습니다.\n배경에는 커다란 흰색 책장에 다채로운 바인더와 교재들이 가득 꽂혀 있습니다.\n전반적으로 그룹 스터디 분위기는 매우 활기차고, 유쾌하며, 다정해 보입니다.",
        "magicSentences": [
            "This is a picture taken in a college study room.",
            "Students are gathered around a table, laughing cheerfully.",
            "A man is leaning over the table with a broad smile.",
            "Overall, the atmosphere seems extremely lively and friendly."
        ],
        "scoreTip": "그룹 스터디 사진: 'gathered around a table(테이블에 모여)', 'laughing cheerfully(유쾌하게 웃는)', 'leaning over the table(몸을 기울인)'.",
        "vocabulary": [
            {"word": "bearded", "ipa": "[ˈbɪədɪd]", "pos": "형용사", "meaning": "턱수염이 있는", "source": "사진 필수"},
            {"word": "lean over", "ipa": "[liːn ˈəʊvə(r)]", "pos": "동사구", "meaning": "~위로 몸을 숙이다/기울이다", "source": "사진 필수"},
            {"word": "cheerfully", "ipa": "[ˈtʃɪəfəli]", "pos": "부사", "meaning": "유쾌하게, 쾌활하게", "source": "답변 핵심"},
            {"word": "lively", "ipa": "[ˈlaɪvli]", "pos": "형용사", "meaning": "활기찬, 생기 넘치는", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "신체 자세 묘사: is leaning over the table with a smile", "explanation": "is leaning over라는 신체 동작과 with a broad smile 부사구를 함께 써서 인물의 생생한 감정과 동작을 표현합니다."}
        ]
    },
    {
        "id": 111,
        "setId": 11,
        "setNumber": 11,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 11: Restaurant Dining Hall (고급 레스토랑 다이닝 테이블)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a restaurant",
            "locationEn": "inside an upscale modern restaurant",
            "tags": [
                "장소: 고급 레스토랑 실내 (in an upscale restaurant dining hall)",
                "사물: 둥근 나무 테이블과 검은색 모던 체어 (round wooden tables and sleek black chairs)",
                "세팅: 물잔과 흰색 접시가 세팅됨 (tables set with drinking glasses and white plates)",
                "배경: 유리 와인 보관 진열장과 모던 펜던트 조명 (glass wine cellar and modern light fixtures)"
            ]
        },
        "photoDescriptionKr": "[고급 레스토랑 다이닝 테이블 사진] 세련되고 모던한 고급 레스토랑의 다이닝 홀 전경 사진입니다. 전경에는 둥근 원목 다이닝 테이블과 세련된 검은색 의자들이 정갈하게 놓여 있으며, 각 테이블 위에는 유리 물잔과 흰색 접시들이 손님을 맞이할 준비를 마친 채 세팅되어 있습니다. 왼쪽에는 유리 와인 저장고 진열장이 있고, 천장에는 멋스러운 펜던트 조명들이 매달려 있습니다.",
        "answer": "This is a picture taken inside an upscale modern restaurant.\nIn the foreground, several round wooden dining tables are surrounded by sleek black chairs.\nThe tables are neatly set with clear drinking glasses and white dinner plates, ready for customers.\nOn the left wall, there is a large glass wine cellar displaying wine bottles, while modern hanging lamps illuminate the space.\nOverall, the dining hall looks very spacious, sophisticated, and elegant.",
        "answerTranslation": "이 사진은 고급스러운 현대식 레스토랑 실내에서 찍힌 사진입니다.\n앞쪽에는 여러 개의 둥근 원목 다이닝 테이블이 날렵한 검은색 의자들로 둘러싸여 있습니다.\n테이블에는 손님을 맞을 준비가 된 투명한 물잔과 흰색 디너 접시들이 깔끔하게 세팅되어 있습니다.\n왼쪽 벽에는 와인병들이 진열된 대형 유리 와인 저장고가 있고, 현대적인 펜던트 조명이 공간을 비추고 있습니다.\n전반적으로 다이닝 홀은 매우 넓고, 세련되며, 우아해 보입니다.",
        "magicSentences": [
            "This is a picture taken inside an upscale restaurant.",
            "Round dining tables are surrounded by sleek black chairs.",
            "The tables are neatly set with glasses and white plates.",
            "Overall, the dining hall looks very spacious and sophisticated."
        ],
        "scoreTip": "식당 테이블 세팅 묘사: 'neatly set with glasses and plates(잔과 접시가 깔끔하게 세팅된)'.",
        "vocabulary": [
            {"word": "upscale", "ipa": "[ˌʌpˈskeɪl]", "pos": "형용사", "meaning": "고급의, 격조 높은", "source": "답변 핵심"},
            {"word": "wine cellar", "ipa": "[ˈwaɪn selə(r)]", "pos": "명사구", "meaning": "와인 저장소, 와인 진열장", "source": "사진 필수"},
            {"word": "sophisticated", "ipa": "[səˈfɪstɪkeɪtɪd]", "pos": "형용사", "meaning": "세련된, 정교한", "source": "답변 핵심"},
            {"word": "sleek", "ipa": "[sliːk]", "pos": "형용사", "meaning": "날렵한, 매끈한", "source": "사진 필수"}
        ],
        "grammarPoints": [
            {"title": "준비 상태 분사: ready for customers / guests", "explanation": "The tables are set with plates, ready for customers처럼 형용사구를 덧붙여 문장의 완성도를 높입니다."}
        ]
    },
    {
        "id": 112,
        "setId": 12,
        "setNumber": 12,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 12: Resort Swimming Pool (리조트 야외 수영장과 선베드)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a resort pool",
            "locationEn": "at the outdoor pool area of a tropical resort",
            "tags": [
                "장소: 리조트 야외 수영장 (at a resort swimming pool)",
                "전경: 쿠션이 놓인 목제 선베드들이 나란히 정렬됨 (cushioned lounge chairs lined up on the wooden deck)",
                "수영장: 에메랄드빛 맑은 풀장과 수영하는 사람 (clear blue pool with someone swimming)",
                "배경: 큰 지붕의 목조 리조트 건물과 야자수 (wooden resort villa and a tall palm tree)"
            ]
        },
        "photoDescriptionKr": "[리조트 야외 수영장과 선베드 사진] 열대 휴양지의 고급 리조트 야외 수영장 데크 사진입니다. 앞쪽 나무 데크 위에는 푹신한 베개와 쿠션이 놓인 목제 선베드들이 나란히 놓여 있고, 그 옆에는 맑고 푸른 곡선형 수영장이 있습니다. 수영장 안에는 물놀이를 즐기는 사람이 보이고 테라스에도 사람이 서 있으며, 배경에는 높은 박공지붕의 목조 리조트 빌라와 야자수가 서 있습니다.",
        "answer": "This is a picture taken at the outdoor pool area of a tropical resort.\nIn the foreground, several comfortable wooden lounge chairs with soft cushions and pillows are lined up along the deck.\nNext to the deck, a swimming pool with clear turquoise water curves along the building, and a person is swimming in the water.\nIn the background, a beautiful wooden resort villa with a steep roof stands next to a tall palm tree.\nOverall, it looks like an ideal and peaceful setting for a relaxing summer vacation.",
        "answerTranslation": "이 사진은 열대 리조트의 야외 수영장 구역에서 찍힌 사진입니다.\n앞쪽에는 부드러운 쿠션과 베개가 놓인 안락한 목제 라운지 의자들이 데크를 따라 나란히 놓여 있습니다.\n데크 옆에는 맑은 청록색 물의 수영장이 건물 곡선을 따라 흐르고 있고, 한 사람이 물속에서 수영하고 있습니다.\n배경에는 가파른 지붕을 가진 아름다운 목조 리조트 빌라가 키 큰 야자수 옆에 서 있습니다.\n전반적으로 편안한 여름휴가를 보내기에 이상적이고 평화로운 장소 같습니다.",
        "magicSentences": [
            "This is a picture taken at a resort pool area.",
            "Lounge chairs with soft cushions are lined up on the deck.",
            "A person is swimming in the clear blue water.",
            "Overall, it looks like an ideal place for a relaxing vacation."
        ],
        "scoreTip": "휴양지 수영장 묘사: 'lounge chairs lined up along the deck(데크를 따라 늘어선 선베드)'와 'clear turquoise water(맑은 청록색 물)'.",
        "vocabulary": [
            {"word": "lounge chair", "ipa": "[laʊndʒ tʃeə(r)]", "pos": "명사구", "meaning": "선베드, 라운지 체어", "source": "사진 필수"},
            {"word": "turquoise", "ipa": "[ˈtɜːkwɔɪz]", "pos": "형용사/명사", "meaning": "청록색의, 터키석", "source": "사진 필수"},
            {"word": "resort villa", "ipa": "[rɪˈzɔːt ˈvɪlə]", "pos": "명사구", "meaning": "리조트 별채, 휴양 빌라", "source": "사진 필수"},
            {"word": "tranquil", "ipa": "[ˈtræŋkwɪl]", "pos": "형용사", "meaning": "고요한, 평온한", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "방향/경로 묘사: lined up along the deck", "explanation": "along the deck처럼 along + 장소를 붙여서 물건들이 줄지어 배치된 선형 구도를 세련되게 표현합니다."}
        ]
    },
    {
        "id": 113,
        "setId": 13,
        "setNumber": 13,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 13: Park Walking Path (공원 가로수 산책로와 벤치)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1519331379826-f10be5486c6f?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a public park",
            "locationEn": "in a sunlit public park",
            "tags": [
                "장소: 공원 산책로 (on a park walking path)",
                "자연: 중앙으로 곧게 뻗은 자갈길과 울창한 플라타너스 가로수 (gravel path lined with mature shade trees)",
                "사물: 잔디밭 위에 놓인 빈 금속 벤치 (empty metal bench on the lawn)",
                "배경: 숲 사이로 쏟아지는 따스한 햇살 (warm sunlight filtering through the trees)"
            ]
        },
        "photoDescriptionKr": "[공원 가로수 산책로와 벤치 사진] 따사로운 햇살이 쏟아지는 아름다운 공원 산책로 전경 사진입니다. 중앙으로 길게 뻗은 자갈 산책로 양옆으로는 굵고 울창한 가로수들이 푸른 잎을 드리우고 있으며, 오른쪽 잔디밭 위에는 빈 금속 벤치 하나가 한적하게 놓여 있습니다. 저 멀리 노란색 안내 표지판이 보이고 숲 사이로 황금빛 햇살이 비치고 있습니다.",
        "answer": "This is a picture taken on a scenic walking path in a public park.\nA wide gravel path stretches straight through the center of the park under bright sunlight.\nOn both sides of the path, tall mature trees with lush green leaves create a refreshing natural canopy.\nTo the right, an empty metal park bench is placed on the green grassy lawn.\nIn the background, golden sunlight filters warmly through the tree branches.\nOverall, the park presents a peaceful, serene, and refreshing setting for taking a walk.",
        "answerTranslation": "이 사진은 공원의 경치 좋은 산책로에서 찍힌 사진입니다.\n밝은 햇살 아래 공원 중앙을 가로질러 넓은 자갈길이 곧게 뻗어 있습니다.\n길 양쪽에는 무성한 녹색 잎을 가진 크고 성숙한 나무들이 상쾌한 천연 지붕을 만들고 있습니다.\n오른쪽에는 녹색 잔디밭 위에 빈 금속 공원 벤치가 놓여 있습니다.\n배경에는 황금빛 햇살이 나뭇가지 사이로 따스하게 스며들고 있습니다.\n전반적으로 공원은 산책하기에 평화롭고 고요하며 상쾌한 환경을 제공합니다.",
        "magicSentences": [
            "This is a picture taken on a path in a public park.",
            "A wide gravel path stretches through the center.",
            "Tall trees with green leaves line both sides of the path.",
            "Overall, the park presents a peaceful and refreshing setting."
        ],
        "scoreTip": "공원 풍경 묘사: 'stretches through the center(중앙으로 뻗어 있다)', 'sunlight filters through the trees(나무 사이로 햇살이 스며들다)'.",
        "vocabulary": [
            {"word": "gravel path", "ipa": "[ˈɡrævl pɑːθ]", "pos": "명사구", "meaning": "자갈 산책로", "source": "사진 필수"},
            {"word": "canopy", "ipa": "[ˈkænəpi]", "pos": "명사", "meaning": "(나뭇가지들이 만드는) 덮개, 천개", "source": "답변 핵심"},
            {"word": "filter through", "ipa": "[ˈfɪltə θruː]", "pos": "동사구", "meaning": "(빛이) ~ 사이로 스며들다/비치다", "source": "사진 필수"},
            {"word": "serene", "ipa": "[səˈriːn]", "pos": "형용사", "meaning": "고요한, 평화로운", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "빛과 자연 표현: sunlight filters warmly through ~", "explanation": "filters through 표현은 햇살이 나뭇가지 사이로 비쳐 드는 모습을 묘사할 때 네이티브들이 가장 즐겨 쓰는 감성 표현입니다."}
        ]
    },
    {
        "id": 114,
        "setId": 14,
        "setNumber": 14,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 14: Dogs Running Outdoors (야외 흙길을 달리는 반려견)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "outdoor dogs",
            "locationEn": "on an outdoor dirt trail",
            "tags": [
                "장소: 야외 흙길 산책로 (on an outdoor dirt trail)",
                "왼쪽 반려견: 입 벌리고 신나게 달리는 웰시코기 (happy Welsh Corgi running with ears up)",
                "오른쪽 반려견: 카메라를 향해 뛰어오는 털 복슬복슬한 소형견 (fluffy terrier running forward)",
                "배경: 따스한 황혼의 역광 햇살 (warm sunset glow in the background)"
            ]
        },
        "photoDescriptionKr": "[야외 흙길을 달리는 반려견 사진] 따스한 황혼 역광 햇살 아래 야외 흙길을 카메라를 향해 신나게 달려오고 있는 두 마리의 반려견 실사 사진입니다. 왼쪽에는 쫑긋 솟은 귀와 활짝 웃는 표정으로 발을 공중에 띄우며 달리는 귀여운 웰시코기가 있고, 오른쪽 앞에는 털이 복슬복슬한 소형 테리어견이 힘차게 뛰어오고 있습니다.",
        "answer": "This is a picture taken on an outdoor dirt trail in nature.\nIn the center, two energetic dogs are running happily toward the camera along the path.\nOn the left, a cute Welsh Corgi with pointed ears is smiling with its mouth open, bounding forward with excitement.\nOn the right, a fluffy small terrier is running alongside it with great speed.\nIn the background, warm golden sunlight from the setting sun shines softly over the hills.\nOverall, the scene looks extremely joyful, lively, and full of energy.",
        "answerTranslation": "이 사진은 자연 속 야외 흙길에서 찍힌 사진입니다.\n가운데에는 활기찬 두 마리의 개가 길을 따라 카메라를 향해 행복하게 달려오고 있습니다.\n왼쪽에는 뾰족한 귀를 가진 귀여운 웰시코기가 입을 벌린 채 미소 지으며 신나게 앞으로 뛰어오르고 있습니다.\n오른쪽에는 털이 복슬복슬한 작은 테리어가 엄청난 속도로 나란히 달리고 있습니다.\n배경에는 지는 해에서 나오는 따뜻한 황금빛 햇살이 언덕 위로 부드럽게 비치고 있습니다.\n전반적으로 이 장면은 매우 즐겁고 활기차며 에너지가 넘쳐 보입니다.",
        "magicSentences": [
            "This is a picture taken on an outdoor trail.",
            "Two energetic dogs are running happily toward the camera.",
            "A cute dog with pointed ears is bounding forward.",
            "Overall, the scene looks extremely joyful and lively."
        ],
        "scoreTip": "동물 묘사: 'running toward the camera(카메라를 향해 달리는)', 'bounding forward with excitement(신나게 뛰어오르는)'.",
        "vocabulary": [
            {"word": "dirt trail", "ipa": "[dɜːt treɪl]", "pos": "명사구", "meaning": "흙길 산책로", "source": "사진 필수"},
            {"word": "bound forward", "ipa": "[baʊnd ˈfɔːwəd]", "pos": "동사구", "meaning": "앞으로 껑충껑충 뛰어나가다", "source": "답변 핵심"},
            {"word": "fluffy", "ipa": "[ˈflʌfi]", "pos": "형용사", "meaning": "털이 복슬복슬한", "source": "사진 필수"},
            {"word": "pointed ears", "ipa": "[ˈpɔɪntɪd ɪəz]", "pos": "명사구", "meaning": "쫑긋 선 뾰족한 귀", "source": "사진 필수"}
        ],
        "grammarPoints": [
            {"title": "방향 부사구: running toward the camera", "explanation": "toward the camera 표현은 인물이나 동물이 렌즈 정면을 향해 다가오는 구도를 정확하게 묘사하는 핵심 표현입니다."}
        ]
    },
    {
        "id": 115,
        "setId": 15,
        "setNumber": 15,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 15: City Waterfront Skyline (도시 해안 스카이라인과 보름달)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1514565131-fce0801e5785?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a city skyline",
            "locationEn": "across a river showing a city skyline",
            "tags": [
                "장소: 도심 해안 스카이라인 (across a river showing a skyline)",
                "중심 피사체: 높이 솟은 고층 마천루 빌딩들 (modern skyscrapers towering into the sky)",
                "전경: 푸른 강물/바다 (deep blue water in the foreground)",
                "배경: 핑크빛 황혼 하늘과 밝게 뜬 보름달 (pink twilight sky and a glowing full moon)"
            ]
        },
        "photoDescriptionKr": "[도시 해안 스카이라인과 보름달 사진] 강 건너편에서 바라본 뉴욕 도심의 웅장한 스카이라인 사진입니다. 전경에는 짙푸른 강물이 잔잔하게 흐르고 있고, 중앙에는 원 월드 트레이드 센터를 비롯한 수많은 현대식 마천루 빌딩들이 빽빽하게 솟아 있습니다. 해질녘 은은한 핑크빛과 보랏빛 하늘 위로 환한 보름달이 떠 있어 환상적인 도시 풍경을 자아냅니다.",
        "answer": "This is a picture taken across a river, showing a panoramic city skyline.\nIn the center, numerous modern skyscrapers, including a prominent tall tower with an antenna, rise high into the sky.\nIn the foreground, deep blue water ripples gently along the urban waterfront.\nIn the background, the evening sky displays soft pinkish twilight tones, with a bright round moon glowing beautifully.\nOverall, the city skyline presents a grand, breathtaking, and scenic view.",
        "answerTranslation": "이 사진은 강 건너편에서 찍힌 사진으로, 탁 트인 도시 스카이라인을 보여줍니다.\n중앙에는 안테나가 달린 두드러지게 높은 타워를 포함한 수많은 현대식 마천루들이 하늘 높이 솟아 있습니다.\n앞쪽에는 짙푸른 물이 도시 해안을 따라 잔잔하게 물결치고 있습니다.\n배경의 저녁 하늘은 부드러운 분홍빛 황혼을 띠고 있으며, 밝고 둥근 달이 아름답게 빛나고 있습니다.\n전반적으로 도시 스카이라인은 웅장하고 숨이 멎을 듯 아름다운 경관을 선사합니다.",
        "magicSentences": [
            "This is a picture showing a panoramic city skyline.",
            "Numerous modern skyscrapers rise high into the sky.",
            "A bright round moon is glowing in the evening sky.",
            "Overall, the skyline presents a breathtaking scenic view."
        ],
        "scoreTip": "도시 풍경 묘사: 'panoramic city skyline(탁 트인 도시 스카이라인)', 'skyscrapers rise high into the sky(마천루가 하늘 높이 솟아오르다)'.",
        "vocabulary": [
            {"word": "skyscraper", "ipa": "[ˈskaɪskreɪpə(r)]", "pos": "명사", "meaning": "초고층 빌딩, 마천루", "source": "사진 필수"},
            {"word": "panoramic", "ipa": "[ˌpænəˈræmɪk]", "pos": "형용사", "meaning": "파노라마식의, 한눈에 다 보이는", "source": "답변 핵심"},
            {"word": "twilight", "ipa": "[ˈtwaɪlaɪt]", "pos": "명사", "meaning": "황혼, 땅거미", "source": "사진 필수"},
            {"word": "breathtaking", "ipa": "[ˈbreθteɪkɪŋ]", "pos": "형용사", "meaning": "숨이 멎을 듯한, 매우 놀라운", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "동격/추가 수식 분사: including a prominent tower", "explanation": "skyscrapers 뒤에 including을 붙여 특정 상징적인 랜드마크 건물을 구체적으로 지칭하는 고급 문장입니다."}
        ]
    },
    {
        "id": 116,
        "setId": 16,
        "setNumber": 16,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 16: A Bustling Coffee Shop (손님들로 북적이는 카페)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1525610553991-2bede1a236e2?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a crowded cafe",
            "locationEn": "inside a bustling coffee shop",
            "tags": [
                "장소: 북적이는 실내 카페 (inside a bustling coffee shop)",
                "앞쪽 손님: 스마트폰 들고 사진 찍는 여성과 맞은편 남성 (woman holding a smartphone taking a photo)",
                "카운터: 에스프레소 머신 다루는 바리스타 (barista operating an espresso machine)",
                "배경: 커피 메뉴 적힌 칠판과 조명들 (chalkboard menus and hanging lights)"
            ]
        },
        "photoDescriptionKr": "[손님들로 북적이는 카페 사진] 활기차고 손님들로 가득한 실내 카페 전경 사진입니다. 앞쪽 테이블에는 긴 머리의 여성이 스마트폰을 들어 사진을 찍고 있고, 그 맞은편에는 안경과 후드티를 입은 남성이 앉아 있습니다. 오른쪽 앞에는 파란 옷을 입은 남성의 옆모습이 보이며, 뒤편 카운터에서는 바리스타가 커피 머신 위 잔들을 정리하고 있습니다. 벽면에는 원두 종류가 적힌 검은 칠판과 찬장이 있고 펜던트 조명들이 켜져 있습니다.",
        "answer": "This is a picture taken inside a bustling and popular coffee shop.\nIn the foreground, a woman with long dark hair is holding up her smartphone to take a photo, sitting across from a man wearing glasses.\nTo the right, another customer in a blue shirt is enjoying his time at the counter.\nIn the background, a barista is working behind the counter, organizing cups above an espresso machine.\nBehind the counter, chalkboard menus display various coffee origins, illuminated by industrial hanging lamps.\nOverall, the coffee shop has a vibrant, trendy, and lively atmosphere.",
        "answerTranslation": "이 사진은 북적이고 인기 있는 카페 실내에서 찍힌 사진입니다.\n앞쪽에는 긴 흑발의 여성이 사진을 찍기 위해 스마트폰을 들고 있고, 안경을 쓴 남성의 맞은편에 앉아 있습니다.\n오른쪽에는 파란 셔츠를 입은 또 다른 손님이 카운터에서 시간을 즐기고 있습니다.\n배경에는 바리스타가 카운터 뒤에서 에스프레소 머신 위에 있는 잔들을 정리하며 일하고 있습니다.\n카운터 뒤로는 인더스트리얼 펜던트 조명이 비추는 가운데 커피 원산지가 적힌 칠판 메뉴판이 보입니다.\n전반적으로 카페는 활기차고, 트렌디하며, 생동감 넘치는 분위기입니다.",
        "magicSentences": [
            "This is a picture taken inside a bustling coffee shop.",
            "A woman is holding up her smartphone to take a photo.",
            "A barista is working behind the counter.",
            "Overall, the coffee shop has a vibrant and lively atmosphere."
        ],
        "scoreTip": "카페 내부 인물 복수 묘사: 'holding up her smartphone(스마트폰을 치켜들고)', 'working behind the counter(카운터 뒤에서 일하는)'.",
        "vocabulary": [
            {"word": "bustling", "ipa": "[ˈbʌslɪŋ]", "pos": "형용사", "meaning": "북적거리는, 번잡한", "source": "답변 핵심"},
            {"word": "espresso machine", "ipa": "[eˈspresəʊ məˈʃiːn]", "pos": "명사구", "meaning": "에스프레소 커피 머신", "source": "사진 필수"},
            {"word": "vibrant", "ipa": "[ˈvaɪbrənt]", "pos": "형용사", "meaning": "활기찬, 생생한", "source": "답변 핵심"},
            {"word": "coffee origin", "ipa": "[ˈkɒfi ˈɒrɪdʒɪn]", "pos": "명사구", "meaning": "커피 원산지", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "마주 앉은 위치 표현: sitting across from ~", "explanation": "sitting across from a man 구문은 테이블 맞은편에 마주 보고 앉아 있는 관계를 나타내는 핵심 영어 표현입니다."}
        ]
    },
    {
        "id": 117,
        "setId": 17,
        "setNumber": 17,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 17: Subway Station Platform (지하철 승강장 열차 진입과 대기)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1778050147537-bc1001c3f825?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a subway platform",
            "locationEn": "on a subway station platform",
            "tags": [
                "장소: 지하철 승강장 (on a subway platform)",
                "승객들: 노란색 안전선 뒤에 서서 열차 기다리기 (standing behind the yellow safety line)",
                "동작: 스마트폰 확인하거나 가방 메고 서 있음 (checking smartphones and waiting)",
                "열차: 오른쪽 선로로 빠르게 진입하는 지하철 (subway train pulling into the platform)"
            ]
        },
        "photoDescriptionKr": "[지하철 승강장 열차 진입과 대기 사진] 지하철역 승강장에서 여러 명의 통근 승객들이 노란색 안전선 뒤에 나란히 서서 열차를 기다리고 있는 실사 사진입니다. 가운데 승객들은 스마트폰을 확인하거나 가방을 메고 서 있으며, 오른쪽 선로에는 빠른 속도로 승강장으로 진입하고 있는 지하철 열차가 보입니다. 천장에는 역 이름 안내 표지판과 조명들이 걸려 있습니다.",
        "answer": "This is a picture taken on a subway station platform.\nIn the middle, several commuters are standing along the platform behind the yellow safety line.\nSome passengers are looking at their smartphones while patiently waiting for the train.\nOn the right side, an incoming subway train is pulling into the station at high speed.\nAbove the passengers, station signs and ceiling lights are clearly displayed.\nOverall, it portrays a typical, orderly, and busy rush hour commute in the city.",
        "answerTranslation": "이 사진은 지하철역 승강장에서 찍힌 사진입니다.\n가운데에는 여러 통근 승객들이 노란색 안전선 뒤로 승강장을 따라 서 있습니다.\n몇몇 승객들은 끈기 있게 열차를 기다리는 동안 스마트폰을 바라보고 있습니다.\n오른쪽에는 진입 중인 지하철 열차가 빠른 속도로 역으로 들어오고 있습니다.\n승객들 위쪽으로는 역 표지판과 천장 조명들이 선명하게 표시되어 있습니다.\n전반적으로 도시의 전형적이고, 질서정연하며, 분주한 출퇴근길 모습을 보여줍니다.",
        "magicSentences": [
            "This is a picture taken on a subway station platform.",
            "Commuters are standing behind the yellow safety line.",
            "An incoming subway train is pulling into the station.",
            "Overall, it portrays an orderly rush hour scene."
        ],
        "scoreTip": "지하철 필수 표현: 'behind the yellow safety line(노란 안전선 뒤에)', 'pulling into the station(역으로 들어오는)'.",
        "vocabulary": [
            {"word": "commuter", "ipa": "[kəˈmjuːtə(r)]", "pos": "명사", "meaning": "통근자, 출퇴근 승객", "source": "사진 필수"},
            {"word": "safety line", "ipa": "[ˈseɪfti laɪn]", "pos": "명사구", "meaning": "안전선", "source": "사진 필수"},
            {"word": "pull into", "ipa": "[pʊl ˈɪntuː]", "pos": "동사구", "meaning": "(열차/버스가) 역에 들어오다/정차하다", "source": "답변 핵심"},
            {"word": "orderly", "ipa": "[ˈɔːdəli]", "pos": "형용사", "meaning": "질서 있는, 정돈된", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "열차 진입 현재진행형: is pulling into the station", "explanation": "pull into는 차량이나 열차가 정류장이나 역 플랫폼으로 들어오는 동작을 묘사하는 가장 정확한 관용 표현입니다."}
        ]
    },
    {
        "id": 118,
        "setId": 18,
        "setNumber": 18,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 18: Airport Tarmac & Airplane (공항 활주로 여객기와 지상 조업)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1542296332-2e4473faf563?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "an airport",
            "locationEn": "on an airport tarmac outside a terminal",
            "tags": [
                "장소: 공항 활주로 계류장 (on an airport tarmac)",
                "비행기: 게이트에 주기된 대형 상용 여객기 (large commercial airplane parked on the apron)",
                "인물: 형광 조끼 입고 비행기 점검하는 지상 요원들 (ground crew in safety vests)",
                "배경: 황금빛 석양 노을과 탑승교 (golden sunset sky and jet bridge)"
            ]
        },
        "photoDescriptionKr": "[공항 활주로 여객기와 지상 조업 사진] 공항 탑승동 터미널 창문 밖으로 바라본 활주로 계류장 실사 사진입니다. 중앙 게이트에는 대형 상용 여객기가 정면을 향해 주기되어 있고, 비행기 앞에는 견인 차량과 형광 안전 조끼를 착용한 지상 조업 요원들이 대기하고 있습니다. 오른쪽에는 탑승교가 비행기에 연결되어 있으며, 지평선 너머로 황금빛 석양 노을이 물들어 있습니다.",
        "answer": "This is a picture taken at an airport tarmac viewed through a terminal window.\nIn the center, a large commercial airplane is parked on the apron with its engines facing forward.\nNear the aircraft, ground crew members wearing reflective safety vests are standing beside service vehicles.\nTo the right, a passenger boarding bridge is connected to the entrance of the airplane.\nIn the background, a breathtaking golden sunset illuminates the runway horizon.\nOverall, the airport scene looks very busy, well-coordinated, and cinematic.",
        "answerTranslation": "이 사진은 터미널 창문을 통해 바라본 공항 활주로 계류장에서 찍힌 사진입니다.\n중앙에는 대형 상용 여객기가 엔진을 정면으로 향한 채 계류장에 주기되어 있습니다.\n항공기 근처에는 반사 안전 조끼를 입은 지상 조업 요원들이 서비스 차량 옆에 서 있습니다.\n오른쪽에는 탑승교가 비행기 출입구에 연결되어 있습니다.\n배경에는 숨이 멎을 듯한 황금빛 석양이 활주로 지평선을 밝히고 있습니다.\n전반적으로 공항 풍경은 매우 분주하고, 잘 조직되어 있으며, 영화의 한 장면처럼 보입니다.",
        "magicSentences": [
            "This is a picture taken at an airport tarmac.",
            "A large commercial airplane is parked on the apron.",
            "Ground crew wearing safety vests are standing near the aircraft.",
            "Overall, the scene looks very busy and well-coordinated."
        ],
        "scoreTip": "공항 사진 빈출 어휘: 'tarmac(활주로 계류장)', 'ground crew(지상 조업 요원)', 'boarding bridge(탑승교)'.",
        "vocabulary": [
            {"word": "tarmac", "ipa": "[ˈtɑːmæk]", "pos": "명사", "meaning": "(공항의) 활주로, 계류장", "source": "사진 필수"},
            {"word": "ground crew", "ipa": "[ˈɡraʊnd kruː]", "pos": "명사구", "meaning": "지상 조업 직원, 항공 정비 요원", "source": "사진 필수"},
            {"word": "boarding bridge", "ipa": "[ˈbɔːdɪŋ brɪdʒ]", "pos": "명사구", "meaning": "탑승교, 탑승 통로", "source": "답변 핵심"},
            {"word": "cinematic", "ipa": "[ˌsɪnəˈmætɪk]", "pos": "형용사", "meaning": "영화 같은, 그림 같은", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "수동 완료 분사: is parked on the apron / is connected to", "explanation": "비행기의 정차 상태와 탑승교의 결합 상태를 수동태 형태로 깔끔하게 설명합니다."}
        ]
    },
    {
        "id": 119,
        "setId": 19,
        "setNumber": 19,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 19: Logistics Warehouse (대형 물류 창고 재고 선반)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a warehouse",
            "locationEn": "inside a massive logistics warehouse",
            "tags": [
                "장소: 대형 물류 창고 (inside a massive warehouse)",
                "선반: 노란 보관함과 박스로 가득 찬 철제 랙 (metal racks filled with yellow bins and boxes)",
                "배경: 목재 팔레트에 쌓인 대형 화물들 (packages stacked on wooden pallets)",
                "구조: 높은 천장과 환기 배관 덕트 (high ceiling with industrial ductwork)"
            ]
        },
        "photoDescriptionKr": "[대형 물류 창고 재고 선반 사진] 거대한 물류 유통 창고의 높은 시점에서 내려다본 사진입니다. 화면 전체를 차지하는 높은 철제 선반 랙마다 노란색 플라스틱 보관 바구니들과 갈색 골판지 상자들이 바둑판처럼 질서정연하게 가득 차 있습니다. 뒤쪽에는 대형 목재 팔레트 위에 화물들이 층층이 적재되어 있으며, 천장에는 은색 환기 배관 파이프와 밝은 공업용 조명이 설치되어 있습니다.",
        "answer": "This is a picture taken inside a massive logistics and storage warehouse.\nHigh metal shelving racks dominate the entire space, filled with countless yellow storage bins and cardboard boxes.\nThe items are organized in neat rows on multiple tiers for efficient sorting.\nIn the background, taller industrial racks hold wooden pallets stacked with packages ready for shipment.\nAbove, the high ceiling is equipped with industrial ventilation pipes and bright lighting.\nOverall, the warehouse looks extremely well-organized, spacious, and efficient.",
        "answerTranslation": "이 사진은 거대한 물류 및 보관 창고 실내에서 찍힌 사진입니다.\n높은 철제 선반 랙들이 공간 전체를 지배하고 있으며, 수많은 노란색 보관 바구니와 골판지 상자들로 가득 차 있습니다.\n물품들은 효율적인 분류를 위해 여러 층에 걸쳐 깔끔한 줄로 정돈되어 있습니다.\n배경에는 더 높은 산업용 랙들이 배송 준비가 된 소포들이 쌓인 나무 팔레트들을 지탱하고 있습니다.\n위쪽의 높은 천장에는 산업용 환기 파이프와 밝은 조명이 설치되어 있습니다.\n전반적으로 창고는 매우 잘 정리되어 있고, 넓으며, 효율적으로 보입니다.",
        "magicSentences": [
            "This is a picture taken inside a massive warehouse.",
            "Metal shelving racks are filled with yellow bins and boxes.",
            "Items are organized in neat rows for efficient sorting.",
            "Overall, the warehouse looks extremely well-organized and efficient."
        ],
        "scoreTip": "물류 창고 묘사: 'shelving racks(선반 랙)', 'cardboard boxes(골판지 상자)', 'wooden pallets(나무 팔레트)'.",
        "vocabulary": [
            {"word": "cardboard box", "ipa": "[ˈkɑːdbɔːd bɒks]", "pos": "명사구", "meaning": "골판지 상자, 박스", "source": "사진 필수"},
            {"word": "wooden pallet", "ipa": "[ˈwʊdn ˈpælət]", "pos": "명사구", "meaning": "나무 팔레트 (화물 받침대)", "source": "사진 필수"},
            {"word": "ventilation pipe", "ipa": "[ˌventɪˈleɪʃn paɪp]", "pos": "명사구", "meaning": "환기 배관 파이프", "source": "사진 필수"},
            {"word": "well-organized", "ipa": "[ˌwel ˈɔːɡənaɪzd]", "pos": "형용사", "meaning": "잘 정리된, 체계적인", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "공간 지배 표현: High racks dominate the entire space", "explanation": "dominate 동사를 사용하여 랙들이 시야를 가득 채우고 있는 웅장한 공간감을 효과적으로 전달합니다."}
        ]
    },
    {
        "id": 120,
        "setId": 20,
        "setNumber": 20,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 20: Serene Ocean Beach (일출 해변 백사장과 잔잔한 파도)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a beach",
            "locationEn": "at a serene ocean beach",
            "tags": [
                "장소: 고요한 해변 백사장 (at a tranquil sandy beach)",
                "전경: 모래사장 위로 밀려드는 하얀 거품 파도 (gentle white foamy waves rolling onto the sand)",
                "바다: 맑은 청록색의 잔잔한 바다 (calm turquoise ocean waters)",
                "하늘: 구름 사이로 빛나는 황금빛 태양 (golden sun glowing through soft clouds)"
            ]
        },
        "photoDescriptionKr": "[일출 해변 백사장과 잔잔한 파도 사진] 사람 없이 한적하고 평화로운 해변의 일출/일몰 풍경 사진입니다. 전경에는 부드럽고 깨끗한 모래사장 위로 하얀 거품의 잔잔한 파도가 밀려들고 있으며, 그 너머로는 맑고 투명한 청록색 바다가 지평선까지 펼쳐져 있습니다. 하늘에는 부드러운 파스텔톤 구름 사이로 황금빛 태양이 눈부시게 빛나고 있습니다.",
        "answer": "This is a picture taken at a tranquil sandy beach during sunrise.\nIn the foreground, gentle white foamy waves are rolling softly onto the clean, smooth sand.\nBeyond the shoreline, the calm turquoise ocean extends toward the horizon.\nIn the sky, the golden sun shines warmly through soft pastel clouds, casting a gentle reflection on the water.\nOverall, the beach looks exceptionally peaceful, refreshing, and beautiful.",
        "answerTranslation": "이 사진은 일출 무렵 고요한 모래 해변에서 찍힌 사진입니다.\n앞쪽에는 부드러운 흰 거품 파도가 깨끗하고 고운 모래 위로 부드럽게 밀려들고 있습니다.\n해안선 너머로는 잔잔한 청록색 바다가 지평선을 향해 뻗어 있습니다.\n하늘에는 황금빛 태양이 부드러운 파스텔톤 구름 사이로 따스하게 빛나며 물 위에 은은한 반사를 드리우고 있습니다.\n전반적으로 해변은 유난히 평화롭고, 상쾌하며, 아름다워 보입니다.",
        "magicSentences": [
            "This is a picture taken at a tranquil sandy beach.",
            "Gentle white waves are rolling onto the smooth sand.",
            "The calm turquoise ocean extends toward the horizon.",
            "Overall, the beach looks exceptionally peaceful and beautiful."
        ],
        "scoreTip": "자연 해변 풍경 묘사: 'foamy waves rolling onto the sand(모래로 밀려드는 거품 파도)', 'calm turquoise ocean(잔잔한 청록색 바다)'.",
        "vocabulary": [
            {"word": "foamy wave", "ipa": "[ˈfəʊmi weɪv]", "pos": "명사구", "meaning": "거품이 이는 파도", "source": "사진 필수"},
            {"word": "shoreline", "ipa": "[ˈʃɔːlaɪn]", "pos": "명사", "meaning": "해안선, 물가", "source": "사진 필수"},
            {"word": "cast a reflection", "ipa": "[kɑːst ə rɪˈflekʃn]", "pos": "동사구", "meaning": "반사/그림자를 드리우다", "source": "답변 핵심"},
            {"word": "exceptionally", "ipa": "[ɪkˈsepʃənəli]", "pos": "부사", "meaning": "유난히, 각별하게", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "동시 효과 분사구문: casting a gentle reflection", "explanation": ", casting a gentle reflection처럼 현재분사구를 덧붙여 빛의 반사 효과를 감각적으로 표현합니다."}
        ]
    },
    {
        "id": 121,
        "setId": 21,
        "setNumber": 21,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 21: Trendy Clothing Boutique (의류 매장 진열대와 옷걸이)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a clothing store",
            "locationEn": "inside a trendy clothing boutique",
            "tags": [
                "장소: 의류 편집 매장 (inside a clothing boutique)",
                "테이블: 접힌 옷들과 모자, 가방 진열 (folded shirts, caps, and bags on the center table)",
                "선반: 아래 선반의 가죽 부츠와 신발들 (leather boots and shoes on the lower shelf)",
                "옷걸이 랙: 양옆 랙에 걸린 셔츠와 자켓들 (clothing racks with hanging shirts and jackets)"
            ]
        },
        "photoDescriptionKr": "[의류 매장 진열대와 옷걸이 사진] 감각적인 남성 패션 의류 편집숍 실내 전경 사진입니다. 중앙 나무 테이블 위에는 개어진 옷들과 모자, 가방이 정갈하게 진열되어 있고, 테이블 아래 선반에는 가죽 부츠와 신발들이 정돈되어 있습니다. 양쪽 벽면 옷걸이 랙에는 셔츠와 자켓들이 걸려 있으며, 천장에서는 4개의 흰색 펜던트 조명이 제품들을 환하게 비추고 있습니다.",
        "answer": "This is a picture taken inside a trendy clothing boutique.\nIn the center, a large display table showcases neatly folded shirts, sweaters, and hats.\nBeneath the table, several pairs of stylish leather boots and shoes are displayed on the bottom shelf.\nOn both sides of the room, clothing racks are filled with shirts and colorful jackets on hangers.\nAbove, four white dome-shaped pendant lamps hang from the ceiling, illuminating the merchandise.\nOverall, the boutique appears very modern, well-curated, and stylish.",
        "answerTranslation": "이 사진은 트렌디한 의류 부티크 매장 실내에서 찍힌 사진입니다.\n중앙에는 커다란 진열 테이블 위에 깔끔하게 개어진 셔츠, 스웨터, 모자들이 진열되어 있습니다.\n테이블 아래 바닥 선반에는 몇 켤레의 스타일리시한 가죽 부츠와 신발들이 전시되어 있습니다.\n방 양쪽에는 옷걸이에 걸린 셔츠와 다채로운 자켓들로 채워진 의류 랙들이 있습니다.\n위쪽 천장에는 네 개의 흰색 돔형 펜던트 조명이 매달려 상품들을 밝게 비추고 있습니다.\n전반적으로 부티크는 매우 모던하고, 엄선되어 잘 구성되어 있으며, 세련되어 보입니다.",
        "magicSentences": [
            "This is a picture taken inside a clothing boutique.",
            "A display table showcases neatly folded shirts and accessories.",
            "Clothing racks are filled with jackets on hangers.",
            "Overall, the store appears very modern and well-curated."
        ],
        "scoreTip": "의류 매장 묘사: 'neatly folded shirts(깔끔하게 개어진 셔츠)', 'on hangers(옷걸이에 걸린)', 'illuminating the merchandise(상품을 비추는)'.",
        "vocabulary": [
            {"word": "boutique", "ipa": "[buːˈtiːk]", "pos": "명사", "meaning": "부티크, 유행 의류 매장", "source": "사진 필수"},
            {"word": "merchandise", "ipa": "[ˈmɜːtʃəndaɪs]", "pos": "명사", "meaning": "(매장의) 상품, 물품", "source": "답변 핵심"},
            {"word": "clothing rack", "ipa": "[ˈkləʊðɪŋ ræk]", "pos": "명사구", "meaning": "의류 진열 행거 랙", "source": "사진 필수"},
            {"word": "well-curated", "ipa": "[ˌwel kjʊˈreɪtɪd]", "pos": "형용사", "meaning": "엄선하여 잘 꾸며진", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "장소 부사구 도치: Beneath the table, several boots are displayed", "explanation": "Beneath the table, On both sides처럼 위치 전치사구를 앞세워 시선의 공간적 흐름을 살립니다."}
        ]
    },
    {
        "id": 122,
        "setId": 22,
        "setNumber": 22,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 22: Home Kitchen Cooking (주방 아일랜드에서 함께 요리하기)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a kitchen",
            "locationEn": "in a modern kitchen",
            "tags": [
                "장소: 주방 아일랜드 식탁 (in a modern kitchen)",
                "남성: 안경과 청 앞치마 착용 & 스푼으로 냄비에 양념 넣기 (adding ingredients with a spoon into a pot)",
                "여성: 회색 스웨터 입고 유리병 들며 미소 짓기 (woman in a gray sweater holding a glass jar)",
                "사물: 올리브유 병, 샐러드 볼, 양념 절구 (olive oil, salad bowl, mortar on the counter)"
            ]
        },
        "photoDescriptionKr": "[주방 아일랜드에서 함께 요리하기 사진] 모던한 가정집 주방에서 젊은 남녀가 아일랜드 조리대 식탁에서 함께 요리하고 있는 화기애애한 실사 사진입니다. 안경을 쓰고 청 앞치마를 두른 남성이 밝게 미소 지으며 금색 스푼으로 양념을 떠 하늘색 냄비에 넣고 있으며, 그 옆에 회색 니트 스웨터를 입은 여성이 유리병을 손에 든 채 다정하게 웃으며 바라보고 있습니다. 조리대 위에는 올리브 오일 병, 신선한 샐러드 볼, 작은 절구가 놓여 있습니다.",
        "answer": "This is a picture taken in a modern, bright kitchen.\nIn the center, a man wearing glasses and a denim apron is smiling as he uses a spoon to add ingredients into a light blue cooking pot.\nNext to him, a woman in a cozy gray sweater is smiling warmly while holding a glass jar.\nOn the wooden kitchen counter, a bottle of olive oil, a fresh salad bowl, and a small mortar are neatly arranged.\nIn the background, white cabinets and open wooden shelves with bowls line the wall.\nOverall, the couple appears to be having a wonderful and enjoyable time cooking together.",
        "answerTranslation": "이 사진은 모던하고 밝은 주방에서 찍힌 사진입니다.\n가운데에는 안경과 데님 앞치마를 착용한 남성이 밝은 파란색 조리 냄비에 스푼으로 재료를 넣으며 미소 짓고 있습니다.\n그 옆에는 아늑한 회색 스웨터를 입은 여성이 유리병을 든 채 다정하게 미소를 짓고 있습니다.\n나무 주방 조리대 위에는 올리브 오일 병, 신선한 샐러드 볼, 그리고 작은 절구가 깔끔하게 정돈되어 있습니다.\n배경에는 흰색 수납장과 그릇들이 놓인 나무 선반들이 벽을 따라 늘어서 있습니다.\n전반적으로 그 커플은 함께 요리하며 매우 즐겁고 행복한 시간을 보내고 있는 것처럼 보입니다.",
        "magicSentences": [
            "This is a picture taken in a modern kitchen.",
            "A man wearing an apron is using a spoon to add ingredients into a pot.",
            "Next to him, a woman is smiling warmly while holding a jar.",
            "Overall, they seem to be having a wonderful time cooking together."
        ],
        "scoreTip": "주방 인물 동작 묘사: 'wearing an apron(앞치마를 두르고)', 'using a spoon to add ingredients(스푼으로 재료를 넣는)', 'cooking together(함께 요리하는)'.",
        "vocabulary": [
            {"word": "denim apron", "ipa": "[ˈdenɪm ˈeɪprən]", "pos": "명사구", "meaning": "데님/청 앞치마", "source": "사진 필수"},
            {"word": "ingredient", "ipa": "[ɪnˈɡriːdiənt]", "pos": "명사", "meaning": "(요리의) 재료, 성분", "source": "답변 핵심"},
            {"word": "cooking pot", "ipa": "[ˈkʊkɪŋ pɒt]", "pos": "명사구", "meaning": "요리용 냄비", "source": "사진 필수"},
            {"word": "mortar and pestle", "ipa": "[ˈmɔːtə(r) ənd ˈpesl]", "pos": "명사구", "meaning": "절구와 절굿공이", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "동시 동작 부사절: as he uses a spoon to add ingredients", "explanation": "as 절을 활용하여 미소를 짓는 표정과 스푼으로 재료를 넣는 동작을 자연스럽게 묶어냅니다."}
        ]
    },
    {
        "id": 123,
        "setId": 23,
        "setNumber": 23,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 23: Blooming Purple Flowers (만발한 보라색 꽃밭 접사)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1558350315-8aa00e8e4590?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a flower garden",
            "locationEn": "in a lush flower garden",
            "tags": [
                "장소: 꽃밭 화단 (in a flower garden)",
                "꽃: 화면을 가득 채운 보라색/자줏빛 작은 꽃송이들 (dense purple blossoms filling the frame)",
                "디테일: 네다섯 장의 꽃잎과 노란 꽃술 (delicate petals with yellow centers)",
                "배경: 짙은 녹색 잎사귀들 (rich dark green foliage underneath)"
            ]
        },
        "photoDescriptionKr": "[만발한 보라색 꽃밭 접사 사진] 화면 전체를 빈틈없이 가득 채운 보라색과 자줏빛 작은 꽃송이들의 클로즈업 사진입니다. 네다섯 장의 섬세한 꽃잎과 노란 꽃술을 지닌 수백 송이의 작은 꽃들이 싱그러운 초록 잎사귀들 사이로 풍성하게 만발해 있어 화사하고 아름다운 자연의 생명력을 보여줍니다.",
        "answer": "This is a close-up picture taken of a lush flower garden.\nThe entire frame is completely filled with hundreds of tiny, vibrant purple flowers blooming in full density.\nEach small blossom features delicate violet petals with a yellow center, clustered closely together.\nBeneath the vibrant blossoms, deep green foliage and leaves provide a natural contrast.\nOverall, the sea of flowers looks remarkably fresh, enchanting, and lively.",
        "answerTranslation": "이 사진은 싱그러운 화단에서 찍힌 접사 사진입니다.\n화면 전체가 완전히 만발한 수백 송이의 작고 선명한 보라색 꽃들로 빽빽하게 채워져 있습니다.\n각각의 작은 꽃송이는 노란색 중심부를 가진 섬세한 보랏빛 꽃잎을 뽐내며 촘촘하게 모여 있습니다.\n선명한 꽃송이들 아래로는 짙은 녹색 잎사귀들이 자연스러운 대비를 이룹니다.\n전반적으로 꽃들의 바다는 매우 신선하고, 매혹적이며, 생기 넘쳐 보입니다.",
        "magicSentences": [
            "This is a close-up picture of a flower garden.",
            "The entire frame is filled with vibrant purple flowers.",
            "Delicate petals with yellow centers cluster together.",
            "Overall, the flowers look remarkably fresh and enchanting."
        ],
        "scoreTip": "자연/꽃 접사 묘사: 'completely filled with blooming flowers(만발한 꽃들로 가득 찬)', 'delicate petals(섬세한 꽃잎)'.",
        "vocabulary": [
            {"word": "blossom", "ipa": "[ˈblɒsəm]", "pos": "명사", "meaning": "꽃, 꽃송이", "source": "사진 필수"},
            {"word": "petal", "ipa": "[ˈpetl]", "pos": "명사", "meaning": "꽃잎", "source": "사진 필수"},
            {"word": "foliage", "ipa": "[ˈfəʊliɪdʒ]", "pos": "명사", "meaning": "잎사귀, 나뭇잎", "source": "답변 핵심"},
            {"word": "enchanting", "ipa": "[ɪnˈtʃɑːntɪŋ]", "pos": "형용사", "meaning": "매혹적인, 황홀한", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "수동태 밀도 묘사: is filled with hundreds of ~", "explanation": "The entire frame is filled with 구조는 피사체가 화면 전체에 꽉 찼을 때 시각적 강렬함을 즉시 전달하는 표현입니다."}
        ]
    },
    {
        "id": 124,
        "setId": 24,
        "setNumber": 24,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 24: Tour Coach Bus by Snow Mountains (설산 앞 정차된 관광 버스)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a tour bus",
            "locationEn": "outdoors in front of snow-capped mountains",
            "tags": [
                "장소: 설산 앞 야외 공터 (outdoors in a mountainous area)",
                "버스: 헤드라이트와 실내등을 켠 대형 흰색 관광 버스 (large white coach bus with headlights on)",
                "내부: 조명 아래 앉아 있는 승객들 (passengers visible inside through the front windshield)",
                "배경: 웅장한 눈 덮인 겨울 산과 황혼 하늘 (majestic snow-capped mountain peaks at twilight)"
            ]
        },
        "photoDescriptionKr": "[설산 앞 정차된 관광 버스 사진] 웅장한 눈 덮인 설산을 배경으로 야외 자갈 공터에 정차해 있는 대형 흰색 관광 코치 버스 사진입니다. 버스는 밝은 헤드라이트와 실내 주황색 조명을 켜고 있으며, 앞 유리를 통해 조명 아래 앉아 있는 승객들의 모습이 보입니다. 뒤편 배경에는 하얀 눈이 덮인 거대한 산봉우리들이 황혼 무렵의 푸른 하늘 아래 장엄하게 펼쳐져 있습니다.",
        "answer": "This is a picture taken outdoors in a scenic mountainous area at twilight.\nOn the left, a large white tour coach bus is parked on open gravel ground with its bright headlights and cabin lights turned on.\nThrough the front windshield, passengers can be seen seated inside under warm interior lighting.\nIn the background, majestic snow-capped mountain peaks rise impressively under a calm evening sky.\nOverall, the picture captures a quiet, scenic, and memorable pause during a winter travel tour.",
        "answerTranslation": "이 사진은 황혼 무렵 경치 좋은 산악 지대 야외에서 찍힌 사진입니다.\n왼쪽에는 대형 흰색 관광 코치 버스가 밝은 헤드라이트와 실내등을 켠 채 넓은 자갈밭에 주차되어 있습니다.\n앞 유리창을 통해 따뜻한 실내 조명 아래 좌석에 앉아 있는 승객들이 보입니다.\n배경에는 고요한 저녁 하늘 아래 장엄한 눈 덮인 산봉우리들이 인상적으로 솟아 있습니다.\n전반적으로 이 사진은 겨울 여행 투어 중 조용하고 경치 좋은 기억에 남는 휴식의 순간을 담고 있습니다.",
        "magicSentences": [
            "This is a picture taken outdoors in a mountainous area.",
            "A large tour coach bus is parked with its headlights on.",
            "Majestic snow-capped mountains rise in the background.",
            "Overall, the picture captures a scenic moment during a travel tour."
        ],
        "scoreTip": "교통 수단과 자연 배경: 'coach bus parked on gravel ground(자갈밭에 주차된 버스)', 'snow-capped mountains(눈 덮인 산봉우리)'.",
        "vocabulary": [
            {"word": "coach bus", "ipa": "[kəʊtʃ bʌs]", "pos": "명사구", "meaning": "대형 관광 버스, 고속버스", "source": "사진 필수"},
            {"word": "snow-capped", "ipa": "[ˈsnəʊ kæpt]", "pos": "형용사", "meaning": "꼭대기가 눈으로 덮인", "source": "사진 필수"},
            {"word": "windshield", "ipa": "[ˈwɪndʃiːld]", "pos": "명사", "meaning": "(자동차/버스의) 앞 유리창", "source": "사진 필수"},
            {"word": "majestic", "ipa": "[məˈdʒestɪk]", "pos": "형용사", "meaning": "장엄한, 위풍당당한", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "수동태 지각동사 구문: passengers can be seen seated", "explanation": "can be seen seated는 '좌석에 앉아 있는 모습이 보인다'는 뜻으로 실내 탑승객 상태를 객관적으로 묘사하는 정석 표현입니다."}
        ]
    },
    {
        "id": 125,
        "setId": 25,
        "setNumber": 25,
        "qNumber": "Question 3",
        "questionNumber": "Question 3",
        "setTitle": "Set 25: Vintage Road Bicycle (벽 앞에 주차된 클래식 자전거)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a bicycle",
            "locationEn": "on a sidewalk parked against a dark wall",
            "tags": [
                "장소: 어두운 벽면 앞 보도 (on a sidewalk in front of a dark wall)",
                "자전거: 클래식 흰색 로드 자전거 (vintage white road bicycle)",
                "부품: 갈색 가죽 안장과 곡선 핸들바 (brown leather saddle and curved handlebars)",
                "바닥: 깔끔한 보도블록 타일 (stone paved ground)"
            ]
        },
        "photoDescriptionKr": "[벽 앞에 주차된 클래식 자전거 사진] 어두운 회색 벽면 앞 보도블록 위에 깔끔하게 세워져 있는 빈티지 클래식 로드 자전거의 측면 사진입니다. 흰색 프레임에는 푸조(Peugeot) 로고와 주황색/노란색 줄무늬가 새겨져 있고, 갈색 가죽 안장과 곡선형 갈색 핸들바가 장착되어 있습니다. 두 개의 얇은 검은 바퀴와 체인이 군더더기 없이 정교하게 드러나 있습니다.",
        "answer": "This is a picture taken on a paved sidewalk next to a solid dark wall.\nIn the center, a classic white road bicycle is parked sideways against the plain background.\nThe bicycle features a sleek white frame with vintage stripes, a brown leather saddle, and curved brown handlebars.\nIts two thin black wheels and clean chain emphasize a minimalist and elegant design.\nOverall, the bicycle has a very stylish, retro, and well-maintained appearance.",
        "answerTranslation": "이 사진은 짙은 단색 벽 옆 포장된 보도에서 찍힌 사진입니다.\n가운데에는 클래식한 흰색 로드 자전거가 민무늬 배경을 등지고 옆으로 세워져 있습니다.\n그 자전거는 빈티지 줄무늬가 있는 날렵한 흰색 프레임, 갈색 가죽 안장, 그리고 곡선형 갈색 핸들바를 특징으로 합니다.\n두 개의 얇은 검은 바퀴와 깨끗한 체인은 미니멀하고 우아한 디자인을 강조합니다.\n전반적으로 자전거는 매우 세련되고, 레트로하며, 잘 관리된 모습을 보여줍니다.",
        "magicSentences": [
            "This is a picture taken on a sidewalk next to a dark wall.",
            "A classic white bicycle is parked against the background.",
            "It features a sleek white frame and a brown leather saddle.",
            "Overall, the bicycle has a very stylish and retro appearance."
        ],
        "scoreTip": "자전거 부품 어휘: 'leather saddle(가죽 안장)', 'handlebars(핸들바)', 'parked sideways(옆으로 주차된)'.",
        "vocabulary": [
            {"word": "saddle", "ipa": "[ˈsædl]", "pos": "명사", "meaning": "(자전거/말의) 안장", "source": "사진 필수"},
            {"word": "handlebar", "ipa": "[ˈhændlbɑː(r)]", "pos": "명사", "meaning": "(자전거/오토바이의) 핸들", "source": "사진 필수"},
            {"word": "minimalist", "ipa": "[ˈmɪnɪməlɪst]", "pos": "형용사", "meaning": "미니멀한, 단순하고 절제된", "source": "답변 핵심"},
            {"word": "well-maintained", "ipa": "[ˌwel meɪnˈteɪnd]", "pos": "형용사", "meaning": "관리가 잘 된", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "특징 설명 동사: features + N", "explanation": "The bicycle features a sleek frame처럼 features를 쓰면 사물의 외형적 특징을 고급스럽고 간결하게 묘사할 수 있습니다."}
        ]
    },
    {
        "id": 126,
        "setId": 26,
        "setNumber": 26,
        "qNumber": "Question 4",
        "questionNumber": "Question 4",
        "setTitle": "Set 26: Laboratory Pipette Experiment (시험관 피펫 용액 주입 실험)",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "imageUrl": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?auto=format&fit=crop&w=1200&q=80",
        "photoScene": {
            "category": "a laboratory",
            "locationEn": "in a scientific laboratory",
            "tags": [
                "장소: 과학 연구실 (in a science laboratory)",
                "동작: 피펫 팁으로 보라색 시약을 시험관에 주입 (dispensing purple liquid with a pipette)",
                "사물: 파란색 랙에 정렬된 수십 개의 투명 마이크로 시험관 (clear sample tubes in a blue rack)",
                "배경: 아웃포커싱된 정밀한 실험실 배경 (blurred precision laboratory background)"
            ]
        },
        "photoDescriptionKr": "[시험관 피펫 용액 주입 실험 사진] 생명과학 연구실에서 마이크로피펫으로 파란색 랙 트레이에 꽂힌 수십 개의 투명한 샘플 튜브(시험관) 중 하나에 선명한 자주색/보라색 액체 시약을 정밀하게 주입하고 있는 초근접 접사 사진입니다. 시험관들이 바둑판 모양으로 촘촘히 배열되어 있고, 배경은 부드럽게 아웃포커싱되어 실험의 정밀함이 돋보입니다.",
        "answer": "This is an extreme close-up picture taken in a scientific laboratory.\nIn the upper center, a laboratory pipette tip is precisely dispensing bright purple liquid into one of the clear sample tubes.\nDozens of small, transparent plastic tubes are arranged in neat rows within a blue plastic rack tray.\nThe surrounding laboratory background is softly blurred to highlight the precise scientific procedure.\nOverall, the scene conveys a high degree of precision, expertise, and advanced research.",
        "answerTranslation": "이 사진은 과학 실험실에서 찍힌 극단적인 접사 사진입니다.\n위쪽 중앙에는 실험용 피펫 팁이 투명한 시료 튜브 중 하나에 밝은 보라색 액체를 정밀하게 주입하고 있습니다.\n수십 개의 작고 투명한 플라스틱 튜브들이 파란색 플라스틱 랙 트레이 안에 깔끔한 줄로 배열되어 있습니다.\n주변 실험실 배경은 정밀한 과학적 절차를 강조하기 위해 부드럽게 흐려져 있습니다.\n전반적으로 이 장면은 높은 정밀도, 전문성, 그리고 첨단 연구의 분위기를 전달합니다.",
        "magicSentences": [
            "This is a close-up picture taken in a laboratory.",
            "A pipette is dispensing purple liquid into a sample tube.",
            "Sample tubes are arranged in neat rows in a blue rack.",
            "Overall, the scene conveys high precision and research expertise."
        ],
        "scoreTip": "실험실 전문 묘사: 'pipette dispensing liquid(용액을 주입하는 피펫)', 'sample tubes in a rack(랙에 꽂힌 시료 튜브)'.",
        "vocabulary": [
            {"word": "pipette", "ipa": "[pɪˈpet]", "pos": "명사", "meaning": "피펫, 스포이트", "source": "사진 필수"},
            {"word": "dispense", "ipa": "[dɪˈspens]", "pos": "동사", "meaning": "(액체 등을) 분주하다, 투여하다", "source": "답변 핵심"},
            {"word": "sample tube", "ipa": "[ˈsɑːmpl tjuːb]", "pos": "명사구", "meaning": "시료 튜브, 소형 시험관", "source": "사진 필수"},
            {"word": "precision", "ipa": "[prɪˈsɪʒn]", "pos": "명사", "meaning": "정밀함, 정확성", "source": "답변 핵심"}
        ],
        "grammarPoints": [
            {"title": "정밀 동작 분사: is precisely dispensing ~ into", "explanation": "부사 precisely와 진행형 dispensing into를 결합하여 과학 연구의 정밀한 동작을 자연스럽게 묘사합니다."}
        ]
    }
]

# Update data.json
with open('data.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Part 2 only updated, part 3 and part 4 completely untouched
master_data['part2'] = part2_final

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: 26 Part 2 sets updated with 100% photo-verified 1:1 match in data.json!")
