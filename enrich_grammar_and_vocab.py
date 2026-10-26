import json
import re

print("Enriching data.json with Grammar Points & Combined (Question + Answer) Vocabulary...")

with open('data.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

# Helper function to generate grammar explanations based on question & answer pattern
def generate_p3_grammar_points(q_text, a_text, q_num, topic):
    points = []
    
    # 1. 'The last time ~ was [about] ~' Pattern
    if "last time" in q_text.lower():
        points.append({
            "title": "구문 핵심: 'The last time S+V was ~'의 주어-동사 구조",
            "explanation": "‘The last time I ~’ 전체가 문장의 주어(명사구) 역할을 하므로, 뒤에 반드시 본동사 'was'가 와야 완전한 문장이 됩니다. 'about'은 전치사가 아니라 '대략, 약'을 뜻하는 부사이므로, 'was about two weeks ago'처럼 was 뒤에 부사 about과 시간 표현이 이어지는 구조입니다. (was를 빠뜨리고 바로 about을 쓰면 동사가 없어 감점됩니다.)"
        })
        points.append({
            "title": "시제 일치: 과거 의문문에 대한 과거형 답변",
            "explanation": "질문에서 'When was the last time ~' 및 'what did you ~'로 과거 시제를 물었으므로, 답변의 동사도 현재형이 아닌 과거형(bought, visited, went 등)과 was로 일치시켜야 합니다."
        })
    elif "do you usually" in q_text.lower() or "how often" in q_text.lower():
        points.append({
            "title": "빈도부사의 어순 & 현재 시제 사용",
            "explanation": "평소 습관을 묻는 질문이므로 현재 시제를 사용하며, 빈도부사(usually, often, always)는 일반동사 앞, be동사/조동사 뒤에 위치합니다. (예: I usually read ~, I often go ~)"
        })
        points.append({
            "title": "접속사 because vs so의 올바른 연결",
            "explanation": "'I do this because S+V' (원인 제시) 또는 'It is faster, so I can save time' (원인, so + 결과) 형태로 문장을 매끄럽게 연결하여 복문을 구사하면 130~140점 채점 기준인 '문장 확장력'에서 가산점을 받습니다."
        })
    elif "which" in q_text.lower() or "if you" in q_text.lower() or "prefer" in q_text.lower() or q_num in ["Question 7", "Q7"]:
        points.append({
            "title": "가정법 및 선호도 표현의 시제 일치 (If I had to ~ I would ~)",
            "explanation": "가정 상황을 묻는 질문('If you had to ~')에 답할 때는 조건절에 과거동사(had to/could), 주절에 'I would choose / I would prefer' (조동사 과거형 would + 동사원형) 구조를 맞춰주는 것이 정석입니다."
        })
        points.append({
            "title": "이유 제시 시 First of all, Also, Finally 담화표지어 활용",
            "explanation": "두 가지 이상의 이유를 말할 때 First of all(우선), Also(또한), Therefore(그러므로)와 같은 담화표지어(Discourse Markers)를 첫머리에 사용하면 논리적 흐름이 명확해져 채점관에게 높은 전달력을 줍니다."
        })
    elif "what are the advantages" in q_text.lower() or "important" in q_text.lower():
        points.append({
            "title": "명사절 보어 및 형용사 보어 구조",
            "explanation": "'The most important factor is [명사구/that절]' 구조를 사용하여 질문의 키워드를 주어로 받아치고, be동사 is 뒤에 핵심 이유를 보어로 제시하는 깔끔한 2형식 문장 구조입니다."
        })
    else:
        points.append({
            "title": "질문 키워드를 활용한 능동적 주어 전환",
            "explanation": "질문의 단어를 그대로 활용하여 답변의 주어로 삼으면 어색한 침묵 없이 즉시 발화를 시작할 수 있으며, 주어-동사의 수일치(단수/복수)를 정확하게 유지하는 것이 핵심입니다."
        })

    # Add general sentence combination point if needed
    if len(points) < 2:
        points.append({
            "title": "원인과 결과의 so 구문 활용",
            "explanation": "'[이유], so I can [결과]' 형태로 연결하여 짧은 단문 두 개를 자연스러운 중문으로 완성합니다."
        })

    return points

def generate_p4_grammar_points(q_text, a_text, q_num):
    points = []
    
    if "q9" in q_num.lower() or "question 9" in q_num.lower():
        points.append({
            "title": "오류 정정 구문: 'No, I'm afraid that you have the wrong information.'",
            "explanation": "'I'm afraid (that) S+V'는 유감스럽거나 상대방의 잘못을 정중하게 지적할 때 쓰는 관용적 공손 표현입니다. that절 이하에 완벽한 평서문이 오며, 접속사 that은 구어체에서 자주 생략됩니다."
        })
        points.append({
            "title": "올바른 정보 전달: 부사 Actually와 미래/수동태 시제",
            "explanation": "정정 문장은 'Actually(사실은)'라는 연결부사로 시작하고, 행사 시작은 'will start at [시간]' (능동) 또는 'is scheduled for [시간]' (수동/예정)으로 표현하여 시간의 전치사 at과 결합합니다."
        })
    elif "q10" in q_num.lower() or "question 10" in q_num.lower():
        points.append({
            "title": "존재 구문 유도부사 There is vs There are 수일치",
            "explanation": "뒤에 오는 명사가 복수(two sessions, two lectures)이므로 유도부사 There 뒤에 복수 be동사 'are'를 사용해야 합니다. (There are two scheduled sessions ~)"
        })
        points.append({
            "title": "시간 범위 표현: 'from [시작] to [종료]' 전치사구",
            "explanation": "일정표의 시간대를 말할 때는 전치사 from A to B 구조를 사용하며, 강연자를 소개할 때는 'presented by [이름]' (과거분사 수식) 또는 '[이름] will give a lecture' 형태로 주어-동사를 연결합니다."
        })
    else: # Q8
        points.append({
            "title": "행사 개최 수동태 구문: 'will be held on [날짜] at [장소]'",
            "explanation": "행사나 회의가 '개최되다'를 표현할 때는 수동태인 'will be held'를 쓰며, 날짜/요일 앞에는 전치사 on, 구체적 장소/시각 앞에는 at을 구분하여 사용하는 것이 토익스피킹 파트 4의 핵심 문법 포인트입니다."
        })
        points.append({
            "title": "금액 및 비용 표현: 'The registration fee is [금액]'",
            "explanation": "비용을 묻는 질문에는 주어를 'The fee / The cost'로 잡고 be동사 is 뒤에 금액을 붙이거나, 무료일 때는 'Admission is free (of charge)'로 표현합니다."
        })

    return points

# Enrich Part 3 Questions
for q in master.get("part3", []):
    # Normalize ID fields
    s_id = q.get("setNumber") or q.get("setId") or 1
    q["setId"] = s_id
    q["setNumber"] = s_id
    q_num = q.get("questionNumber") or q.get("qNumber") or "Question 5"
    q["qNumber"] = q_num
    q["questionNumber"] = q_num
    
    # Generate Grammar Points
    q["grammarPoints"] = generate_p3_grammar_points(q["question"], q["answer"], q_num, q.get("setTitle", ""))
    
    # Enhance Vocabulary to include Question Words + Answer Words
    existing_vocab = q.get("vocabulary", [])
    # Mark existing as Answer vocab if not already tagged
    for v in existing_vocab:
        if "source" not in v:
            v["source"] = "답변 핵심"
            
    # Add Question Keywords based on question text
    q_words = []
    q_lower = q["question"].lower()
    
    if "online" in q_lower and not any(v["word"] == "online" for v in existing_vocab):
        q_words.append({"word": "online", "ipa": "[ˌɒnˈlaɪn]", "pos": "형용사/부사", "meaning": "온라인의, 인터넷상의", "source": "문제 필수"})
    if "last time" in q_lower and not any("last time" in v["word"] for v in existing_vocab):
        q_words.append({"word": "the last time", "ipa": "[ðə lɑːst taɪm]", "pos": "명사구", "meaning": "마지막으로 ~한 때", "source": "문제 필수"})
    if "customer review" in q_lower and not any("review" in v["word"] for v in existing_vocab):
        q_words.append({"word": "customer review", "ipa": "[ˈkʌstəmər rɪˈvjuː]", "pos": "명사구", "meaning": "고객 이용 후기, 리뷰", "source": "문제 필수"})
    if "recommend" in q_lower and not any("recommend" in v["word"] for v in existing_vocab):
        q_words.append({"word": "recommend", "ipa": "[ˌrekəˈmend]", "pos": "동사", "meaning": "추천하다", "source": "문제 필수"})
    if "consider" in q_lower and not any("consider" in v["word"] for v in existing_vocab):
        q_words.append({"word": "consider", "ipa": "[kənˈsɪdə(r)]", "pos": "동사", "meaning": "고려하다, 감안하다", "source": "문제 필수"})
    if "prefer" in q_lower and not any("prefer" in v["word"] for v in existing_vocab):
        q_words.append({"word": "prefer", "ipa": "[prɪˈfɜː(r)]", "pos": "동사", "meaning": "선호하다, 더 좋아하다", "source": "문제 필수"})
    if "advantage" in q_lower and not any("advantage" in v["word"] for v in existing_vocab):
        q_words.append({"word": "advantage", "ipa": "[ədˈvɑːntɪdʒ]", "pos": "명사", "meaning": "장점, 유리한 점", "source": "문제 필수"})
    if "feature" in q_lower and not any("feature" in v["word"] for v in existing_vocab):
        q_words.append({"word": "feature", "ipa": "[ˈfiːtʃə(r)]", "pos": "명사", "meaning": "특징, 기능", "source": "문제 필수"})
    if "routine" in q_lower and not any("routine" in v["word"] for v in existing_vocab):
        q_words.append({"word": "daily routine", "ipa": "[ˈdeɪli ruːˈtiːn]", "pos": "명사구", "meaning": "일상적인 일과", "source": "문제 필수"})
    if "frequently" in q_lower and not any("frequently" in v["word"] for v in existing_vocab):
        q_words.append({"word": "frequently", "ipa": "[ˈfriːkwəntli]", "pos": "부사", "meaning": "자주, 빈번하게", "source": "문제 필수"})
    if "dessert" in q_lower and not any("dessert" in v["word"] for v in existing_vocab):
        q_words.append({"word": "dessert", "ipa": "[dɪˈzɜːt]", "pos": "명사", "meaning": "디저트, 후식", "source": "문제 필수"})
    if "public transportation" in q_lower and not any("transportation" in v["word"] for v in existing_vocab):
        q_words.append({"word": "public transportation", "ipa": "[ˌpʌblɪk ˌtrænspɔːˈteɪʃn]", "pos": "명사구", "meaning": "대중교통", "source": "문제 필수"})
        
    q["vocabulary"] = q_words + existing_vocab

# Enrich Part 4 Questions
for s in master.get("part4", []):
    s_num = s.get("setNumber", 1)
    for q in s.get("questions", []):
        q_num = q.get("qNumber") or q.get("questionNumber") or "Question 8"
        q["qNumber"] = q_num
        q["grammarPoints"] = generate_p4_grammar_points(q["question"], q["answer"], q_num)
        
        # Tag existing vocab as Answer vocab
        existing_vocab = q.get("vocabulary", [])
        for v in existing_vocab:
            if "source" not in v:
                v["source"] = "답변 핵심"
                
        # Extract Question Keywords
        q_words = []
        q_lower = q["question"].lower()
        if "scheduled" in q_lower and not any("schedule" in v["word"] for v in existing_vocab):
            q_words.append({"word": "scheduled", "ipa": "[ˈskedʒuːld]", "pos": "형용사", "meaning": "예정된, 일정에 잡힌", "source": "문제 필수"})
        if "correct" in q_lower and not any("correct" in v["word"] for v in existing_vocab):
            q_words.append({"word": "correct", "ipa": "[kəˈrekt]", "pos": "형용사", "meaning": "정확한, 올바른", "source": "문제 필수"})
        if "remember" in q_lower and not any("remember" in v["word"] for v in existing_vocab):
            q_words.append({"word": "if I remember correctly", "ipa": "[ɪf aɪ rɪˈmembə(r) kəˈrektli]", "pos": "관용구", "meaning": "내가 제대로 기억한다면", "source": "문제 필수"})
        if "detail" in q_lower and not any("detail" in v["word"] for v in existing_vocab):
            q_words.append({"word": "details", "ipa": "[ˈdiːteɪlz]", "pos": "명사", "meaning": "세부 사항, 정보", "source": "문제 필수"})
        if "location" in q_lower and not any("location" in v["word"] for v in existing_vocab):
            q_words.append({"word": "location", "ipa": "[ləʊˈkeɪʃn]", "pos": "명사", "meaning": "장소, 위치", "source": "문제 필수"})
        if "fee" in q_lower and not any("fee" in v["word"] for v in existing_vocab):
            q_words.append({"word": "registration fee", "ipa": "[ˌredʒɪˈstreɪʃn fiː]", "pos": "명사구", "meaning": "등록비, 참가비", "source": "문제 필수"})

        q["vocabulary"] = q_words + existing_vocab

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print("Successfully enriched data.json with Grammar Points & Question Vocabularies!")
