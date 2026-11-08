#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/expand_dataset_2x.py
- 파트 1~5 전 파트 문항 수를 정확히 2배로 확장 (총 92문항 ➔ 184문항)
  * Part 1: 10문항 ➔ 20문항 (#01 ~ #20)
  * Part 2: 10문항 ➔ 20문항 (#01 ~ #20, git 71b8f33의 실제 시험 고화질 Base64 사진 10장 추가 매핑)
  * Part 3: 30문항 ➔ 60문항 (#01 ~ #60, 5개 유형 × 12문항)
  * Part 4: 8세트(32문항) ➔ 16세트(64문항, 8개 표 속성 × 2세트 × 4문항)
  * Part 5: 10문항 ➔ 20문항 (#01 ~ #20)
- Part 3 유형 탭 문구 간소화: 전체 / 시점 최근 경험 / 빈도 장소 동행인 / 양자택일 선호도 찬반 / 3자택일 최적 선택 / 장단점 중요 이유
- Part 4 표 속성 탭 문구 간소화: '전체 표 속성 (...)' ➔ '전체' 및 각 속성명 정리
"""

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER_JSON_PATH = ROOT / "data" / "toeic_parts_master.json"


def load_git_71b8f33_part2_images():
    """git 71b8f33 커밋에서 실제 시험 고화질 Base64 사진 데이터를 가져옵니다."""
    raw = subprocess.check_output(["git", "show", "71b8f33:data.json"])
    data = json.loads(raw)
    img_map = {}
    for item in data.get("part2", []):
        sid = item.get("setNumber")
        img_map[sid] = item.get("imageUrl", "")
    return img_map


def get_new_part1_items():
    return [
        {
            "id": "p1-11",
            "part": 1,
            "qNum": "#11",
            "category": "공항 체크인 안내",
            "topic": "Boston International Airport - Check-in & Luggage Guide",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Welcome to the Boston International Airport.",
                    "chunking": "Welcome / to the Boston International Airport. ↘",
                    "ko": "보스턴 국제공항에 오신 것을 환영합니다."
                },
                {
                    "en": "Your check-in process will take approximately ten to fifteen minutes.",
                    "chunking": "Your check-in process / will take approximately ten to fifteen minutes. ↘",
                    "ko": "수속 절차는 약 10분에서 15분 정도 소요될 예정입니다."
                },
                {
                    "en": "In order to speed up the process, please have your identification and boarding pass ready as you approach the counter.",
                    "chunking": "In order to speed up the process, / please have your identification and boarding pass ready / as you approach the counter. ↘",
                    "ko": "빠른 수속을 위해 카운터로 다가오실 때 신분증과 탑승권을 미리 준비해 주시기 바랍니다."
                },
                {
                    "en": "Also, please make sure your luggage is clearly labeled with your name↑, address↑, and telephone number↘.",
                    "chunking": "Also, / please make sure your luggage is clearly labeled / with your name↑, address↑, and telephone number↘.",
                    "ko": "또한 수하물에 성함, 주소, 그리고 전화번호 라벨이 명확히 부착되어 있는지 확인해 주세요."
                }
            ],
            "vocabulary": [
                {"word": "approximately", "ipa": "[əˈprɑːksɪmətli]", "pos": "부사", "meaning": "대략, 약"},
                {"word": "identification", "ipa": "[aɪˌdentɪfɪˈkeɪʃn]", "pos": "명사", "meaning": "신분증"},
                {"word": "approach", "ipa": "[əˈproʊtʃ]", "pos": "동사", "meaning": "다가가다, 접근하다"},
                {"word": "luggage", "ipa": "[ˈlʌɡɪdʒ]", "pos": "명사", "meaning": "수하물, 여행 가방"}
            ],
            "readingTips": "마지막 문장의 병렬 나열 name(↗), address(↗), and telephone number(↘)에서 억양의 높낮이를 명확히 살려 읽어주세요."
        },
        {
            "id": "p1-12",
            "part": 1,
            "qNum": "#12",
            "category": "고속버스 휴게소 안내",
            "topic": "Fast Brothers Bus Service - Travel Plaza Rest Stop",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Attention, Fast Brothers Bus passengers.",
                    "chunking": "Attention, / Fast Brothers Bus passengers. ↘",
                    "ko": "패스트 브라더스 버스 승객 여러분, 주목해 주시기 바랍니다."
                },
                {
                    "en": "In a few minutes, we will be making a quick stop at the Westport Travel Plaza.",
                    "chunking": "In a few minutes, / we will be making a quick stop / at the Westport Travel Plaza. ↘",
                    "ko": "잠시 후 저희 버스는 웨스트포트 여행자 휴게소에 잠시 정차할 예정입니다."
                },
                {
                    "en": "At the plaza, you will find restaurants↑, coffee shops↑, and a convenience store↘.",
                    "chunking": "At the plaza, / you will find restaurants↑, / coffee shops↑, / and a convenience store↘.",
                    "ko": "휴게소에는 식당, 커피숍, 그리고 편의점이 마련되어 있습니다."
                },
                {
                    "en": "Because staying on schedule is very important, we request that you return to the bus within fifteen minutes.",
                    "chunking": "Because staying on schedule is very important, / we request that you return to the bus / within fifteen minutes. ↘",
                    "ko": "정시 운행이 매우 중요하므로 15분 이내에 버스로 돌아와 주시기를 부탁드립니다."
                }
            ],
            "vocabulary": [
                {"word": "passengers", "ipa": "[ˈpæsɪndʒərz]", "pos": "명사", "meaning": "승객들"},
                {"word": "convenience store", "ipa": "[kənˈviːniəns stɔːr]", "pos": "명사", "meaning": "편의점"},
                {"word": "schedule", "ipa": "[ˈskedʒuːl]", "pos": "명사", "meaning": "일정, 스케줄"},
                {"word": "within", "ipa": "[wɪˈðɪn]", "pos": "전치사", "meaning": "~이내에"}
            ],
            "readingTips": "fifteen minutes는 [피프틴]에서 뒷음절 -teen에 강세를 주어 fifty(50)와 명확히 구분되게 발음하세요."
        },
        {
            "id": "p1-13",
            "part": 1,
            "qNum": "#13",
            "category": "비즈니스 워크숍 환영사",
            "topic": "Maxview Business Workshop - Entrepreneurship Seminar",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Thank you for attending the Maxview Business Workshop.",
                    "chunking": "Thank you for attending / the Maxview Business Workshop. ↘",
                    "ko": "맥스뷰 비즈니스 워크숍에 참석해 주셔서 감사합니다."
                },
                {
                    "en": "In today's session, we will learn practical strategies on how to start your own business.",
                    "chunking": "In today's session, / we will learn practical strategies / on how to start your own business. ↘",
                    "ko": "오늘 세션에서 우리는 나만의 사업을 시작하는 실용적인 전략들을 배울 것입니다."
                },
                {
                    "en": "Each lecture will help you develop creative ideas for designing↑, producing↑, and marketing your products↘.",
                    "chunking": "Each lecture will help you develop creative ideas / for designing↑, producing↑, and marketing your products↘.",
                    "ko": "각 강의는 제품 디자인, 생산, 그리고 마케팅을 위한 창의적인 아이디어를 발전시키는 데 도움을 줄 것입니다."
                },
                {
                    "en": "At the end of the day, we will award the Brighton Business Prize to the most innovative proposal.",
                    "chunking": "At the end of the day, / we will award the Brighton Business Prize / to the most innovative proposal. ↘",
                    "ko": "오늘 일과 끝에는 가장 혁신적인 제안서에 브라이튼 비즈니스 상을 수여할 예정입니다."
                }
            ],
            "vocabulary": [
                {"word": "practical", "ipa": "[ˈpræktɪkl]", "pos": "형용사", "meaning": "실용적인, 실무적인"},
                {"word": "strategies", "ipa": "[ˈstrætədʒiz]", "pos": "명사", "meaning": "전략들"},
                {"word": "innovative", "ipa": "[ˈɪnəveɪtɪv]", "pos": "형용사", "meaning": "혁신적인"},
                {"word": "proposal", "ipa": "[prəˈpoʊzl]", "pos": "명사", "meaning": "제안서, 기획안"}
            ],
            "readingTips": "동명사 병렬 구문인 designing(↗), producing(↗), and marketing(↘)에서 리듬감 있게 끊어 읽으세요."
        },
        {
            "id": "p1-14",
            "part": 1,
            "qNum": "#14",
            "category": "도서관 마감 안내 방송",
            "topic": "Central City Public Library - Closing Announcement",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "May I have your attention, please, all library patrons.",
                    "chunking": "May I have your attention, please, / all library patrons. ↘",
                    "ko": "도서관 이용객 여러분, 잠시 주목해 주시기 바랍니다."
                },
                {
                    "en": "The Central City Public Library will be closing in twenty minutes at 9:00 PM.",
                    "chunking": "The Central City Public Library / will be closing in twenty minutes / at nine P.M. ↘",
                    "ko": "센트럴 시티 공공도서관은 20분 후인 오후 9시에 문을 닫습니다."
                },
                {
                    "en": "If you would like to borrow books↑, magazines↑, or DVDs↘, please bring them to the first-floor checkout desk now.",
                    "chunking": "If you would like to borrow books↑, magazines↑, or DVDs↘, / please bring them / to the first-floor checkout desk now. ↘",
                    "ko": "도서, 잡지, 또는 DVD를 대출하시려면 지금 1층 대출 데스크로 가져와 주시기 바랍니다."
                },
                {
                    "en": "Please remember to take all of your personal belongings with you before leaving the building.",
                    "chunking": "Please remember to take / all of your personal belongings with you / before leaving the building. ↘",
                    "ko": "건물을 나가시기 전에 모든 개인 소지품을 챙기셨는지 꼭 확인하시기 바랍니다."
                }
            ],
            "vocabulary": [
                {"word": "patrons", "ipa": "[ˈpeɪtrənz]", "pos": "명사", "meaning": "이용객, 고객"},
                {"word": "borrow", "ipa": "[ˈbɑːroʊ]", "pos": "동사", "meaning": "빌리다, 대출하다"},
                {"word": "checkout desk", "ipa": "[ˈtʃekaʊt desk]", "pos": "명사", "meaning": "대출 창구, 계산대"},
                {"word": "belongings", "ipa": "[bɪˈlɔːŋɪŋz]", "pos": "명사", "meaning": "소지품"}
            ],
            "readingTips": "DVDs는 [디-브이-디즈]로 끝의 복수형 [z] 발음을 놓치지 말고 부드럽게 내려 읽으세요."
        },
        {
            "id": "p1-15",
            "part": 1,
            "qNum": "#15",
            "category": "가전제품 라디오 광고",
            "topic": "CleanWave Robo-Vacuum - Smart Home Commercial",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Are you tired of spending your entire weekend cleaning the house? ↑",
                    "chunking": "Are you tired of spending your entire weekend / cleaning the house? ↑",
                    "ko": "주말 내내 집안 청소를 하느라 지치셨나요?"
                },
                {
                    "en": "Meet the all-new CleanWave Robot Vacuum, your ultimate smart home assistant!",
                    "chunking": "Meet the all-new CleanWave Robot Vacuum, / your ultimate smart home assistant! ↘",
                    "ko": "최고의 스마트 홈 도우미, 완전히 새로워진 클린웨이브 로봇 청소기를 만나보세요!"
                },
                {
                    "en": "With powerful suction, quiet operation, and smart mapping technology, it cleans carpets↑, hardwood floors↑, and tiles↘ effortlessly.",
                    "chunking": "With powerful suction, / quiet operation, / and smart mapping technology, / it cleans carpets↑, hardwood floors↑, and tiles↘ effortlessly.",
                    "ko": "강력한 흡입력, 조용한 작동, 스마트 매핑 기술로 카펫, 원목 마루, 타일을 손쉽게 청소합니다."
                },
                {
                    "en": "Visit our official website this week to claim a free replacement filter kit with your order!",
                    "chunking": "Visit our official website this week / to claim a free replacement filter kit / with your order! ↘",
                    "ko": "이번 주 공식 웹사이트를 방문해 주문 시 무료 교체용 필터 키트를 받아 가세요!"
                }
            ],
            "vocabulary": [
                {"word": "vacuum", "ipa": "[ˈvækjuːm]", "pos": "명사", "meaning": "진공청소기"},
                {"word": "suction", "ipa": "[ˈsʌkʃn]", "pos": "명사", "meaning": "흡입(력)"},
                {"word": "effortlessly", "ipa": "[ˈefərtləsli]", "pos": "부사", "meaning": "손쉽게, 수월하게"},
                {"word": "replacement", "ipa": "[rɪˈpleɪsmənt]", "pos": "명사", "meaning": "교체, 대체품"}
            ],
            "readingTips": "첫 문장은 Be동사 의문문(Are you tired of ~?)이므로 문장 끝을 확실히 올려(↗) 호기심을 유발하듯 읽으세요."
        },
        {
            "id": "p1-16",
            "part": 1,
            "qNum": "#16",
            "category": "기차역 승강장 변경 방송",
            "topic": "Metro Rail Express - Platform Change Notice",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Attention all passengers waiting for the 9:15 Metro Express train to Chicago.",
                    "chunking": "Attention all passengers / waiting for the nine-fifteen Metro Express train / to Chicago. ↘",
                    "ko": "시카고행 9시 15분 메트로 급행열차를 기다리시는 승객 여러분께 안내 말씀드립니다."
                },
                {
                    "en": "Due to a track maintenance issue, your train will now depart from Platform 7 instead of Platform 3.",
                    "chunking": "Due to a track maintenance issue, / your train will now depart from Platform seven / instead of Platform three. ↘",
                    "ko": "선로 점검 문제로 인해 해당 열차는 3번 승강장 대신 7번 승강장에서 출발합니다."
                },
                {
                    "en": "Passengers with heavy suitcases↑, strollers↑, or wheelchairs↘ may use the elevators located near the main ticket booth.",
                    "chunking": "Passengers with heavy suitcases↑, strollers↑, or wheelchairs↘ / may use the elevators / located near the main ticket booth. ↘",
                    "ko": "무거운 여행 가방, 유모차, 또는 휠체어를 이용하시는 승객께서는 중앙 매표소 근처 엘리베이터를 이용하실 수 있습니다."
                },
                {
                    "en": "We apologize for any inconvenience and appreciate your cooperation.",
                    "chunking": "We apologize for any inconvenience / and appreciate your cooperation. ↘",
                    "ko": "불편을 끼쳐 드려 죄송하며 협조해 주셔서 감사합니다."
                }
            ],
            "vocabulary": [
                {"word": "maintenance", "ipa": "[ˈmeɪntənəns]", "pos": "명사", "meaning": "보수, 점검, 유지관리"},
                {"word": "depart", "ipa": "[dɪˈpɑːrt]", "pos": "동사", "meaning": "출발하다"},
                {"word": "inconvenience", "ipa": "[ˌɪnkənˈviːniəns]", "pos": "명사", "meaning": "불편"},
                {"word": "cooperation", "ipa": "[koʊˌɑːpəˈreɪʃn]", "pos": "명사", "meaning": "협조, 협력"}
            ],
            "readingTips": "Platform 7과 Platform 3은 대조되는 핵심 정보이므로 숫자 seven과 three에 강한 강세를 넣어 읽어주세요."
        },
        {
            "id": "p1-17",
            "part": 1,
            "qNum": "#17",
            "category": "요리 클래스 오리엔테이션",
            "topic": "Star Culinary Academy - Italian Cooking Class",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Welcome to Star Culinary Academy! We are thrilled to have you in our beginner's Italian cooking class.",
                    "chunking": "Welcome to Star Culinary Academy! / We are thrilled to have you / in our beginner's Italian cooking class. ↘",
                    "ko": "스타 요리 아카데미에 오신 것을 환영합니다! 초급 이탈리아 요리 수업에 함께하게 되어 매우 기쁩니다."
                },
                {
                    "en": "Today, Chef Marco will show you how to make fresh pasta dough and authentic tomato basil sauce from scratch.",
                    "chunking": "Today, / Chef Marco will show you / how to make fresh pasta dough / and authentic tomato basil sauce from scratch. ↘",
                    "ko": "오늘 마르코 셰프님이 신선한 파스타 반죽과 정통 토마토 바질 소스를 처음부터 직접 만드는 법을 보여드릴 것입니다."
                },
                {
                    "en": "On your workstation, you will find flour↑, olive oil↑, garlic↑, and fresh herbs↘.",
                    "chunking": "On your workstation, / you will find flour↑, olive oil↑, garlic↑, and fresh herbs↘.",
                    "ko": "조리대 위에는 밀가루, 올리브 오일, 마늘, 그리고 신선한 허브가 준비되어 있습니다."
                },
                {
                    "en": "Before we begin, please put on your apron and wash your hands thoroughly at the sink.",
                    "chunking": "Before we begin, / please put on your apron / and wash your hands thoroughly at the sink. ↘",
                    "ko": "시작하기 전에 앞치마를 착용하시고 싱크대에서 손을 깨끗이 씻어 주시기 바랍니다."
                }
            ],
            "vocabulary": [
                {"word": "culinary", "ipa": "[ˈkʌlɪneri]", "pos": "형용사", "meaning": "요리의, 주방의"},
                {"word": "authentic", "ipa": "[ɔːˈθentɪk]", "pos": "형용사", "meaning": "정통의, 진짜의"},
                {"word": "dough", "ipa": "[doʊ]", "pos": "명사", "meaning": "밀가루 반죽 (묵음 gh 주의)"},
                {"word": "thoroughly", "ipa": "[ˈθɜːroʊli]", "pos": "부사", "meaning": "철저히, 꼼꼼하게"}
            ],
            "readingTips": "dough는 [도우], thoroughly는 [써러울리]로 발음합니다. 특히 묵음 gh가 들어간 단어에 주의하세요."
        },
        {
            "id": "p1-18",
            "part": 1,
            "qNum": "#18",
            "category": "병원 고객센터 ARS 안내",
            "topic": "Green Valley Medical Clinic - Automated Voicemail",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Thank you for calling the Green Valley Medical Clinic.",
                    "chunking": "Thank you for calling / the Green Valley Medical Clinic. ↘",
                    "ko": "그린 밸리 메디컬 클리닉에 전화해 주셔서 감사합니다."
                },
                {
                    "en": "Our regular clinic hours are Monday through Friday from 8:30 AM to 6:00 PM, and Saturday from 9:00 AM to 1:00 PM.",
                    "chunking": "Our regular clinic hours / are Monday through Friday from eight-thirty A.M. to six P.M., / and Saturday from nine A.M. to one P.M. ↘",
                    "ko": "저희 정규 진료 시간은 월요일부터 금요일 오전 8시 30분부터 오후 6시까지, 토요일은 오전 9시부터 오후 1시까지입니다."
                },
                {
                    "en": "If you are calling to schedule an appointment↑, check test results↑, or request a prescription refill↘, please press one now.",
                    "chunking": "If you are calling to schedule an appointment↑, / check test results↑, / or request a prescription refill↘, / please press one now.",
                    "ko": "진료 예약, 검사 결과 확인, 또는 처방전 재발급을 요청하시려면 지금 1번을 눌러 주세요."
                },
                {
                    "en": "To speak directly with a nurse or receptionist, please stay on the line and someone will assist you shortly.",
                    "chunking": "To speak directly with a nurse or receptionist, / please stay on the line / and someone will assist you shortly. ↘",
                    "ko": "간호사나 접수처 직원과 직접 통화하시려면 끊지 말고 기다려 주시면 곧 안내해 드리겠습니다."
                }
            ],
            "vocabulary": [
                {"word": "appointment", "ipa": "[əˈpɔɪntmənt]", "pos": "명사", "meaning": "예약, 약속"},
                {"word": "prescription", "ipa": "[prɪˈskrɪpʃn]", "pos": "명사", "meaning": "처방전"},
                {"word": "receptionist", "ipa": "[rɪˈsepʃənɪst]", "pos": "명사", "meaning": "접수 담당 직원"},
                {"word": "assist", "ipa": "[əˈsɪst]", "pos": "동사", "meaning": "돕다, 안내하다"}
            ],
            "readingTips": "ARS 안내문은 차분하고 또렷한 콜센터 톤으로 읽고, 8:30 AM(eight-thirty A.M.) 같은 시각 표현을 막힘없이 읽으세요."
        },
        {
            "id": "p1-19",
            "part": 1,
            "qNum": "#19",
            "category": "마라톤 행사 출발 안내",
            "topic": "10th Annual City Charity Marathon - Pre-race Briefing",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Good morning, runners, and welcome to the 10th Annual City Charity Marathon!",
                    "chunking": "Good morning, runners, / and welcome to the tenth Annual City Charity Marathon! ↘",
                    "ko": "참가자 여러분, 좋은 아침입니다! 제10회 연례 시티 자선 마라톤 대회에 오신 것을 환영합니다!"
                },
                {
                    "en": "Thanks to your generous registration fees, we have raised over 50,000 dollars for local children's hospitals.",
                    "chunking": "Thanks to your generous registration fees, / we have raised over fifty thousand dollars / for local children's hospitals. ↘",
                    "ko": "여러분의 따뜻한 참가비 덕분에 지역 어린이 병원을 위해 5만 달러 이상의 기금을 모금했습니다."
                },
                {
                    "en": "Along the race course, volunteers will hand out water↑, energy drinks↑, and fresh fruit↘ every three kilometers.",
                    "chunking": "Along the race course, / volunteers will hand out water↑, energy drinks↑, and fresh fruit↘ / every three kilometers.",
                    "ko": "마라톤 코스 내내 자원봉사자들이 3킬로미터마다 생수, 에너지 음료, 그리고 신선한 과일을 나눠드릴 예정입니다."
                },
                {
                    "en": "Please line up at the starting gate according to your pace group, and have a safe, enjoyable run!",
                    "chunking": "Please line up at the starting gate / according to your pace group, / and have a safe, enjoyable run! ↘",
                    "ko": "본인의 페이스 그룹에 맞춰 출발선에 줄을 서 주시고, 안전하고 즐거운 레이스 되시길 바랍니다!"
                }
            ],
            "vocabulary": [
                {"word": "charity", "ipa": "[ˈtʃærəti]", "pos": "명사", "meaning": "자선 (단체/행사)"},
                {"word": "generous", "ipa": "[ˈdʒenərəs]", "pos": "형용사", "meaning": "후한, 너그러운"},
                {"word": "volunteers", "ipa": "[ˌvɑːlənˈtɪrz]", "pos": "명사", "meaning": "자원봉사자들"},
                {"word": "kilometers", "ipa": "[kɪˈlɑːmɪtərz]", "pos": "명사", "meaning": "킬로미터"}
            ],
            "readingTips": "50,000 dollars는 [피프티 싸우전드 달러즈]로 읽으며, 야외 행사 진행자처럼 활기차고 에너지 넘치는 톤을 유지하세요."
        },
        {
            "id": "p1-20",
            "part": 1,
            "qNum": "#20",
            "category": "사내 IT 서버 점검 공지",
            "topic": "Corporate IT Department - Weekend System Upgrade",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Attention all employees. This is an important announcement from the IT Support Department.",
                    "chunking": "Attention all employees. ↘ / This is an important announcement / from the IT Support Department. ↘",
                    "ko": "전 임직원 여러분께 알립니다. IT 지원 부서에서 중요 공지사항을 전달해 드립니다."
                },
                {
                    "en": "Starting this Friday at 8:00 PM, we will be performing a scheduled security upgrade on our internal servers.",
                    "chunking": "Starting this Friday at eight P.M., / we will be performing a scheduled security upgrade / on our internal servers. ↘",
                    "ko": "이번 주 금요일 오후 8시부터 사내 서버에 대한 정기 보안 업그레이드 작업을 진행할 예정입니다."
                },
                {
                    "en": "During the maintenance window, access to company email↑, cloud storage↑, and the employee portal↘ will be temporarily unavailable.",
                    "chunking": "During the maintenance window, / access to company email↑, cloud storage↑, and the employee portal↘ / will be temporarily unavailable.",
                    "ko": "점검 시간 동안 사내 이메일, 클라우드 스토리지, 그리고 직원 포털 접속이 일시적으로 제한됩니다."
                },
                {
                    "en": "Please save all of your active documents and log out of your computers before leaving the office on Friday.",
                    "chunking": "Please save all of your active documents / and log out of your computers / before leaving the office on Friday. ↘",
                    "ko": "금요일 퇴근 전 작업 중인 모든 문서를 저장하시고 컴퓨터에서 로그아웃해 주시기 바랍니다."
                }
            ],
            "vocabulary": [
                {"word": "scheduled", "ipa": "[ˈskedʒuːld]", "pos": "형용사", "meaning": "예정된, 정기적인"},
                {"word": "internal", "ipa": "[ɪnˈtɜːrnl]", "pos": "형용사", "meaning": "내부의, 사내의"},
                {"word": "temporarily", "ipa": "[ˌtempəˈrerəli]", "pos": "부사", "meaning": "일시적으로"},
                {"word": "unavailable", "ipa": "[ˌʌnəˈveɪləbl]", "pos": "형용사", "meaning": "이용할 수 없는"}
            ],
            "readingTips": "temporarily unavailable [템퍼레럴리 언어베일러블] 구간은 발음이 꼬이기 쉬우므로 두 단어를 또박또박 끊어 읽으세요."
        }
    ]


def get_new_part2_items(img_map):
    """git 71b8f33의 실제 시험 고화질 Base64 사진 10장(Set 3, 5, 11, 13, 15, 16, 17, 19, 24, 26)을 #11~#20으로 매핑"""
    return [
        {
            "id": "p2-11",
            "part": 2,
            "qNum": "#11",
            "category": "카페·레스토랑 라운지",
            "topic": "카페 창가 소파 좌석 태블릿 사용 및 음료 휴식 (Cafe & Lounge)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[3],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at an indoor cafe or a restaurant lounge.", "ko": "이 사진은 실내 카페나 레스토랑 라운지에서 찍힌 사진입니다."},
                {"step": "2. 오른쪽 인물 묘사", "en": "On the right side of the picture, a woman wearing a red blouse is sitting on a sofa and looking at a tablet PC.", "ko": "사진 오른쪽에는 빨간 블라우스를 입은 여성이 소파에 앉아 태블릿 PC를 보고 있습니다."},
                {"step": "3. 왼쪽 인물 및 테이블", "en": "On the left side, a man in a dark suit and tie is sitting at a small round table with a glass on it.", "ko": "왼쪽에는 어두운 정장과 넥타이를 맨 남성이 유리잔이 놓인 작은 원형 테이블에 앉아 있습니다."},
                {"step": "4. 배경 및 분위기 마무리", "en": "In the background, there are potted plants by the large window, and the atmosphere looks calm and relaxing.", "ko": "배경에는 큰 창문 옆으로 화분들이 놓여 있고, 분위기는 차분하고 여유로워 보입니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken at a cafe.", "ko": "이 사진은 카페에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #010 (카페/식당 첫 문장)"},
                {"en": "She is sitting on a sofa and using a tablet PC.", "ko": "그녀는 소파에 앉아 태블릿 PC를 사용하고 있습니다.", "tip": "시계토끼 만능 #046 (전자기기 사용 동작)"}
            ],
            "vocabulary": [
                {"word": "lounge", "ipa": "[laʊndʒ]", "pos": "명사", "meaning": "라운지, 휴게실"},
                {"word": "tablet PC", "ipa": "[ˈtæblət ˌpiːˈsiː]", "pos": "명사", "meaning": "태블릿 컴퓨터"},
                {"word": "potted plant", "ipa": "[ˈpɑːtɪd plænt]", "pos": "명사구", "meaning": "화분에 심은 식물"}
            ],
            "explanation": "창가 소파에 앉아 있는 남녀 2인을 왼쪽(a man in a suit)과 오른쪽(a woman in a red blouse using a tablet PC)으로 나누어 묘사하면 30초를 완벽히 채울 수 있습니다."
        },
        {
            "id": "p2-12",
            "part": 2,
            "qNum": "#12",
            "category": "회의실·비즈니스 미팅",
            "topic": "벽돌 인테리어 회의실 여성 2인 노트북·필기 대화 (Office Meeting)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[5],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken in a meeting room at an office.", "ko": "이 사진은 사무실 회의실에서 찍힌 사진입니다."},
                {"step": "2. 왼쪽 인물 묘사", "en": "On the left side, a woman wearing glasses and a blue shirt is holding a pen and taking notes in a notebook.", "ko": "왼쪽에는 안경과 파란 셔츠를 입은 여성이 펜을 들고 공책에 필기를 하고 있습니다."},
                {"step": "3. 오른쪽 인물 묘사", "en": "On the right side, another woman in a black jacket is sitting in front of an open laptop and talking with a smile.", "ko": "오른쪽에는 검은 재킷을 입은 다른 여성이 열린 노트북 앞에 앉아 미소 지으며 이야기하고 있습니다."},
                {"step": "4. 배경 및 분위기 마무리", "en": "In the background, there is a brick wall, and they seem to be having a friendly business discussion.", "ko": "배경에는 벽돌 벽이 보이고, 두 사람은 화기애애한 업무 논의를 나누는 것처럼 보입니다."}
            ],
            "magicSentences": [
                {"en": "She is taking notes in a notebook.", "ko": "그녀는 공책에 필기를 하고 있습니다.", "tip": "시계토끼 만능 #048 (사무실/교실 필기 동작)"},
                {"en": "They are having a conversation at a wooden table.", "ko": "그들은 나무 테이블에서 대화를 나누고 있습니다.", "tip": "시계토끼 만능 #095 (테이블 대화 만능 표현)"}
            ],
            "vocabulary": [
                {"word": "take notes", "ipa": "[teɪk noʊts]", "pos": "숙어", "meaning": "필기하다, 메모하다"},
                {"word": "brick wall", "ipa": "[brɪk wɔːl]", "pos": "명사구", "meaning": "벽돌 벽"},
                {"word": "discussion", "ipa": "[dɪˈskʌʃn]", "pos": "명사", "meaning": "논의, 토의"}
            ],
            "explanation": "2인 구도 사진의 정석입니다. 왼쪽 여성(wearing glasses, taking notes)과 오른쪽 여성(wearing a black jacket, using a laptop)의 동작을 대비해 묘사하세요."
        },
        {
            "id": "p2-13",
            "part": 2,
            "qNum": "#13",
            "category": "베이커리·매장 카운터",
            "topic": "베이커리 카운터 앞치마 직원 및 태블릿 업무 대화 (Bakery Counter)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[11],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at a bakery or a coffee shop counter.", "ko": "이 사진은 베이커리나 커피숍 카운터에서 찍힌 사진입니다."},
                {"step": "2. 왼쪽 인물 묘사", "en": "On the left side, a man wearing a blue shirt and a red apron is leaning on the counter and listening carefully.", "ko": "왼쪽에는 파란 셔츠에 빨간 앞치마를 착용한 남성이 카운터에 기대어 주의 깊게 듣고 있습니다."},
                {"step": "3. 오른쪽 인물 묘사", "en": "Next to him, a woman in a white top is holding a tablet PC in one hand and explaining something to the man.", "ko": "그 옆에는 흰 상의를 입은 여성이 한 손에 태블릿 PC를 들고 남성에게 무언가를 설명하고 있습니다."},
                {"step": "4. 배경 사물 마무리", "en": "In the foreground, there is a display case with bread, and various bottles and boxes are arranged on the shelves behind them.", "ko": "전경에는 빵이 든 진열장이 있고, 그들 뒤쪽 선반에는 다양한 병과 상자들이 진열되어 있습니다."}
            ],
            "magicSentences": [
                {"en": "He is wearing an apron and standing behind the counter.", "ko": "그는 앞치마를 입고 카운터 뒤에 서 있습니다.", "tip": "시계토끼 만능 #032 (매장 직원 복장·위치 공식)"},
                {"en": "Various items are displayed on the shelves.", "ko": "선반 위에 다양한 물품들이 진열되어 있습니다.", "tip": "시계토끼 만능 #118 (매장 배경 만능 마무리)"}
            ],
            "vocabulary": [
                {"word": "apron", "ipa": "[ˈeɪprən]", "pos": "명사", "meaning": "앞치마"},
                {"word": "lean on", "ipa": "[liːn ɑːn]", "pos": "숙어", "meaning": "~에 기대다"},
                {"word": "display case", "ipa": "[dɪˈspleɪ keɪs]", "pos": "명사구", "meaning": "진열장, 쇼케이스"}
            ],
            "explanation": "카페·베이커리 직원 사진에서는 apron(앞치마), counter(카운터), display case(진열장), shelves(선반) 4개 어휘만 챙겨도 고득점이 보장됩니다."
        },
        {
            "id": "p2-14",
            "part": 2,
            "qNum": "#14",
            "category": "호텔 리셉션·로비",
            "topic": "호텔 프런트 데스크 여행객 2인 체크인 응대 (Hotel Reception)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[13],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at a hotel reception desk.", "ko": "이 사진은 호텔 리셉션 데스크에서 찍힌 사진입니다."},
                {"step": "2. 카운터 앞 고객 묘사", "en": "In front of the desk, two women with suitcases are standing side by side to check in at the hotel.", "ko": "데스크 앞에는 여행 가방을 든 두 여성이 호텔 체크인을 하기 위해 나란히 서 있습니다."},
                {"step": "3. 카운터 뒤 직원 묘사", "en": "Behind the counter, a hotel clerk wearing a vest and a bow tie is assisting the guests with a smile.", "ko": "카운터 뒤편에서는 조끼와 나비넥타이를 착용한 호텔 직원이 미소를 지으며 손님들을 응대하고 있습니다."},
                {"step": "4. 주변 사물 마무리", "en": "On the counter, there is a pink vase with flowers and a reception sign, and pendant lights are hanging from the ceiling.", "ko": "카운터 위에는 꽃이 꽂힌 분홍색 화병과 리셉션 표지판이 있고, 천장에는 펜던트 조명이 매달려 있습니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken at a hotel lobby.", "ko": "이 사진은 호텔 로비에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #014 (호텔/프런트 첫 문장)"},
                {"en": "A staff member is helping customers at the counter.", "ko": "직원이 카운터에서 고객들을 도와주고 있습니다.", "tip": "시계토끼 만능 #051 (고객 응대 만능 표현)"}
            ],
            "vocabulary": [
                {"word": "reception desk", "ipa": "[rɪˈsepʃn desk]", "pos": "명사구", "meaning": "프런트 데스크, 접수처"},
                {"word": "suitcase", "ipa": "[ˈsuːtkeɪs]", "pos": "명사", "meaning": "여행용 가방, 캐리어"},
                {"word": "check in", "ipa": "[tʃek ɪn]", "pos": "숙어", "meaning": "체크인하다, 탑승 수속하다"}
            ],
            "explanation": "호텔 로비/체크인 사진은 손님(standing with suitcases, checking in)과 직원(standing behind the counter, assisting guests)의 상호작용을 중심으로 묘사하세요."
        },
        {
            "id": "p2-15",
            "part": 2,
            "qNum": "#15",
            "category": "공항·호텔 대기 라운지",
            "topic": "대기 라운지 안락의자 태블릿 사용 및 캐리어 여행객 (Waiting Lounge)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[15],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken in a waiting lounge at a hotel or an airport.", "ko": "이 사진은 호텔이나 공항의 대기 라운지에서 찍힌 사진입니다."},
                {"step": "2. 중심 인물 묘사", "en": "In the center of the picture, a blonde woman wearing a blue vest over a white shirt is sitting in a brown leather armchair.", "ko": "사진 중앙에는 흰 셔츠 위에 파란 조끼를 입은 금발 여성이 갈색 가죽 안락의자에 앉아 있습니다."},
                {"step": "3. 세부 동작 및 주변 인물", "en": "She is looking down and using a tablet PC on her lap, and on the right, another woman is standing with a rolling suitcase.", "ko": "그녀는 무릎 위의 태블릿 PC를 내려다보며 사용하고 있고, 오른쪽에는 다른 여성이 바퀴 달린 캐리어를 잡고 서 있습니다."},
                {"step": "4. 배경 묘사 마무리", "en": "In the background, green trees can be seen through the large glass windows.", "ko": "배경에는 커다란 유리창 너머로 푸른 나무들이 보입니다."}
            ],
            "magicSentences": [
                {"en": "She is sitting in an armchair and looking at a tablet.", "ko": "그녀는 안락의자에 앉아 태블릿을 보고 있습니다.", "tip": "시계토끼 만능 #047 (의자 착석 및 기기 사용)"},
                {"en": "Trees can be seen through the window in the background.", "ko": "배경의 창문 너머로 나무들이 보입니다.", "tip": "시계토끼 만능 #125 (실내 창문 배경 공식)"}
            ],
            "vocabulary": [
                {"word": "waiting lounge", "ipa": "[ˈweɪtɪŋ laʊndʒ]", "pos": "명사구", "meaning": "대기실, 라운지"},
                {"word": "armchair", "ipa": "[ˈɑːrmtʃer]", "pos": "명사", "meaning": "팔걸이가 있는 안락의자"},
                {"word": "on her lap", "ipa": "[ɑːn hɜːr læp]", "pos": "전치사구", "meaning": "그녀의 무릎 위에"}
            ],
            "explanation": "앉아 있는 중심 인물의 복장(blue vest over a white shirt)과 동작(using a tablet on her lap), 그리고 오른쪽의 캐리어(rolling suitcase)를 순서대로 짚어주면 완벽합니다."
        },
        {
            "id": "p2-16",
            "part": 2,
            "qNum": "#16",
            "category": "야외 공원·거리 공연",
            "topic": "도심 공원 악보대 앞 바이올린 연주 및 시민 휴식 (Park Violinist)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[16],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken outdoors at a city park.", "ko": "이 사진은 도심 공원 야외에서 찍힌 사진입니다."},
                {"step": "2. 전경 중심 인물 묘사", "en": "In the foreground on the right, a man wearing a light blue short-sleeved shirt is standing in front of a music stand and playing the violin.", "ko": "전경 오른쪽에는 하늘색 반팔 셔츠를 입은 남성이 보면대 앞에 서서 바이올린을 연주하고 있습니다."},
                {"step": "3. 중경 인물 묘사", "en": "Behind him, a woman is walking along the path, and several people are sitting on the grass and benches enjoying the music.", "ko": "그의 뒤로는 한 여성이 산책로를 따라 걷고 있고, 여러 사람들이 잔디밭과 벤치에 앉아 음악을 감상하고 있습니다."},
                {"step": "4. 배경 묘사 마무리", "en": "In the background, there are tall green trees and city buildings under a clear sky.", "ko": "배경에는 맑은 하늘 아래 키 큰 푸른 나무들과 도시 건물들이 있습니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken outdoors at a park.", "ko": "이 사진은 야외 공원에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #005 (야외 공원 첫 문장)"},
                {"en": "He is playing a musical instrument outdoors.", "ko": "그는 야외에서 악기를 연주하고 있습니다.", "tip": "시계토끼 만능 #068 (거리 공연/악기 연주)"}
            ],
            "vocabulary": [
                {"word": "music stand", "ipa": "[ˈmjuːzɪk stænd]", "pos": "명사구", "meaning": "보면대, 악보대"},
                {"word": "play the violin", "ipa": "[pleɪ ðə ˌvaɪəˈlɪn]", "pos": "숙어", "meaning": "바이올린을 연주하다"},
                {"word": "in the foreground", "ipa": "[ɪn ðə ˈfɔːrɡraʊnd]", "pos": "전치사구", "meaning": "사진의 전경(앞쪽)에"}
            ],
            "explanation": "악기 이름 앞에는 정관사 the를 붙여 'playing the violin'으로 표현하며, 앞쪽 연주자 ➔ 중간 산책객 및 벤치 사람들 ➔ 뒤쪽 나무와 빌딩 순으로 원근감을 살려 묘사하세요."
        },
        {
            "id": "p2-17",
            "part": 2,
            "qNum": "#17",
            "category": "야외 노천카페·테라스",
            "topic": "야외 노천카페 파라솔 및 나무 그늘 아래 손님들 (Outdoor Cafe Terrace)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[17],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at an outdoor cafe terrace.", "ko": "이 사진은 야외 노천카페 테라스에서 찍힌 사진입니다."},
                {"step": "2. 중심 인물들 묘사", "en": "In the middle of the picture, many people are sitting at tables under large white patio umbrellas and green trees.", "ko": "사진 중앙에는 많은 사람들이 커다란 흰색 파라솔과 푸른 나무들 아래 테이블에 앉아 있습니다."},
                {"step": "3. 세부 동작 묘사", "en": "They are having meals, drinking beverages, and chatting with each other.", "ko": "그들은 식사를 하고 음료를 마시며 서로 담소를 나누고 있습니다."},
                {"step": "4. 배경 및 분위기 마무리", "en": "In the background, there are classic brick buildings, and the weather looks sunny and pleasant.", "ko": "배경에는 고풍스러운 벽돌 건물들이 있고, 날씨는 화창하고 쾌적해 보입니다."}
            ],
            "magicSentences": [
                {"en": "People are sitting at outdoor tables under umbrellas.", "ko": "사람들이 파라솔 아래 야외 테이블에 앉아 있습니다.", "tip": "시계토끼 만능 #098 (야외 테라스 식당 공식)"},
                {"en": "The weather looks sunny and pleasant.", "ko": "날씨가 화창하고 기분 좋아 보입니다.", "tip": "시계토끼 만능 #142 (야외 날씨 마무리 공식)"}
            ],
            "vocabulary": [
                {"word": "terrace", "ipa": "[ˈterəs]", "pos": "명사", "meaning": "테라스, 야외 좌석"},
                {"word": "patio umbrella", "ipa": "[ˈpætioʊ ʌmˈbrelə]", "pos": "명사구", "meaning": "야외용 대형 파라솔"},
                {"word": "chat with", "ipa": "[tʃæt wɪð]", "pos": "숙어", "meaning": "~와 담소를 나누다"}
            ],
            "explanation": "여러 사람이 모인 야외 테라스 사진은 특정 한 명을 길게 묘사하기보다 'Many people are sitting at tables under umbrellas, chatting with each other'처럼 그룹 동작으로 묶어주면 훨씬 자연스럽습니다."
        },
        {
            "id": "p2-18",
            "part": 2,
            "qNum": "#18",
            "category": "야외 해변·가족 여가",
            "topic": "해변 파라솔 아래 가족 모래놀이 및 라켓 게임 (Beach Family Activity)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[19],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at a sandy beach on a sunny day.", "ko": "이 사진은 화창한 날 모래 해변에서 찍힌 사진입니다."},
                {"step": "2. 중앙 가족 묘사", "en": "In the middle of the picture, parents and two little girls are sitting on the sand and playing with a yellow bucket and toy shovels.", "ko": "사진 중앙에는 부모와 두 어린 소녀가 모래 위에 앉아 노란 양동이와 장난감 삽을 가지고 놀고 있습니다."},
                {"step": "3. 주변 아이들 묘사", "en": "Next to them, a girl under a striped beach umbrella and a boy in a white T-shirt are holding rackets and playing a beach game.", "ko": "그들 옆에서는 줄무늬 해변 파라솔 아래의 소녀와 흰 티셔츠를 입은 소년이 라켓을 들고 해변 게임을 하고 있습니다."},
                {"step": "4. 배경 바다 마무리", "en": "In the background, blue ocean waves can be seen, and the family is having a wonderful time together.", "ko": "배경에는 푸른 바다 파도가 보이고, 가족들이 함께 즐거운 시간을 보내고 있습니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken at the beach.", "ko": "이 사진은 해변에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #008 (바닷가/휴양지 첫 문장)"},
                {"en": "They are having a good time together on the sand.", "ko": "그들은 모래 위에서 함께 즐거운 시간을 보내고 있습니다.", "tip": "시계토끼 만능 #145 (여가/가족 사진 만능 마무리)"}
            ],
            "vocabulary": [
                {"word": "sandy beach", "ipa": "[ˈsændi biːtʃ]", "pos": "명사구", "meaning": "모래 해변, 백사장"},
                {"word": "striped umbrella", "ipa": "[straɪpt ʌmˈbrelə]", "pos": "명사구", "meaning": "줄무늬 파라솔"},
                {"word": "ocean waves", "ipa": "[ˈoʊʃn weɪvz]", "pos": "명사구", "meaning": "바다 파도"}
            ],
            "explanation": "해변 가족 사진에서는 앉아서 모래놀이를 하는 그룹(sitting on the sand, playing with a bucket)과 서서 라켓 게임을 하는 아이들(standing and holding rackets), 그리고 뒤쪽 바다(blue ocean)를 순서대로 묘사하세요."
        },
        {
            "id": "p2-19",
            "part": 2,
            "qNum": "#19",
            "category": "물류 창고·작업 현장",
            "topic": "물류 창고 작업자 2인 대형 박스 운반 및 지게차 (Logistics Warehouse)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[24],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken inside a large logistics warehouse.", "ko": "이 사진은 대형 물류 창고 내부에서 찍힌 사진입니다."},
                {"step": "2. 중심 작업자 2인 묘사", "en": "In the center of the picture, two men wearing safety glasses and blue work gloves are lifting a large cardboard box together.", "ko": "사진 중앙에는 보안경과 파란 작업용 장갑을 착용한 두 남성이 함께 커다란 종이 상자를 들어 올리고 있습니다."},
                {"step": "3. 복장 및 주변 장비", "en": "The man on the right is wearing a red plaid shirt, and on the left side, there is a red and black forklift.", "ko": "오른쪽 남성은 빨간 체크무늬 셔츠를 입고 있으며, 왼쪽에는 빨간색과 검은색 지게차가 있습니다."},
                {"step": "4. 배경 선반 마무리", "en": "In the background, many boxes are stacked high on metal shelves.", "ko": "배경에는 철제 선반 위에 많은 상자들이 높이 쌓여 있습니다."}
            ],
            "magicSentences": [
                {"en": "Two men are carrying a large cardboard box together.", "ko": "두 남성이 함께 큰 종이 상자를 나르고 있습니다.", "tip": "시계토끼 만능 #062 (작업장 운반 동작 공식)"},
                {"en": "Many boxes are stacked on the shelves in the background.", "ko": "배경의 선반 위에 많은 상자들이 쌓여 있습니다.", "tip": "시계토끼 만능 #120 (창고/매장 적재 배경 공식)"}
            ],
            "vocabulary": [
                {"word": "warehouse", "ipa": "[ˈwerhaʊs]", "pos": "명사", "meaning": "물류 창고"},
                {"word": "cardboard box", "ipa": "[ˈkɑːrdbɔːrd bɑːks]", "pos": "명사구", "meaning": "골판지(종이) 상자"},
                {"word": "forklift", "ipa": "[ˈfɔːrklɪft]", "pos": "명사", "meaning": "지게차"}
            ],
            "explanation": "창고/작업장 빈출 사진입니다. 작업자 2인의 협동 동작(lifting/carrying a cardboard box), 착용 장비(safety glasses, gloves), 배경의 선반(stacked on shelves)과 지게차(forklift)를 말해주면 만점 답변이 됩니다."
        },
        {
            "id": "p2-20",
            "part": 2,
            "qNum": "#20",
            "category": "과학 실험실·연구실",
            "topic": "실험실 연구원 2인 현미경 관찰 및 클립보드 기록 (Science Laboratory)",
            "prepTime": 45,
            "responseTime": 30,
            "imageBase64": img_map[26],
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken in a science laboratory.", "ko": "이 사진은 과학 실험실에서 찍힌 사진입니다."},
                {"step": "2. 공통 복장 묘사", "en": "Two researchers wearing white lab coats, masks, hairnets, and gloves are sitting at a desk.", "ko": "흰 실험 가운, 마스크, 위생 모자, 장갑을 착용한 두 연구원이 책상에 앉아 있습니다."},
                {"step": "3. 좌우 인물 개별 동작", "en": "On the left, a woman is writing notes on a clipboard with a pen, while on the right, a man is looking through a microscope.", "ko": "왼쪽에서는 여성이 펜으로 클립보드에 기록을 하고 있고, 오른쪽에서는 남성이 현미경을 들여다보고 있습니다."},
                {"step": "4. 주변 실험 기구 마무리", "en": "On the desk and by the window, there are glassware items and folders, and they look very focused on their experiment.", "ko": "책상 위와 창가에는 유리 실험 기구들과 폴더들이 놓여 있으며, 그들은 실험에 매우 집중한 모습입니다."}
            ],
            "magicSentences": [
                {"en": "They are wearing white lab coats and protective gear.", "ko": "그들은 흰 실험 가운과 보호 장비를 착용하고 있습니다.", "tip": "시계토끼 만능 #035 (연구원/의료진 복장 공식)"},
                {"en": "They look very focused on their work.", "ko": "그들은 업무에 매우 집중하고 있는 것처럼 보입니다.", "tip": "시계토끼 만능 #148 (실내 업무/연구 사진 만능 마무리)"}
            ],
            "vocabulary": [
                {"word": "laboratory", "ipa": "[ˈlæbrətɔːri]", "pos": "명사", "meaning": "실험실, 연구실"},
                {"word": "lab coat", "ipa": "[læb koʊt]", "pos": "명사구", "meaning": "실험복, 가운"},
                {"word": "microscope", "ipa": "[ˈmaɪkrəskoʊp]", "pos": "명사", "meaning": "현미경"}
            ],
            "explanation": "실험실 사진에서는 공통 착용 복장(white lab coats, masks, gloves)을 먼저 묶어서 말한 뒤, 왼쪽 여성(writing on a clipboard)과 오른쪽 남성(looking through a microscope)의 동작을 나눠 묘사하면 매우 체계적입니다."
        }
    ]



