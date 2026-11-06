#!/usr/bin/env python3
"""
scripts/extract_youtube_toeic.py
유튜브 영상 자막 및 타임스탬프를 추출하여 토익스피킹 문제 데이터(data/toeic_data.json)로 변환하는 스크립트.

사용법:
    python3 scripts/extract_youtube_toeic.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
    python3 scripts/extract_youtube_toeic.py --sample  # 샘플 데이터 생성 및 검증
"""

import argparse
import json
import os
import re
import sys
from urllib.parse import parse_qs, urlparse

# 파트별 기본 시간 설정 (초 단위)
PART_DEFAULT_TIMES = {
    1: {"prep_time": 45, "response_time": 45},  # 지문 읽기
    2: {"prep_time": 45, "response_time": 30},  # 사진 묘사
    3: {"prep_time": 3, "response_time": 15},   # 일상 질문
    4: {"prep_time": 3, "response_time": 15},   # 정보 보고 답하기
    5: {"prep_time": 45, "response_time": 60},  # 의견 제시
}


def extract_video_id(url: str) -> str:
    """유튜브 URL에서 비디오 ID를 추출합니다."""
    parsed = urlparse(url)
    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        if parsed.path == "/watch":
            qs = parse_qs(parsed.query)
            return qs.get("v", [""])[0]
        elif parsed.path.startswith(("/embed/", "/v/")):
            return parsed.path.split("/")[2]
    elif parsed.hostname in ("youtu.be", "www.youtu.be"):
        return parsed.path.lstrip("/")
    # 이미 ID만 전달된 경우 처리
    if re.match(r"^[a-zA-Z0-9_-]{11}$", url):
        return url
    return ""


