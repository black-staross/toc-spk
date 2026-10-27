import json

# Define the exact 1:1 mapped sentences for all 26 Part 2 questions
PART2_SENTENCES = [
    # Q1
    {
        "en": [
            "This is a picture taken in an office.",
            "The first thing I can see from this picture is two men sitting at a desk.",
            "On the right side of the picture, a man wearing glasses and a gray sweater is working on a laptop and a computer monitor.",
            "Next to him, another man in a black shirt is also typing on a keyboard.",
            "On the desk, I can see a smartphone, headphones, and some potted plants.",
            "Overall, it seems like they are busy working."
        ],
        "ko": [
            "이 사진은 사무실에서 찍힌 사진입니다.",
            "사진에서 가장 먼저 보이는 것은 책상에 앉아 있는 두 남성입니다.",
            "사진 오른쪽에서는 안경과 회색 스웨터를 입은 남성이 노트북과 컴퓨터 모니터로 일하고 있습니다.",
            "그 옆에는 검은색 셔츠를 입은 다른 남성도 키보드로 타이핑을 하고 있습니다.",
            "책상 위에는 스마트폰, 헤드폰, 화분들이 보입니다.",
            "전반적으로 그들은 바쁘게 일하고 있는 것 같습니다."
        ]
    },
    # Q2
    {
        "en": [
            "This is a picture taken in an office.",
            "There are three people in this picture, and all of them are wearing formal clothes.",
            "In the middle of the picture, a woman in a beige suit and a man in a gray suit are standing and looking at a document on the table.",
            "She is holding a piece of paper and pointing at the table.",
            "In the foreground on the right, there is another man in a suit.",
            "In the background, I can see large windows and tall buildings."
        ],
        "ko": [
            "이 사진은 사무실에서 찍힌 사진입니다.",
            "사진에 세 사람이 있으며 모두 정장을 입고 있습니다.",
            "사진 가운데에는 베이지색 정장을 입은 여성과 회색 정장을 입은 남성이 서서 테이블 위의 문서를 보고 있습니다.",
            "그녀는 종이를 한 손에 들고 테이블을 가리키고 있습니다.",
            "오른쪽 앞에는 정장을 입은 또 다른 남성이 있습니다.",
            "배경에는 큰 창문들과 고층 빌딩들이 보입니다."
        ]
    },
    # Q3
    {
        "en": [
            "This is a picture taken at a cafe or a restaurant.",
            "On the right side of the picture, a woman wearing a red shirt is sitting on a sofa and looking at a tablet PC.",
            "In front of her, there is a glass of wine on the round table.",
            "On the left side of the picture, a man wearing a black suit and a blue tie is sitting at another table with a glass of water.",
            "In the background, I can see large potted plants by the window."
        ],
        "ko": [
            "이 사진은 카페나 레스토랑에서 찍힌 사진입니다.",
            "사진 오른쪽에는 빨간색 상의를 입은 여성이 소파에 앉아 태블릿 PC를 보고 있습니다.",
            "그녀 앞의 원형 테이블 위에는 와인 한 잔이 놓여 있습니다.",
            "사진 왼쪽에는 검은색 정장과 파란색 넥타이를 맨 남성이 물잔이 놓인 다른 테이블에 앉아 있습니다.",
            "배경에는 창가에 큰 화분들이 보입니다."
        ]
    },
    # Q4
    {
        "en": [
            "This is a picture taken in a meeting room.",
            "There are five people having a meeting.",
            "In the middle of the picture, a woman in a gray dress is standing and giving a presentation, pointing at a graph on a whiteboard.",
            "Around the glass table, four people are sitting and listening to the speaker, and a man on the right is writing something in a notebook.",
            "On the table, there are glasses of water.",
            "In the background, I can see large glass windows with a city view."
        ],
        "ko": [
            "이 사진은 회의실에서 찍힌 사진입니다.",
            "다섯 명의 사람이 회의를 하고 있습니다.",
            "사진 가운데에는 회색 원피스를 입은 여성이 서서 발표를 하고 있으며 화이트보드의 그래프를 가리키고 있습니다.",
            "유리 테이블 주변에는 네 사람이 앉아 발표자의 말을 듣고 있고, 오른쪽의 한 남성은 공책에 무언가를 적고 있습니다.",
            "테이블 위에는 물잔들이 놓여 있습니다.",
            "배경에는 도시 전망이 보이는 커다란 유리창이 보입니다."
        ]
    },
    # Q5
    {
        "en": [
            "This is a picture taken at an office.",
            "There are four people sitting around a conference table.",
            "In the middle of the picture, a woman with blonde hair wearing a pink shirt is smiling and showing a tablet PC to a man next to her.",
            "The man in a blue shirt is looking at the screen, and two other coworkers are sitting across the table.",
            "On the wooden table, there are some documents and cups."
        ],
        "ko": [
            "이 사진은 사무실에서 찍힌 사진입니다.",
            "회의 테이블 주변에 네 사람이 앉아 있습니다.",
            "사진 가운데에는 분홍색 셔츠를 입은 금발 여성이 미소를 지으며 옆에 있는 남성에게 태블릿 PC를 보여주고 있습니다.",
            "파란 셔츠를 입은 남성은 화면을 바라보고 있고, 다른 두 명의 동료는 테이블 건너편에 앉아 있습니다.",
            "나무 테이블 위에는 문서들과 컵들이 놓여 있습니다."
        ]
    },
    # Q6
    {
        "en": [
            "This is a picture taken in a classroom.",
            "On the right side of the picture, a man wearing a purple shirt and black pants is standing in front of a whiteboard.",
            "He is pointing at the whiteboard and teaching a class.",
            "On the left side of the picture, five students are sitting at the desks and listening to the teacher.",
            "There are some books and pens on the desks, and I can see large windows with blinds on the left."
        ],
        "ko": [
            "이 사진은 강의실에서 찍힌 사진입니다.",
            "사진 오른쪽에는 자주색 셔츠와 검은 바지를 입은 남성이 화이트보드 앞에 서 있습니다.",
            "그는 화이트보드를 가리키며 수업을 진행하고 있습니다.",
            "사진 왼쪽에는 다섯 명의 학생들이 책상에 앉아 선생님의 설명을 듣고 있습니다.",
            "책상 위에는 책과 펜들이 놓여 있고 왼쪽에는 블라인드가 있는 큰 창문이 보입니다."
        ]
    },
    # Q7
    {
        "en": [
            "This is a picture taken in a classroom.",
            "On the left side of the picture, a teacher wearing glasses and a gray jacket is standing and holding a tablet PC.",
            "On the right side of the picture, six students are sitting at their wooden desks.",
            "Some of the students are raising their hands to answer a question.",
            "In the background, I can see a globe, many books on the shelves, and a world map on the wall."
        ],
        "ko": [
            "이 사진은 교실에서 찍힌 사진입니다.",
            "사진 왼쪽에는 안경과 회색 자켓을 입은 선생님이 태블릿 PC를 들고 서 있습니다.",
            "사진 오른쪽에는 여섯 명의 학생들이 나무 책상에 앉아 있습니다.",
            "일부 학생들은 질문에 답하기 위해 손을 들고 있습니다.",
            "배경에는 지구본과 선반 위의 책들, 벽에 걸린 세계지도가 보입니다."
        ]
    },
    # Q8
    {
        "en": [
            "This is a picture taken at a restaurant.",
            "The first thing I can see from this picture is two women sitting at a table.",
            "In the middle of the picture, a woman with long blonde hair is drinking a beverage from a glass.",
            "Next to her, another woman is eating some food.",
            "On the table, there are dishes, bottles, and glasses.",
            "In the background, I can see many other customers sitting at tables and a waiter working."
        ],
        "ko": [
            "이 사진은 레스토랑에서 찍힌 사진입니다.",
            "가장 먼저 보이는 것은 테이블에 앉아 있는 두 여성입니다.",
            "사진 가운데에 있는 긴 금발 머리 여성은 유리잔으로 음료를 마시고 있습니다.",
            "그 옆의 다른 여성은 음식을 먹고 있습니다.",
            "테이블 위에는 접시와 병, 유리잔들이 놓여 있습니다.",
            "배경에는 테이블에 앉은 다른 많은 손님들과 일하는 웨이터가 보입니다."
        ]
    },
    # Q9
    {
        "en": [
            "This is a picture taken at a cafe or a bakery.",
            "In the middle of the picture, a woman wearing a blue shirt is ordering something at the counter.",
            "A staff member behind the counter is wearing a black shirt and taking her order.",
            "In front of the counter, there is a glass display case filled with delicious bread and cakes.",
            "In the background, I can see shelves with coffee cups and a menu board on the wall."
        ],
        "ko": [
            "이 사진은 카페나 베이커리에서 찍힌 사진입니다.",
            "사진 가운데에서는 파란색 셔츠를 입은 여성이 카운터에서 주문을 하고 있습니다.",
            "카운터 뒤의 직원은 검은색 상의를 입고 그녀의 주문을 받고 있습니다.",
            "카운터 앞에는 맛있는 빵과 케이크로 가득 찬 유리 진열장이 있습니다.",
            "배경에는 커피잔이 놓인 선반과 벽에 걸린 메뉴판이 보입니다."
        ]
    },
    # Q10
    {
        "en": [
            "This is a picture taken at an outdoor cafe.",
            "In the foreground on the left, a man wearing a red t-shirt and sunglasses is reading a newspaper with a cup of coffee on the table.",
            "Along the outdoor terrace, several other people are sitting at tables under large red parasols, talking or having drinks.",
            "In the background, I can see a historic building and green trees."
        ],
        "ko": [
            "이 사진은 야외 카페에서 찍힌 사진입니다.",
            "왼쪽 앞에는 빨간 티셔츠를 입고 선글라스를 낀 남성이 테이블 위의 커피 한 잔과 함께 신문을 읽고 있습니다.",
            "야외 테라스를 따라 여러 사람들이 커다란 빨간 파라솔 아래 테이블에 앉아 대화를 나누거나 음료를 마시고 있습니다.",
            "배경에는 유서 깊은 건물과 푸른 나무들이 보입니다."
        ]
    },
    # Q11
    {
        "en": [
            "This is a picture taken at an outdoor market.",
            "On the right side of the picture, a woman wearing a dark coat and a brown shoulder bag is looking at fresh vegetables.",
            "In the middle, a vendor wearing an apron is standing behind the wooden stall, talking to a customer.",
            "On the stalls, there are many colorful fruits and vegetables such as carrots, tomatoes, and pumpkins.",
            "In the background, other shoppers are walking around the market."
        ],
        "ko": [
            "이 사진은 야외 시장에서 찍힌 사진입니다.",
            "사진 오른쪽에는 어두운 코트를 입고 갈색 숄더백을 멘 여성이 신선한 채소들을 살펴보고 있습니다.",
            "가운데에는 앞치마를 두른 상인이 나무 가판대 뒤에 서서 손님과 이야기를 나누고 있습니다.",
            "가판대에는 당근, 토마토, 호박 같은 다채로운 과일과 채소들이 많이 놓여 있습니다.",
            "배경에는 다른 쇼핑객들이 시장 주변을 걷고 있습니다."
        ]
    },
    # Q12
    {
        "en": [
            "This is a picture taken at a grocery store.",
            "There are two women at the checkout counter.",
            "On the left side of the picture, a cashier wearing a green vest is holding a food container and scanning the item.",
            "On the right side of the picture, a customer with blonde hair is wearing a blue jacket.",
            "She is smiling and looking at the item being scanned.",
            "Next to them, there is a cash register and a monitor."
        ],
        "ko": [
            "이 사진은 식료품점에서 찍힌 사진입니다.",
            "계산대에 두 여성이 있습니다.",
            "사진 왼쪽에는 초록색 조끼를 입은 계산원이 식품 용기를 들고 상품을 스캔하고 있습니다.",
            "사진 오른쪽에는 금발 머리에 파란색 자켓을 입은 고객이 있습니다.",
            "그녀는 미소를 지으며 스캔되는 물건을 바라보고 있습니다.",
            "그들 옆에는 계산대와 모니터가 있습니다."
        ]
    },
    # Q13
    {
        "en": [
            "This is a picture taken at a clothing store.",
            "In the middle of the picture, two young women are shopping for clothes together.",
            "The woman on the left wearing a gray sweater is holding up a white blouse and showing it to her friend.",
            "Her friend, wearing a black leather jacket, is smiling and giving her advice.",
            "In the background, there are clothing racks filled with colorful clothes and a full-length mirror."
        ],
        "ko": [
            "이 사진은 옷가게에서 찍힌 사진입니다.",
            "사진 가운데에서는 두 명의 젊은 여성이 함께 옷을 쇼핑하고 있습니다.",
            "회색 스웨터를 입은 왼쪽 여성은 흰 블라우스를 들어 올려 친구에게 보여주고 있습니다.",
            "검은색 가죽 자켓을 입은 그녀의 친구는 미소를 지으며 조언을 해주고 있습니다.",
            "배경에는 다채로운 옷들이 걸린 옷걸이 행거와 전신 거울이 놓여 있습니다."
        ]
    },
    # Q14
    {
        "en": [
            "This is a picture taken at a subway station.",
            "On the left side of the picture, a man wearing a brown coat and a backpack is walking along the platform while holding a white plastic bag.",
            "On the right side of the picture, another man carrying a bag is standing near the yellow subway train.",
            "In the background, several passengers are getting on the subway.",
            "I can also see large white pillars and bright lights on the ceiling."
        ],
        "ko": [
            "이 사진은 지하철역에서 찍힌 사진입니다.",
            "사진 왼쪽에는 갈색 코트를 입고 백팩을 멘 남성이 흰 비닐봉지를 든 채 승강장을 따라 걷고 있습니다.",
            "사진 오른쪽에는 가방을 멘 다른 남성이 노란색 지하철 열차 근처에 서 있습니다.",
            "배경에서는 여러 승객들이 지하철에 탑승하고 있습니다.",
            "또한 커다란 흰 기둥들과 천장의 밝은 조명들도 보입니다."
        ]
    },
    # Q15
    {
        "en": [
            "This is a picture taken at an airport.",
            "In the middle of the picture, a family of four is walking through the terminal, carrying their luggage.",
            "The father on the left is wearing a blue shirt and pulling a black suitcase, and the mother next to him is holding her daughter's hand.",
            "The little boy is pulling a small blue suitcase behind them.",
            "In the background, I can see a flight information board, large glass windows, and airplanes outside."
        ],
        "ko": [
            "이 사진은 공항에서 찍힌 사진입니다.",
            "사진 가운데에는 네 명의 가족이 짐을 들고 터미널을 걸어가고 있습니다.",
            "왼쪽의 아버지는 파란 셔츠를 입고 검은 여행가방을 끌고 있으며, 옆에 있는 어머니는 딸의 손을 잡고 있습니다.",
            "어린 아들은 그들 뒤에서 작은 파란 여행가방을 끌고 있습니다.",
            "배경에는 항공편 안내 전광판, 큰 유리창, 그리고 바깥의 비행기들이 보입니다."
        ]
    },
    # Q16
    {
        "en": [
            "This is a picture taken at a park or a garden.",
            "In the middle of the picture, a man wearing a green polo shirt and a sun hat is working in the garden.",
            "He is kneeling on the grass and using a small shovel to plant some flowers.",
            "Next to him, there is a green watering can and a brown pot filled with soil.",
            "In the background, I can see many blooming flowers and green bushes."
        ],
        "ko": [
            "이 사진은 공원이나 정원에서 찍힌 사진입니다.",
            "사진 가운데에는 초록색 폴로 셔츠와 챙 넓은 모자를 쓴 남성이 정원에서 일하고 있습니다.",
            "그는 잔디밭 위에 무릎을 꿇고 작은 모종삽을 사용해 꽃을 심고 있습니다.",
            "그 옆에는 초록색 물뿌리개와 흙이 담긴 갈색 화분이 놓여 있습니다.",
            "배경에는 활짝 핀 꽃들과 푸른 관목들이 보입니다."
        ]
    },
    # Q17
    {
        "en": [
            "This is a picture taken at an outdoor park.",
            "In the middle of the picture, a man and a woman in athletic clothes are jogging along a paved path.",
            "The man is wearing a gray sleeveless shirt and black shorts, and the woman is wearing a pink sports top and black leggings.",
            "They are both smiling and looking ahead.",
            "In the background, there are large green trees, a grassy lawn, and a small wooden bridge over a pond."
        ],
        "ko": [
            "이 사진은 야외 공원에서 찍힌 사진입니다.",
            "사진 가운데에서는 운동복을 입은 남성과 여성이 포장된 산책로를 따라 조깅을 하고 있습니다.",
            "남성은 회색 민소매 셔츠와 검은 반바지를 입고 있고, 여성은 분홍색 운동복 상의와 검은 레깅스를 입고 있습니다.",
            "두 사람 모두 미소를 지으며 앞을 바라보고 있습니다.",
            "배경에는 커다란 푸른 나무들과 잔디밭, 연못 위의 작은 나무다리가 보입니다."
        ]
    },
    # Q18
    {
        "en": [
            "This is a picture taken on a hiking trail.",
            "In the middle of the picture, three people with backpacks are hiking up a rocky mountain trail.",
            "The person in front is using trekking poles to climb the hill, and the other two are following closely behind.",
            "They are all wearing outdoor clothing and hiking boots.",
            "In the background, I can see beautiful mountain peaks under a clear blue sky."
        ],
        "ko": [
            "이 사진은 등산로에서 찍힌 사진입니다.",
            "사진 가운데에서는 배낭을 멘 세 사람이 바위가 많은 산길을 하이킹하고 있습니다.",
            "맨 앞의 사람은 등산 스틱을 사용하여 언덕을 오르고 있으며, 다른 두 사람은 바로 뒤를 따르고 있습니다.",
            "그들은 모두 아웃도어 의류와 등산화를 착용하고 있습니다.",
            "배경에는 맑고 푸른 하늘 아래 아름다운 산봉우리들이 보입니다."
        ]
    },
    # Q19
    {
        "en": [
            "This is a picture taken at the beach.",
            "A family is having a good time on the sand.",
            "In the middle of the picture, a man, a woman, and two little girls are sitting on the sand and playing with sand and a yellow bucket.",
            "On the left side, a girl wearing a pink striped top and shorts is standing under a blue striped parasol, playing a racket game with a boy on the right.",
            "In the background, I can see the blue sea and waves.",
            "Overall, it seems like a beautiful sunny day."
        ],
        "ko": [
            "이 사진은 해변에서 찍힌 사진입니다.",
            "한 가족이 모래사장에서 즐거운 시간을 보내고 있습니다.",
            "사진 가운데에는 남성과 여성, 그리고 두 어린 소녀가 모래 위에 앉아 노란 양동이를 가지고 모래놀이를 하고 있습니다.",
            "왼쪽에는 분홍색 줄무늬 상의와 반바지를 입은 소녀가 파란 줄무늬 파라솔 아래에 서서 오른쪽의 소년과 라켓 게임을 하고 있습니다.",
            "배경에는 푸른 바다와 파도가 보입니다.",
            "전반적으로 아름답고 화창한 날 같습니다."
        ]
    },
    # Q20
    {
        "en": [
            "This is a picture taken on a street.",
            "In the middle of the picture, a woman and two children are standing in front of a crosswalk, and I can see their backs.",
            "The woman is wearing a black jacket and black pants, and she is holding the children's hands.",
            "The boy on the left is wearing a black backpack, and the girl on the right is wearing pink clothes and an orange backpack.",
            "In front of them, there is a crosswalk and a traffic light, and I can see trees and buildings in the background."
        ],
        "ko": [
            "이 사진은 거리에서 찍힌 사진입니다.",
            "사진 가운데에 한 여성과 두 아이가 횡단보도 앞에 서 있으며 그들의 뒷모습이 보입니다.",
            "여성은 검은 자켓과 검은 바지를 입고 아이들의 손을 잡고 있습니다.",
            "왼쪽 남자아이는 검은 백팩을 메고 있고 오른쪽 여자아이는 분홍색 옷과 주황색 백팩을 메고 있습니다.",
            "그들 앞에는 횡단보도와 신호등이 있으며 배경에는 나무들과 건물들이 보입니다."
        ]
    },
    # Q21
    {
        "en": [
            "This is a picture taken on a street.",
            "On the left side of the picture, a man wearing a yellow t-shirt and black shorts is riding a bicycle on the road, and I can see his back.",
            "On the right side of the picture, an older man wearing a white shirt and gray pants is walking on the sidewalk.",
            "In the background, there is a restaurant with a blue signboard, and several people are standing outside the store.",
            "Overall, it seems like a busy day in a city."
        ],
        "ko": [
            "이 사진은 거리에서 찍힌 사진입니다.",
            "사진 왼쪽에는 노란 티셔츠와 검은 반바지를 입은 남성이 도로에서 자전거를 타고 있으며 뒷모습이 보입니다.",
            "사진 오른쪽에는 흰 셔츠와 회색 바지를 입은 한 남성이 인도를 따라 걷고 있습니다.",
            "배경에는 파란 간판이 달린 식당이 있고 여러 사람들이 가게 밖에 서 있습니다.",
            "전반적으로 도시의 분주한 날 같습니다."
        ]
    },
    # Q22
    {
        "en": [
            "This is a picture taken at a park.",
            "In the foreground on the left, two people are sitting on the grass and relaxing on a mat.",
            "Along the path in the middle, some people are walking on the left, and three people are riding bicycles on the right.",
            "In the background, I can see many large green trees and a wide grassy field.",
            "Overall, it seems like a beautiful sunny and peaceful day."
        ],
        "ko": [
            "이 사진은 공원에서 찍힌 사진입니다.",
            "왼쪽 앞에는 두 사람이 잔디밭 위 매트에 앉아 휴식을 취하고 있습니다.",
            "가운데 산책로를 따라 왼쪽에는 몇몇 사람들이 걷고 있고, 오른쪽에는 세 사람이 자전거를 타고 있습니다.",
            "배경에는 커다란 푸른 나무들과 넓은 잔디밭이 보입니다.",
            "전반적으로 아름답고 화창하며 평화로운 날 같습니다."
        ]
    },
    # Q23
    {
        "en": [
            "This is a picture taken on a narrow street in a city.",
            "In the middle of the picture, several people wearing dark jackets and coats are walking along the stone street.",
            "On both sides of the street, there are tall, colorful buildings with shops on the first floor.",
            "I can also see many signboards and a flag hanging on the walls of the buildings.",
            "Overall, it seems like a peaceful day in a historic city."
        ],
        "ko": [
            "이 사진은 도시의 좁은 거리에서 찍힌 사진입니다.",
            "사진 가운데에는 어두운 자켓과 코트를 입은 여러 사람들이 돌길을 따라 걷고 있습니다.",
            "거리 양쪽에는 1층에 상점이 있는 높고 다채로운 색상의 건물들이 늘어서 있습니다.",
            "또한 건물 벽면에 걸려 있는 여러 간판들과 깃발도 보입니다.",
            "전반적으로 유서 깊은 도시의 평화로운 날 같습니다."
        ]
    },
    # Q24
    {
        "en": [
            "This is a picture taken at a warehouse.",
            "In the middle of the picture, two men wearing blue gloves and safety glasses are carrying a large cardboard box together.",
            "The man on the right is wearing a red checked shirt, and they are putting the box onto a wooden pallet.",
            "On the left side of the picture, there is a forklift.",
            "In the background, I can see many boxes stacked on the shelves.",
            "Overall, it seems like they are busy working."
        ],
        "ko": [
            "이 사진은 창고에서 찍힌 사진입니다.",
            "사진 가운데에서는 파란 장갑과 보안경을 착용한 두 남성이 함께 커다란 종이 박스를 운반하고 있습니다.",
            "오른쪽 남성은 빨간 체크무늬 셔츠를 입고 있으며, 그들은 나무 팔레트 위에 박스를 내려놓고 있습니다.",
            "사진 왼쪽에는 지게차가 한 대 있습니다.",
            "배경에는 선반 위에 많은 박스들이 쌓여 있는 것이 보입니다.",
            "전반적으로 그들은 바쁘게 일하고 있는 것 같습니다."
        ]
    },
    # Q25
    {
        "en": [
            "This is a picture taken at a large warehouse.",
            "On the right side of the picture, a man wearing a yellow safety vest and jeans is standing and looking at a device in his hands.",
            "On the left side of the picture, another worker is operating an orange forklift, and there is a third worker standing in the aisle in the distance.",
            "In the background, I can see many boxes stacked high on the tall shelves.",
            "Overall, it seems like they are busy working."
        ],
        "ko": [
            "이 사진은 대형 창고에서 찍힌 사진입니다.",
            "사진 오른쪽에는 노란색 안전 조끼와 청바지를 입은 남성이 서서 손에 든 기기를 보고 있습니다.",
            "사진 왼쪽에는 다른 작업자가 주황색 지게차를 운전하고 있으며, 멀리 통로에 세 번째 작업자가 서 있습니다.",
            "배경에는 높은 선반 위에 많은 박스들이 높이 쌓여 있는 것이 보입니다.",
            "전반적으로 그들은 바쁘게 일하고 있는 것 같습니다."
        ]
    },
    # Q26
    {
        "en": [
            "This is a picture taken at a laboratory.",
            "There are two researchers sitting at a desk and wearing white lab coats, masks, hairnets, and gloves.",
            "On the left side of the picture, a woman is holding a pen and writing something down on a clipboard.",
            "On the right side of the picture, a man is looking through a microscope.",
            "On the table, there are some petri dishes and lab equipment, and I can see many binders arranged on the shelves in the background."
        ],
        "ko": [
            "이 사진은 실험실에서 찍힌 사진입니다.",
            "두 명의 연구원이 흰 실험 가운과 마스크, 위생 모자, 장갑을 착용하고 책상에 앉아 있습니다.",
            "사진 왼쪽에서는 한 여성이 펜을 들고 클립보드에 무언가를 적고 있습니다.",
            "사진 오른쪽에서는 한 남성이 현미경을 들여다보고 있습니다.",
            "테이블 위에는 페트리 접시와 실험 기구들이 놓여 있고 배경의 선반에는 많은 바인더 파일들이 정리되어 있습니다."
        ]
    }
]

print(f"Loaded definitions for {len(PART2_SENTENCES)} questions.")

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

part2 = data.get('part2', [])
assert len(part2) == len(PART2_SENTENCES), f"Count mismatch: {len(part2)} vs {len(PART2_SENTENCES)}"

for i in range(len(part2)):
    spec = PART2_SENTENCES[i]
    en_sentences = spec['en']
    ko_sentences = spec['ko']
    assert len(en_sentences) == len(ko_sentences), f"Q{i+1} en/ko mismatch: {len(en_sentences)} vs {len(ko_sentences)}"

    # Format into newline-separated sentences like Part 3 and Part 4
    formatted_en = "\n\n".join(en_sentences)
    formatted_ko = "\n\n".join(ko_sentences)

    part2[i]['answer'] = formatted_en
    part2[i]['answerTranslation'] = formatted_ko

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully updated all 26 Part 2 questions in data.json with structured sentences!")