def get_new_part3_items():
    """유형별 6문항씩 총 30문항 추가 (유튜브 최신 기출 반영)"""
    return [
        # --- p3-t1: 시점 최근 경험 (6문항 추가) ---
        {
            "id": "p3-new-01",
            "part": 3,
            "qNum": "#07",
            "typeId": "p3-t1",
            "typeName": "시점 최근 경험",
            "typeBadge": "시점 최근 경험",
            "topic": "콘서트·라이브 공연 최근 관람 경험 (Live Concert)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you attended a live concert or music performance, and who did you go with?",
            "questionKo": "라이브 콘서트나 음악 공연에 마지막으로 갔던 것이 언제였고, 누구와 함께 갔나요?",
            "sentences": [
                {"step": "1. 과거 시점 제시", "en": "The last time I attended a live concert was about two months ago.", "ko": "제가 라이브 콘서트에 마지막으로 갔던 것은 약 두 달 전이었습니다."},
                {"step": "2. 동행인 및 장소", "en": "I went to a pop music concert at the Olympic Stadium with my best friend.", "ko": "저는 가장 친한 친구와 함께 올림픽 경기장에서 열린 팝 음악 콘서트에 갔습니다."},
                {"step": "3. 부연 마무리", "en": "We sang along to our favorite songs and relieved a lot of stress.", "ko": "저희는 좋아하는 노래를 따라 부르며 스트레스를 많이 풀었습니다."}
            ],
            "magicSentences": [
                {"en": "The last time I attended a concert was two months ago.", "ko": "마지막으로 콘서트에 간 것은 두 달 전이었습니다.", "tip": "When was the last time~ 과거 시점 공식"},
                {"en": "We relieved a lot of stress and had a great time.", "ko": "스트레스를 많이 풀고 즐거운 시간을 보냈습니다.", "tip": "시계토끼 만능 #051 (스트레스 해소 만능 문장)"}
            ],
            "vocabulary": [
                {"word": "attend", "ipa": "[əˈtend]", "pos": "동사", "meaning": "참석하다, 가다"},
                {"word": "sing along", "ipa": "[sɪŋ əˈlɔːŋ]", "pos": "숙어", "meaning": "따라 부르다"},
                {"word": "relieve stress", "ipa": "[rɪˈliːv stres]", "pos": "숙어", "meaning": "스트레스를 해소하다"}
            ],
            "explanation": "공연·전시 관람 경험 질문은 'two months ago'로 시점을 먼저 말하고, 'with my best friend'와 'relieved a lot of stress'를 붙여주면 15초가 깔끔하게 채워집니다."
        },
        {
            "id": "p3-new-02",
            "part": 3,
            "qNum": "#08",
            "typeId": "p3-t1",
            "typeName": "시점 최근 경험",
            "typeBadge": "시점 최근 경험",
            "topic": "전자기기 최근 구매 경험 및 구매처 (Electronic Device)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you bought an electronic device, and where did you buy it?",
            "questionKo": "전자기기를 마지막으로 구매한 것이 언제였고, 어디에서 구매했나요?",
            "sentences": [
                {"step": "1. 구매 시점 및 품목", "en": "The last time I bought an electronic device was last month when I purchased wireless earphones.", "ko": "전자기기를 마지막으로 산 것은 지난달에 무선 이어폰을 구매했을 때입니다."},
                {"step": "2. 구매처 제시", "en": "I bought them at an online shopping mall using my smartphone.", "ko": "저는 스마트폰을 이용해 온라인 쇼핑몰에서 그것을 구매했습니다."},
                {"step": "3. 구매 이유 마무리", "en": "It was much cheaper than buying it at a department store because I used a discount coupon.", "ko": "할인 쿠폰을 사용했기 때문에 백화점에서 사는 것보다 훨씬 저렴했습니다."}
            ],
            "magicSentences": [
                {"en": "I bought it at an online shopping mall last month.", "ko": "지난달에 온라인 쇼핑몰에서 구매했습니다.", "tip": "시계토끼 만능 #068 (온라인 쇼핑 구매처 만능)"},
                {"en": "It was much cheaper because I used a discount coupon.", "ko": "할인 쿠폰을 사용해서 훨씬 저렴했습니다.", "tip": "시계토끼 만능 #070 (가격 할인 만능 이유)"}
            ],
            "vocabulary": [
                {"word": "electronic device", "ipa": "[ɪˌlekˈtrɑːnɪk dɪˈvaɪs]", "pos": "명사구", "meaning": "전자기기"},
                {"word": "wireless earphones", "ipa": "[ˈwaɪərləs ˈɪrfoʊnz]", "pos": "명사구", "meaning": "무선 이어폰"},
                {"word": "discount coupon", "ipa": "[ˈdɪskaʊnt ˈkuːpɑːn]", "pos": "명사구", "meaning": "할인 쿠폰"}
            ],
            "explanation": "전자기기, 가전제품, 생필품 등 구매처(Where did you buy it?)를 묻는 모든 질문에는 'online shopping mall' + 'discount coupon' 조합이 가장 말하기 쉽습니다."
        },
        {
            "id": "p3-new-03",
            "part": 3,
            "qNum": "#09",
            "typeId": "p3-t1",
            "typeName": "시점 최근 경험",
            "typeBadge": "시점 최근 경험",
            "topic": "새로운 식당 최근 방문 및 메뉴 (New Restaurant)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you tried a new restaurant, and what kind of food did you have?",
            "questionKo": "새로운 식당에 마지막으로 가본 것이 언제였고, 어떤 음식을 먹었나요?",
            "sentences": [
                {"step": "1. 방문 시점 제시", "en": "The last time I tried a new restaurant was last Friday evening.", "ko": "제가 새로운 식당에 마지막으로 가본 것은 지난주 금요일 저녁이었습니다."},
                {"step": "2. 장소 및 음식 종류", "en": "I went to a newly opened Italian restaurant near my office and had seafood pasta and pizza.", "ko": "저는 사무실 근처에 새로 문을 연 이탈리안 레스토랑에 가서 해산물 파스타와 피자를 먹었습니다."},
                {"step": "3. 소감 마무리", "en": "The food was really delicious and the atmosphere was very cozy.", "ko": "음식이 정말 맛있었고 분위기도 매우 아늑했습니다."}
            ],
            "magicSentences": [
                {"en": "I went to an Italian restaurant and had pasta and pizza.", "ko": "이탈리안 식당에 가서 파스타와 피자를 먹었습니다.", "tip": "음식 종류 질문에 가장 발음하기 쉬운 만능 메뉴"},
                {"en": "The food was delicious and the atmosphere was cozy.", "ko": "음식이 맛있고 분위기가 아늑했습니다.", "tip": "시계토끼 만능 #082 (식당·카페 후기 만능 표현)"}
            ],
            "vocabulary": [
                {"word": "newly opened", "ipa": "[ˈnuːli ˈoʊpənd]", "pos": "형용사구", "meaning": "새로 문을 연"},
                {"word": "atmosphere", "ipa": "[ˈætməsfɪr]", "pos": "명사", "meaning": "분위기"},
                {"word": "cozy", "ipa": "[ˈkoʊzi]", "pos": "형용사", "meaning": "아늑한, 편안한"}
            ],
            "explanation": "식당 관련 과거 경험 질문에서는 'Italian restaurant - seafood pasta and pizza - delicious and cozy' 3단 세트를 외워두면 어떤 질문에도 즉각 대응할 수 있습니다."
        },
        {
            "id": "p3-new-04",
            "part": 3,
            "qNum": "#10",
            "typeId": "p3-t1",
            "typeName": "시점 최근 경험",
            "typeBadge": "시점 최근 경험",
            "topic": "친구·가족에게 선물 구매한 최근 경험 (Buying a Gift)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you bought a gift for someone, and what did you buy?",
            "questionKo": "누군가를 위해 선물을 마지막으로 산 것이 언제였고, 무엇을 샀나요?",
            "sentences": [
                {"step": "1. 구매 시점 및 대상", "en": "The last time I bought a gift for someone was two weeks ago for my mother's birthday.", "ko": "누군가를 위해 선물을 마지막으로 산 것은 2주 전 어머니 생신 때였습니다."},
                {"step": "2. 구매 품목 제시", "en": "I bought a warm cashmere scarf and a birthday cake at a department store.", "ko": "저는 백화점에서 따뜻한 캐시미어 스카프와 생일 케이크를 샀습니다."},
                {"step": "3. 반응 마무리", "en": "She really loved the color and wore it right away.", "ko": "어머니께서 색상을 무척 마음에 들어 하시며 바로 착용하셨습니다."}
            ],
            "magicSentences": [
                {"en": "It was two weeks ago for my mother's birthday.", "ko": "2주 전 어머니 생신 때였습니다.", "tip": "선물·기념일 질문 만능 시점 & 이유"},
                {"en": "She really loved it and was very happy.", "ko": "그녀가 정말 마음에 들어 했고 매우 기뻐했습니다.", "tip": "선물 후기 마무리 만능 문장"}
            ],
            "vocabulary": [
                {"word": "scarf", "ipa": "[skɑːrf]", "pos": "명사", "meaning": "스카프, 목도리"},
                {"word": "department store", "ipa": "[dɪˈpɑːrtmənt stɔːr]", "pos": "명사구", "meaning": "백화점"},
                {"word": "right away", "ipa": "[raɪt əˈweɪ]", "pos": "숙어", "meaning": "즉시, 곧바로"}
            ],
            "explanation": "선물(gift/present) 질문은 대상(for my mother's birthday)과 품목(a scarf and a cake)만 명확히 넣어도 고득점이 나옵니다."
        },
        {
            "id": "p3-new-05",
            "part": 3,
            "qNum": "#11",
            "typeId": "p3-t1",
            "typeName": "시점 최근 경험",
            "typeBadge": "시점 최근 경험",
            "topic": "온라인 강의·교육 최근 수강 경험 (Online Class)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you took an online class or lecture, and what was it about?",
            "questionKo": "온라인 수업이나 강의를 마지막으로 들은 것이 언제였고, 무엇에 관한 수업이었나요?",
            "sentences": [
                {"step": "1. 수강 시점 제시", "en": "The last time I took an online lecture was yesterday evening at home.", "ko": "제가 온라인 강의를 마지막으로 들은 것은 어제저녁 집에서였습니다."},
                {"step": "2. 강의 주제 설명", "en": "It was an online business English speaking course on YouTube.", "ko": "유튜브에서 진행되는 비즈니스 영어 스피킹 온라인 강의였습니다."},
                {"step": "3. 장점 마무리", "en": "It was very helpful because I could study at my own pace without commuting.", "ko": "이동할 필요 없이 제 속도에 맞춰 공부할 수 있어서 매우 유익했습니다."}
            ],
            "magicSentences": [
                {"en": "It was an English speaking course on YouTube.", "ko": "유튜브의 영어 스피킹 강의였습니다.", "tip": "수업·강의 주제 만능 답변"},
                {"en": "I could study at my own pace at home.", "ko": "집에서 제 속도에 맞춰 공부할 수 있었습니다.", "tip": "시계토끼 만능 #155 (온라인 학습 만능 장점)"}
            ],
            "vocabulary": [
                {"word": "lecture", "ipa": "[ˈlektʃər]", "pos": "명사", "meaning": "강의, 강연"},
                {"word": "at one's own pace", "ipa": "[æt wʌnz oʊn peɪs]", "pos": "숙어", "meaning": "자신의 속도에 맞춰"},
                {"word": "commute", "ipa": "[kəˈmjuːt]", "pos": "동사", "meaning": "통학하다, 통근하다"}
            ],
            "explanation": "최근 온라인 강의 수강 경험은 'yesterday evening' + 'English speaking course' 조합이 가장 자연스럽고 발음하기도 편합니다."
        },
        {
            "id": "p3-new-06",
            "part": 3,
            "qNum": "#12",
            "typeId": "p3-t1",
            "typeName": "시점 최근 경험",
            "typeBadge": "시점 최근 경험",
            "topic": "박물관·미술관 최근 방문 경험 (Museum or Art Gallery)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you visited a museum or an art gallery, and what did you see there?",
            "questionKo": "박물관이나 미술관에 마지막으로 방문한 것이 언제였고, 그곳에서 무엇을 보았나요?",
            "sentences": [
                {"step": "1. 방문 시점 제시", "en": "The last time I visited an art gallery was last month on the weekend.", "ko": "제가 미술관에 마지막으로 방문한 것은 지난달 주말이었습니다."},
                {"step": "2. 관람 내용 설명", "en": "I went to the National Art Museum in Seoul and saw a modern photography exhibition.", "ko": "저는 서울 국립미술관에 가서 현대 사진전을 관람했습니다."},
                {"step": "3. 느낀 점 마무리", "en": "The photos were very impressive and I learned a lot about modern art.", "ko": "사진들이 매우 인상적이었고 현대 예술에 대해 많은 것을 배웠습니다."}
            ],
            "magicSentences": [
                {"en": "I went to the National Museum and saw a photography exhibition.", "ko": "국립박물관에 가서 사진전을 보았습니다.", "tip": "박물관·전시회 관람 품목 만능 답변"},
                {"en": "It was very impressive and I learned a lot.", "ko": "매우 인상적이었고 많은 것을 배웠습니다.", "tip": "시계토끼 만능 #090 (문화·전시 감상 만능 마무리)"}
            ],
            "vocabulary": [
                {"word": "art gallery", "ipa": "[ɑːrt ˈɡæləri]", "pos": "명사구", "meaning": "미술관"},
                {"word": "exhibition", "ipa": "[ˌeksɪˈbɪʃn]", "pos": "명사", "meaning": "전시회"},
                {"word": "impressive", "ipa": "[ɪmˈpresɪv]", "pos": "형용사", "meaning": "인상 깊은, 감명 깊은"}
            ],
            "explanation": "박물관이나 미술관 질문에서 구체적인 작품 이름이 떠오르지 않을 때는 'a modern photography exhibition(현대 사진전)'이라고 답하면 아주 자연스럽습니다."
        },

        # --- p3-t2: 빈도 장소 동행인 (6문항 추가) ---
        {
            "id": "p3-new-07",
            "part": 3,
            "qNum": "#19",
            "typeId": "p3-t2",
            "typeName": "빈도 장소 동행인",
            "typeBadge": "빈도 장소 동행인",
            "topic": "음식 배달 앱 이용 빈도 및 선호 메뉴 (Food Delivery App)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you use food delivery apps, and what kind of food do you usually order?",
            "questionKo": "음식 배달 앱을 얼마나 자주 이용하며, 주로 어떤 음식을 주문하나요?",
            "sentences": [
                {"step": "1. 이용 빈도 제시", "en": "I usually use food delivery apps about twice a week, especially on weekends.", "ko": "저는 주로 주말을 중심으로 일주일에 두 번 정도 음식 배달 앱을 이용합니다."},
                {"step": "2. 주로 시키는 메뉴", "en": "I mostly order fried chicken or pizza when I watch movies at home with my family.", "ko": "집에서 가족들과 영화를 볼 때 주로 프라이드치킨이나 피자를 주문합니다."},
                {"step": "3. 이유 마무리", "en": "It is very convenient because the food is delivered right to my door within 30 minutes.", "ko": "30분 이내에 문 앞까지 바로 음식이 배달되기 때문에 매우 편리합니다."}
            ],
            "magicSentences": [
                {"en": "I usually use it about twice a week on weekends.", "ko": "주말에 일주일에 두 번 정도 이용합니다.", "tip": "How often~ 빈도 질문 만능 첫 문장"},
                {"en": "It is delivered right to my door quickly.", "ko": "문 앞까지 빠르게 바로 배달됩니다.", "tip": "시계토끼 만능 #075 (배달 서비스 장점 만능)"}
            ],
            "vocabulary": [
                {"word": "twice a week", "ipa": "[twaɪs ə wiːk]", "pos": "부사구", "meaning": "일주일에 두 번"},
                {"word": "order", "ipa": "[ˈɔːrdər]", "pos": "동사", "meaning": "주문하다"},
                {"word": "right to my door", "ipa": "[raɪt tuː maɪ dɔːr]", "pos": "부사구", "meaning": "바로 문 앞까지"}
            ],
            "explanation": "빈도(How often)와 메뉴(What kind of food)를 함께 묻는 2중 질문입니다. 'twice a week' + 'fried chicken or pizza'로 두 가지를 모두 명확히 짚어주세요."
        },
        {
            "id": "p3-new-08",
            "part": 3,
            "qNum": "#20",
            "typeId": "p3-t2",
            "typeName": "빈도 장소 동행인",
            "typeBadge": "빈도 장소 동행인",
            "topic": "유튜브·동영상 플랫폼 시청 빈도 및 콘텐츠 (Watching Videos)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you watch videos online, and where do you usually watch them?",
            "questionKo": "온라인 동영상을 얼마나 자주 시청하며, 주로 어디에서 보나요?",
            "sentences": [
                {"step": "1. 시청 빈도 제시", "en": "I watch online videos on YouTube almost every day.", "ko": "저는 거의 매일 유튜브에서 온라인 동영상을 시청합니다."},
                {"step": "2. 시청 장소 및 상황", "en": "I usually watch them on the subway while commuting to work or in my bedroom before going to sleep.", "ko": "주로 출퇴근길 지하철 안이나 잠들기 전 침실에서 시청합니다."},
                {"step": "3. 주요 시청 콘텐츠", "en": "Watching travel vlogs and music videos on my smartphone helps me relax.", "ko": "스마트폰으로 여행 브이로그나 뮤직비디오를 보면 긴장을 푸는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "I watch online videos almost every day.", "ko": "거의 매일 온라인 동영상을 봅니다.", "tip": "스마트폰·미디어 빈도 질문 만능 답변"},
                {"en": "I usually watch them on the subway while commuting.", "ko": "출퇴근하면서 지하철에서 주로 봅니다.", "tip": "시계토끼 만능 #058 (스마트폰 사용 장소 만능)"}
            ],
            "vocabulary": [
                {"word": "almost every day", "ipa": "[ˈɔːlmoʊst ˈevri deɪ]", "pos": "부사구", "meaning": "거의 매일"},
                {"word": "while commuting", "ipa": "[waɪl kəˈmjuːtɪŋ]", "pos": "부사구", "meaning": "통근/통학하는 동안"},
                {"word": "travel vlog", "ipa": "[ˈtrævl vlɔːɡ]", "pos": "명사구", "meaning": "여행 브이로그"}
            ],
            "explanation": "디지털 기기나 미디어 이용 장소(Where)를 물어볼 때는 'on the subway while commuting(출퇴근 지하철에서)' 또는 'in my bedroom at home(집 침실에서)'이 만능입니다."
        },
        {
            "id": "p3-new-09",
            "part": 3,
            "qNum": "#21",
            "typeId": "p3-t2",
            "typeName": "빈도 장소 동행인",
            "typeBadge": "빈도 장소 동행인",
            "topic": "외식 빈도 및 주로 함께 가는 사람 (Eating Out)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you eat out at restaurants, and who do you usually go with?",
            "questionKo": "식당에서 외식을 얼마나 자주 하며, 주로 누구와 함께 가나요?",
            "sentences": [
                {"step": "1. 외식 빈도 제시", "en": "I usually eat out at restaurants once or twice a week.", "ko": "저는 보통 일주일에 한두 번 정도 식당에서 외식을 합니다."},
                {"step": "2. 동행인 제시", "en": "I mostly go there with my close friends or coworkers on Friday evenings.", "ko": "금요일 저녁에 주로 친한 친구들이나 직장 동료들과 함께 갑니다."},
                {"step": "3. 부연 마무리", "en": "We enjoy eating delicious food and talking about our daily lives together.", "ko": "저희는 맛있는 음식을 먹으며 일상 이야기를 나누는 것을 즐깁니다."}
            ],
            "magicSentences": [
                {"en": "I usually eat out once or twice a week.", "ko": "보통 일주일에 한두 번 외식합니다.", "tip": "외식·여가 빈도 만능 표현"},
                {"en": "I mostly go there with my close friends.", "ko": "주로 친한 친구들과 함께 갑니다.", "tip": "Who 동행인 질문 1순위 만능 답변"}
            ],
            "vocabulary": [
                {"word": "eat out", "ipa": "[iːt aʊt]", "pos": "숙어", "meaning": "외식하다"},
                {"word": "coworker", "ipa": "[ˈkoʊwɜːrkər]", "pos": "명사", "meaning": "직장 동료"},
                {"word": "daily lives", "ipa": "[ˈdeɪli laɪvz]", "pos": "명사구", "meaning": "일상생활"}
            ],
            "explanation": "동행인(Who) 질문에는 항상 'with my close friends or family members'를 고정 템플릿으로 사용하세요."
        },
        {
            "id": "p3-new-10",
            "part": 3,
            "qNum": "#22",
            "typeId": "p3-t2",
            "typeName": "빈도 장소 동행인",
            "typeBadge": "빈도 장소 동행인",
            "topic": "집에서 직접 요리하는 빈도 및 선호 메뉴 (Cooking at Home)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you cook at home, and what kind of dishes do you like to make?",
            "questionKo": "집에서 얼마나 자주 요리를 하며, 어떤 요리를 만드는 것을 좋아하나요?",
            "sentences": [
                {"step": "1. 요리 빈도 제시", "en": "I usually cook at home three or four times a week after work.", "ko": "저는 보통 퇴근 후에 일주일에 세네 번 정도 집에서 요리를 합니다."},
                {"step": "2. 선호 메뉴 설명", "en": "I like to make simple and healthy dishes such as kimchi fried rice, pasta, and fresh salads.", "ko": "김치볶음밥, 파스타, 신선한 샐러드처럼 간단하고 건강한 요리를 만드는 것을 좋아합니다."},
                {"step": "3. 이유 마무리", "en": "Cooking at home helps me save money and eat healthier ingredients.", "ko": "집에서 요리를 하면 돈을 절약하고 더 건강한 식재료를 먹을 수 있어 좋습니다."}
            ],
            "magicSentences": [
                {"en": "I like to make simple dishes such as pasta and salad.", "ko": "파스타와 샐러드 같은 간단한 요리를 만드는 것을 좋아합니다.", "tip": "요리 메뉴 질문에 가장 말하기 쉬운 만능 답변"},
                {"en": "It helps me save money and stay healthy.", "ko": "돈을 절약하고 건강을 유지하는 데 도움이 됩니다.", "tip": "시계토끼 만능 #054 (건강·절약 결합 공식)"}
            ],
            "vocabulary": [
                {"word": "dish", "ipa": "[dɪʃ]", "pos": "명사", "meaning": "요리, 음식"},
                {"word": "ingredient", "ipa": "[ɪnˈɡriːdiənt]", "pos": "명사", "meaning": "식재료, 성분"},
                {"word": "save money", "ipa": "[seɪv ˈmʌni]", "pos": "숙어", "meaning": "돈을 절약하다"}
            ],
            "explanation": "집밥/요리 질문에서는 'pasta and salad'처럼 영어로 말하기 쉬운 메뉴를 대고, 장점으로 'save money and stay healthy'를 덧붙이면 만점입니다."
        },
        {
            "id": "p3-new-11",
            "part": 3,
            "qNum": "#23",
            "typeId": "p3-t2",
            "typeName": "빈도 장소 동행인",
            "typeBadge": "빈도 장소 동행인",
            "topic": "날씨 예보 확인 빈도 및 확인 방법 (Checking Weather Forecast)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you check the weather forecast, and how do you usually check it?",
            "questionKo": "일기예보를 얼마나 자주 확인하며, 주로 어떤 방법으로 확인하나요?",
            "sentences": [
                {"step": "1. 확인 빈도 제시", "en": "I check the weather forecast every morning before leaving home.", "ko": "저는 집을 나서기 전 매일 아침 일기예보를 확인합니다."},
                {"step": "2. 확인 수단 설명", "en": "I usually check it using a weather application on my smartphone.", "ko": "주로 스마트폰에 있는 날씨 애플리케이션을 이용해 확인합니다."},
                {"step": "3. 이유 마무리", "en": "It helps me decide what clothes to wear and whether to bring an umbrella.", "ko": "어떤 옷을 입을지, 그리고 우산을 챙겨야 할지 결정하는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "I check it every morning using my smartphone app.", "ko": "스마트폰 앱을 이용해 매일 아침 확인합니다.", "tip": "뉴스·날씨·정보 확인 방법 만능 답변"},
                {"en": "It helps me decide what to wear and whether to bring an umbrella.", "ko": "무엇을 입을지와 우산을 가져갈지 결정하는 데 도움이 됩니다.", "tip": "날씨 확인 이유 필수 표현"}
            ],
            "vocabulary": [
                {"word": "weather forecast", "ipa": "[ˈweðər ˈfɔːrkæst]", "pos": "명사구", "meaning": "일기예보"},
                {"word": "application", "ipa": "[ˌæplɪˈkeɪʃn]", "pos": "명사", "meaning": "애플리케이션, 앱"},
                {"word": "bring an umbrella", "ipa": "[brɪŋ ən ʌmˈbrelə]", "pos": "숙어", "meaning": "우산을 챙기다"}
            ],
            "explanation": "최근 자주 출제되는 날씨/뉴스 확인 빈도 질문입니다. 'every morning' + 'using a smartphone app'으로 간결하게 답하세요."
        },
        {
            "id": "p3-new-12",
            "part": 3,
            "qNum": "#24",
            "typeId": "p3-t2",
            "typeName": "빈도 장소 동행인",
            "typeBadge": "빈도 장소 동행인",
            "topic": "스마트폰 사진 촬영 빈도 및 주요 피사체 (Taking Photos)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you take pictures with your smartphone, and what do you usually take pictures of?",
            "questionKo": "스마트폰으로 사진을 얼마나 자주 찍으며, 주로 무엇을 찍나요?",
            "sentences": [
                {"step": "1. 촬영 빈도 제시", "en": "I take pictures with my smartphone almost every day.", "ko": "저는 거의 매일 스마트폰으로 사진을 찍습니다."},
                {"step": "2. 주요 촬영 대상", "en": "I usually take pictures of delicious food at restaurants, beautiful scenery, and my friends.", "ko": "주로 식당의 맛있는 음식이나 아름다운 풍경, 그리고 친구들의 사진을 찍습니다."},
                {"step": "3. 활용 방법 마무리", "en": "I like sharing those photos on social media to keep good memories.", "ko": "좋은 추억을 남기기 위해 그 사진들을 소셜 미디어에 공유하는 것을 좋아합니다."}
            ],
            "magicSentences": [
                {"en": "I usually take pictures of delicious food and my friends.", "ko": "주로 맛있는 음식과 친구들 사진을 찍습니다.", "tip": "사진 촬영 대상 만능 표현"},
                {"en": "It helps me keep good memories with my loved ones.", "ko": "소중한 사람들과 좋은 추억을 남기는 데 도움이 됩니다.", "tip": "시계토끼 만능 #094 (사진·추억 만능 문장)"}
            ],
            "vocabulary": [
                {"word": "take pictures of", "ipa": "[teɪk ˈpɪktʃərz ʌv]", "pos": "숙어", "meaning": "~의 사진을 찍다"},
                {"word": "scenery", "ipa": "[ˈsiːnəri]", "pos": "명사", "meaning": "풍경, 경치"},
                {"word": "keep memories", "ipa": "[kiːp ˈmeməriz]", "pos": "숙어", "meaning": "추억을 간직하다"}
            ],
            "explanation": "사진 촬영 질문은 'delicious food, beautiful scenery, and my friends' 세 가지를 나열하면 15초 분량이 완벽하게 채워집니다."
        },

        # --- p3-t3: 양자택일 선호도 찬반 (6문항 추가) ---
        {
            "id": "p3-new-13",
            "part": 3,
            "qNum": "#31",
            "typeId": "p3-t3",
            "typeName": "양자택일 선호도 찬반",
            "typeBadge": "양자택일 선호도 찬반",
            "topic": "실내 활동 vs 야외 활동 여가 선호도 (Indoor vs. Outdoor Activities)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer enjoying indoor activities or outdoor activities in your free time, and why?",
            "questionKo": "여가 시간에 실내 활동을 즐기는 것과 야외 활동을 즐기는 것 중 어느 쪽을 선호하며, 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 선호 입장 선택", "en": "I definitely prefer enjoying outdoor activities in my free time.", "ko": "저는 여가 시간에 야외 활동을 즐기는 것을 훨씬 선호합니다."},
                {"step": "2. 핵심 이유 제시", "en": "Since I sit in front of a computer inside the office all day, I want to get some fresh air outside.", "ko": "하루 종일 사무실 안에서 컴퓨터 앞에 앉아 있기 때문에, 밖에서 상쾌한 공기를 마시고 싶습니다."},
                {"step": "3. 구체적 행동 마무리", "en": "Walking in the park under the sunshine helps me refresh my mind and relieve stress.", "ko": "햇살 아래 공원을 산책하면 기분이 상쾌해지고 스트레스가 풀립니다."}
            ],
            "magicSentences": [
                {"en": "I want to get some fresh air and refresh my mind.", "ko": "상쾌한 공기를 마시고 기분을 전환하고 싶습니다.", "tip": "시계토끼 만능 #051 (야외 활동 선호 1순위 이유)"},
                {"en": "It helps me relieve stress after work.", "ko": "퇴근 후 스트레스를 푸는 데 도움이 됩니다.", "tip": "여가 활동 만능 결론"}
            ],
            "vocabulary": [
                {"word": "outdoor activity", "ipa": "[ˈaʊtdɔːr ækˈtɪvəti]", "pos": "명사구", "meaning": "야외 활동"},
                {"word": "refresh one's mind", "ipa": "[rɪˈfreʃ wʌnz maɪnd]", "pos": "숙어", "meaning": "기분을 전환하다"},
                {"word": "sunshine", "ipa": "[ˈsʌnʃaɪn]", "pos": "명사", "meaning": "햇살, 햇빛"}
            ],
            "explanation": "실내 vs 야외 선택 질문에서는 야외(outdoor)를 선택해 'get some fresh air'와 'relieve stress' 만능 문장으로 연결하는 것이 가장 쉽습니다."
        },
        {
            "id": "p3-new-14",
            "part": 3,
            "qNum": "#32",
            "typeId": "p3-t3",
            "typeName": "양자택일 선호도 찬반",
            "typeBadge": "양자택일 선호도 찬반",
            "topic": "혼자 여행하기 vs 단체·친구와 여행하기 (Traveling Alone vs. With Others)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer traveling alone or traveling with a group of friends, and why?",
            "questionKo": "혼자 여행하는 것과 친구들과 함께 여행하는 것 중 어느 쪽을 선호하며, 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 선호 입장 선택", "en": "I prefer traveling with a group of friends rather than traveling alone.", "ko": "저는 혼자 여행하는 것보다 친구들과 함께 여행하는 것을 선호합니다."},
                {"step": "2. 이유 1 (즐거움과 안전)", "en": "First, it is much safer and more fun to explore new places together.", "ko": "첫째, 새로운 장소를 함께 탐험하는 것이 훨씬 안전하고 더 재미있습니다."},
                {"step": "3. 이유 2 (비용 절감)", "en": "Also, we can share travel expenses such as hotel rooms and food, so we can save money.", "ko": "또한 호텔 숙박비나 식비 같은 여행 경비를 나눌 수 있어서 돈을 절약할 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "It is much safer and more fun to go together.", "ko": "함께 가는 것이 훨씬 안전하고 더 재미있습니다.", "tip": "동행 선호 질문 만능 이유"},
                {"en": "We can share expenses and save money.", "ko": "비용을 분담하여 돈을 절약할 수 있습니다.", "tip": "시계토끼 만능 #072 (비용 분담 만능 표현)"}
            ],
            "vocabulary": [
                {"word": "explore", "ipa": "[ɪkˈsplɔːr]", "pos": "동사", "meaning": "탐험하다, 둘러보다"},
                {"word": "share expenses", "ipa": "[ʃer ɪkˈspensɪz]", "pos": "숙어", "meaning": "비용을 분담하다"},
                {"word": "rather than", "ipa": "[ˈræðər ðæn]", "pos": "전치사구", "meaning": "~라기보다는"}
            ],
            "explanation": "혼자 vs 함께 여행 질문은 'with friends'를 골라 1) safer and more fun(안전하고 재미있음), 2) share expenses and save money(비용 분담) 두 가지 이유를 대면 완벽합니다."
        },
        {
            "id": "p3-new-15",
            "part": 3,
            "qNum": "#33",
            "typeId": "p3-t3",
            "typeName": "양자택일 선호도 찬반",
            "typeBadge": "양자택일 선호도 찬반",
            "topic": "아침 운동 vs 저녁 운동 선호도 (Morning vs. Evening Exercise)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer exercising in the morning or in the evening, and why?",
            "questionKo": "아침에 운동하는 것과 저녁에 운동하는 것 중 어느 쪽을 선호하며, 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 선호 입장 선택", "en": "I definitely prefer exercising in the evening after work.", "ko": "저는 퇴근 후 저녁에 운동하는 것을 확실히 선호합니다."},
                {"step": "2. 핵심 이유 설명", "en": "In the morning, I am always busy getting ready for work, so I don't have enough time.", "ko": "아침에는 출근 준비로 항상 바빠서 시간이 충분하지 않기 때문입니다."},
                {"step": "3. 부연 효과 마무리", "en": "However, working out in the evening helps me relieve daily stress and sleep better at night.", "ko": "반면 저녁에 운동을 하면 하루의 스트레스를 풀고 밤에 숙면을 취하는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "I am too busy in the morning, so I have more time in the evening.", "ko": "아침에는 너무 바빠서 저녁에 시간이 더 많습니다.", "tip": "시간대 선택(아침 vs 저녁) 만능 이유"},
                {"en": "It helps me relieve stress and sleep better at night.", "ko": "스트레스를 풀고 밤에 잠을 더 잘 자게 해 줍니다.", "tip": "저녁 운동/휴식 만능 효과"}
            ],
            "vocabulary": [
                {"word": "get ready for", "ipa": "[ɡet ˈredi fɔːr]", "pos": "숙어", "meaning": "~을 준비하다"},
                {"word": "work out", "ipa": "[wɜːrk aʊt]", "pos": "숙어", "meaning": "운동하다"},
                {"word": "sleep better", "ipa": "[sliːp ˈbetər]", "pos": "숙어", "meaning": "숙면을 취하다"}
            ],
            "explanation": "아침 vs 저녁(운동, 공부, 쇼핑 등) 질문은 언제나 저녁(evening)을 선택하고 '아침에는 출근/등교 준비로 바쁘다(busy in the morning)'고 답하는 것이 가장 수월합니다."
        },
        {
            "id": "p3-new-16",
            "part": 3,
            "qNum": "#34",
            "typeId": "p3-t3",
            "typeName": "양자택일 선호도 찬반",
            "typeBadge": "양자택일 선호도 찬반",
            "topic": "전화 통화 vs 문자 메시지 소통 선호도 (Phone Calls vs. Text Messages)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer communicating by phone call or by text message, and why?",
            "questionKo": "전화 통화로 소통하는 것과 문자 메시지로 소통하는 것 중 어느 쪽을 선호하며, 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 선호 입장 선택", "en": "I prefer communicating by text message rather than making phone calls.", "ko": "저는 전화 통화를 하는 것보다 문자 메시지로 소통하는 것을 선호합니다."},
                {"step": "2. 이유 1 (시공간 편리성)", "en": "First, I can send and check messages anytime, anywhere, even when I am in a meeting or on the subway.", "ko": "첫째, 회의 중이거나 지하철에 있을 때도 언제 어디서나 메시지를 보내고 확인할 수 있습니다."},
                {"step": "3. 이유 2 (기록 보관)", "en": "Also, text messages leave a written record, so I don't forget important information.", "ko": "또한 문자 메시지는 기록이 남기 때문에 중요한 정보를 잊어버리지 않습니다."}
            ],
            "magicSentences": [
                {"en": "I can send messages anytime, anywhere.", "ko": "언제 어디서나 메시지를 보낼 수 있습니다.", "tip": "시계토끼 만능 #158 (시공간 제약 없음 공식)"},
                {"en": "It leaves a record, so I don't forget important details.", "ko": "기록이 남아서 중요한 내용을 잊지 않습니다.", "tip": "문자/이메일 선호 핵심 이유"}
            ],
            "vocabulary": [
                {"word": "communicate", "ipa": "[kəˈmjuːnɪkeɪt]", "pos": "동사", "meaning": "소통하다, 연락하다"},
                {"word": "leave a record", "ipa": "[liːv ə ˈrekərd]", "pos": "숙어", "meaning": "기록을 남기다"},
                {"word": "important details", "ipa": "[ɪmˈpɔːrtnt ˈdiːteɪlz]", "pos": "명사구", "meaning": "중요한 세부 사항"}
            ],
            "explanation": "전화 vs 문자/이메일 양자택일은 문자(text message)를 선택해 'anytime, anywhere'와 'leave a record(기록이 남는다)' 두 가지를 말하면 완벽합니다."
        },
        {
            "id": "p3-new-17",
            "part": 3,
            "qNum": "#35",
            "typeId": "p3-t3",
            "typeName": "양자택일 선호도 찬반",
            "typeBadge": "양자택일 선호도 찬반",
            "topic": "대도시 거주 vs 시골·소도시 거주 선호도 (Big City vs. Countryside)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Would you rather live in a big city or in the countryside, and why?",
            "questionKo": "대도시에 사는 것과 시골에 사는 것 중 어느 쪽을 선호하며, 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 선호 입장 선택", "en": "I would definitely rather live in a big city than in the countryside.", "ko": "저는 시골보다 대도시에 사는 것을 확실히 더 선호합니다."},
                {"step": "2. 이유 1 (대중교통 및 편의시설)", "en": "Big cities have a well-developed public transportation system such as subways and buses.", "ko": "대도시에는 지하철이나 버스 같은 대중교통 시스템이 잘 발달되어 있습니다."},
                {"step": "3. 이유 2 (문화·의료 인프라)", "en": "Also, there are many hospitals, shopping malls, and cultural facilities near my house, which is very convenient.", "ko": "또한 집 근처에 병원, 쇼핑몰, 문화 시설이 많아서 생활하기에 매우 편리합니다."}
            ],
            "magicSentences": [
                {"en": "It has a convenient public transportation system.", "ko": "편리한 대중교통 시스템을 갖추고 있습니다.", "tip": "시계토끼 만능 #060 (도시·위치 장점 만능)"},
                {"en": "There are many hospitals and shopping malls nearby.", "ko": "근처에 병원과 쇼핑몰이 많습니다.", "tip": "편의시설 인프라 만능 표현"}
            ],
            "vocabulary": [
                {"word": "countryside", "ipa": "[ˈkʌntrisaɪd]", "pos": "명사", "meaning": "시골, 지방"},
                {"word": "well-developed", "ipa": "[wel dɪˈveləpt]", "pos": "형용사", "meaning": "잘 발달된"},
                {"word": "cultural facility", "ipa": "[ˈkʌltʃərəl fəˈsɪləti]", "pos": "명사구", "meaning": "문화 시설"}
            ],
            "explanation": "거주지(대도시 vs 시골, 아파트 vs 주택) 질문은 대중교통(public transportation)과 편의시설(convenient facilities)을 이유로 들 수 있는 대도시/아파트를 고르는 것이 유리합니다."
        },
        {
            "id": "p3-new-18",
            "part": 3,
            "qNum": "#36",
            "typeId": "p3-t3",
            "typeName": "양자택일 선호도 찬반",
            "typeBadge": "양자택일 선호도 찬반",
            "topic": "현금 결제 vs 신용카드·모바일 페이 선호도 (Cash vs. Credit Card)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer paying with cash or paying with a credit card or mobile pay, and why?",
            "questionKo": "현금으로 결제하는 것과 신용카드나 모바일 페이로 결제하는 것 중 어느 쪽을 선호하며, 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 선호 입장 선택", "en": "I strongly prefer paying with a credit card or mobile pay rather than cash.", "ko": "저는 현금보다 신용카드나 모바일 페이로 결제하는 것을 강력히 선호합니다."},
                {"step": "2. 이유 1 (휴대 간편성)", "en": "First, I don't need to carry a heavy wallet or coins because I only need my smartphone.", "ko": "첫째, 스마트폰만 있으면 되기 때문에 무거운 지갑이나 동전을 들고 다닐 필요가 없습니다."},
                {"step": "3. 이유 2 (할인·포인트 혜택)", "en": "Second, I can get reward points and various discounts, and easily track my spending history.", "ko": "둘째, 적립 포인트와 다양한 할인 혜택을 받을 수 있고 지출 내역도 쉽게 확인할 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "I don't need to carry a heavy wallet or coins.", "ko": "무거운 지갑이나 동전을 들고 다닐 필요가 없습니다.", "tip": "모바일 페이·카드 선호 핵심 표현"},
                {"en": "I can get reward points and various discounts.", "ko": "적립 포인트와 다양한 할인을 받을 수 있습니다.", "tip": "시계토끼 만능 #070 (쇼핑·결제 혜택 만능)"}
            ],
            "vocabulary": [
                {"word": "reward points", "ipa": "[rɪˈwɔːrd pɔɪnts]", "pos": "명사구", "meaning": "적립 포인트"},
                {"word": "track", "ipa": "[træk]", "pos": "동사", "meaning": "추적하다, 확인하다"},
                {"word": "spending history", "ipa": "[ˈspendɪŋ ˈhɪstəri]", "pos": "명사구", "meaning": "지출 내역"}
            ],
            "explanation": "결제 수단 질문은 카드/모바일 페이를 선택해 1) 지갑 불필요(no heavy wallet), 2) 포인트/할인(reward points and discounts)을 말하면 만점입니다."
        },

        # --- p3-t4: 3자택일 최적 선택 (6문항 추가) ---
        {
            "id": "p3-new-19",
            "part": 3,
            "qNum": "#43",
            "typeId": "p3-t4",
            "typeName": "3자택일 최적 선택",
            "typeBadge": "3자택일 최적 선택",
            "topic": "직장·직업 선택 시 가장 중요한 기준 (Choosing a Job)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When choosing a job, which of the following is the most important to you: high salary, work-life balance, or friendly coworkers?",
            "questionKo": "직장을 선택할 때 다음 중 본인에게 가장 중요한 것은 무엇인가요: 높은 연봉, 워라밸(일과 삶의 균형), 친절한 동료?",
            "sentences": [
                {"step": "1. 최우선 요소 선택", "en": "Among the three options, work-life balance is the most important factor to me when choosing a job.", "ko": "세 가지 선택지 중에서 직장을 고를 때 저에게 가장 중요한 요소는 워라밸(일과 삶의 균형)입니다."},
                {"step": "2. 이유 1 (번아웃 방지)", "en": "If I work overtime every day, I will easily get burned out and lose my health.", "ko": "만약 매일 야근을 한다면 쉽게 번아웃이 오고 건강을 잃게 될 것입니다."},
                {"step": "3. 이유 2 (업무 효율 향상)", "en": "Having enough rest after work actually helps me focus better and be more productive at the office.", "ko": "퇴근 후 충분한 휴식을 취하는 것이 실제로 회사에서 더 잘 집중하고 생산성을 높이는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "Among the three options, work-life balance is the most important to me.", "ko": "세 가지 선택지 중 워라밸이 저에게 가장 중요합니다.", "tip": "3자택일 첫 문장 만능 공식"},
                {"en": "Having enough rest helps me be more productive at work.", "ko": "충분한 휴식을 취하면 업무 생산성을 높이는 데 도움이 됩니다.", "tip": "시계토끼 만능 #162 (휴식·워라밸 만능 문장)"}
            ],
            "vocabulary": [
                {"word": "work-life balance", "ipa": "[wɜːrk laɪf ˈbæləns]", "pos": "명사구", "meaning": "일과 삶의 균형(워라밸)"},
                {"word": "work overtime", "ipa": "[wɜːrk ˈoʊvərtaɪm]", "pos": "숙어", "meaning": "야근하다, 초과 근무하다"},
                {"word": "productive", "ipa": "[prəˈdʌktɪv]", "pos": "형용사", "meaning": "생산적인"}
            ],
            "explanation": "직장 선택 3자택일에서는 'work-life balance'나 'high salary'가 가장 답변하기 쉽습니다. 건강 유지와 업무 생산성(productive)을 연결해 보세요."
        },
        {
            "id": "p3-new-20",
            "part": 3,
            "qNum": "#44",
            "typeId": "p3-t4",
            "typeName": "3자택일 최적 선택",
            "typeBadge": "3자택일 최적 선택",
            "topic": "식당 선택 시 가장 중요한 요소 (Choosing a Restaurant)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When choosing a restaurant, what is the most important factor to you: taste of food, reasonable price, or good service?",
            "questionKo": "식당을 고를 때 다음 중 가장 중요한 요소는 무엇인가요: 음식의 맛, 합리적인 가격, 친절한 서비스?",
            "sentences": [
                {"step": "1. 최우선 요소 선택", "en": "When choosing a restaurant, the taste of food is definitely the most important factor to me.", "ko": "식당을 고를 때 저에게 가장 중요한 요소는 단연 음식의 맛입니다."},
                {"step": "2. 핵심 이유 설명", "en": "Even if the price is cheap and the staff are friendly, I will never visit the restaurant again if the food doesn't taste good.", "ko": "가격이 저렴하고 직원이 친절하더라도, 음식이 맛없으면 그 식당에 다시는 가지 않을 것이기 때문입니다."},
                {"step": "3. 부연 마무리", "en": "Eating delicious food makes me happy and helps me relieve stress.", "ko": "맛있는 음식을 먹는 것은 저를 행복하게 만들고 스트레스를 푸는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "The taste of food is the most important factor to me.", "ko": "음식의 맛이 저에게 가장 중요한 요소입니다.", "tip": "식당·카페 선택 기준 만능 답변"},
                {"en": "Eating delicious food makes me happy and relieves stress.", "ko": "맛있는 음식을 먹으면 행복해지고 스트레스가 풀립니다.", "tip": "시계토끼 만능 #051 응용"}
            ],
            "vocabulary": [
                {"word": "reasonable price", "ipa": "[ˈriːznəbl praɪs]", "pos": "명사구", "meaning": "합리적인 가격"},
                {"word": "even if", "ipa": "[ˈiːvn ɪf]", "pos": "접속사구", "meaning": "비록 ~일지라도"},
                {"word": "taste good", "ipa": "[teɪst ɡʊd]", "pos": "숙어", "meaning": "맛이 좋다"}
            ],
            "explanation": "3자택일에서 나머지 두 옵션을 가볍게 언급하며('Even if the price is cheap...') 내가 고른 옵션의 중요성을 강조하면 AL 수준의 논리적인 답변이 됩니다."
        },
        {
            "id": "p3-new-21",
            "part": 3,
            "qNum": "#45",
            "typeId": "p3-t4",
            "typeName": "3자택일 최적 선택",
            "typeBadge": "3자택일 최적 선택",
            "topic": "이사할 집·아파트를 고를 때 가장 중요한 요소 (Choosing a Place to Live)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When choosing a place to live, which is the most important to you: proximity to public transit, affordable rent, or quiet neighborhood?",
            "questionKo": "살 집을 고를 때 다음 중 가장 중요한 것은 무엇인가요: 대중교통 접근성, 저렴한 집세, 조용한 동네 환경?",
            "sentences": [
                {"step": "1. 최우선 요소 선택", "en": "When choosing a place to live, proximity to public transit is the most important factor to me.", "ko": "살 집을 고를 때 저에게 가장 중요한 요소는 대중교통 접근성입니다."},
                {"step": "2. 이유 1 (출퇴근 시간 절약)", "en": "Since I take the subway to work every day, living near a subway station saves me a lot of commuting time and energy.", "ko": "매일 지하철로 출퇴근하기 때문에 지하철역 근처에 살면 통근 시간과 에너지를 많이 아낄 수 있습니다."},
                {"step": "3. 이유 2 (안전성)", "en": "Also, areas around stations are usually bright and safe when I come home late at night.", "ko": "또한 역 주변 지역은 보통 밝아서 밤늦게 귀가할 때도 안전합니다."}
            ],
            "magicSentences": [
                {"en": "Living near a subway station saves me a lot of commuting time.", "ko": "지하철역 근처에 살면 출퇴근 시간을 많이 절약해 줍니다.", "tip": "시계토끼 만능 #060 (위치·교통 선택 만능 이유)"},
                {"en": "It is very convenient for daily commuting.", "ko": "매일 출퇴근하기에 매우 편리합니다.", "tip": "주거지·오피스 위치 만능 마무리"}
            ],
            "vocabulary": [
                {"word": "proximity to", "ipa": "[prɑːkˈsɪməti tuː]", "pos": "명사구", "meaning": "~와의 가까움, 접근성"},
                {"word": "affordable rent", "ipa": "[əˈfɔːrdəbl rent]", "pos": "명사구", "meaning": "감당할 수 있는(저렴한) 집세"},
                {"word": "commuting time", "ipa": "[kəˈmjuːtɪŋ taɪm]", "pos": "명사구", "meaning": "통근/통학 시간"}
            ],
            "explanation": "집·호텔·사무실 선택 시 '위치/교통(location / public transit)'이 보기에 있다면 무조건 그것을 선택해 'saves commuting time(이동 시간 절약)'으로 푸는 것이 가장 빠릅니다."
        },
        {
            "id": "p3-new-22",
            "part": 3,
            "qNum": "#46",
            "typeId": "p3-t4",
            "typeName": "3자택일 최적 선택",
            "typeBadge": "3자택일 최적 선택",
            "topic": "호텔·숙소 예약 시 가장 중요한 기준 (Booking a Hotel)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When booking a hotel for a trip, what is the most important factor to you: room cleanliness, central location, or price?",
            "questionKo": "여행을 위해 호텔을 예약할 때 가장 중요한 요소는 무엇인가요: 객실 청결도, 중심가 위치, 가격?",
            "sentences": [
                {"step": "1. 최우선 요소 선택", "en": "When booking a hotel for a trip, room cleanliness is the most important factor to me.", "ko": "여행용 호텔을 예약할 때 저에게 가장 중요한 요소는 객실 청결도입니다."},
                {"step": "2. 핵심 이유 제시", "en": "If the bedsheets or bathroom are dirty, I cannot relax comfortably after a long day of sightseeing.", "ko": "침대 시트나 욕실이 지저분하면 하루 종일 관광을 마친 뒤에 편안하게 쉴 수가 없습니다."},
                {"step": "3. 부연 마무리", "en": "Therefore, I always check guest photos and cleanliness ratings carefully before making a reservation.", "ko": "따라서 저는 예약하기 전에 항상 투숙객 사진과 청결도 평점을 꼼꼼히 확인합니다."}
            ],
            "magicSentences": [
                {"en": "Room cleanliness is the most important factor to me.", "ko": "객실 청결도가 저에게 가장 중요한 요소입니다.", "tip": "숙소·시설 선택 만능 기준"},
                {"en": "I always check online reviews and ratings before booking.", "ko": "예약 전에 항상 온라인 리뷰와 평점을 확인합니다.", "tip": "시계토끼 만능 #074 (리뷰 확인 만능 문장)"}
            ],
            "vocabulary": [
                {"word": "cleanliness", "ipa": "[ˈklenlinəs]", "pos": "명사", "meaning": "청결, 깨끗함"},
                {"word": "sightseeing", "ipa": "[ˈsaɪtsiːɪŋ]", "pos": "명사", "meaning": "관광"},
                {"word": "make a reservation", "ipa": "[meɪk ə ˌrezərˈveɪʃn]", "pos": "숙어", "meaning": "예약하다"}
            ],
            "explanation": "호텔 선택 기준 질문은 청결도(cleanliness) 또는 위치(central location) 중 본인이 발음하기 편한 쪽을 골라 답변하세요."
        },
        {
            "id": "p3-new-23",
            "part": 3,
            "qNum": "#47",
            "typeId": "p3-t4",
            "typeName": "3자택일 최적 선택",
            "typeBadge": "3자택일 최적 선택",
            "topic": "지역 행사 홍보에 가장 효과적인 방법 (Promoting a Local Event)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "What is the most effective way to promote a local community event: social media ads, posters on streets, or local newspaper articles?",
            "questionKo": "지역 사회 행사를 홍보하는 가장 효과적인 방법은 무엇인가요: 소셜 미디어 광고, 거리 포스터, 지역 신문 기사?",
            "sentences": [
                {"step": "1. 최적 방법 선택", "en": "I think using social media ads is the most effective way to promote a local community event.", "ko": "지역 사회 행사를 홍보하는 데는 소셜 미디어 광고를 활용하는 것이 가장 효과적이라고 생각합니다."},
                {"step": "2. 이유 1 (높은 스마트폰 이용률)", "en": "Nowadays, almost everyone uses smartphones and checks social media such as Instagram and YouTube multiple times a day.", "ko": "요즘은 거의 모든 사람이 스마트폰을 사용하고 인스타그램이나 유튜브 같은 소셜 미디어를 하루에도 여러 번 확인합니다."},
                {"step": "3. 이유 2 (빠른 공유 및 비용 효율)", "en": "Also, people can easily share the event information with their friends for free.", "ko": "게다가 사람들이 행사 정보를 친구들에게 무료로 쉽게 공유할 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "Almost everyone uses smartphones and checks social media every day.", "ko": "거의 모든 사람이 매일 스마트폰을 쓰고 소셜 미디어를 확인합니다.", "tip": "시계토끼 만능 #160 (홍보·마케팅 질문 절대 만능)"},
                {"en": "People can easily share information with their friends.", "ko": "사람들이 친구들과 정보를 쉽게 공유할 수 있습니다.", "tip": "SNS 홍보 파급력 핵심 표현"}
            ],
            "vocabulary": [
                {"word": "effective", "ipa": "[ɪˈfektɪv]", "pos": "형용사", "meaning": "효과적인"},
                {"word": "promote", "ipa": "[prəˈmoʊt]", "pos": "동사", "meaning": "홍보하다, 촉진하다"},
                {"word": "multiple times", "ipa": "[ˈmʌltɪpl taɪmz]", "pos": "부사구", "meaning": "여러 번"}
            ],
            "explanation": "홍보·광고 수단(SNS vs TV vs 전단지/신문)을 묻는 3자택일 문제는 무조건 'social media ads'를 고르세요! Part 5에서도 그대로 쓸 수 있는 핵심 템플릿입니다."
        },
        {
            "id": "p3-new-24",
            "part": 3,
            "qNum": "#48",
            "typeId": "p3-t4",
            "typeName": "3자택일 최적 선택",
            "typeBadge": "3자택일 최적 선택",
            "topic": "팀 프로젝트 리더에게 가장 중요한 자질 (Team Leader Quality)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Which quality is the most important for a team leader: communication skills, professional knowledge, or decisiveness?",
            "questionKo": "팀 리더에게 가장 중요한 자질은 무엇인가요: 의사소통 능력, 전문 지식, 결단력?",
            "sentences": [
                {"step": "1. 최우선 자질 선택", "en": "Among the three qualities, I believe communication skills are the most important for a team leader.", "ko": "세 가지 자질 중 팀 리더에게는 의사소통 능력이 가장 중요하다고 생각합니다."},
                {"step": "2. 이유 1 (의견 조율 및 갈등 해결)", "en": "A good leader needs to listen carefully to team members' opinions and resolve conflicts smoothly.", "ko": "좋은 리더는 팀원들의 의견을 경청하고 갈등을 원만하게 해결해야 합니다."},
                {"step": "3. 이유 2 (팀워크 향상)", "en": "Clear communication builds strong teamwork and helps the team achieve its goal efficiently.", "ko": "명확한 소통은 탄탄한 팀워크를 구축하고 팀이 목표를 효율적으로 달성하도록 돕습니다."}
            ],
            "magicSentences": [
                {"en": "Communication skills are the most important quality for a leader.", "ko": "의사소통 능력은 리더에게 가장 중요한 자질입니다.", "tip": "리더·동료·직원 자질 질문 1순위 만능 답변"},
                {"en": "It builds strong teamwork and helps achieve goals efficiently.", "ko": "강한 팀워크를 만들고 목표를 효율적으로 달성하게 돕습니다.", "tip": "시계토끼 만능 #165 (비즈니스 협업 만능 결론)"}
            ],
            "vocabulary": [
                {"word": "communication skills", "ipa": "[kəˌmjuːnɪˈkeɪʃn skɪlz]", "pos": "명사구", "meaning": "의사소통 능력"},
                {"word": "decisiveness", "ipa": "[dɪˈsaɪsɪvnəs]", "pos": "명사", "meaning": "결단력"},
                {"word": "resolve conflicts", "ipa": "[rɪˈzɑːlv ˈkɑːnflɪkts]", "pos": "숙어", "meaning": "갈등을 해결하다"}
            ],
            "explanation": "리더나 동료의 자질을 묻는 문제는 Part 3와 Part 5 모두 단골 기출입니다. 언제나 'communication skills(소통 능력)'를 골라 팀워크(teamwork)로 풀어가세요."
        },

        # --- p3-t5: 장단점 중요 이유 (6문항 추가) ---
        {
            "id": "p3-new-25",
            "part": 3,
            "qNum": "#55",
            "typeId": "p3-t5",
            "typeName": "장단점 중요 이유",
            "typeBadge": "장단점 중요 이유",
            "topic": "외국어를 배우는 것의 장점 (Benefits of Learning a Foreign Language)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "What are the advantages of learning a foreign language?",
            "questionKo": "외국어를 배우는 것의 장점은 무엇인가요?",
            "sentences": [
                {"step": "1. 장점 1 (취업·커리어 기회)", "en": "First of all, learning a foreign language gives us more career opportunities in global companies.", "ko": "무엇보다도 외국어를 배우면 글로벌 기업에서 더 많은 취업 및 커리어 기회를 얻을 수 있습니다."},
                {"step": "2. 장점 2 (해외여행 및 문화 교류)", "en": "Second, when we travel abroad, we can communicate directly with local people and understand their culture deeply.", "ko": "둘째, 해외여행을 할 때 현지인들과 직접 소통하고 그들의 문화를 깊이 이해할 수 있습니다."},
                {"step": "3. 요약 마무리", "en": "Therefore, it broadens our horizons and makes traveling much more enjoyable.", "ko": "따라서 우리의 시야를 넓혀주고 여행을 훨씬 더 즐겁게 만들어 줍니다."}
            ],
            "magicSentences": [
                {"en": "It gives us more career opportunities.", "ko": "우리에게 더 많은 커리어(취업) 기회를 줍니다.", "tip": "시계토끼 만능 #168 (교육·자기계발 만능 장점)"},
                {"en": "It broadens our horizons and helps us understand other cultures.", "ko": "시야를 넓혀주고 다른 문화를 이해하도록 돕습니다.", "tip": "여행·어학·독서 공통 만능 표현"}
            ],
            "vocabulary": [
                {"word": "foreign language", "ipa": "[ˈfɔːrən ˈlæŋɡwɪdʒ]", "pos": "명사구", "meaning": "외국어"},
                {"word": "career opportunity", "ipa": "[kəˈrɪr ˌɑːpərˈtuːnəti]", "pos": "명사구", "meaning": "취업/경력 기회"},
                {"word": "broaden one's horizons", "ipa": "[ˈbrɔːdn wʌnz həˈraɪznz]", "pos": "숙어", "meaning": "시야(견문)를 넓히다"}
            ],
            "explanation": "외국어 학습의 장점은 1) 취업 기회 확대(more career opportunities), 2) 해외여행 시 현지인 소통(communicate with locals when traveling abroad) 두 가지로 정리하세요."
        },
        {
            "id": "p3-new-26",
            "part": 3,
            "qNum": "#56",
            "typeId": "p3-t5",
            "typeName": "장단점 중요 이유",
            "typeBadge": "장단점 중요 이유",
            "topic": "박물관·미술관 무료입장 정책의 장점 (Free Admission to Museums)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Why do you think it is important for museums to offer free admission to the public?",
            "questionKo": "박물관이 대중에게 무료입장을 제공하는 것이 왜 중요하다고 생각하나요?",
            "sentences": [
                {"step": "1. 핵심 이유 1 (교육 기회 평등)", "en": "Offering free admission is important because it allows everyone, especially students and families, to enjoy cultural education without financial burden.", "ko": "무료입장을 제공하는 것은 특히 학생들과 가족들을 포함한 모든 사람이 경제적 부담 없이 문화 교육을 누릴 수 있게 해주므로 중요합니다."},
                {"step": "2. 핵심 이유 2 (방문객 증가 및 지역 활성화)", "en": "Also, it attracts more visitors and tourists, which helps revitalize the local economy.", "ko": "또한 더 많은 방문객과 관광객을 유치하여 지역 경제를 활성화하는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "Everyone can enjoy cultural education without financial burden.", "ko": "모두가 경제적 부담 없이 문화 교육을 누릴 수 있습니다.", "tip": "공공시설·무료 혜택 질문 만능 문장"},
                {"en": "It attracts more visitors and helps the local economy.", "ko": "더 많은 방문객을 유치하고 지역 경제에 도움을 줍니다.", "tip": "시계토끼 만능 #172 (지역 행사·관광 활성화 공식)"}
            ],
            "vocabulary": [
                {"word": "free admission", "ipa": "[friː ədˈmɪʃn]", "pos": "명사구", "meaning": "무료입장"},
                {"word": "financial burden", "ipa": "[faɪˈnænʃl ˈbɜːrdn]", "pos": "명사구", "meaning": "경제적 부담"},
                {"word": "revitalize", "ipa": "[ˌriːˈvaɪtəlaɪz]", "pos": "동사", "meaning": "활성화하다, 활력을 불어넣다"}
            ],
            "explanation": "박물관·도서관·공원 등 공공시설의 중요성을 물을 때는 'without financial burden(경제적 부담 없이)'이 만능 열쇠입니다."
        },
        {
            "id": "p3-new-27",
            "part": 3,
            "qNum": "#57",
            "typeId": "p3-t5",
            "typeName": "장단점 중요 이유",
            "typeBadge": "장단점 중요 이유",
            "topic": "온라인 쇼핑의 단점 및 주의점 (Disadvantages of Online Shopping)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "What are some disadvantages of shopping online for clothes or shoes?",
            "questionKo": "옷이나 신발을 온라인으로 쇼핑할 때의 단점은 무엇인가요?",
            "sentences": [
                {"step": "1. 단점 1 (착용 불가 및 사이즈 오류)", "en": "The biggest disadvantage of shopping online for clothes is that I cannot try them on in person.", "ko": "온라인 의류 쇼핑의 가장 큰 단점은 직접 입어볼 수 없다는 점입니다."},
                {"step": "2. 구체적 문제 설명", "en": "Sometimes the actual size, color, or fabric quality looks quite different from the photos on the screen.", "ko": "가끔 실제 사이즈나 색상, 원단 품질이 화면 속 사진과 꽤 다르게 보일 때가 있습니다."},
                {"step": "3. 단점 2 (반품·교환 번거로움)", "en": "Also, returning or exchanging items takes extra time and shipping fees.", "ko": "또한 상품을 반품하거나 교환하는 데 추가 시간과 배송비가 듭니다."}
            ],
            "magicSentences": [
                {"en": "I cannot try them on in person before buying.", "ko": "구매 전에 직접 입어볼(착용해 볼) 수 없습니다.", "tip": "온라인 쇼핑 단점 1순위 필수 표현"},
                {"en": "Returning or exchanging items is inconvenient and takes time.", "ko": "반품이나 교환이 번거롭고 시간이 걸립니다.", "tip": "온라인 구매 단점 마무리 공식"}
            ],
            "vocabulary": [
                {"word": "try on", "ipa": "[traɪ ɑːn]", "pos": "숙어", "meaning": "(옷·신발을) 입어보다, 신어보다"},
                {"word": "in person", "ipa": "[ɪn ˈpɜːrsn]", "pos": "부사구", "meaning": "직접, 실제로"},
                {"word": "shipping fee", "ipa": "[ˈʃɪpɪŋ fiː]", "pos": "명사구", "meaning": "배송비"}
            ],
            "explanation": "온라인 쇼핑의 단점(disadvantages)을 물어볼 때는 'cannot try them on in person(직접 입어볼 수 없다)'과 'returning takes time(반품에 시간이 걸린다)' 두 문장이면 끝납니다."
        },
        {
            "id": "p3-new-28",
            "part": 3,
            "qNum": "#58",
            "typeId": "p3-t5",
            "typeName": "장단점 중요 이유",
            "typeBadge": "장단점 중요 이유",
            "topic": "사내 직원 휴게 공간·카페테리아 제공의 장점 (Employee Lounge)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "What are the benefits of having a comfortable lounge or cafeteria for employees in an office?",
            "questionKo": "사무실 내에 직원을 위한 편안한 휴게 공간이나 카페테리아를 두는 것의 장점은 무엇인가요?",
            "sentences": [
                {"step": "1. 장점 1 (휴식 및 재충전)", "en": "First, employees can take a short break with a cup of coffee and recharge their energy during work hours.", "ko": "첫째, 직원들이 근무 시간 중에 커피 한 잔과 함께 짧은 휴식을 취하며 에너지를 재충전할 수 있습니다."},
                {"step": "2. 장점 2 (타 부서 소통 및 창의성)", "en": "Second, they can chat naturally with coworkers from other departments, which improves communication and teamwork.", "ko": "둘째, 다른 부서 동료들과 자연스럽게 대화를 나눌 수 있어 소통과 팀워크가 향상됩니다."},
                {"step": "3. 결론 마무리", "en": "As a result, it increases job satisfaction and overall work productivity.", "ko": "결과적으로 직무 만족도와 전반적인 업무 생산성을 높여줍니다."}
            ],
            "magicSentences": [
                {"en": "Employees can take a break and recharge their energy.", "ko": "직원들이 휴식을 취하고 에너지를 재충전할 수 있습니다.", "tip": "사내 복지·휴식 질문 만능 문장"},
                {"en": "It increases job satisfaction and work productivity.", "ko": "직무 만족도와 업무 생산성을 높여줍니다.", "tip": "시계토끼 만능 #162 (직장·오피스 질문 만능 결론)"}
            ],
            "vocabulary": [
                {"word": "recharge one's energy", "ipa": "[ˌriːˈtʃɑːrdʒ wʌnz ˈenərdʒi]", "pos": "숙어", "meaning": "에너지를 재충전하다"},
                {"word": "job satisfaction", "ipa": "[dʒɑːb ˌsætɪsˈfækʃn]", "pos": "명사구", "meaning": "직무 만족도"},
                {"word": "productivity", "ipa": "[ˌproʊdʌkˈtɪvəti]", "pos": "명사", "meaning": "생산성"}
            ],
            "explanation": "사내 복지(휴게실, 유연근무제, 간식 제공 등)의 장점을 묻는 모든 질문에는 'recharge energy' + 'increase job satisfaction and productivity' 공식을 쓰세요."
        },
        {
            "id": "p3-new-29",
            "part": 3,
            "qNum": "#59",
            "typeId": "p3-t5",
            "typeName": "장단점 중요 이유",
            "typeBadge": "장단점 중요 이유",
            "topic": "자전거 이용이 개인과 도시 환경에 주는 장점 (Riding a Bicycle)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Why is it beneficial for people to ride a bicycle for commuting or short trips?",
            "questionKo": "출퇴근이나 가까운 거리를 이동할 때 자전거를 타는 것이 왜 유익한가요?",
            "sentences": [
                {"step": "1. 장점 1 (개인 건강 및 운동)", "en": "First, riding a bicycle is a great cardiovascular exercise that helps people stay fit and healthy in their busy daily lives.", "ko": "첫째, 자전거 타기는 바쁜 일상 속에서 건강과 체력을 유지하도록 돕는 훌륭한 유산소 운동입니다."},
                {"step": "2. 장점 2 (비용 절감 및 친환경)", "en": "Second, it saves transportation costs and is eco-friendly because it does not produce air pollution or traffic jams.", "ko": "둘째, 교통비를 절약해 주고 대기 오염이나 교통 체증을 유발하지 않아 친환경적입니다."}
            ],
            "magicSentences": [
                {"en": "It helps people stay healthy and saves transportation costs.", "ko": "건강을 유지하도록 돕고 교통비를 절약해 줍니다.", "tip": "자전거·도보·대중교통 장점 만능 공식"},
                {"en": "It is eco-friendly because it reduces air pollution.", "ko": "대기 오염을 줄여주기 때문에 친환경적입니다.", "tip": "시계토끼 만능 #175 (친환경 만능 문장)"}
            ],
            "vocabulary": [
                {"word": "beneficial", "ipa": "[ˌbenɪˈfɪʃl]", "pos": "형용사", "meaning": "유익한, 이로운"},
                {"word": "transportation cost", "ipa": "[ˌtrænspərˈteɪʃn kɔːst]", "pos": "명사구", "meaning": "교통비"},
                {"word": "air pollution", "ipa": "[er pəˈluːʃn]", "pos": "명사구", "meaning": "대기 오염"}
            ],
            "explanation": "자전거/대중교통의 장점은 1) 건강·비용 절감(stay healthy & save money), 2) 환경 보호(eco-friendly, reduce air pollution)로 묶으면 완벽합니다."
        },
        {
            "id": "p3-new-30",
            "part": 3,
            "qNum": "#60",
            "typeId": "p3-t5",
            "typeName": "장단점 중요 이유",
            "typeBadge": "장단점 중요 이유",
            "topic": "소비자가 상품 구매 전 온라인 리뷰를 읽는 이유 (Reading Online Reviews)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Why do many customers read online reviews before purchasing a product or service?",
            "questionKo": "많은 소비자들이 상품이나 서비스를 구매하기 전에 온라인 리뷰를 읽는 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 핵심 이유 1 (실제 품질 확인)", "en": "Customers read online reviews because they want to get honest information from real users about the product's actual quality.", "ko": "소비자들은 제품의 실제 품질에 대해 실사용자들의 솔직한 정보를 얻고 싶기 때문에 온라인 리뷰를 읽습니다."},
                {"step": "2. 핵심 이유 2 (실패 없는 현명한 소비)", "en": "Advertisements only show good sides, so checking reviews helps people avoid bad products and make a smart purchasing decision.", "ko": "광고는 좋은 면만 보여주기 때문에, 리뷰를 확인하면 불량 제품을 피하고 현명한 구매 결정을 내리는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "People can get honest information from real users.", "ko": "실사용자로부터 솔직한 정보를 얻을 수 있습니다.", "tip": "시계토끼 만능 #074 (온라인 리뷰 핵심 이유)"},
                {"en": "It helps people avoid wasting money and make a smart decision.", "ko": "돈 낭비를 피하고 현명한 결정을 내리도록 돕습니다.", "tip": "소비·쇼핑 판단 만능 결론"}
            ],
            "vocabulary": [
                {"word": "honest information", "ipa": "[ˈɑːnɪst ˌɪnfərˈmeɪʃn]", "pos": "명사구", "meaning": "솔직한 정보"},
                {"word": "real user", "ipa": "[ˈriːəl ˈjuːzər]", "pos": "명사구", "meaning": "실사용자"},
                {"word": "purchasing decision", "ipa": "[ˈpɜːrtʃəsɪŋ dɪˈsɪʒn]", "pos": "명사구", "meaning": "구매 결정"}
            ],
            "explanation": "온라인 리뷰의 중요성 질문은 'get honest information from real users(실사용자의 솔직한 정보 획득)' + 'avoid wasting money(돈 낭비 방지)' 두 문장으로 깔끔하게 답하세요."
        }
    ]



def get_new_part4_sets():
    """8개 표 속성별 1세트(4문항)씩 총 8세트(32문항) 추가 (Set 9 ~ Set 16)"""
    return [
        # Set 9: table-conf (컨퍼런스·학술 심포지엄)
        {
            "id": "p4-set9",
            "part": 4,
            "setNum": "Set 9",
            "tableTypeId": "table-conf",
            "tableTypeName": "컨퍼런스·학술 심포지엄",
            "tableTypeBadge": "컨퍼런스·학술 심포지엄",
            "topic": "2026 International Green Energy Symposium",
            "prepTime": 45,
            "scheduleTable": {
                "headerTitle": "2026 International Green Energy Symposium",
                "metaInfo": [
                    {"label": "Date & Location", "value": "December 4, 2026 / Pacific Convention Center, Hall B"},
                    {"label": "Ticket Price", "value": "$100 (Free for university students with a valid student ID)"}
                ],
                "rows": [
                    {"date": "09:00 AM", "time": "Opening Remarks", "event": "Future of Solar Power", "location": "Auditorium 1", "note": "Speaker: Dr. Alan Grant"},
                    {"date": "10:30 AM", "time": "Breakout Session", "event": "Electric Vehicle Battery Tech", "location": "Room 102", "note": "Speaker: Elena Rostova"},
                    {"date": "01:30 PM", "time": "Special Forum", "event": "Wind Energy Policy", "location": "Room 205 (Moved from Room 102)", "note": "Speaker: Marcus Vance"},
                    {"date": "03:30 PM", "time": "Workshop", "event": "Zero-Carbon Smart Cities", "location": "Auditorium 1", "note": "Speaker: Elena Rostova"}
                ]
            },
            "questions": [
                {
                    "qId": "p4-s9-q8",
                    "qNum": "Question 8",
                    "topic": "심포지엄 개최 일시·장소 및 대학생 참가비",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "When and where will the International Green Energy Symposium take place, and how much is the ticket for university students?",
                    "questionKo": "국제 그린 에너지 심포지엄은 언제 어디에서 열리며, 대학생 참가 티켓 가격은 얼마인가요?",
                    "sentences": [
                        {"step": "1. 일시 및 장소 안내", "en": "The International Green Energy Symposium will take place on December 4th at the Pacific Convention Center, Hall B.", "ko": "국제 그린 에너지 심포지엄은 12월 4일 퍼시픽 컨벤션 센터 B홀에서 열릴 예정입니다."},
                        {"step": "2. 대학생 무료 혜택", "en": "Also, the ticket is free for university students if they bring a valid student ID.", "ko": "또한 유효한 학생증을 지참한 대학생에게는 티켓이 무료입니다."}
                    ],
                    "magicSentences": [
                        {"en": "It will take place on December 4th at the Pacific Convention Center.", "ko": "12월 4일 퍼시픽 컨벤션 센터에서 열릴 예정입니다.", "tip": "시계토끼 만능 #097 (일시·장소 안내 공식)"},
                        {"en": "It is free of charge for university students with a valid ID.", "ko": "유효한 학생증이 있는 대학생에게는 무료입니다.", "tip": "할인·무료 조건 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "take place", "ipa": "[teɪk pleɪs]", "pos": "숙어", "meaning": "개최되다, 열리다"},
                        {"word": "valid", "ipa": "[ˈvælɪd]", "pos": "형용사", "meaning": "유효한"}
                    ],
                    "explanation": "상단 요약 정보(Date & Location)와 참가비 괄호 조건(Free for university students)을 정확히 짚어 읽어주세요."
                },
                {
                    "qId": "p4-s9-q9",
                    "qNum": "Question 9",
                    "topic": "장소 변경 세션 확인 (Q9 단골 유형)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "I heard that the afternoon forum on Wind Energy Policy will be held in Room 102. Is that right?",
                    "questionKo": "오후에 열리는 풍력 에너지 정책 포럼이 102호에서 열린다고 들었는데 맞나요?",
                    "sentences": [
                        {"step": "1. 오류 정정", "en": "No, actually, there has been a change in the room location.", "ko": "아니요, 사실 강의실 위치에 변경 사항이 있습니다."},
                        {"step": "2. 정확한 장소 및 시간 안내", "en": "The Special Forum on Wind Energy Policy led by Marcus Vance has been moved from Room 102 to Room 205, starting at 1:30 PM.", "ko": "마커스 밴스가 진행하는 풍력 에너지 정책 특별 포럼은 102호에서 205호로 변경되었으며, 오후 1시 30분에 시작합니다."}
                    ],
                    "magicSentences": [
                        {"en": "Actually, there has been a change in the schedule.", "ko": "사실 일정에 변경 사항이 있습니다.", "tip": "시계토끼 만능 #128 (Q9 오류 정정 첫 문장)"},
                        {"en": "It has been moved from Room 102 to Room 205.", "ko": "102호에서 205호로 장소가 이동되었습니다.", "tip": "장소 변경(Moved from) 필수 수동태 표현"}
                    ],
                    "vocabulary": [
                        {"word": "moved from A to B", "ipa": "[muːvd frʌm eɪ tuː biː]", "pos": "숙어", "meaning": "A에서 B로 이전된"}
                    ],
                    "explanation": "표에 'Moved from Room 102'가 보이면 9번 문제에서 100% 출제됩니다. 'No, actually it has been moved to Room 205'로 정정하세요."
                },
                {
                    "qId": "p4-s9-q10",
                    "qNum": "Question 10",
                    "topic": "특정 연사(Elena Rostova)의 전체 강연 일정 (Q10 2개 찾기)",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "I am a big fan of Elena Rostova. Could you tell me about all the sessions she will be leading?",
                    "questionKo": "저는 엘레나 로스토바의 팬입니다. 그녀가 진행하는 모든 세션에 대해 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 제시", "en": "Sure, Elena Rostova will be leading two sessions at the symposium.", "ko": "네, 엘레나 로스토바는 이번 심포지엄에서 두 개의 세션을 진행할 예정입니다."},
                        {"step": "2. 첫 번째 세션", "en": "First, at 10:30 AM, she will lead a Breakout Session on Electric Vehicle Battery Tech in Room 102.", "ko": "첫째, 오전 10시 30분에 102호에서 전기차 배터리 기술에 관한 분과 세션을 진행합니다."},
                        {"step": "3. 두 번째 세션", "en": "Second, at 3:30 PM, she will lead a Workshop on Zero-Carbon Smart Cities in Auditorium 1.", "ko": "둘째, 오후 3시 30분에 제1강당에서 제로 카본 스마트 시티에 관한 워크숍을 진행합니다."}
                    ],
                    "magicSentences": [
                        {"en": "Sure, she will be leading two sessions.", "ko": "네, 그녀는 두 개의 세션을 진행할 예정입니다.", "tip": "시계토끼 만능 #140 (Q10 2개 항목 도입 공식)"},
                        {"en": "First, at 10:30 AM, there is a session on ~ in Room 102.", "ko": "첫째, 오전 10시 30분에 102호에서 ~에 관한 세션이 있습니다.", "tip": "시각 + 주제 + 장소 3박자 공식"}
                    ],
                    "vocabulary": [
                        {"word": "breakout session", "ipa": "[ˈbreɪkaʊt ˈseʃn]", "pos": "명사구", "meaning": "분과 세션, 소그룹 강연"}
                    ],
                    "explanation": "우측 Note 열에서 'Elena Rostova'가 적힌 두 행(10:30 AM, 3:30 PM)을 찾아 시간, 제목, 장소를 차례대로 읽어주면 만점입니다."
                },
                {
                    "qId": "p4-s9-q11",
                    "qNum": "Question 11",
                    "topic": "오전 첫 세션(기조연설) 상세 안내",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Who is giving the opening remarks at 9:00 AM, and what is the topic?",
                    "questionKo": "오전 9시에 개회사를 맡은 연사는 누구이며, 주제는 무엇인가요?",
                    "sentences": [
                        {"step": "1. 연사 및 주제 안내", "en": "Dr. Alan Grant will be giving the opening remarks at 9:00 AM on the topic of Future of Solar Power.", "ko": "앨런 그랜트 박사가 오전 9시에 '태양광 발전의 미래'라는 주제로 개회사를 진행할 예정입니다."},
                        {"step": "2. 장소 부연", "en": "This session will be held in Auditorium 1.", "ko": "이 세션은 제1강당에서 열립니다."}
                    ],
                    "magicSentences": [
                        {"en": "It will be given by Dr. Alan Grant on the topic of ~.", "ko": "앨런 그랜트 박사가 ~라는 주제로 진행할 예정입니다.", "tip": "연사 및 주제 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "opening remarks", "ipa": "[ˈoʊpənɪŋ rɪˈmɑːrks]", "pos": "명사구", "meaning": "개회사"}
                    ],
                    "explanation": "9:00 AM 행의 연사(Dr. Alan Grant), 주제(Future of Solar Power), 장소(Auditorium 1)를 빠짐없이 읽어주세요."
                }
            ]
        },

        # Set 10: table-museum (박물관 전시·문화 강연)
        {
            "id": "p4-set10",
            "part": 4,
            "setNum": "Set 10",
            "tableTypeId": "table-museum",
            "tableTypeName": "박물관 전시·문화 강연",
            "tableTypeBadge": "박물관 전시·문화 강연",
            "topic": "Royal Science Museum - Weekend Family Day Schedule",
            "prepTime": 45,
            "scheduleTable": {
                "headerTitle": "Royal Science Museum - Weekend Family Day",
                "metaInfo": [
                    {"label": "Date & Hours", "value": "Saturday, November 21 / 10:00 AM – 06:00 PM"},
                    {"label": "Admission", "value": "Adults $15 / Children under 12: Free (Audio Guide Rental: $5)"}
                ],
                "rows": [
                    {"date": "10:30 AM", "time": "Special Exhibition", "event": "History of Space Exploration", "location": "1st Floor Main Gallery", "note": "Curator: Hannah Abbott"},
                    {"date": "01:00 PM", "time": "Kids Hands-on Class", "event": "Building Mini Robots", "location": "2nd Floor Science Lab", "note": "Instructor: Sam Carter (Pre-registration required)"},
                    {"date": "03:00 PM", "time": "3D Dome Screening", "event": "Deep Ocean Mysteries", "location": "B1 Planetarium", "note": "Canceled due to projector maintenance"},
                    {"date": "04:30 PM", "time": "Interactive Talk", "event": "Dinosaur Fossils Up Close", "location": "1st Floor Main Gallery", "note": "Curator: Hannah Abbott"}
                ]
            },
            "questions": [
                {
                    "qId": "p4-s10-q8",
                    "qNum": "Question 8",
                    "topic": "박물관 운영 시간 및 어린이 입장료·오디오 가이드 대여료",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "What are the museum's operating hours on Saturday, November 21st, and how much is admission for children under 12?",
                    "questionKo": "11월 21일 토요일 박물관 운영 시간은 어떻게 되며, 12세 미만 어린이 입장료는 얼마인가요?",
                    "sentences": [
                        {"step": "1. 운영 시간 안내", "en": "On Saturday, November 21st, the Royal Science Museum is open from 10:00 AM to 6:00 PM.", "ko": "11월 21일 토요일에 로열 과학 박물관은 오전 10시부터 오후 6시까지 운영됩니다."},
                        {"step": "2. 어린이 입장료 및 부가 정보", "en": "Admission is free for children under 12, while adult tickets are 15 dollars.", "ko": "12세 미만 어린이는 입장료가 무료이며, 성인 티켓은 15달러입니다."}
                    ],
                    "magicSentences": [
                        {"en": "The museum is open from 10:00 AM to 6:00 PM.", "ko": "박물관은 오전 10시부터 오후 6시까지 문을 엽니다.", "tip": "시계토끼 만능 #108 (운영 시간 안내 공식)"},
                        {"en": "Admission is free for children under 12.", "ko": "12세 미만 어린이는 입장료가 무료입니다.", "tip": "입장료 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "operating hours", "ipa": "[ˈɑːpəreɪtɪŋ ˈaʊərz]", "pos": "명사구", "meaning": "운영 시간"},
                        {"word": "admission", "ipa": "[ədˈmɪʃn]", "pos": "명사", "meaning": "입장료"}
                    ],
                    "explanation": "운영 시간(from 10:00 AM to 6:00 PM)과 12세 미만 무료(free for children under 12) 정보를 차례로 읽어주세요."
                },
                {
                    "qId": "p4-s10-q9",
                    "qNum": "Question 9",
                    "topic": "취소된 상영회 확인 (Q9 Canceled 유형)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "My kids really want to watch the 3D Dome Screening of Deep Ocean Mysteries at 3:00 PM. Can we attend that session?",
                    "questionKo": "아이들이 오후 3시에 심해의 신비 3D 돔 상영회를 꼭 보고 싶어 하는데, 참석할 수 있나요?",
                    "sentences": [
                        {"step": "1. 참석 불가 안내", "en": "I'm sorry, but you cannot attend that screening.", "ko": "죄송하지만 그 상영회에는 참석하실 수 없습니다."},
                        {"step": "2. 취소 사유 설명", "en": "The 3D Dome Screening of Deep Ocean Mysteries scheduled for 3:00 PM at the B1 Planetarium has been canceled due to projector maintenance.", "ko": "지하 1층 플라네타리움에서 오후 3시에 예정되어 있던 '심해의 신비' 3D 돔 상영회는 프로젝터 점검으로 인해 취소되었습니다."}
                    ],
                    "magicSentences": [
                        {"en": "I'm sorry, but that session has been canceled.", "ko": "죄송하지만 그 세션은 취소되었습니다.", "tip": "시계토끼 만능 #131 (취소 일정 안내 필수 표현)"},
                        {"en": "It was canceled due to projector maintenance.", "ko": "프로젝터 점검 때문에 취소되었습니다.", "tip": "취소 사유(due to ~) 읽기"}
                    ],
                    "vocabulary": [
                        {"word": "projector maintenance", "ipa": "[prəˈdʒektər ˈmeɪntənəns]", "pos": "명사구", "meaning": "프로젝터 보수 점검"}
                    ],
                    "explanation": "표에 'Canceled due to ~'가 있으면 무조건 9번 문제입니다. 'has been canceled due to projector maintenance'를 그대로 읽어주세요."
                },
                {
                    "qId": "p4-s10-q10",
                    "qNum": "Question 10",
                    "topic": "1층 메인 갤러리(1st Floor Main Gallery)에서 열리는 모든 프로그램 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Could you tell me about all the events taking place in the 1st Floor Main Gallery?",
                    "questionKo": "1층 메인 갤러리에서 진행되는 모든 행사에 대해 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 제시", "en": "Sure, there are two events taking place in the 1st Floor Main Gallery, both led by Curator Hannah Abbott.", "ko": "네, 1층 메인 갤러리에서는 해나 애벗 큐레이터가 진행하는 두 개의 행사가 열립니다."},
                        {"step": "2. 첫 번째 행사", "en": "First, at 10:30 AM, there is a Special Exhibition titled History of Space Exploration.", "ko": "첫째, 오전 10시 30분에 '우주 탐사의 역사'라는 제목의 특별전이 열립니다."},
                        {"step": "3. 두 번째 행사", "en": "Second, at 4:30 PM, there will be an Interactive Talk on Dinosaur Fossils Up Close.", "ko": "둘째, 오후 4시 30분에 '공룡 화석 가까이 보기'에 관한 참여형 강연이 진행됩니다."}
                    ],
                    "magicSentences": [
                        {"en": "Sure, there are two events taking place in the 1st Floor Main Gallery.", "ko": "네, 1층 메인 갤러리에서 열리는 행사가 두 개 있습니다.", "tip": "장소 기준 필터링 도입 공식"}
                    ],
                    "vocabulary": [
                        {"word": "space exploration", "ipa": "[speɪs ˌekspləˈreɪʃn]", "pos": "명사구", "meaning": "우주 탐사"},
                        {"word": "fossil", "ipa": "[ˈfɑːsl]", "pos": "명사", "meaning": "화석"}
                    ],
                    "explanation": "Location 열에서 '1st Floor Main Gallery'인 두 행(10:30 AM, 4:30 PM)을 찾아 시간, 프로그램 종류, 제목을 읽어주세요."
                },
                {
                    "qId": "p4-s10-q11",
                    "qNum": "Question 11",
                    "topic": "오후 1시 어린이 로봇 만들기 수업 신청 조건 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "What time does the Building Mini Robots class start, and is there anything I should know before attending?",
                    "questionKo": "미니 로봇 만들기 수업은 몇 시에 시작하며, 참석 전에 알아두어야 할 사항이 있나요?",
                    "sentences": [
                        {"step": "1. 시간 및 장소 안내", "en": "The Kids Hands-on Class on Building Mini Robots starts at 1:00 PM in the 2nd Floor Science Lab.", "ko": "미니 로봇 만들기 어린이 체험 수업은 2층 과학 실험실에서 오후 1시에 시작합니다."},
                        {"step": "2. 사전 등록 조건 안내", "en": "Please note that it is taught by Sam Carter and pre-registration is required.", "ko": "샘 카터 강사가 진행하며, 사전 등록이 필수라는 점을 참고하시기 바랍니다."}
                    ],
                    "magicSentences": [
                        {"en": "Please note that pre-registration is required.", "ko": "사전 등록이 필수라는 점을 참고해 주세요.", "tip": "시계토끼 만능 #122 (Note 주의사항 전달 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "hands-on", "ipa": "[hændz ɑːn]", "pos": "형용사", "meaning": "직접 해보는, 체험형의"},
                        {"word": "pre-registration", "ipa": "[ˌpriː redʒɪˈstreɪʃn]", "pos": "명사", "meaning": "사전 등록"}
                    ],
                    "explanation": "1:00 PM 행의 시작 시각, 장소(2nd Floor Science Lab), 그리고 Note의 'Pre-registration required'를 전달하면 만점입니다."
                }
            ]
        },

        # Set 11: table-training (사내 직원 연수·워크숍)
        {
            "id": "p4-set11",
            "part": 4,
            "setNum": "Set 11",
            "tableTypeId": "table-training",
            "tableTypeName": "사내 직원 연수·워크숍",
            "tableTypeBadge": "사내 직원 연수·워크숍",
            "topic": "Nova Tech - Annual Sales Team Training Workshop",
            "prepTime": 45,
            "scheduleTable": {
                "headerTitle": "Nova Tech - Annual Sales Team Training Workshop",
                "metaInfo": [
                    {"label": "Date & Venue", "value": "Friday, October 23 / 4th Floor Training Center"},
                    {"label": "Dress Code & Notice", "value": "Business Casual / Bring your company laptop"}
                ],
                "rows": [
                    {"date": "09:30 AM", "time": "Session 1", "event": "Global Market Analysis", "location": "Room A", "note": "Trainer: Director Paul Kim"},
                    {"date": "11:00 AM", "time": "Session 2", "event": "CRM Software Hands-on", "location": "Computer Lab", "note": "Trainer: IT Manager Clara Oswald"},
                    {"date": "02:00 PM", "time": "Session 3", "event": "Client Negotiation Skills", "location": "Room A", "note": "Trainer: Director Paul Kim"},
                    {"date": "04:00 PM", "time": "Session 4", "event": "B2B Presentation Coaching", "location": "Room B", "note": "Trainer: Guest Coach Ryan Gosling (Replaced Mina Park)"}
                ]
            },
            "questions": [
                {
                    "qId": "p4-s11-q8",
                    "qNum": "Question 8",
                    "topic": "연수 일시·장소 및 복장·준비물 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Where will the Annual Sales Team Training Workshop be held, and what should participants bring?",
                    "questionKo": "연례 영업팀 교육 워크숍은 어디에서 열리며, 참가자들은 무엇을 챙겨와야 하나요?",
                    "sentences": [
                        {"step": "1. 장소 및 날짜 안내", "en": "The Annual Sales Team Training Workshop will be held in the 4th Floor Training Center on Friday, October 23rd.", "ko": "연례 영업팀 교육 워크숍은 10월 23일 금요일 4층 연수 센터에서 열립니다."},
                        {"step": "2. 준비물 및 복장 규정 안내", "en": "Participants should bring their company laptop, and the dress code is business casual.", "ko": "참가자들은 회사 노트북을 지참해야 하며, 복장 규정은 비즈니스 캐주얼입니다."}
                    ],
                    "magicSentences": [
                        {"en": "You should bring your company laptop.", "ko": "회사 노트북을 가져오셔야 합니다.", "tip": "준비물 안내 공식"},
                        {"en": "The dress code is business casual.", "ko": "복장 규정은 비즈니스 캐주얼입니다.", "tip": "복장 규정(Dress Code) 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "dress code", "ipa": "[dres koʊd]", "pos": "명사구", "meaning": "복장 규정"},
                        {"word": "business casual", "ipa": "[ˈbɪznəs ˈkæʒuəl]", "pos": "명사구", "meaning": "비즈니스 캐주얼(단정한 평상복)"}
                    ],
                    "explanation": "상단 요약란의 장소(4th Floor Training Center)와 준비물(Bring your company laptop)을 정확히 읽어주세요."
                },
                {
                    "qId": "p4-s11-q9",
                    "qNum": "Question 9",
                    "topic": "강사 변경 확인 (Q9 Replaced 유형)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "I was told that Mina Park will be coaching the B2B Presentation session at 4:00 PM. Is that correct?",
                    "questionKo": "오후 4시에 미나 박이 B2B 프레젠테이션 코칭 세션을 진행한다고 들었는데 맞나요?",
                    "sentences": [
                        {"step": "1. 오류 정정", "en": "No, actually, the trainer for that session has been changed.", "ko": "아니요, 사실 해당 세션의 강사가 변경되었습니다."},
                        {"step": "2. 변경된 강사 안내", "en": "Guest Coach Ryan Gosling has replaced Mina Park and will lead the B2B Presentation Coaching session at 4:00 PM in Room B.", "ko": "초빙 코치 라이언 고슬링이 미나 박을 대신하여 오후 4시 B룸에서 B2B 프레젠테이션 코칭 세션을 진행할 예정입니다."}
                    ],
                    "magicSentences": [
                        {"en": "No, actually, the instructor has been changed.", "ko": "아니요, 사실 강사가 변경되었습니다.", "tip": "강사·연사 변경 정정 공식"},
                        {"en": "Ryan Gosling will lead the session instead of Mina Park.", "ko": "미나 박 대신 라이언 고슬링이 세션을 진행합니다.", "tip": "시계토끼 만능 #135 (instead of / replaced 표현)"}
                    ],
                    "vocabulary": [
                        {"word": "replace", "ipa": "[rɪˈpleɪs]", "pos": "동사", "meaning": "대신하다, 교체하다"}
                    ],
                    "explanation": "Note에 'Replaced Mina Park'라고 적혀 있으므로 'Ryan Gosling has replaced Mina Park(또는 will lead the session instead of Mina Park)'으로 답하세요."
                },
                {
                    "qId": "p4-s11-q10",
                    "qNum": "Question 10",
                    "topic": "Paul Kim 이사가 진행하는 모든 교육 세션 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Could you give me all the details of the sessions conducted by Director Paul Kim?",
                    "questionKo": "폴 킴 이사가 진행하는 모든 세션의 세부 정보를 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 및 장소 제시", "en": "Sure, Director Paul Kim will conduct two sessions, and both will take place in Room A.", "ko": "네, 폴 킴 이사는 두 개의 세션을 진행하며, 두 세션 모두 A룸에서 열립니다."},
                        {"step": "2. 첫 번째 세션", "en": "First, at 9:30 AM, he will lead Session 1 on Global Market Analysis.", "ko": "첫째, 오전 9시 30분에 글로벌 시장 분석에 관한 세션 1을 진행합니다."},
                        {"step": "3. 두 번째 세션", "en": "Second, at 2:00 PM, he will lead Session 3 on Client Negotiation Skills.", "ko": "둘째, 오후 2시에 고객 협상 기술에 관한 세션 3을 진행합니다."}
                    ],
                    "magicSentences": [
                        {"en": "Sure, he will conduct two sessions in Room A.", "ko": "네, 그는 A룸에서 두 개의 세션을 진행할 예정입니다.", "tip": "공통 장소 묶어 말하기 꿀팁"}
                    ],
                    "vocabulary": [
                        {"word": "negotiation skills", "ipa": "[nɪˌɡoʊʃiˈeɪʃn skɪlz]", "pos": "명사구", "meaning": "협상 기술"}
                    ],
                    "explanation": "Paul Kim이 진행하는 09:30 AM(Global Market Analysis)과 02:00 PM(Client Negotiation Skills) 두 세션을 차례대로 읽어주세요."
                },
                {
                    "qId": "p4-s11-q11",
                    "qNum": "Question 11",
                    "topic": "오전 11시 컴퓨터 실습실 세션 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "What session is scheduled at 11:00 AM, and where will it take place?",
                    "questionKo": "오전 11시에는 어떤 세션이 예정되어 있으며, 어디에서 열리나요?",
                    "sentences": [
                        {"step": "1. 세션명 및 장소 안내", "en": "At 11:00 AM, Session 2 on CRM Software Hands-on is scheduled in the Computer Lab.", "ko": "오전 11시에는 컴퓨터 실습실에서 CRM 소프트웨어 실습에 관한 세션 2가 예정되어 있습니다."},
                        {"step": "2. 강사 부연", "en": "It will be led by IT Manager Clara Oswald.", "ko": "이 세션은 클라라 오스왈드 IT 매니저가 진행합니다."}
                    ],
                    "magicSentences": [
                        {"en": "At 11:00 AM, there is a session on ~ in the Computer Lab.", "ko": "오전 11시에 컴퓨터 실습실에서 ~에 관한 세션이 있습니다.", "tip": "단일 일정 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "computer lab", "ipa": "[kəmˈpjuːtər læb]", "pos": "명사구", "meaning": "컴퓨터 실습실"}
                    ],
                    "explanation": "11:00 AM 행의 과목명(CRM Software Hands-on), 장소(Computer Lab), 강사(IT Manager Clara Oswald)를 읽어주세요."
                }
            ]
        },

        # Set 12: table-tour (여행·시티 투어 여정표)
        {
            "id": "p4-set12",
            "part": 4,
            "setNum": "Set 12",
            "tableTypeId": "table-tour",
            "tableTypeName": "여행·시티 투어 여정표",
            "tableTypeBadge": "여행·시티 투어 여정표",
            "topic": "Golden Valley Winery & Nature Bus Tour",
            "prepTime": 45,
            "scheduleTable": {
                "headerTitle": "Golden Valley Winery & Nature Bus Tour",
                "metaInfo": [
                    {"label": "Tour Date & Guide", "value": "Sunday, November 15 / Lead Guide: Lucas Meyer"},
                    {"label": "Meeting Point", "value": "Central Station Exit 4 at 08:30 AM (Bus departs strictly at 08:45 AM)"}
                ],
                "rows": [
                    {"date": "10:00 AM", "time": "Morning Stop", "event": "Pine Ridge Botanical Garden", "location": "Guided Walking Tour", "note": "Admission included"},
                    {"date": "12:30 PM", "time": "Lunch Break", "event": "Lakeside Grill Restaurant", "location": "Buffet Lunch", "note": "Vegetarian menu available"},
                    {"date": "02:30 PM", "time": "Afternoon Stop", "event": "Sunset Hill Winery", "location": "Cellar Tour & Wine Tasting", "note": "Must bring passport or ID"},
                    {"date": "05:00 PM", "time": "Evening Stop", "event": "Old Town Souvenir Market", "location": "Free Shopping Time", "note": "Canceled due to road construction"}
                ]
            },
            "questions": [
                {
                    "qId": "p4-s12-q8",
                    "qNum": "Question 8",
                    "topic": "투어 집결 장소·시각 및 버스 출발 시각",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Where and what time should we meet for the Golden Valley Bus Tour, and when does the bus depart?",
                    "questionKo": "골든 밸리 버스 투어를 위해 몇 시에 어디에서 만나야 하며, 버스는 언제 출발하나요?",
                    "sentences": [
                        {"step": "1. 집결 장소 및 시각", "en": "You should meet at Central Station Exit 4 at 8:30 AM on Sunday, November 15th.", "ko": "11월 15일 일요일 오전 8시 30분에 중앙역 4번 출구에서 만나셔야 합니다."},
                        {"step": "2. 버스 출발 시각 강조", "en": "Please don't be late because the bus departs strictly at 8:45 AM.", "ko": "버스가 오전 8시 45분 정각에 출발하므로 늦지 않도록 주의해 주세요."}
                    ],
                    "magicSentences": [
                        {"en": "We should meet at Central Station Exit 4 at 8:30 AM.", "ko": "오전 8시 30분에 중앙역 4번 출구에서 만나야 합니다.", "tip": "시계토끼 만능 #110 (투어 집결지 안내 공식)"},
                        {"en": "The bus departs strictly at 8:45 AM.", "ko": "버스는 8시 45분 정각에 출발합니다.", "tip": "출발 시각 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "meeting point", "ipa": "[ˈmiːtɪŋ pɔɪnt]", "pos": "명사구", "meaning": "집결 장소"},
                        {"word": "depart", "ipa": "[dɪˈpɑːrt]", "pos": "동사", "meaning": "출발하다"}
                    ],
                    "explanation": "투어 여정표의 8번 문제는 집결 장소(Meeting Point)와 출발 시각(departs at 8:45 AM)을 묻는 것이 정석입니다."
                },
                {
                    "qId": "p4-s12-q9",
                    "qNum": "Question 9",
                    "topic": "오후 5시 전통 시장 쇼핑 일정 취소 확인 (Q9)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "I am looking forward to buying gifts at the Old Town Souvenir Market at 5:00 PM. Will we still visit there?",
                    "questionKo": "오후 5시에 올드타운 기념품 시장에서 선물을 사고 싶은데, 예정대로 방문하나요?",
                    "sentences": [
                        {"step": "1. 방문 취소 안내", "en": "I'm sorry, but we will not be visiting the Old Town Souvenir Market.", "ko": "죄송하지만 올드타운 기념품 시장에는 방문하지 않을 예정입니다."},
                        {"step": "2. 취소 사유 설명", "en": "The evening stop at 5:00 PM for Free Shopping Time has been canceled due to road construction.", "ko": "오후 5시 자유 쇼핑 시간으로 예정된 저녁 코스는 도로 공사로 인해 취소되었습니다."}
                    ],
                    "magicSentences": [
                        {"en": "I'm sorry, but that stop has been canceled due to road construction.", "ko": "죄송하지만 그 코스는 도로 공사로 인해 취소되었습니다.", "tip": "시계토끼 만능 #131 (투어 일정 취소 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "souvenir", "ipa": "[ˌsuːvəˈnɪr]", "pos": "명사", "meaning": "기념품"},
                        {"word": "road construction", "ipa": "[roʊd kənˈstrʌkʃn]", "pos": "명사구", "meaning": "도로 공사"}
                    ],
                    "explanation": "5:00 PM 행의 Note에 있는 'Canceled due to road construction'을 그대로 읽어주며 방문 불가를 안내하세요."
                },
                {
                    "qId": "p4-s12-q10",
                    "qNum": "Question 10",
                    "topic": "식사 이후 진행되는 오후 일정 안내 및 준비물",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Could you tell me about the morning and afternoon sightseeing stops, excluding lunch and the canceled market?",
                    "questionKo": "점심 식사와 취소된 시장을 제외하고, 오전과 오후에 방문하는 관광 코스들에 대해 모두 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 제시", "en": "Sure, there are two main sightseeing stops in the morning and afternoon.", "ko": "네, 오전과 오후에 방문하는 주요 관광 코스는 두 곳입니다."},
                        {"step": "2. 오전 일정", "en": "First, at 10:00 AM, we will visit Pine Ridge Botanical Garden for a Guided Walking Tour, and admission is included.", "ko": "첫째, 오전 10시에 파인 리지 식물원을 방문해 가이드 워킹 투어를 진행하며, 입장료가 포함되어 있습니다."},
                        {"step": "3. 오후 일정", "en": "Second, at 2:30 PM, we will visit Sunset Hill Winery for a Cellar Tour and Wine Tasting, and you must bring your passport or ID.", "ko": "둘째, 오후 2시 30분에 선셋 힐 와이너리를 방문해 와인 저장고 투어 및 시음을 진행하며, 여권이나 신분증을 반드시 지참하셔야 합니다."}
                    ],
                    "magicSentences": [
                        {"en": "First, at 10:00 AM, we will visit ~ for a Guided Walking Tour.", "ko": "첫째, 오전 10시에 가이드 워킹 투어를 위해 ~를 방문합니다.", "tip": "투어 일정 안내 공식"},
                        {"en": "Please note that you must bring your passport or ID.", "ko": "여권이나 신분증을 반드시 챙기셔야 한다는 점을 참고해 주세요.", "tip": "필수 지참물 안내"}
                    ],
                    "vocabulary": [
                        {"word": "botanical garden", "ipa": "[bəˈtænɪkl ˈɡɑːrdn]", "pos": "명사구", "meaning": "식물원"},
                        {"word": "wine tasting", "ipa": "[waɪn ˈteɪstɪŋ]", "pos": "명사구", "meaning": "와인 시음"}
                    ],
                    "explanation": "점심(Lunch)과 취소된 5시 일정을 제외한 오전 10:00 AM 식물원 투어와 오후 2:30 PM 와이너리 투어 두 가지를 상세히 읽어주세요."
                },
                {
                    "qId": "p4-s12-q11",
                    "qNum": "Question 11",
                    "topic": "점심 식사 장소 및 채식주의자 메뉴 유무 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Where will we have lunch, and is there an option for vegetarians?",
                    "questionKo": "점심 식사는 어디에서 하며, 채식주의자를 위한 메뉴도 있나요?",
                    "sentences": [
                        {"step": "1. 점심 시간 및 식당 안내", "en": "We will have a buffet lunch at 12:30 PM at the Lakeside Grill Restaurant.", "ko": "오후 12시 30분에 레이크사이드 그릴 레스토랑에서 뷔페 점심 식사를 할 예정입니다."},
                        {"step": "2. 채식 메뉴 확인", "en": "And yes, a vegetarian menu is available there.", "ko": "그리고 네, 그곳에서 채식주의자 메뉴를 이용하실 수 있습니다."}
                    ],
                    "magicSentences": [
                        {"en": "Yes, a vegetarian menu is available.", "ko": "네, 채식 메뉴가 준비되어 있습니다.", "tip": "식단 옵션 확인 공식"}
                    ],
                    "vocabulary": [
                        {"word": "vegetarian", "ipa": "[ˌvedʒəˈteriən]", "pos": "명사/형용사", "meaning": "채식주의자(의)"}
                    ],
                    "explanation": "12:30 PM 행의 식당 이름(Lakeside Grill Restaurant), 식사 형태(Buffet Lunch), 그리고 Note의 'Vegetarian menu available'을 읽어주세요."
                }
            ]
        },

        # Set 13: table-interview (인사 채용 면접·이력 요약)
        {
            "id": "p4-set13",
            "part": 4,
            "setNum": "Set 13",
            "tableTypeId": "table-interview",
            "tableTypeName": "인사 채용 면접·이력 요약",
            "tableTypeBadge": "인사 채용 면접·이력 요약",
            "topic": "Global Logistics Dept - Final Job Interview Schedule",
            "prepTime": 45,
            "scheduleTable": {
                "headerTitle": "Global Logistics Dept - Final Job Interview Schedule",
                "metaInfo": [
                    {"label": "Interview Date & Room", "value": "Wednesday, November 11 / 8th Floor Interview Room B"},
                    {"label": "Interviewer", "value": "VP Sophia Martinez (Candidates must arrive 15 mins early)"}
                ],
                "rows": [
                    {"date": "10:00 AM", "time": "Candidate 1", "event": "Jason Bourne (5 yrs exp.)", "location": "In-person Interview", "note": "Fluent in Spanish & English"},
                    {"date": "11:00 AM", "time": "Candidate 2", "event": "Chloe Kim (3 yrs exp.)", "location": "Zoom Video Interview", "note": "Certified Supply Chain Analyst"},
                    {"date": "02:00 PM", "time": "Candidate 3", "event": "Liam Neeson (7 yrs exp.)", "location": "In-person Interview", "note": "Rescheduled to 04:30 PM today"},
                    {"date": "03:00 PM", "time": "Candidate 4", "event": "Emma Stone (4 yrs exp.)", "location": "Zoom Video Interview", "note": "Fluent in Mandarin & English"}
                ]
            },
            "questions": [
                {
                    "qId": "p4-s13-q8",
                    "qNum": "Question 8",
                    "topic": "면접 일시·장소 및 면접관·도착 유의사항",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Who is conducting the final interviews on Wednesday, November 11th, and where will they take place?",
                    "questionKo": "11월 11일 수요일 최종 면접은 누가 진행하며, 어디에서 열리나요?",
                    "sentences": [
                        {"step": "1. 면접관 및 장소 안내", "en": "Vice President Sophia Martinez will be conducting the final interviews in the 8th Floor Interview Room B on Wednesday, November 11th.", "ko": "11월 11일 수요일 8층 면접실 B에서 소피아 마르티네즈 부사장이 최종 면접을 진행할 예정입니다."},
                        {"step": "2. 도착 시간 안내", "en": "Also, all candidates must arrive 15 minutes early.", "ko": "또한 모든 지원자는 15분 일찍 도착해야 합니다."}
                    ],
                    "magicSentences": [
                        {"en": "The interviews will be conducted by VP Sophia Martinez in Interview Room B.", "ko": "면접은 소피아 마르티네즈 부사장이 면접실 B에서 진행합니다.", "tip": "면접관·장소 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "candidate", "ipa": "[ˈkændɪdət]", "pos": "명사", "meaning": "지원자, 후보자"},
                        {"word": "conduct an interview", "ipa": "[kənˈdʌkt ən ˈɪntərvjuː]", "pos": "숙어", "meaning": "면접을 진행하다"}
                    ],
                    "explanation": "상단 요약 정보의 면접관(VP Sophia Martinez), 장소(8th Floor Interview Room B), 주의사항(arrive 15 mins early)을 읽어주세요."
                },
                {
                    "qId": "p4-s13-q9",
                    "qNum": "Question 9",
                    "topic": "면접 시간 변경 확인 (Q9 Rescheduled 유형)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "We are interviewing Liam Neeson at 2:00 PM today, right?",
                    "questionKo": "오늘 오후 2시에 리암 니슨 지원자를 면접하는 것이 맞죠?",
                    "sentences": [
                        {"step": "1. 시간 변경 정정", "en": "No, actually, his interview time has been changed.", "ko": "아니요, 사실 그의 면접 시간이 변경되었습니다."},
                        {"step": "2. 변경된 시각 안내", "en": "The in-person interview with Liam Neeson, who has 7 years of experience, has been rescheduled from 2:00 PM to 4:30 PM today.", "ko": "7년 경력을 가진 리암 니슨과의 대면 면접은 오늘 오후 2시에서 오후 4시 30분으로 일정이 변경되었습니다."}
                    ],
                    "magicSentences": [
                        {"en": "No, actually, it has been rescheduled to 4:30 PM today.", "ko": "아니요, 사실 오늘 오후 4시 30분으로 일정이 변경되었습니다.", "tip": "시계토끼 만능 #129 (Rescheduled 시간 변경 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "reschedule", "ipa": "[ˌriːˈskedʒuːl]", "pos": "동사", "meaning": "일정을 변경하다"},
                        {"word": "in-person", "ipa": "[ˌɪn ˈpɜːrsn]", "pos": "형용사", "meaning": "대면의, 직접 만나는"}
                    ],
                    "explanation": "2:00 PM 행의 Note에 'Rescheduled to 04:30 PM today'가 있으므로 이를 정확히 짚어 정정해 주세요."
                },
                {
                    "qId": "p4-s13-q10",
                    "qNum": "Question 10",
                    "topic": "줌 화상 면접(Zoom Video Interview)으로 진행되는 지원자 전체 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Could you tell me about all the candidates who will have a Zoom Video Interview today?",
                    "questionKo": "오늘 줌 화상 면접을 보는 모든 지원자에 대해 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 인원 제시", "en": "Sure, there are two candidates who will have a Zoom Video Interview today.", "ko": "네, 오늘 줌 화상 면접을 진행하는 지원자는 두 명입니다."},
                        {"step": "2. 첫 번째 지원자", "en": "First, at 11:00 AM, we will interview Chloe Kim, who has 3 years of experience and is a Certified Supply Chain Analyst.", "ko": "첫째, 오전 11시에 3년 경력의 공인 공급망 분석가인 클로이 킴을 면접합니다."},
                        {"step": "3. 두 번째 지원자", "en": "Second, at 3:00 PM, we will interview Emma Stone, who has 4 years of experience and is fluent in Mandarin and English.", "ko": "둘째, 오후 3시에 4년 경력이 있고 중국어와 영어에 능통한 엠마 스톤을 면접합니다."}
                    ],
                    "magicSentences": [
                        {"en": "Sure, there are two candidates having a Zoom Video Interview.", "ko": "네, 줌 화상 면접을 보는 지원자는 두 명입니다.", "tip": "면접 방식 필터링 도입 공식"},
                        {"en": "She has 3 years of experience and is fluent in ~.", "ko": "그녀는 3년의 경력이 있으며 ~에 능통합니다.", "tip": "이력서 경력·특기 설명 공식"}
                    ],
                    "vocabulary": [
                        {"word": "fluent in", "ipa": "[ˈfluːənt ɪn]", "pos": "형용사구", "meaning": "~에 유창한, 능통한"},
                        {"word": "supply chain", "ipa": "[səˈplaɪ tʃeɪn]", "pos": "명사구", "meaning": "공급망, 물류망"}
                    ],
                    "explanation": "'5 yrs exp.'와 같은 약어는 반드시 'five years of experience'로 풀어서 읽어야 감점되지 않습니다!"
                },
                {
                    "qId": "p4-s13-q11",
                    "qNum": "Question 11",
                    "topic": "오전 10시 첫 번째 지원자 자격 요건 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Who is the first candidate at 10:00 AM, and what languages does he speak?",
                    "questionKo": "오전 10시 첫 번째 지원자는 누구이며, 어떤 언어를 구사하나요?",
                    "sentences": [
                        {"step": "1. 이름 및 경력 안내", "en": "The first candidate at 10:00 AM is Jason Bourne, who has 5 years of experience.", "ko": "오전 10시 첫 번째 지원자는 5년 경력을 가진 제이슨 본입니다."},
                        {"step": "2. 구사 언어 및 면접 형태", "en": "He will have an in-person interview, and he is fluent in Spanish and English.", "ko": "그는 대면 면접을 보며, 스페인어와 영어에 능통합니다."}
                    ],
                    "magicSentences": [
                        {"en": "He has 5 years of experience and is fluent in Spanish and English.", "ko": "그는 5년의 경력이 있고 스페인어와 영어에 유창합니다.", "tip": "지원자 스펙 요약 공식"}
                    ],
                    "vocabulary": [
                        {"word": "experience", "ipa": "[ɪkˈspɪriəns]", "pos": "명사", "meaning": "경력, 경험"}
                    ],
                    "explanation": "10:00 AM 행의 이름(Jason Bourne), 경력(5 years of experience), 언어 능력(Fluent in Spanish & English)을 연결해 답하세요."
                }
            ]
        },

        # Set 14: table-medical (병원·건강 세미나 일정표)
        {
            "id": "p4-set14",
            "part": 4,
            "setNum": "Set 14",
            "tableTypeId": "table-medical",
            "tableTypeName": "병원·건강 세미나 일정표",
            "tableTypeBadge": "병원·건강 세미나 일정표",
            "topic": "Hope General Hospital - Community Health Fair",
            "prepTime": 45,
            "scheduleTable": {
                "headerTitle": "Hope General Hospital - Community Health Fair",
                "metaInfo": [
                    {"label": "Date & Location", "value": "Saturday, November 28 / Main Lobby & 2F Auditorium"},
                    {"label": "Special Benefit", "value": "Free blood pressure check & gift bag for all visitors"}
                ],
                "rows": [
                    {"date": "10:00 AM", "time": "Health Lecture", "event": "Preventing Winter Flu", "location": "2F Auditorium", "note": "Dr. Gregory House"},
                    {"date": "11:30 AM", "time": "Nutrition Talk", "event": "Low-Sugar Diet Habits", "location": "Seminar Room 1", "note": "Dietitian: Rachel Green"},
                    {"date": "02:00 PM", "time": "Posture Clinic", "event": "Back Pain & Stretching", "location": "2F Auditorium", "note": "Dr. Meredith Grey"},
                    {"date": "03:30 PM", "time": "Dental Care", "event": "Healthy Teeth for Seniors", "location": "Seminar Room 2 (Moved from Seminar Room 1)", "note": "Dr. Gregory House"}
                ]
            },
            "questions": [
                {
                    "qId": "p4-s14-q8",
                    "qNum": "Question 8",
                    "topic": "건강 박람회 개최 일자·장소 및 방문객 무료 혜택",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "When will the Community Health Fair be held at Hope General Hospital, and what special benefit is provided to visitors?",
                    "questionKo": "호프 종합병원 지역 건강 박람회는 언제 열리며, 방문객들에게 어떤 특별 혜택이 제공되나요?",
                    "sentences": [
                        {"step": "1. 날짜 및 장소 안내", "en": "The Community Health Fair will be held on Saturday, November 28th in the Main Lobby and 2nd Floor Auditorium.", "ko": "지역 건강 박람회는 11월 28일 토요일 메인 로비와 2층 강당에서 열릴 예정입니다."},
                        {"step": "2. 방문객 특별 혜택", "en": "Also, all visitors will receive a free blood pressure check and a gift bag.", "ko": "또한 모든 방문객에게는 무료 혈압 검사와 기념품 가방이 제공됩니다."}
                    ],
                    "magicSentences": [
                        {"en": "All visitors will receive a free blood pressure check and a gift bag.", "ko": "모든 방문객은 무료 혈압 체크와 기프트 백을 받게 됩니다.", "tip": "무료 제공 혜택 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "blood pressure", "ipa": "[blʌd ˈpreʃər]", "pos": "명사구", "meaning": "혈압"},
                        {"word": "health fair", "ipa": "[helθ fer]", "pos": "명사구", "meaning": "건강 박람회"}
                    ],
                    "explanation": "상단 Date & Location과 Special Benefit 항목을 그대로 읽어주면 됩니다."
                },
                {
                    "qId": "p4-s14-q9",
                    "qNum": "Question 9",
                    "topic": "오후 3시 30분 치아 건강 강연 장소 변경 확인 (Q9)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "I heard the Dental Care session on Healthy Teeth for Seniors at 3:30 PM is in Seminar Room 1. Is that right?",
                    "questionKo": "오후 3시 30분에 열리는 어르신 치아 건강 세션이 제1세미나실에서 열린다고 들었는데 맞나요?",
                    "sentences": [
                        {"step": "1. 장소 오류 정정", "en": "No, actually, the room for that session has been changed.", "ko": "아니요, 사실 그 세션의 강의실이 변경되었습니다."},
                        {"step": "2. 정확한 장소 안내", "en": "The Dental Care session on Healthy Teeth for Seniors led by Dr. Gregory House at 3:30 PM has been moved from Seminar Room 1 to Seminar Room 2.", "ko": "오후 3시 30분 그레고리 하우스 박사가 진행하는 어르신 치아 건강 세션은 제1세미나실에서 제2세미나실로 이전되었습니다."}
                    ],
                    "magicSentences": [
                        {"en": "It has been moved from Seminar Room 1 to Seminar Room 2.", "ko": "제1세미나실에서 제2세미나실로 장소가 변경되었습니다.", "tip": "장소 이동 정정 공식"}
                    ],
                    "vocabulary": [
                        {"word": "senior", "ipa": "[ˈsiːniər]", "pos": "명사", "meaning": "어르신, 노인"}
                    ],
                    "explanation": "3:30 PM 행의 Location에 적힌 'Seminar Room 2 (Moved from Seminar Room 1)'를 정확히 읽어주세요."
                },
                {
                    "qId": "p4-s14-q10",
                    "qNum": "Question 10",
                    "topic": "2층 강당(2F Auditorium)에서 열리는 모든 강연 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Could you tell me about all the sessions taking place in the 2nd Floor Auditorium?",
                    "questionKo": "2층 강당에서 열리는 모든 세션에 대해 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 제시", "en": "Sure, there are two sessions taking place in the 2nd Floor Auditorium.", "ko": "네, 2층 강당에서 열리는 세션은 두 개입니다."},
                        {"step": "2. 첫 번째 세션", "en": "First, at 10:00 AM, there is a Health Lecture on Preventing Winter Flu led by Dr. Gregory House.", "ko": "첫째, 오전 10시에 그레고리 하우스 박사가 진행하는 겨울 독감 예방 건강 강연이 있습니다."},
                        {"step": "3. 두 번째 세션", "en": "Second, at 2:00 PM, there is a Posture Clinic on Back Pain and Stretching led by Dr. Meredith Grey.", "ko": "둘째, 오후 2시에 메러디스 그레이 박사가 진행하는 허리 통증과 스트레칭에 관한 자세 교정 클리닉이 있습니다."}
                    ],
                    "magicSentences": [
                        {"en": "Sure, there are two sessions in the 2nd Floor Auditorium.", "ko": "네, 2층 강당에서는 두 개의 세션이 열립니다.", "tip": "'2F'는 'second floor'로 풀어서 읽기"}
                    ],
                    "vocabulary": [
                        {"word": "prevent", "ipa": "[prɪˈvent]", "pos": "동사", "meaning": "예방하다"},
                        {"word": "posture", "ipa": "[ˈpɑːstʃər]", "pos": "명사", "meaning": "자세"}
                    ],
                    "explanation": "'2F'는 반드시 'second floor'로 읽어야 합니다. 10:00 AM과 2:00 PM 두 행을 차례로 읽어주세요."
                },
                {
                    "qId": "p4-s14-q11",
                    "qNum": "Question 11",
                    "topic": "오전 11시 30분 영양 강연 상세 안내",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "What topic will Dietitian Rachel Green talk about, and when does her session start?",
                    "questionKo": "레이첼 그린 영양사는 어떤 주제로 강연하며, 몇 시에 시작하나요?",
                    "sentences": [
                        {"step": "1. 주제 및 시작 시각 안내", "en": "Dietitian Rachel Green will give a Nutrition Talk on Low-Sugar Diet Habits starting at 11:30 AM.", "ko": "레이첼 그린 영양사는 오전 11시 30분부터 저당 식단 습관에 관한 영양 강연을 진행합니다."},
                        {"step": "2. 장소 부연", "en": "Her session will take place in Seminar Room 1.", "ko": "그녀의 세션은 제1세미나실에서 열립니다."}
                    ],
                    "magicSentences": [
                        {"en": "She will talk about Low-Sugar Diet Habits at 11:30 AM.", "ko": "그녀는 오전 11시 30분에 저당 식단 습관에 대해 이야기할 예정입니다.", "tip": "강연 주제·시각 답변 공식"}
                    ],
                    "vocabulary": [
                        {"word": "dietitian", "ipa": "[ˌdaɪəˈtɪʃn]", "pos": "명사", "meaning": "영양사"}
                    ],
                    "explanation": "11:30 AM 행의 주제(Low-Sugar Diet Habits), 시간(11:30 AM), 장소(Seminar Room 1)를 명확히 전달하세요."
                }
            ]
        },

        # Set 15: table-itinerary (비행·해외 출장 일정표)
        {
            "id": "p4-set15",
            "part": 4,
            "setNum": "Set 15",
            "tableTypeId": "table-itinerary",
            "tableTypeName": "비행·해외 출장 일정표",
            "tableTypeBadge": "비행·해외 출장 일정표",
            "topic": "Director Jessica Alba - Business Trip Itinerary to Tokyo",
            "prepTime": 45,
            "scheduleTable": {
                "headerTitle": "Jessica Alba - One-Day Business Trip to Tokyo",
                "metaInfo": [
                    {"label": "Travel Date & Flight", "value": "Tuesday, December 8 / Flight KE703 (Departs Seoul 08:00 AM -> Arrives Tokyo 10:20 AM)"},
                    {"label": "Hotel & Transport", "value": "Shinjuku Grand Hotel / Airport Limousine Bus reserved"}
                ],
                "rows": [
                    {"date": "12:00 PM", "time": "Business Lunch", "event": "Welcome Lunch with Branch Director", "location": "Ginza Sushi House", "note": "With Mr. Kenji Sato"},
                    {"date": "02:00 PM", "time": "Site Inspection", "event": "Tokyo Logistics Center Tour", "location": "Yokohama Warehouse", "note": "Safety helmet required"},
                    {"date": "04:30 PM", "time": "Contract Meeting", "event": "2027 Supply Contract Signing", "location": "Tokyo HQ Room 501", "note": "Delayed to 05:00 PM (Was 04:30 PM)"},
                    {"date": "07:00 PM", "time": "Networking Dinner", "event": "Dinner with Marketing Team", "location": "Shinjuku Grand Hotel", "note": "With Ms. Yuki Tanaka"}
                ]
            },
            "questions": [
                {
                    "qId": "p4-s15-q8",
                    "qNum": "Question 8",
                    "topic": "도쿄 출장 항공편 출발·도착 시각 및 숙소",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "What flight is Jessica Alba taking to Tokyo on December 8th, and when does it arrive?",
                    "questionKo": "제시카 알바는 12월 8일에 어떤 항공편으로 도쿄에 가며, 몇 시에 도착하나요?",
                    "sentences": [
                        {"step": "1. 항공편 및 출발·도착 시각 안내", "en": "On Tuesday, December 8th, Jessica Alba is taking Flight KE703, which departs from Seoul at 8:00 AM and arrives in Tokyo at 10:20 AM.", "ko": "12월 8일 화요일에 제시카 알바는 오전 8시에 서울에서 출발해 오전 10시 20분에 도쿄에 도착하는 KE703 항공편을 이용합니다."},
                        {"step": "2. 호텔 및 이동 수단 부연", "en": "Also, she will stay at the Shinjuku Grand Hotel and an airport limousine bus is reserved.", "ko": "또한 신주쿠 그랜드 호텔에 묵을 예정이며 공항 리무진 버스가 예약되어 있습니다."}
                    ],
                    "magicSentences": [
                        {"en": "She is taking Flight KE703, arriving in Tokyo at 10:20 AM.", "ko": "오전 10시 20분 도쿄에 도착하는 KE703편을 탑승합니다.", "tip": "시계토끼 만능 #115 (항공편 출도착 안내 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "itinerary", "ipa": "[aɪˈtɪnəreri]", "pos": "명사", "meaning": "여행/출장 일정표"},
                        {"word": "limousine bus", "ipa": "[ˈlɪməziːn bʌs]", "pos": "명사구", "meaning": "리무진 버스"}
                    ],
                    "explanation": "항공편명(Flight KE703)을 읽을 때는 'K-E-seven-oh-three' 또는 'seven-hundred-three'로 또박또박 읽고 도착 시각(10:20 AM)을 말해주세요."
                },
                {
                    "qId": "p4-s15-q9",
                    "qNum": "Question 9",
                    "topic": "계약 체결 회의 시간 연기 확인 (Q9 Delayed 유형)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "The 2027 Supply Contract Signing meeting is still starting at 4:30 PM, right?",
                    "questionKo": "2027년 공급 계약 서명 회의는 예정대로 오후 4시 30분에 시작하는 것이 맞죠?",
                    "sentences": [
                        {"step": "1. 시간 연기 정정", "en": "No, actually, the meeting has been delayed by 30 minutes.", "ko": "아니요, 사실 그 회의는 30분 연기되었습니다."},
                        {"step": "2. 변경된 시작 시각 안내", "en": "The 2027 Supply Contract Signing meeting in Tokyo HQ Room 501 has been delayed from 4:30 PM to 5:00 PM.", "ko": "도쿄 본사 501호에서 열리는 2027년 공급 계약 서명 회의는 오후 4시 30분에서 오후 5시로 연기되었습니다."}
                    ],
                    "magicSentences": [
                        {"en": "No, actually, the meeting has been delayed to 5:00 PM.", "ko": "아니요, 사실 회의가 오후 5시로 연기되었습니다.", "tip": "Delayed to ~ 시간 연기 정정 공식"}
                    ],
                    "vocabulary": [
                        {"word": "delayed", "ipa": "[dɪˈleɪd]", "pos": "형용사/과거분사", "meaning": "지연된, 연기된"},
                        {"word": "contract signing", "ipa": "[ˈkɑːntrækt ˈsaɪnɪŋ]", "pos": "명사구", "meaning": "계약 서명(체결)"}
                    ],
                    "explanation": "Note의 'Delayed to 05:00 PM (Was 04:30 PM)'을 보고 오후 5시로 늦춰졌음을 정확히 알려주세요."
                },
                {
                    "qId": "p4-s15-q10",
                    "qNum": "Question 10",
                    "topic": "출장 중 예정된 모든 식사(Lunch & Dinner) 일정 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Could you tell me about all the meal appointments scheduled on her itinerary?",
                    "questionKo": "그녀의 일정표에 잡혀 있는 모든 식사 약속에 대해 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 제시", "en": "Sure, there are two meal appointments scheduled on her itinerary.", "ko": "네, 일정표에는 두 건의 식사 약속이 예정되어 있습니다."},
                        {"step": "2. 점심 오찬 일정", "en": "First, at 12:00 PM, she will have a Welcome Lunch with the Branch Director, Mr. Kenji Sato, at Ginza Sushi House.", "ko": "첫째, 오후 12시에 긴자 스시 하우스에서 지사장인 사토 켄지 씨와 환영 오찬을 가집니다."},
                        {"step": "3. 저녁 만찬 일정", "en": "Second, at 7:00 PM, she will have a Networking Dinner with the Marketing Team and Ms. Yuki Tanaka at the Shinjuku Grand Hotel.", "ko": "둘째, 오후 7시에 신주쿠 그랜드 호텔에서 다나카 유키 씨 및 마케팅팀과 네트워킹 만찬을 가집니다."}
                    ],
                    "magicSentences": [
                        {"en": "Sure, there are two meal appointments: one lunch and one dinner.", "ko": "네, 점심과 저녁 총 두 건의 식사 약속이 있습니다.", "tip": "출장 식사 일정 묶기 공식"}
                    ],
                    "vocabulary": [
                        {"word": "meal appointment", "ipa": "[miːl əˈpɔɪntmənt]", "pos": "명사구", "meaning": "식사 약속"},
                        {"word": "branch director", "ipa": "[bræntʃ dəˈrektər]", "pos": "명사구", "meaning": "지사장"}
                    ],
                    "explanation": "'meal appointments(식사 약속)'라는 상위 개념어로 질문했을 때 표에서 Business Lunch(12:00 PM)와 Networking Dinner(7:00 PM) 두 개를 찾아내야 합니다."
                },
                {
                    "qId": "p4-s15-q11",
                    "qNum": "Question 11",
                    "topic": "오후 2시 물류 센터 현장 점검 일정 및 주의사항",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Where will the Site Inspection take place at 2:00 PM, and what is required?",
                    "questionKo": "오후 2시 현장 점검은 어디에서 진행되며, 무엇이 필요한가요?",
                    "sentences": [
                        {"step": "1. 일정 및 장소 안내", "en": "At 2:00 PM, the Site Inspection for the Tokyo Logistics Center Tour will take place at the Yokohama Warehouse.", "ko": "오후 2시 도쿄 물류 센터 투어를 위한 현장 점검은 요코하마 창고에서 진행됩니다."},
                        {"step": "2. 안전모 착용 안내", "en": "Please note that a safety helmet is required during the tour.", "ko": "투어 중에는 안전모 착용이 필수라는 점을 참고하시기 바랍니다."}
                    ],
                    "magicSentences": [
                        {"en": "Please note that a safety helmet is required.", "ko": "안전모가 필수라는 점을 참고해 주세요.", "tip": "현장 방문 필수 장비 안내"}
                    ],
                    "vocabulary": [
                        {"word": "site inspection", "ipa": "[saɪt ɪnˈspekʃn]", "pos": "명사구", "meaning": "현장 점검, 현장 시찰"},
                        {"word": "safety helmet", "ipa": "[ˈseɪfti ˈhelmɪt]", "pos": "명사구", "meaning": "안전모"}
                    ],
                    "explanation": "2:00 PM 행의 장소(Yokohama Warehouse)와 Note의 'Safety helmet required'를 빠짐없이 읽어주세요."
                }
            ]
        },

        # Set 16: table-fitness (스포츠·피트니스 강습표)
        {
            "id": "p4-set16",
            "part": 4,
            "setNum": "Set 16",
            "tableTypeId": "table-fitness",
            "tableTypeName": "스포츠·피트니스 강습표",
            "tableTypeBadge": "스포츠·피트니스 강습표",
            "topic": "Starlight Wellness Center - Weekend Yoga & Pilates Schedule",
            "prepTime": 45,
            "scheduleTable": {
                "headerTitle": "Starlight Wellness Center - Weekend Class Schedule",
                "metaInfo": [
                    {"label": "Monthly Membership", "value": "$120 per month (10% discount for 3-month registration)"},
                    {"label": "Center Notice", "value": "Free yoga mat rental / Bring your own water bottle"}
                ],
                "rows": [
                    {"date": "09:00 AM", "time": "Beginner Level", "event": "Morning Healing Yoga", "location": "Studio A", "note": "Instructor: Maya Lin"},
                    {"date": "11:00 AM", "time": "Intermediate", "event": "Core Reformer Pilates", "location": "Pilates Room", "note": "Instructor: Chloe Park (Class is Full)"},
                    {"date": "02:00 PM", "time": "All Levels", "event": "Foam Roller Stretching", "location": "Studio B", "note": "Instructor: Maya Lin"},
                    {"date": "04:00 PM", "time": "Advanced Level", "event": "Power Vinyasa Yoga", "location": "Studio A", "note": "Instructor: Noah Williams"}
                ]
            },
            "questions": [
                {
                    "qId": "p4-s16-q8",
                    "qNum": "Question 8",
                    "topic": "월 수강료·할인 혜택 및 요가 매트 대여 안내",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "How much is the monthly membership at Starlight Wellness Center, and is there any discount available?",
                    "questionKo": "스타라이트 웰니스 센터의 월 회원권 가격은 얼마이며, 이용 가능한 할인 혜택이 있나요?",
                    "sentences": [
                        {"step": "1. 월 회비 및 3개월 할인 안내", "en": "The monthly membership at Starlight Wellness Center is 120 dollars per month, and you can get a 10 percent discount if you register for 3 months.", "ko": "스타라이트 웰니스 센터의 월 회원권은 월 120달러이며, 3개월 등록 시 10% 할인을 받으실 수 있습니다."},
                        {"step": "2. 무료 대여 혜택 부연", "en": "Also, free yoga mat rental is provided, and you should bring your own water bottle.", "ko": "또한 무료 요가 매트 대여가 제공되며, 개인 물통을 지참하셔야 합니다."}
                    ],
                    "magicSentences": [
                        {"en": "It is 120 dollars per month, with a 10 percent discount for 3-month registration.", "ko": "월 120달러이며, 3개월 등록 시 10% 할인이 됩니다.", "tip": "수강료 및 기간 할인 공식"}
                    ],
                    "vocabulary": [
                        {"word": "membership", "ipa": "[ˈmembərʃɪp]", "pos": "명사", "meaning": "회원권, 멤버십"},
                        {"word": "yoga mat rental", "ipa": "[ˈjoʊɡə mæt ˈrentl]", "pos": "명사구", "meaning": "요가 매트 대여"}
                    ],
                    "explanation": "상단 Monthly Membership 가격($120)과 괄호 안의 3개월 등록 시 10% 할인 조건을 함께 읽어주세요."
                },
                {
                    "qId": "p4-s16-q9",
                    "qNum": "Question 9",
                    "topic": "정원 마감 강좌 확인 (Q9 Class is Full 유형)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "I'd like to sign up for the Core Reformer Pilates class at 11:00 AM. Can I still register for it?",
                    "questionKo": "오전 11시에 열리는 코어 리포머 필라테스 수업을 신청하고 싶은데, 지금도 등록할 수 있나요?",
                    "sentences": [
                        {"step": "1. 등록 불가 안내", "en": "I'm sorry, but you cannot register for that class anymore.", "ko": "죄송하지만 그 수업은 더 이상 등록하실 수 없습니다."},
                        {"step": "2. 마감 사유 설명", "en": "The Intermediate Core Reformer Pilates class at 11:00 AM taught by Chloe Park in the Pilates Room is already full.", "ko": "오전 11시 필라테스 룸에서 클로이 박 강사가 진행하는 중급 코어 리포머 필라테스 수업은 이미 정원이 마감되었습니다."}
                    ],
                    "magicSentences": [
                        {"en": "I'm sorry, but that class is already full.", "ko": "죄송하지만 그 수업은 이미 정원이 다 찼습니다.", "tip": "시계토끼 만능 #133 (Class is full 마감 안내 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "sign up for", "ipa": "[saɪn ʌp fɔːr]", "pos": "숙어", "meaning": "~을 수강 신청하다"},
                        {"word": "intermediate", "ipa": "[ˌɪntərˈmiːdiət]", "pos": "형용사", "meaning": "중급의"}
                    ],
                    "explanation": "피트니스·강습 표에서 'Class is Full(정원 마감)'이나 'Closed'는 9번 단골 출제 포인트입니다."
                },
                {
                    "qId": "p4-s16-q10",
                    "qNum": "Question 10",
                    "topic": "Maya Lin 강사가 담당하는 모든 수업 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Could you tell me about all the classes taught by Instructor Maya Lin?",
                    "questionKo": "마야 린 강사가 가르치는 모든 수업에 대해 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 제시", "en": "Sure, Instructor Maya Lin teaches two classes on the schedule.", "ko": "네, 마야 린 강사는 시간표에서 두 개의 수업을 담당하고 있습니다."},
                        {"step": "2. 첫 번째 수업", "en": "First, at 9:00 AM, she teaches a Beginner Level class called Morning Healing Yoga in Studio A.", "ko": "첫째, 오전 9시에 스튜디오 A에서 초급 과정인 모닝 힐링 요가 수업을 가르칩니다."},
                        {"step": "3. 두 번째 수업", "en": "Second, at 2:00 PM, she teaches an All Levels class called Foam Roller Stretching in Studio B.", "ko": "둘째, 오후 2시에 스튜디오 B에서 전 레벨 대상인 폼롤러 스트레칭 수업을 가르칩니다."}
                    ],
                    "magicSentences": [
                        {"en": "Sure, Instructor Maya Lin teaches two classes.", "ko": "네, 마야 린 강사는 두 개의 수업을 가르칩니다.", "tip": "강사 기준 필터링 도입 공식"}
                    ],
                    "vocabulary": [
                        {"word": "beginner level", "ipa": "[bɪˈɡɪnər ˈlevl]", "pos": "명사구", "meaning": "초급 단계"},
                        {"word": "all levels", "ipa": "[ɔːl ˈlevlz]", "pos": "명사구", "meaning": "모든 수준(전 레벨)"}
                    ],
                    "explanation": "Maya Lin이 담당하는 09:00 AM(Morning Healing Yoga)과 02:00 PM(Foam Roller Stretching) 두 수업을 시간·레벨·수업명·장소 순으로 읽어주세요."
                },
                {
                    "qId": "p4-s16-q11",
                    "qNum": "Question 11",
                    "topic": "오후 4시 상급자 요가 수업 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "What class is offered for advanced students, and what time does it start?",
                    "questionKo": "상급자 수강생을 위해 어떤 수업이 개설되어 있으며, 몇 시에 시작하나요?",
                    "sentences": [
                        {"step": "1. 수업명 및 시간 안내", "en": "For advanced students, Power Vinyasa Yoga is offered starting at 4:00 PM.", "ko": "상급자 수강생을 위해 오후 4시에 시작하는 파워 빈야사 요가 수업이 개설되어 있습니다."},
                        {"step": "2. 장소 및 강사 부연", "en": "It takes place in Studio A and is taught by Instructor Noah Williams.", "ko": "이 수업은 스튜디오 A에서 진행되며 노아 윌리엄스 강사가 가르칩니다."}
                    ],
                    "magicSentences": [
                        {"en": "Power Vinyasa Yoga is offered at 4:00 PM in Studio A.", "ko": "오후 4시에 스튜디오 A에서 파워 빈야사 요가 수업이 제공됩니다.", "tip": "강좌 개설 안내 공식"}
                    ],
                    "vocabulary": [
                        {"word": "advanced level", "ipa": "[ədˈvænst ˈlevl]", "pos": "명사구", "meaning": "고급/상급 단계"}
                    ],
                    "explanation": "Advanced Level 행(4:00 PM)의 수업명(Power Vinyasa Yoga), 장소(Studio A), 강사(Noah Williams)를 읽어주면 완성됩니다."
                }
            ]
        }
    ]