def get_transcript(video_id: str, languages=("ko", "en")):
    """youtube_transcript_api를 사용해 자막을 가져옵니다."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        return YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    except ImportError:
        print("[안내] youtube_transcript_api 라이브러리가 설치되어 있지 않습니다.", file=sys.stderr)
        print("  필요 시 실행: pip install youtube_transcript_api", file=sys.stderr)
        return None
    except Exception as e:
        print(f"[경고] 자막 추출 실패 ({video_id}): {e}", file=sys.stderr)
        return None


def parse_transcript_to_questions(transcript_items, default_part=1):
    """자막 목록을 토익스피킹 문제 항목으로 클러스터링합니다."""
    questions = []
    current_q = None

    # 'Question 1', 'Part 1', 'Q1' 등의 패턴 감지
    q_pattern = re.compile(r"(?:Question|Part|Q)\s*(\d+)", re.IGNORECASE)

    for item in transcript_items:
        text = item.get("text", "").strip()
        start = int(item.get("start", 0))

        match = q_pattern.search(text)
        if match:
            q_num = int(match.group(1))
            # 파트 추정
            part = default_part
            if q_num in (1, 2):
                part = 1
            elif q_num in (3, 4):
                part = 2
            elif q_num in (5, 6, 7):
                part = 3
            elif q_num in (8, 9, 10):
                part = 4
            elif q_num >= 11:
                part = 5

            times = PART_DEFAULT_TIMES.get(part, {"prep_time": 45, "response_time": 45})

            current_q = {
                "part": part,
                "question_text": text,
                "prep_time": times["prep_time"],
                "response_time": times["response_time"],
                "model_answer": "",
                "youtube_timestamp": start,
            }
            questions.append(current_q)
        elif current_q is not None:
            # 질문 뒤에 이어지는 문장들을 모범답안 또는 지문으로 추가
            if not current_q["model_answer"]:
                current_q["model_answer"] = text
            else:
                current_q["model_answer"] += " " + text

    return questions


def generate_sample_data():
    """테스트 및 초기 구동용 토익스피킹 샘플 데이터를 생성합니다."""
    return [
        {
            "part": 1,
            "question_text": "Attention all passengers waiting for Flight 302 to Chicago. Due to severe weather conditions in the Midwest, your departure has been delayed by approximately 45 minutes. Please remain in the gate area and listen for further announcements.",
            "prep_time": 45,
            "response_time": 45,
            "model_answer": "Attention all passengers waiting for Flight 302 to Chicago. Due to severe weather conditions in the Midwest, your departure has been delayed by approximately 45 minutes. Please remain in the gate area and listen for further announcements.",
            "youtube_timestamp": 15,
        },
        {
            "part": 2,
            "question_text": "Describe a picture: An outdoor coffee shop patio on a sunny afternoon.",
            "prep_time": 45,
            "response_time": 30,
            "model_answer": "This picture was taken outdoors at a busy cafe patio. In the foreground, two people are sitting at a wooden table enjoying iced coffee. In the background, green trees and pedestrians walking along the sidewalk can be seen.",
            "youtube_timestamp": 125,
        },
        {
            "part": 3,
            "question_text": "When was the last time you bought clothes online, and what did you buy?",
            "prep_time": 3,
            "response_time": 15,
            "model_answer": "The last time I bought clothes online was last week, and I bought a black cotton T-shirt. It was very convenient and saved me a lot of time.",
            "youtube_timestamp": 240,
        },
        {
            "part": 3,
            "question_text": "Do you prefer shopping for clothes alone or with friends? Why?",
            "prep_time": 3,
            "response_time": 30,
            "model_answer": "I definitely prefer shopping for clothes alone. When I shop alone, I can take my time and choose whatever I like without feeling rushed or distracted by others.",
            "youtube_timestamp": 310,
        },
        {
            "part": 4,
            "question_text": "Could you tell me what time the keynote speech starts and who the speaker is?",
            "prep_time": 3,
            "response_time": 15,
            "model_answer": "According to the schedule, the keynote speech will start at 9:00 AM in Room 101, and it will be delivered by Dr. Sarah Jenkins.",
            "youtube_timestamp": 450,
        },
        {
            "part": 5,
            "question_text": "Do you agree or disagree with the following statement? Working from home is more productive than working in a traditional office. Give reasons and examples.",
            "prep_time": 45,
            "response_time": 60,
            "model_answer": "I strongly agree that working from home is more productive. First, employees do not need to spend hours commuting in heavy traffic, which reduces fatigue. Second, a quiet home environment allows workers to concentrate deeply on their tasks without office noise.",
            "youtube_timestamp": 600,
        },
    ]


def main():
    parser = argparse.ArgumentParser(description="유튜브 영상에서 토익스피킹 문제 데이터 추출")
    parser.add_argument("--url", type=str, help="유튜브 영상 URL 또는 비디오 ID")
    parser.add_argument("--output", type=str, default="data/toeic_data.json", help="출력 JSON 파일 경로")
    parser.add_argument("--sample", action="store_true", help="표준 샘플 데이터 세트 생성")
    parser.add_argument("--part", type=int, default=1, choices=[1, 2, 3, 4, 5], help="기본 파트 번호")

    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    if args.sample or not args.url:
        print("[정보] 샘플 토익스피킹 데이터를 생성합니다.")
        data = generate_sample_data()
    else:
        video_id = extract_video_id(args.url)
        if not video_id:
            print(f"[오류] 유효한 유튜브 URL/ID를 파싱할 수 없습니다: {args.url}", file=sys.stderr)
            sys.exit(1)

        print(f"[정보] 비디오 ID '{video_id}' 자막 추출 시도 중...")
        transcript = get_transcript(video_id)
        if transcript:
            data = parse_transcript_to_questions(transcript, default_part=args.part)
            if not data:
                print("[경고] 자막에서 문항 구조를 자동 감지하지 못해 타임스탬프 원본 기반으로 생성합니다.")
                # 자막 첫 몇 개를 묶어서 생성
                data = [
                    {
                        "part": args.part,
                        "question_text": " ".join(t["text"] for t in transcript[:5]),
                        "prep_time": PART_DEFAULT_TIMES[args.part]["prep_time"],
                        "response_time": PART_DEFAULT_TIMES[args.part]["response_time"],
                        "model_answer": " ".join(t["text"] for t in transcript[5:15]),
                        "youtube_timestamp": int(transcript[0]["start"]) if transcript else 0,
                    }
                ]
        else:
            print("[안내] 자막 추출이 불가하여 표준 템플릿 데이터를 저장합니다.")
            data = generate_sample_data()

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 성공: 총 {len(data)}개 문항이 '{args.output}'에 저장되었습니다.")


if __name__ == "__main__":
    main()

