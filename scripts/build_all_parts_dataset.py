#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2025~2026 토익스피킹 파트별 통합 마스터 데이터셋 빌더 (scripts/build_all_parts_dataset.py)
- 날짜/유튜브 출처 구분 없이 오직 파트별(Part 1~5) 및 유형별(Part 3: 5유형×5문제=25문제, Part 4: 4유형×5문제=20문제)로 통합
- Part 1: 10문제 (문장별 쪼개기 + 표준/느린 발음 + 핵심 어휘 발음)
- Part 2: 10문제 (실제 시험 고화질 사진 10장 + 문장별 모범답안 발음 + 쓰인 만능문장 + 핵심어휘 발음 + 해설)
- Part 3: 25문제 (5개 유형 × 5문제씩 + 문장별 모범답안 발음 + 쓰인 만능문장 + 핵심어휘 발음 + 해설)
- Part 4: 20문제 (4개 유형 × 5문제씩 + 일정표/이력서 표 + 문장별 모범답안 발음 + 쓰인 만능문장 + 핵심어휘 발음 + 해설)
- Part 5: 10문제 (2025~2026 최신 빈출 10문제 + 문장별 모범답안 발음 + 쓰인 만능문장 + 핵심어휘 발음 + 해설)
"""

import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def encode_image_base64(rel_path: str) -> str:
    p = ROOT / rel_path
    if not p.exists():
        return ""
    b64 = base64.b64encode(p.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"


def split_sentences_en_ko(en_text: str, ko_text: str, default_steps=None):
    """영어 문장과 한국어 문장을 1:1 문장 단위로 분리"""
    en_lines = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", en_text.strip()) if s.strip()]
    ko_lines = [s.strip() for s in re.split(r"(?<=[.!?다요죠])\s+|\n+", ko_text.strip()) if s.strip()]
    result = []
    for i, en in enumerate(en_lines):
        ko = ko_lines[i] if i < len(ko_lines) else (ko_lines[-1] if ko_lines else "")
        step = default_steps[i] if (default_steps and i < len(default_steps)) else f"문장 {i+1}"
        result.append({"step": step, "en": en, "ko": ko})
    return result


def build_part1():
    """Part 1: 10문항 (모범답안 토글 없이 지문을 문장별로 분리하여 표준/느린 속도 스피커 제공)"""
    return [
        {
            "id": "p1-01",
            "part": 1,
            "qNum": "Part 1 - #01",
            "category": "여행·관광 가이드 안내",
            "topic": "Secret Food Tours - Global Culinary Tour Guide",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Welcome to Secret Food Tours, where every trip is a treat for your taste buds.",
                    "chunking": "Welcome to Secret Food Tours, / where every trip / is a treat for your taste buds. ↘",
                    "ko": "모든 여행이 여러분의 미각에 즐거움이 되는 시크릿 푸드 투어에 오신 것을 환영합니다."
                },
                {
                    "en": "Over the past year, we've shared delicious meals in more than 60 cities around the world.",
                    "chunking": "Over the past year, / we've shared delicious meals / in more than sixty cities around the world. ↘",
                    "ko": "지난 한 해 동안 저희는 전 세계 60개 이상의 도시에서 맛있는 식사를 함께 나누었습니다."
                },
                {
                    "en": "Next month, we are launching new night market tours in Bangkok↑, Taipei↑, and Seoul↘.",
                    "chunking": "Next month, / we are launching new night market tours / in Bangkok↑, Taipei↑, and Seoul↘.",
                    "ko": "다음 달에 저희는 방콕, 타이베이, 그리고 서울에서 새로운 야시장 투어를 시작합니다."
                },
                {
                    "en": "Book your spot online today and enjoy a 15 percent early-bird discount!",
                    "chunking": "Book your spot online today / and enjoy a fifteen percent early-bird discount! ↘",
                    "ko": "오늘 온라인으로 자리를 예약하시고 15% 얼리버드 할인을 누리세요!"
                }
            ],
            "vocabulary": [
                {"word": "taste buds", "ipa": "[ˈteɪst bʌdz]", "pos": "명사", "meaning": "미뢰, 미각"},
                {"word": "delicious", "ipa": "[dɪˈlɪʃəs]", "pos": "형용사", "meaning": "맛있는"},
                {"word": "launching", "ipa": "[ˈlɔːntʃɪŋ]", "pos": "동사", "meaning": "출시하다, 시작하다"},
                {"word": "discount", "ipa": "[ˈdɪskaʊnt]", "pos": "명사", "meaning": "할인"}
            ],
            "readingTips": "고유명사 3개 나열 시 Bangkok(↗), Taipei(↗)는 올려 읽고, and Seoul(↘)에서 확실히 내려 읽으세요."
        },
        {
            "id": "p1-02",
            "part": 1,
            "qNum": "Part 1 - #02",
            "category": "기내·공항 방송",
            "topic": "Skyline Airways - Flight Boarding Announcement",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Thank you for flying with Skyline Airways on our nonstop service to San Francisco.",
                    "chunking": "Thank you for flying with Skyline Airways / on our nonstop service to San Francisco. ↘",
                    "ko": "샌프란시스코행 직항편 스카이라인 항공을 이용해 주셔서 감사합니다."
                },
                {
                    "en": "We are now inviting passengers in Group A to begin boarding through Gate 24.",
                    "chunking": "We are now inviting passengers in Group A / to begin boarding / through Gate twenty-four. ↘",
                    "ko": "지금부터 A그룹 승객 여러분께서는 24번 게이트를 통해 탑승을 시작해 주시기 바랍니다."
                },
                {
                    "en": "Please have your boarding pass↑, passport↑, and photo ID↘ ready for inspection.",
                    "chunking": "Please have your boarding pass↑, / passport↑, / and photo ID↘ / ready for inspection.",
                    "ko": "검사를 위해 탑승권, 여권, 그리고 사진이 부착된 신분증을 미리 준비해 주세요."
                },
                {
                    "en": "We wish you a pleasant, comfortable, and relaxing flight with us today.",
                    "chunking": "We wish you a pleasant↑, / comfortable↑, / and relaxing flight↘ / with us today.",
                    "ko": "오늘 저희와 함께 즐겁고 편안하며 여유로운 비행 되시기를 바랍니다."
                }
            ],
            "vocabulary": [
                {"word": "nonstop", "ipa": "[ˌnɑːnˈstɑːp]", "pos": "형용사", "meaning": "직항의, 무착륙의"},
                {"word": "passengers", "ipa": "[ˈpæsɪndʒərz]", "pos": "명사", "meaning": "승객들"},
                {"word": "inspection", "ipa": "[ɪnˈspekʃn]", "pos": "명사", "meaning": "검사, 점검"},
                {"word": "comfortable", "ipa": "[ˈkʌmftəbl]", "pos": "형용사", "meaning": "편안한 (3음절 발음 주의)"}
            ],
            "readingTips": "comfortable은 [컴-퍼-터-블] 4음절이 아닌 [컴프터블(kʌmftəbl)] 3음절로 자연스럽게 발음하세요."
        },
        {
            "id": "p1-03",
            "part": 1,
            "qNum": "Part 1 - #03",
            "category": "사내 로비·보안 안내",
            "topic": "Grandview Office Building - Lobby Renovation Notice",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Attention all visitors to the Grandview Office Building.",
                    "chunking": "Attention / all visitors / to the Grandview Office Building. ↘",
                    "ko": "그랜드뷰 오피스 빌딩 방문객 여러분께 안내 말씀드립니다."
                },
                {
                    "en": "Starting next Monday, the main lobby will undergo a two-week renovation to upgrade our security gates.",
                    "chunking": "Starting next Monday, / the main lobby will undergo a two-week renovation / to upgrade our security gates. ↘",
                    "ko": "다음 주 월요일부터 보안 게이트 업그레이드를 위해 메인 로비에서 2주간 리모델링 공사가 진행됩니다."
                },
                {
                    "en": "During this period, please use the side entrance↑, the parking garage elevator↑, or the rear walkway↘.",
                    "chunking": "During this period, / please use the side entrance↑, / the parking garage elevator↑, / or the rear walkway↘.",
                    "ko": "이 기간 동안에는 측면 출입구, 주차장 엘리베이터, 또는 후면 통로를 이용해 주십시오."
                },
                {
                    "en": "We apologize for any inconvenience and appreciate your cooperation.",
                    "chunking": "We apologize for any inconvenience / and appreciate your cooperation. ↘",
                    "ko": "불편을 끼쳐 드려 죄송하며 여러분의 협조에 감사드립니다."
                }
            ],
            "vocabulary": [
                {"word": "undergo", "ipa": "[ˌʌndərˈɡoʊ]", "pos": "동사", "meaning": "(공사·변화를) 겪다, 거치다"},
                {"word": "renovation", "ipa": "[ˌrenəˈveɪʃn]", "pos": "명사", "meaning": "보수 공사, 리모델링"},
                {"word": "inconvenience", "ipa": "[ˌɪnkənˈviːniəns]", "pos": "명사", "meaning": "불편"},
                {"word": "cooperation", "ipa": "[koʊˌɑːpəˈreɪʃn]", "pos": "명사", "meaning": "협조, 협력"}
            ],
            "readingTips": "inconvenience와 cooperation 같은 다음절 명사는 강세 음절(-ve-, -ra-)을 분명히 살려 읽어야 감점이 없습니다."
        },
        {
            "id": "p1-04",
            "part": 1,
            "qNum": "Part 1 - #04",
            "category": "컨퍼런스·행사 개회사",
            "topic": "Annual Green Tech Summit - Opening Remarks",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Good morning, ladies and gentlemen, and welcome to the Annual Green Tech Summit.",
                    "chunking": "Good morning, ladies and gentlemen, / and welcome to the Annual Green Tech Summit. ↘",
                    "ko": "안녕하십니까, 신사 숙녀 여러분, 연례 그린 테크 서밋에 오신 것을 환영합니다."
                },
                {
                    "en": "Today's sessions will focus on renewable energy↑, smart manufacturing↑, and sustainable packaging↘.",
                    "chunking": "Today's sessions will focus on / renewable energy↑, / smart manufacturing↑, / and sustainable packaging↘.",
                    "ko": "오늘 세션은 재생 에너지, 스마트 제조, 그리고 지속 가능한 패키징에 초점을 맞출 예정입니다."
                },
                {
                    "en": "Complimentary coffee, tea, and light refreshments are available in the hallway outside Hall B.",
                    "chunking": "Complimentary coffee↑, tea↑, and light refreshments↘ / are available in the hallway / outside Hall B.",
                    "ko": "무료 커피, 차, 그리고 가벼운 다과가 B홀 바깥 복도에 준비되어 있습니다."
                },
                {
                    "en": "Please remember to set your mobile phones to silent mode before the keynote speech begins.",
                    "chunking": "Please remember / to set your mobile phones to silent mode / before the keynote speech begins. ↘",
                    "ko": "기조연설이 시작되기 전에 휴대전화를 무음 모드로 설정해 주시기 바랍니다."
                }
            ],
            "vocabulary": [
                {"word": "renewable", "ipa": "[rɪˈnuːəbl]", "pos": "형용사", "meaning": "재생 가능한"},
                {"word": "sustainable", "ipa": "[səˈsteɪnəbl]", "pos": "형용사", "meaning": "지속 가능한"},
                {"word": "complimentary", "ipa": "[ˌkɑːmplɪˈmentri]", "pos": "형용사", "meaning": "무료로 제공되는"},
                {"word": "refreshments", "ipa": "[rɪˈfreʃmənts]", "pos": "명사", "meaning": "다과, 가벼운 식음료"}
            ],
            "readingTips": "complimentary [ˌkɑːmplɪˈmentri]와 refreshments [rɪˈfreʃmənts]는 파트 1과 파트 4에서 모두 최빈출되는 어휘입니다."
        },
        {
            "id": "p1-05",
            "part": 1,
            "qNum": "Part 1 - #05",
            "category": "쇼핑몰·매장 판촉 방송",
            "topic": "Maplewood Department Store - Weekend Mega Sale",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Welcome to Maplewood Department Store, where our Annual Autumn Sale is now underway!",
                    "chunking": "Welcome to Maplewood Department Store, / where our Annual Autumn Sale / is now underway! ↘",
                    "ko": "연례 가을 세일이 진행 중인 메이플우드 백화점에 오신 것을 환영합니다!"
                },
                {
                    "en": "Shoppers can save up to 40 percent on winter coats↑, leather boots↑, and cashmere sweaters↘ on the third floor.",
                    "chunking": "Shoppers can save up to forty percent / on winter coats↑, / leather boots↑, / and cashmere sweaters↘ / on the third floor.",
                    "ko": "쇼핑객 여러분께서는 3층에서 겨울 코트, 가죽 부츠, 그리고 캐시미어 스웨터를 최대 40% 할인받으실 수 있습니다."
                },
                {
                    "en": "In addition, if you sign up for our store membership card today, you'll receive a free tote bag at the customer service desk.",
                    "chunking": "In addition, / if you sign up for our store membership card today, ↗ / you'll receive a free tote bag / at the customer service desk. ↘",
                    "ko": "또한 오늘 매장 멤버십 카드를 신청하시면 고객 서비스 데스크에서 무료 에코백을 받으실 수 있습니다."
                }
            ],
            "vocabulary": [
                {"word": "underway", "ipa": "[ˌʌndərˈweɪ]", "pos": "형용사", "meaning": "진행 중인"},
                {"word": "leather", "ipa": "[ˈleðər]", "pos": "명사", "meaning": "가죽"},
                {"word": "cashmere", "ipa": "[ˈkæʃmɪr]", "pos": "명사", "meaning": "캐시미어"},
                {"word": "membership", "ipa": "[ˈmembərʃɪp]", "pos": "명사", "meaning": "회원 자격, 멤버십"}
            ],
            "readingTips": "if절 조건문에서는 today(↗) 끝을 살짝 올려 읽고 주절 마지막 desk(↘)에서 내려 읽으면 원어민 억양처럼 자연스럽습니다."
        },
        {
            "id": "p1-06",
            "part": 1,
            "qNum": "Part 1 - #06",
            "category": "건강·피트니스 광고",
            "topic": "Vitality Fitness Center - Grand Opening Promotion",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Are you looking for an effective way to stay active and boost your energy this winter?",
                    "chunking": "Are you looking for an effective way / to stay active / and boost your energy this winter? ↗",
                    "ko": "올겨울 활력을 유지하고 에너지를 높일 효과적인 방법을 찾고 계신가요?"
                },
                {
                    "en": "At Vitality Fitness Center, we offer yoga classes↑, strength training↑, and personal coaching↘ for all fitness levels.",
                    "chunking": "At Vitality Fitness Center, / we offer yoga classes↑, / strength training↑, / and personal coaching↘ / for all fitness levels.",
                    "ko": "바이탈리티 피트니스 센터에서는 모든 체력 수준에 맞춘 요가 수업, 근력 운동, 그리고 개인 코칭을 제공합니다."
                },
                {
                    "en": "Our facility is conveniently located right next to Central Subway Station and stays open 24 hours a day.",
                    "chunking": "Our facility is conveniently located / right next to Central Subway Station / and stays open twenty-four hours a day. ↘",
                    "ko": "저희 시설은 센트럴 지하철역 바로 옆의 편리한 위치에 있으며 하루 24시간 운영됩니다."
                },
                {
                    "en": "Stop by this weekend for a free tour and a complimentary fitness consultation!",
                    "chunking": "Stop by this weekend / for a free tour / and a complimentary fitness consultation! ↘",
                    "ko": "이번 주말에 방문하셔서 무료 투어와 무료 피트니스 상담을 받아보세요!"
                }
            ],
            "vocabulary": [
                {"word": "effective", "ipa": "[ɪˈfektɪv]", "pos": "형용사", "meaning": "효과적인"},
                {"word": "strength", "ipa": "[streŋkθ]", "pos": "명사", "meaning": "근력, 힘"},
                {"word": "conveniently", "ipa": "[kənˈviːniəntli]", "pos": "부사", "meaning": "편리하게"},
                {"word": "consultation", "ipa": "[ˌkɑːnslˈteɪʃn]", "pos": "명사", "meaning": "상담, 컨설팅"}
            ],
            "readingTips": "첫 문장이 의문문(Are you looking for...?)이므로 문장 끝 winter?(↗)의 억양을 자연스럽게 올려 읽으세요."
        },
        {
            "id": "p1-07",
            "part": 1,
            "qNum": "Part 1 - #07",
            "category": "라디오 날씨·교통 방송",
            "topic": "WKRB Morning Radio - Weather & Commuter Traffic Update",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Good morning, listeners! Here is your seven o'clock weather and traffic update on WKRB Radio.",
                    "chunking": "Good morning, listeners! / Here is your seven o'clock weather and traffic update / on WKRB Radio. ↘",
                    "ko": "좋은 아침입니다, 청취자 여러분! WKRB 라디오의 7시 날씨 및 교통 정보입니다."
                },
                {
                    "en": "Heavy rain is expected throughout the morning, followed by clear skies and mild temperatures in the afternoon.",
                    "chunking": "Heavy rain is expected throughout the morning, ↗ / followed by clear skies and mild temperatures / in the afternoon. ↘",
                    "ko": "오전 내내 강한 비가 예상되며, 오후에는 맑은 하늘과 온화한 기온이 이어지겠습니다."
                },
                {
                    "en": "Due to road construction on Highway 95, commuters should expect delays of up to 30 minutes.",
                    "chunking": "Due to road construction on Highway ninety-five, ↗ / commuters should expect delays / of up to thirty minutes. ↘",
                    "ko": "95번 고속도로의 도로 공사로 인해 통근자분들은 최대 30분의 지연을 예상하셔야 합니다."
                },
                {
                    "en": "We recommend taking public transportation↑, carpooling↑, or using an alternative route↘ today.",
                    "chunking": "We recommend / taking public transportation↑, / carpooling↑, / or using an alternative route↘ today.",
                    "ko": "오늘은 대중교통 이용, 카풀, 또는 우회 도로 이용을 권장합니다."
                }
            ],
            "vocabulary": [
                {"word": "throughout", "ipa": "[θruːˈaʊt]", "pos": "전치사", "meaning": "~내내, 줄곧"},
                {"word": "temperatures", "ipa": "[ˈtemprətʃərz]", "pos": "명사", "meaning": "기온, 온도"},
                {"word": "commuters", "ipa": "[kəˈmjuːtərz]", "pos": "명사", "meaning": "통근자들"},
                {"word": "alternative", "ipa": "[ɔːlˈtɜːrnətɪv]", "pos": "형용사", "meaning": "대안의, 우회의"}
            ],
            "readingTips": "temperatures는 [템-퍼-러-처스]가 아니라 [템프러처즈(temprətʃərz)]로 가운데 모음을 약화시켜 읽는 것이 핵심입니다."
        },
        {
            "id": "p1-08",
            "part": 1,
            "qNum": "Part 1 - #08",
            "category": "호텔 투숙객 환영 안내",
            "topic": "Oceanfront Resort & Spa - Guest Welcome Guide",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Welcome to the Oceanfront Resort and Spa, your premier destination for relaxation.",
                    "chunking": "Welcome to the Oceanfront Resort and Spa, / your premier destination / for relaxation. ↘",
                    "ko": "휴식을 위한 최고의 여행지, 오션프론트 리조트 앤 스파에 오신 것을 환영합니다."
                },
                {
                    "en": "Breakfast is served daily from 6:30 to 10:30 AM in the Palm Tree Dining Room on the ground floor.",
                    "chunking": "Breakfast is served daily / from six-thirty to ten-thirty AM / in the Palm Tree Dining Room / on the ground floor. ↘",
                    "ko": "조식은 매일 오전 6시 30분부터 10시 30분까지 1층 팜트리 다이닝 룸에서 제공됩니다."
                },
                {
                    "en": "As our guest, you have unlimited access to the heated swimming pool↑, the fitness studio↑, and the rooftop lounge↘.",
                    "chunking": "As our guest, / you have unlimited access / to the heated swimming pool↑, / the fitness studio↑, / and the rooftop lounge↘.",
                    "ko": "투숙객 여러분께서는 온수 수영장, 피트니스 스튜디오, 그리고 루프탑 라운지를 무제한으로 이용하실 수 있습니다."
                },
                {
                    "en": "If you need extra towels or room service, simply dial zero from your in-room telephone.",
                    "chunking": "If you need extra towels or room service, ↗ / simply dial zero / from your in-room telephone. ↘",
                    "ko": "추가 수건이나 룸서비스가 필요하시면 객실 내 전화기에서 0번을 눌러주세요."
                }
            ],
            "vocabulary": [
                {"word": "premier", "ipa": "[prɪˈmɪr]", "pos": "형용사", "meaning": "최고의, 으뜸가는"},
                {"word": "relaxation", "ipa": "[ˌriːlækˈseɪʃn]", "pos": "명사", "meaning": "휴식"},
                {"word": "unlimited", "ipa": "[ʌnˈlɪmɪtɪd]", "pos": "형용사", "meaning": "무제한의"},
                {"word": "heated", "ipa": "[ˈhiːtɪd]", "pos": "형용사", "meaning": "온수의, 난방이 된"}
            ],
            "readingTips": "시각 표현 6:30 to 10:30 AM은 [six-thirty to ten-thirty A-M]으로 또박또박 읽고, Palm의 l은 묵음([pɑːm])임에 유의하세요."
        },
        {
            "id": "p1-09",
            "part": 1,
            "qNum": "Part 1 - #09",
            "category": "박물관·전시관 오디오 가이드",
            "topic": "Metropolitan Science Museum - Interactive Tour Introduction",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Thank you for visiting the Metropolitan Science Museum, where curiosity comes to life.",
                    "chunking": "Thank you for visiting the Metropolitan Science Museum, / where curiosity comes to life. ↘",
                    "ko": "호기심이 살아 숨 쉬는 메트로폴리탄 과학 박물관을 방문해 주셔서 감사합니다."
                },
                {
                    "en": "On the second floor, you can explore interactive exhibits on space exploration↑, robotics↑, and marine biology↘.",
                    "chunking": "On the second floor, / you can explore interactive exhibits / on space exploration↑, / robotics↑, / and marine biology↘.",
                    "ko": "2층에서는 우주 탐사, 로봇 공학, 그리고 해양 생물학에 관한 체험형 전시물을 탐험하실 수 있습니다."
                },
                {
                    "en": "Flash photography, food, and beverages are strictly prohibited inside all exhibition galleries.",
                    "chunking": "Flash photography↑, food↑, and beverages↘ / are strictly prohibited / inside all exhibition galleries.",
                    "ko": "모든 전시실 내부에서는 플래시 촬영, 음식물, 그리고 음료 반입이 엄격히 금지되어 있습니다."
                },
                {
                    "en": "Don't forget to visit our museum gift shop on your way out for unique souvenirs and educational books!",
                    "chunking": "Don't forget to visit our museum gift shop on your way out / for unique souvenirs and educational books! ↘",
                    "ko": "나가시는 길에 박물관 기념품점에 들러 특별한 기념품과 교육용 도서를 만나보세요!"
                }
            ],
            "vocabulary": [
                {"word": "curiosity", "ipa": "[ˌkjʊriˈɑːsəti]", "pos": "명사", "meaning": "호기심"},
                {"word": "exhibits", "ipa": "[ɪɡˈzɪbɪts]", "pos": "명사", "meaning": "전시물 (h 묵음 주의)"},
                {"word": "prohibited", "ipa": "[prəˈhɪbɪtɪd]", "pos": "형용사/분사", "meaning": "금지된"},
                {"word": "souvenirs", "ipa": "[ˌsuːvəˈnɪrz]", "pos": "명사", "meaning": "기념품"}
            ],
            "readingTips": "exhibits [ɪɡˈzɪbɪts]에서는 h가 묵음이고, souvenirs [ˌsuːvəˈnɪrz]는 뒷음절(-nirs)에 강세가 옵니다."
        },
        {
            "id": "p1-10",
            "part": 1,
            "qNum": "Part 1 - #10",
            "category": "고객센터 자동응답 안내",
            "topic": "Horizon Telecom - Automated Customer Support",
            "prepTime": 45,
            "responseTime": 45,
            "sentences": [
                {
                    "en": "Thank you for calling Horizon Telecom, your trusted partner in high-speed internet and mobile services.",
                    "chunking": "Thank you for calling Horizon Telecom, / your trusted partner / in high-speed internet and mobile services. ↘",
                    "ko": "초고속 인터넷 및 모바일 서비스의 든든한 파트너, 호라이즌 텔레콤에 전화해 주셔서 감사합니다."
                },
                {
                    "en": "Our customer support representatives are available Monday through Friday from 8:00 AM to 7:00 PM.",
                    "chunking": "Our customer support representatives are available / Monday through Friday / from eight AM to seven PM. ↘",
                    "ko": "저희 고객 지원 상담원은 월요일부터 금요일까지 오전 8시에서 오후 7시 사이에 통화 가능합니다."
                },
                {
                    "en": "You can easily check your monthly bill↑, upgrade your data plan↑, or report a technical issue↘ on our mobile app.",
                    "chunking": "You can easily check your monthly bill↑, / upgrade your data plan↑, / or report a technical issue↘ / on our mobile app.",
                    "ko": "모바일 앱에서 월간 요금 조회, 데이터 요금제 업그레이드, 또는 기술적 문제 신고를 간편하게 하실 수 있습니다."
                },
                {
                    "en": "Please stay on the line, and the next available agent will be with you shortly.",
                    "chunking": "Please stay on the line, ↗ / and the next available agent / will be with you shortly. ↘",
                    "ko": "전화를 끊지 말고 기다려 주시면 곧 상담 가능한 직원이 연결해 드리겠습니다."
                }
            ],
            "vocabulary": [
                {"word": "representatives", "ipa": "[ˌreprɪˈzentətɪvz]", "pos": "명사", "meaning": "상담원, 담당자"},
                {"word": "available", "ipa": "[əˈveɪləbl]", "pos": "형용사", "meaning": "이용 가능한, 통화 가능한"},
                {"word": "technical", "ipa": "[ˈteknɪkl]", "pos": "형용사", "meaning": "기술적인"},
                {"word": "shortly", "ipa": "[ˈʃɔːrtli]", "pos": "부사", "meaning": "곧, 잠시 후"}
            ],
            "readingTips": "representatives [ˌreprɪˈzentətɪvz]는 -zen-에 강세를 두어 리듬감 있게 발음하세요."
        }
    ]


def build_part2():
    """Part 2: 10문항 (고화질 실제 기출 사진 Base64 내장 + 문장별 발음 + 만능문장 + 핵심어휘 + 해설)"""
    items = [
        {
            "id": "p2-01",
            "part": 2,
            "qNum": "Part 2 - #01",
            "category": "실내 마트·계산대",
            "topic": "슈퍼마켓 계산대 바코드 스캔 및 고객 결제 (Supermarket Checkout)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q12_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at a grocery store checkout counter.", "ko": "이 사진은 식료품점 계산대에서 찍힌 사진입니다."},
                {"step": "2. 왼쪽 계산원 묘사", "en": "On the left side of the picture, a female cashier wearing a green vest is holding a food container and scanning the item.", "ko": "사진 왼쪽에는 초록색 조끼를 입은 여성 계산원이 식품 용기를 들고 바코드를 스캔하고 있습니다."},
                {"step": "3. 오른쪽 고객 묘사", "en": "On the right side, a customer with blonde hair in a blue jacket is smiling and looking at the item being scanned.", "ko": "오른쪽에는 파란 재킷을 입은 금발 머리 고객이 미소를 지으며 스캔되는 물건을 바라보고 있습니다."},
                {"step": "4. 전경/주변 사물", "en": "Next to them on the counter, there is a cash register monitor and a payment terminal.", "ko": "그들 옆 계산대 위에는 포스기 모니터와 결제 단말기가 있습니다."},
                {"step": "5. 총평 마무리", "en": "Overall, it seems like the customer is paying for her groceries in a friendly atmosphere.", "ko": "전반적으로 손님이 친절한 분위기 속에서 식료품을 계산하고 있는 것 같습니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken at a grocery store.", "ko": "이 사진은 식료품점에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #001 (실내 매장 첫 문장 공식)"},
                {"en": "A cashier wearing a uniform is scanning the item.", "ko": "유니폼을 입은 계산원이 상품을 스캔하고 있습니다.", "tip": "시계토끼 만능 #011 & #027 (계산대 필수 동작)"},
                {"en": "The customer is waiting to pay for her items.", "ko": "손님이 물건값을 계산하기 위해 기다리고 있습니다.", "tip": "시계토끼 만능 #027 (쇼핑 계산대 묘사)"}
            ],
            "vocabulary": [
                {"word": "checkout counter", "ipa": "[ˈtʃekaʊt ˈkaʊntər]", "pos": "명사", "meaning": "계산대"},
                {"word": "cashier", "ipa": "[kæˈʃɪr]", "pos": "명사", "meaning": "계산원, 캐셔"},
                {"word": "scan the item", "ipa": "[skæn ði ˈaɪtəm]", "pos": "숙어", "meaning": "상품(바코드)을 스캔하다"},
                {"word": "cash register", "ipa": "[kæʃ ˈredʒɪstər]", "pos": "명사", "meaning": "금전 등록기, 포스기"}
            ],
            "explanation": "마트·상점 계산대 사진에서는 왼쪽의 직원(cashier wearing a vest, scanning the item)과 오른쪽의 손님(customer smiling, paying for groceries), 그리고 계산대 위 포스기(cash register / monitor) 세 가지를 짚어주면 만점입니다."
        },
        {
            "id": "p2-02",
            "part": 2,
            "qNum": "Part 2 - #02",
            "category": "야외 공원·피크닉",
            "topic": "화창한 잔디 공원 돗자리 휴식 및 자전거 타기 (Sunny City Park)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q22_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken outdoors at a spacious park.", "ko": "이 사진은 넓은 야외 공원에서 찍힌 사진입니다."},
                {"step": "2. 전경 왼쪽 인물", "en": "In the foreground on the left, two people are sitting on a mat on the grass and relaxing together.", "ko": "왼쪽 전경에는 두 사람이 잔디밭 위 매트에 앉아 함께 휴식을 취하고 있습니다."},
                {"step": "3. 중앙 및 오른쪽 인물", "en": "Along the walkway in the middle, some people are taking a walk, and three people are riding bicycles on the right.", "ko": "가운데 산책로를 따라 몇몇 사람들이 산책을 하고 있고, 오른쪽에는 세 사람이 자전거를 타고 있습니다."},
                {"step": "4. 배경 자연 묘사", "en": "In the background, I can see many tall green trees and a wide grassy field.", "ko": "배경에는 키 큰 푸른 나무들과 넓은 잔디밭이 보입니다."},
                {"step": "5. 총평 마무리", "en": "Overall, it looks like a peaceful and sunny weekend at the park.", "ko": "전반적으로 공원에서의 평화롭고 화창한 주말처럼 보입니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken outdoors at a park.", "ko": "이 사진은 야외 공원에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #006 (야외 공원 첫 문장)"},
                {"en": "They are sitting on the grass and relaxing.", "ko": "그들은 잔디밭에 앉아 휴식을 취하고 있습니다.", "tip": "시계토끼 만능 #035 (공원 돗자리 휴식 묘사)"},
                {"en": "Some people are riding bicycles along the path.", "ko": "몇몇 사람들이 산책로를 따라 자전거를 타고 있습니다.", "tip": "시계토끼 만능 #032 (야외 자전거 동작)"}
            ],
            "vocabulary": [
                {"word": "spacious", "ipa": "[ˈspeɪʃəs]", "pos": "형용사", "meaning": "넓은, 탁 트인"},
                {"word": "foreground", "ipa": "[ˈfɔːrɡraʊnd]", "pos": "명사", "meaning": "전경, 사진 앞쪽"},
                {"word": "riding bicycles", "ipa": "[ˈraɪdɪŋ ˈbaɪsɪklz]", "pos": "숙어", "meaning": "자전거를 타고 있는"},
                {"word": "grassy field", "ipa": "[ˈɡræsi fiːld]", "pos": "명사", "meaning": "잔디밭, 초원"}
            ],
            "explanation": "야외 공원 전경 사진은 구역을 3등분하여 1) 앞쪽 잔디밭(sitting on the grass) -> 2) 중간 산책로(walking / riding bicycles) -> 3) 뒤쪽 배경 나무(tall green trees in the background) 순으로 묘사하면 가장 체계적입니다."
        },
        {
            "id": "p2-03",
            "part": 2,
            "qNum": "Part 2 - #03",
            "category": "대중교통·지하철역",
            "topic": "지하철 승강장 열차 진입 및 승객 탑승 대기 (Subway Platform)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q14_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at an indoor subway station platform.", "ko": "이 사진은 실내 지하철역 승강장에서 찍힌 사진입니다."},
                {"step": "2. 왼쪽 인물 묘사", "en": "On the left side of the picture, a man wearing a brown coat and a blue backpack is walking while holding a white plastic bag.", "ko": "사진 왼쪽에는 갈색 코트에 파란 백팩을 멘 남성이 흰 비닐봉지를 든 채 걸어가고 있습니다."},
                {"step": "3. 오른쪽 인물 및 열차", "en": "On the right side, a yellow subway train has stopped at the platform, and a man carrying a shoulder bag is standing near the train.", "ko": "오른쪽에는 노란색 지하철 열차가 승강장에 멈춰 서 있고, 가방을 멘 남성이 열차 근처에 서 있습니다."},
                {"step": "4. 배경 구조물 묘사", "en": "In the background, several passengers are boarding the train, and there are large white pillars along the platform.", "ko": "배경에는 여러 승객들이 열차에 탑승하고 있으며, 승강장을 따라 커다란 흰 기둥들이 줄지어 있습니다."},
                {"step": "5. 총평 마무리", "en": "Overall, commuters are busy moving at the subway station.", "ko": "전반적으로 통근객들이 지하철역에서 분주하게 이동하고 있습니다."}
            ],
            "magicSentences": [
                {"en": "He is wearing a backpack and walking along the platform.", "ko": "그는 백팩을 메고 승강장을 따라 걷고 있습니다.", "tip": "시계토끼 만능 #010 & #031 결합"},
                {"en": "Several passengers are getting on the subway train.", "ko": "여러 승객들이 지하철 열차에 탑승하고 있습니다.", "tip": "대중교통 탑승 핵심 표현"},
                {"en": "There are bright lights on the ceiling.", "ko": "천장에는 밝은 조명들이 켜져 있습니다.", "tip": "시계토끼 만능 #045 (실내 천장 배경 묘사)"}
            ],
            "vocabulary": [
                {"word": "platform", "ipa": "[ˈplætfɔːrm]", "pos": "명사", "meaning": "(기차·지하철) 승강장"},
                {"word": "backpack", "ipa": "[ˈbækpæk]", "pos": "명사", "meaning": "배낭, 백팩"},
                {"word": "boarding", "ipa": "[ˈbɔːrdɪŋ]", "pos": "동사/분사", "meaning": "(열차·버스에) 탑승하는"},
                {"word": "pillars", "ipa": "[ˈpɪlərz]", "pos": "명사", "meaning": "기둥들"}
            ],
            "explanation": "기차역·지하철역 승강장 사진에서는 걸어가는 승객(walking along the platform), 멈춰 서 있는 열차(a subway train stopped at the station), 그리고 탑승하는 승객들(boarding / getting on the train)을 차례로 묘사하세요."
        },
        {
            "id": "p2-04",
            "part": 2,
            "qNum": "Part 2 - #04",
            "category": "학교·강의실",
            "topic": "강의실 화이트보드 판서 강사 및 수강생들 (Classroom Lecture)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q06_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken in a bright classroom.", "ko": "이 사진은 밝은 강의실에서 찍힌 사진입니다."},
                {"step": "2. 오른쪽 강사 묘사", "en": "On the right side of the picture, a male instructor wearing a purple shirt is standing and pointing at the whiteboard.", "ko": "사진 오른쪽에는 자주색 셔츠를 입은 남성 강사가 서서 화이트보드를 가리키고 있습니다."},
                {"step": "3. 왼쪽 학생들 묘사", "en": "On the left side, five students are sitting at long desks and focusing on the teacher's lecture.", "ko": "왼쪽에는 다섯 명의 학생들이 긴 책상에 앉아 강사의 수업에 집중하고 있습니다."},
                {"step": "4. 책상 및 창문 묘사", "en": "On the desks, there are textbooks, notebooks, and water bottles, and large windows with blinds can be seen on the left wall.", "ko": "책상 위에는 교재, 공책, 물병들이 놓여 있고 왼쪽 벽면에는 블라인드가 쳐진 큰 창문이 보입니다."},
                {"step": "5. 총평 마무리", "en": "Overall, it seems like everyone is concentrating hard on the class.", "ko": "전반적으로 모두가 수업에 열심히 집중하고 있는 것 같습니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken in a classroom.", "ko": "이 사진은 교실(강의실)에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #005 (교육 공간 첫 문장)"},
                {"en": "He is standing and pointing at the whiteboard.", "ko": "그는 서서 화이트보드를 가리키고 있습니다.", "tip": "시계토끼 만능 #016 & #038 (강의·발표 핵심 동작)"},
                {"en": "The students are sitting at the desks and listening carefully.", "ko": "학생들은 책상에 앉아 주의 깊게 듣고 있습니다.", "tip": "시계토끼 만능 #013 & #039 결합"}
            ],
            "vocabulary": [
                {"word": "instructor", "ipa": "[ɪnˈstrʌktər]", "pos": "명사", "meaning": "강사, 교사"},
                {"word": "whiteboard", "ipa": "[ˈwaɪtbɔːrd]", "pos": "명사", "meaning": "화이트보드"},
                {"word": "blinds", "ipa": "[blaɪndz]", "pos": "명사", "meaning": "창문 블라인드"},
                {"word": "concentrating", "ipa": "[ˈkɑːnsntreɪtɪŋ]", "pos": "동사/분사", "meaning": "집중하는"}
            ],
            "explanation": "강의실 수업 사진은 오른쪽의 강사(standing in front of the whiteboard, pointing at the board)와 왼쪽의 수강생들(sitting at the desks, listening to the lecture)의 1:다수 대칭 구도로 설명하면 완벽합니다."
        },
        {
            "id": "p2-05",
            "part": 2,
            "qNum": "Part 2 - #05",
            "category": "사무실·컴퓨터 업무",
            "topic": "사무실 남성 2인 나란히 노트북·모니터 업무 (Office Desk)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q01_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken in a bright office.", "ko": "이 사진은 밝은 사무실에서 찍힌 사진입니다."},
                {"step": "2. 오른쪽 인물 묘사", "en": "On the right side of the picture, a man wearing glasses and a gray sweater is typing on a keyboard.", "ko": "사진 오른쪽에는 안경과 회색 스웨터를 입은 남성이 키보드로 타이핑을 하고 있습니다."},
                {"step": "3. 왼쪽 인물 묘사", "en": "Next to him, another man in a black shirt is also sitting at the desk and working on a computer.", "ko": "그 옆에는 검은 셔츠를 입은 또 다른 남성도 책상에 앉아 컴퓨터로 일하고 있습니다."},
                {"step": "4. 책상 위 사물", "en": "On the desk, I can see a laptop on a stand, headphones, and some small potted plants.", "ko": "책상 위에는 거치대 위의 노트북, 헤드폰, 그리고 작은 화분들이 보입니다."},
                {"step": "5. 총평 마무리", "en": "Overall, it seems like they are busy working on their tasks.", "ko": "전반적으로 그들은 각자의 업무로 바쁘게 일하고 있는 것 같습니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken in an office.", "ko": "이 사진은 사무실에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #002 (오피스 사진 1순위 첫 문장)"},
                {"en": "He is wearing glasses and typing on a keyboard.", "ko": "그는 안경을 쓰고 키보드로 타이핑하고 있습니다.", "tip": "시계토끼 만능 #009 & #019 결합"},
                {"en": "Overall, it seems like they are busy working.", "ko": "전반적으로 그들은 바쁘게 일하고 있는 것 같습니다.", "tip": "시계토끼 만능 #049 (오피스 총평 마무리)"}
            ],
            "vocabulary": [
                {"word": "typing on a keyboard", "ipa": "[ˈtaɪpɪŋ ɑːn ə ˈkiːbɔːrd]", "pos": "동작구", "meaning": "키보드로 타자를 치는"},
                {"word": "computer monitor", "ipa": "[kəmˈpjuːtər ˈmɑːnɪtər]", "pos": "명사", "meaning": "컴퓨터 모니터"},
                {"word": "headphones", "ipa": "[ˈhedfoʊnz]", "pos": "명사", "meaning": "헤드폰"},
                {"word": "potted plants", "ipa": "[ˈpɑːtɪd plænts]", "pos": "명사", "meaning": "화분에 심어진 식물들"}
            ],
            "explanation": "사무실 2인 업무 사진입니다. 두 사람의 옷차림(gray sweater vs. black shirt)을 구분해 주고, 책상 위 소품(laptop, monitor, potted plants)을 짚어주면 완벽합니다."
        },
        {
            "id": "p2-06",
            "part": 2,
            "qNum": "Part 2 - #06",
            "category": "사무실·회의",
            "topic": "고층 사무실 정장 3인 서류 논의 및 창밖 빌딩 (Business Discussion)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q02_photo.jpg",
            "sentences": [
                {"step": "1. 장소 및 복장", "en": "This is a picture taken in an office, and there are three people wearing formal clothes.", "ko": "이 사진은 사무실에서 찍힌 사진이며 정장을 입은 세 사람이 있습니다."},
                {"step": "2. 중앙 남녀 묘사", "en": "In the middle of the picture, a woman in a beige suit is holding a document and pointing at the table.", "ko": "사진 가운데에는 베이지색 정장을 입은 여성이 서류를 들고 테이블을 가리키고 있습니다."},
                {"step": "3. 옆 인물 묘사", "en": "Next to her, a man wearing a gray suit and a tie is looking down at the paper with her.", "ko": "그녀 옆에는 회색 정장과 넥타이를 맨 남성이 그녀와 함께 서류를 내려다보고 있습니다."},
                {"step": "4. 배경 묘사", "en": "In the background, I can see tall buildings through the large glass windows.", "ko": "배경에는 커다란 유리창 너머로 고층 빌딩들이 보입니다."},
                {"step": "5. 총평 마무리", "en": "Overall, it looks like they are having a serious business discussion.", "ko": "전반적으로 그들은 진지한 업무 논의를 나누고 있는 것처럼 보입니다."}
            ],
            "magicSentences": [
                {"en": "Most of them are wearing formal clothes.", "ko": "그들 대부분은 정장을 입고 있습니다.", "tip": "시계토끼 만능 #008 (비즈니스 복장 일괄 묘사)"},
                {"en": "She is holding a document and pointing at the table.", "ko": "그녀는 서류를 들고 테이블을 가리키고 있습니다.", "tip": "시계토끼 만능 #015 & #016 결합"},
                {"en": "In the background, I can see tall buildings through the window.", "ko": "배경에는 창문 너머로 고층 빌딩들이 보입니다.", "tip": "시계토끼 만능 #047 (고층 사무실 배경 공식)"}
            ],
            "vocabulary": [
                {"word": "formal clothes", "ipa": "[ˈfɔːrml kloʊðz]", "pos": "명사구", "meaning": "정장, 격식 있는 복장"},
                {"word": "document", "ipa": "[ˈdɑːkjumənt]", "pos": "명사", "meaning": "문서, 서류"},
                {"word": "pointing at", "ipa": "[ˈpɔɪntɪŋ æt]", "pos": "숙어", "meaning": "~을 가리키는"},
                {"word": "discussion", "ipa": "[dɪˈskʌʃn]", "pos": "명사", "meaning": "논의, 토의"}
            ],
            "explanation": "비즈니스 미팅 사진에서 정장 차림을 일괄 묘사하는 'wearing formal clothes'와 서류를 보며 대화하는 'looking at a document'는 가장 활용도가 높은 만능 표현입니다."
        },
        {
            "id": "p2-07",
            "part": 2,
            "qNum": "Part 2 - #07",
            "category": "회의실·프레젠테이션",
            "topic": "회의실 차트 보드 프레젠테이션 발표 및 필기 (Presentation Meeting)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q04_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken in a meeting room, and five people are having a meeting.", "ko": "이 사진은 회의실에서 찍힌 사진이며 다섯 사람이 회의를 하고 있습니다."},
                {"step": "2. 중앙 발표자 묘사", "en": "In the middle of the picture, a woman wearing a gray dress is standing and pointing at the graphs on the whiteboard.", "ko": "사진 가운데에는 회색 원피스를 입은 여성이 서서 화이트보드의 그래프를 가리키며 발표하고 있습니다."},
                {"step": "3. 참석자 동작 묘사", "en": "Around the glass table, four people are sitting and listening to her presentation, and one man on the right is taking notes.", "ko": "유리 테이블 주변에는 네 사람이 앉아 발표를 경청하고 있고, 오른쪽의 한 남성은 노트에 필기를 하고 있습니다."},
                {"step": "4. 테이블 위 사물", "en": "On the table, there is a water pitcher and several glasses of water.", "ko": "테이블 위에는 물병(저그)과 여러 개의 물잔이 놓여 있습니다."},
                {"step": "5. 총평 마무리", "en": "Overall, everyone is paying close attention to the business presentation.", "ko": "전반적으로 모두가 비즈니스 발표에 깊이 집중하고 있습니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken in a meeting room.", "ko": "이 사진은 회의실에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #003 (회의실 첫 문장)"},
                {"en": "She is making a presentation and pointing at the whiteboard.", "ko": "그녀는 발표를 하며 화이트보드를 가리키고 있습니다.", "tip": "시계토끼 만능 #016 & #038 결합"},
                {"en": "He is taking notes in a notebook.", "ko": "그는 공책에 필기를 하고 있습니다.", "tip": "시계토끼 만능 #020 (회의·수업 필기 동작)"}
            ],
            "vocabulary": [
                {"word": "making a presentation", "ipa": "[ˈmeɪkɪŋ ə ˌpriːznˈteɪʃn]", "pos": "숙어", "meaning": "프레젠테이션(발표)을 하는"},
                {"word": "graphs", "ipa": "[ɡræfs]", "pos": "명사", "meaning": "그래프, 도표"},
                {"word": "taking notes", "ipa": "[ˈteɪkɪŋ noʊts]", "pos": "숙어", "meaning": "필기하는, 메모하는"},
                {"word": "paying attention", "ipa": "[ˈpeɪɪŋ əˈtenʃn]", "pos": "숙어", "meaning": "주의를 기울이는"}
            ],
            "explanation": "회의실 발표 사진에서는 서서 발표하는 사람(standing and making a presentation)과 앉아서 경청하거나 필기하는 참석자들(sitting around the table and taking notes)을 구분해 주면 만점입니다."
        },
        {
            "id": "p2-08",
            "part": 2,
            "qNum": "Part 2 - #08",
            "category": "교실·발표 수업",
            "topic": "교실 학생들 손들기 발표 및 지구본·세계지도 배경 (School Classroom)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q07_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken in a school classroom.", "ko": "이 사진은 학교 교실에서 찍힌 사진입니다."},
                {"step": "2. 왼쪽 교사 묘사", "en": "On the left side of the picture, a male teacher wearing glasses and a gray jacket is standing and holding a tablet PC.", "ko": "사진 왼쪽에는 안경과 회색 재킷을 입은 남자 선생님이 태블릿 PC를 들고 서 있습니다."},
                {"step": "3. 오른쪽 학생들 묘사", "en": "On the right side, six students are sitting at wooden desks, and several of them are raising their hands high.", "ko": "오른쪽에는 여섯 명의 학생들이 나무 책상에 앉아 있으며, 그중 여러 명이 손을 높이 들고 있습니다."},
                {"step": "4. 교실 뒤편 배경", "en": "In the background, I can see a globe, bookshelves full of books, and a world map on the wall.", "ko": "배경에는 지구본과 책이 가득 꽂힌 책장, 그리고 벽면에 걸린 세계지도가 보입니다."},
                {"step": "5. 총평 마무리", "en": "Overall, the students are actively participating in the lesson.", "ko": "전반적으로 학생들이 수업에 적극적으로 참여하고 있습니다."}
            ],
            "magicSentences": [
                {"en": "Some of the students are raising their hands.", "ko": "학생들 중 일부가 손을 들고 있습니다.", "tip": "시계토끼 만능 #040 (교실·세미나 질문 동작)"},
                {"en": "He is standing and holding a tablet PC.", "ko": "그는 서서 태블릿 PC를 들고 있습니다.", "tip": "시계토끼 만능 #015 응용"},
                {"en": "They are actively participating in the class.", "ko": "그들은 수업에 적극적으로 참여하고 있습니다.", "tip": "교실·세미나 사진 총평 마무리 문장"}
            ],
            "vocabulary": [
                {"word": "raising their hands", "ipa": "[ˈreɪzɪŋ ðer hændz]", "pos": "숙어", "meaning": "손을 들고 있는"},
                {"word": "globe", "ipa": "[ɡloʊb]", "pos": "명사", "meaning": "지구본"},
                {"word": "world map", "ipa": "[wɜːrld mæp]", "pos": "명사", "meaning": "세계지도"},
                {"word": "participating", "ipa": "[pɑːrˈtɪsɪpeɪtɪŋ]", "pos": "동사/분사", "meaning": "참여하는"}
            ],
            "explanation": "교실/강연장 사진에서 손을 드는 동작은 타동사 raise를 써서 'raising their hands'로 표현합니다(rising과 혼동하지 않도록 주의하세요)."
        },
        {
            "id": "p2-09",
            "part": 2,
            "qNum": "Part 2 - #09",
            "category": "레스토랑·카페",
            "topic": "레스토랑 테이블 식사 대화 및 웨이트리스 서빙 (Restaurant Dining)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q09_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at a restaurant.", "ko": "이 사진은 레스토랑에서 찍힌 사진입니다."},
                {"step": "2. 전경 3인 묘사", "en": "In the foreground, three people are sitting at a table and having a conversation while eating salad.", "ko": "전경에는 세 사람이 테이블에 앉아 샐러드를 먹으며 대화를 나누고 있습니다."},
                {"step": "3. 인물 복장 묘사", "en": "The man on the left is wearing a blue shirt and a striped tie, and the two women are smiling.", "ko": "왼쪽의 남성은 파란 셔츠와 줄무늬 넥타이를 매고 있고, 두 여성은 미소를 짓고 있습니다."},
                {"step": "4. 배경 종업원 묘사", "en": "In the background on the right, a waitress wearing a uniform is serving food to customers at another table.", "ko": "오른쪽 배경에는 유니폼을 입은 웨이트리스가 다른 테이블 손님들에게 음식을 서빙하고 있습니다."},
                {"step": "5. 총평 마무리", "en": "Overall, the customers are enjoying their meal in a pleasant atmosphere.", "ko": "전반적으로 손님들이 기분 좋은 분위기 속에서 식사를 즐기고 있습니다."}
            ],
            "magicSentences": [
                {"en": "This is a picture taken at a restaurant.", "ko": "이 사진은 식당(레스토랑)에서 찍힌 사진입니다.", "tip": "시계토끼 만능 #004 (식당·카페 첫 문장)"},
                {"en": "They are sitting at a table and having a conversation.", "ko": "그들은 테이블에 앉아 대화를 나누고 있습니다.", "tip": "시계토끼 만능 #013 & #017 결합"},
                {"en": "A waitress wearing a uniform is serving food to customers.", "ko": "유니폼을 입은 종업원이 손님들에게 음식을 서빙하고 있습니다.", "tip": "시계토끼 만능 #011 & #024 결합"}
            ],
            "vocabulary": [
                {"word": "foreground", "ipa": "[ˈfɔːrɡraʊnd]", "pos": "명사", "meaning": "전경, 사진 앞쪽"},
                {"word": "conversation", "ipa": "[ˌkɑːnvərˈseɪʃn]", "pos": "명사", "meaning": "대화"},
                {"word": "waitress", "ipa": "[ˈweɪtrəs]", "pos": "명사", "meaning": "여성 종업원"},
                {"word": "serving food", "ipa": "[ˈsɜːrvɪŋ fuːd]", "pos": "동작구", "meaning": "음식을 서빙하는"}
            ],
            "explanation": "식당 사진은 전경의 손님 그룹(sitting at a table, eating food, having a conversation)과 배경의 직원(wearing a uniform, serving food to customers)을 나눠 묘사하면 구도가 명확해집니다."
        },
        {
            "id": "p2-10",
            "part": 2,
            "qNum": "Part 2 - #10",
            "category": "야외 시장·식료품점",
            "topic": "야외 청과물 시장 과일 가판대 쇼핑 장면 (Outdoor Fruit Market)",
            "prepTime": 45,
            "responseTime": 30,
            "imageRelPath": "toeic_part2_images/part2_q10_photo.jpg",
            "sentences": [
                {"step": "1. 장소 소개", "en": "This is a picture taken at an outdoor fruit market.", "ko": "이 사진은 야외 과일 시장에서 찍힌 사진입니다."},
                {"step": "2. 오른쪽 고객 묘사", "en": "On the right side of the picture, a woman wearing a gray padded jacket and jeans is looking at the fruits.", "ko": "사진 오른쪽에는 회색 패딩 점퍼와 청바지를 입은 여성이 과일들을 살펴보고 있습니다."},
                {"step": "3. 가판대 뒤 상인", "en": "Behind the stand, a male vendor wearing a cap and a black jacket is working.", "ko": "가판대 뒤에서는 모자와 검은 재킷을 입은 남성 상인이 일하고 있습니다."},
                {"step": "4. 전경 상품 묘사", "en": "In the foreground, various fruits such as oranges, lemons, bananas, and pineapples are on display with price tags.", "ko": "전경에는 오렌지, 레몬, 바나나, 파인애플 같은 다양한 과일들이 가격표와 함께 진열되어 있습니다."},
                {"step": "5. 총평 마무리", "en": "Overall, the market stall is full of fresh groceries.", "ko": "전반적으로 시장 가판대에 신선한 식료품들이 가득 차 있습니다."}
            ],
            "magicSentences": [
                {"en": "She is wearing a padded jacket and jeans.", "ko": "그녀는 패딩 재킷과 청바지를 입고 있습니다.", "tip": "시계토끼 만능 #012 (야외 겨울/환절기 복장)"},
                {"en": "She is standing and looking at the products.", "ko": "그녀는 서서 상품들을 살펴보고 있습니다.", "tip": "시계토끼 만능 #025 (쇼핑객 핵심 동작)"},
                {"en": "Various fruits and groceries are on display.", "ko": "다양한 과일과 식료품들이 진열되어 있습니다.", "tip": "시계토끼 만능 #048 (시장/마트 진열 표현)"}
            ],
            "vocabulary": [
                {"word": "padded jacket", "ipa": "[ˈpædɪd ˈdʒækɪt]", "pos": "명사", "meaning": "패딩 점퍼/재킷"},
                {"word": "vendor", "ipa": "[ˈvendər]", "pos": "명사", "meaning": "노점 상인, 판매원"},
                {"word": "on display", "ipa": "[ɑːn dɪˈspleɪ]", "pos": "숙어", "meaning": "진열되어 있는"},
                {"word": "groceries", "ipa": "[ˈɡroʊsəriz]", "pos": "명사", "meaning": "식료품, 청과물"}
            ],
            "explanation": "마트·시장 사진에서 구체적인 과일/채소 이름이 기억나지 않을 때는 상위 개념어인 'fresh fruits and groceries are on display'로 통칭하면 막힘없이 답변할 수 있습니다."
        }
    ]
    for item in items:
        item["imageBase64"] = encode_image_base64(item["imageRelPath"])
    return items


def build_part3():
    """Part 3: 5개 유형 × 5문제씩 = 총 25문제 (2025~2026 최신 기출)"""
    return [
        # =====================================================================
        # 유형 1: 시점·최근 경험 (When was the last time / Past Experience) - 5문항
        # =====================================================================
        {
            "id": "p3-01",
            "part": 3,
            "qNum": "Part 3 - #01 (Q5)",
            "typeId": "p3-t1",
            "typeName": "유형 1: 시점·최근 경험 (When / Past)",
            "typeBadge": "유형 1 · 시점·최근 경험",
            "topic": "근처 공원 방문 경험 (Neighborhood Park)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you visited a park in your neighborhood, and what did you do there?",
            "questionKo": "동네 공원에 마지막으로 방문한 것이 언제였고, 거기서 무엇을 했나요?",
            "sentences": [
                {"step": "1. 과거 시점 제시", "en": "The last time I visited a park in my neighborhood was last weekend.", "ko": "제가 동네 공원에 마지막으로 방문한 것은 지난 주말이었습니다."},
                {"step": "2. 구체적 행동", "en": "I went there with my best friend to take a walk and get some fresh air.", "ko": "저는 산책을 하고 상쾌한 공기를 마시기 위해 가장 친한 친구와 그곳에 갔습니다."},
                {"step": "3. 부연 마무리", "en": "We also drank iced coffee on a bench and had a great time.", "ko": "저희는 벤치에서 아이스 커피도 마시며 즐거운 시간을 보냈습니다."}
            ],
            "magicSentences": [
                {"en": "The last time I visited a park was last weekend.", "ko": "마지막으로 공원에 간 것은 지난 주말이었습니다.", "tip": "When was the last time~ 질문은 주어+was last weekend로 바로 받아치기"},
                {"en": "I went there to take a walk and get some fresh air.", "ko": "산책을 하고 맑은 공기를 마시기 위해 거기에 갔습니다.", "tip": "시계토끼 만능 #051 (스트레스 해소·산책 만능 이유)"}
            ],
            "vocabulary": [
                {"word": "neighborhood", "ipa": "[ˈneɪbərhʊd]", "pos": "명사", "meaning": "동네, 인근 지역"},
                {"word": "take a walk", "ipa": "[teɪk ə wɔːk]", "pos": "숙어", "meaning": "산책하다"},
                {"word": "get some fresh air", "ipa": "[ɡet sʌm freʃ er]", "pos": "숙어", "meaning": "상쾌한 공기를 마시다"}
            ],
            "explanation": "질문의 'When was the last time you visited~'를 그대로 'The last time I visited ~ was last weekend'로 받아치면 문법 실수 없이 첫 문장을 2초 만에 시작할 수 있습니다."
        },
        {
            "id": "p3-02",
            "part": 3,
            "qNum": "Part 3 - #02 (Q5)",
            "typeId": "p3-t1",
            "typeName": "유형 1: 시점·최근 경험 (When / Past)",
            "typeBadge": "유형 1 · 시점·최근 경험",
            "topic": "패션 아이템·의류 최근 구매 (Fashion Accessories)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you bought a fashion item such as a bag or shoes, and where did you buy it?",
            "questionKo": "가방이나 신발 같은 패션 아이템을 마지막으로 산 것이 언제였고, 어디서 구매했나요?",
            "sentences": [
                {"step": "1. 과거 시점 제시", "en": "The last time I bought a fashion item was two weeks ago.", "ko": "제가 패션 아이템을 마지막으로 산 것은 2주 전이었습니다."},
                {"step": "2. 구매 품목 및 장소", "en": "I bought a pair of running shoes at an online shopping mall.", "ko": "저는 온라인 쇼핑몰에서 운동화 한 켤레를 구매했습니다."},
                {"step": "3. 구매 이유", "en": "I bought them there because the price was very reasonable and delivery was fast.", "ko": "가격이 매우 합리적이고 배송이 빨라서 그곳에서 구매했습니다."}
            ],
            "magicSentences": [
                {"en": "I bought it at an online shopping mall.", "ko": "저는 그것을 온라인 쇼핑몰에서 샀습니다.", "tip": "Where did you buy~ 질문의 만능 장소 답변"},
                {"en": "The price is reasonable and affordable.", "ko": "가격이 합리적이고 부담 없습니다.", "tip": "시계토끼 만능 #069 (가성비 만능문장)"}
            ],
            "vocabulary": [
                {"word": "a pair of running shoes", "ipa": "[ə per ʌv ˈrʌnɪŋ ʃuːz]", "pos": "명사구", "meaning": "운동화 한 켤레"},
                {"word": "reasonable", "ipa": "[ˈriːznəbl]", "pos": "형용사", "meaning": "(가격이) 합리적인"},
                {"word": "affordable", "ipa": "[əˈfɔːrdəbl]", "pos": "형용사", "meaning": "감당할 수 있는, 저렴한"}
            ],
            "explanation": "쇼핑 관련 과거 경험 질문에서는 무조건 'two weeks ago' + 'at an online shopping mall' + 'because the price was reasonable' 3단 공식으로 연결하세요."
        },
        {
            "id": "p3-03",
            "part": 3,
            "qNum": "Part 3 - #03 (Q5)",
            "typeId": "p3-t1",
            "typeName": "유형 1: 시점·최근 경험 (When / Past)",
            "typeBadge": "유형 1 · 시점·최근 경험",
            "topic": "대중교통 최근 이용 경험 (Public Transportation)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you used public transportation, and where did you go?",
            "questionKo": "마지막으로 대중교통을 이용한 것이 언제였고, 어디에 갔나요?",
            "sentences": [
                {"step": "1. 과거 시점 제시", "en": "The last time I used public transportation was this morning.", "ko": "제가 대중교통을 마지막으로 이용한 것은 오늘 아침이었습니다."},
                {"step": "2. 수단 및 목적지", "en": "I took the subway to go to my office in downtown Seoul.", "ko": "저는 서울 시내에 있는 사무실에 출근하기 위해 지하철을 탔습니다."},
                {"step": "3. 부연 이유", "en": "It is always on time, so I can avoid heavy traffic jams during rush hour.", "ko": "지하철은 항상 정시에 와서 출퇴근 시간대의 심한 교통 체증을 피할 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "It is always on time, so I can avoid traffic jams.", "ko": "항상 정시에 운행되어 교통 체증을 피할 수 있습니다.", "tip": "시계토끼 만능 #063 (대중교통 정시성·교통체증 회피)"},
                {"en": "I can save a lot of time during rush hour.", "ko": "출퇴근 혼잡 시간대에 시간을 많이 절약할 수 있습니다.", "tip": "시계토끼 만능 #062 (시간 절약 만능문장)"}
            ],
            "vocabulary": [
                {"word": "public transportation", "ipa": "[ˈpʌblɪk ˌtrænspərˈteɪʃn]", "pos": "명사", "meaning": "대중교통"},
                {"word": "on time", "ipa": "[ɑːn taɪm]", "pos": "숙어", "meaning": "정시에, 시간을 어기지 않고"},
                {"word": "traffic jam", "ipa": "[ˈtræfɪk dʒæm]", "pos": "명사", "meaning": "교통 체증"}
            ],
            "explanation": "대중교통 시점 질문은 'this morning' 또는 'yesterday'로 답하고, 'took the subway to go to work/school'로 이어가면 가장 자연스럽습니다."
        },
        {
            "id": "p3-04",
            "part": 3,
            "qNum": "Part 3 - #04 (Q6)",
            "typeId": "p3-t1",
            "typeName": "유형 1: 시점·최근 경험 (When / Past)",
            "typeBadge": "유형 1 · 시점·최근 경험",
            "topic": "영화관 최근 방문 및 관람작 (Movie Theater)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When was the last time you went to a movie theater, and who did you go with?",
            "questionKo": "마지막으로 영화관에 간 것이 언제였고, 누구와 함께 갔나요?",
            "sentences": [
                {"step": "1. 과거 시점 및 동행인", "en": "The last time I went to a movie theater was last Friday evening with my family.", "ko": "마지막으로 영화관에 간 것은 지난 금요일 저녁에 가족들과 함께였습니다."},
                {"step": "2. 구체적 활동", "en": "We watched a famous action movie on a large screen and ate caramel popcorn.", "ko": "저희는 대형 스크린으로 유명한 액션 영화를 보고 카라멜 팝콘을 먹었습니다."},
                {"step": "3. 소감 마무리", "en": "It was a great way to relieve stress and strengthen our family bond.", "ko": "스트레스를 해소하고 가족 간의 유대감을 다지는 좋은 방법이었습니다."}
            ],
            "magicSentences": [
                {"en": "It is a great way to relieve stress.", "ko": "스트레스를 해소하는 아주 좋은 방법입니다.", "tip": "시계토끼 만능 #051 (취미·여가 부동의 1위 만능문장)"},
                {"en": "We could strengthen our bond and make good memories.", "ko": "유대감을 강화하고 좋은 추억을 만들 수 있었습니다.", "tip": "시계토끼 만능 #083 (동행인 질문 만능 마무리)"}
            ],
            "vocabulary": [
                {"word": "relieve stress", "ipa": "[rɪˈliːv stres]", "pos": "숙어", "meaning": "스트레스를 해소하다"},
                {"word": "strengthen", "ipa": "[ˈstreŋkθn]", "pos": "동사", "meaning": "강화하다, 다지다"},
                {"word": "bond", "ipa": "[bɑːnd]", "pos": "명사", "meaning": "유대감, 결속"}
            ],
            "explanation": "영화·콘서트·공연 관련 과거 경험 질문에서는 무조건 'watched an action movie with my family/friends' + 'relieve stress' 조합을 사용하세요."
        },
        {
            "id": "p3-05",
            "part": 3,
            "qNum": "Part 3 - #05 (Q5)",
            "typeId": "p3-t1",
            "typeName": "유형 1: 시점·최근 경험 (When / Past)",
            "typeBadge": "유형 1 · 시점·최근 경험",
            "topic": "마지막 여행 시점 및 여행지 (Last Vacation)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "When did you go on your last vacation, and where did you go?",
            "questionKo": "마지막 휴가는 언제 갔고, 어디로 다녀왔나요?",
            "sentences": [
                {"step": "1. 시점 및 장소 제시", "en": "I went on my last vacation last summer, and I visited Jeju Island with my friends.", "ko": "저는 지난여름에 마지막 휴가를 갔고, 친구들과 제주도에 다녀왔습니다."},
                {"step": "2. 현지 활동 묘사", "en": "We walked along the beautiful beach, ate fresh seafood, and took a lot of pictures.", "ko": "저희는 아름다운 해변을 따라 걷고 신선한 해산물을 먹으며 사진을 많이 찍었습니다."},
                {"step": "3. 소감 마무리", "en": "Thanks to the trip, I could refresh my mind and make unforgettable memories.", "ko": "그 여행 덕분에 기분을 전환하고 잊지 못할 추억을 만들 수 있었습니다."}
            ],
            "magicSentences": [
                {"en": "I could refresh my mind and recharge my batteries.", "ko": "기분을 전환하고 재충전할 수 있었습니다.", "tip": "시계토끼 만능 #051 & #052 (여행·휴가 만능 효과)"},
                {"en": "We made unforgettable memories together.", "ko": "함께 잊지 못할 추억을 만들었습니다.", "tip": "시계토끼 만능 #083 (여행·모임 마무리 공식)"}
            ],
            "vocabulary": [
                {"word": "vacation", "ipa": "[veɪˈkeɪʃn]", "pos": "명사", "meaning": "휴가, 방학"},
                {"word": "refresh my mind", "ipa": "[rɪˈfreʃ maɪ maɪnd]", "pos": "숙어", "meaning": "기분을 전환하다, 머리를 식히다"},
                {"word": "unforgettable", "ipa": "[ˌʌnfərˈɡetəbl]", "pos": "형용사", "meaning": "잊지 못할"}
            ],
            "explanation": "국내외 여행지 질문에서는 발음하기 쉽고 활동 묘사(해변 산책, 해산물 맛집, 사진 촬영)가 풍부한 'Jeju Island'를 고정 답변으로 준비해 두면 어떤 여행 질문에도 대응할 수 있습니다."
        },

        # =====================================================================
        # 유형 2: 빈도·장소·동행인 (How often / Where & With whom) - 5문항
        # =====================================================================
        {
            "id": "p3-06",
            "part": 3,
            "qNum": "Part 3 - #06 (Q5)",
            "typeId": "p3-t2",
            "typeName": "유형 2: 빈도·장소·동행인 (How often / Where)",
            "typeBadge": "유형 2 · 빈도·일상 습관",
            "topic": "카페 방문 빈도 및 동행인 (Coffee Shop)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you visit a coffee shop, and who do you usually go with?",
            "questionKo": "카페에 얼마나 자주 방문하며, 주로 누구와 함께 가나요?",
            "sentences": [
                {"step": "1. 빈도 및 동행인", "en": "I usually visit a coffee shop three or four times a week, and I mostly go there with my coworkers.", "ko": "저는 보통 일주일에 서너 번 카페에 방문하며, 주로 직장 동료들과 함께 갑니다."},
                {"step": "2. 구체적 상황", "en": "After having lunch together, we always stop by a cafe near our office.", "ko": "함께 점심을 먹은 후에 저희는 항상 사무실 근처 카페에 들릅니다."},
                {"step": "3. 이유 및 효과", "en": "Chatting over a cup of coffee helps us relieve work stress and share useful ideas.", "ko": "커피 한 잔을 마시며 수다를 떠는 것은 업무 스트레스를 풀고 유용한 아이디어를 공유하는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "I usually go there three or four times a week with my coworkers.", "ko": "보통 일주일에 서너 번 동료들과 그곳에 갑니다.", "tip": "How often + Who 동시 해결 첫 문장"},
                {"en": "It helps us relieve stress and share useful information.", "ko": "스트레스를 풀고 유용한 정보를 공유하는 데 도움이 됩니다.", "tip": "시계토끼 만능 #051 & #082 결합"}
            ],
            "vocabulary": [
                {"word": "coworkers", "ipa": "[ˈkoʊwɜːrkərz]", "pos": "명사", "meaning": "직장 동료들"},
                {"word": "stop by", "ipa": "[stɑːp baɪ]", "pos": "숙어", "meaning": "잠시 들르다"},
                {"word": "chat over coffee", "ipa": "[tʃæt ˈoʊvər ˈkɔːfi]", "pos": "숙어", "meaning": "커피를 마시며 담소를 나누다"}
            ],
            "explanation": "How often 질문에는 'once or twice a week' 또는 'three or four times a week'를 고정 템플릿으로 쓰세요."
        },
        {
            "id": "p3-07",
            "part": 3,
            "qNum": "Part 3 - #07 (Q5)",
            "typeId": "p3-t2",
            "typeName": "유형 2: 빈도·장소·동행인 (How often / Where)",
            "typeBadge": "유형 2 · 빈도·일상 습관",
            "topic": "주로 하는 운동 종류 및 빈도 (Regular Exercise)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "What kind of exercise do you usually do, and how often do you do it?",
            "questionKo": "주로 어떤 종류의 운동을 하며, 얼마나 자주 하나요?",
            "sentences": [
                {"step": "1. 운동 종류 및 빈도", "en": "I usually go jogging at a park near my house, and I do it three times a week.", "ko": "저는 보통 집 근처 공원에서 조깅을 하며, 일주일에 세 번 합니다."},
                {"step": "2. 선택 이유 (비용/접근성)", "en": "I don't need any special equipment, so I can easily work out whenever I have free time.", "ko": "특별한 장비가 필요하지 않아서 여유 시간이 있을 때마다 쉽게 운동할 수 있습니다."},
                {"step": "3. 건강 효과", "en": "It is a great way to stay healthy and keep in shape.", "ko": "건강을 유지하고 몸매를 관리하는 아주 좋은 방법입니다."}
            ],
            "magicSentences": [
                {"en": "It is near my house, so it is very accessible.", "ko": "집 근처에 있어서 접근성이 매우 좋습니다.", "tip": "시계토끼 만능 #066 (집 근처 접근성 만능문장)"},
                {"en": "It is good for my physical and mental health.", "ko": "신체적·정신적 건강에 좋습니다.", "tip": "시계토끼 만능 #077 (운동·건강 만능문장)"}
            ],
            "vocabulary": [
                {"word": "go jogging", "ipa": "[ɡoʊ ˈdʒɑːɡɪŋ]", "pos": "숙어", "meaning": "조깅하러 가다"},
                {"word": "equipment", "ipa": "[ɪˈkwɪpmənt]", "pos": "명사", "meaning": "장비, 기구 (불가산명사)"},
                {"word": "keep in shape", "ipa": "[kiːp ɪn ʃeɪp]", "pos": "숙어", "meaning": "건강/몸매를 유지하다"}
            ],
            "explanation": "운동 질문에서는 'go jogging at a park near my house'가 만능입니다. 비용이 들지 않고(for free), 접근성이 좋으며(near my house), 건강에 좋다(stay healthy)는 3가지 이유를 모두 쓸 수 있습니다."
        },
        {
            "id": "p3-08",
            "part": 3,
            "qNum": "Part 3 - #08 (Q6)",
            "typeId": "p3-t2",
            "typeName": "유형 2: 빈도·장소·동행인 (How often / Where)",
            "typeBadge": "유형 2 · 빈도·일상 습관",
            "topic": "모바일 메신저 사용 빈도 및 대상 (Instant Messaging)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you use text messaging apps, and who do you usually message the most?",
            "questionKo": "문자 메신저 앱을 얼마나 자주 사용하며, 주로 누구에게 가장 많이 메시지를 보내나요?",
            "sentences": [
                {"step": "1. 빈도 및 대상", "en": "I use text messaging apps every single day, and I message my friends and coworkers the most.", "ko": "저는 문자 메신저 앱을 매일 사용하며, 친구들과 직장 동료들에게 가장 많이 메시지를 보냅니다."},
                {"step": "2. 구체적 활용", "en": "We share daily updates, schedule meetings, and send work files instantly.", "ko": "저희는 일상 소식을 공유하고, 회의 일정을 잡고, 업무 파일을 즉시 전송합니다."},
                {"step": "3. 장점 마무리", "en": "It is very fast and convenient to stay in touch with people anytime, anywhere.", "ko": "언제 어디서나 사람들과 연락을 유지하기에 매우 빠르고 편리합니다."}
            ],
            "magicSentences": [
                {"en": "I can use it anytime, anywhere with my smartphone.", "ko": "스마트폰으로 언제 어디서나 사용할 수 있습니다.", "tip": "시계토끼 만능 #067 (디지털·모바일 만능문장)"},
                {"en": "It is very fast and convenient to stay in touch.", "ko": "연락을 주고받기에 매우 빠르고 편리합니다.", "tip": "시계토끼 만능 #064 (편리성 만능문장)"}
            ],
            "vocabulary": [
                {"word": "instantly", "ipa": "[ˈɪnstəntli]", "pos": "부사", "meaning": "즉시, 즉각적으로"},
                {"word": "stay in touch", "ipa": "[steɪ ɪn tʌtʃ]", "pos": "숙어", "meaning": "연락을 유지하다"},
                {"word": "anytime, anywhere", "ipa": "[ˈenitaɪm ˈeniwer]", "pos": "부사구", "meaning": "언제 어디서나"}
            ],
            "explanation": "스마트폰·앱·인터넷 사용 빈도는 'every single day (하루도 빠짐없이 매일)'로 답하고 'anytime, anywhere with my smartphone' 공식을 붙이면 자연스럽습니다."
        },
        {
            "id": "p3-09",
            "part": 3,
            "qNum": "Part 3 - #09 (Q5)",
            "typeId": "p3-t2",
            "typeName": "유형 2: 빈도·장소·동행인 (How often / Where)",
            "typeBadge": "유형 2 · 빈도·일상 습관",
            "topic": "책·전자책 독서 빈도 및 장소 (Reading Books)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you read books, and where do you usually like to read?",
            "questionKo": "책을 얼마나 자주 읽으며, 주로 어디서 읽는 것을 좋아하나요?",
            "sentences": [
                {"step": "1. 빈도 및 장소", "en": "I read books about twice a week, and I usually like to read in my bedroom at home.", "ko": "저는 일주일에 두 번 정도 책을 읽으며, 주로 집 침실에서 읽는 것을 좋아합니다."},
                {"step": "2. 장소 선택 이유", "en": "My room is very quiet and cozy, so I am not interrupted by anyone.", "ko": "제 방은 매우 조용하고 아늑해서 누구에게도 방해받지 않습니다."},
                {"step": "3. 효과 마무리", "en": "Therefore, I can focus better on the book and broaden my horizons.", "ko": "따라서 책에 더 잘 집중할 수 있고 식견을 넓힐 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "It is quiet and cozy, so I am not interrupted by anyone.", "ko": "조용하고 아늑해서 누구에게도 방해받지 않습니다.", "tip": "시계토끼 만능 #055 & #058 (집·독서실 선호 이유)"},
                {"en": "I can focus better and broaden my horizons.", "ko": "더 잘 집중할 수 있고 식견을 넓힐 수 있습니다.", "tip": "시계토끼 만능 #057 & #086 결합"}
            ],
            "vocabulary": [
                {"word": "cozy", "ipa": "[ˈkoʊzi]", "pos": "형용사", "meaning": "아늑한, 편안한"},
                {"word": "interrupted", "ipa": "[ˌɪntəˈrʌptɪd]", "pos": "분사", "meaning": "방해받는"},
                {"word": "broaden my horizons", "ipa": "[ˈbrɔːdn maɪ həˈraɪznz]", "pos": "숙어", "meaning": "식견(시야)을 넓히다"}
            ],
            "explanation": "Where do you usually~ 질문에서 가장 만능인 장소는 'at home (in my bedroom)'입니다. 조용하고(quiet), 방해받지 않으며(not interrupted), 집중이 잘 된다(focus better)는 3단 콤보를 그대로 쓸 수 있기 때문입니다."
        },
        {
            "id": "p3-10",
            "part": 3,
            "qNum": "Part 3 - #10 (Q5)",
            "typeId": "p3-t2",
            "typeName": "유형 2: 빈도·장소·동행인 (How often / Where)",
            "typeBadge": "유형 2 · 빈도·일상 습관",
            "topic": "식료품 쇼핑 빈도 및 선호 매장 (Grocery Shopping)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "How often do you go grocery shopping, and where do you usually buy your groceries?",
            "questionKo": "식료품 쇼핑을 얼마나 자주 가며, 주로 어디서 식료품을 구매하나요?",
            "sentences": [
                {"step": "1. 빈도 및 장소", "en": "I usually go grocery shopping once a week on weekends, and I buy groceries at a large supermarket near my house.", "ko": "저는 보통 주말마다 일주일에 한 번 식료품 쇼핑을 가며, 집 근처 대형 마트에서 식료품을 구매합니다."},
                {"step": "2. 이유 1 (다양성/신선도)", "en": "They have a wide variety of fresh fruits, vegetables, and daily necessities in one place.", "ko": "그곳에는 다양한 신선한 과일, 채소, 그리고 생필품이 한곳에 모여 있습니다."},
                {"step": "3. 이유 2 (할인 혜택)", "en": "Also, they offer many discount promotions, so I can save money.", "ko": "또한 할인 행사를 많이 진행해서 돈을 절약할 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "They have a wide variety of products in one place.", "ko": "한곳에 매우 다양한 상품들을 갖추고 있습니다.", "tip": "시계토끼 만능 #093 (다양한 선택지 만능문장)"},
                {"en": "They offer many discounts and promotions, so I can save money.", "ko": "많은 할인과 프로모션을 제공해서 돈을 아낄 수 있습니다.", "tip": "시계토끼 만능 #068 & #071 결합"}
            ],
            "vocabulary": [
                {"word": "grocery shopping", "ipa": "[ˈɡroʊsəri ˈʃɑːpɪŋ]", "pos": "명사", "meaning": "식료품 쇼핑, 장보기"},
                {"word": "a wide variety of", "ipa": "[ə waɪd vəˈraɪəti ʌv]", "pos": "숙어", "meaning": "매우 다양한 ~"},
                {"word": "daily necessities", "ipa": "[ˈdeɪli nəˈsesətiz]", "pos": "명사", "meaning": "생필품"}
            ],
            "explanation": "대형 마트나 온라인 몰을 선택했을 때는 'a wide variety of products(다양한 상품)'와 'discount promotions(할인 행사)' 두 가지를 핵심 이유로 제시하세요."
        },

        # =====================================================================
        # 유형 3: 양자택일 선호도·찬반 (Prefer A or B / Yes or No) - 5문항
        # =====================================================================
        {
            "id": "p3-11",
            "part": 3,
            "qNum": "Part 3 - #11 (Q6)",
            "typeId": "p3-t3",
            "typeName": "유형 3: 양자택일 선호도·찬반 (Prefer A or B)",
            "typeBadge": "유형 3 · 선호도·찬반",
            "topic": "공원 내 소규모 상점 입점 찬반 (Small Shops in Parks)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you think it is a good idea to have small shops that sell snacks and drinks inside a park? Why or why not?",
            "questionKo": "공원 안에 간식과 음료를 파는 작은 상점들이 있는 것이 좋은 생각이라고 보시나요? 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 찬성 입장 표명", "en": "Yes, I definitely think it is a great idea to have small shops inside a park.", "ko": "네, 공원 안에 작은 상점들이 있는 것은 정말 좋은 생각이라고 생각합니다."},
                {"step": "2. 이유 1 (편리성)", "en": "First, it is very convenient for visitors because they don't have to bring heavy bags from home.", "ko": "첫째, 방문객들이 집에서 무거운 가방을 챙겨 오지 않아도 되므로 매우 편리합니다."},
                {"step": "3. 이유 2 (즉각적 필요)", "en": "Second, people can easily buy cold water or snacks whenever they get thirsty after exercising.", "ko": "둘째, 사람들이 운동 후 목이 마를 때마다 시원한 물이나 간식을 쉽게 사 먹을 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "It is very convenient and saves a lot of time.", "ko": "매우 편리하고 시간을 많이 절약해 줍니다.", "tip": "시계토끼 만능 #062 & #064 (편의시설 찬성 공식)"},
                {"en": "Visitors don't have to bring heavy items from home.", "ko": "방문객들이 집에서 무거운 물건을 가져올 필요가 없습니다.", "tip": "공원·관광지 대여점/매점 찬성 핵심 논리"}
            ],
            "vocabulary": [
                {"word": "definitely", "ipa": "[ˈdefɪnətli]", "pos": "부사", "meaning": "분명히, 확실히"},
                {"word": "convenient", "ipa": "[kənˈviːniənt]", "pos": "형용사", "meaning": "편리한"},
                {"word": "thirsty", "ipa": "[ˈθɜːrsti]", "pos": "형용사", "meaning": "목이 마른, 갈증 나는"}
            ],
            "explanation": "2026년 최신 기출 문제입니다. 시설 설치 찬반(Do you think it is a good idea~?) 질문은 무조건 Yes로 답하고 'It is very convenient for visitors'로 풀어가면 막힘이 없습니다."
        },
        {
            "id": "p3-12",
            "part": 3,
            "qNum": "Part 3 - #12 (Q6)",
            "typeId": "p3-t3",
            "typeName": "유형 3: 양자택일 선호도·찬반 (Prefer A or B)",
            "typeBadge": "유형 3 · 선호도·찬반",
            "topic": "패션 아이템 구매 시 온라인 vs 오프라인 매장 (Online vs. In-store)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer buying fashion accessories online or at an offline store? Why?",
            "questionKo": "패션 잡화를 온라인으로 사는 것과 오프라인 매장에서 사는 것 중 어느 쪽을 선호하나요? 왜 그런가요?",
            "sentences": [
                {"step": "1. 선호 대상 선택", "en": "I definitely prefer buying fashion accessories at an offline store rather than online.", "ko": "저는 패션 잡화를 온라인보다 오프라인 매장에서 구매하는 것을 확실히 선호합니다."},
                {"step": "2. 이유 1 (직접 착용)", "en": "At a physical store, I can try on the items in person and check the exact size and color.", "ko": "실제 매장에서는 제품을 직접 착용해 보고 정확한 사이즈와 색상을 확인할 수 있습니다."},
                {"step": "3. 이유 2 (실패 방지)", "en": "Also, I can ask the store clerk for recommendations and avoid the hassle of returning items.", "ko": "또한 매장 직원에게 추천을 받을 수 있고 반품하는 번거로움을 피할 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "I can check the quality and size in person before buying.", "ko": "구매 전에 직접 품질과 사이즈를 확인할 수 있습니다.", "tip": "오프라인 쇼핑 선택 시 만능 이유"},
                {"en": "I can avoid the hassle of exchanging or returning items.", "ko": "교환이나 반품을 하는 번거로움을 피할 수 있습니다.", "tip": "의류·잡화 오프라인 구매 고득점 표현"}
            ],
            "vocabulary": [
                {"word": "in person", "ipa": "[ɪn ˈpɜːrsn]", "pos": "숙어", "meaning": "직접, 몸소"},
                {"word": "physical store", "ipa": "[ˈfɪzɪkl stɔːr]", "pos": "명사", "meaning": "오프라인 실제 매장"},
                {"word": "hassle", "ipa": "[ˈhæsl]", "pos": "명사", "meaning": "번거로움, 귀찮은 일"}
            ],
            "explanation": "의류·신발·안경 등 착용이 필요한 품목은 오프라인 매장(try them on in person, check the exact size)을 선택하는 것이 할 말이 훨씬 많습니다."
        },
        {
            "id": "p3-13",
            "part": 3,
            "qNum": "Part 3 - #13 (Q6)",
            "typeId": "p3-t3",
            "typeName": "유형 3: 양자택일 선호도·찬반 (Prefer A or B)",
            "typeBadge": "유형 3 · 선호도·찬반",
            "topic": "자가용 운전 vs 대중교통 이용 선호도 (Driving vs. Public Transit)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer driving your own car or taking public transportation when commuting? Why?",
            "questionKo": "통근할 때 자가용 운전과 대중교통 이용 중 어느 쪽을 선호하나요? 이유는 무엇인가요?",
            "sentences": [
                {"step": "1. 선호 선택", "en": "I prefer taking public transportation rather than driving my own car when commuting.", "ko": "저는 통근할 때 자가용을 운전하는 것보다 대중교통을 이용하는 것을 선호합니다."},
                {"step": "2. 이유 1 (비용 절감)", "en": "First of all, the subway fare is much cheaper than paying for gas and parking fees.", "ko": "무엇보다도 지하철 요금이 주유비와 주차비를 내는 것보다 훨씬 저렴합니다."},
                {"step": "3. 이유 2 (시간 활용)", "en": "In addition, I don't have to worry about traffic jams, and I can read news on my phone while moving.", "ko": "게다가 교통 체증을 걱정할 필요가 없고 이동하면서 스마트폰으로 뉴스를 읽을 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "It is much cheaper, so I can save money on gas and parking fees.", "ko": "훨씬 저렴해서 주유비와 주차비를 절약할 수 있습니다.", "tip": "시계토끼 만능 #068 & #073 (비용 절감)"},
                {"en": "I don't have to worry about traffic jams during rush hour.", "ko": "출퇴근 시간에 교통 체증을 걱정할 필요가 없습니다.", "tip": "시계토끼 만능 #063 (대중교통 핵심 장점)"}
            ],
            "vocabulary": [
                {"word": "commuting", "ipa": "[kəˈmjuːtɪŋ]", "pos": "동명사", "meaning": "통근, 출퇴근"},
                {"word": "fare", "ipa": "[fer]", "pos": "명사", "meaning": "(대중교통) 요금"},
                {"word": "parking fee", "ipa": "[ˈpɑːrkɪŋ fiː]", "pos": "명사", "meaning": "주차 요금"}
            ],
            "explanation": "교통수단 양자택일에서는 대중교통(public transportation)을 선택하면 비용 절약(save money on gas and parking)과 정시성(avoid traffic jams) 두 가지 만능문장을 동시에 쓸 수 있습니다."
        },
        {
            "id": "p3-14",
            "part": 3,
            "qNum": "Part 3 - #14 (Q6)",
            "typeId": "p3-t3",
            "typeName": "유형 3: 양자택일 선호도·찬반 (Prefer A or B)",
            "typeBadge": "유형 3 · 선호도·찬반",
            "topic": "혼자 운동하기 vs 다른 사람들과 함께 운동하기 (Exercising Alone vs. Together)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer exercising alone or exercising with other people? Why?",
            "questionKo": "혼자 운동하는 것과 다른 사람들과 함께 운동하는 것 중 어느 쪽을 선호하나요? 왜 그런가요?",
            "sentences": [
                {"step": "1. 선호 선택", "en": "I prefer exercising with other people rather than exercising alone.", "ko": "저는 혼자 운동하는 것보다 다른 사람들과 함께 운동하는 것을 선호합니다."},
                {"step": "2. 이유 1 (동기부여)", "en": "When I work out with my friends, we can encourage and motivate each other not to give up.", "ko": "친구들과 함께 운동하면 서로 포기하지 않도록 격려하고 동기부여를 해줄 수 있습니다."},
                {"step": "3. 이유 2 (재미/지속성)", "en": "Also, it is much more fun and less boring, so I can exercise consistently.", "ko": "또한 훨씬 더 재미있고 덜 지루해서 꾸준히 운동할 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "We can motivate each other to achieve our goals.", "ko": "목표를 달성하도록 서로에게 동기부여를 해줄 수 있습니다.", "tip": "시계토끼 만능 #084 (함께하기 선택 시 1순위 문장)"},
                {"en": "It is much more fun and less boring than doing it alone.", "ko": "혼자 하는 것보다 훨씬 더 재미있고 덜 지루합니다.", "tip": "동행 선호 만능 비교 구문"}
            ],
            "vocabulary": [
                {"word": "motivate each other", "ipa": "[ˈmoʊtɪveɪt iːtʃ ˈʌðər]", "pos": "숙어", "meaning": "서로에게 동기를 부여하다"},
                {"word": "encourage", "ipa": "[ɪnˈkɜːrɪdʒ]", "pos": "동사", "meaning": "격려하다, 북돋우다"},
                {"word": "consistently", "ipa": "[kənˈsɪstəntli]", "pos": "부사", "meaning": "꾸준히, 일관되게"}
            ],
            "explanation": "혼자 vs 함께(alone vs. with others) 질문은 운동·공부·여행 어디에서 나오든 'motivate each other(서로 동기부여)'와 'much more fun(더 재미있음)' 두 문장으로 해결됩니다."
        },
        {
            "id": "p3-15",
            "part": 3,
            "qNum": "Part 3 - #15 (Q6)",
            "typeId": "p3-t3",
            "typeName": "유형 3: 양자택일 선호도·찬반 (Prefer A or B)",
            "typeBadge": "유형 3 · 선호도·찬반",
            "topic": "집에서 공부/업무 vs 카페에서 공부/업무 (At Home vs. At a Cafe)",
            "prepTime": 3,
            "responseTime": 15,
            "question": "Do you prefer studying or working at home or at a coffee shop? Why?",
            "questionKo": "집에서 공부하거나 일하는 것과 카페에서 하는 것 중 어느 쪽을 선호하나요? 왜 그런가요?",
            "sentences": [
                {"step": "1. 선호 선택", "en": "I definitely prefer working at home rather than at a coffee shop.", "ko": "저는 카페보다 집에서 일하는 것을 확실히 선호합니다."},
                {"step": "2. 이유 1 (집중력)", "en": "First, my room is very quiet and comfortable, so I am not distracted by noise.", "ko": "첫째, 제 방은 매우 조용하고 편안해서 소음에 방해받지 않습니다."},
                {"step": "3. 이유 2 (시간·비용 절약)", "en": "Second, I don't have to spend time getting dressed or spend money on expensive drinks.", "ko": "둘째, 옷을 차려입는 데 시간을 쓰거나 비싼 음료에 돈을 쓸 필요가 없습니다."}
            ],
            "magicSentences": [
                {"en": "It is quiet and comfortable, so I can focus better on my work.", "ko": "조용하고 편안해서 업무에 더 잘 집중할 수 있습니다.", "tip": "시계토끼 만능 #055 & #057 결합"},
                {"en": "I don't have to waste time getting ready to go out.", "ko": "외출 준비를 하느라 시간을 낭비할 필요가 없습니다.", "tip": "시계토끼 만능 #060 (재택 선호 핵심 이유)"}
            ],
            "vocabulary": [
                {"word": "distracted", "ipa": "[dɪˈstræktɪd]", "pos": "분사/형용사", "meaning": "산만해진, 방해받는"},
                {"word": "get dressed", "ipa": "[ɡet drest]", "pos": "숙어", "meaning": "옷을 차려입다"},
                {"word": "focus on", "ipa": "[ˈfoʊkəs ɑːn]", "pos": "숙어", "meaning": "~에 집중하다"}
            ],
            "explanation": "집(At home) vs 외부 장소 비교 질문에서는 집을 선택하면 '조용해서 집중이 잘 됨(quiet -> focus better)' + '외출 준비 시간과 비용 절약(save time and money)' 논리를 그대로 쓸 수 있어 매우 유리합니다."
        },

        # =====================================================================
        # 유형 4: 3자택일 최적 선택 (3 Options Choice - Q7 30초) - 5문항
        # =====================================================================
        {
            "id": "p3-16",
            "part": 3,
            "qNum": "Part 3 - #16 (Q7)",
            "typeId": "p3-t4",
            "typeName": "유형 4: 3자택일 최적 선택 (3 Options - Q7)",
            "typeBadge": "유형 4 · 3자택일 (30초)",
            "topic": "패션 아이템 구매 시 가장 중요한 고려 요소 (Fashion Item Factor)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "Which of the following is the most important factor when buying a fashion item: brand reputation, price, or design? Why?",
            "questionKo": "패션 아이템을 구매할 때 다음 중 가장 중요한 요소는 무엇인가요? (브랜드 인지도 / 가격 / 디자인)",
            "sentences": [
                {"step": "1. 핵심 선택 제시", "en": "Among the three options, I think design is the most important factor when buying a fashion item.", "ko": "세 가지 선택지 중에서 저는 패션 아이템을 살 때 디자인이 가장 중요한 요소라고 생각합니다."},
                {"step": "2. 이유 1 (개성 표현)", "en": "First of all, fashion is a great way to express my personality and make a good first impression.", "ko": "무엇보다도 패션은 저의 개성을 표현하고 좋은 첫인상을 남기는 훌륭한 방법입니다."},
                {"step": "3. 이유 2 (실용적 활용도)", "en": "Even if an item is cheap or from a famous brand, I will never wear it if I don't like the design.", "ko": "아무리 가격이 저렴하거나 유명 브랜드 제품이라도 디자인이 마음에 들지 않으면 절대 착용하지 않게 됩니다."},
                {"step": "4. 결론 재강조", "en": "However, if the design goes well with my style, I can wear it for a long time with satisfaction. That's why design is my top priority.", "ko": "반면 디자인이 제 스타일과 잘 어울리면 오랫동안 만족하며 착용할 수 있습니다. 그것이 디자인이 제 최우선 순위인 이유입니다."}
            ],
            "magicSentences": [
                {"en": "Among the three options, I think design is the most important factor.", "ko": "세 가지 선택지 중 디자인이 가장 중요한 요소라고 생각합니다.", "tip": "Q7 3자택일 오프닝 고정 공식"},
                {"en": "If it goes well with my style, I can use it for a long time.", "ko": "제 스타일과 잘 어울리면 오랫동안 사용할 수 있습니다.", "tip": "디자인 선택 시 30초 분량 확보 문장"}
            ],
            "vocabulary": [
                {"word": "brand reputation", "ipa": "[brænd ˌrepjuˈteɪʃn]", "pos": "명사", "meaning": "브랜드 평판, 인지도"},
                {"word": "first impression", "ipa": "[fɜːrst ɪmˈpreʃn]", "pos": "명사", "meaning": "첫인상"},
                {"word": "top priority", "ipa": "[tɑːp praɪˈɔːrəti]", "pos": "명사", "meaning": "최우선 순위"}
            ],
            "explanation": "2026년 11월 기출 Q7(30초) 문제입니다. '디자인' 또는 '가격' 중 하나를 골라 1) 긍정적 이유 + 2) 반대 가정(Even if it is cheap...) + 3) 결론(That's why...) 구조로 말하면 30초를 꽉 채울 수 있습니다."
        },
        {
            "id": "p3-17",
            "part": 3,
            "qNum": "Part 3 - #17 (Q7)",
            "typeId": "p3-t4",
            "typeName": "유형 4: 3자택일 최적 선택 (3 Options - Q7)",
            "typeBadge": "유형 4 · 3자택일 (30초)",
            "topic": "취미 강좌 수강 시 가장 선호하는 방식 (Learning a New Hobby)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "If you were to learn a new hobby, which of the following would you prefer: taking an online class, joining a group club, or taking private lessons? Why?",
            "questionKo": "새로운 취미를 배운다면 다음 중 어느 방식을 선호하나요? (온라인 강의 수강 / 동호회 가입 / 1:1 개인 레슨)",
            "sentences": [
                {"step": "1. 핵심 선택 제시", "en": "Among the three options, I would definitely prefer taking an online class to learn a new hobby.", "ko": "세 가지 선택지 중에서 저는 새로운 취미를 배울 때 온라인 강의를 듣는 것을 확실히 선호합니다."},
                {"step": "2. 이유 1 (시공간 자유)", "en": "First, since I have a busy schedule, I can watch the lecture videos anytime, anywhere with my smartphone.", "ko": "첫째, 저는 일정이 바쁘기 때문에 스마트폰으로 언제 어디서나 강의 영상을 시청할 수 있습니다."},
                {"step": "3. 이유 2 (시간·비용 절약)", "en": "Second, I don't have to waste commuting time, and the tuition fee is much more affordable than private lessons.", "ko": "둘째, 이동 시간을 낭비할 필요가 없고 수강료가 개인 레슨보다 훨씬 저렴합니다."},
                {"step": "4. 부연 및 결론", "en": "Plus, I can replay difficult parts as many times as I want. For these reasons, online classes are the best choice for me.", "ko": "게다가 어려운 부분은 원하는 만큼 반복 재생할 수 있습니다. 이러한 이유로 온라인 강의가 저에게 최고의 선택입니다."}
            ],
            "magicSentences": [
                {"en": "I can take the class anytime, anywhere with my smartphone.", "ko": "스마트폰으로 언제 어디서나 수업을 들을 수 있습니다.", "tip": "시계토끼 만능 #067 (온라인 강의 1순위 장점)"},
                {"en": "The tuition fee is much more affordable, so I can save money.", "ko": "수강료가 훨씬 저렴해서 돈을 절약할 수 있습니다.", "tip": "시계토끼 만능 #068 & #069 결합"}
            ],
            "vocabulary": [
                {"word": "private lessons", "ipa": "[ˈpraɪvət ˈlesnz]", "pos": "명사", "meaning": "1:1 개인 교습, 과외"},
                {"word": "tuition fee", "ipa": "[tuˈɪʃn fiː]", "pos": "명사", "meaning": "수강료, 수업료"},
                {"word": "replay", "ipa": "[ˌriːˈpleɪ]", "pos": "동사", "meaning": "반복 재생하다, 다시 보다"}
            ],
            "explanation": "교육/강좌 방식 3자택일에서는 '온라인 강의(taking an online class)'를 고르면 시공간의 자유(anytime, anywhere), 이동 시간 절약(save commuting time), 저렴한 수강료(affordable tuition), 반복 재생(replay)까지 4가지 이유가 자동으로 따라옵니다."
        },
        {
            "id": "p3-18",
            "part": 3,
            "qNum": "Part 3 - #18 (Q7)",
            "typeId": "p3-t4",
            "typeName": "유형 4: 3자택일 최적 선택 (3 Options - Q7)",
            "typeBadge": "유형 4 · 3자택일 (30초)",
            "topic": "온라인 쇼핑 시 가장 중요한 요소 (Online Shopping Factor)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "Which of the following is the most important factor when you shop online: fast delivery, low price, or customer reviews?",
            "questionKo": "온라인 쇼핑을 할 때 다음 중 가장 중요한 요소는 무엇인가요? (빠른 배송 / 저렴한 가격 / 고객 리뷰)",
            "sentences": [
                {"step": "1. 핵심 선택 제시", "en": "Among the three factors, I believe customer reviews are the most important when shopping online.", "ko": "세 가지 요소 중 저는 온라인 쇼핑을 할 때 고객 리뷰가 가장 중요하다고 생각합니다."},
                {"step": "2. 이유 1 (직접 확인 불가 보완)", "en": "First, since I cannot see or touch the product in person online, it is hard to judge the actual quality.", "ko": "첫째, 온라인에서는 상품을 직접 보거나 만져볼 수 없기 때문에 실제 품질을 판단하기 어렵습니다."},
                {"step": "3. 이유 2 (실구매자 정보)", "en": "However, by reading honest reviews and looking at real photos from other buyers, I can avoid buying defective items.", "ko": "하지만 다른 구매자들의 솔직한 후기와 실제 사진을 확인함으로써 불량품을 구매하는 일을 피할 수 있습니다."},
                {"step": "4. 결론 마무리", "en": "Therefore, checking customer reviews helps me make a smart purchasing decision without regret.", "ko": "따라서 고객 리뷰를 확인하는 것은 후회 없이 현명한 구매 결정을 내리는 데 도움이 됩니다."}
            ],
            "magicSentences": [
                {"en": "I can get a lot of useful information from other buyers.", "ko": "다른 구매자들로부터 유용한 정보를 많이 얻을 수 있습니다.", "tip": "시계토끼 만능 #089 (정보 획득 만능문장)"},
                {"en": "It helps me make a smart decision without regret.", "ko": "후회 없이 현명한 결정을 내리는 데 도움이 됩니다.", "tip": "리뷰/추천 선택 시 30초 마무리 문장"}
            ],
            "vocabulary": [
                {"word": "customer reviews", "ipa": "[ˈkʌstəmər rɪˈvjuːz]", "pos": "명사", "meaning": "고객 후기, 리뷰"},
                {"word": "in person", "ipa": "[ɪn ˈpɜːrsn]", "pos": "숙어", "meaning": "직접, 실물로"},
                {"word": "purchasing decision", "ipa": "[ˈpɜːrtʃəsɪŋ dɪˈsɪʒn]", "pos": "명사", "meaning": "구매 결정"}
            ],
            "explanation": "온라인 쇼핑 3자택일에서는 'customer reviews(고객 리뷰)' 또는 'low price(저렴한 가격)' 중 본인이 입에 잘 붙는 하나를 정해두세요."
        },
        {
            "id": "p3-19",
            "part": 3,
            "qNum": "Part 3 - #19 (Q7)",
            "typeId": "p3-t4",
            "typeName": "유형 4: 3자택일 최적 선택 (3 Options - Q7)",
            "typeBadge": "유형 4 · 3자택일 (30초)",
            "topic": "카페 선택 시 가장 중요하게 보는 기준 (Choosing a Coffee Shop)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "What is the most important thing you consider when choosing a coffee shop to visit: location, atmosphere, or variety of drinks?",
            "questionKo": "방문할 카페를 고를 때 가장 중요하게 고려하는 것은 무엇인가요? (위치 / 분위기 / 음료의 다양성)",
            "sentences": [
                {"step": "1. 핵심 선택 제시", "en": "When choosing a coffee shop to visit, the most important factor I consider is location.", "ko": "방문할 카페를 고를 때 제가 가장 중요하게 고려하는 요소는 위치입니다."},
                {"step": "2. 이유 1 (시간 절약)", "en": "First of all, I have a very busy schedule on weekdays, so I don't want to waste time traveling far.", "ko": "무엇보다도 저는 평일에 일정이 매우 바빠서 멀리 이동하느라 시간을 낭비하고 싶지 않습니다."},
                {"step": "3. 이유 2 (접근성)", "en": "If a coffee shop is located near my house or office, it is very accessible and convenient to drop by anytime.", "ko": "카페가 집이나 사무실 근처에 위치해 있으면 접근성이 매우 좋고 언제든 들르기 편리합니다."},
                {"step": "4. 결론 마무리", "en": "Even if a cafe has a nice atmosphere, I won't go there often if it is too far away. That's why location matters the most.", "ko": "아무리 분위기가 좋은 카페라도 너무 멀리 있으면 자주 가지 않게 됩니다. 그것이 위치가 가장 중요한 이유입니다."}
            ],
            "magicSentences": [
                {"en": "It is near my house or office, so it is very accessible.", "ko": "집이나 사무실 근처여서 접근성이 매우 좋습니다.", "tip": "시계토끼 만능 #066 (위치 선택 시 1순위 만능문장)"},
                {"en": "I have a busy schedule, so I can save a lot of time.", "ko": "일정이 바빠서 시간을 많이 절약할 수 있습니다.", "tip": "시계토끼 만능 #061 & #062 결합"}
            ],
            "vocabulary": [
                {"word": "accessible", "ipa": "[əkˈsesəbl]", "pos": "형용사", "meaning": "접근하기 쉬운"},
                {"word": "drop by", "ipa": "[drɑːp baɪ]", "pos": "숙어", "meaning": "잠깐 들르다"},
                {"word": "atmosphere", "ipa": "[ˈætməsfɪr]", "pos": "명사", "meaning": "분위기"}
            ],
            "explanation": "보기 중에 'location(위치)'이 있으면 무조건 위치를 고르세요! 'near my house/office' + 'accessible' + 'save time because I have a busy schedule' 만능 공식이 100% 들어맞습니다."
        },
        {
            "id": "p3-20",
            "part": 3,
            "qNum": "Part 3 - #20 (Q7)",
            "typeId": "p3-t4",
            "typeName": "유형 4: 3자택일 최적 선택 (3 Options - Q7)",
            "typeBadge": "유형 4 · 3자택일 (30초)",
            "topic": "휴가지 선정 시 가장 중요한 요소 (Vacation Destination Factor)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "What is the most important factor when choosing a vacation destination: travel cost, tourist attractions, or delicious local food?",
            "questionKo": "휴가 여행지를 고를 때 가장 중요한 요소는 무엇인가요? (여행 비용 / 관광 명소 / 맛있는 현지 음식)",
            "sentences": [
                {"step": "1. 핵심 선택 제시", "en": "When choosing a vacation destination, I think delicious local food is the most important factor.", "ko": "휴가 여행지를 고를 때 저는 맛있는 현지 음식이 가장 중요한 요소라고 생각합니다."},
                {"step": "2. 이유 1 (개인 성향/스트레스 해소)", "en": "First, I am a big fan of trying new dishes, and eating delicious food is the best way for me to relieve stress.", "ko": "첫째, 저는 새로운 음식을 맛보는 것을 무척 좋아하며, 맛있는 음식을 먹는 것이 저에게 최고의 스트레스 해소법입니다."},
                {"step": "3. 이유 2 (현지 문화 체험)", "en": "Second, by enjoying traditional local cuisine, I can experience the unique culture of the region.", "ko": "둘째, 전통 현지 요리를 즐김으로써 그 지역의 독특한 문화를 생생하게 경험할 수 있습니다."},
                {"step": "4. 결론 마무리", "en": "Also, I can take great food photos and make unforgettable memories with my companions. That's why food is my top priority.", "ko": "또한 멋진 음식 사진을 찍고 동행인들과 잊지 못할 추억을 만들 수 있습니다. 그것이 음식이 제 최우선 순위인 이유입니다."}
            ],
            "magicSentences": [
                {"en": "Eating delicious food is the best way to relieve stress.", "ko": "맛있는 음식을 먹는 것은 스트레스를 푸는 최고의 방법입니다.", "tip": "시계토끼 만능 #051 응용"},
                {"en": "I can experience the unique culture and make good memories.", "ko": "독특한 문화를 경험하고 좋은 추억을 만들 수 있습니다.", "tip": "시계토끼 만능 #083 & #086 결합"}
            ],
            "vocabulary": [
                {"word": "destination", "ipa": "[ˌdestɪˈneɪʃn]", "pos": "명사", "meaning": "여행지, 목적지"},
                {"word": "local cuisine", "ipa": "[ˈloʊkl kwɪˈziːn]", "pos": "명사", "meaning": "현지 요리, 향토 음식"},
                {"word": "companions", "ipa": "[kəmˈpænjənz]", "pos": "명사", "meaning": "동행인, 일행"}
            ],
            "explanation": "여행지 선택 3자택일에서는 'delicious local food(맛있는 현지 음식)' 또는 'travel cost(여행 비용 - on a tight budget)' 중 하나로 답변하면 30초를 여유 있게 채울 수 있습니다."
        },

        # =====================================================================
        # 유형 5: 장단점·중요 이유 설명 (Advantages / Why important - Q7) - 5문항
        # =====================================================================
        {
            "id": "p3-21",
            "part": 3,
            "qNum": "Part 3 - #21 (Q7)",
            "typeId": "p3-t5",
            "typeName": "유형 5: 장단점·중요 이유 설명 (Advantages - Q7)",
            "typeBadge": "유형 5 · 장점·중요 이유 (30초)",
            "topic": "도심 속 공원이 주민들에게 주는 장점 (Advantages of City Parks)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "What are the advantages of having a large public park in the center of a city?",
            "questionKo": "도심 한가운데에 큰 공공 공원이 있을 때의 장점들은 무엇인가요?",
            "sentences": [
                {"step": "1. 핵심 주제문", "en": "There are several great advantages of having a large public park in the center of a city.", "ko": "도심 한가운데에 큰 공공 공원이 있으면 몇 가지 큰 장점이 있습니다."},
                {"step": "2. 장점 1 (건강/운동)", "en": "First of all, residents can easily exercise, take a walk, and get some fresh air near their homes for free.", "ko": "무엇보다도 주민들이 집 근처에서 무료로 쉽게 운동하고 산책하며 상쾌한 공기를 마실 수 있습니다."},
                {"step": "3. 장점 2 (휴식/교류)", "en": "Second, it provides a peaceful place for families and friends to gather, have a picnic, and relieve daily stress.", "ko": "둘째, 가족과 친구들이 모여 피크닉을 즐기고 일상 스트레스를 해소할 수 있는 평화로운 장소를 제공합니다."},
                {"step": "4. 장점 3 (환경 개선)", "en": "Finally, green trees and plants help reduce air pollution and make the city more eco-friendly.", "ko": "마지막으로 푸른 나무와 식물들이 대기 오염을 줄이고 도시를 더욱 친환경적으로 만들어 줍니다."}
            ],
            "magicSentences": [
                {"en": "Residents can exercise and get some fresh air for free.", "ko": "주민들이 무료로 운동하고 상쾌한 공기를 마실 수 있습니다.", "tip": "시계토끼 만능 #070 & #077 결합"},
                {"en": "It is eco-friendly and helps reduce air pollution.", "ko": "친환경적이며 대기 오염을 줄이는 데 도움이 됩니다.", "tip": "시계토끼 만능 #081 (환경 보호 만능문장)"}
            ],
            "vocabulary": [
                {"word": "residents", "ipa": "[ˈrezɪdənts]", "pos": "명사", "meaning": "거주민, 지역 주민"},
                {"word": "air pollution", "ipa": "[er pəˈluːʃn]", "pos": "명사", "meaning": "대기 오염"},
                {"word": "eco-friendly", "ipa": "[ˌiːkoʊ ˈfrendli]", "pos": "형용사", "meaning": "친환경적인"}
            ],
            "explanation": "2026년 11월 기출 Q7 문제입니다. 'What are the advantages of ~' 유형은 무조건 'There are several advantages of ~'로 시작해 First(건강/비용) -> Second(스트레스 해소/친목) -> Finally(환경/편리성) 순으로 나열하세요."
        },
        {
            "id": "p3-22",
            "part": 3,
            "qNum": "Part 3 - #22 (Q7)",
            "typeId": "p3-t5",
            "typeName": "유형 5: 장단점·중요 이유 설명 (Advantages - Q7)",
            "typeBadge": "유형 5 · 장점·중요 이유 (30초)",
            "topic": "규칙적인 운동의 장점 (Advantages of Regular Exercise)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "What are the advantages of exercising on a regular basis?",
            "questionKo": "규칙적으로 운동하는 것의 장점은 무엇인가요?",
            "sentences": [
                {"step": "1. 핵심 주제문", "en": "There are many important benefits of exercising on a regular basis.", "ko": "규칙적으로 운동하는 것에는 많은 중요한 이점이 있습니다."},
                {"step": "2. 장점 1 (신체 건강)", "en": "First, it is very good for our physical health because it strengthens our muscles and prevents various diseases.", "ko": "첫째, 근육을 강화하고 다양한 질병을 예방해 주기 때문에 신체 건강에 매우 좋습니다."},
                {"step": "3. 장점 2 (정신 건강)", "en": "Second, working out regularly helps us relieve stress, refresh our minds, and sleep better at night.", "ko": "둘째, 규칙적으로 운동하는 것은 스트레스를 해소하고 기분을 전환하며 밤에 숙면을 취하는 데 도움이 됩니다."},
                {"step": "4. 결론 마무리", "en": "As a result, having more energy allows us to improve our work efficiency during the day.", "ko": "그 결과 활력이 넘치게 되어 낮 시간 동안 업무 효율성도 높일 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "It is good for both physical and mental health.", "ko": "신체적 건강과 정신적 건강 모두에 좋습니다.", "tip": "시계토끼 만능 #077 (건강 만능문장)"},
                {"en": "It helps us relieve stress and improve work efficiency.", "ko": "스트레스를 해소하고 업무 효율을 높이는 데 도움이 됩니다.", "tip": "시계토끼 만능 #051 & #059 결합"}
            ],
            "vocabulary": [
                {"word": "on a regular basis", "ipa": "[ɑːn ə ˈreɡjələr ˈbeɪsɪs]", "pos": "숙어", "meaning": "규칙적으로, 정기적으로"},
                {"word": "prevent diseases", "ipa": "[prɪˈvent dɪˈziːzɪz]", "pos": "숙어", "meaning": "질병을 예방하다"},
                {"word": "work efficiency", "ipa": "[wɜːrk ɪˈfɪʃnsi]", "pos": "명사", "meaning": "업무 효율성"}
            ],
            "explanation": "건강/운동의 장점을 묻는 30초 문제에서는 1) 신체 건강(physical health, prevent diseases) + 2) 정신 건강(mental health, relieve stress) + 3) 업무/학업 능률 향상(improve work efficiency) 3단계로 답하면 완벽합니다."
        },
        {
            "id": "p3-23",
            "part": 3,
            "qNum": "Part 3 - #23 (Q7)",
            "typeId": "p3-t5",
            "typeName": "유형 5: 장단점·중요 이유 설명 (Advantages - Q7)",
            "typeBadge": "유형 5 · 장점·중요 이유 (30초)",
            "topic": "전자책·태블릿 독서의 장점 (Advantages of E-books)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "What are the advantages of reading e-books on a tablet or smartphone compared to paper books?",
            "questionKo": "종이책과 비교했을 때 태블릿이나 스마트폰으로 전자책을 읽는 것의 장점은 무엇인가요?",
            "sentences": [
                {"step": "1. 핵심 주제문", "en": "There are several clear advantages of reading e-books compared to paper books.", "ko": "종이책과 비교했을 때 전자책을 읽는 것에는 몇 가지 분명한 장점이 있습니다."},
                {"step": "2. 장점 1 (휴대성)", "en": "First of all, it is very portable and convenient because I don't have to carry heavy paper books in my bag.", "ko": "무엇보다도 가방에 무거운 종이책을 들고 다닐 필요가 없어서 휴대성이 뛰어나고 매우 편리합니다."},
                {"step": "3. 장점 2 (시공간 접근성)", "en": "Instead, I can store hundreds of books on my tablet and read them anytime, anywhere while commuting.", "ko": "대신 태블릿 하나에 수백 권의 책을 저장해 두고 출퇴근하면서 언제 어디서나 읽을 수 있습니다."},
                {"step": "4. 장점 3 (비용 절감)", "en": "Finally, e-books are usually cheaper than printed books, so I can save money and space at home.", "ko": "마지막으로 전자책은 보통 인쇄된 책보다 저렴해서 돈과 집 안의 수납공간을 절약할 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "I can read them anytime, anywhere with my smartphone or tablet.", "ko": "스마트폰이나 태블릿으로 언제 어디서나 읽을 수 있습니다.", "tip": "시계토끼 만능 #067 (디지털 기기 만능문장)"},
                {"en": "It is cheaper than paper books, so I can save money.", "ko": "종이책보다 저렴해서 돈을 아낄 수 있습니다.", "tip": "시계토끼 만능 #068 (비용 절약)"}
            ],
            "vocabulary": [
                {"word": "portable", "ipa": "[ˈpɔːrtəbl]", "pos": "형용사", "meaning": "휴대하기 편한"},
                {"word": "printed books", "ipa": "[ˈprɪntɪd bʊks]", "pos": "명사", "meaning": "인쇄된 종이책"},
                {"word": "save space", "ipa": "[seɪv speɪs]", "pos": "숙어", "meaning": "공간을 절약하다"}
            ],
            "explanation": "전자책·스트리밍·모바일 앱 등 디지털 서비스의 장점은 1) 휴대성(portable, anytime anywhere) + 2) 비용 절감(cheaper, save money) 두 축으로 설명하면 어떤 주제든 만점을 받습니다."
        },
        {
            "id": "p3-24",
            "part": 3,
            "qNum": "Part 3 - #24 (Q7)",
            "typeId": "p3-t5",
            "typeName": "유형 5: 장단점·중요 이유 설명 (Advantages - Q7)",
            "typeBadge": "유형 5 · 장점·중요 이유 (30초)",
            "topic": "지역 도서관이 제공하는 프로그램의 중요성 (Public Library Programs)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "Why do you think it is important for public libraries to offer free educational programs for local residents?",
            "questionKo": "공공 도서관이 지역 주민들을 위해 무료 교육 프로그램을 제공하는 것이 왜 중요하다고 생각하나요?",
            "sentences": [
                {"step": "1. 핵심 주제문", "en": "I think it is very important for public libraries to offer free educational programs for several reasons.", "ko": "저는 몇 가지 이유로 공공 도서관이 무료 교육 프로그램을 제공하는 것이 매우 중요하다고 생각합니다."},
                {"step": "2. 이유 1 (경제적 부담 해소)", "en": "First, since the programs are free of charge, anyone can learn new skills without any financial burden.", "ko": "첫째, 프로그램이 무료로 제공되기 때문에 누구나 경제적 부담 없이 새로운 기술을 배울 수 있습니다."},
                {"step": "3. 이유 2 (식견 확대)", "en": "Second, residents can gain useful knowledge and broaden their horizons on various topics such as computers or foreign languages.", "ko": "둘째, 주민들이 컴퓨터나 외국어 같은 다양한 주제에 대해 유용한 지식을 얻고 식견을 넓힐 수 있습니다."},
                {"step": "4. 이유 3 (커뮤니티 교류)", "en": "Finally, it is a great opportunity to meet neighbors with similar interests and build a stronger community.", "ko": "마지막으로 비슷한 관심사를 가진 이웃들을 만나고 더 끈끈한 지역 사회를 만드는 좋은 기회가 됩니다."}
            ],
            "magicSentences": [
                {"en": "Anyone can learn new skills without any financial burden.", "ko": "누구나 경제적 부담 없이 새로운 기술을 배울 수 있습니다.", "tip": "시계토끼 만능 #070 & #075 응용"},
                {"en": "Residents can gain useful knowledge and broaden their horizons.", "ko": "주민들이 유용한 지식을 얻고 식견을 넓힐 수 있습니다.", "tip": "시계토끼 만능 #086 & #088 결합"}
            ],
            "vocabulary": [
                {"word": "free of charge", "ipa": "[friː ʌv tʃɑːrdʒ]", "pos": "숙어", "meaning": "무료로"},
                {"word": "financial burden", "ipa": "[faɪˈnænʃl ˈbɜːrdn]", "pos": "명사", "meaning": "경제적 부담"},
                {"word": "similar interests", "ipa": "[ˈsɪmələr ˈɪntrəsts]", "pos": "명사구", "meaning": "비슷한 관심사"}
            ],
            "explanation": "공공기관/도서관/문화센터 무료 프로그램 질문에서는 1) 무료여서 경제적 부담 없음(free of charge, no financial burden) + 2) 지식 습득 및 시야 확대(broaden their horizons) + 3) 이웃과의 교류(meet people with similar interests) 3단계를 활용하세요."
        },
        {
            "id": "p3-25",
            "part": 3,
            "qNum": "Part 3 - #25 (Q7)",
            "typeId": "p3-t5",
            "typeName": "유형 5: 장단점·중요 이유 설명 (Advantages - Q7)",
            "typeBadge": "유형 5 · 장점·중요 이유 (30초)",
            "topic": "재택근무 제도의 장점 (Advantages of Working from Home)",
            "prepTime": 3,
            "responseTime": 30,
            "question": "What are the advantages of allowing employees to work from home once or twice a week?",
            "questionKo": "직원들에게 일주일에 한두 번 재택근무를 허용하는 것의 장점은 무엇인가요?",
            "sentences": [
                {"step": "1. 핵심 주제문", "en": "Allowing employees to work from home has many positive effects for both workers and the company.", "ko": "직원들에게 재택근무를 허용하는 것은 근로자와 회사 양측 모두에게 많은 긍정적인 효과가 있습니다."},
                {"step": "2. 장점 1 (통근 시간·스트레스 절감)", "en": "First of all, employees can save a lot of commuting time and avoid stressful traffic jams during rush hour.", "ko": "무엇보다도 직원들이 출퇴근 시간을 많이 절약할 수 있고 혼잡 시간대의 스트레스 받는 교통 체증을 피할 수 있습니다."},
                {"step": "3. 장점 2 (워라밸 및 집중력)", "en": "Second, they can work in a quiet and comfortable environment at home, which improves their work-life balance.", "ko": "둘째, 집의 조용하고 편안한 환경에서 일할 수 있어 일과 삶의 균형(워라밸)이 향상됩니다."},
                {"step": "4. 결론 (업무 효율 향상)", "en": "As a result, satisfied employees can focus better on their tasks and increase overall productivity.", "ko": "그 결과 만족도가 높아진 직원들은 업무에 더 잘 집중할 수 있고 전반적인 생산성을 높일 수 있습니다."}
            ],
            "magicSentences": [
                {"en": "Employees can save commuting time and avoid traffic jams.", "ko": "직원들이 통근 시간을 아끼고 교통 체증을 피할 수 있습니다.", "tip": "시계토끼 만능 #062 & #063 결합"},
                {"en": "It improves work-life balance and increases overall productivity.", "ko": "워라밸을 개선하고 전반적인 생산성을 높여 줍니다.", "tip": "시계토끼 만능 #059 (직장·업무 최빈출 문장)"}
            ],
            "vocabulary": [
                {"word": "commuting time", "ipa": "[kəˈmjuːtɪŋ taɪm]", "pos": "명사", "meaning": "통근(출퇴근) 시간"},
                {"word": "work-life balance", "ipa": "[wɜːrk laɪf ˈbæləns]", "pos": "명사", "meaning": "일과 삶의 균형 (워라밸)"},
                {"word": "productivity", "ipa": "[ˌproʊdʌkˈtɪvəti]", "pos": "명사", "meaning": "생산성"}
            ],
            "explanation": "재택근무/유연근무제 질문은 파트 3뿐만 아니라 파트 5에서도 단골로 출제됩니다. '통근 시간 절약(save commuting time)' -> '워라밸 향상(improve work-life balance)' -> '생산성 증가(increase productivity)' 공식을 꼭 암기해 두세요."
        }
    ]


def build_part4():
    """Part 4: 표의 속성에 따라 5개 세트로 분류 및 같은 표의 문제를 엮어서 이어지게 구성"""
    t_conf = {
        "headerTitle": "2026 Global Digital Marketing Summit",
        "metaInfo": [
            {"label": "Date & Venue", "value": "November 18, 2026 / Grand Ballroom, Star Hotel"},
            {"label": "Registration Fee", "value": "$80 per person ($60 for early-bird registration by Nov 5)"}
        ],
        "rows": [
            {"date": "09:30 AM", "time": "Opening Keynote", "event": "AI Trends in Advertising", "location": "Main Hall A", "note": "Speaker: Dr. Kevin Park"},
            {"date": "11:00 AM", "time": "Morning Workshop", "event": "Social Media Branding", "location": "Room 204", "note": "Speaker: Sarah Jenkins"},
            {"date": "02:00 PM", "time": "Afternoon Session", "event": "Video Content Strategy", "location": "Room 301", "note": "Speaker: Michael Chen (Changed from 1:00 PM)"},
            {"date": "04:00 PM", "time": "Panel Discussion", "event": "Global E-Commerce Growth", "location": "Main Hall A", "note": "Speaker: Sarah Jenkins"}
        ]
    }
    t_museum = {
        "headerTitle": "Green Library Museum - Autumn Exhibition & Lecture Schedule",
        "metaInfo": [
            {"label": "Location", "value": "Main Exhibition Hall & Conference Room B"},
            {"label": "Admission", "value": "Free for museum members ($15 for non-members)"}
        ],
        "rows": [
            {"date": "Oct 10", "time": "10:00 AM", "event": "New Collection Introduction", "location": "Room 101", "note": "Led by Curator David Smith"},
            {"date": "Oct 17", "time": "02:00 PM", "event": "Historic Preservation Lecture", "location": "Conf. Room B", "note": "Guest Speaker: Dr. Emily Brown"},
            {"date": "Oct 24", "time": "11:00 AM", "event": "Kids Clay Art Workshop", "location": "Outdoor Plaza", "note": "Pre-registration required"},
            {"date": "Oct 31", "time": "03:00 PM", "event": "Ancient Sculpture Seminar", "location": "Conf. Room B", "note": "Guest Speaker: Dr. Emily Brown"}
        ]
    }
    t_training = {
        "headerTitle": "Apex Corp - New Employee Orientation & Training Schedule",
        "metaInfo": [
            {"label": "Date & Location", "value": "September 14 / 4th Floor Training Center"},
            {"label": "Important Note", "value": "All attendees must bring a company ID card and a laptop"}
        ],
        "rows": [
            {"date": "09:00 AM", "time": "Session 1", "event": "Company Vision & Culture", "location": "Room A", "note": "Instructor: HR Director Laura Kim"},
            {"date": "10:30 AM", "time": "Session 2", "event": "IT Security & Software Setup", "location": "Computer Lab 2", "note": "Instructor: Robert Miller"},
            {"date": "01:30 PM", "time": "Session 3", "event": "Business Email Etiquette", "location": "Room A", "note": "Instructor: Laura Kim (Cancelled - Replaced by Sales Overview)"},
            {"date": "03:30 PM", "time": "Session 4", "event": "Advanced Excel & Data Tools", "location": "Computer Lab 2", "note": "Instructor: Robert Miller"}
        ]
    }
    t_tour = {
        "headerTitle": "Blue Harbor One-Day City Sightseeing Tour",
        "metaInfo": [
            {"label": "Departure", "value": "8:30 AM sharp at Central Station Exit 4"},
            {"label": "Tour Fee", "value": "$55 (Includes bus & admission tickets / Lunch is NOT included)"}
        ],
        "rows": [
            {"date": "09:00 AM", "time": "Stop 1", "event": "Old Castle Walking Tour", "location": "Historic District", "note": "Guide: Alex Morgan"},
            {"date": "12:00 PM", "time": "Stop 2", "event": "Seafood Market Free Time", "location": "Harbor Pier", "note": "Buy your own lunch"},
            {"date": "02:00 PM", "time": "Stop 3", "event": "Botanical Garden Visit", "location": "East Hill", "note": "Guide: Alex Morgan"},
            {"date": "04:30 PM", "time": "Stop 4", "event": "Sunset Harbor Cruise", "location": "Dock 3", "note": "Life jacket required"}
        ]
    }
    t_interview = {
        "headerTitle": "Marketing Department - Job Interview & Resume Summary",
        "metaInfo": [
            {"label": "Interview Date", "value": "October 22 / Conference Room 502 (In-person or Zoom)"},
            {"label": "Position", "value": "Senior Overseas Marketing Specialist"}
        ],
        "rows": [
            {"date": "10:00 AM", "time": "Daniel Carter", "event": "5 yrs at Global Ad Agency", "location": "In-person", "note": "Fluent in Spanish / MBA Degree"},
            {"date": "11:00 AM", "time": "Jessica Lee", "event": "2 yrs at Retail Startup", "location": "Zoom (Online)", "note": "Certified Data Analyst"},
            {"date": "02:00 PM", "time": "Brian Gomez", "event": "4 yrs at Tech Corp", "location": "In-person", "note": "Fluent in Chinese & English"},
            {"date": "03:30 PM", "time": "Hannah Cho", "event": "6 yrs at Media Group", "location": "Zoom (Online)", "note": "Former Team Leader"}
        ]
    }

    sets = [
        # =====================================================================
        # 세트 1: 컨퍼런스·학술 심포지엄 일정표
        # =====================================================================
        {
            "id": "p4-set1",
            "part": 4,
            "setNum": "Part 4 - Set 1",
            "tableTypeId": "table-conf",
            "tableTypeName": "컨퍼런스·학술 심포지엄",
            "tableTypeBadge": "컨퍼런스 일정표",
            "topic": "2026 Global Digital Marketing Summit",
            "prepTime": 45,
            "scheduleTable": t_conf,
            "questions": [
                {
                    "qId": "p4-s1-q8",
                    "qNum": "Question 8",
                    "topic": "개최 일시·장소 및 개막 기조연설 시작 시각",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "When and where will the Global Digital Marketing Summit be held, and what time does the opening keynote start?",
                    "questionKo": "글로벌 디지털 마케팅 서밋은 언제 어디서 열리며, 개막 기조연설은 몇 시에 시작하나요?",
                    "sentences": [
                        {"step": "1. 일시 및 장소 안내", "en": "The Global Digital Marketing Summit will be held on November 18th at the Grand Ballroom in the Star Hotel.", "ko": "글로벌 디지털 마케팅 서밋은 11월 18일에 스타 호텔 그랜드 볼룸에서 열릴 예정입니다."},
                        {"step": "2. 첫 세션 시작 시각", "en": "Also, the opening keynote on AI Trends in Advertising starts at 9:30 AM in Main Hall A.", "ko": "또한 광고 분야 AI 트렌드에 관한 개막 기조연설은 메인 홀 A에서 오전 9시 30분에 시작합니다."}
                    ],
                    "magicSentences": [
                        {"en": "It will be held on November 18th at the Grand Ballroom.", "ko": "11월 18일에 그랜드 볼룸에서 열릴 예정입니다.", "tip": "시계토끼 만능 #097 & #099 (행사 개최 일시·장소 공식)"},
                        {"en": "The opening keynote starts at 9:30 AM.", "ko": "개막 기조연설은 오전 9시 30분에 시작합니다.", "tip": "시계토끼 만능 #106 (시작 시각 안내 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "be held", "ipa": "[biː held]", "pos": "수동태", "meaning": "(행사가) 개최되다, 열리다"},
                        {"word": "keynote", "ipa": "[ˈkiːnoʊt]", "pos": "명사", "meaning": "기조연설"},
                        {"word": "ballroom", "ipa": "[ˈbɔːlruːm]", "pos": "명사", "meaning": "대연회장"}
                    ],
                    "explanation": "표 상단의 개최 일시(November 18th), 장소(Grand Ballroom in Star Hotel), 첫 강연 시각(9:30 AM)을 차례로 읽어주면 완벽합니다."
                },
                {
                    "qId": "p4-s1-q9",
                    "qNum": "Question 9",
                    "topic": "오후 세션 시간 변경 오류 정정",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "I heard that the afternoon session on Video Content Strategy starts at 1:00 PM. Is that right?",
                    "questionKo": "'비디오 콘텐츠 전략' 오후 세션이 오후 1시에 시작한다고 들었는데, 맞나요?",
                    "sentences": [
                        {"step": "1. 오류 부정 표현", "en": "No, I'm afraid you have the wrong information.", "ko": "아니요, 유감스럽지만 잘못된 정보를 알고 계십니다."},
                        {"step": "2. 변경 내역 정정", "en": "The afternoon session on Video Content Strategy was originally scheduled at 1:00 PM, but it has been changed to 2:00 PM.", "ko": "비디오 콘텐츠 전략 오후 세션은 원래 오후 1시로 예정되어 있었으나 오후 2시로 변경되었습니다."},
                        {"step": "3. 장소 및 강연자 부연", "en": "It will be led by Michael Chen in Room 301.", "ko": "301호에서 마이클 첸의 진행으로 열릴 예정입니다."}
                    ],
                    "magicSentences": [
                        {"en": "No, I'm afraid you have the wrong information.", "ko": "아니요, 유감스럽지만 잘못된 정보를 알고 계십니다.", "tip": "시계토끼 만능 #114 (Q9 오류 정정 1순위 오프닝)"},
                        {"en": "It has been changed from 1:00 PM to 2:00 PM.", "ko": "오후 1시에서 오후 2시로 변경되었습니다.", "tip": "시계토끼 만능 #118 (시간/장소 변경 완료형 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "originally", "ipa": "[əˈrɪdʒənəli]", "pos": "부사", "meaning": "원래, 본래"},
                        {"word": "strategy", "ipa": "[ˈstrætədʒi]", "pos": "명사", "meaning": "전략"},
                        {"word": "be changed to", "ipa": "[biː tʃeɪndʒd tuː]", "pos": "수동태", "meaning": "~로 변경되다"}
                    ],
                    "explanation": "표에 (Changed from 1:00 PM) 메모가 있으므로 질문자의 정보가 틀렸음을 밝히고 올바른 시각(2:00 PM)과 장소(Room 301)를 전달하세요."
                },
                {
                    "qId": "p4-s1-q10",
                    "qNum": "Question 10",
                    "topic": "특정 연사(Sarah Jenkins) 진행 세션 전체 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "I am a big fan of Sarah Jenkins. Could you please give me all the details about the sessions led by her?",
                    "questionKo": "저는 사라 젠킨스의 큰 팬입니다. 그녀가 진행하는 모든 세션의 세부 정보를 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 안내 (오프닝)", "en": "Sure! There are two sessions led by Sarah Jenkins at the summit.", "ko": "물론입니다! 이번 서밋에는 사라 젠킨스가 진행하는 세션이 두 개 있습니다."},
                        {"step": "2. 첫 번째 항목 안내", "en": "First, at 11:00 AM, she will lead the Morning Workshop on Social Media Branding in Room 204.", "ko": "첫째, 오전 11시에 204호에서 소셜 미디어 브랜딩에 관한 오전 워크숍을 진행합니다."},
                        {"step": "3. 두 번째 항목 안내", "en": "Second, at 4:00 PM, she will lead the Panel Discussion on Global E-Commerce Growth in Main Hall A.", "ko": "둘째, 오후 4시에 메인 홀 A에서 글로벌 이커머스 성장에 관한 패널 토론을 진행할 예정입니다."}
                    ],
                    "magicSentences": [
                        {"en": "Sure, there are two sessions led by Sarah Jenkins.", "ko": "물론입니다, 사라 젠킨스가 이끄는 세션이 두 개 있습니다.", "tip": "시계토끼 만능 #129 (Q10 30초 오프닝 공식)"},
                        {"en": "First, at 11:00 AM, there is Social Media Branding in Room 204.", "ko": "첫째, 오전 11시에 204호에서 소셜 미디어 브랜딩이 있습니다.", "tip": "시계토끼 만능 #131 (First / Second 순차 나열 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "branding", "ipa": "[ˈbrændɪŋ]", "pos": "명사", "meaning": "브랜딩, 브랜드 구축"},
                        {"word": "panel discussion", "ipa": "[ˈpænl dɪˈskʌʃn]", "pos": "명사", "meaning": "패널 토의, 공개 토론"},
                        {"word": "e-commerce", "ipa": "[ˈiː kɑːmɜːrs]", "pos": "명사", "meaning": "전자상거래"}
                    ],
                    "explanation": "표의 11:00 AM 워크숍과 4:00 PM 패널 토론 두 개 항목을 순서대로 시간-제목-장소를 또박또박 전달하세요."
                },
                {
                    "qId": "p4-s1-q-extra",
                    "qNum": "추가 문제 (등록비·할인)",
                    "topic": "서밋 참가 등록비 및 얼리버드 할인 혜택 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "How much is the registration fee for the summit, and how can I get a discount?",
                    "questionKo": "서밋 참가 등록비는 얼마이며, 어떻게 하면 할인을 받을 수 있나요?",
                    "sentences": [
                        {"step": "1. 기본 참가비 안내", "en": "The regular registration fee for the summit is 80 dollars per person.", "ko": "서밋의 일반 등록비는 1인당 80달러입니다."},
                        {"step": "2. 얼리버드 할인 조건", "en": "However, if you sign up for early-bird registration by November 5th, you can get a discounted price of 60 dollars.", "ko": "하지만 11월 5일까지 얼리버드 등록을 신청하시면 60달러의 할인된 가격으로 등록하실 수 있습니다."}
                    ],
                    "magicSentences": [
                        {"en": "The regular registration fee is 80 dollars per person.", "ko": "일반 등록비는 1인당 80달러입니다.", "tip": "시계토끼 만능 #121 (등록비/참가비 안내 공식)"},
                        {"en": "However, if you register by November 5th, it is 60 dollars.", "ko": "하지만 11월 5일까지 등록하시면 60달러입니다.", "tip": "시계토끼 만능 #124 (얼리버드 할인 조건 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "registration fee", "ipa": "[ˌredʒɪˈstreɪʃn fiː]", "pos": "명사", "meaning": "등록비, 참가비"},
                        {"word": "per person", "ipa": "[pɜːr ˈpɜːrsn]", "pos": "숙어", "meaning": "1인당"},
                        {"word": "early-bird", "ipa": "[ˈɜːrli bɜːrd]", "pos": "형용사", "meaning": "조기 신청(얼리버드)의"}
                    ],
                    "explanation": "표 상단 메타 정보의 Registration Fee를 바탕으로 일반 요금과 얼리버드 할인 기한(by Nov 5)을 답변하세요."
                }
            ]
        },

        # =====================================================================
        # 세트 2: 박물관 전시·문화 강연 일정표
        # =====================================================================
        {
            "id": "p4-set2",
            "part": 4,
            "setNum": "Part 4 - Set 2",
            "tableTypeId": "table-museum",
            "tableTypeName": "박물관 전시·문화 강연",
            "tableTypeBadge": "박물관 전시표",
            "topic": "Green Library Museum - Autumn Exhibition & Lecture Schedule",
            "prepTime": 45,
            "scheduleTable": t_museum,
            "questions": [
                {
                    "qId": "p4-s2-q8",
                    "qNum": "Question 8",
                    "topic": "10월 첫 번째 행사 및 개최 장소 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "What is the first event scheduled in October, and when and where will it take place?",
                    "questionKo": "10월에 예정된 첫 번째 행사는 무엇이며, 언제 어디서 열리나요?",
                    "sentences": [
                        {"step": "1. 첫 번째 행사명 안내", "en": "The first event scheduled in October is the New Collection Introduction.", "ko": "10월에 예정된 첫 번째 행사는 '신규 컬렉션 소개'입니다."},
                        {"step": "2. 일시 및 장소 안내", "en": "It will take place on October 10th at 10:00 AM in Room 101, and it will be led by Curator David Smith.", "ko": "10월 10일 오전 10시에 101호에서 열릴 예정이며, 큐레이터 데이비드 스미스가 진행합니다."}
                    ],
                    "magicSentences": [
                        {"en": "It will take place on October 10th at 10:00 AM in Room 101.", "ko": "10월 10일 오전 10시에 101호에서 열립니다.", "tip": "시계토끼 만능 #098 (take place 개최 공식)"},
                        {"en": "It will be led by Curator David Smith.", "ko": "큐레이터 데이비드 스미스에 의해 진행될 것입니다.", "tip": "시계토끼 만능 #110 (진행자 안내 수동태)"}
                    ],
                    "vocabulary": [
                        {"word": "take place", "ipa": "[teɪk pleɪs]", "pos": "숙어", "meaning": "개최되다, 열리다"},
                        {"word": "curator", "ipa": "[kjʊˈreɪtər]", "pos": "명사", "meaning": "박물관 큐레이터"},
                        {"word": "collection", "ipa": "[kəˈlekʃn]", "pos": "명사", "meaning": "소장품, 컬렉션"}
                    ],
                    "explanation": "표 첫 줄의 October 10th, 10:00 AM, Room 101, New Collection Introduction을 말하세요."
                },
                {
                    "qId": "p4-s2-q9",
                    "qNum": "Question 9",
                    "topic": "역사 보존 특강 시작 시각 오류 정정",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "If I remember correctly, the Historic Preservation Lecture on October 17th is scheduled to start at 5:00 PM. Is that correct?",
                    "questionKo": "제가 기억하기로는 10월 17일 역사 보존 특강이 오후 5시에 시작하는 것으로 되어 있는데 맞나요?",
                    "sentences": [
                        {"step": "1. 오류 부정 표현", "en": "No, I'm sorry, that is not correct.", "ko": "아니요, 죄송하지만 그렇지 않습니다."},
                        {"step": "2. 올바른 정보 전달", "en": "Actually, the Historic Preservation Lecture on October 17th is scheduled to start at 2:00 PM, not 5:00 PM.", "ko": "사실 10월 17일 역사 보존 특강은 오후 5시가 아니라 오후 2시에 시작할 예정입니다."},
                        {"step": "3. 장소 및 연사 안내", "en": "It will take place in Conference Room B with Guest Speaker Dr. Emily Brown.", "ko": "초청 연사 에밀리 브라운 박사와 함께 회의실 B에서 열릴 것입니다."}
                    ],
                    "magicSentences": [
                        {"en": "No, I'm sorry, that is not correct.", "ko": "아니요, 죄송하지만 맞지 않습니다.", "tip": "시계토끼 만능 #115 (간결한 부정 오프닝)"},
                        {"en": "Actually, it is scheduled to start at 2:00 PM in Conference Room B.", "ko": "사실 회의실 B에서 오후 2시에 시작할 예정입니다.", "tip": "시계토끼 만능 #116 (Actually 정정 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "historic preservation", "ipa": "[hɪˈstɔːrɪk ˌprezərˈveɪʃn]", "pos": "명사", "meaning": "역사 유적 보존"},
                        {"word": "lecture", "ipa": "[ˈlektʃər]", "pos": "명사", "meaning": "강연, 강의"}
                    ],
                    "explanation": "질문자가 말한 5:00 PM이 아니라 실제 표에 적힌 2:00 PM임을 정정하세요."
                },
                {
                    "qId": "p4-s2-q10",
                    "qNum": "Question 10",
                    "topic": "에밀리 브라운 박사(Dr. Emily Brown) 특강 전체 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "I would love to attend all the events featuring Dr. Emily Brown. Could you tell me all the details about her sessions?",
                    "questionKo": "에밀리 브라운 박사가 나오는 모든 행사에 참석하고 싶습니다. 그녀의 세션에 대한 모든 세부 정보를 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 안내", "en": "Of course! There are two events featuring Guest Speaker Dr. Emily Brown in October.", "ko": "물론입니다! 10월에 초청 연사 에밀리 브라운 박사가 진행하는 행사가 두 개 있습니다."},
                        {"step": "2. 첫 번째 행사 안내", "en": "First, on October 17th at 2:00 PM, there is the Historic Preservation Lecture in Conference Room B.", "ko": "첫째, 10월 17일 오후 2시에 회의실 B에서 역사 보존 특강이 열립니다."},
                        {"step": "3. 두 번째 행사 안내", "en": "Second, on October 31st at 3:00 PM, she will lead the Ancient Sculpture Seminar, which will also be held in Conference Room B.", "ko": "둘째, 10월 31일 오후 3시에는 고대 조각 세미나를 진행하며, 이 역시 회의실 B에서 열립니다."}
                    ],
                    "magicSentences": [
                        {"en": "There are two events featuring Dr. Emily Brown.", "ko": "에밀리 브라운 박사가 출연하는 행사가 두 개 있습니다.", "tip": "시계토끼 만능 #129 (총 개수 선제시)"},
                        {"en": "Second, on October 31st at 3:00 PM, there is Ancient Sculpture Seminar.", "ko": "둘째, 10월 31일 오후 3시에 고대 조각 세미나가 있습니다.", "tip": "시계토끼 만능 #132 (두 번째 항목 연결)"}
                    ],
                    "vocabulary": [
                        {"word": "featuring", "ipa": "[ˈfiːtʃərɪŋ]", "pos": "분사", "meaning": "~을 특별히 다루는, 출연하는"},
                        {"word": "ancient sculpture", "ipa": "[ˈeɪnʃənt ˈskʌlptʃər]", "pos": "명사", "meaning": "고대 조각"}
                    ],
                    "explanation": "10월 17일 강연과 10월 31일 세미나 두 가지 일정을 순서대로 읽어주세요."
                },
                {
                    "qId": "p4-s2-q-extra",
                    "qNum": "추가 문제 (입장료·사전등록)",
                    "topic": "박물관 입장료 및 사전 등록 필요 행사 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "How much is the admission fee for the museum, and which event requires pre-registration?",
                    "questionKo": "박물관 입장료는 얼마이며, 어떤 행사가 사전 등록을 필요로 하나요?",
                    "sentences": [
                        {"step": "1. 회원/비회원 입장료 안내", "en": "Admission is free of charge for museum members, and it is 15 dollars for non-members.", "ko": "입장료는 박물관 회원에게는 무료이며, 비회원에게는 15달러입니다."},
                        {"step": "2. 사전 등록 행사 안내", "en": "Also, the Kids Clay Art Workshop on October 24th at 11:00 AM in the Outdoor Plaza requires pre-registration.", "ko": "또한 10월 24일 오전 11시 야외 광장에서 열리는 어린이 클레이 아트 워크숍은 사전 등록이 필요합니다."}
                    ],
                    "magicSentences": [
                        {"en": "Admission is free for members and 15 dollars for non-members.", "ko": "입장료는 회원은 무료이고 비회원은 15달러입니다.", "tip": "시계토끼 만능 #122 & #123 결합"},
                        {"en": "Pre-registration is required for the Kids Clay Art Workshop.", "ko": "어린이 클레이 아트 워크숍은 사전 등록이 필수입니다.", "tip": "시계토끼 만능 #127 (사전 등록 필수 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "admission", "ipa": "[ədˈmɪʃn]", "pos": "명사", "meaning": "입장료"},
                        {"word": "pre-registration", "ipa": "[ˌpriː redʒɪˈstreɪʃn]", "pos": "명사", "meaning": "사전 등록"}
                    ],
                    "explanation": "상단 Admission 정보와 표 세 번째 줄의 Kids Clay Art Workshop 사전 등록 비고를 답변하세요."
                }
            ]
        },

        # =====================================================================
        # 세트 3: 사내 직원 연수·워크숍 일정표
        # =====================================================================
        {
            "id": "p4-set3",
            "part": 4,
            "setNum": "Part 4 - Set 3",
            "tableTypeId": "table-training",
            "tableTypeName": "사내 직원 연수·교육",
            "tableTypeBadge": "직원 연수표",
            "topic": "Apex Corp - New Employee Orientation & Training Schedule",
            "prepTime": 45,
            "scheduleTable": t_training,
            "questions": [
                {
                    "qId": "p4-s3-q8",
                    "qNum": "Question 8",
                    "topic": "교육 장소 및 필수 지참물 확인",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Where is the new employee training taking place, and what do attendees need to bring?",
                    "questionKo": "신입사원 교육은 어디서 열리며, 참석자들은 무엇을 지참해야 하나요?",
                    "sentences": [
                        {"step": "1. 교육 일시 및 장소", "en": "The new employee training is taking place on September 14th at the 4th Floor Training Center.", "ko": "신입사원 교육은 9월 14일에 4층 교육 센터에서 열립니다."},
                        {"step": "2. 필수 지참물 안내", "en": "Please note that all attendees are required to bring a company ID card and a laptop.", "ko": "모든 참석자는 사원증과 노트북을 필수로 지참해야 한다는 점을 참고해 주십시오."}
                    ],
                    "magicSentences": [
                        {"en": "It is taking place at the 4th Floor Training Center.", "ko": "4층 교육 센터에서 열립니다.", "tip": "층수 앞 서수 발음 주의"},
                        {"en": "All attendees are required to bring a company ID card and a laptop.", "ko": "모든 참석자는 사원증과 노트북을 지참해야 합니다.", "tip": "시계토끼 만능 #128 (지참물 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "attendees", "ipa": "[əˌtenˈdiːz]", "pos": "명사", "meaning": "참석자들"},
                        {"word": "be required to", "ipa": "[biː rɪˈkwaɪərd tuː]", "pos": "숙어", "meaning": "~해야 한다"}
                    ],
                    "explanation": "일시(September 14), 장소(4th Floor Training Center), 필수 지참물(ID card and a laptop)을 차례로 전달하세요."
                },
                {
                    "qId": "p4-s3-q9",
                    "qNum": "Question 9",
                    "topic": "이메일 에티켓 세션 취소 및 대체 안내",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "I am looking forward to taking the Business Email Etiquette session at 1:30 PM. Can I still attend that session?",
                    "questionKo": "오후 1시 30분에 있는 비즈니스 이메일 에티켓 세션을 기대하고 있는데, 그 세션에 참석할 수 있나요?",
                    "sentences": [
                        {"step": "1. 참석 불가 안내", "en": "No, I'm afraid you cannot attend that session.", "ko": "아니요, 유감스럽지만 그 세션에는 참석하실 수 없습니다."},
                        {"step": "2. 취소 및 대체 사실 전달", "en": "Unfortunately, the Business Email Etiquette session at 1:30 PM has been cancelled.", "ko": "안타깝게도 오후 1시 30분 비즈니스 이메일 에티켓 세션은 취소되었습니다."},
                        {"step": "3. 대체 프로그램 안내", "en": "Instead, it has been replaced by the Sales Overview session in Room A.", "ko": "대신 A룸에서 열리는 '영업 개요' 세션으로 대체되었습니다."}
                    ],
                    "magicSentences": [
                        {"en": "Unfortunately, that session has been cancelled.", "ko": "안타깝게도 그 세션은 취소되었습니다.", "tip": "시계토끼 만능 #117 (취소 안내 수동태 공식)"},
                        {"en": "Instead, it has been replaced by Sales Overview.", "ko": "대신 영업 개요 세션으로 대체되었습니다.", "tip": "시계토끼 만능 #120 (대체 프로그램 안내)"}
                    ],
                    "vocabulary": [
                        {"word": "be cancelled", "ipa": "[biː ˈkænsld]", "pos": "수동태", "meaning": "취소되다"},
                        {"word": "be replaced by", "ipa": "[biː rɪˈpleɪst baɪ]", "pos": "수동태", "meaning": "~로 대체되다"}
                    ],
                    "explanation": "표에 취소선으로 표시된 1:30 PM 세션의 취소와 Sales Overview 대체 사실을 설명하세요."
                },
                {
                    "qId": "p4-s3-q10",
                    "qNum": "Question 10",
                    "topic": "로버트 밀러(Robert Miller) 강사의 실습 세션 전체 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Can you give me all the information about the training sessions taught by Robert Miller?",
                    "questionKo": "로버트 밀러가 가르치는 교육 세션에 대한 모든 정보를 알려주실 수 있나요?",
                    "sentences": [
                        {"step": "1. 총 개수 안내", "en": "Sure! There are two training sessions taught by Robert Miller on September 14th.", "ko": "물론입니다! 9월 14일에 로버트 밀러가 가르치는 교육 세션이 두 개 있습니다."},
                        {"step": "2. 오전 세션 안내", "en": "First, at 10:30 AM, he will teach Session 2 on IT Security and Software Setup in Computer Lab 2.", "ko": "첫째, 오전 10시 30분에 컴퓨터 실습실 2에서 IT 보안 및 소프트웨어 설정에 관한 세션 2를 가르칩니다."},
                        {"step": "3. 오후 세션 안내", "en": "Second, at 3:30 PM, he will lead Session 4 on Advanced Excel and Data Tools in Computer Lab 2 as well.", "ko": "둘째, 오후 3시 30분에도 컴퓨터 실습실 2에서 고급 엑셀 및 데이터 도구에 관한 세션 4를 진행합니다."}
                    ],
                    "magicSentences": [
                        {"en": "There are two sessions taught by Robert Miller.", "ko": "로버트 밀러가 가르치는 세션이 두 개 있습니다.", "tip": "시계토끼 만능 #129 & #111 결합"},
                        {"en": "Both sessions will take place in Computer Lab 2.", "ko": "두 세션 모두 컴퓨터 실습실 2에서 열립니다.", "tip": "장소가 동일할 때 묶어주는 고득점 표현"}
                    ],
                    "vocabulary": [
                        {"word": "IT security", "ipa": "[ˌaɪ ˈtiː sɪˈkjʊrəti]", "pos": "명사", "meaning": "IT 보안"},
                        {"word": "software setup", "ipa": "[ˈsɔːftwer ˈsetʌp]", "pos": "명사", "meaning": "소프트웨어 설치/설정"}
                    ],
                    "explanation": "오전 10:30과 오후 3:30 실습실 2에서 진행되는 두 세션을 순서대로 설명하세요."
                }
            ]
        },

        # =====================================================================
        # 세트 4: 여행·시티 투어 여정표
        # =====================================================================
        {
            "id": "p4-set4",
            "part": 4,
            "setNum": "Part 4 - Set 4",
            "tableTypeId": "table-tour",
            "tableTypeName": "여행·시티 투어 여정",
            "tableTypeBadge": "시티 투어표",
            "topic": "Blue Harbor One-Day City Sightseeing Tour",
            "prepTime": 45,
            "scheduleTable": t_tour,
            "questions": [
                {
                    "qId": "p4-s4-q8",
                    "qNum": "Question 8",
                    "topic": "투어 집결 장소 및 버스 출발 시각 안내",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Where is the meeting point for the city sightseeing tour, and what time does the bus depart?",
                    "questionKo": "도시 관광 투어의 집결 장소는 어디이며, 버스는 몇 시에 출발하나요?",
                    "sentences": [
                        {"step": "1. 집결지 및 출발 시각", "en": "The meeting point for the tour is Central Station Exit 4, and the bus departs at 8:30 AM sharp.", "ko": "투어 집결 장소는 센트럴역 4번 출구이며, 버스는 오전 8시 30분 정각에 출발합니다."},
                        {"step": "2. 첫 일정 부연", "en": "After departure, the first stop will be the Old Castle Walking Tour at 9:00 AM.", "ko": "출발 후 첫 번째 코스는 오전 9시 고성 도보 투어입니다."}
                    ],
                    "magicSentences": [
                        {"en": "We will meet at Central Station Exit 4, and the bus leaves at 8:30 AM.", "ko": "센트럴역 4번 출구에서 만나며 버스는 오전 8시 30분에 출발합니다.", "tip": "시계토끼 만능 #108 (투어 출발 시각 공식)"}
                    ],
                    "vocabulary": [
                        {"word": "sightseeing", "ipa": "[ˈsaɪtsiːɪŋ]", "pos": "명사", "meaning": "관광"},
                        {"word": "depart", "ipa": "[dɪˈpɑːrt]", "pos": "동사", "meaning": "출발하다"}
                    ],
                    "explanation": "표 상단의 Departure 항목(8:30 AM sharp at Central Station Exit 4)을 정확히 읽어주세요."
                },
                {
                    "qId": "p4-s4-q9",
                    "qNum": "Question 9",
                    "topic": "투어 참가비 점심 식사 포함 여부 정정",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "I heard that lunch at the Harbor Seafood Market is included in the $55 tour fee. Is that right?",
                    "questionKo": "하버 수산시장에서의 점심 식사가 55달러 투어 요금에 포함되어 있다고 들었는데 맞나요?",
                    "sentences": [
                        {"step": "1. 오류 부정 표현", "en": "No, I'm afraid you have the wrong information.", "ko": "아니요, 유감스럽지만 잘못된 정보를 알고 계십니다."},
                        {"step": "2. 포함 내역 및 불포함 정정", "en": "The 55-dollar tour fee only includes the bus and admission tickets, and lunch is not included.", "ko": "55달러 투어 요금에는 버스와 입장권만 포함되어 있으며, 점심 식사는 포함되어 있지 않습니다."},
                        {"step": "3. 부연 설명", "en": "Therefore, you need to buy your own lunch during the free time at the Seafood Market at 12:00 PM.", "ko": "따라서 낮 12시 수산시장 자유 시간 동안 본인의 점심 식사를 직접 사 드셔야 합니다."}
                    ],
                    "magicSentences": [
                        {"en": "The fee includes the bus and admission tickets, but lunch is not included.", "ko": "요금에는 버스와 입장권이 포함되지만 점심은 포함되지 않습니다.", "tip": "시계토끼 만능 #126 (포함/불포함 구분)"}
                    ],
                    "vocabulary": [
                        {"word": "admission ticket", "ipa": "[ədˈmɪʃn ˈtɪkɪt]", "pos": "명사", "meaning": "입장권"},
                        {"word": "be included in", "ipa": "[biː ɪnˈkluːdɪd ɪn]", "pos": "수동태", "meaning": "~에 포함되다"}
                    ],
                    "explanation": "Tour Fee 항목의 'Lunch is NOT included'를 짚어 질문자의 오해를 바로잡으세요."
                },
                {
                    "qId": "p4-s4-q10",
                    "qNum": "Question 10",
                    "topic": "가이드 알렉스 모건(Alex Morgan) 인솔 코스 전체 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "Could you tell me all the details about the sightseeing stops led by Guide Alex Morgan?",
                    "questionKo": "가이드 알렉스 모건이 인솔하는 관광 코스에 대한 모든 세부 정보를 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 안내", "en": "Certainly! There are two sightseeing stops led by Guide Alex Morgan during the tour.", "ko": "물론입니다! 투어 중 가이드 알렉스 모건이 인솔하는 관광 코스가 두 곳 있습니다."},
                        {"step": "2. 첫 번째 코스 안내", "en": "First, at 9:00 AM, there is the Old Castle Walking Tour in the Historic District.", "ko": "첫째, 오전 9시에 역사 지구에서 고성 도보 투어가 진행됩니다."},
                        {"step": "3. 두 번째 코스 안내", "en": "Second, at 2:00 PM in the afternoon, he will lead the Botanical Garden Visit at East Hill.", "ko": "둘째, 오후 2시에 이스트 힐에서 식물원 방문 일정을 인솔할 예정입니다."}
                    ],
                    "magicSentences": [
                        {"en": "There are two stops led by Guide Alex Morgan.", "ko": "알렉스 모건 가이드가 인솔하는 코스가 두 곳 있습니다.", "tip": "시계토끼 만능 #110 & #129 결합"}
                    ],
                    "vocabulary": [
                        {"word": "historic district", "ipa": "[hɪˈstɔːrɪk ˈdɪstrɪkt]", "pos": "명사", "meaning": "역사 지구"},
                        {"word": "botanical garden", "ipa": "[bəˈtænɪkl ˈɡɑːrdn]", "pos": "명사", "meaning": "식물원"}
                    ],
                    "explanation": "오전 9시 고성 투어와 오후 2시 식물원 방문 일정을 시간, 장소와 함께 안내하세요."
                },
                {
                    "qId": "p4-s4-q-extra",
                    "qNum": "추가 문제 (안전 규정)",
                    "topic": "선셋 크루즈 탑승 시각·장소 및 구명조끼 필수 착용 안내",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "What is the last activity of the tour, and is there any safety requirement for participants?",
                    "questionKo": "투어의 마지막 활동은 무엇이며, 참가자들을 위한 안전 필수 사항이 있나요?",
                    "sentences": [
                        {"step": "1. 마지막 일정 안내", "en": "The last activity of the tour is the Sunset Harbor Cruise, which starts at 4:30 PM at Dock 3.", "ko": "투어의 마지막 활동은 오후 4시 30분에 3번 선착장에서 시작하는 선셋 하버 크루즈입니다."},
                        {"step": "2. 안전 수칙 안내", "en": "Also, for safety reasons, all participants are required to wear a life jacket during the cruise.", "ko": "또한 안전상의 이유로 모든 참가자는 크루즈 탑승 중 구명조끼를 필수로 착용해야 합니다."}
                    ],
                    "magicSentences": [
                        {"en": "All participants are required to wear a life jacket.", "ko": "모든 참가자는 구명조끼를 착용해야 합니다.", "tip": "시계토끼 만능 #128 응용 (안전 복장 필수)"}
                    ],
                    "vocabulary": [
                        {"word": "harbor cruise", "ipa": "[ˈhɑːrbər kruːz]", "pos": "명사", "meaning": "항구 크루즈"},
                        {"word": "life jacket", "ipa": "[laɪf ˈdʒækɪt]", "pos": "명사", "meaning": "구명조끼"}
                    ],
                    "explanation": "마지막 행인 4:30 PM Sunset Harbor Cruise와 'Life jacket required'를 완전한 문장으로 말하세요."
                }
            ]
        },

        # =====================================================================
        # 세트 5: 인사 채용 면접·이력서 요약표
        # =====================================================================
        {
            "id": "p4-set5",
            "part": 4,
            "setNum": "Part 4 - Set 5",
            "tableTypeId": "table-interview",
            "tableTypeName": "인사 채용 면접·이력서",
            "tableTypeBadge": "채용 면접표",
            "topic": "Marketing Department - Job Interview & Resume Summary",
            "prepTime": 45,
            "scheduleTable": t_interview,
            "questions": [
                {
                    "qId": "p4-s5-q8",
                    "qNum": "Question 8",
                    "topic": "면접 일시·장소 및 첫 번째 면접자 안내",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "When and where will the job interviews be held, and who is the first candidate?",
                    "questionKo": "채용 면접은 언제 어디서 열리며, 첫 번째 면접 대상자는 누구인가요?",
                    "sentences": [
                        {"step": "1. 면접 일시 및 장소", "en": "The job interviews will be held on October 22nd in Conference Room 502.", "ko": "채용 면접은 10월 22일에 502호 회의실에서 열릴 예정입니다."},
                        {"step": "2. 첫 면접자 안내", "en": "The first candidate is Daniel Carter, and his in-person interview is scheduled at 10:00 AM.", "ko": "첫 번째 지원자는 다니엘 카터이며, 그의 대면 면접은 오전 10시에 예정되어 있습니다."}
                    ],
                    "magicSentences": [
                        {"en": "The interviews will be held on October 22nd in Conference Room 502.", "ko": "면접은 10월 22일 502호 회의실에서 열립니다.", "tip": "시계토끼 만능 #097 & #100"}
                    ],
                    "vocabulary": [
                        {"word": "candidate", "ipa": "[ˈkændɪdət]", "pos": "명사", "meaning": "지원자, 후보자"},
                        {"word": "in-person", "ipa": "[ˌɪn ˈpɜːrsn]", "pos": "형용사", "meaning": "대면의"}
                    ],
                    "explanation": "October 22nd, Conference Room 502, 그리고 첫 번째 지원자 Daniel Carter(10:00 AM)를 답변하세요."
                },
                {
                    "qId": "p4-s5-q9",
                    "qNum": "Question 9",
                    "topic": "전원 대면 참석 여부 오류 정정 (줌 온라인 면접)",
                    "prepTime": 3,
                    "responseTime": 15,
                    "question": "Are all candidates required to attend the interview in person at Conference Room 502?",
                    "questionKo": "모든 면접 지원자가 502호 회의실에 직접 대면으로 참석해야 하나요?",
                    "sentences": [
                        {"step": "1. 오류 부정 표현", "en": "No, not all candidates are required to attend the interview in person.", "ko": "아니요, 모든 지원자가 대면으로 면접에 참석해야 하는 것은 아닙니다."},
                        {"step": "2. 대면/비대면 구분 설명", "en": "While Daniel Carter and Brian Gomez will have in-person interviews, Jessica Lee and Hannah Cho will have online interviews via Zoom.", "ko": "다니엘 카터와 브라이언 고메즈는 대면 면접을 보지만, 제시카 리와 한나 조는 줌(Zoom)을 통해 온라인 면접을 볼 예정입니다."}
                    ],
                    "magicSentences": [
                        {"en": "No, that is not correct. Some interviews will be held online via Zoom.", "ko": "아니요, 그렇지 않습니다. 일부 면접은 줌을 통해 온라인으로 진행됩니다.", "tip": "온라인/대면 혼합 일정표 정정 공식"}
                    ],
                    "vocabulary": [
                        {"word": "via Zoom", "ipa": "[ˈvaɪə zuːm]", "pos": "전치사구", "meaning": "줌을 통하여"}
                    ],
                    "explanation": "표에 In-person과 Zoom (Online)이 나뉘어 있으므로 Jessica Lee와 Hannah Cho는 온라인 참석임을 밝히세요."
                },
                {
                    "qId": "p4-s5-q10",
                    "qNum": "Question 10",
                    "topic": "오후 시간대(Afternoon) 예정 면접자 전체 안내",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "I have another meeting in the morning, so I can only join the interviews in the afternoon. Can you tell me all the interviews scheduled in the afternoon?",
                    "questionKo": "제가 오전에 다른 회의가 있어서 오후 면접에만 참석할 수 있습니다. 오후에 예정된 모든 면접 일정을 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 총 개수 안내", "en": "Sure! There are two interviews scheduled in the afternoon on October 22nd.", "ko": "물론입니다! 10월 22일 오후에는 두 건의 면접이 예정되어 있습니다."},
                        {"step": "2. 첫 번째 오후 면접", "en": "First, at 2:00 PM, we have an in-person interview with Brian Gomez, who has four years of experience at Tech Corp and is fluent in Chinese and English.", "ko": "첫째, 오후 2시에 테크 코프에서 4년 경력이 있고 중국어와 영어에 능통한 브라이언 고메즈와의 대면 면접이 있습니다."},
                        {"step": "3. 두 번째 오후 면접", "en": "Second, at 3:30 PM, there is an online Zoom interview with Hannah Cho, who has six years of experience at Media Group as a former team leader.", "ko": "둘째, 오후 3시 30분에는 미디어 그룹에서 이전 팀장으로 6년 경력이 있는 한나 조와의 온라인 줌 면접이 있습니다."}
                    ],
                    "magicSentences": [
                        {"en": "There are two interviews scheduled in the afternoon.", "ko": "오후에 예정된 면접이 두 건 있습니다.", "tip": "시계토끼 만능 #129 (오후 필터링)"}
                    ],
                    "vocabulary": [
                        {"word": "fluent in", "ipa": "[ˈfluːənt ɪn]", "pos": "숙어", "meaning": "~에 유창한"}
                    ],
                    "explanation": "오후 2:00 Brian Gomez와 오후 3:30 Hannah Cho 두 지원자의 경력과 면접 방식을 전달하세요."
                },
                {
                    "qId": "p4-s5-q-extra",
                    "qNum": "추가 문제 (자격 요건)",
                    "topic": "3년 이상 경력직 지원자 전체 확인",
                    "prepTime": 3,
                    "responseTime": 30,
                    "question": "We are looking for experienced candidates who have more than three years of work experience. Could you tell me all the candidates who meet this requirement?",
                    "questionKo": "저희는 3년 이상의 근무 경력을 가진 경력직 지원자를 찾고 있습니다. 이 조건을 충족하는 모든 지원자를 알려주시겠어요?",
                    "sentences": [
                        {"step": "1. 조건 충족 인원 안내", "en": "Sure! There are three candidates who have more than three years of work experience.", "ko": "물론입니다! 3년 이상의 근무 경력을 가진 지원자가 세 명 있습니다."},
                        {"step": "2. 첫 번째 지원자", "en": "First, Daniel Carter at 10:00 AM has five years of experience at Global Ad Agency, and he has an MBA degree.", "ko": "첫째, 오전 10시의 다니엘 카터는 글로벌 광고 대행사에서 5년 경력이 있으며 MBA 학위를 가지고 있습니다."},
                        {"step": "3. 두 번째 지원자", "en": "Second, Brian Gomez at 2:00 PM has four years of experience at Tech Corp, and he is fluent in Chinese and English.", "ko": "둘째, 오후 2시의 브라이언 고메즈는 테크 코프에서 4년 경력이 있으며 중국어와 영어에 능통합니다."},
                        {"step": "4. 세 번째 지원자", "en": "Finally, Hannah Cho at 3:30 PM has six years of experience at Media Group as a former team leader.", "ko": "마지막으로 오후 3시 30분의 한나 조는 미디어 그룹에서 전직 팀장으로 6년의 경력이 있습니다."}
                    ],
                    "magicSentences": [
                        {"en": "There are three candidates who have more than three years of work experience.", "ko": "3년 이상의 근무 경력을 가진 지원자가 세 명 있습니다.", "tip": "이력서 조건 필터링 오프닝"}
                    ],
                    "vocabulary": [
                        {"word": "work experience", "ipa": "[wɜːrk ɪkˈspɪriəns]", "pos": "명사", "meaning": "근무 경력"}
                    ],
                    "explanation": "2년 경력인 Jessica Lee를 제외하고 3년 이상 경력자인 Daniel Carter(5년), Brian Gomez(4년), Hannah Cho(6년) 세 명을 차례로 소개하세요."
                }
            ]
        }
    ]

    return sets


def build_part5():
    """Part 5: 10문항 (2025~2026 최신 기출 10선 + 문장별 발음 + 만능문장 + 핵심어휘 + 해설)"""
    return [
        {
            "id": "p5-01",
            "part": 5,
            "qNum": "Part 5 - #01 (Q11)",
            "category": "일상·라이프스타일",
            "topic": "Will E-books Completely Replace Paper Books in the Future?",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you agree or disagree with the following statement? E-books will completely replace paper books in the near future. Give specific reasons and examples to support your opinion.",
            "questionKo": "다음 진술에 동의하십니까, 반대하십니까? '가까운 미래에 전자책이 종이책을 완전히 대체할 것이다.' 구체적인 이유와 예시를 들어 의견을 뒷받침하시오.",
            "sentences": [
                {"step": "1. 서론 (찬성 입장)", "en": "I strongly agree with the statement that e-books will completely replace paper books in the near future.", "ko": "저는 가까운 미래에 전자책이 종이책을 완전히 대체할 것이라는 진술에 강력히 동의합니다."},
                {"step": "2. 본론 1 (휴대성·편리성)", "en": "First of all, e-books are much more portable and convenient than heavy paper books.", "ko": "무엇보다도 전자책은 무거운 종이책보다 훨씬 휴대성이 뛰어나고 편리합니다."},
                {"step": "3. 본론 1 부연", "en": "People can store hundreds of books on a single tablet or smartphone and read them anytime, anywhere while commuting.", "ko": "사람들은 태블릿이나 스마트폰 하나에 수백 권의 책을 저장해 두고 출퇴근하면서 언제 어디서나 읽을 수 있습니다."},
                {"step": "4. 본론 2 (비용·환경 보호)", "en": "Second, reading e-books is economical and eco-friendly because it saves printing costs and reduces paper waste.", "ko": "둘째, 전자책을 읽는 것은 인쇄 비용을 아끼고 종이 쓰레기를 줄여주기 때문에 경제적이면서도 친환경적입니다."},
                {"step": "5. 개인 경험 예시", "en": "For example, since I bought a tablet last year, I have only downloaded e-books because they are 30 percent cheaper and don't take up space in my room.", "ko": "예를 들어 저는 작년에 태블릿을 산 이후로 가격이 30% 더 저렴하고 방 공간을 차지하지 않는 전자책만 다운로드해서 읽고 있습니다."},
                {"step": "6. 결론 재강조", "en": "For these reasons, I firmly believe that e-books will eventually replace traditional paper books.", "ko": "이러한 이유들로 저는 전자책이 결국 전통적인 종이책을 대체할 것이라고 확신합니다."}
            ],
            "magicSentences": [
                {"en": "People can read them anytime, anywhere with their smartphones.", "ko": "스마트폰으로 언제 어디서나 읽을 수 있습니다.", "tip": "시계토끼 만능 #158 (디지털 기술 찬성 핵심)"},
                {"en": "It is eco-friendly because it reduces paper waste and protects the environment.", "ko": "종이 낭비를 줄이고 환경을 보호하므로 친환경적입니다.", "tip": "시계토끼 만능 #175 (환경 보호 만능문장)"}
            ],
            "vocabulary": [
                {"word": "replace", "ipa": "[rɪˈpleɪs]", "pos": "동사", "meaning": "대체하다"},
                {"word": "portable", "ipa": "[ˈpɔːrtəbl]", "pos": "형용사", "meaning": "휴대하기 편한"},
                {"word": "economical", "ipa": "[ˌiːkəˈnɑːmɪkl]", "pos": "형용사", "meaning": "경제적인, 비용이 적게 드는"},
                {"word": "take up space", "ipa": "[teɪk ʌp speɪs]", "pos": "숙어", "meaning": "공간을 차지하다"}
            ],
            "explanation": "2026년 11월 기출 문제입니다. 종이 vs 디지털(전자책, 모바일 신문, 전자 영수증) 주제는 1) 휴대성·시공간 자유(anytime, anywhere) + 2) 비용 절감 및 친환경(save money & eco-friendly) 두 가지로 답하면 60초 분량이 완벽하게 채워집니다."
        },
        {
            "id": "p5-02",
            "part": 5,
            "qNum": "Part 5 - #02 (Q11)",
            "category": "직장·리더십",
            "topic": "Most Important Quality of a Good Leader: Listening vs. Charisma",
            "prepTime": 45,
            "responseTime": 60,
            "question": "What do you think is the most important quality of a good leader: listening to employees' opinions or making quick decisions on their own? Explain your answer with specific reasons.",
            "questionKo": "좋은 리더의 가장 중요한 자질은 무엇이라고 생각합니까? (직원들의 의견 경청하기 vs 스스로 신속하게 의사결정 내리기)",
            "sentences": [
                {"step": "1. 서론 (선택 제시)", "en": "I definitely think that listening to employees' opinions is the most important quality of a good leader.", "ko": "저는 직원들의 의견을 경청하는 것이 좋은 리더의 가장 중요한 자질이라고 확실히 생각합니다."},
                {"step": "2. 본론 1 (신뢰·팀워크)", "en": "First of all, open communication builds strong trust and teamwork within the company.", "ko": "무엇보다도 열린 소통은 회사 내에서 끈끈한 신뢰와 팀워크를 구축해 줍니다."},
                {"step": "3. 본론 1 부연", "en": "When a leader respects team members' ideas, employees feel valued and become more motivated to work hard.", "ko": "리더가 팀원들의 아이디어를 존중할 때 직원들은 존중받는다고 느끼고 더 열심히 일하려는 동기를 얻게 됩니다."},
                {"step": "4. 본론 2 (창의적 해결책)", "en": "Second, by gathering diverse perspectives from employees, a leader can come up with more creative solutions and avoid costly mistakes.", "ko": "둘째, 직원들로부터 다양한 관점을 수렴함으로써 리더는 더 창의적인 해결책을 떠올리고 큰 실수를 피할 수 있습니다."},
                {"step": "5. 구체적 예시", "en": "For example, my former manager always held weekly feedback sessions, which helped our team increase sales by 20 percent.", "ko": "예를 들어 저의 이전 매니저님은 항상 주간 피드백 회의를 열어 팀원의 의견을 들었고, 그 덕분에 팀 매출을 20% 늘릴 수 있었습니다."},
                {"step": "6. 결론 마무리", "en": "Therefore, I believe listening to employees is the key to becoming a successful leader.", "ko": "따라서 저는 직원들의 말에 귀 기울이는 것이 성공적인 리더가 되는 핵심 열쇠라고 믿습니다."}
            ],
            "magicSentences": [
                {"en": "It builds strong trust and improves teamwork among employees.", "ko": "직원들 간의 강한 신뢰를 쌓고 팀워크를 향상시킵니다.", "tip": "시계토끼 만능 #147 & #148 (리더십·조직문화 만능문장)"},
                {"en": "Employees feel valued and become more motivated to work hard.", "ko": "직원들이 존중받는다고 느끼며 열심히 일할 동기를 얻습니다.", "tip": "시계토끼 만능 #145 (동기부여 만능문장)"}
            ],
            "vocabulary": [
                {"word": "quality", "ipa": "[ˈkwɑːləti]", "pos": "명사", "meaning": "자질, 덕목"},
                {"word": "feel valued", "ipa": "[fiːl ˈvæljuːd]", "pos": "숙어", "meaning": "존중받는다고 느끼다"},
                {"word": "perspective", "ipa": "[pərˈspektɪv]", "pos": "명사", "meaning": "관점, 시각"},
                {"word": "come up with", "ipa": "[kʌm ʌp wɪð]", "pos": "숙어", "meaning": "(아이디어·해결책을) 떠올리다"}
            ],
            "explanation": "리더십/매니저의 자질을 묻는 파트 5 문제는 항상 '소통·경청(listening & communication)'을 선택하세요. 신뢰 구축(build trust) + 동기부여(motivate employees) + 다양한 아이디어(creative ideas) 3단 공식이 만능으로 적용됩니다."
        },
        {
            "id": "p5-03",
            "part": 5,
            "qNum": "Part 5 - #03 (Q11)",
            "category": "기술·인공지능(AI)",
            "topic": "Positive Impact of AI Tools on Work and Learning",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Nowadays, many people use AI tools for their work and studies. Do you think this is a positive or negative trend? Support your response with specific reasons and examples.",
            "questionKo": "오늘날 많은 사람들이 업무와 학업에 AI 도구를 사용합니다. 이것이 긍정적인 추세라고 생각합니까, 부정적인 추세라고 생각합니까?",
            "sentences": [
                {"step": "1. 서론 (긍정 입장)", "en": "I strongly believe that using AI tools for work and studies is a very positive trend.", "ko": "저는 업무와 학업에 AI 도구를 사용하는 것이 매우 긍정적인 추세라고 강력히 믿습니다."},
                {"step": "2. 본론 1 (시간 절약·생산성)", "en": "First of all, AI tools help people save a tremendous amount of time and increase work productivity.", "ko": "무엇보다도 AI 도구는 사람들이 엄청난 시간을 절약하고 업무 생산성을 높이도록 도와줍니다."},
                {"step": "3. 본론 1 부연", "en": "Workers can quickly summarize long documents, translate foreign languages, and analyze data in just a few seconds.", "ko": "직장인들은 단 몇 초 만에 긴 문서를 요약하고 외국어를 번역하며 데이터를 분석할 수 있습니다."},
                {"step": "4. 본론 2 (맞춤형 학습)", "en": "Second, for students, AI acts as a personal tutor available 24 hours a day, helping them understand difficult concepts easily.", "ko": "둘째, 학생들에게 AI는 하루 24시간 이용 가능한 개인 튜터 역할을 하여 어려운 개념을 쉽게 이해하도록 도와줍니다."},
                {"step": "5. 개인 경험 예시", "en": "For instance, I use an AI tool at my office to draft English emails, and it has cut my working time in half.", "ko": "예를 들어 저는 사무실에서 영문 이메일 초안을 작성할 때 AI 도구를 사용하는데, 덕분에 업무 시간이 절반으로 줄었습니다."},
                {"step": "6. 결론 마무리", "en": "For these reasons, I think using AI technology brings great benefits to our daily lives.", "ko": "이러한 이유로 저는 AI 기술을 활용하는 것이 우리 일상에 큰 혜택을 가져다준다고 생각합니다."}
            ],
            "magicSentences": [
                {"en": "It helps people save a lot of time and increase work productivity.", "ko": "많은 시간을 절약하고 업무 생산성을 높이는 데 도움이 됩니다.", "tip": "시계토끼 만능 #141 & #142 (기술·IT 찬성 1순위 문장)"},
                {"en": "People can get useful information in just a few seconds.", "ko": "단 몇 초 만에 유용한 정보를 얻을 수 있습니다.", "tip": "시계토끼 만능 #156 (인터넷·AI 정보 검색 장점)"}
            ],
            "vocabulary": [
                {"word": "tremendous", "ipa": "[trəˈmendəs]", "pos": "형용사", "meaning": "엄청난, 막대한"},
                {"word": "summarize", "ipa": "[ˈsʌməraɪz]", "pos": "동사", "meaning": "요약하다"},
                {"word": "concept", "ipa": "[ˈkɑːnsept]", "pos": "명사", "meaning": "개념"},
                {"word": "cut in half", "ipa": "[kʌt ɪn hæf]", "pos": "숙어", "meaning": "절반으로 줄이다"}
            ],
            "explanation": "2026년 하반기 최빈출 토픽인 AI·자동화·신기술 문제는 무조건 'Positive(긍정)'를 선택하고 'save time(시간 절약)' + 'increase productivity(생산성 향상)' + '영문 이메일 작성 예시'를 말하면 AL(160~180점)을 받을 수 있습니다."
        },
        {
            "id": "p5-04",
            "part": 5,
            "qNum": "Part 5 - #04 (Q11)",
            "category": "직장·근무환경",
            "topic": "Adopting Flexible Work Hours, 4-Day Workweeks, and Remote Work",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you agree or disagree that companies should allow employees to have flexible working hours or work from home? Give specific reasons to support your opinion.",
            "questionKo": "기업들이 직원들에게 유연근무제나 재택근무를 허용해야 한다는 의견에 동의하십니까, 반대하십니까?",
            "sentences": [
                {"step": "1. 서론 (찬성 입장)", "en": "I completely agree that companies should allow employees to have flexible working hours and work from home.", "ko": "저는 기업들이 직원들에게 유연근무제와 재택근무를 허용해야 한다는 의견에 전적으로 동의합니다."},
                {"step": "2. 본론 1 (통근 스트레스 해소)", "en": "First, employees can save commuting time and avoid stressful traffic jams during rush hour.", "ko": "첫째, 직원들은 출퇴근 시간을 절약하고 러시아워의 스트레스 받는 교통 체증을 피할 수 있습니다."},
                {"step": "3. 본론 1 부연", "en": "Instead of wasting two hours on the road every day, they can use that time to rest or exercise.", "ko": "매일 길 위에서 두 시간을 낭비하는 대신 그 시간을 휴식을 취하거나 운동하는 데 쓸 수 있습니다."},
                {"step": "4. 본론 2 (워라밸 및 애사심)", "en": "Second, it greatly improves employees' work-life balance and job satisfaction, which reduces employee turnover.", "ko": "둘째, 직원들의 워라밸과 직무 만족도를 크게 높여주어 직원 이직률을 낮춰줍니다."},
                {"step": "5. 구체적 예시", "en": "For example, after my company introduced flexible working hours last year, employees became much happier and overall productivity increased.", "ko": "예를 들어 저희 회사가 작년에 유연근무제를 도입한 이후 직원들이 훨씬 행복해졌고 전반적인 생산성도 향상되었습니다."},
                {"step": "6. 결론 마무리", "en": "Therefore, flexible working policies are beneficial for both employees and companies.", "ko": "따라서 유연한 근무 정책은 직원과 회사 모두에게 유익합니다."}
            ],
            "magicSentences": [
                {"en": "It greatly improves employees' work-life balance and job satisfaction.", "ko": "직원들의 워라밸과 직무 만족도를 크게 향상시킵니다.", "tip": "시계토끼 만능 #143 & #144 결합"},
                {"en": "Happy employees can focus better and increase overall productivity.", "ko": "행복한 직원들은 더 잘 집중할 수 있고 전체 생산성을 높입니다.", "tip": "시계토끼 만능 #141 (직장 복지 찬성 결론)"}
            ],
            "vocabulary": [
                {"word": "flexible working hours", "ipa": "[ˈfleksəbl ˈwɜːrkɪŋ ˈaʊərz]", "pos": "명사구", "meaning": "유연근무제, 탄력근무 시간"},
                {"word": "job satisfaction", "ipa": "[dʒɑːb ˌsætɪsˈfækʃn]", "pos": "명사", "meaning": "직무 만족도"},
                {"word": "employee turnover", "ipa": "[ɪmˈplɔɪiː ˈtɜːrnoʊvər]", "pos": "명사", "meaning": "직원 이직률"},
                {"word": "beneficial", "ipa": "[ˌbenɪˈfɪʃl]", "pos": "형용사", "meaning": "유익한, 이로운"}
            ],
            "explanation": "사내 복지·유연근무·휴가 확대 주제는 언제나 '통근 피로 감소(save commuting time)' -> '워라밸 및 직무 만족도 상승(job satisfaction)' -> '생산성 향상 및 이직률 감소(increase productivity)'로 연결하세요."
        },
        {
            "id": "p5-05",
            "part": 5,
            "qNum": "Part 5 - #05 (Q11)",
            "category": "직업·커리어 선택",
            "topic": "Choosing a Job: High Salary vs. More Vacation & Free Time",
            "prepTime": 45,
            "responseTime": 60,
            "question": "When choosing a job, which do you think is more important: a high salary or plenty of vacation time? Use specific reasons and examples to support your choice.",
            "questionKo": "직장을 선택할 때 높은 연봉과 충분한 휴가 기간 중 어느 것이 더 중요하다고 생각합니까?",
            "sentences": [
                {"step": "1. 서론 (높은 연봉 선택)", "en": "When choosing a job, I definitely think a high salary is more important than plenty of vacation time.", "ko": "직장을 선택할 때 저는 충분한 휴가 기간보다 높은 연봉이 확실히 더 중요하다고 생각합니다."},
                {"step": "2. 본론 1 (생계비 및 경제적 안정)", "en": "First of all, the cost of living is rising rapidly these days, so financial stability is essential for a happy life.", "ko": "무엇보다도 요즘 물가(생활비)가 빠르게 오르고 있어서 행복한 삶을 위해서는 경제적 안정이 필수적입니다."},
                {"step": "3. 본론 1 부연", "en": "Even if I have a lot of vacation days, I cannot travel abroad or enjoy hobbies if I am on a tight budget.", "ko": "아무리 휴가 일수가 많더라도 예산이 빠듯하면 해외여행을 가거나 취미 생활을 즐길 수 없습니다."},
                {"step": "4. 본론 2 (강력한 동기부여)", "en": "Second, a high salary is the strongest motivation for employees to work hard and achieve their goals.", "ko": "둘째, 높은 연봉은 직원들이 열심히 일하고 목표를 달성하게 만드는 가장 강력한 동기부여입니다."},
                {"step": "5. 개인 예시", "en": "For example, when I received a salary raise and bonus last year, I felt strongly rewarded and worked with much greater passion.", "ko": "예를 들어 제가 작년에 연봉 인상과 보너스를 받았을 때 큰 보상을 받았다고 느꼈고 훨씬 더 큰 열정을 가지고 일했습니다."},
                {"step": "6. 결론 마무리", "en": "For these reasons, I believe a high salary is the most important factor when choosing a job.", "ko": "이러한 이유들로 저는 직업을 선택할 때 높은 연봉이 가장 중요한 요소라고 믿습니다."}
            ],
            "magicSentences": [
                {"en": "Financial stability is essential because the cost of living is rising.", "ko": "생활비가 오르고 있기 때문에 경제적 안정은 필수적입니다.", "tip": "시계토끼 만능 #151 (연봉·급여 선택 1순위 논리)"},
                {"en": "A high salary is the strongest motivation to work hard.", "ko": "높은 연봉은 열심히 일하게 하는 가장 강력한 동기부여입니다.", "tip": "시계토끼 만능 #152 (금전적 보상 효과)"}
            ],
            "vocabulary": [
                {"word": "cost of living", "ipa": "[kɔːst ʌv ˈlɪvɪŋ]", "pos": "명사", "meaning": "생활비, 물가"},
                {"word": "financial stability", "ipa": "[faɪˈnænʃl stəˈbɪləti]", "pos": "명사", "meaning": "경제적 안정"},
                {"word": "on a tight budget", "ipa": "[ɑːn ə taɪt ˈbʌdʒɪt]", "pos": "숙어", "meaning": "예산이 빠듯한"},
                {"word": "rewarded", "ipa": "[rɪˈwɔːrdɪd]", "pos": "분사/형용사", "meaning": "보상받은"}
            ],
            "explanation": "연봉(High salary) vs 워라밸/적성/동료 비교 문제에서는 연봉을 선택해 '물가 상승으로 인한 경제적 안정(cost of living & financial stability)'과 '돈이 있어야 여가도 즐길 수 있음'을 말하면 논리가 매우 탄탄해집니다."
        },
        {
            "id": "p5-06",
            "part": 5,
            "qNum": "Part 5 - #06 (Q11)",
            "category": "교육·학습",
            "topic": "Education & Training: Group Projects vs. Individual Assignments",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you think it is better for students and employees to work on group projects or work individually? Give specific reasons and examples to support your opinion.",
            "questionKo": "학생들과 직장인들이 그룹 프로젝트를 하는 것과 개인별로 과제를 하는 것 중 어느 쪽이 더 낫다고 생각합니까?",
            "sentences": [
                {"step": "1. 서론 (그룹 프로젝트 선택)", "en": "I strongly believe that working on group projects is much better than working individually.", "ko": "저는 그룹 프로젝트를 하는 것이 개인별로 일하는 것보다 훨씬 더 낫다고 강력히 믿습니다."},
                {"step": "2. 본론 1 (다양한 아이디어 및 문제 해결)", "en": "First of all, people can share diverse ideas and solve complex problems much faster together.", "ko": "무엇보다도 사람들이 다양한 아이디어를 공유하고 복잡한 문제를 함께 훨씬 더 빠르게 해결할 수 있습니다."},
                {"step": "3. 본론 1 부연", "en": "By dividing the workload according to each member's strengths, the team can achieve better results in less time.", "ko": "각 구성원의 강점에 따라 업무량을 분담함으로써 팀은 더 짧은 시간에 더 나은 결과를 달성할 수 있습니다."},
                {"step": "4. 본론 2 (사회성·소통 능력)", "en": "Second, working in a group helps people develop communication skills, teamwork, and responsibility.", "ko": "둘째, 그룹으로 일하는 것은 사람들이 의사소통 능력, 팀워크, 그리고 책임감을 기르는 데 도움이 됩니다."},
                {"step": "5. 개인 경험 예시", "en": "For example, when I prepared a marketing presentation with three teammates last month, we combined our ideas and won first prize.", "ko": "예를 들어 지난달에 세 명의 팀원과 함께 마케팅 발표를 준비했을 때 저희의 아이디어를 결합해 1등 상을 받았습니다."},
                {"step": "6. 결론 마무리", "en": "Therefore, I think group projects are far more effective than working alone.", "ko": "따라서 저는 그룹 프로젝트가 혼자 일하는 것보다 훨씬 더 효과적이라고 생각합니다."}
            ],
            "magicSentences": [
                {"en": "People can share diverse ideas and solve problems faster together.", "ko": "다양한 아이디어를 공유하고 문제를 함께 더 빨리 해결할 수 있습니다.", "tip": "시계토끼 만능 #163 (팀워크·그룹 활동 찬성 공식)"},
                {"en": "It helps people develop communication skills and teamwork.", "ko": "의사소통 기술과 팀워크를 기르는 데 도움이 됩니다.", "tip": "시계토끼 만능 #164 (협업 교육 효과)"}
            ],
            "vocabulary": [
                {"word": "individually", "ipa": "[ˌɪndɪˈvɪdʒuəli]", "pos": "부사", "meaning": "개별적으로, 혼자서"},
                {"word": "workload", "ipa": "[ˈwɜːrkloʊd]", "pos": "명사", "meaning": "업무량"},
                {"word": "strengths", "ipa": "[streŋkθs]", "pos": "명사", "meaning": "강점, 장점"},
                {"word": "communication skills", "ipa": "[kəˌmjuːnɪˈkeɪʃn skɪlz]", "pos": "명사", "meaning": "의사소통 능력"}
            ],
            "explanation": "팀 프로젝트 vs 개인 과제 주제는 파트 3와 파트 5 모두에서 단골로 출제됩니다. '아이디어 공유 및 업무 분담(share ideas & divide the workload)' + '소통 능력 및 협동심 함양(communication skills & teamwork)' 두 가지를 기억하세요."
        },
        {
            "id": "p5-07",
            "part": 5,
            "qNum": "Part 5 - #07 (Q11)",
            "category": "비즈니스·마케팅",
            "topic": "Corporate Promotion: Social Media Marketing vs. Traditional Ads",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Which do you think is a more effective way for companies to advertise their new products: social media marketing or traditional television commercials? Explain why.",
            "questionKo": "기업이 신제품을 광고할 때 소셜 미디어 마케팅과 전통적인 TV 광고 중 어느 것이 더 효과적인 방법이라고 생각합니까?",
            "sentences": [
                {"step": "1. 서론 (소셜 미디어 선택)", "en": "I definitely think social media marketing is a much more effective way to advertise new products than television commercials.", "ko": "저는 신제품을 광고할 때 소셜 미디어 마케팅이 TV 광고보다 훨씬 더 효과적인 방법이라고 확실히 생각합니다."},
                {"step": "2. 본론 1 (저비용 고효율)", "en": "First, social media advertising is much more cost-effective, especially for small businesses with a limited budget.", "ko": "첫째, 소셜 미디어 광고는 비용 대비 효율이 훨씬 뛰어나며, 특히 예산이 제한된 소규모 기업에 유리합니다."},
                {"step": "3. 본론 2 (타겟팅 및 확산성)", "en": "Second, companies can target specific age groups and interests, and viral videos can reach millions of users worldwide in seconds.", "ko": "둘째, 기업들이 특정 연령대와 관심사를 타겟팅할 수 있고, 입소문 영상은 단 몇 초 만에 전 세계 수백만 명의 사용자에게 도달할 수 있습니다."},
                {"step": "4. 본론 2 부연 (스마트폰 사용)", "en": "Nowadays, people spend much more time looking at their smartphones than watching TV.", "ko": "오늘날 사람들은 TV를 보는 시간보다 스마트폰을 보는 데 훨씬 더 많은 시간을 보냅니다."},
                {"step": "5. 개인 경험 예시", "en": "For example, I recently bought a new cosmetic product right after watching a short review video on Instagram.", "ko": "예를 들어 저도 최근에 인스타그램에서 짧은 리뷰 영상을 본 직후에 바로 새로운 화장품을 구매했습니다."},
                {"step": "6. 결론 마무리", "en": "For these reasons, social media marketing is the most powerful advertising tool today.", "ko": "이러한 이유로 소셜 미디어 마케팅은 오늘날 가장 강력한 광고 수단입니다."}
            ],
            "magicSentences": [
                {"en": "It is much more cost-effective and saves advertising costs.", "ko": "비용 대비 효율이 훨씬 뛰어나고 광고비를 절약해 줍니다.", "tip": "시계토끼 만능 #169 (마케팅·비즈니스 비용 효율 문장)"},
                {"en": "People spend a lot of time on their smartphones every day.", "ko": "사람들은 매일 스마트폰에 많은 시간을 소비합니다.", "tip": "시계토끼 만능 #159 (모바일·SNS 트렌드 근거)"}
            ],
            "vocabulary": [
                {"word": "cost-effective", "ipa": "[ˌkɔːst ɪˈfektɪv]", "pos": "형용사", "meaning": "비용 대비 효과가 뛰어난, 가성비 좋은"},
                {"word": "commercials", "ipa": "[kəˈmɜːrʃlz]", "pos": "명사", "meaning": "(TV·라디오) 상업 광고"},
                {"word": "viral", "ipa": "[ˈvaɪrəl]", "pos": "형용사", "meaning": "입소문이 퍼지는, 바이럴의"},
                {"word": "target", "ipa": "[ˈtɑːrɡɪt]", "pos": "동사", "meaning": "겨냥하다, 타겟으로 삼다"}
            ],
            "explanation": "비즈니스/마케팅 광고 수단 비교 문제에서는 'Social Media Marketing'을 선택하면 가성비(cost-effective), 스마트폰 사용 시간(spend time on smartphones), 즉각적 구매 연결(Instagram 예시)을 자연스럽게 말할 수 있습니다."
        },
        {
            "id": "p5-08",
            "part": 5,
            "qNum": "Part 5 - #08 (Q11)",
            "category": "아동·청소년 교육",
            "topic": "Teaching Children Foreign Languages and Financial Concepts Early",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you agree or disagree that children should start learning a foreign language as early as possible? Support your opinion with specific reasons and examples.",
            "questionKo": "아이들이 가능한 한 일찍부터 외국어를 배우기 시작해야 한다는 의견에 동의하십니까, 반대하십니까?",
            "sentences": [
                {"step": "1. 서론 (찬성 입장)", "en": "I strongly agree that children should start learning a foreign language as early as possible.", "ko": "저는 아이들이 가능한 한 일찍 외국어를 배우기 시작해야 한다는 의견에 강력히 동의합니다."},
                {"step": "2. 본론 1 (빠른 흡수력 및 발음)", "en": "First of all, young children have flexible brains, so they can absorb new words and natural pronunciation much faster than adults.", "ko": "무엇보다도 어린아이들은 두뇌가 유연해서 성인보다 새로운 단어와 자연스러운 발음을 훨씬 더 빠르게 흡수할 수 있습니다."},
                {"step": "3. 본론 1 부연", "en": "Also, they are not afraid of making mistakes, which helps them gain confidence in speaking.", "ko": "또한 실수하는 것을 두려워하지 않기 때문에 말하기에 대한 자신감을 얻는 데 도움이 됩니다."},
                {"step": "4. 본론 2 (글로벌 경쟁력)", "en": "Second, in this globalized world, being fluent in a foreign language will give them more career opportunities in the future.", "ko": "둘째, 이 세계화된 시대에서 외국어에 능통한 것은 미래에 아이들에게 더 많은 직업적 기회를 줄 것입니다."},
                {"step": "5. 구체적 예시", "en": "For example, my nephew started watching English cartoons at age five, and now he speaks English fluently without stress.", "ko": "예를 들어 제 조카는 다섯 살 때부터 영어 만화를 보기 시작했는데 지금은 스트레스 없이 영어를 유창하게 구사합니다."},
                {"step": "6. 결론 마무리", "en": "Therefore, early foreign language education is very beneficial for children's future.", "ko": "따라서 조기 외국어 교육은 아이들의 미래에 매우 유익합니다."}
            ],
            "magicSentences": [
                {"en": "Children can absorb new knowledge much faster than adults.", "ko": "아이들은 성인보다 새로운 지식을 훨씬 더 빨리 흡수할 수 있습니다.", "tip": "시계토끼 만능 #166 (아동 조기 교육 찬성 1순위 문장)"},
                {"en": "It will give them more opportunities in the future.", "ko": "미래에 그들에게 더 많은 기회를 줄 것입니다.", "tip": "시계토끼 만능 #168 (교육의 미래 가치 만능문장)"}
            ],
            "vocabulary": [
                {"word": "absorb", "ipa": "[əbˈzɔːrb]", "pos": "동사", "meaning": "(지식·언어를) 흡수하다, 습득하다"},
                {"word": "pronunciation", "ipa": "[prəˌnʌnsiˈeɪʃn]", "pos": "명사", "meaning": "발음"},
                {"word": "globalized", "ipa": "[ˈɡloʊbəlaɪzd]", "pos": "형용사", "meaning": "세계화된"},
                {"word": "nephew", "ipa": "[ˈnefjuː]", "pos": "명사", "meaning": "조카"}
            ],
            "explanation": "아이들(Children)에게 외국어, 코딩, 악기, 경제 관념 등을 일찍 가르쳐야 하는가? 하는 질문은 모두 '어릴수록 흡수가 빠르고 좋은 습관이 형성됨(absorb faster)' + '미래에 큰 자산이 됨(great asset in the future)'으로 답하면 됩니다."
        },
        {
            "id": "p5-09",
            "part": 5,
            "qNum": "Part 5 - #09 (Q11)",
            "category": "환경·사회 정책",
            "topic": "Government Regulations on Single-Use Plastics and Public Transit",
            "prepTime": 45,
            "responseTime": 60,
            "question": "Do you agree or disagree that the government should strictly restrict the use of disposable plastic products in cafes and supermarkets? Give specific reasons.",
            "questionKo": "정부가 카페와 대형 마트에서 일회용 플라스틱 제품의 사용을 엄격히 제한해야 한다는 의견에 동의하십니까?",
            "sentences": [
                {"step": "1. 서론 (찬성 입장)", "en": "I strongly agree that the government should strictly restrict the use of disposable plastic products.", "ko": "저는 정부가 일회용 플라스틱 제품의 사용을 엄격히 제한해야 한다는 의견에 강력히 동의합니다."},
                {"step": "2. 본론 1 (환경 오염 심각성)", "en": "First of all, plastic waste takes hundreds of years to break down and causes serious environmental pollution.", "ko": "무엇보다도 플라스틱 쓰레기는 분해되는 데 수백 년이 걸리며 심각한 환경 오염을 유발합니다."},
                {"step": "3. 본론 2 (강제 규제의 필요성)", "en": "Second, although many people know the importance of protecting the environment, they still use disposable cups out of habit.", "ko": "둘째, 많은 사람들이 환경 보호의 중요성을 알고 있음에도 불구하고 습관적으로 일회용 컵을 사용합니다."},
                {"step": "4. 본론 2 부연", "en": "However, strong government regulations encourage citizens to bring their own reusable tumblers and eco-bags.", "ko": "하지만 강력한 정부 규제는 시민들이 개인 다회용 텀블러와 에코백을 지참하도록 장려합니다."},
                {"step": "5. 개인 경험 예시", "en": "For example, after plastic bags were banned at supermarkets in Korea, carrying an eco-bag became a natural daily habit for everyone.", "ko": "예를 들어 한국 대형 마트에서 비닐봉지가 금지된 이후 에코백을 들고 다니는 것이 모두에게 자연스러운 일상 습관이 되었습니다."},
                {"step": "6. 결론 마무리", "en": "For these reasons, government restrictions are essential to protect our planet for future generations.", "ko": "이러한 이유로 미래 세대를 위해 지구를 보호하려면 정부의 규제가 필수적입니다."}
            ],
            "magicSentences": [
                {"en": "It reduces plastic waste and protects the environment.", "ko": "플라스틱 쓰레기를 줄이고 환경을 보호합니다.", "tip": "시계토끼 만능 #175 (환경 정책 찬성 1순위 문장)"},
                {"en": "It encourages citizens to use reusable tumblers and eco-bags.", "ko": "시민들이 다회용 텀블러와 에코백을 사용하도록 장려합니다.", "tip": "일회용품 규제 구체적 효과"}
            ],
            "vocabulary": [
                {"word": "restrict", "ipa": "[rɪˈstrɪkt]", "pos": "동사", "meaning": "제한하다, 규제하다"},
                {"word": "disposable", "ipa": "[dɪˈspoʊzəbl]", "pos": "형용사", "meaning": "일회용의"},
                {"word": "reusable", "ipa": "[ˌriːˈjuːzəbl]", "pos": "형용사", "meaning": "재사용 가능한, 다회용의"},
                {"word": "regulation", "ipa": "[ˌreɡjuˈleɪʃn]", "pos": "명사", "meaning": "규제, 법규"}
            ],
            "explanation": "환경 보호 및 정부 규제(Government regulation) 관련 파트 5 문제는 찬성(Agree) 입장을 취하고 '환경 오염 감소(reduce pollution)'와 '텀블러/에코백 사용 습관화(reusable tumblers and eco-bags)' 예시를 들면 만점 답변이 완성됩니다."
        },
        {
            "id": "p5-10",
            "part": 5,
            "qNum": "Part 5 - #10 (Q11)",
            "category": "채용·인사관리",
            "topic": "Hiring New College Graduates vs. Hiring Experienced Workers",
            "prepTime": 45,
            "responseTime": 60,
            "question": "When hiring new employees, do you think companies should prefer experienced workers or recent university graduates? Give specific reasons and examples.",
            "questionKo": "신규 직원을 채용할 때 기업이 경력직 근로자와 최근 대학 졸업자(신입) 중 어느 쪽을 더 선호해야 한다고 생각합니까?",
            "sentences": [
                {"step": "1. 서론 (경력직 선택)", "en": "When hiring new employees, I definitely think companies should prefer experienced workers over recent university graduates.", "ko": "신규 직원을 채용할 때 저는 기업이 최근 대학 졸업자보다 경력직 근로자를 확실히 더 선호해야 한다고 생각합니다."},
                {"step": "2. 본론 1 (교육 시간·비용 절감)", "en": "First of all, experienced workers already have practical skills and industry knowledge, so the company can save time and money on training.", "ko": "무엇보다도 경력직 근로자들은 이미 실무 기술과 업계 지식을 갖추고 있어서 회사가 교육에 드는 시간과 비용을 절약할 수 있습니다."},
                {"step": "3. 본론 1 부연", "en": "They can adapt to the new workplace immediately and start contributing to projects right away.", "ko": "그들은 새로운 직장에 즉시 적응할 수 있고 프로젝트에 바로 기여하기 시작할 수 있습니다."},
                {"step": "4. 본론 2 (위기 대처 능력)", "en": "Second, based on their past experience, they can handle unexpected problems professionally without panicking.", "ko": "둘째, 과거 경험을 바탕으로 예상치 못한 문제들도 당황하지 않고 전문적으로 처리할 수 있습니다."},
                {"step": "5. 구체적 예시", "en": "For example, when our team hired an experienced marketer last year, she immediately solved a client issue and boosted our team's performance.", "ko": "예를 들어 작년에 저희 팀이 경력직 마케터를 채용했을 때 그녀는 즉시 고객사 문제를 해결하고 팀 성과를 끌어올렸습니다."},
                {"step": "6. 결론 마무리", "en": "Therefore, hiring experienced workers is much more advantageous for a company's growth.", "ko": "따라서 경력직 근로자를 채용하는 것이 기업의 성장에 훨씬 더 유리합니다."}
            ],
            "magicSentences": [
                {"en": "The company can save a lot of time and money on training.", "ko": "회사가 교육에 드는 많은 시간과 비용을 아낄 수 있습니다.", "tip": "시계토끼 만능 #153 (경력직 채용 찬성 핵심 문장)"},
                {"en": "They can adapt to the workplace immediately and handle problems professionally.", "ko": "직장에 즉시 적응하고 문제를 전문적으로 처리할 수 있습니다.", "tip": "시계토끼 만능 #154 (실무 적응력 강조)"}
            ],
            "vocabulary": [
                {"word": "experienced workers", "ipa": "[ɪkˈspɪriənst ˈwɜːrkərz]", "pos": "명사구", "meaning": "경력직 근로자들"},
                {"word": "practical skills", "ipa": "[ˈpræktɪkl skɪlz]", "pos": "명사구", "meaning": "실무 기술"},
                {"word": "adapt to", "ipa": "[əˈdæpt tuː]", "pos": "숙어", "meaning": "~에 적응하다"},
                {"word": "advantageous", "ipa": "[ˌædvənˈteɪdʒəs]", "pos": "형용사", "meaning": "유리한, 이로운"}
            ],
            "explanation": "경력직(Experienced workers) vs 신입(New graduates) 비교 문제는 경력직을 선택하면 1) 교육 시간·비용 절감(save time and money on training) + 2) 즉시 실무 투입 및 문제 해결(adapt immediately & solve problems) 논리로 60초를 막힘없이 말할 수 있습니다."
        }
    ]


def main():
    p1 = build_part1()
    p2 = build_part2()
    p3 = build_part3()
    p4_sets = build_part4()
    p5 = build_part5()

    total_p4_questions = sum(len(s["questions"]) for s in p4_sets)

    master = {
        "title": "2025~2026 토익스피킹 파트별 기출 마스터 (Apple Glassmorphic Edition)",
        "counts": {
            "part1": len(p1),
            "part2": len(p2),
            "part3": len(p3),
            "part4_sets": len(p4_sets),
            "part4_questions": total_p4_questions,
            "part5": len(p5),
            "totalQuestions": len(p1) + len(p2) + len(p3) + total_p4_questions + len(p5)
        },
        "part3Types": [
            {"id": "ALL", "name": "전체 유형 (25문항)"},
            {"id": "p3-t1", "name": "유형 1: 시점·최근 경험 (5문항)"},
            {"id": "p3-t2", "name": "유형 2: 빈도·장소·동행인 (5문항)"},
            {"id": "p3-t3", "name": "유형 3: 양자택일 선호도·찬반 (5문항)"},
            {"id": "p3-t4", "name": "유형 4: 3자택일 최적 선택 (5문항)"},
            {"id": "p3-t5", "name": "유형 5: 장단점·중요 이유 (5문항)"}
        ],
        "part4TableTypes": [
            {"id": "ALL", "name": "전체 표 속성 (5개 세트)"},
            {"id": "table-conf", "name": "컨퍼런스·학술 심포지엄 일정표"},
            {"id": "table-museum", "name": "박물관 전시·문화 강연 일정표"},
            {"id": "table-training", "name": "사내 직원 연수·워크숍 일정표"},
            {"id": "table-tour", "name": "여행·시티 투어 여정표"},
            {"id": "table-interview", "name": "인사 채용 면접·이력서 요약표"}
        ],
        "part1": p1,
        "part2": p2,
        "part3": p3,
        "part4": p4_sets,
        "part5": p5
    }

    out_path = ROOT / "data" / "toeic_parts_master.json"
    out_path.write_text(json.dumps(master, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 파트별 마스터 데이터셋 생성 완료: {out_path}")
    print(f"   - Part 1: {len(p1)}문항")
    print(f"   - Part 2: {len(p2)}문항 (고화질 사진 내장)")
    print(f"   - Part 3: {len(p3)}문항 (5개 유형 × 5문제)")
    print(f"   - Part 4: {len(p4_sets)}개 표 세트 (총 {total_p4_questions}문제 엮음)")
    print(f"   - Part 5: {len(p5)}문항")
    print(f"   - 총 기출 문항 수: {master['counts']['totalQuestions']}문항")


if __name__ == "__main__":
    main()