def get_new_part5_items():
    """Part 5 최신 기출 10문항 추가 (#11 ~ #20)"""
    return [
        {
            "id": "p5-11",
            "part": 5,
            "qNum": "#11",
            "category": "비즈니스·직장 환경",
            "topic": "주 4일 근무제(Four-day Workweek) 또는 유연근무제 도입 찬반",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you agree or disagree with the following statement? Companies should allow employees to have flexible working hours or a four-day workweek. Give specific reasons and examples to support your opinion.",
            "questionKo": "다음 진술에 동의하십니까, 반대하십니까? '기업은 직원들에게 유연근무제나 주 4일 근무제를 허용해야 한다.' 구체적인 이유와 예시를 들어 의견을 뒷받침하시오.",
            "sentences": [
                {"step": "1. 서론 (찬성 입장)", "en": "I strongly agree with the statement that companies should allow employees to have flexible working hours or a four-day workweek.", "ko": "저는 기업이 직원들에게 유연근무제나 주 4일 근무제를 허용해야 한다는 진술에 강력히 동의합니다."},
                {"step": "2. 본론 1 (워라밸 및 번아웃 예방)", "en": "First of all, it greatly improves employees' work-life balance and prevents burnout.", "ko": "무엇보다도 이는 직원들의 워라밸(일과 삶의 균형)을 크게 개선하고 번아웃을 예방해 줍니다."},
                {"step": "3. 본론 1 부연", "en": "When workers have enough time to rest and spend time with their families, they can relieve stress and recharge their energy.", "ko": "근로자들이 휴식을 취하고 가족과 시간을 보낼 충분한 여유가 있을 때, 스트레스를 해소하고 에너지를 재충전할 수 있습니다."},
                {"step": "4. 본론 2 (업무 집중도 및 생산성 향상)", "en": "Second, it actually increases work efficiency and overall productivity during working hours.", "ko": "둘째, 근무 시간 동안의 업무 효율성과 전반적인 생산성을 실제로 높여줍니다."},
                {"step": "5. 구체적 예시", "en": "For example, when my company introduced flexible working hours last year, employees avoided rush-hour traffic jams and focused much better on their tasks, which increased our team sales by 20 percent.", "ko": "예를 들어 저희 회사가 작년에 유연근무제를 도입했을 때, 직원들이 출퇴근 교통 체증을 피하고 업무에 훨씬 더 잘 집중하여 팀 매출이 20% 증가했습니다."},
                {"step": "6. 결론 재강조", "en": "For these reasons, I firmly believe that offering flexible working hours is beneficial for both companies and employees.", "ko": "이러한 이유들로 저는 유연근무제를 제공하는 것이 회사와 직원 모두에게 유익하다고 확신합니다."}
            ],
            "magicSentences": [
                {"en": "It improves work-life balance and prevents burnout.", "ko": "워라밸을 개선하고 번아웃을 예방합니다.", "tip": "시계토끼 만능 #162 (직장·근무제도 찬성 1순위)"},
                {"en": "Employees can focus better and increase work productivity.", "ko": "직원들이 더 잘 집중하고 업무 생산성을 높일 수 있습니다.", "tip": "기업 입장의 이익(생산성 향상) 만능 문장"}
            ],
            "vocabulary": [
                {"word": "flexible working hours", "ipa": "[ˈfleksəbl ˈwɜːrkɪŋ ˈaʊərz]", "pos": "명사구", "meaning": "유연근무제(탄력근무 시간)"},
                {"word": "burnout", "ipa": "[ˈbɜːrnaʊt]", "pos": "명사", "meaning": "번아웃, 극도의 피로"},
                {"word": "rush-hour traffic", "ipa": "[rʌʃ ˈaʊər ˈtræfɪk]", "pos": "명사구", "meaning": "출퇴근 시간대 교통 체증"}
            ],
            "explanation": "유튜브 기출 빈도 최상위 주제인 '유연근무제/주 4일제/재택근무'입니다. 1) 워라밸 및 에너지 재충전(recharge energy), 2) 출퇴근 피로 감소로 인한 업무 생산성 향상(increase productivity) 두 가지로 답하세요."
        },
        {
            "id": "p5-12",
            "part": 5,
            "qNum": "#12",
            "category": "기술·인공지능(AI)",
            "topic": "인공지능(AI)과 로봇 기술이 인간의 삶을 더 풍요롭게 만드는가?",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Some people think artificial intelligence (AI) and robots will threaten human jobs, while others think they will make our lives better. Which view do you agree with, and why?",
            "questionKo": "어떤 사람들은 인공지능(AI)과 로봇이 인간의 일자리를 위협할 것이라고 생각하는 반면, 다른 사람들은 우리의 삶을 더 나아지게 할 것이라고 생각합니다. 어느 의견에 동의하며 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 서론 (삶을 더 낫게 한다는 입장)", "en": "I definitely agree with the view that artificial intelligence and robots will make our lives much better.", "ko": "저는 인공지능과 로봇이 우리의 삶을 훨씬 더 나아지게 만들 것이라는 의견에 전적으로 동의합니다."},
                {"step": "2. 본론 1 (반복 업무 감소 및 시간 절약)", "en": "First of all, AI technology helps people save a lot of time and energy by handling repetitive and dangerous tasks.", "ko": "무엇보다도 AI 기술은 반복적이고 위험한 업무를 대신 처리해 줌으로써 사람들이 많은 시간과 에너지를 절약하도록 돕습니다."},
                {"step": "3. 본론 1 부연", "en": "As a result, humans can focus on more creative and meaningful work.", "ko": "그 결과 인간은 더 창의적이고 의미 있는 일에 집중할 수 있습니다."},
                {"step": "4. 본론 2 (일상생활의 편리성)", "en": "Second, smart appliances and AI assistants make our daily lives much more convenient.", "ko": "둘째, 스마트 가전과 AI 비서는 우리의 일상생활을 훨씬 더 편리하게 만들어 줍니다."},
                {"step": "5. 개인 경험 예시", "en": "For example, at work, I use an AI translation and summarizing tool every day, and it cuts my document preparation time in half.", "ko": "예를 들어 저는 직장에서 매일 AI 번역 및 요약 도구를 사용하는데, 문서 준비 시간을 절반으로 줄여줍니다."},
                {"step": "6. 결론 재강조", "en": "Therefore, I strongly believe that AI and robots will improve our quality of life.", "ko": "따라서 저는 AI와 로봇이 우리의 삶의 질을 향상시킬 것이라고 굳게 믿습니다."}
            ],
            "magicSentences": [
                {"en": "It helps people save a lot of time and energy.", "ko": "사람들이 많은 시간과 에너지를 아끼도록 도와줍니다.", "tip": "시계토끼 만능 #158 (기술·AI 찬성 절대 공식)"},
                {"en": "People can focus on more creative and important tasks.", "ko": "사람들이 더 창의적이고 중요한 업무에 집중할 수 있습니다.", "tip": "AI/자동화 효과 핵심 문장"}
            ],
            "vocabulary": [
                {"word": "artificial intelligence", "ipa": "[ˌɑːrtɪˈfɪʃl ɪnˈtelɪdʒəns]", "pos": "명사구", "meaning": "인공지능(AI)"},
                {"word": "repetitive", "ipa": "[rɪˈpetətɪv]", "pos": "형용사", "meaning": "반복적인"},
                {"word": "quality of life", "ipa": "[ˈkwɑːləti ʌv laɪf]", "pos": "명사구", "meaning": "삶의 질"}
            ],
            "explanation": "2025~2026년 최신 트렌드 기출인 AI/자동화 주제입니다. 'saves time and energy'와 'focus on creative tasks' 두 구문만 외워도 만점 답변이 가능합니다."
        },
        {
            "id": "p5-13",
            "part": 5,
            "qNum": "#13",
            "category": "교육·어린이 성장",
            "topic": "어린이들이 어릴 때부터 팀 스포츠이나 단체 활동에 참여해야 하는가?",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you agree or disagree that children should participate in team sports or group activities from an early age? Use specific reasons and examples to support your answer.",
            "questionKo": "어린이들이 어릴 때부터 팀 스포츠나 단체 활동에 참여해야 한다는 의견에 동의하십니까, 반대하십니까? 구체적인 이유와 예시를 들어 답변을 뒷받침하시오.",
            "sentences": [
                {"step": "1. 서론 (찬성 입장)", "en": "I strongly agree that children should participate in team sports or group activities from an early age.", "ko": "저는 어린이들이 어릴 때부터 팀 스포츠나 단체 활동에 참여해야 한다는 의견에 강력히 동의합니다."},
                {"step": "2. 본론 1 (사회성 및 협동심 함양)", "en": "First of all, children can learn social skills, teamwork, and how to cooperate with others.", "ko": "무엇보다도 아이들은 사회성 기술과 팀워크, 그리고 다른 사람들과 협력하는 방법을 배울 수 있습니다."},
                {"step": "3. 본론 1 부연", "en": "By playing together toward a common goal, they learn to respect rules and care for their teammates.", "ko": "공동의 목표를 향해 함께 뛰면서 규칙을 존중하고 팀원들을 배려하는 법을 배웁니다."},
                {"step": "4. 본론 2 (신체 건강 및 스트레스 해소)", "en": "Second, playing sports outdoors keeps children physically healthy and reduces their smartphone screen time.", "ko": "둘째, 야외에서 스포츠를 하면 아이들의 신체 건강을 지켜주고 스마트폰 사용 시간을 줄여줍니다."},
                {"step": "5. 구체적 예시", "en": "For example, when my younger nephew joined a youth soccer club last year, he became much more outgoing, made many close friends, and got healthier.", "ko": "예를 들어 제 어린 조카가 작년에 유소년 축구 클럽에 들어갔을 때, 성격이 훨씬 활발해지고 친한 친구도 많이 사귀었으며 건강해졌습니다."},
                {"step": "6. 결론 재강조", "en": "For these reasons, participating in team sports is essential for children's growth.", "ko": "이러한 이유들로 팀 스포츠에 참여하는 것은 어린이들의 성장에 필수적입니다."}
            ],
            "magicSentences": [
                {"en": "Children can learn social skills and how to cooperate with others.", "ko": "아이들은 사회성과 타인과 협력하는 법을 배울 수 있습니다.", "tip": "시계토끼 만능 #170 (어린이·교육 주제 만능 공식)"},
                {"en": "It keeps them healthy and reduces smartphone use.", "ko": "아이들을 건강하게 해 주고 스마트폰 사용을 줄여줍니다.", "tip": "야외 활동·운동 교육 만능 이유"}
            ],
            "vocabulary": [
                {"word": "participate in", "ipa": "[pɑːrˈtɪsɪpeɪt ɪn]", "pos": "숙어", "meaning": "~에 참여하다"},
                {"word": "cooperate with", "ipa": "[koʊˈɑːpəreɪt wɪð]", "pos": "숙어", "meaning": "~와 협력하다, 협동하다"},
                {"word": "outgoing", "ipa": "[ˈaʊtɡoʊɪŋ]", "pos": "형용사", "meaning": "외향적인, 사교적인"}
            ],
            "explanation": "어린이 교육(팀 스포츠, 음악/미술 수업, 캠프 참여 등) 주제는 언제나 'learn social skills and teamwork(사회성과 협동심 학습)'가 만능 키입니다."
        },
        {
            "id": "p5-14",
            "part": 5,
            "qNum": "#14",
            "category": "소비·마케팅",
            "topic": "유명 연예인·인플루언서 광고가 소비자의 구매 결정에 큰 영향을 미치는가?",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you think advertisements featuring famous celebrities or social media influencers actually encourage people to buy products? Why or why not?",
            "questionKo": "유명 연예인이나 소셜 미디어 인플루언서가 등장하는 광고가 실제로 사람들의 제품 구매를 촉진한다고 생각하십니까? 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 서론 (긍정 입장)", "en": "I definitely think that advertisements featuring famous celebrities or influencers strongly encourage people to buy products.", "ko": "저는 유명 연예인이나 인플루언서가 등장하는 광고가 사람들의 제품 구매를 강력하게 촉진한다고 생각합니다."},
                {"step": "2. 본론 1 (대중의 시선 집중 및 인지도 상승)", "en": "First of all, famous stars quickly grab people's attention and increase brand awareness in a short time.", "ko": "무엇보다도 유명 스타들은 사람들의 시선을 빠르게 사로잡고 단기간에 브랜드 인지도를 높여줍니다."},
                {"step": "3. 본론 2 (신뢰감 및 모방 심리)", "en": "Second, fans trust their favorite influencers and want to wear or use the same items.", "ko": "둘째, 팬들은 자신이 좋아하는 인플루언서를 신뢰하며 같은 아이템을 착용하거나 사용하고 싶어 합니다."},
                {"step": "4. 개인 경험 예시", "en": "For example, last month, I saw my favorite YouTuber reviewing a new skincare product on Instagram, and I bought it right away because it looked so reliable.", "ko": "예를 들어 지난달에 제가 가장 좋아하는 유튜버가 인스타그램에서 새 스킨케어 제품을 리뷰하는 것을 보았고, 매우 믿음이 가서 즉시 구매했습니다."},
                {"step": "5. 부연 결과", "en": "In fact, that product sold out within two days thanks to the influencer's popularity.", "ko": "실제로 그 제품은 인플루언서의 인기 덕분에 이틀 만에 품절되었습니다."},
                {"step": "6. 결론 재강조", "en": "Therefore, celebrity and influencer marketing is a very powerful way to boost sales.", "ko": "따라서 연예인 및 인플루언서 마케팅은 매출을 끌어올리는 매우 강력한 방법입니다."}
            ],
            "magicSentences": [
                {"en": "It quickly grabs people's attention and increases brand awareness.", "ko": "사람들의 시선을 빠르게 끌고 브랜드 인지도를 높입니다.", "tip": "시계토끼 만능 #160 (광고·마케팅 기출 만능 표현)"},
                {"en": "It is a very effective way to boost sales.", "ko": "매출을 높이는 매우 효과적인 방법입니다.", "tip": "비즈니스·마케팅 결론 공식"}
            ],
            "vocabulary": [
                {"word": "celebrity", "ipa": "[səˈlebrəti]", "pos": "명사", "meaning": "유명 연예인, 셀럽"},
                {"word": "brand awareness", "ipa": "[brænd əˈwernəs]", "pos": "명사구", "meaning": "브랜드 인지도"},
                {"word": "boost sales", "ipa": "[buːst seɪlz]", "pos": "숙어", "meaning": "매출을 증대시키다"}
            ],
            "explanation": "연예인/인플루언서 광고 문제는 'grab attention(시선 집중)' + 'increase brand awareness(브랜드 인지도 상승)' + 'boost sales(매출 증대)' 3단 콤보로 구성하면 완벽합니다."
        },
        {
            "id": "p5-15",
            "part": 5,
            "qNum": "#15",
            "category": "환경·공공 정책",
            "topic": "정부가 일회용 플라스틱 및 비닐봉지 사용을 법적으로 금지·규제해야 하는가?",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you agree or disagree with the following statement? The government should strictly ban or charge extra fees for single-use plastics in cafes and supermarkets. Support your opinion with specific reasons.",
            "questionKo": "다음 진술에 동의하십니까, 반대하십니까? '정부는 카페와 슈퍼마켓에서 일회용 플라스틱 사용을 엄격히 금지하거나 추가 요금을 부과해야 한다.' 구체적인 이유로 의견을 뒷받침하시오.",
            "sentences": [
                {"step": "1. 서론 (찬성 입장)", "en": "I strongly agree that the government should strictly regulate single-use plastics in cafes and supermarkets.", "ko": "저는 정부가 카페와 슈퍼마켓에서 일회용 플라스틱을 엄격히 규제해야 한다는 의견에 강력히 동의합니다."},
                {"step": "2. 본론 1 (환경 오염 및 기후 변화 심각성)", "en": "First of all, plastic waste takes hundreds of years to break down and causes serious environmental pollution.", "ko": "무엇보다도 플라스틱 쓰레기는 분해되는 데 수백 년이 걸리며 심각한 환경 오염을 유발합니다."},
                {"step": "3. 본론 2 (친환경 습관 유도)", "en": "Second, strict regulations encourage citizens to use eco-friendly items such as personal tumblers and reusable shopping bags.", "ko": "둘째, 엄격한 규제는 시민들이 개인 텀블러나 장바구니 같은 친환경 물품을 사용하도록 유도합니다."},
                {"step": "4. 구체적 예시", "en": "For example, since supermarkets in Korea banned free plastic bags, I always carry a reusable cloth bag in my backpack and bring my own tumbler to coffee shops.", "ko": "예를 들어 한국의 대형마트들이 무료 비닐봉지 제공을 금지한 이후로, 저는 항상 가방에 다회용 장바구니를 넣어 다니고 카페에도 개인 텀블러를 가져갑니다."},
                {"step": "5. 결론 재강조", "en": "For these reasons, government regulation on plastics is necessary to protect our environment for future generations.", "ko": "이러한 이유들로 미래 세대를 위해 환경을 보호하려면 정부의 플라스틱 규제가 반드시 필요합니다."}
            ],
            "magicSentences": [
                {"en": "It reduces plastic waste and protects the environment.", "ko": "플라스틱 쓰레기를 줄이고 환경을 보호합니다.", "tip": "시계토끼 만능 #175 (환경·친환경 기출 1순위 문장)"},
                {"en": "It encourages people to use reusable tumblers and bags.", "ko": "사람들이 다회용 텀블러와 장바구니를 쓰도록 장려합니다.", "tip": "일회용품 규제 구체적 효과"}
            ],
            "vocabulary": [
                {"word": "single-use plastic", "ipa": "[ˈsɪŋɡl juːs ˈplæstɪk]", "pos": "명사구", "meaning": "일회용 플라스틱"},
                {"word": "environmental pollution", "ipa": "[ɪnˌvaɪrənˈmentl pəˈluːʃn]", "pos": "명사구", "meaning": "환경 오염"},
                {"word": "reusable bag", "ipa": "[ˌriːˈjuːzəbl bæɡ]", "pos": "명사구", "meaning": "다회용 장바구니(에코백)"}
            ],
            "explanation": "환경 보호 관련 Part 5 문제(일회용품 금지, 대중교통 장려, 재활용 의무화)는 'reduce waste and protect the environment' 문장 하나로 서론·본론·결론을 관통할 수 있습니다."
        },
        {
            "id": "p5-16",
            "part": 5,
            "qNum": "#16",
            "category": "커리어·자기계발",
            "topic": "한 직장에서 평생 근무하기 vs 여러 직장으로 이직하며 커리어 쌓기",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Some people prefer to work for the same company for their entire career, while others prefer to change jobs several times. Which do you think is better, and why?",
            "questionKo": "어떤 사람들은 평생 한 회사에서 일하는 것을 선호하는 반면, 다른 사람들은 여러 번 이직하는 것을 선호합니다. 어느 쪽이 더 낫다고 생각하며 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 서론 (이직 선호 입장)", "en": "I think changing jobs several times during a career is much better than working for only one company.", "ko": "저는 커리어 동안 여러 번 이직하는 것이 한 회사에서만 일하는 것보다 훨씬 더 낫다고 생각합니다."},
                {"step": "2. 본론 1 (다양한 실무 경험과 폭넓은 인맥)", "en": "First of all, by working at different companies, people can gain diverse work experiences and build a wider professional network.", "ko": "무엇보다도 여러 회사에서 일함으로써 다양한 실무 경험을 쌓고 더 폭넓은 인적 네트워크를 구축할 수 있습니다."},
                {"step": "3. 본론 1 부연", "en": "This helps them learn new skills quickly and adapt to changing business trends.", "ko": "이는 새로운 기술을 빠르게 배우고 변화하는 비즈니스 트렌드에 적응하는 데 도움이 됩니다."},
                {"step": "4. 본론 2 (연봉 인상 및 승진 기회)", "en": "Second, changing jobs is often the fastest way to get a higher salary and a better position.", "ko": "둘째, 이직은 종종 더 높은 연봉과 더 나은 직급을 얻는 가장 빠른 방법입니다."},
                {"step": "5. 구체적 예시", "en": "For example, my older brother moved to a new IT company last year, and he not only received a 25 percent salary raise but also learned advanced cloud skills.", "ko": "예를 들어 저희 형은 작년에 새로운 IT 기업으로 이직했는데, 연봉이 25% 인상되었을 뿐만 아니라 고급 클라우드 기술도 배울 수 있었습니다."},
                {"step": "6. 결론 재강조", "en": "Therefore, I believe changing jobs is a great way to grow professionally.", "ko": "따라서 저는 이직이 전문가로서 성장하는 훌륭한 방법이라고 생각합니다."}
            ],
            "magicSentences": [
                {"en": "People can gain diverse experiences and broaden their horizons.", "ko": "다양한 경험을 쌓고 시야를 넓힐 수 있습니다.", "tip": "시계토끼 만능 #168 (새로운 도전·이직·여행 만능)"},
                {"en": "They can get a higher salary and better career opportunities.", "ko": "더 높은 연봉과 더 나은 커리어 기회를 얻을 수 있습니다.", "tip": "이직·외국어 학습 공통 만능 이유"}
            ],
            "vocabulary": [
                {"word": "entire career", "ipa": "[ɪnˈtaɪər kəˈrɪr]", "pos": "명사구", "meaning": "평생의 직장 생활(전 경력)"},
                {"word": "professional network", "ipa": "[prəˈfeʃənl ˈnetwɜːrk]", "pos": "명사구", "meaning": "업무상 인맥, 인적 네트워크"},
                {"word": "salary raise", "ipa": "[ˈsæləri reɪz]", "pos": "명사구", "meaning": "연봉(급여) 인상"}
            ],
            "explanation": "평생직장 vs 이직 주제에서는 이직(changing jobs)을 선택해 1) 다양한 경험과 인맥(diverse experiences & network), 2) 연봉 인상(higher salary)을 말하는 것이 훨씬 풍부합니다."
        },
        {
            "id": "p5-17",
            "part": 5,
            "qNum": "#17",
            "category": "여행·문화",
            "topic": "여행 전 철저하게 계획 세우기 vs 계획 없이 즉흥적으로 여행하기",
            "prepTime": 45,
            "responseTime": 60,
            "question": "When traveling, some people like to plan every detail in advance, while others prefer to travel without a fixed schedule. Which style do you prefer, and why?",
            "questionKo": "여행할 때 어떤 사람들은 사전에 모든 세부 일정을 계획하는 것을 좋아하고, 다른 사람들은 정해진 일정 없이 여행하는 것을 선호합니다. 어떤 스타일을 선호하며 그 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 서론 (사전 계획 선호)", "en": "When traveling, I definitely prefer to plan every detail in advance rather than traveling without a schedule.", "ko": "여행할 때 저는 일정 없이 여행하는 것보다 사전에 모든 세부 사항을 계획하는 것을 확실히 선호합니다."},
                {"step": "2. 본론 1 (시간 절약 및 필수 명소 방문)", "en": "First of all, planning ahead helps me save precious time during the trip and visit all the famous tourist attractions efficiently.", "ko": "무엇보다도 미리 계획을 세우면 여행 중 귀중한 시간을 아끼고 유명한 관광 명소들을 효율적으로 모두 방문할 수 있습니다."},
                {"step": "3. 본론 2 (비용 절감 및 매진 방지)", "en": "Second, I can save a lot of money by booking flights, hotels, and popular restaurants early.", "ko": "둘째, 항공권과 호텔, 인기 식당을 미리 예약함으로써 많은 돈을 절약할 수 있습니다."},
                {"step": "4. 개인 경험 예시", "en": "For example, when I traveled to Japan last summer, I reserved all my train tickets and hotels two months in advance, so I got a 30 percent early-bird discount and didn't waste time waiting in long lines.", "ko": "예를 들어 지난여름 일본으로 여행을 갔을 때, 두 달 전에 기차표와 호텔을 모두 예약해서 30% 얼리버드 할인을 받았고 긴 줄을 서느라 시간을 낭비하지 않았습니다."},
                {"step": "5. 결론 재강조", "en": "For these reasons, I always plan my trip carefully in advance.", "ko": "이러한 이유들로 저는 항상 사전에 여행을 꼼꼼히 계획합니다."}
            ],
            "magicSentences": [
                {"en": "Planning ahead helps me save time and money.", "ko": "미리 계획하면 시간과 돈을 절약하는 데 도움이 됩니다.", "tip": "시계토끼 만능 #054 & #158 (시간·비용 절약 절대 공식)"},
                {"en": "I don't have to waste time waiting in long lines.", "ko": "긴 줄을 서느라 시간을 낭비할 필요가 없습니다.", "tip": "사전 예약·계획의 핵심 장점"}
            ],
            "vocabulary": [
                {"word": "in advance", "ipa": "[ɪn ədˈvæns]", "pos": "부사구", "meaning": "미리, 사전에"},
                {"word": "tourist attraction", "ipa": "[ˈtʊrɪst əˈtrækʃn]", "pos": "명사구", "meaning": "관광 명소"},
                {"word": "wait in a long line", "ipa": "[weɪt ɪn ə lɔːŋ laɪn]", "pos": "숙어", "meaning": "긴 줄을 서서 기다리다"}
            ],
            "explanation": "계획 여행 vs 즉흥 여행은 'plan in advance(사전 계획)'를 선택하면 'save time and money(시간과 비용 절약)' 만능 공식을 그대로 적용할 수 있어 매우 쉽습니다."
        },
        {
            "id": "p5-18",
            "part": 5,
            "qNum": "#18",
            "category": "교육·학습 방식",
            "topic": "새로운 지식이나 기술을 배울 때 책으로 독학하기 vs 동영상·온라인 강의로 배우기",
            "prepTime": 45,
            "responseTime": 60,
            "question": "When learning a new skill or subject, do you prefer reading books on your own or watching instructional videos online? Give specific reasons and examples.",
            "questionKo": "새로운 기술이나 과목을 배울 때 혼자 책을 읽는 것과 온라인 교육 동영상을 시청하는 것 중 어느 쪽을 선호합니까? 구체적인 이유와 예시를 들어 설명하시오.",
            "sentences": [
                {"step": "1. 서론 (동영상 강의 선호)", "en": "When learning a new skill, I strongly prefer watching instructional videos online rather than reading books on my own.", "ko": "새로운 기술을 배울 때 저는 혼자 책을 읽는 것보다 온라인 교육 동영상을 보는 것을 강력히 선호합니다."},
                {"step": "2. 본론 1 (시각·청각 자료를 통한 쉬운 이해)", "en": "First of all, video lectures provide visual demonstrations and step-by-step explanations, making complex topics much easier to understand.", "ko": "무엇보다도 동영상 강의는 시각적인 시연과 단계별 설명을 제공하므로 복잡한 주제를 훨씬 더 이해하기 쉽게 만들어 줍니다."},
                {"step": "3. 본론 2 (무료 콘텐츠 및 반복 학습 용이)", "en": "Second, there are thousands of free tutorials on YouTube, and I can pause or replay difficult parts anytime, anywhere.", "ko": "둘째, 유튜브에 수천 개의 무료 튜토리얼이 있으며, 어려운 부분은 언제 어디서나 일시 정지하거나 다시 재생할 수 있습니다."},
                {"step": "4. 개인 경험 예시", "en": "For example, when I first learned how to cook pasta and edit videos last month, watching 10-minute YouTube tutorials was much faster and clearer than reading a thick textbook.", "ko": "예를 들어 지난달에 처음 파스타 요리법과 영상 편집을 배울 때, 두꺼운 교재를 읽는 것보다 10분짜리 유튜브 튜토리얼을 보는 것이 훨씬 빠르고 명확했습니다."},
                {"step": "5. 결론 재강조", "en": "Therefore, watching online videos is the most effective way for me to learn new skills.", "ko": "따라서 온라인 동영상을 시청하는 것이 저에게 새로운 기술을 배우는 가장 효과적인 방법입니다."}
            ],
            "magicSentences": [
                {"en": "Visual explanations make it much easier to understand.", "ko": "시각적인 설명이 이해하기 훨씬 쉽게 만들어 줍니다.", "tip": "동영상·시각 자료 선호 핵심 표현"},
                {"en": "I can pause and replay lectures anytime, anywhere.", "ko": "언제 어디서나 강의를 멈추고 다시 볼 수 있습니다.", "tip": "시계토끼 만능 #155 & #158 (온라인 강의 만능 장점)"}
            ],
            "vocabulary": [
                {"word": "instructional video", "ipa": "[ɪnˈstrʌkʃənl ˈvɪdioʊ]", "pos": "명사구", "meaning": "교육용 비디오, 강의 영상"},
                {"word": "step-by-step", "ipa": "[step baɪ step]", "pos": "형용사", "meaning": "단계별의, 차근차근한"},
                {"word": "replay", "ipa": "[ˌriːˈpleɪ]", "pos": "동사", "meaning": "다시 재생하다, 반복 시청하다"}
            ],
            "explanation": "독학(책) vs 영상 학습 질문에서는 영상(instructional videos)을 선택해 1) 시각적 설명으로 이해가 쉬움(easier to understand), 2) 반복 시청 가능(replay anytime, anywhere)으로 답하세요."
        },
        {
            "id": "p5-19",
            "part": 5,
            "qNum": "#19",
            "category": "비즈니스·기업 사회적 책임",
            "topic": "기업이 수익의 일부를 지역 사회 기부나 봉사 활동에 사용해야 하는가?",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you agree or disagree with the following statement? Companies have a responsibility to donate part of their profits to help the local community. Support your answer with specific reasons and examples.",
            "questionKo": "다음 진술에 동의하십니까, 반대하십니까? '기업은 지역 사회를 돕기 위해 수익의 일부를 기부할 책임이 있다.' 구체적인 이유와 예시를 들어 답변을 뒷받침하시오.",
            "sentences": [
                {"step": "1. 서론 (찬성 입장)", "en": "I strongly agree that companies have a responsibility to donate part of their profits to help the local community.", "ko": "저는 기업이 지역 사회를 돕기 위해 수익의 일부를 기부할 책임이 있다는 의견에 강력히 동의합니다."},
                {"step": "2. 본론 1 (기업 이미지 제고 및 고객 신뢰)", "en": "First of all, supporting the local community builds a positive brand image and earns customers' trust.", "ko": "무엇보다도 지역 사회를 지원하는 것은 긍정적인 브랜드 이미지를 구축하고 고객의 신뢰를 얻게 해 줍니다."},
                {"step": "3. 본론 1 부연", "en": "Nowadays, consumers prefer buying products from socially responsible companies, which eventually increases long-term sales.", "ko": "요즘 소비자들은 사회적 책임을 다하는 기업의 제품을 구매하는 것을 선호하며, 이는 결국 장기적인 매출을 증가시킵니다."},
                {"step": "4. 본론 2 (지역 사회와의 상생 발전)", "en": "Second, companies grow thanks to local residents, so giving back to society helps the community and the company grow together.", "ko": "둘째, 기업은 지역 주민들 덕분에 성장하므로 사회에 환원하는 것은 지역 사회와 기업이 함께 성장하도록 돕습니다."},
                {"step": "5. 구체적 예시", "en": "For example, a famous bakery brand in my city donates fresh bread to local children's centers every week, and citizens love the brand so much that its sales doubled last year.", "ko": "예를 들어 우리 도시의 한 유명 베이커리 브랜드는 매주 지역 아동 센터에 신선한 빵을 기부하는데, 시민들이 그 브랜드를 무척 사랑해서 작년에 매출이 두 배로 늘었습니다."},
                {"step": "6. 결론 재강조", "en": "For these reasons, donating to the community is a win-win strategy for both companies and society.", "ko": "이러한 이유들로 지역 사회에 기부하는 것은 기업과 사회 모두에게 윈윈(상생) 전략입니다."}
            ],
            "magicSentences": [
                {"en": "It builds a positive brand image and earns customers' trust.", "ko": "긍정적인 브랜드 이미지를 만들고 고객의 신뢰를 얻습니다.", "tip": "시계토끼 만능 #160 응용 (기업 활동·CSR 만능 문장)"},
                {"en": "It is a win-win strategy that increases long-term sales.", "ko": "장기적인 매출을 높여주는 윈윈 전략입니다.", "tip": "비즈니스 기출 고급 마무리 표현"}
            ],
            "vocabulary": [
                {"word": "donate", "ipa": "[ˈdoʊneɪt]", "pos": "동사", "meaning": "기부하다"},
                {"word": "socially responsible", "ipa": "[ˈsoʊʃəli rɪˈspɑːnsəbl]", "pos": "형용사구", "meaning": "사회적 책임을 다하는"},
                {"word": "give back to society", "ipa": "[ɡɪv bæk tuː səˈsaɪəti]", "pos": "숙어", "meaning": "사회에 환원하다"}
            ],
            "explanation": "기업의 사회적 책임(기부, 친환경 경영, 지역 후원) 문제는 'builds a positive brand image(긍정적 브랜드 이미지 구축)' + 'increases long-term sales(장기 매출 상승)'로 연결하면 완벽합니다."
        },
        {
            "id": "p5-20",
            "part": 5,
            "qNum": "#20",
            "category": "라이프스타일·소비 습관",
            "topic": "물건을 직접 구매해 소유하기 vs 필요할 때만 대여·구독 서비스 이용하기",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Nowadays, many people rent items such as cars, home appliances, or clothes instead of buying them. Do you think this is a positive or negative trend? Give specific reasons and examples.",
            "questionKo": "오늘날 많은 사람들이 자동차, 가전제품, 의류 같은 물건을 구매하는 대신 대여(렌탈)해서 사용합니다. 이것이 긍정적인 추세라고 생각하십니까, 부정적인 추세라고 생각하십니까? 구체적인 이유와 예시를 들어 설명하시오.",
            "sentences": [
                {"step": "1. 서론 (긍정적 트렌드 입장)", "en": "I definitely think that renting items instead of buying them is a very positive trend.", "ko": "저는 물건을 구매하는 대신 대여해서 사용하는 것이 매우 긍정적인 추세라고 생각합니다."},
                {"step": "2. 본론 1 (초기 비용 절감 및 합리적 소비)", "en": "First of all, it is very economical because people don't have to pay a large amount of money all at once for expensive items.", "ko": "무엇보다도 비싼 물건을 사기 위해 한꺼번에 큰돈을 지불할 필요가 없기 때문에 매우 경제적입니다."},
                {"step": "3. 본론 2 (유지보수 편리성 및 환경 보호)", "en": "Second, rental companies provide free maintenance services, and sharing items reduces unnecessary waste, which is eco-friendly.", "ko": "둘째, 렌탈 업체에서 무료 관리 서비스를 제공해 주며, 물건을 공유하면 불필요한 쓰레기를 줄일 수 있어 친환경적입니다."},
                {"step": "4. 개인 경험 예시", "en": "For example, instead of buying an expensive water purifier and air purifier, my family rents them for a small monthly fee, and a technician visits every three months to replace the filters for free.", "ko": "예를 들어 저희 가족은 비싼 정수기와 공기청정기를 직접 사는 대신 저렴한 월 요금으로 렌탈해서 쓰는데, 3개월마다 기사님이 방문해 무료로 필터를 교체해 주셔서 정말 편리합니다."},
                {"step": "5. 결론 재강조", "en": "For these reasons, renting items is a smart and practical way of consumption in modern society.", "ko": "이러한 이유들로 물건을 대여하는 것은 현대 사회에서 현명하고 실용적인 소비 방식입니다."}
            ],
            "magicSentences": [
                {"en": "It is very economical because people can save a lot of money.", "ko": "많은 돈을 아낄 수 있어서 매우 경제적입니다.", "tip": "시계토끼 만능 #054 (경제적 이유 만능)"},
                {"en": "It reduces unnecessary waste and protects the environment.", "ko": "불필요한 쓰레기를 줄이고 환경을 보호합니다.", "tip": "시계토끼 만능 #175 (공유 경제·렌탈 친환경 이유)"}
            ],
            "vocabulary": [
                {"word": "home appliance", "ipa": "[hoʊm əˈplaɪəns]", "pos": "명사구", "meaning": "가전제품"},
                {"word": "all at once", "ipa": "[ɔːl æt wʌns]", "pos": "부사구", "meaning": "한꺼번에, 일시불로"},
                {"word": "water purifier", "ipa": "[ˈwɔːtər ˈpjʊrɪfaɪər]", "pos": "명사구", "meaning": "정수기"}
            ],
            "explanation": "렌탈/공유 경제/구독 서비스 트렌드 기출입니다. 1) 경제적 부담 감소(economical, save money), 2) 관리 편리성 및 친환경(free maintenance & eco-friendly)으로 구성하세요."
        }
    ]


