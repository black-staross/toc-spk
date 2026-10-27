import json
import re

print("Integrating 26 Real Exam Base64 Photos into data.json...")

with open('toeic_speaking_part2_with_base64_images.json', 'r', encoding='utf-8') as f:
    source_p2 = json.load(f)

with open('data.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

raw_questions = source_p2.get('photo_questions', [])

# Helper for grammar points
def generate_p2_grammar(sample_answer, location):
    points = []
    points.append({
        "title": "사진 묘사 1단계: 장소 도입 구문 'This is a picture taken in/at ~'",
        "explanation": "'This is a picture taken in/at [장소]'는 시험장 0초 침묵을 방지하는 필수 공식입니다. 실내나 넓은 공간은 in, 특정 시설이나 상점은 at을 구분하여 사용합니다."
    })
    
    if "wearing" in sample_answer.lower():
        points.append({
            "title": "착용 상태 묘사: 현재진행형 'is wearing [의복/안경]'",
            "explanation": "이미 옷이나 안경을 착용하고 있는 상태는 반드시 'is/are wearing'을 쓰며, 동작을 나타내는 'put on'과 혼동하지 않아야 합니다."
        })
    elif "sitting" in sample_answer.lower() or "standing" in sample_answer.lower():
        points.append({
            "title": "자세 및 상태 묘사: 현재분사 'sitting at / standing in'",
            "explanation": "책상이나 테이블에 앉아 있을 때는 전치사 at('sitting at a desk/table'), 의자에 앉아 있을 때는 on('sitting on a chair')을 씁니다."
        })
    else:
        points.append({
            "title": "인물 동작 묘사: 현재진행형 (be + -ing)",
            "explanation": "사진 속 인물의 모든 동작은 'is typing, is talking, is looking'처럼 100% 현재진행형으로 표현하는 것이 토익스피킹 채점 기준의 절대 원칙입니다."
        })

    if "overall" in sample_answer.lower():
        points.append({
            "title": "마무리 총평 구문: 'Overall, it seems like S+V'",
            "explanation": "답변 마지막 3~5초에는 'Overall, it seems like they are busy working / having a good time'으로 전체적인 분위기를 한 문장으로 정리해 주면 전달력 점수가 크게 상승합니다."
        })
    else:
        points.append({
            "title": "사물 존재 표현: 유도부사 'There is / There are'",
            "explanation": "단수 사물은 'There is a computer', 복수 사물은 'There are many books'로 수일치를 정확히 지켜 표현합니다."
        })
        
    return points

# Helper for vocabulary
def generate_p2_vocab(q_data):
    answer = q_data.get("sample_answer", "")
    desc = q_data.get("photo_description_kr", "")
    vocab_list = []
    
    # Common TOEIC Part 2 Words with IPA & POS
    dict_db = {
        "office": ("ˈɒfɪs", "명사", "사무실"),
        "desk": ("desk", "명사", "책상"),
        "laptop": ("ˈlæptɒp", "명사", "노트북 컴퓨터"),
        "monitor": ("ˈmɒnɪtə(r)", "명사", "컴퓨터 모니터"),
        "glasses": ("ˈɡlɑːsɪz", "명사", "안경"),
        "sweater": ("ˈswetə(r)", "명사", "스웨터"),
        "type on": ("ˈtaɪp ɒn", "동사구", "~에 타이핑하다"),
        "keyboard": ("ˈkiːbɔːd", "명사", "키보드, 자판"),
        "smartphone": ("ˈsmɑːtfəʊn", "명사", "스마트폰"),
        "headphones": ("ˈhedfəʊnz", "명사", "헤드폰"),
        "potted plant": ("ˈpɒtɪd plɑːnt", "명사", "화분 식물"),
        "busy": ("ˈbɪzi", "형용사", "바쁜, 분주한"),
        "suit": ("suːt", "명사", "정장"),
        "discuss": ("dɪˈskʌs", "동사", "논의하다, 상의하다"),
        "document": ("ˈdɒkjumənt", "명사", "문서, 서류"),
        "lounge": ("laʊndʒ", "명사", "라운지, 휴게실"),
        "tablet": ("ˈtæblət", "명사", "태블릿 PC"),
        "presentation": ("ˌpreznˈteɪʃn", "명사", "발표, 프레젠테이션"),
        "whiteboard": ("ˈwaɪtbɔːd", "명사", "화이트보드"),
        "point at": ("pɔɪnt æt", "동사구", "~을 가리키다"),
        "brick wall": ("brɪk wɔːl", "명사구", "벽돌 벽"),
        "conversation": ("ˌkɒnvəˈseɪʃn", "명사", "대화"),
        "handout": ("ˈhændaʊt", "명사", "유인물, 프린트물"),
        "shelves": ("ʃelvz", "명사", "선반, 진열대"),
        "grocery": ("ˈɡrəʊsəri", "명사", "식료품"),
        "shopping cart": ("ˈʃɒpɪŋ kɑːt", "명사", "쇼핑카트"),
        "cashier": ("kæˈʃɪə(r)", "명사", "계산원, 계산대"),
        "counter": ("ˈkaʊntə(r)", "명사", "카운터, 계산대"),
        "overall": ("ˌəʊvərˈɔːl", "부사", "전반적으로"),
        "conference": ("ˈkɒnfərəns", "명사", "회의, 회담"),
        "customer": ("ˈkʌstəmə(r)", "명사", "고객, 손님"),
        "apron": ("ˈeɪprən", "명사", "앞치마"),
        "credit card": ("ˈkredɪt kɑːd", "명사", "신용카드"),
        "hand over": ("hænd ˈəʊvə(r)", "동사구", "건네주다")
    }

    ans_lower = answer.lower()
    for word, (ipa, pos, meaning) in dict_db.items():
        if word in ans_lower:
            vocab_list.append({
                "word": word,
                "ipa": f"[{ipa}]",
                "pos": pos,
                "meaning": meaning,
                "source": "답변 핵심"
            })
            if len(vocab_list) >= 4:
                break
                
    # Add a photo keyword
    loc = q_data.get("location", "photo")
    vocab_list.insert(0, {
        "word": loc.replace("an ", "").replace("a ", "").strip(),
        "ipa": "[장소 어휘]",
        "pos": "명사",
        "meaning": f"사진 촬영 장소 ({loc})",
        "source": "사진 필수"
    })
    
    return vocab_list[:5]

part2_integrated = []

for q in raw_questions:
    qid = q.get("q_id", 1)
    qnum_raw = q.get("question_num", f"Problem {qid:02d}")
    location = q.get("location", "the scene")
    desc_kr = q.get("photo_description_kr", "")
    
    # Extract short title from description
    short_title = desc_kr.split("]")[0].replace("[", "").strip() if "]" in desc_kr else location
    
    item = {
        "id": qid,
        "setNumber": qid,
        "setId": qid,
        "qNumber": f"Question 3 / 4 ({qnum_raw})",
        "questionNumber": f"Question 3 / 4 ({qnum_raw})",
        "setTitle": f"Set {qid}: {location.title()} ({short_title})",
        "prepTime": 45,
        "responseTime": 30,
        "question": "Describe the picture on your screen in as much detail as you can.",
        "questionTranslation": "화면에 보이는 사진을 가능한 한 자세하게 묘사하세요.",
        "photoDescriptionKr": desc_kr,
        "photoScene": {
            "category": location,
            "locationEn": f"in {location}",
            "tags": q.get("key_elements", [])[:4]
        },
        "imageUrl": q.get("image_data_uri", ""),
        "answer": q.get("sample_answer", ""),
        "answerTranslation": q.get("sample_answer_kr", ""),
        "magicSentences": q.get("applied_templates", []),
        "grammarPoints": generate_p2_grammar(q.get("sample_answer", ""), location),
        "vocabulary": generate_p2_vocab(q),
        "scoreTip": q.get("explanation", "만능문장 공식에 맞춰 차분하게 묘사하세요.")
    }
    part2_integrated.append(item)

master["part2"] = part2_integrated
master["metadata"]["part2_count"] = len(part2_integrated)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print(f"Successfully integrated {len(part2_integrated)} Real Exam Base64 Photos into data.json!")
