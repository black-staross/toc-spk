import json

# Read existing data.json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extended vocabulary definitions mapped by problem ID (3 to 5 words each)
vocab_enrichment = {
    1: [
        {"word": "convenient", "ipa": "[kənˈviːniənt]", "pos": "형용사", "meaning": "편리한, 간편한"},
        {"word": "comfortable", "ipa": "[ˈkʌmftəbl]", "pos": "형용사", "meaning": "편안한, 안락한"},
        {"word": "purchase", "ipa": "[ˈpɜːtʃəs]", "pos": "동사/명사", "meaning": "구매하다, 구매품"},
        {"word": "online store", "ipa": "[ˈɒnlaɪn stɔː(r)]", "pos": "명사구", "meaning": "온라인 쇼핑몰"}
    ],
    2: [
        {"word": "customer review", "ipa": "[ˈkʌstəmə rɪˈvjuː]", "pos": "명사구", "meaning": "고객 후기"},
        {"word": "useful", "ipa": "[ˈjuːsfl]", "pos": "형용사", "meaning": "유용한, 도움되는"},
        {"word": "decision", "ipa": "[dɪˈsɪʒn]", "pos": "명사", "meaning": "결정, 선택"},
        {"word": "satisfaction", "ipa": "[ˌsætɪsˈfækʃn]", "pos": "명사", "meaning": "만족, 만족도"}
    ],
    3: [
        {"word": "reasonable", "ipa": "[ˈriːznəbl]", "pos": "형용사", "meaning": "합리적인, 적당한"},
        {"word": "tight budget", "ipa": "[taɪt ˈbʌdʒɪt]", "pos": "명사구", "meaning": "빠듯한 예산"},
        {"word": "delivery", "ipa": "[dɪˈlɪvəri]", "pos": "명사", "meaning": "배송, 배달"},
        {"word": "factor", "ipa": "[ˈfæktə(r)]", "pos": "명사", "meaning": "요소, 요인"},
        {"word": "essential", "ipa": "[ɪˈsenʃl]", "pos": "형용사", "meaning": "필수적인"}
    ],
    4: [
        {"word": "frequently", "ipa": "[ˈfriːkwəntli]", "pos": "부사", "meaning": "자주, 흔히"},
        {"word": "companion", "ipa": "[kəmˈpæniən]", "pos": "명사", "meaning": "동행인, 친구"},
        {"word": "conversation", "ipa": "[ˌkɒnvəˈseɪʃn]", "pos": "명사", "meaning": "대화, 담소"},
        {"word": "beverage", "ipa": "[ˈbevərɪdʒ]", "pos": "명사", "meaning": "음료 (커피/차 등)"}
    ],
    5: [
        {"word": "relieve", "ipa": "[rɪˈliːv]", "pos": "동사", "meaning": "(스트레스를) 덜다, 해소하다"},
        {"word": "stressed out", "ipa": "[strest aʊt]", "pos": "형용사구", "meaning": "스트레스가 쌓인"},
        {"word": "atmosphere", "ipa": "[ˈætməsfɪə(r)]", "pos": "명사", "meaning": "분위기"},
        {"word": "environment", "ipa": "[ɪnˈvaɪrənmənt]", "pos": "명사", "meaning": "환경, 주변 여건"}
    ],
    6: [
        {"word": "location", "ipa": "[ləʊˈkeɪʃn]", "pos": "명사", "meaning": "위치, 장소"},
        {"word": "daily routine", "ipa": "[ˈdeɪli ruːˈtiːn]", "pos": "명사구", "meaning": "일상, 일과"},
        {"word": "accessible", "ipa": "[əkˈsesəbl]", "pos": "형용사", "meaning": "접근하기 쉬운"},
        {"word": "variety", "ipa": "[vəˈraɪəti]", "pos": "명사", "meaning": "다양성, 여러 가지"}
    ],
    7: [
        {"word": "regularly", "ipa": "[ˈreɡjələli]", "pos": "부사", "meaning": "규칙적으로, 정기적으로"},
        {"word": "jogging", "ipa": "[ˈdʒɒɡɪŋ]", "pos": "명사", "meaning": "조깅, 가벼운 달리기"},
        {"word": "healthy", "ipa": "[ˈhelθi]", "pos": "형용사", "meaning": "건강한"},
        {"word": "stamina", "ipa": "[ˈstæmɪnə]", "pos": "명사", "meaning": "체력, 원기"}
    ],
    8: [
        {"word": "prefer", "ipa": "[prɪˈfɜː(r)]", "pos": "동사", "meaning": "더 좋아하다, 선호하다"},
        {"word": "quality time", "ipa": "[ˈkwɒləti taɪm]", "pos": "명사구", "meaning": "소중하고 의미 있는 시간"},
        {"word": "motivate", "ipa": "[ˈməʊtɪveɪt]", "pos": "동사", "meaning": "동기를 부여하다, 자극하다"},
        {"word": "enjoyable", "ipa": "[ɪnˈdʒɔɪəbl]", "pos": "형용사", "meaning": "즐거운, 유쾌한"}
    ],
    9: [
        {"word": "advantage", "ipa": "[ədˈvɑːntɪdʒ]", "pos": "명사", "meaning": "장점, 이점"},
        {"word": "regular basis", "ipa": "[ˈreɡjələ ˈbeɪsɪs]", "pos": "명사구", "meaning": "정기적인/규칙적인 기준"},
        {"word": "refreshed", "ipa": "[rɪˈfreʃt]", "pos": "형용사", "meaning": "상쾌해진, 기운이 난"},
        {"word": "mental health", "ipa": "[ˈmentl helθ]", "pos": "명사구", "meaning": "정신 건강"},
        {"word": "vitality", "ipa": "[vaɪˈtæləti]", "pos": "명사", "meaning": "활력, 생기"}
    ],
    10: [
        {"word": "comfortable", "ipa": "[ˈkʌmftəbl]", "pos": "형용사", "meaning": "편안한"},
        {"word": "relaxing", "ipa": "[rɪˈlæksɪŋ]", "pos": "형용사", "meaning": "마음을 편안하게 해주는"},
        {"word": "couch", "ipa": "[kaʊtʃ]", "pos": "명사", "meaning": "소파"},
        {"word": "leisure time", "ipa": "[ˈleʒə taɪm]", "pos": "명사구", "meaning": "여가 시간"}
    ],
    11: [
        {"word": "theater", "ipa": "[ˈθɪətə(r)]", "pos": "명사", "meaning": "영화관, 극장"},
        {"word": "action movie", "ipa": "[ˈækʃn ˈmuːvi]", "pos": "명사구", "meaning": "액션 영화"},
        {"word": "exciting", "ipa": "[ɪkˈsaɪtɪŋ]", "pos": "형용사", "meaning": "신나는, 흥미진진한"},
        {"word": "relieved", "ipa": "[rɪˈliːvd]", "pos": "형용사/과거", "meaning": "안도한, 풀린"}
    ],
    12: [
        {"word": "streaming service", "ipa": "[ˈstriːmɪŋ ˈsɜːvɪs]", "pos": "명사구", "meaning": "스트리밍 서비스"},
        {"word": "expensive", "ipa": "[ɪkˈspensɪv]", "pos": "형용사", "meaning": "비싼"},
        {"word": "anytime and anywhere", "ipa": "[ˈenitaɪm ənd ˈeniweə(r)]", "pos": "부사구", "meaning": "언제 어디서나"},
        {"word": "subscription", "ipa": "[səbˈskrɪpʃn]", "pos": "명사", "meaning": "구독 (월정액 등)"}
    ],
    13: [
        {"word": "vacation", "ipa": "[veɪˈkeɪʃn]", "pos": "명사", "meaning": "휴가, 방학"},
        {"word": "island", "ipa": "[ˈaɪlənd]", "pos": "명사", "meaning": "섬 (s 발음 안 됨)"},
        {"word": "destination", "ipa": "[ˌdestɪˈneɪʃn]", "pos": "명사", "meaning": "목적지, 여행지"},
        {"word": "memorable", "ipa": "[ˈmemərəbl]", "pos": "형용사", "meaning": "기억에 남는, 인상 깊은"}
    ],
    14: [
        {"word": "recommendation", "ipa": "[ˌrekəmenˈdeɪʃn]", "pos": "명사", "meaning": "추천, 권고"},
        {"word": "honest review", "ipa": "[ˈɒnɪst rɪˈvjuː]", "pos": "명사구", "meaning": "솔직한 후기"},
        {"word": "social media", "ipa": "[ˌsəʊʃl ˈmiːdiə]", "pos": "명사구", "meaning": "SNS, 소셜 미디어"},
        {"word": "itinerary", "ipa": "[aɪˈtɪnərəri]", "pos": "명사", "meaning": "여행 일정표"}
    ],
    15: [
        {"word": "attraction", "ipa": "[əˈtrækʃn]", "pos": "명사", "meaning": "관광 명소, 볼거리"},
        {"word": "companion", "ipa": "[kəmˈpæniən]", "pos": "명사", "meaning": "동행인, 친구"},
        {"word": "unforgettable", "ipa": "[ˌʌnfəˈɡetəbl]", "pos": "형용사", "meaning": "잊을 수 없는"},
        {"word": "scenery", "ipa": "[ˈsiːnəri]", "pos": "명사", "meaning": "경치, 풍경"},
        {"word": "experience", "ipa": "[ɪkˈspɪəriəns]", "pos": "명사/동사", "meaning": "경험, 경험하다"}
    ],
    16: [
        {"word": "public transportation", "ipa": "[ˈpʌblɪk ˌtrænspɔːˈteɪʃn]", "pos": "명사구", "meaning": "대중교통"},
        {"word": "subway", "ipa": "[ˈsʌbweɪ]", "pos": "명사", "meaning": "지하철"},
        {"word": "commute", "ipa": "[kəˈmjuːt]", "pos": "명사/동사", "meaning": "통근, 통학하다"},
        {"word": "convenient", "ipa": "[kənˈviːniənt]", "pos": "형용사", "meaning": "편리한"}
    ],
    17: [
        {"word": "boring", "ipa": "[ˈbɔːrɪŋ]", "pos": "형용사", "meaning": "지루한, 따분한"},
        {"word": "commute time", "ipa": "[kəˈmjuːt taɪm]", "pos": "명사구", "meaning": "출퇴근 시간"},
        {"word": "earphones", "ipa": "[ˈɪəfəʊnz]", "pos": "명사", "meaning": "이어폰"},
        {"word": "pass the time", "ipa": "[pɑːs ðə taɪm]", "pos": "동사구", "meaning": "시간을 보내다"}
    ],
    18: [
        {"word": "rush hour", "ipa": "[ˈrʌʃ aʊə(r)]", "pos": "명사구", "meaning": "혼잡 시간대, 출퇴근 시간"},
        {"word": "parking fee", "ipa": "[ˈpɑːkɪŋ fiː]", "pos": "명사구", "meaning": "주차 요금"},
        {"word": "traffic jam", "ipa": "[ˈtræfɪk dʒæm]", "pos": "명사구", "meaning": "교통 체증"},
        {"word": "economical", "ipa": "[ˌiːkəˈnɒmɪkl]", "pos": "형용사", "meaning": "경제적인, 절약되는"}
    ],
    19: [
        {"word": "eat out", "ipa": "[iːt aʊt]", "pos": "동사구", "meaning": "외식하다"},
        {"word": "delicious", "ipa": "[dɪˈlɪʃəs]", "pos": "형용사", "meaning": "맛있는"},
        {"word": "cuisine", "ipa": "[kwɪˈziːn]", "pos": "명사", "meaning": "요리, 음식"},
        {"word": "barbecue", "ipa": "[ˈbɑːbɪkjuː]", "pos": "명사", "meaning": "바비큐, 고기구이"}
    ],
    20: [
        {"word": "prevent", "ipa": "[prɪˈvent]", "pos": "동사", "meaning": "예방하다, 막다"},
        {"word": "mistake", "ipa": "[mɪˈsteɪk]", "pos": "명사", "meaning": "실수, 착오"},
        {"word": "rating", "ipa": "[ˈreɪtɪŋ]", "pos": "명사", "meaning": "평점, 등급"},
        {"word": "reputation", "ipa": "[ˌrepjuˈteɪʃn]", "pos": "명사", "meaning": "평판, 명성"}
    ],
    21: [
        {"word": "cozy", "ipa": "[ˈkəʊzi]", "pos": "형용사", "meaning": "아늑한, 포근한"},
        {"word": "atmosphere", "ipa": "[ˈætməsfɪə(r)]", "pos": "명사", "meaning": "분위기"},
        {"word": "satisfying", "ipa": "[ˈsætɪsfaɪɪŋ]", "pos": "형용사", "meaning": "만족스러운"},
        {"word": "hospitality", "ipa": "[ˌhɒspɪˈtæləti]", "pos": "명사", "meaning": "환대, 친절함"}
    ],
    22: [
        {"word": "peaceful", "ipa": "[ˈpiːsfl]", "pos": "형용사", "meaning": "평화로운, 조용한"},
        {"word": "quiet", "ipa": "[ˈkwaɪət]", "pos": "형용사", "meaning": "조용한, 한적한"},
        {"word": "novel", "ipa": "[ˈnɒvl]", "pos": "명사", "meaning": "소설"},
        {"word": "habit", "ipa": "[ˈhæbɪt]", "pos": "명사", "meaning": "습관"}
    ],
    23: [
        {"word": "lightweight", "ipa": "[ˈlaɪtweɪt]", "pos": "형용사", "meaning": "가벼운"},
        {"word": "e-book", "ipa": "[ˈiː bʊk]", "pos": "명사", "meaning": "전자책"},
        {"word": "portable", "ipa": "[ˈpɔːtəbl]", "pos": "형용사", "meaning": "휴대용의, 들고 다닐 수 있는"},
        {"word": "device", "ipa": "[dɪˈvaɪs]", "pos": "명사", "meaning": "기기, 장치"}
    ],
    24: [
        {"word": "concentrate", "ipa": "[ˈkɒnsntreɪt]", "pos": "동사", "meaning": "집중하다"},
        {"word": "borrow", "ipa": "[ˈbɒrəʊ]", "pos": "동사", "meaning": "빌리다, 대여하다"},
        {"word": "distraction", "ipa": "[dɪˈstrækʃn]", "pos": "명사", "meaning": "집중을 방해하는 것"},
        {"word": "public facility", "ipa": "[ˈpʌblɪk fəˈsɪləti]", "pos": "명사구", "meaning": "공공 시설"}
    ],
    25: [
        {"word": "messaging", "ipa": "[ˈmesɪdʒɪŋ]", "pos": "명사", "meaning": "문자 전송"},
        {"word": "screen time", "ipa": "[skriːn taɪm]", "pos": "명사구", "meaning": "스마트폰 화면 사용 시간"},
        {"word": "entertainment", "ipa": "[ˌentəˈteɪnmənt]", "pos": "명사", "meaning": "오락, 여가 즐길거리"},
        {"word": "indispensable", "ipa": "[ˌɪndɪˈspensəbl]", "pos": "형용사", "meaning": "없어서는 안 될, 필수적인"}
    ],
    26: [
        {"word": "keep in touch", "ipa": "[kiːp ɪn tʌtʃ]", "pos": "동사구", "meaning": "연락을 유지하다"},
        {"word": "stay connected", "ipa": "[steɪ kəˈnektɪd]", "pos": "동사구", "meaning": "소통하며 지내다"},
        {"word": "instant", "ipa": "[ˈɪnstənt]", "pos": "형용사", "meaning": "즉각적인, 빠른"},
        {"word": "distance", "ipa": "[ˈdɪstəns]", "pos": "명사", "meaning": "거리, 간격"}
    ],
    27: [
        {"word": "arrival time", "ipa": "[əˈraɪvl taɪm]", "pos": "명사구", "meaning": "도착 시간"},
        {"word": "convenience", "ipa": "[kənˈviːniəns]", "pos": "명사", "meaning": "편리함, 편의"},
        {"word": "efficiency", "ipa": "[ɪˈfɪʃnsi]", "pos": "명사", "meaning": "효율성, 능률"},
        {"word": "application", "ipa": "[ˌæplɪˈkeɪʃn]", "pos": "명사", "meaning": "응용 프로그램, 앱"}
    ],
    28: [
        {"word": "fried rice", "ipa": "[fraɪd raɪs]", "pos": "명사구", "meaning": "볶음밥"},
        {"word": "simple to make", "ipa": "[ˈsɪmpl tə meɪk]", "pos": "형용사구", "meaning": "만들기 간단한"},
        {"word": "home-cooked meal", "ipa": "[həʊm kʊkt miːl]", "pos": "명사구", "meaning": "집밥"},
        {"word": "ingredient", "ipa": "[ɪnˈɡriːdiənt]", "pos": "명사", "meaning": "재료, 식재료"}
    ],
    29: [
        {"word": "delivery fee", "ipa": "[dɪˈlɪvəri fiː]", "pos": "명사구", "meaning": "배달비"},
        {"word": "nutritious", "ipa": "[njuːˈtrɪʃəs]", "pos": "형용사", "meaning": "영양가 있는"},
        {"word": "hygienic", "ipa": "[haɪˈdʒiːnɪk]", "pos": "형용사", "meaning": "위생적인, 청결한"},
        {"word": "save money", "ipa": "[seɪv ˈmʌni]", "pos": "동사구", "meaning": "돈을 절약하다"}
    ],
    30: [
        {"word": "recipe", "ipa": "[ˈresəpi]", "pos": "명사", "meaning": "조리법, 요리 레시피"},
        {"word": "step by step", "ipa": "[step baɪ step]", "pos": "부사구", "meaning": "차근차근, 단계별로"},
        {"word": "visual guide", "ipa": "[ˈvɪʒuəl ɡaɪd]", "pos": "명사구", "meaning": "시각적 안내"},
        {"word": "beginner", "ipa": "[bɪˈɡɪnə(r)]", "pos": "명사", "meaning": "초보자, 입문자"}
    ],
    31: [
        {"word": "take a walk", "ipa": "[teɪk ə wɔːk]", "pos": "동사구", "meaning": "산책하다"},
        {"word": "fresh air", "ipa": "[freʃ eə(r)]", "pos": "명사구", "meaning": "신선한 공기"},
        {"word": "peace of mind", "ipa": "[piːs əv maɪnd]", "pos": "명사구", "meaning": "마음의 평화"},
        {"word": "unwind", "ipa": "[ˌʌnˈwaɪnd]", "pos": "동사", "meaning": "긴장을 풀다, 휴식하다"}
    ],
    32: [
        {"word": "citizen", "ipa": "[ˈsɪtɪzn]", "pos": "명사", "meaning": "시민, 거주자"},
        {"word": "mental health", "ipa": "[ˈmentl helθ]", "pos": "명사구", "meaning": "정신 건강"},
        {"word": "green space", "ipa": "[ɡriːn speɪs]", "pos": "명사구", "meaning": "녹지 공간"},
        {"word": "urban life", "ipa": "[ˈɜːbən laɪf]", "pos": "명사구", "meaning": "도시 생활"}
    ],
    33: [
        {"word": "facility", "ipa": "[fəˈsɪləti]", "pos": "명사", "meaning": "시설, 설비"},
        {"word": "walking path", "ipa": "[ˈwɔːkɪŋ pɑːθ]", "pos": "명사구", "meaning": "산책로, 보행로"},
        {"word": "recharge", "ipa": "[ˌriːˈtʃɑːdʒ]", "pos": "동사", "meaning": "재충전하다"},
        {"word": "rest area", "ipa": "[rest ˈeəriə]", "pos": "명사구", "meaning": "쉼터, 휴식 구역"}
    ],
    34: [
        {"word": "grocery shopping", "ipa": "[ˈɡrəʊsəri ˈʃɒpɪŋ]", "pos": "명사구", "meaning": "식료품 장보기"},
        {"word": "vegetable", "ipa": "[ˈvedʒtəbl]", "pos": "명사", "meaning": "채소, 야채"},
        {"word": "freshness", "ipa": "[ˈfreʃnəs]", "pos": "명사", "meaning": "신선도"},
        {"word": "shopping list", "ipa": "[ˈʃɒpɪŋ lɪst]", "pos": "명사구", "meaning": "구매 목록"}
    ],
    35: [
        {"word": "variety of options", "ipa": "[vəˈraɪəti əv ˈɒpʃnz]", "pos": "명사구", "meaning": "다양한 선택지"},
        {"word": "discount", "ipa": "[ˈdɪskaʊnt]", "pos": "명사", "meaning": "할인"},
        {"word": "bulk purchase", "ipa": "[bʌlk ˈpɜːtʃəs]", "pos": "명사구", "meaning": "대량 구매"},
        {"word": "affordability", "ipa": "[əˌfɔːdəˈbɪləti]", "pos": "명사", "meaning": "적당한 가격대"}
    ],
    36: [
        {"word": "fresh ingredient", "ipa": "[freʃ ɪnˈɡriːdiənt]", "pos": "명사구", "meaning": "신선한 식재료"},
        {"word": "nutritional value", "ipa": "[njuːˈtrɪʃənl ˈvæljuː]", "pos": "명사구", "meaning": "영양가"},
        {"word": "flavor", "ipa": "[ˈfleɪvə(r)]", "pos": "명사", "meaning": "맛, 풍미"},
        {"word": "well-being", "ipa": "[ˈwel biːɪŋ]", "pos": "명사", "meaning": "웰빙, 건강한 삶"}
    ],
    37: [
        {"word": "genre", "ipa": "[ˈʒɑːnrə]", "pos": "명사", "meaning": "음악 장르, 유형"},
        {"word": "acoustic song", "ipa": "[əˈkuːstɪk sɒŋ]", "pos": "명사구", "meaning": "어쿠스틱 곡"},
        {"word": "uplifting", "ipa": "[ˌʌpˈlɪftɪŋ]", "pos": "형용사", "meaning": "기운을 북돋우는"},
        {"word": "playlist", "ipa": "[ˈpleɪlɪst]", "pos": "명사", "meaning": "재생 목록"}
    ],
    38: [
        {"word": "podcast", "ipa": "[ˈpɒdkɑːst]", "pos": "명사", "meaning": "팟캐스트 방송"},
        {"word": "educational", "ipa": "[ˌedʒuˈkeɪʃənl]", "pos": "형용사", "meaning": "교육적인"},
        {"word": "knowledge", "ipa": "[ˈnɒlɪdʒ]", "pos": "명사", "meaning": "지식, 정보"},
        {"word": "multitask", "ipa": "[ˌmʌltiˈtɑːsk]", "pos": "동사", "meaning": "동시에 여러 일을 하다"}
    ],
    39: [
        {"word": "live concert", "ipa": "[laɪv ˈkɒnsət]", "pos": "명사구", "meaning": "라이브 콘서트"},
        {"word": "performance", "ipa": "[pəˈfɔːməns]", "pos": "명사", "meaning": "공연, 연주"},
        {"word": "unforgettable", "ipa": "[ˌʌnfəˈɡetəbl]", "pos": "형용사", "meaning": "잊을 수 없는"},
        {"word": "enthusiasm", "ipa": "[ɪnˈθjuːziæzəm]", "pos": "명사", "meaning": "열정, 열광"}
    ],
    40: [
        {"word": "currently", "ipa": "[ˈkʌrəntli]", "pos": "부사", "meaning": "현재, 지금"},
        {"word": "friendly", "ipa": "[ˈfrendli]", "pos": "형용사", "meaning": "다정한, 친근한"},
        {"word": "affection", "ipa": "[əˈfekʃn]", "pos": "명사", "meaning": "애정, 사랑"},
        {"word": "pet dog", "ipa": "[pet dɒɡ]", "pos": "명사구", "meaning": "반려견"}
    ],
    41: [
        {"word": "benefit", "ipa": "[ˈbenɪfɪt]", "pos": "명사", "meaning": "장점, 혜택"},
        {"word": "comforting", "ipa": "[ˈkʌmfətɪŋ]", "pos": "형용사", "meaning": "위로가 되는"},
        {"word": "companion", "ipa": "[kəmˈpæniən]", "pos": "명사", "meaning": "반려동물, 동반자"},
        {"word": "good mood", "ipa": "[ɡʊd muːd]", "pos": "명사구", "meaning": "좋은 기분"}
    ],
    42: [
        {"word": "responsibility", "ipa": "[rɪˌspɒnsəˈbɪləti]", "pos": "명사", "meaning": "책임, 의무"},
        {"word": "veterinarian (vet)", "ipa": "[ˌvetərɪˈneəriən]", "pos": "명사", "meaning": "수의사, 동물병원"},
        {"word": "essential", "ipa": "[ɪˈsenʃl]", "pos": "형용사", "meaning": "필수적인, 극히 중요한"},
        {"word": "healthcare", "ipa": "[ˈhelθkeə(r)]", "pos": "명사", "meaning": "건강 관리"}
    ],
    43: [
        {"word": "recycle", "ipa": "[ˌriːˈsaɪkl]", "pos": "동사", "meaning": "재활용하다, 분리수거하다"},
        {"word": "cardboard box", "ipa": "[ˈkɑːdbɔːd bɒks]", "pos": "명사구", "meaning": "종이 박스"},
        {"word": "plastic bottle", "ipa": "[ˈplæstɪk ˈbɒtl]", "pos": "명사구", "meaning": "플라스틱 병"},
        {"word": "separate", "ipa": "[ˈsepəreɪt]", "pos": "동사", "meaning": "분리하다, 분류하다"}
    ],
    44: [
        {"word": "reusable bag", "ipa": "[ˌriːˈjuːzəbl bæɡ]", "pos": "명사구", "meaning": "다회용 장바구니"},
        {"word": "protect environment", "ipa": "[prəˈtekt ɪnˈvaɪrənmənt]", "pos": "동사구", "meaning": "환경을 보호하다"},
        {"word": "reduce waste", "ipa": "[rɪˈdjuːs weɪst]", "pos": "동사구", "meaning": "쓰레기를 줄이다"},
        {"word": "eco-friendly", "ipa": "[ˌiːkəʊ ˈfrendli]", "pos": "형용사", "meaning": "친환경적인"}
    ],
    45: [
        {"word": "encourage", "ipa": "[ɪnˈkʌrɪdʒ]", "pos": "동사", "meaning": "권장하다, 독려하다"},
        {"word": "financial benefit", "ipa": "[faɪˈnænʃl ˈbenɪfɪt]", "pos": "명사구", "meaning": "금전적 혜택"},
        {"word": "public awareness", "ipa": "[ˈpʌblɪk əˈweənəs]", "pos": "명사구", "meaning": "대중적 인식"},
        {"word": "effective", "ipa": "[ɪˈfektɪv]", "pos": "형용사", "meaning": "효과적인"}
    ]
}

# Update sentences with clear line breaks for readability
for item in data:
    item_id = item["id"]
    
    # Enrich vocabulary
    if item_id in vocab_enrichment:
        item["vocabulary"] = vocab_enrichment[item_id]
        
    # Format Answer with clean line breaks (\n\n) between sentences
    ans = item["answer"]
    # Replace period + space with period + newline
    # Make sure common acronyms or decimals don't break incorrectly
    sentences = [s.strip() for s in ans.split(". ") if s.strip()]
    formatted_ans = ".\n\n".join(sentences)
    if not formatted_ans.endswith('.'):
        formatted_ans += '.'
    item["answer"] = formatted_ans

    # Format Korean translation with line breaks
    ko = item["answerTranslation"]
    ko_sentences = [s.strip() for s in ko.split(". ") if s.strip()]
    formatted_ko = ".\n\n".join(ko_sentences)
    if not formatted_ko.endswith('.'):
        formatted_ko += '.'
    item["answerTranslation"] = formatted_ko

# Write back
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json successfully updated with sentence line-breaks and 3-5 vocab items each!")