def main():
    with open(MASTER_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. Part 1: 기존 10문항 + 신규 10문항 = 20문항
    existing_p1 = [item for item in data["part1"] if int(item["qNum"].replace("#", "")) <= 10]
    new_p1 = get_new_part1_items()
    data["part1"] = existing_p1 + new_p1
    for idx, item in enumerate(data["part1"], start=1):
        item["id"] = f"p1-{idx:02d}"
        item["qNum"] = f"#{idx:02d}"

    # 2. Part 2: 기존 10문항 + 신규 10문항 (실제 고화질 시험 사진) = 20문항
    img_map = load_git_71b8f33_part2_images()
    existing_p2 = [item for item in data["part2"] if int(item["qNum"].replace("#", "")) <= 10]
    new_p2 = get_new_part2_items(img_map)
    data["part2"] = existing_p2 + new_p2
    for idx, item in enumerate(data["part2"], start=1):
        item["id"] = f"p2-{idx:02d}"
        item["qNum"] = f"#{idx:02d}"

    # 3. Part 3: 유형 문구 탭 스타일로 깔끔하게 정리 & 유형별 6문항 + 6문항 = 12문항씩 총 60문항
    clean_p3_types = [
        {"id": "ALL", "name": "전체"},
        {"id": "p3-t1", "name": "시점 최근 경험"},
        {"id": "p3-t2", "name": "빈도 장소 동행인"},
        {"id": "p3-t3", "name": "양자택일 선호도 찬반"},
        {"id": "p3-t4", "name": "3자택일 최적 선택"},
        {"id": "p3-t5", "name": "장단점 중요 이유"}
    ]
    data["part3Types"] = clean_p3_types
    type_name_map = {t["id"]: t["name"] for t in clean_p3_types if t["id"] != "ALL"}

    existing_p3 = data["part3"][:30] if len(data["part3"]) == 30 else [
        item for item in data["part3"] if not item.get("isExpanded2x")
    ]
    new_p3 = get_new_part3_items()
    for item in new_p3:
        item["isExpanded2x"] = True

    combined_p3 = []
    for type_id in ["p3-t1", "p3-t2", "p3-t3", "p3-t4", "p3-t5"]:
        old_of_type = [x for x in existing_p3 if x["typeId"] == type_id][:6]
        new_of_type = [x for x in new_p3 if x["typeId"] == type_id][:6]
        combined_p3.extend(old_of_type + new_of_type)

    for idx, item in enumerate(combined_p3, start=1):
        item["id"] = f"p3-{idx:02d}"
        item["qNum"] = f"#{idx:02d}"
        clean_label = type_name_map[item["typeId"]]
        item["typeName"] = clean_label
        item["typeBadge"] = clean_label
    data["part3"] = combined_p3

    # 4. Part 4: 전체 표 속성 -> 전체 & 기존 8세트 + 신규 8세트 = 16세트 (64문항)
    for t in data["part4TableTypes"]:
        if t["id"] == "ALL":
            t["name"] = "전체"
    existing_p4 = data["part4"][:8]
    new_p4 = get_new_part4_sets()
    data["part4"] = existing_p4 + new_p4
    for idx, s in enumerate(data["part4"], start=1):
        s["id"] = f"p4-set{idx}"
        s["setNum"] = f"Set {idx}"

    # 5. Part 5: 기존 10문항 + 신규 10문항 = 20문항
    existing_p5 = data["part5"][:10]
    new_p5 = get_new_part5_items()
    data["part5"] = existing_p5 + new_p5
    for idx, item in enumerate(data["part5"], start=1):
        item["id"] = f"p5-{idx:02d}"
        item["qNum"] = f"#{idx:02d}"

    with open(MASTER_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total_p4_q = sum(len(s["questions"]) for s in data["part4"])
    print(f"Successfully expanded dataset 2x!")
    print(f"Part 1: {len(data['part1'])} items")
    print(f"Part 2: {len(data['part2'])} items")
    print(f"Part 3: {len(data['part3'])} items")
    print(f"Part 4: {len(data['part4'])} sets ({total_p4_q} questions)")
    print(f"Part 5: {len(data['part5'])} items")
    print(f"Total Questions: {len(data['part1']) + len(data['part2']) + len(data['part3']) + total_p4_q + len(data['part5'])}")


if __name__ == "__main__":
    main()
