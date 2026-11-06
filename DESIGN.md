---
name: TOEIC Speaking CBT Master Trainer
description: ETS 토익스피킹 CBT 시험장 실무 인터페이스 및 린 디자인 시스템
colors:
  primary: "#1e3a8a"
  primary-hover: "#172554"
  accent-red: "#dc2626"
  accent-green: "#16a34a"
  accent-amber: "#d97706"
  neutral-bg: "#f1f5f9"
  neutral-surface: "#ffffff"
  neutral-border: "#cbd5e1"
  text-primary: "#0f172a"
  text-secondary: "#475569"
  text-muted: "#94a3b8"
typography:
  display:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: "1.875rem"
    fontWeight: 700
    lineHeight: 1.2
  headline:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.3
  title:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 600
    lineHeight: 1.4
  body:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  mono:
    fontFamily: "Inter, monospace"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1
rounded:
  none: "0px"
  sm: "4px"
  md: "6px"
  lg: "8px"
  full: "9999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  timer-bar:
    backgroundColor: "{colors.neutral-border}"
    height: "10px"
    rounded: "{rounded.full}"
  status-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "#ffffff"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  action-button:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.md}"
    padding: "8px 18px"
---

## Overview
실제 토익스피킹 CBT(Computer-Based Test) 시험장의 긴장감과 집중도를 살린 실무 중심 디자인 시스템입니다.
AI 특유의 엉성하고 장식적인 카드 그리드(Anti-Slop)를 지양하고, 수험생의 시선 동선(상단 상태/타이머 ➔ 중앙 지문/자료 ➔ 하단 녹음 상태 및 액션)에 최적화된 화면 구성을 지향합니다.

## Colors
- **Primary (`#1e3a8a`, Blue 900)**: 시험 안내 헤더, 상단 네비게이션 및 주요 제어 요소. 공신력 있고 차분한 시험 환경 조성.
- **Accent Red (`#dc2626`)**: 실전 녹음 중(RECORDING) 상태 인디케이터 및 긴급 카운트다운(마지막 3초) 강조.
- **Accent Green (`#16a34a`)**: 준비 시간(PREPARATION) 진행 및 완료 상태 표시.
- **Accent Amber (`#d97706`)**: 시스템 안내 및 주의 상태 알림.
- **Neutral Background (`#f1f5f9`, Slate 100)**: 눈의 피로를 최소화하는 차분한 CBT 모니터 톤.
- **Neutral Surface (`#ffffff`)**: 중앙 지문, 사진, 표 및 모범답안 표시 카드.
- **Neutral Border (`#cbd5e1`, Slate 300)**: 명확한 영역 구분을 위한 1px 헤어라인 테두리.

## Typography
- **기본 텍스트**: `Pretendard`, sans-serif (한국어와 영문 모두 균일하고 또렷한 가독성 보장)
- **타이머 / 카운트다운**: `Inter` / 고정폭(tabular-nums) 폰트 (초 단위 숫자가 바뀔 때 레이아웃 흔들림 방지)
- **질문 지문**: 1.25rem ~ 1.5rem, Semibold, 줄간격 1.5 (시험장에서 모니터를 보는 적정 가독 거리 반영)
- **모범답안 & 핵심 표현**: 1rem, Regular/Semibold, 주요 구문은 백그라운드 하이라이트(`bg-amber-100 text-amber-900`)

## Layout
- **3단 수직 구조 (Three-Tier CBT Layout)**:
  1. **Top Bar**: 파트 번호, 문항 인덱스, 모드 토글(실전 vs 연습), 준비/답변 진행 상태 라벨 및 실시간 프로그레스 게이지 바.
  2. **Center Stage**: 시험 문항 영역 (Part 1 지문, Part 2 이미지, Part 3 텍스트 질문, Part 4 데이터 표). 여백을 충분히 확보하여 시선 분산을 방지.
  3. **Bottom Control Bar**: 실시간 녹음 상태(MediaRecorder 연동), 마이크 볼륨 미터(선택), 이전/다음 네비게이션 및 모범답안 토글 버튼.
- **모달 및 피드백 뷰**: 답변 종료 후 하단 또는 중앙에 확장되어 모범답안, 자가 녹음 재생기, 원본 유튜브 싱크 컨트롤을 한눈에 제공.

## Elevation & Depth
- 과도한 드롭 섀도우(Drop Shadow) 배제.
- 절제된 1px 보더(`border border-slate-200`)와 최소한의 섀도우(`shadow-sm`)로 실제 데스크톱 테스트 클라이언트의 평면적이고 견고한 느낌 유지.

## Shapes
- CBT 시험 환경에 어울리는 정돈된 라운딩 (`rounded-md`: 6px ~ 8px).
- 알약형 뱃지(`rounded-full`): 녹음 중 깜빡임 인디케이터, 파트 라벨 등 상태 알림에만 제한적으로 사용.

## Components
- **CBT 타이머 바**: 전체 시간 대비 잔여 시간을 백분율로 채우며, 단계 전환(준비 ➔ 답변) 시 색상이 자연스럽게 전환됨.
- **녹음 인디케이터**: `MediaRecorder`가 활성화되면 붉은색 점이 은은하게 펄스(Blink) 애니메이션으로 작동하여 수험생이 녹음 여부를 즉시 인지.
- **오디오 플레이어**: 브라우저 표준 `<audio>` 기반 또는 커스텀 슬림 컨트롤러로 자가 녹음 음성을 즉시 재생/탐색 가능.
- **모범답안 하이라이트 박스**: 모범답안 내의 고득점 만능 표현과 연계 단어들을 명확히 시각화.

## Do's and Don'ts
- **DO**:
  - 숫자가 바뀌는 타이머에는 반드시 `tabular-nums` 또는 모노스페이스 서체를 적용해 너비 흔들림을 막을 것.
  - 외부 오디오 라이브러리 대신 순수 `Web Audio API`와 `MediaRecorder`를 활용해 종속성을 최소화할 것.
  - 실제 CBT 시험의 호흡(준비 시간 ➔ Beep음 ➔ 녹음 ➔ Beep음)을 정확히 지킬 것.
- **DON'T**:
  - 알록달록한 그라데이션, 화려한 글래스모피즘, 불필요한 3D 효과 등 집중을 해치는 장식을 넣지 말 것.
  - 마이크 권한 요청 실패 시 화면이 멈추지 않고 적절한 안내(Fallback)를 표시할 것.

