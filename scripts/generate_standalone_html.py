#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apple Website & iOS Liquid Glass 스타일 독립 실행형 HTML 빌더
(scripts/generate_standalone_html.py)

최신 개선 반영:
1. Part 2 사진 크기를 검은 레터박스 없이 카드 너비에 맞춰 큼직하고 시원하게 렌더링 (aspect-ratio & width 100%)
2. Part 2~5 모범답안 안에 '전체 답안 발음 토글(1.0x / 0.75x)' 내장 (외부 노출 제거)
3. 이전, 다음 버튼을 상단 우측에 고정(flex-shrink:0) + 스크롤 시에도 언제나 조작 가능한 플로팅 하단 글래스 컨트롤 바 제공
4. Part 4는 듣기 시험이므로 질문 지문은 처음에 숨기고 [질문 보기 ▼] 버튼으로 토글, 지문 안에는 한국어 해석도 함께 제공 (듣기 1.0x / 0.75x 먼저 수행 가능)
5. 실제 CBT 시험처럼 준비 시간 ➔ 삐(Beep) ➔ 답변 시간으로 초가 흐르는 실시간 디지털 타이머 & 프로그레스 바 내장 (Web Audio API Beep 지원)
6. 발음 말하는 중간에 언제든 멈출 수 있는 독립된 '정지' 버튼 배치 (배속 버튼 그룹, 헤더, 플로팅 바 어디서나 원클릭 정지)
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    master_data = json.loads((ROOT / "data" / "toeic_parts_master.json").read_text(encoding="utf-8"))
    magic_data = json.loads((ROOT / "data" / "magic_187_vocab.json").read_text(encoding="utf-8"))
    vocab_data = json.loads((ROOT / "data" / "toeic_essential_vocab.json").read_text(encoding="utf-8"))

    master_json_str = json.dumps(master_data, ensure_ascii=False)
    magic_json_str = json.dumps(magic_data, ensure_ascii=False)
    vocab_json_str = json.dumps(vocab_data, ensure_ascii=False)

    html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>TOEIC Speaking Master - Apple Glassmorphic Edition</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --apple-bg: #F5F5F7;
      --apple-card: rgba(255, 255, 255, 0.75);
      --apple-card-hover: rgba(255, 255, 255, 0.9);
      --apple-card-solid: #FFFFFF;
      --apple-border: rgba(255, 255, 255, 0.85);
      --apple-border-subtle: rgba(0, 0, 0, 0.08);
      --apple-border-strong: rgba(0, 0, 0, 0.16);
      --apple-text: #1D1D1F;
      --apple-text-secondary: #6E6E73;
      --apple-text-muted: #86868B;
      --apple-blue: #0071E3;
      --apple-blue-hover: #0077ED;
      --apple-blue-bg: rgba(0, 113, 227, 0.08);
      --apple-blue-border: rgba(0, 113, 227, 0.22);
      --apple-red: #FF3B30;
      --apple-red-bg: rgba(255, 59, 48, 0.08);
      --apple-red-border: rgba(255, 59, 48, 0.25);
      --apple-emerald: #34C759;
      --apple-emerald-bg: rgba(52, 199, 89, 0.1);
      --apple-amber: #FF9500;
      --apple-amber-bg: rgba(255, 149, 0, 0.1);
      --apple-shadow-sm: 0 2px 10px rgba(0, 0, 0, 0.03), 0 1px 2px rgba(0, 0, 0, 0.02);
      --apple-shadow-md: 0 12px 36px rgba(0, 0, 0, 0.06), 0 2px 6px rgba(0, 0, 0, 0.03);
      --apple-shadow-lg: 0 24px 60px rgba(0, 0, 0, 0.12), 0 4px 12px rgba(0, 0, 0, 0.04);
      --glass-blur: blur(28px) saturate(190%);
      --radius-sm: 10px;
      --radius-md: 16px;
      --radius-lg: 22px;
      --radius-pill: 9999px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Noto Sans KR", sans-serif;
      background: #EEF2F6;
      background-attachment: fixed;
      color: var(--apple-text);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    /* 5. 컴퓨터 & 태블릿에서도 모바일 앱 환경 사이트 레이아웃으로 완벽 고정 */
    .mobile-app-shell {
      width: 100%;
      max-width: 480px;
      min-height: 100vh;
      background: radial-gradient(circle at 15% 15%, #FFFFFF 0%, #F5F5F7 60%, #EBEBF0 100%);
      box-shadow: 0 0 50px rgba(0, 0, 0, 0.08);
      position: relative;
      display: flex;
      flex-direction: column;
      padding-bottom: 90px;
      margin: 0 auto;
      box-sizing: border-box;
    }
    body.dark .mobile-app-shell {
      background: #000000;
      box-shadow: 0 0 60px rgba(0, 0, 0, 0.75);
      border-left: 1px solid rgba(255, 255, 255, 0.08);
      border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* iOS 리퀴드 글래스 헤더 */
    .apple-header {
      position: sticky;
      top: 0;
      z-index: 100;
      width: 100%;
      background: rgba(255, 255, 255, 0.82);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border-bottom: 1px solid var(--apple-border-subtle);
      transition: background 0.3s ease;
    }

    .header-inner {
      width: 100%;
      max-width: 480px;
      margin: 0 auto;
      padding: 12px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      box-sizing: border-box;
    }

    /* 다크모드 테마 스타일 */
    body.dark {
      --apple-bg: #000000;
      --apple-bg-subtle: #121214;
      --apple-card-bg: rgba(28, 28, 30, 0.88);
      --apple-card-solid: #1C1C1E;
      --apple-card-inner: rgba(44, 44, 46, 0.75);
      --apple-border: rgba(255, 255, 255, 0.16);
      --apple-border-subtle: rgba(255, 255, 255, 0.1);
      --apple-text: #F5F5F7;
      --apple-text-secondary: #A1A1A6;
      --apple-text-muted: #86868B;
      --apple-blue: #0A84FF;
      --apple-blue-hover: #409CFF;
      --apple-blue-bg: rgba(10, 132, 255, 0.18);
      --apple-blue-border: rgba(10, 132, 255, 0.45);
      --apple-red: #FF453A;
      --apple-red-bg: rgba(255, 69, 58, 0.18);
      --apple-red-border: rgba(255, 69, 58, 0.45);
      --apple-emerald: #30D158;
      --apple-emerald-bg: rgba(48, 209, 88, 0.15);
      --apple-amber: #FF9F0A;
      --apple-amber-bg: rgba(255, 159, 10, 0.15);
      background: radial-gradient(circle at 15% 15%, #1C1C1E 0%, #0D0D0E 60%, #000000 100%) !important;
      background-attachment: fixed !important;
      color: #F5F5F7 !important;
    }
    body.dark .apple-header {
      background: rgba(20, 20, 22, 0.86) !important;
      border-bottom-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .apple-segmented-bar {
      background: rgba(20, 20, 22, 0.8) !important;
      border-bottom-color: rgba(255, 255, 255, 0.08) !important;
    }
    body.dark .segmented-control {
      background: rgba(255, 255, 255, 0.08) !important;
      border-color: rgba(255, 255, 255, 0.1) !important;
    }
    body.dark .segment-btn {
      color: #A1A1A6 !important;
    }
    body.dark .segment-btn:hover:not(.active) {
      color: #FFFFFF !important;
      background: rgba(255, 255, 255, 0.06) !important;
    }
    body.dark .segment-btn.active {
      background: rgba(255, 255, 255, 0.2) !important;
      color: #FFFFFF !important;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5) !important;
    }
    body.dark .segment-count {
      background: rgba(255, 255, 255, 0.12) !important;
      color: #E5E5EA !important;
    }
    body.dark .segment-btn.active .segment-count {
      background: #0A84FF !important;
      color: #FFFFFF !important;
    }
    body.dark .glass-card {
      background: rgba(28, 28, 30, 0.88) !important;
      border-color: rgba(255, 255, 255, 0.14) !important;
      box-shadow: 0 16px 48px rgba(0, 0, 0, 0.6) !important;
    }
    body.dark .glass-card-header {
      border-bottom-color: rgba(255, 255, 255, 0.1) !important;
    }
    body.dark .card-title {
      color: #FFFFFF !important;
    }

    /* 다크모드 Part 1 전체 지문 & 끊어 읽기 문장 */
    body.dark .p1-full-passage-card {
      background: rgba(38, 38, 42, 0.95) !important;
      border-color: rgba(255, 255, 255, 0.14) !important;
    }
    body.dark .p1-full-passage-text {
      color: #FFFFFF !important;
    }
    body.dark .sentence-item-card {
      background: rgba(44, 44, 48, 0.82) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
      color: #F5F5F7 !important;
    }
    body.dark .sentence-item-card:hover {
      border-color: rgba(10, 132, 255, 0.5) !important;
      background: rgba(52, 52, 56, 0.95) !important;
    }
    body.dark .sentence-step-badge {
      background: rgba(10, 132, 255, 0.22) !important;
      color: #64D2FF !important;
      border: 1px solid rgba(10, 132, 255, 0.4) !important;
    }
    body.dark .sentence-en-text {
      color: #FFFFFF !important;
    }
    body.dark .sentence-chunk-text {
      background: rgba(10, 132, 255, 0.16) !important;
      color: #64D2FF !important;
      border: 1px solid rgba(10, 132, 255, 0.3) !important;
    }
    body.dark .sentence-ko-text {
      color: #A1A1A6 !important;
    }

    /* 다크모드 질문 프롬프트 & 지문 */
    body.dark .question-prompt-card {
      background: rgba(38, 38, 42, 0.92) !important;
      border-color: rgba(255, 255, 255, 0.14) !important;
    }
    body.dark .prompt-tag-title {
      color: #A1A1A6 !important;
    }
    body.dark .question-prompt-en {
      color: #FFFFFF !important;
    }

    /* 다크모드 모범답안 토글 & 해석 배너 */
    body.dark .btn-toggle-answer {
      background: rgba(44, 44, 48, 0.9) !important;
      color: #F5F5F7 !important;
      border-color: rgba(255, 255, 255, 0.18) !important;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4) !important;
    }
    body.dark .btn-toggle-answer:hover {
      background: rgba(58, 58, 62, 1) !important;
      border-color: rgba(255, 255, 255, 0.3) !important;
      color: #FFFFFF !important;
    }
    body.dark .btn-toggle-answer.opened {
      background: rgba(10, 132, 255, 0.24) !important;
      color: #64D2FF !important;
      border-color: rgba(10, 132, 255, 0.5) !important;
    }
    body.dark .answer-collapse-box {
      border-top-color: rgba(255, 255, 255, 0.1) !important;
    }
    body.dark .question-translation-banner {
      background: rgba(255, 255, 255, 0.06) !important;
      border-left: 4px solid #0A84FF !important;
      color: #D1D1D6 !important;
    }
    body.dark .question-translation-banner strong {
      color: #64D2FF !important;
    }

    /* 다크모드 만능문장 카드 (Golden Formula) */
    body.dark .magic-sentence-card {
      background: rgba(255, 159, 10, 0.14) !important;
      border-color: rgba(255, 159, 10, 0.35) !important;
    }
    body.dark .magic-sentence-en {
      color: #FFD60A !important;
    }
    body.dark .magic-sentence-ko {
      color: #FFE680 !important;
    }
    body.dark .magic-sentence-tip {
      color: #FBBF24 !important;
    }

    /* 다크모드 핵심 어휘 카드 */
    body.dark .vocab-capsule-card {
      background: rgba(44, 44, 48, 0.8) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .vocab-capsule-card:hover {
      border-color: rgba(10, 132, 255, 0.45) !important;
      background: rgba(52, 52, 58, 0.95) !important;
    }
    body.dark .vocab-word-bold {
      color: #FFFFFF !important;
    }
    body.dark .vocab-ipa-subtle {
      color: #64D2FF !important;
    }
    body.dark .vocab-mean-subtle {
      color: #A1A1A6 !important;
    }

    /* 다크모드 해설 & 발음 팁 콜아웃 */
    body.dark .explanation-callout {
      background: rgba(48, 209, 88, 0.14) !important;
      border-color: rgba(48, 209, 88, 0.35) !important;
      color: #A7F3D0 !important;
    }
    body.dark .explanation-callout strong {
      color: #30D158 !important;
    }

    /* 다크모드 Part 4 표 & LC 카드 */
    body.dark .part4-table-card {
      background: #1C1C1E !important;
      border-color: rgba(255, 255, 255, 0.14) !important;
    }
    body.dark .table-top-banner {
      background: #2C2C2E !important;
      color: #FFFFFF !important;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .table-meta-pills {
      background: #242426 !important;
      border-color: rgba(255, 255, 255, 0.1) !important;
      color: #D1D1D6 !important;
    }
    body.dark .table-meta-pills strong {
      color: #FFFFFF !important;
    }
    body.dark .part4-clean-table th {
      background: #2A2A2D !important;
      color: #FFFFFF !important;
      border-bottom: 1px solid rgba(255, 255, 255, 0.15) !important;
    }
    body.dark .part4-clean-table td {
      background: #1C1C1E !important;
      color: #E5E5EA !important;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    body.dark .part4-clean-table td strong {
      color: #FFFFFF !important;
    }
    body.dark .part4-clean-table tbody tr:hover td {
      background: rgba(255, 255, 255, 0.05) !important;
    }
    body.dark .p4-lc-question-card {
      background: rgba(38, 38, 42, 0.88) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .btn-toggle-qtext {
      background: rgba(255, 255, 255, 0.08) !important;
      color: #F5F5F7 !important;
      border-color: rgba(255, 255, 255, 0.16) !important;
    }
    body.dark .btn-toggle-qtext:hover {
      background: rgba(255, 255, 255, 0.15) !important;
      color: #FFFFFF !important;
    }
    body.dark .btn-toggle-qtext.opened {
      background: rgba(10, 132, 255, 0.24) !important;
      color: #64D2FF !important;
      border-color: rgba(10, 132, 255, 0.5) !important;
    }
    body.dark .p4-qtext-collapse {
      background: rgba(10, 132, 255, 0.1) !important;
      border-color: rgba(10, 132, 255, 0.35) !important;
      color: #F5F5F7 !important;
    }

    /* 다크모드 CBT 타이머 */
    body.dark .cbt-timer-card {
      background: rgba(38, 38, 42, 0.88) !important;
      border-color: rgba(255, 255, 255, 0.14) !important;
    }
    body.dark .timer-digital-display {
      color: #FFFFFF !important;
      text-shadow: 0 0 14px rgba(255, 255, 255, 0.25) !important;
    }
    body.dark .timer-stage-badge.standby {
      background: rgba(255, 255, 255, 0.08) !important;
      color: #A1A1A6 !important;
      border-color: rgba(255, 255, 255, 0.14) !important;
    }
    body.dark .btn-timer-ctrl {
      background: rgba(58, 58, 62, 0.9) !important;
      color: #F5F5F7 !important;
      border-color: rgba(255, 255, 255, 0.18) !important;
    }
    body.dark .btn-timer-ctrl:hover {
      background: rgba(72, 72, 78, 1) !important;
      color: #FFFFFF !important;
    }
    body.dark .timer-progress-track {
      background: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .timer-info-caption {
      color: #A1A1A6 !important;
    }

    /* 다크모드 태그 & 네비게이션 */
    body.dark .tag-part {
      background: #2C2C2E !important;
      color: #FFFFFF !important;
      border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    body.dark .tag-time {
      background: rgba(255, 255, 255, 0.08) !important;
      color: #A1A1A6 !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .btn-circle-nav {
      background: rgba(44, 44, 48, 0.85) !important;
      color: #F5F5F7 !important;
      border-color: rgba(255, 255, 255, 0.16) !important;
    }
    body.dark .btn-circle-nav:hover:not(:disabled) {
      background: rgba(58, 58, 62, 1) !important;
      color: #FFFFFF !important;
      border-color: rgba(255, 255, 255, 0.28) !important;
    }
    body.dark .btn-qlist-toggle {
      background: rgba(44, 44, 48, 0.85) !important;
      color: #F5F5F7 !important;
      border-color: rgba(255, 255, 255, 0.16) !important;
    }
    body.dark .btn-qlist-toggle:hover {
      background: rgba(58, 58, 62, 1) !important;
      color: #FFFFFF !important;
    }
    body.dark .btn-vocab-toggle {
      background: rgba(10, 132, 255, 0.16) !important;
      border-color: rgba(10, 132, 255, 0.45) !important;
      color: #64D2FF !important;
    }
    body.dark .btn-vocab-toggle:hover {
      background: rgba(10, 132, 255, 0.28) !important;
      color: #FFFFFF !important;
    }
    body.dark .voice-badge {
      background: rgba(255, 255, 255, 0.08) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
      color: #D1D1D6 !important;
    }

    /* 다크모드 발음 선택형 칸 (Speech Selectable) */
    body.dark .speech-selectable {
      background: rgba(44, 44, 48, 0.65) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .speech-selectable:hover {
      border-color: rgba(10, 132, 255, 0.5) !important;
      background: rgba(10, 132, 255, 0.14) !important;
    }
    body.dark .speech-selectable.selected {
      border-color: #0A84FF !important;
      background: rgba(10, 132, 255, 0.25) !important;
      box-shadow: 0 0 0 2px rgba(10, 132, 255, 0.6), 0 8px 24px rgba(0, 0, 0, 0.5) !important;
    }

    /* 다크모드 하단 플로팅 바 & 컨트롤 */
    body.dark .floating-bottom-bar {
      background: rgba(24, 24, 26, 0.94) !important;
      border-color: rgba(255, 255, 255, 0.18) !important;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.7) !important;
    }
    body.dark .btn-floating-drawer {
      background: rgba(255, 255, 255, 0.08) !important;
      border-color: rgba(255, 255, 255, 0.14) !important;
      color: #F5F5F7 !important;
    }
    body.dark .btn-floating-drawer:hover {
      background: rgba(255, 255, 255, 0.16) !important;
      color: #FFFFFF !important;
    }
    body.dark .btn-floating-nav {
      color: #F5F5F7 !important;
    }
    body.dark .btn-floating-nav:hover:not(:disabled) {
      background: rgba(255, 255, 255, 0.1) !important;
      color: #FFFFFF !important;
    }
    body.dark .floating-nav-info {
      border-left-color: rgba(255, 255, 255, 0.14) !important;
      border-right-color: rgba(255, 255, 255, 0.14) !important;
      color: #D1D1D6 !important;
    }
    body.dark .btn-rate-capsule {
      background: rgba(10, 132, 255, 0.16) !important;
      border-color: rgba(10, 132, 255, 0.45) !important;
      color: #64D2FF !important;
    }
    body.dark .btn-rate-capsule:hover {
      background: rgba(10, 132, 255, 0.28) !important;
      color: #FFFFFF !important;
    }
    body.dark .btn-floating-rate {
      background: rgba(10, 132, 255, 0.18) !important;
      border-color: rgba(10, 132, 255, 0.45) !important;
      color: #64D2FF !important;
    }
    body.dark .btn-floating-rate:hover {
      background: #0A84FF !important;
      color: #FFFFFF !important;
    }
    body.dark .btn-header-stop,
    body.dark .btn-rate-stop,
    body.dark .btn-floating-stop {
      background: rgba(255, 69, 58, 0.18) !important;
      border-color: rgba(255, 69, 58, 0.45) !important;
      color: #FF453A !important;
    }
    body.dark .btn-header-stop:hover,
    body.dark .btn-rate-stop:hover,
    body.dark .btn-floating-stop:hover {
      background: rgba(255, 69, 58, 0.3) !important;
      color: #FFFFFF !important;
    }

    /* 다크모드 드로어 & 만능문장 모달 */
    body.dark .glass-drawer {
      background: rgba(24, 24, 26, 0.96) !important;
      border-right-color: rgba(255, 255, 255, 0.14) !important;
    }
    body.dark .drawer-header {
      border-bottom-color: rgba(255, 255, 255, 0.1) !important;
    }
    body.dark .drawer-title {
      color: #FFFFFF !important;
    }
    body.dark .btn-drawer-close {
      background: rgba(255, 255, 255, 0.1) !important;
      color: #F5F5F7 !important;
    }
    body.dark .drawer-q-item {
      background: rgba(44, 44, 48, 0.65) !important;
      border-color: rgba(255, 255, 255, 0.1) !important;
      color: #F5F5F7 !important;
    }
    body.dark .drawer-q-item:hover {
      background: rgba(58, 58, 62, 0.95) !important;
      color: #FFFFFF !important;
      border-color: rgba(255, 255, 255, 0.22) !important;
    }
    body.dark .drawer-q-item.active {
      background: rgba(10, 132, 255, 0.28) !important;
      border-color: #0A84FF !important;
    }
    body.dark .vocab-modal-window {
      background: rgba(24, 24, 26, 0.97) !important;
      border-color: rgba(255, 255, 255, 0.16) !important;
    }
    body.dark .vocab-modal-header {
      border-bottom-color: rgba(255, 255, 255, 0.1) !important;
    }
    body.dark .vocab-search-input {
      background: rgba(44, 44, 48, 0.85) !important;
      border-color: rgba(255, 255, 255, 0.18) !important;
      color: #F5F5F7 !important;
    }
    body.dark .vocab-item-card {
      background: rgba(44, 44, 48, 0.75) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .vocab-item-card.memorized {
      background: rgba(48, 209, 88, 0.16) !important;
      border-color: rgba(48, 209, 88, 0.45) !important;
    }
    body.dark .btn-mem-toggle {
      border-color: rgba(255, 255, 255, 0.25) !important;
      color: #D1D1D6 !important;
    }
    body.dark .btn-mem-toggle.checked {
      background: #30D158 !important;
      color: #000000 !important;
      font-weight: 700;
    }

    .brand-title-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* 3. 다크모드 버튼 (사진과 동일한 모던 스퀘어클 아이콘 버튼) */
    .btn-theme-toggle {
      width: 40px;
      height: 40px;
      border-radius: 14px;
      background: #F0F4F8;
      border: 1px solid rgba(0, 113, 227, 0.12);
      color: #1E293B;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0;
      flex-shrink: 0;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      user-select: none;
      -webkit-user-select: none;
    }
    .btn-theme-toggle:hover {
      background: #E4ECF4;
      border-color: rgba(0, 113, 227, 0.25);
      color: #0071E3;
      transform: scale(1.05);
    }
    .btn-theme-toggle:active {
      transform: scale(0.95);
    }
    body.dark .btn-theme-toggle {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.14);
      color: #FFD60A;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.25);
    }
    body.dark .btn-theme-toggle:hover {
      background: rgba(255, 255, 255, 0.16);
      border-color: rgba(255, 255, 255, 0.25);
      color: #FFE66D;
      transform: scale(1.05);
    }
    .btn-theme-toggle .icon-moon,
    .btn-theme-toggle .icon-sun {
      width: 20px;
      height: 20px;
      stroke-width: 2;
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease;
    }
    .btn-theme-toggle .icon-sun {
      display: none;
    }
    .btn-theme-toggle .icon-moon {
      display: block;
    }
    body.dark .btn-theme-toggle .icon-sun {
      display: block;
      animation: rotateSun 0.35s ease-out forwards;
    }
    body.dark .btn-theme-toggle .icon-moon {
      display: none;
    }
    @keyframes rotateSun {
      from { transform: rotate(-45deg) scale(0.8); opacity: 0; }
      to { transform: rotate(0deg) scale(1); opacity: 1; }
    }

    .brand-main-title {
      font-size: 18px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--apple-text);
    }

    /* 제목 옆 만능문장 187 토글 버튼 (이모티콘 없이 깔끔한 애플 캡슐) */
    .btn-vocab-toggle {
      background: rgba(0, 113, 227, 0.08);
      color: var(--apple-blue);
      border: 1px solid var(--apple-blue-border);
      border-radius: var(--radius-pill);
      padding: 7px 16px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
      user-select: none;
    }

    .btn-vocab-toggle:hover {
      background: var(--apple-blue);
      color: #FFFFFF;
      border-color: var(--apple-blue);
      box-shadow: 0 2px 8px rgba(0, 113, 227, 0.3);
      transform: translateY(-1px);
    }
    body.dark .btn-vocab-toggle {
      background: rgba(10, 132, 255, 0.15);
      color: #0A84FF;
      border-color: rgba(10, 132, 255, 0.3);
    }
    body.dark .btn-vocab-toggle:hover {
      background: #0A84FF;
      color: #FFFFFF;
      box-shadow: 0 2px 10px rgba(10, 132, 255, 0.45);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .voice-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 0, 0, 0.04);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-pill);
      padding: 5px 12px;
      font-size: 12px;
      font-weight: 600;
      color: var(--apple-text-secondary);
    }

    .voice-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--apple-emerald);
      box-shadow: 0 0 6px rgba(52, 199, 89, 0.6);
    }

    .btn-header-stop {
      background: var(--apple-red-bg);
      color: var(--apple-red);
      border: 1px solid var(--apple-red-border);
      border-radius: var(--radius-pill);
      padding: 6px 13px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.16s ease;
    }
    .btn-header-stop:hover {
      background: rgba(255, 59, 48, 0.16);
    }

    .btn-qlist-toggle {
      background: rgba(255, 255, 255, 0.9);
      color: var(--apple-text);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-pill);
      padding: 7px 15px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      box-shadow: var(--apple-shadow-sm);
      transition: all 0.2s ease;
    }

    .btn-qlist-toggle:hover {
      background: #FFFFFF;
      border-color: var(--apple-border-strong);
      transform: translateY(-1px);
    }

    /* iOS 세그먼트 컨트롤 탭 (모바일 뷰 고정) */
    .apple-segmented-bar {
      width: 100%;
      max-width: 480px;
      margin: 10px auto 0;
      padding: 0 12px;
      box-sizing: border-box;
    }

    .segmented-control {
      display: flex;
      background: rgba(0, 0, 0, 0.05);
      padding: 4px;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(0, 0, 0, 0.04);
      overflow-x: auto;
      gap: 4px;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }
    .segmented-control::-webkit-scrollbar {
      display: none;
    }

    .segment-btn {
      flex: 1;
      min-width: 82px;
      background: transparent;
      border: none;
      border-radius: var(--radius-pill);
      padding: 8px 12px;
      font-size: 13.5px;
      font-weight: 700;
      color: var(--apple-text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
      min-height: 38px;
    }

    .segment-btn:hover:not(.active) {
      color: var(--apple-text);
    }

    .segment-btn.active {
      background: #FFFFFF;
      color: var(--apple-text);
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0, 0, 0, 0.04);
    }

    .segment-count {
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: var(--radius-pill);
      background: rgba(0, 0, 0, 0.06);
      color: var(--apple-text-secondary);
    }

    .segment-btn.active .segment-count {
      background: var(--apple-blue-bg);
      color: var(--apple-blue);
    }

    /* 메인 뷰포트 레이아웃 (모바일 뷰 고정) */
    .main-viewport {
      width: 100%;
      max-width: 480px;
      margin: 14px auto 30px;
      padding: 0 12px;
      box-sizing: border-box;
    }

    /* 리퀴드 글래스 메인 카드 (모바일 최적화) */
    .glass-card {
      background: var(--apple-card);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--apple-border);
      border-radius: 20px;
      padding: 20px 16px;
      box-shadow: var(--apple-shadow-md);
      transition: border-color 0.2s ease;
      position: relative;
    }

    /* 3. 이전/다음 버튼 고정 헤더 */
    .glass-card-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 16px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--apple-border-subtle);
      margin-bottom: 24px;
    }

    .header-text-group {
      flex: 1;
      min-width: 0;
    }

    .card-meta-tags {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 8px;
    }

    .tag-pill {
      font-size: 12px;
      font-weight: 700;
      padding: 4px 11px;
      border-radius: var(--radius-pill);
      letter-spacing: -0.01em;
    }

    .tag-part {
      background: #1D1D1F;
      color: #FFFFFF;
    }

    .tag-category {
      background: var(--apple-blue-bg);
      color: var(--apple-blue);
      border: 1px solid var(--apple-blue-border);
    }

    .tag-time {
      background: rgba(0, 0, 0, 0.04);
      color: var(--apple-text-secondary);
      border: 1px solid var(--apple-border-subtle);
    }

    .card-title {
      font-size: 22px;
      font-weight: 700;
      letter-spacing: -0.025em;
      color: var(--apple-text);
      line-height: 1.35;
    }

    /* 3. 상단 우측 고정 네비게이션 버튼 (줄바꿈되지 않음) */
    .card-nav-controls {
      display: flex;
      gap: 8px;
      flex-shrink: 0;
      align-items: center;
    }

    .btn-circle-nav {
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-pill);
      padding: 8px 16px;
      font-size: 13px;
      font-weight: 600;
      color: var(--apple-text);
      cursor: pointer;
      box-shadow: var(--apple-shadow-sm);
      transition: all 0.18s ease;
      white-space: nowrap;
    }

    .btn-circle-nav:hover:not(:disabled) {
      background: #FFFFFF;
      border-color: var(--apple-border-strong);
      transform: translateY(-1px);
    }

    .btn-circle-nav:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }

    /* 5 & 6. 미니멀 배속 버튼 + 정지 버튼 */
    .rate-capsule-group {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      flex-shrink: 0;
    }

    .btn-rate-capsule {
      background: rgba(0, 113, 227, 0.08);
      color: var(--apple-blue);
      border: 1px solid var(--apple-blue-border);
      border-radius: var(--radius-pill);
      padding: 4px 11px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.16s ease;
      font-variant-numeric: tabular-nums;
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
    }

    .btn-rate-capsule:hover {
      background: rgba(0, 113, 227, 0.16);
      transform: scale(1.03);
    }

    .btn-rate-capsule.active-playing {
      background: var(--apple-blue);
      color: #FFFFFF;
      border-color: var(--apple-blue);
      box-shadow: 0 0 10px rgba(0, 113, 227, 0.4);
    }

    /* 6. 인라인 정지 버튼 */
    .btn-rate-stop {
      background: var(--apple-red-bg);
      color: var(--apple-red);
      border-color: var(--apple-red-border);
    }
    .btn-rate-stop:hover {
      background: rgba(255, 59, 48, 0.18);
    }

    /* 5. 실전 시험 타이머 (CBT Digital Timer) */
    .cbt-timer-card {
      background: rgba(255, 255, 255, 0.85);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      margin: 20px 0 24px;
      box-shadow: var(--apple-shadow-sm);
    }

    .timer-top-line {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 12px;
      margin-bottom: 10px;
      width: 100%;
    }

    .timer-stage-badge {
      justify-self: start;
      font-size: 12px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      letter-spacing: -0.01em;
      white-space: nowrap;
    }

    .timer-stage-badge.prep {
      background: var(--apple-blue-bg);
      color: var(--apple-blue);
      border: 1px solid var(--apple-blue-border);
    }

    .timer-stage-badge.response {
      background: var(--apple-red-bg);
      color: var(--apple-red);
      border: 1px solid var(--apple-red-border);
    }

    .timer-stage-badge.standby {
      background: rgba(0, 0, 0, 0.05);
      color: var(--apple-text-secondary);
      border: 1px solid var(--apple-border-subtle);
    }

    .timer-digital-display {
      justify-self: center;
      text-align: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 24px;
      font-weight: 700;
      color: var(--apple-text);
      font-variant-numeric: tabular-nums;
      letter-spacing: -0.02em;
    }

    .timer-btn-actions {
      justify-self: end;
      display: flex;
      gap: 6px;
      align-items: center;
    }

    .btn-timer-ctrl {
      background: #FFFFFF;
      border: 1px solid var(--apple-border-subtle);
      border-radius: 50%;
      width: 36px;
      height: 36px;
      min-width: 36px;
      padding: 0;
      font-size: 14px;
      font-weight: 700;
      color: var(--apple-text);
      cursor: pointer;
      box-shadow: var(--apple-shadow-sm);
      transition: all 0.16s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }
    .btn-timer-ctrl:hover {
      background: #F8F8FA;
      border-color: var(--apple-border-strong);
      transform: scale(1.06);
    }

    .timer-progress-track {
      height: 6px;
      background: rgba(0, 0, 0, 0.06);
      border-radius: var(--radius-pill);
      overflow: hidden;
      margin-bottom: 6px;
    }

    .timer-progress-fill {
      height: 100%;
      background: var(--apple-blue);
      border-radius: var(--radius-pill);
      transition: width 1s linear, background-color 0.3s ease;
    }

    .timer-info-caption {
      font-size: 12px;
      color: var(--apple-text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* 1. Part 2 사진 쇼케이스: 레터박스 없이 꽉 차게 큼직하게 렌더링 */
    .photo-display-full {
      width: 100%;
      border-radius: var(--radius-lg);
      overflow: hidden;
      margin-bottom: 26px;
      box-shadow: var(--apple-shadow-md);
      background: transparent;
      border: 1px solid var(--apple-border);
    }

    .photo-display-full img {
      width: 100%;
      height: auto;
      max-height: 640px;
      display: block;
      border-radius: var(--radius-lg);
      object-fit: cover;
    }

    /* 질문 프롬프트 카드 */
    .question-prompt-card {
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-md);
      padding: 22px 26px;
      margin-bottom: 24px;
      box-shadow: var(--apple-shadow-sm);
    }

    .question-prompt-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 10px;
    }

    .prompt-tag-title {
      font-size: 12px;
      font-weight: 700;
      color: var(--apple-text-secondary);
      letter-spacing: 0.04em;
    }

    .question-prompt-en {
      font-size: 18px;
      font-weight: 700;
      color: var(--apple-text);
      line-height: 1.45;
      letter-spacing: -0.015em;
    }

    /* 4. Part 4 LC 질문 카드: 질문 지문 숨김 토글 & 지문 내 해석 */
    .p4-lc-question-card {
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-md);
      padding: 22px;
      margin-bottom: 20px;
      box-shadow: var(--apple-shadow-sm);
    }

    .btn-toggle-qtext {
      background: rgba(0, 0, 0, 0.04);
      color: var(--apple-text);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-pill);
      height: 34px;
      padding: 0 14px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      transition: all 0.16s ease;
      box-sizing: border-box;
      white-space: nowrap;
    }

    .btn-toggle-qtext:hover {
      background: rgba(0, 0, 0, 0.08);
      border-color: var(--apple-border-strong);
    }

    .btn-toggle-qtext.opened {
      background: var(--apple-blue-bg);
      color: var(--apple-blue);
      border-color: var(--apple-blue-border);
    }

    .p4-qtext-collapse {
      margin-top: 14px;
      padding: 14px 18px;
      background: rgba(0, 113, 227, 0.04);
      border: 1px solid var(--apple-blue-border);
      border-radius: var(--radius-sm);
      display: none;
      animation: fadeIn 0.2s ease-out forwards;
    }

    .p4-qtext-collapse.show {
      display: block;
    }

    /* 모범답안 토글 버튼 */
    .btn-toggle-answer {
      background: #FFFFFF;
      color: var(--apple-text);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-pill);
      padding: 9px 20px;
      font-size: 13.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      box-shadow: var(--apple-shadow-sm);
      transition: all 0.2s ease;
    }

    .btn-toggle-answer:hover {
      background: #FAFAFA;
      border-color: var(--apple-border-strong);
      transform: translateY(-1px);
    }

    .btn-toggle-answer.opened {
      background: var(--apple-blue-bg);
      color: var(--apple-blue);
      border-color: var(--apple-blue-border);
    }

    /* 모범답안 펼침 영역 */
    .answer-collapse-box {
      margin-top: 20px;
      padding-top: 22px;
      border-top: 1px solid var(--apple-border-subtle);
      display: none;
      animation: fadeIn 0.25s ease-out forwards;
    }

    .answer-collapse-box.show {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .question-translation-banner {
      background: rgba(0, 0, 0, 0.035);
      border-left: 3px solid var(--apple-blue);
      border-radius: 0 8px 8px 0;
      padding: 12px 16px;
      margin-bottom: 20px;
      font-size: 14.5px;
      color: var(--apple-text-secondary);
      line-height: 1.5;
    }

    .question-translation-banner strong {
      color: var(--apple-text);
      margin-right: 6px;
    }

    /* Part 1 전체 지문 카드 */
    .p1-full-passage-card {
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--apple-border);
      border-radius: var(--radius-md);
      padding: 24px 28px;
      margin-bottom: 26px;
      box-shadow: var(--apple-shadow-sm);
    }

    .p1-full-passage-text {
      font-size: 19px;
      line-height: 1.7;
      color: var(--apple-text);
      font-weight: 500;
      letter-spacing: -0.01em;
    }

    /* 문장 카드 */
    .sentence-block-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 14px;
    }

    .sentence-item-card {
      background: rgba(255, 255, 255, 0.85);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 16px;
      transition: all 0.16s ease;
    }

    .sentence-item-card:hover {
      border-color: rgba(0, 113, 227, 0.3);
      box-shadow: var(--apple-shadow-sm);
    }

    .sentence-step-badge {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      color: var(--apple-blue);
      background: var(--apple-blue-bg);
      padding: 2px 8px;
      border-radius: 5px;
      margin-bottom: 5px;
    }

    .sentence-en-text {
      font-size: 16.5px;
      font-weight: 600;
      color: var(--apple-text);
      line-height: 1.45;
      letter-spacing: -0.01em;
    }

    .sentence-chunk-text {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: #0056B3;
      background: rgba(0, 113, 227, 0.05);
      padding: 5px 10px;
      border-radius: 6px;
      margin: 6px 0;
      display: inline-block;
    }

    .sentence-ko-text {
      font-size: 14px;
      color: var(--apple-text-secondary);
      margin-top: 2px;
    }

    /* 만능문장 카드 */
    .magic-sentence-card {
      background: var(--apple-amber-bg);
      border: 1px solid rgba(255, 149, 0, 0.25);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 14px;
    }

    .magic-sentence-en {
      font-size: 15px;
      font-weight: 700;
      color: #92400E;
    }

    .magic-sentence-ko {
      font-size: 13.5px;
      color: #B45309;
      margin-top: 2px;
    }

    .magic-sentence-tip {
      font-size: 12px;
      color: #D97706;
      font-weight: 600;
      margin-top: 4px;
    }

    /* 어휘 카드 */
    .vocab-capsule-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 10px;
      margin-top: 12px;
    }

    .vocab-capsule-card {
      background: rgba(255, 255, 255, 0.85);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-sm);
      padding: 11px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
    }

    .vocab-word-bold {
      font-size: 14px;
      font-weight: 700;
      color: var(--apple-text);
    }

    .vocab-ipa-subtle {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      color: var(--apple-blue);
      margin-left: 5px;
    }

    .vocab-mean-subtle {
      font-size: 12.5px;
      color: var(--apple-text-secondary);
      margin-top: 1px;
    }

    .explanation-callout {
      background: var(--apple-emerald-bg);
      border: 1px solid rgba(52, 199, 89, 0.25);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      font-size: 14px;
      color: #166534;
      line-height: 1.55;
      margin-top: 20px;
    }
    .explanation-title {
      font-size: 14px;
      font-weight: 800;
      color: #166534;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .explanation-body {
      font-size: 14px;
      color: #15803D;
      line-height: 1.6;
    }
    body.dark .explanation-title {
      color: #30D158 !important;
    }
    body.dark .explanation-body {
      color: #A7F3D0 !important;
    }

    /* Part 4 표 카드 */
    .part4-table-card {
      background: #FFFFFF;
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      margin-bottom: 28px;
      box-shadow: var(--apple-shadow-sm);
    }

    .table-top-banner {
      background: #1D1D1F;
      color: #FFFFFF;
      padding: 14px 20px;
      font-size: 16px;
      font-weight: 700;
      text-align: center;
      letter-spacing: -0.01em;
    }

    .table-meta-pills {
      background: #F8F8F9;
      padding: 10px 18px;
      border-bottom: 1px solid var(--apple-border-subtle);
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 16px;
      font-size: 13px;
      color: var(--apple-text-secondary);
    }

    .part4-clean-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
    }

    .part4-clean-table th {
      background: #F2F2F4;
      color: var(--apple-text);
      font-weight: 700;
      padding: 10px 14px;
      text-align: left;
      border-bottom: 1px solid var(--apple-border-subtle);
    }

    .part4-clean-table td {
      padding: 11px 14px;
      border-bottom: 1px solid rgba(0, 0, 0, 0.05);
      color: var(--apple-text);
    }

    .part4-clean-table tr:last-child td {
      border-bottom: none;
    }

    /* 3. 화면 하단 고정 플로팅 바 (언제나 손이 닿는 이전/다음/정지) */
    .floating-bottom-bar {
      position: fixed;
      bottom: 36px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 90;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--apple-border);
      border-radius: var(--radius-pill);
      padding: 7px 16px;
      box-shadow: var(--apple-shadow-lg);
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .btn-floating-drawer {
      background: rgba(0, 0, 0, 0.05);
      border: 1px solid rgba(0, 0, 0, 0.08);
      color: var(--apple-text);
      cursor: pointer;
      width: 40px;
      height: 40px;
      min-width: 40px;
      border-radius: 50%;
      transition: all 0.16s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0;
      flex-shrink: 0;
    }
    .btn-floating-drawer svg {
      width: 22px;
      height: 22px;
      stroke-width: 2.2;
    }
    .btn-floating-drawer:hover {
      background: rgba(0, 0, 0, 0.1);
      border-color: rgba(0, 0, 0, 0.15);
      transform: scale(1.06);
    }
    .btn-floating-drawer:active {
      transform: scale(0.94);
    }

    .btn-floating-nav {
      background: transparent;
      border: none;
      color: var(--apple-text);
      cursor: pointer;
      width: 38px;
      height: 38px;
      min-width: 38px;
      border-radius: 50%;
      transition: all 0.16s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0;
      flex-shrink: 0;
    }
    .btn-floating-nav svg {
      width: 22px;
      height: 22px;
      stroke-width: 2.5;
    }
    .btn-floating-nav:hover:not(:disabled) {
      background: rgba(0, 0, 0, 0.08);
      color: var(--apple-blue);
      transform: scale(1.08);
    }
    .btn-floating-nav:active:not(:disabled) {
      transform: scale(0.92);
    }
    .btn-floating-nav:disabled {
      opacity: 0.25;
      cursor: not-allowed;
    }

    .floating-nav-info {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--apple-text);
      padding: 0 10px;
      font-variant-numeric: tabular-nums;
      letter-spacing: -0.01em;
      white-space: nowrap;
      user-select: none;
      -webkit-user-select: none;
    }

    .btn-floating-stop {
      background: var(--apple-red-bg);
      color: var(--apple-red);
      border: 1px solid var(--apple-red-border);
      border-radius: 50%;
      width: 38px;
      height: 38px;
      min-width: 38px;
      cursor: pointer;
      transition: all 0.16s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0;
      flex-shrink: 0;
    }
    .btn-floating-stop svg {
      width: 15px;
      height: 15px;
    }
    .btn-floating-stop:hover {
      background: rgba(255, 59, 48, 0.2);
      transform: scale(1.06);
    }
    .btn-floating-stop:active {
      transform: scale(0.94);
    }

    /* 1. 하단 플로팅 바 배속 토글 버튼 (1.0x, 0.75x) - 다른 원형 버튼(38px)과 완벽한 수평 높이 일치 */
    .btn-floating-rate {
      height: 38px;
      min-width: 48px;
      padding: 0 12px;
      border-radius: var(--radius-pill);
      background: rgba(0, 113, 227, 0.08);
      border: 1px solid var(--apple-blue-border);
      color: var(--apple-blue);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.16s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      line-height: 1;
    }
    .btn-floating-rate:hover {
      background: var(--apple-blue);
      color: #FFFFFF;
      transform: scale(1.05);
    }
    .btn-floating-rate.active-playing {
      background: var(--apple-blue) !important;
      color: #FFFFFF !important;
      box-shadow: 0 0 12px rgba(0, 113, 227, 0.45);
    }
    @keyframes pulseRate {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.04); opacity: 0.85; }
    }

    /* 2. 파트 3 유형 & 파트 4 표 속성 세그먼트 탭 바 */
    .sub-segmented-bar {
      margin-bottom: 22px;
    }
    .sub-segmented-control {
      display: flex;
      background: rgba(0, 0, 0, 0.05);
      padding: 4px;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(0, 0, 0, 0.04);
      overflow-x: auto;
      gap: 3px;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }
    .sub-segmented-control::-webkit-scrollbar {
      display: none;
    }
    body.dark .sub-segmented-control {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.12);
    }

    .sub-segment-btn {
      flex: 1;
      min-width: max-content;
      background: transparent;
      border: none;
      border-radius: var(--radius-pill);
      padding: 8px 15px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--apple-text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
      user-select: none;
    }
    .sub-segment-btn:hover:not(.active) {
      color: var(--apple-text);
      background: rgba(255, 255, 255, 0.45);
    }
    .sub-segment-btn.active {
      background: #FFFFFF;
      color: var(--apple-blue);
      font-weight: 700;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0, 0, 0, 0.04);
    }
    body.dark .sub-segment-btn {
      color: #AEAEB2;
    }
    body.dark .sub-segment-btn:hover:not(.active) {
      color: #F5F5F7;
      background: rgba(255, 255, 255, 0.06);
    }
    body.dark .sub-segment-btn.active {
      background: #0A84FF !important;
      color: #FFFFFF !important;
      box-shadow: 0 3px 12px rgba(10, 132, 255, 0.4) !important;
    }

    /* 2. 발음 가능한 선택형 칸 스타일 */
    .speech-selectable {
      cursor: pointer;
      position: relative;
      border: 1.5px solid var(--apple-border-subtle);
      border-radius: var(--radius-md);
      background: var(--apple-card-inner);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .speech-selectable:hover {
      border-color: var(--apple-blue-border);
      background: var(--apple-blue-bg);
      transform: translateY(-1px);
    }
    .speech-selectable.selected {
      border-color: var(--apple-blue) !important;
      background: var(--apple-blue-bg) !important;
      box-shadow: 0 0 0 2px var(--apple-blue-border), 0 6px 18px rgba(0, 113, 227, 0.14) !important;
      transform: translateY(-1.5px);
    }

    /* 드로어 & 모달 */
    .drawer-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.25);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 200;
      opacity: 0;
      visibility: hidden;
      transition: all 0.25s ease;
    }

    .drawer-overlay.active {
      opacity: 1;
      visibility: visible;
    }

    .glass-drawer {
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      width: 360px;
      max-width: 85vw;
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(35px) saturate(200%);
      -webkit-backdrop-filter: blur(35px) saturate(200%);
      border-right: 1px solid var(--apple-border);
      box-shadow: var(--apple-shadow-lg);
      z-index: 210;
      transform: translateX(-100%);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }

    .glass-drawer.active {
      transform: translateX(0);
    }

    .drawer-header {
      padding: 20px 22px;
      border-bottom: 1px solid var(--apple-border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .drawer-title {
      font-size: 17px;
      font-weight: 700;
      color: var(--apple-text);
    }

    .btn-drawer-close {
      background: rgba(0, 0, 0, 0.05);
      border: none;
      border-radius: var(--radius-pill);
      width: 30px;
      height: 30px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--apple-text-secondary);
    }

    .drawer-scroll-body {
      flex: 1;
      overflow-y: auto;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .drawer-q-item {
      background: rgba(255, 255, 255, 0.6);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      cursor: pointer;
      text-align: left;
      transition: all 0.16s ease;
    }

    .drawer-q-item:hover {
      background: #FFFFFF;
      border-color: var(--apple-border-strong);
    }

    .drawer-q-item.active {
      background: var(--apple-blue-bg);
      border-color: var(--apple-blue);
      box-shadow: 0 0 0 1px var(--apple-blue);
    }

    .vocab-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.35);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      z-index: 300;
      opacity: 0;
      visibility: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      transition: all 0.25s ease;
    }

    .vocab-modal-backdrop.active {
      opacity: 1;
      visibility: visible;
    }

    .vocab-modal-window {
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(40px) saturate(200%);
      -webkit-backdrop-filter: blur(40px) saturate(200%);
      border: 1px solid var(--apple-border);
      border-radius: 24px;
      width: 480px;
      max-width: 95vw;
      height: 86vh;
      box-shadow: var(--apple-shadow-lg);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transform: scale(0.96);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .vocab-modal-backdrop.active .vocab-modal-window {
      transform: scale(1);
    }

    /* 6. 만능문장 & 단어장 모달 헤더 (상단 문구 삭제 & 알약 토글 가운데 정렬) */
    .vocab-modal-header {
      padding: 14px 16px 12px;
      border-bottom: 1px solid var(--apple-border-subtle);
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: rgba(255, 255, 255, 0.7);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
    }
    body.dark .vocab-modal-header {
      background: rgba(28, 28, 30, 0.75);
    }
    .vocab-modal-top-bar {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      min-height: 40px;
    }

    /* 4. X 버튼 왼쪽에 배치되는 알약 형태 모드 전환 탭 (만능문장 187 vs 빈출 단어장 120) */
    .modal-mode-pill-toggle {
      display: inline-flex;
      background: rgba(118, 118, 128, 0.12);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      padding: 3px;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(0, 0, 0, 0.06);
      gap: 2px;
    }
    body.dark .modal-mode-pill-toggle {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.12);
    }
    .mode-pill-btn {
      background: transparent;
      border: none;
      border-radius: var(--radius-pill);
      padding: 6px 13px;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--apple-text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
    }
    .mode-pill-btn:hover:not(.active) {
      color: var(--apple-text);
    }
    .mode-pill-btn.active {
      background: #FFFFFF;
      color: var(--apple-blue);
      font-weight: 700;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1), 0 0.5px 1.5px rgba(0, 0, 0, 0.06);
    }
    body.dark .mode-pill-btn.active {
      background: #0A84FF;
      color: #FFFFFF;
      box-shadow: 0 2px 8px rgba(10, 132, 255, 0.4);
    }

    /* 1. iOS 정통 리퀴드 글래스 (Liquid Glass) 닫기(X) 버튼 */
    .btn-ios-liquid-close {
      width: 36px;
      height: 36px;
      min-width: 36px;
      min-height: 36px;
      border-radius: 50%;
      background: rgba(118, 118, 128, 0.14);
      backdrop-filter: blur(20px) saturate(190%);
      -webkit-backdrop-filter: blur(20px) saturate(190%);
      border: 1px solid rgba(255, 255, 255, 0.45);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.6);
      color: #3C3C43;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      flex-shrink: 0;
      padding: 0;
    }
    .btn-ios-liquid-close svg {
      width: 14px;
      height: 14px;
      stroke: currentColor;
      transition: transform 0.2s ease;
    }
    .btn-ios-liquid-close:hover {
      background: rgba(118, 118, 128, 0.24);
      transform: scale(1.08);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
    }
    .btn-ios-liquid-close:active {
      transform: scale(0.92);
    }
    body.dark .btn-ios-liquid-close {
      background: rgba(118, 118, 128, 0.28);
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.2);
      color: #EBEBF5;
    }
    body.dark .btn-ios-liquid-close:hover {
      background: rgba(118, 118, 128, 0.42);
    }

    /* 검색창 행 */
    .vocab-modal-search-row {
      width: 100%;
    }
    .vocab-search-wrap {
      position: relative;
      width: 100%;
      display: flex;
      align-items: center;
    }
    .vocab-search-wrap svg {
      position: absolute;
      left: 14px;
      color: var(--apple-text-muted);
      pointer-events: none;
    }
    .vocab-search-input {
      width: 100%;
      padding: 9px 16px 9px 38px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--apple-border-strong);
      background: rgba(255, 255, 255, 0.9);
      font-size: 13.5px;
      color: var(--apple-text);
      outline: none;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .vocab-search-input:focus {
      border-color: var(--apple-blue);
      box-shadow: 0 0 0 3px var(--apple-blue-bg);
    }
    body.dark .vocab-search-input {
      background: rgba(44, 44, 46, 0.9);
      border-color: rgba(255, 255, 255, 0.15);
      color: #FFFFFF;
    }

    /* 만능문장 & 단어장 모달 파트 세그먼트 탭 (모바일 짤림 방지 가로 스크롤) */
    .modal-segmented-bar {
      padding: 8px 14px;
      border-bottom: 1px solid var(--apple-border-subtle);
      background: rgba(255, 255, 255, 0.45);
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }
    .modal-segmented-bar::-webkit-scrollbar {
      display: none;
    }
    body.dark .modal-segmented-bar {
      background: rgba(28, 28, 30, 0.45);
      border-color: rgba(255, 255, 255, 0.08);
    }

    /* 7. 북마크 아이콘 버튼 + 파트 탭 분리 툴바 (모바일 짤림 방지 및 중앙 정렬) */
    .modal-filter-toolbar {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      gap: 6px;
      min-width: max-content;
      margin: 0 auto;
    }
    .btn-modal-bookmark-filter {
      height: 36px;
      min-width: 44px;
      padding: 0 10px;
      border-radius: var(--radius-pill);
      background: rgba(0, 0, 0, 0.05);
      border: 1px solid var(--apple-border-subtle);
      color: var(--apple-text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      flex-shrink: 0;
      user-select: none;
    }
    .btn-modal-bookmark-filter svg {
      width: 16px;
      height: 16px;
      transition: all 0.2s ease;
    }
    .btn-modal-bookmark-filter .bookmark-badge-num {
      font-size: 11px;
      font-weight: 700;
      padding: 1px 5px;
      border-radius: var(--radius-pill);
      background: rgba(0, 0, 0, 0.08);
    }
    .btn-modal-bookmark-filter:hover {
      background: rgba(0, 0, 0, 0.08);
      color: var(--apple-text);
    }
    .btn-modal-bookmark-filter.active {
      background: var(--apple-blue);
      color: #FFFFFF;
      border-color: var(--apple-blue);
      box-shadow: 0 2px 8px rgba(0, 113, 227, 0.35);
    }
    .btn-modal-bookmark-filter.active svg {
      fill: currentColor;
    }
    .btn-modal-bookmark-filter.active .bookmark-badge-num {
      background: rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
    }
    body.dark .btn-modal-bookmark-filter {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.12);
      color: #A1A1A6;
    }
    body.dark .btn-modal-bookmark-filter.active {
      background: #0A84FF;
      color: #FFFFFF;
      border-color: #0A84FF;
    }

    .modal-filter-divider {
      width: 1px;
      height: 20px;
      background: var(--apple-border-subtle);
      flex-shrink: 0;
      margin: 0 2px;
    }
    .modal-segmented-control {
      display: flex;
      justify-content: center;
      background: rgba(0, 0, 0, 0.05);
      padding: 4px;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(0, 0, 0, 0.04);
      gap: 4px;
      overflow-x: auto;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }
    .modal-segmented-control::-webkit-scrollbar {
      display: none;
    }
    body.dark .modal-segmented-control {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.12);
    }
    .modal-segment-btn {
      flex: 1;
      min-width: max-content;
      background: transparent;
      border: none;
      border-radius: var(--radius-pill);
      padding: 7px 14px;
      font-size: 13px;
      font-weight: 600;
      color: var(--apple-text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
      user-select: none;
    }
    .modal-segment-btn:hover:not(.active) {
      color: var(--apple-text);
      background: rgba(255, 255, 255, 0.4);
    }
    .modal-segment-btn.active {
      background: #FFFFFF;
      color: var(--apple-blue);
      font-weight: 700;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.04);
    }
    body.dark .modal-segment-btn {
      color: #8E8E93;
    }
    body.dark .modal-segment-btn:hover:not(.active) {
      color: #FFFFFF;
    }
    body.dark .modal-segment-btn.active {
      background: #0A84FF !important;
      color: #FFFFFF !important;
      box-shadow: 0 2px 10px rgba(10, 132, 255, 0.4) !important;
    }
    .modal-segment-count {
      font-size: 11px;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: var(--radius-pill);
      background: rgba(0, 0, 0, 0.06);
      color: var(--apple-text-secondary);
    }
    .modal-segment-btn.active .modal-segment-count {
      background: var(--apple-blue-bg);
      color: var(--apple-blue);
    }
    body.dark .modal-segment-btn.active .modal-segment-count {
      background: rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
    }

    .vocab-modal-body {
      flex: 1;
      overflow-y: auto;
      padding: 18px 22px;
    }

    .vocab-grid-cards {
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }

    /* 2. 카드 상단 헤더 바 (좌측: ID/카테고리 칩, 우측: 1.0x/0.75x 배속 + 인스타 북마크) */
    .vocab-card-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      width: 100%;
      margin-bottom: 8px;
    }

    .vocab-card-actions {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }

    @keyframes bookmarkPop {
      0% { transform: scale(0.8); }
      50% { transform: scale(1.25); }
      100% { transform: scale(1); }
    }

    .btn-bookmark-icon {
      width: 34px;
      height: 34px;
      min-width: 34px;
      min-height: 34px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.04);
      border: 1px solid rgba(0, 0, 0, 0.06);
      color: var(--apple-text-muted);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      padding: 0;
    }
    .btn-bookmark-icon svg {
      width: 17px;
      height: 17px;
      stroke-width: 2;
      transition: transform 0.2s ease, fill 0.2s ease;
    }
    .btn-bookmark-icon:hover {
      background: rgba(0, 113, 227, 0.08);
      color: var(--apple-blue);
      transform: scale(1.1);
    }
    .btn-bookmark-icon.saved {
      background: rgba(0, 113, 227, 0.12);
      border-color: rgba(0, 113, 227, 0.3);
      color: var(--apple-blue);
      animation: bookmarkPop 0.32s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    body.dark .btn-bookmark-icon {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.1);
      color: #8E8E93;
    }
    body.dark .btn-bookmark-icon:hover {
      background: rgba(10, 132, 255, 0.15);
      color: #0A84FF;
    }
    body.dark .btn-bookmark-icon.saved {
      background: rgba(10, 132, 255, 0.22);
      border-color: rgba(10, 132, 255, 0.45);
      color: #0A84FF;
    }

    /* 저장 버튼 바로 밑에 문장/단어와 나란히 배치되는 배속 선택 버튼 그룹 */
    .vocab-audio-mini-group {
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .btn-audio-mini {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 3px;
      padding: 4px 8px;
      border-radius: var(--radius-pill);
      font-size: 11.5px;
      font-weight: 700;
      background: rgba(0, 113, 227, 0.09);
      color: var(--apple-blue);
      border: 1px solid rgba(0, 113, 227, 0.22);
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .btn-audio-mini svg {
      width: 11px;
      height: 11px;
    }
    .btn-audio-mini:hover {
      background: var(--apple-blue);
      color: #FFFFFF;
    }
    .btn-audio-mini.subtle {
      background: rgba(0, 0, 0, 0.04);
      color: var(--apple-text-secondary);
      border-color: rgba(0, 0, 0, 0.07);
    }
    .btn-audio-mini.subtle:hover {
      background: rgba(0, 0, 0, 0.1);
      color: var(--apple-text);
    }
    body.dark .btn-audio-mini {
      background: rgba(10, 132, 255, 0.18);
      color: #409CFF;
      border-color: rgba(10, 132, 255, 0.35);
    }
    body.dark .btn-audio-mini:hover {
      background: #0A84FF;
      color: #FFFFFF;
    }
    body.dark .btn-audio-mini.subtle {
      background: rgba(255, 255, 255, 0.08);
      color: #A1A1A6;
      border-color: rgba(255, 255, 255, 0.12);
    }
    body.dark .btn-audio-mini.subtle:hover {
      background: rgba(255, 255, 255, 0.18);
      color: #FFFFFF;
    }

    /* 공통 카드 메타 상단 바 (파트 뱃지는 중복 제거하여 삭제하고, ID 및 카테고리만 노출) */
    .vocab-card-meta-row {
      display: flex;
      align-items: center;
      gap: 7px;
      margin-bottom: 8px;
      padding-right: 90px; /* 우측 상단 액션 버튼 공간 확보 */
      flex-wrap: wrap;
    }
    .vocab-card-id {
      font-size: 12.5px;
      font-weight: 800;
      color: var(--apple-blue);
      font-family: 'JetBrains Mono', monospace;
    }
    body.dark .vocab-card-id {
      color: #0A84FF;
    }
    .vocab-category-chip {
      font-size: 11.5px;
      font-weight: 600;
      color: var(--apple-text-secondary);
      background: rgba(0, 0, 0, 0.04);
      padding: 2px 8px;
      border-radius: 6px;
    }
    body.dark .vocab-category-chip {
      background: rgba(255, 255, 255, 0.08);
      color: #A1A1A6;
    }

    /* 만능문장 카드 */
    .vocab-item-card {
      position: relative;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid var(--apple-border-subtle);
      border-radius: 18px;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 10px;
      transition: all 0.2s ease;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.03);
    }
    body.dark .vocab-item-card {
      background: rgba(36, 36, 38, 0.88);
      border-color: rgba(255, 255, 255, 0.1);
    }
    .magic-sentence-main-group {
      width: 100%;
      padding-right: 0; /* 상단 헤더 분리로 배속 버튼과 겹침 0% 원천 차단 및 가로폭 100% 활용 */
    }
    .magic-en-sentence {
      font-size: 16.5px;
      font-weight: 700;
      color: var(--apple-text);
      line-height: 1.45;
      letter-spacing: -0.015em;
    }
    .magic-ko-translation {
      font-size: 14px;
      color: var(--apple-text-secondary);
      line-height: 1.45;
      margin-top: 3px;
    }

    /* 3. 단어장 카드 (인터넷 사전 & 단어장 프리미엄 레이아웃) */
    .vocab-word-card {
      position: relative;
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid var(--apple-border-subtle);
      border-radius: 18px;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: all 0.2s ease;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.03);
    }
    body.dark .vocab-word-card {
      background: rgba(36, 36, 38, 0.88);
      border-color: rgba(255, 255, 255, 0.1);
    }

    /* 표제어 + 발음기호 + 품사 */
    .vocab-headword-section {
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
      width: 100%;
      padding-right: 0;
    }
    .vocab-word-title-group {
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }
    .vocab-word-text {
      font-size: 21px;
      font-weight: 800;
      color: var(--apple-text);
      letter-spacing: -0.02em;
      line-height: 1.2;
    }
    .vocab-word-ipa {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: var(--apple-blue);
      font-weight: 600;
    }
    body.dark .vocab-word-ipa {
      color: #409CFF;
    }
    .vocab-word-pos-tag {
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 5px;
      background: rgba(0, 113, 227, 0.08);
      color: var(--apple-blue);
    }
    body.dark .vocab-word-pos-tag {
      background: rgba(10, 132, 255, 0.18);
      color: #409CFF;
    }
    .vocab-word-ipa {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: var(--apple-blue);
      font-weight: 600;
    }
    .vocab-word-pos-tag {
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 5px;
      background: rgba(0, 113, 227, 0.08);
      color: var(--apple-blue);
    }
    body.dark .vocab-word-pos-tag {
      background: rgba(10, 132, 255, 0.18);
      color: #409CFF;
    }

    /* 미니 오디오 버튼 캡슐 */
    .vocab-audio-mini-group {
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    .btn-audio-mini {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      font-size: 12px;
      font-weight: 700;
      background: rgba(0, 113, 227, 0.09);
      color: var(--apple-blue);
      border: 1px solid rgba(0, 113, 227, 0.22);
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .btn-audio-mini svg {
      width: 12px;
      height: 12px;
    }
    .btn-audio-mini:hover {
      background: var(--apple-blue);
      color: #FFFFFF;
    }
    .btn-audio-mini.subtle {
      background: rgba(0, 0, 0, 0.04);
      color: var(--apple-text-secondary);
      border-color: rgba(0, 0, 0, 0.07);
    }
    .btn-audio-mini.subtle:hover {
      background: rgba(0, 0, 0, 0.1);
      color: var(--apple-text);
    }
    body.dark .btn-audio-mini {
      background: rgba(10, 132, 255, 0.18);
      color: #409CFF;
      border-color: rgba(10, 132, 255, 0.35);
    }
    body.dark .btn-audio-mini:hover {
      background: #0A84FF;
      color: #FFFFFF;
    }
    body.dark .btn-audio-mini.subtle {
      background: rgba(255, 255, 255, 0.08);
      color: #A1A1A6;
      border-color: rgba(255, 255, 255, 0.12);
    }
    body.dark .btn-audio-mini.subtle:hover {
      background: rgba(255, 255, 255, 0.18);
      color: #FFFFFF;
    }

    /* 핵심 뜻 */
    .vocab-meaning-block {
      margin-top: -2px;
    }
    .vocab-meaning-text {
      font-size: 15.5px;
      font-weight: 700;
      color: var(--apple-text);
      line-height: 1.45;
    }

    /* 자주 쓰이는 표현 (연어구) 카드 */
    .vocab-collocation-card {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 7px 11px;
      border-radius: 9px;
      background: rgba(0, 113, 227, 0.05);
      border: 1px solid rgba(0, 113, 227, 0.14);
      font-size: 13px;
    }
    body.dark .vocab-collocation-card {
      background: rgba(10, 132, 255, 0.09);
      border-color: rgba(10, 132, 255, 0.22);
    }
    .collocation-tag {
      font-size: 10.5px;
      font-weight: 700;
      color: var(--apple-blue);
      background: rgba(0, 113, 227, 0.1);
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
    }
    body.dark .collocation-tag {
      color: #409CFF;
      background: rgba(10, 132, 255, 0.2);
    }
    .collocation-phrase {
      font-weight: 700;
      color: var(--apple-text);
      letter-spacing: -0.01em;
    }

    /* 기출 예문 블록 */
    .vocab-example-block {
      padding: 8px 12px;
      border-left: 3px solid var(--apple-blue);
      background: rgba(0, 0, 0, 0.02);
      border-radius: 0 9px 9px 0;
    }
    body.dark .vocab-example-block {
      background: rgba(255, 255, 255, 0.03);
    }
    .example-en-sentence {
      font-size: 13.5px;
      font-weight: 600;
      color: var(--apple-text);
      line-height: 1.5;
    }
    .example-ko-translation {
      font-size: 12.5px;
      color: var(--apple-text-secondary);
      margin-top: 3px;
      line-height: 1.4;
    }

    /* 시험 출제 및 발음 팁 콜아웃 */
    .vocab-exam-tip-box {
      display: flex;
      align-items: flex-start;
      gap: 6px;
      padding: 8px 12px;
      border-radius: 9px;
      background: rgba(255, 149, 0, 0.08);
      border: 1px solid rgba(255, 149, 0, 0.22);
      font-size: 12px;
      line-height: 1.45;
      color: #B26200;
    }
    body.dark .vocab-exam-tip-box {
      background: rgba(255, 159, 10, 0.12);
      border-color: rgba(255, 159, 10, 0.3);
      color: #FFB340;
    }
    .tip-icon-label {
      font-weight: 700;
      white-space: nowrap;
    }
    .tip-content-text {
      color: inherit;
    }

    /* 카드 하단 푸터 (만능문장 오디오 재생) */
    .vocab-card-footer {
      display: flex;
      justify-content: flex-end;
      padding-top: 8px;
      border-top: 1px solid var(--apple-border-subtle);
    }

    /* =========================================================================
       반응형 레이아웃 시스템 (Mobile < 640px, Tablet 641px~1024px, Desktop > 1025px)
       ========================================================================= */

    /* 유틸리티: 반응형 텍스트 스위치 */
    .btn-text-short {
      display: none;
    }
    .btn-text-full {
      display: inline;
    }

    /* 태블릿 & 모바일 공통 (<= 1024px) */
    @media (max-width: 1024px) {
      .apple-header .header-inner {
        padding: 12px 20px;
      }
      .apple-segmented-bar {
        padding: 0 16px;
        margin-top: 14px;
      }
      .main-viewport {
        padding: 0 16px;
        margin: 20px auto 36px;
      }
      .glass-card {
        padding: 24px;
        border-radius: 24px;
      }
      .part4-table-card {
        padding: 18px;
      }
      .cbt-timer-card {
        padding: 18px;
      }
    }

    /* 모바일 집중 최적화 (<= 640px) */
    @media (max-width: 640px) {
      /* 텍스트 축약 제어 */
      .btn-text-short {
        display: inline !important;
      }
      .btn-text-full {
        display: none !important;
      }

      /* 헤더 */
      .apple-header {
        position: sticky;
        top: 0;
      }
      .apple-header .header-inner {
        padding: 10px 14px;
        gap: 8px;
      }
      .brand-title-wrap {
        gap: 8px;
        min-width: 0;
      }
      .btn-theme-toggle {
        width: 36px;
        height: 36px;
        border-radius: 12px;
      }
      .btn-theme-toggle .icon-moon,
      .btn-theme-toggle .icon-sun {
        width: 18px;
        height: 18px;
      }
      .brand-main-title {
        font-size: 16px;
        font-weight: 800;
        letter-spacing: -0.025em;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .btn-vocab-toggle {
        padding: 7px 12px;
        font-size: 13px;
        font-weight: 700;
        gap: 5px;
        flex-shrink: 0;
      }

      /* 세그먼트 컨트롤 탭 (모바일 시인성 & 터치감 강화) */
      .apple-segmented-bar {
        padding: 0 10px;
        margin-top: 10px;
      }
      .segmented-control {
        padding: 4px;
        gap: 4px;
        scrollbar-width: none;
        -ms-overflow-style: none;
      }
      .segmented-control::-webkit-scrollbar {
        display: none;
      }
      .segment-btn {
        min-width: 100px;
        padding: 9px 12px;
        font-size: 14px;
        font-weight: 700;
        gap: 6px;
        min-height: 40px;
      }
      .segment-count {
        font-size: 11px;
        font-weight: 700;
        padding: 2px 6px;
      }

      /* 메인 뷰포트 & 카드 */
      .main-viewport {
        padding: 0 12px;
        margin: 14px auto 120px;
      }
      .sub-segmented-bar {
        margin-bottom: 16px;
      }
      .sub-segmented-control {
        padding: 4px;
        gap: 4px;
      }
      .sub-segment-btn {
        padding: 8px 14px;
        font-size: 13.5px;
        font-weight: 700;
        min-height: 38px;
      }
      .glass-card {
        padding: 18px 16px;
        border-radius: 20px;
      }
      .glass-card-header {
        flex-direction: column;
        align-items: stretch;
        gap: 12px;
        padding-bottom: 14px;
        margin-bottom: 18px;
      }
      .card-meta-tags {
        gap: 6px;
        margin-bottom: 6px;
      }
      .tag-pill {
        font-size: 12.5px;
        font-weight: 700;
        padding: 4px 11px;
      }
      .card-title {
        font-size: 19px;
        font-weight: 800;
        line-height: 1.4;
        letter-spacing: -0.02em;
      }
      .card-nav-controls {
        width: 100%;
        display: flex;
        justify-content: space-between;
        gap: 10px;
      }
      .btn-circle-nav {
        flex: 1;
        justify-content: center;
        text-align: center;
        padding: 10px 14px;
        font-size: 14px;
        font-weight: 700;
        min-height: 42px;
      }

      /* 질문 프롬프트 카드 (글씨 크게 키우고 시원하게) */
      .question-prompt-card {
        padding: 18px 16px;
        margin-bottom: 20px;
        border-radius: 16px;
      }
      .prompt-tag-title {
        font-size: 12.5px;
        font-weight: 700;
      }
      .question-prompt-en {
        font-size: 19px;
        font-weight: 700;
        line-height: 1.5;
        letter-spacing: -0.015em;
      }

      /* Part 1 전체 지문 & 끊어 읽기 문장 카드 (낭독에 최적화된 큰 글씨) */
      .p1-full-passage-card {
        padding: 18px 16px;
        margin-bottom: 20px;
        border-radius: 16px;
      }
      .p1-full-passage-text {
        font-size: 19px;
        line-height: 1.75;
        font-weight: 600;
      }
      .sentence-block-list {
        gap: 12px;
        margin-top: 12px;
      }
      .sentence-item-card {
        padding: 16px 14px;
        border-radius: 16px;
        gap: 10px;
      }
      .sentence-step-badge {
        font-size: 12px;
        padding: 3px 9px;
      }
      .sentence-en-text {
        font-size: 17.5px;
        font-weight: 700;
        line-height: 1.5;
      }
      .sentence-chunk-text {
        font-size: 14.5px;
        line-height: 1.5;
        padding: 6px 11px;
        margin: 6px 0;
        border-radius: 8px;
      }
      .sentence-ko-text {
        font-size: 15px;
        line-height: 1.5;
        margin-top: 3px;
      }

      /* Part 2 사진 영역: 모바일에서도 시원하게 꽉 차게 렌더링 */
      .photo-display-full {
        border-radius: 16px;
        margin-bottom: 20px;
      }
      .photo-display-full img {
        max-height: 380px;
        border-radius: 16px;
        object-fit: cover;
      }

      /* 모범답안 토글 버튼: 모바일에서 누르기 쉬운 풀 위드 버튼 */
      .btn-toggle-answer {
        width: 100%;
        justify-content: center;
        padding: 13px 20px;
        font-size: 15.5px;
        font-weight: 700;
        min-height: 48px;
        border-radius: var(--radius-pill);
      }
      .question-translation-banner {
        padding: 13px 15px;
        font-size: 15px;
        line-height: 1.55;
        margin-bottom: 18px;
      }

      /* 만능문장 카드 & 어휘 카드 폰트 확대 */
      .magic-sentence-card {
        padding: 15px 16px;
        border-radius: 14px;
      }
      .magic-sentence-en {
        font-size: 16.5px;
        font-weight: 700;
        line-height: 1.45;
      }
      .magic-sentence-ko {
        font-size: 14.5px;
        line-height: 1.45;
      }
      .magic-sentence-tip {
        font-size: 13px;
        margin-top: 4px;
      }
      .vocab-capsule-grid {
        grid-template-columns: 1fr;
        gap: 9px;
      }
      .vocab-capsule-card {
        padding: 13px 15px;
        border-radius: 12px;
      }
      .vocab-word-bold {
        font-size: 16px;
      }
      .vocab-ipa-subtle {
        font-size: 13px;
      }
      .vocab-mean-subtle {
        font-size: 14.5px;
        line-height: 1.4;
      }
      .explanation-callout {
        padding: 15px 16px;
        font-size: 14.5px;
        line-height: 1.6;
        border-radius: 14px;
      }

      /* Part 4 표(Table) 영역 (가로 스크롤 & 큰 글씨) */
      .part4-table-card {
        border-radius: 16px;
        margin-bottom: 22px;
      }
      .table-top-banner {
        font-size: 15.5px;
        padding: 12px 14px;
        font-weight: 700;
      }
      .table-meta-pills {
        padding: 9px 14px;
        font-size: 13px;
        gap: 10px;
      }
      .part4-clean-table {
        min-width: 500px;
        font-size: 13.5px;
      }
      .part4-clean-table th,
      .part4-clean-table td {
        padding: 9px 11px;
      }
      .p4-lc-question-card {
        padding: 18px 15px;
        border-radius: 16px;
        margin-bottom: 18px;
      }
      .btn-toggle-qtext {
        height: 34px;
        padding: 0 14px;
        font-size: 12.5px;
        font-weight: 700;
        box-sizing: border-box;
      }
      .p4-qtext-collapse {
        padding: 12px 14px;
        font-size: 15.5px;
      }

      /* CBT 실전 타이머 (숫자 큼직하고 조작 편하게) */
      .cbt-timer-card {
        padding: 16px;
        border-radius: 18px;
        margin: 16px 0 20px;
      }
      .timer-top-line {
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        align-items: center;
        gap: 8px;
        width: 100%;
      }
      .timer-stage-badge {
        justify-self: start;
        font-size: 11.5px;
        font-weight: 700;
        padding: 3px 8px;
        white-space: nowrap;
      }
      .timer-digital-display {
        justify-self: center;
        text-align: center;
        font-size: 24px;
        font-weight: 800;
      }
      .timer-btn-actions {
        justify-self: end;
        display: flex;
        gap: 5px;
      }
      .btn-timer-ctrl {
        width: 34px;
        height: 34px;
        min-width: 34px;
        border-radius: 50%;
        padding: 0;
        font-size: 13px;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }
      .timer-info-caption {
        font-size: 12px;
        margin-top: 4px;
      }

      /* 하단 고정 플로팅 바 (모바일 삐져나옴 완벽 방지: 여유로운 너비 및 컴팩트 정렬) */
      .floating-bottom-bar {
        bottom: max(14px, env(safe-area-inset-bottom, 12px));
        width: auto;
        max-width: calc(100% - 10px);
        padding: 5px 8px;
        gap: 4px;
        justify-content: center;
      }
      .btn-floating-drawer {
        width: 36px;
        height: 36px;
        min-width: 36px;
        padding: 0;
      }
      .btn-floating-drawer svg {
        width: 18px;
        height: 18px;
      }
      .btn-floating-nav {
        width: 34px;
        height: 34px;
        min-width: 34px;
        padding: 0;
      }
      .btn-floating-nav svg {
        width: 18px;
        height: 18px;
      }
      .floating-nav-info {
        padding: 0 2px;
        font-size: 12px;
        font-weight: 700;
      }
      .btn-floating-stop {
        width: 34px;
        height: 34px;
        min-width: 34px;
        padding: 0;
      }
      .btn-floating-stop svg {
        width: 14px;
        height: 14px;
      }
      .btn-floating-rate {
        height: 34px;
        min-width: 38px;
        padding: 0 7px;
        font-size: 11.5px;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }

      /* 단어장 모달 파트 탭 모바일 짤림 방지 */
      .modal-segmented-bar {
        padding: 6px 10px;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }
      .modal-filter-toolbar {
        justify-content: flex-start;
        min-width: max-content;
      }
      .btn-modal-bookmark-filter {
        height: 32px;
        min-width: 40px;
        padding: 0 8px;
        font-size: 11.5px;
      }
      .modal-segment-btn {
        padding: 5px 10px;
        font-size: 12px;
      }

      /* 문항 목록 드로어 */
      .glass-drawer {
        width: 86vw;
        max-width: 340px;
      }
      .drawer-header {
        padding: 16px 18px;
      }
      .drawer-title {
        font-size: 17px;
      }
      .drawer-scroll-body {
        padding: 12px 14px;
        gap: 8px;
      }
      .drawer-q-item {
        padding: 13px 14px;
        font-size: 14px;
      }

      /* 만능문장 & 빈출 단어장 모달 모바일 최적화 */
      .vocab-modal-window {
        width: 96vw;
        height: 94vh;
        border-radius: 22px;
      }
      .vocab-modal-header {
        padding: 12px 14px 10px;
        gap: 10px;
      }
      .vocab-modal-title {
        font-size: 16px;
      }
      .vocab-modal-saved-badge {
        font-size: 11px;
        padding: 1.5px 6px;
      }
      .mode-pill-btn {
        padding: 5px 9px;
        font-size: 12px;
      }
      .btn-ios-liquid-close {
        width: 34px;
        height: 34px;
        min-width: 34px;
        min-height: 34px;
      }
      .modal-segmented-bar {
        padding: 8px 10px;
      }
      .modal-segment-btn {
        padding: 6px 10px;
        font-size: 12px;
      }
      .vocab-search-input {
        font-size: 13.5px;
        padding: 8px 14px 8px 36px;
      }
      .vocab-modal-body {
        padding: 12px 10px;
      }
      .vocab-grid-cards {
        grid-template-columns: 1fr;
        gap: 10px;
      }
      .vocab-item-card,
      .vocab-word-card {
        padding: 14px 15px;
        border-radius: 16px;
      }
      .vocab-card-top-bar {
        gap: 6px;
        margin-bottom: 6px;
      }
      .vocab-audio-mini-group {
        gap: 3px;
      }
      .btn-audio-mini {
        padding: 3px 7px;
        font-size: 11px;
      }
      .btn-bookmark-icon {
        width: 30px;
        height: 30px;
        min-width: 30px;
        min-height: 30px;
      }
      .btn-bookmark-icon svg {
        width: 15px;
        height: 15px;
      }
      .magic-en-sentence {
        font-size: 15.5px;
        line-height: 1.45;
      }
      .vocab-word-text {
        font-size: 19px;
      }
    }
  </style>
</head>
<body>

  <!-- 5. 컴퓨터 & 태블릿 환경에서도 모바일 프레임 레이아웃으로 고정하는 앱 셸 -->
  <div class="mobile-app-shell" id="appMobileShell">

    <!-- 상단 글래스 헤더 -->
    <header class="apple-header">
    <div class="header-inner">
      <div class="brand-title-wrap">
        <h1 class="brand-main-title">토익스피킹 기출 마스터</h1>
      </div>

      <div class="header-actions">
        <!-- 만능문장 187 & 빈출 단어장 모달 버튼 (이모티콘 없이 깔끔한 캡슐) -->
        <button type="button" class="btn-vocab-toggle" onclick="toggleVocabModal()" title="만능문장 187 & 빈출 단어장">
          <span>만능문장 & 단어장</span>
        </button>

        <!-- 5. 다크모드 버튼 (제일 오른쪽 상단에 위치) -->
        <button type="button" class="btn-theme-toggle" id="themeToggleBtn" onclick="toggleDarkMode()" title="다크/라이트 모드 전환" aria-label="다크 모드 전환">
          <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>
          <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- 세그먼트 컨트롤 (파트 1~5 탭) -->
  <nav class="apple-segmented-bar" aria-label="파트 선택">
    <div class="segmented-control" id="partTabContainer"></div>
  </nav>

  <!-- 메인 뷰포트 -->
  <main class="main-viewport" id="appMainViewport"></main>

  <!-- 1 & 3. 화면 하단 고정 플로팅 바 (문항목록 | 이전 | 번호 | 다음 | 정지 | 1.0x | 0.75x 순서) -->
  <aside class="floating-bottom-bar" id="floatingBottomBar" aria-label="빠른 조작 바">
    <!-- 1. 문항 목록 햄버거 버튼 (문구 없이 아이콘만 크게) -->
    <button type="button" class="btn-floating-drawer" onclick="openDrawer()" aria-label="문항 목록 열기" title="문항 목록">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
    <div class="floating-divider" style="width: 1px; height: 18px; background: rgba(127,127,127,0.22); margin: 0 1px;"></div>

    <!-- 2. 이전 문항 버튼 (문구 없이 화살표만 크게) -->
    <button type="button" class="btn-floating-nav" id="btnFloatingPrev" onclick="navPrev()" aria-label="이전 문항" title="이전 문항">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="15 18 9 12 15 6"></polyline>
      </svg>
    </button>
    <span class="floating-nav-info" id="floatingNavText">1 / 10</span>

    <!-- 2. 다음 문항 버튼 (문구 없이 화살표만 크게) -->
    <button type="button" class="btn-floating-nav" id="btnFloatingNext" onclick="navNext()" aria-label="다음 문항" title="다음 문항">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="9 18 15 12 9 6"></polyline>
      </svg>
    </button>
    <div class="floating-divider" style="width: 1px; height: 18px; background: rgba(127,127,127,0.22); margin: 0 1px;"></div>

    <!-- 3. 발음 정지 버튼 (퍼지 멈춤 아이콘) -->
    <button type="button" class="btn-floating-stop" id="btnFloatingStop" onclick="stopSpeech()" aria-label="발음 재생 정지" title="발음 정지">
      <svg viewBox="0 0 24 24" fill="currentColor">
        <rect x="6" y="5" width="4" height="14" rx="1.5"></rect>
        <rect x="14" y="5" width="4" height="14" rx="1.5"></rect>
      </svg>
    </button>
    <button type="button" class="btn-floating-rate" id="btnFloatingRate10" onclick="playSelectedRate(1.0)">1.0x</button>
    <button type="button" class="btn-floating-rate" id="btnFloatingRate075" onclick="playSelectedRate(0.75)">0.75x</button>
  </aside>
  </div><!-- /.mobile-app-shell -->

  <!-- 문항 목록 리퀴드 글래스 사이드 드로어 -->
  <div class="drawer-overlay" id="drawerOverlay" onclick="closeDrawer()"></div>
  <aside class="glass-drawer" id="glassDrawer" aria-label="문항 목록">
    <div class="drawer-header">
      <span class="drawer-title" id="drawerTitleText">문항 목록</span>
      <button type="button" class="btn-drawer-close" onclick="closeDrawer()">✕</button>
    </div>
    <div class="drawer-scroll-body" id="drawerListContainer"></div>
  </aside>

  <!-- 만능문장 187 & 빈출 단어장 리퀴드 글래스 모달 -->
  <div class="vocab-modal-backdrop" id="vocabModalBackdrop" onclick="handleModalBackdropClick(event)">
    <div class="vocab-modal-window" onclick="event.stopPropagation()">
      <div class="vocab-modal-header">
        <!-- 6. 상단 문구 삭제 & 알약 토글만 가운데 정렬 -->
        <div class="vocab-modal-top-bar">
          <div class="modal-mode-pill-toggle" id="modalMainModeBar" role="tablist">
            <button type="button" class="mode-pill-btn active" id="btnModeMagic" onclick="setModalMainMode('magic')">
              <span>만능문장 187</span>
            </button>
            <button type="button" class="mode-pill-btn" id="btnModeVocab" onclick="setModalMainMode('vocab')">
              <span>빈출 단어장 120</span>
            </button>
          </div>

          <!-- iOS 리퀴드 글래스 닫기(X) 버튼 -->
          <button type="button" class="btn-ios-liquid-close" onclick="toggleVocabModal()" aria-label="닫기" style="position: absolute; right: 0;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
              <line x1="17" y1="7" x2="7" y2="17"></line>
              <line x1="7" y1="7" x2="17" y2="17"></line>
            </svg>
          </button>
        </div>

        <div class="vocab-modal-search-row">
          <div class="vocab-search-wrap">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input type="search" class="vocab-search-input" id="modalVocabSearch" placeholder="단어, 표현, 한국어 뜻 검색..." oninput="handleModalSearch(this.value)" />
          </div>
        </div>
      </div>

      <!-- 7. 파트 선택 세그먼트 바 (좌측에 북마크 버튼 분리 & 파트 탭에서 전체/저장됨 제거) -->
      <div class="modal-segmented-bar">
        <div class="modal-filter-toolbar">
          <button type="button" class="btn-modal-bookmark-filter" id="btnModalBookmarkFilter"
                  onclick="toggleModalSavedFilter()" title="저장된 항목 보기" aria-label="저장된 항목 보기">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
            </svg>
            <span class="bookmark-badge-num" id="modalBookmarkCountBadge">0</span>
          </button>
          <div class="modal-filter-divider"></div>
          <div class="modal-segmented-control" id="modalPartFilterContainer" role="tablist"></div>
        </div>
      </div>
      <div class="vocab-modal-body">
        <div class="vocab-grid-cards" id="modalVocabGrid"></div>
      </div>
    </div>
  </div>

  <script>
    const MASTER_DATA = __MASTER_JSON__;
    const MAGIC_DATA = __MAGIC_JSON__; // Part 2~5 순수 187개
    const VOCAB_DATA = __VOCAB_JSON__; // Part 1~5 기출 빈출 단어 120개

    // 이전 버전(암기체크) 호환 마이그레이션
    const legacyMem = JSON.parse(localStorage.getItem('toeic_memorized_187') || '{}');
    const initMagicSaved = JSON.parse(localStorage.getItem('toeic_saved_magic_sentences') || JSON.stringify(legacyMem));
    const initVocabSaved = JSON.parse(localStorage.getItem('toeic_saved_vocab_words') || '{}');

    // 앱 상태
    const state = {
      activePart: 'part1',
      selectedIndex: 0,
      part3TypeFilter: 'ALL',
      part4TableTypeFilter: 'ALL',
      isAnswerOpen: false,
      p4AnswerOpenMap: {},
      p4QTextOpenMap: {}, // 파트 4 질문 지문 숨김/열림 맵
      isVocabModalOpen: false,
      modalMainMode: 'magic', // 'magic' | 'vocab'
      modalPartFilter: '2', // 7. 'ALL'/'SAVED' 제외 후 기본 선택 Part 2
      modalSearchQuery: '',
      bookmarkedMagicIds: initMagicSaved,
      bookmarkedVocabIds: initVocabSaved,
      playingKey: null,
      // 2. 발음 선택 상태
      selectedItemId: null,
      selectedSpeechText: '',
      isDarkMode: localStorage.getItem('toeic_dark_mode') === 'true',
      // CBT 타이머 상태
      timerInterval: null,
      timerStage: 'standby', // 'standby' | 'prep' | 'response' | 'ended'
      timerTotalSeconds: 45,
      timerRemainingSeconds: 45,
      timerPrepLimit: 45,
      timerResponseLimit: 45
    };

    // 3. 다크모드 버튼 토글 함수
    function toggleDarkMode() {
      state.isDarkMode = !state.isDarkMode;
      document.body.classList.toggle('dark', state.isDarkMode);
      localStorage.setItem('toeic_dark_mode', state.isDarkMode ? 'true' : 'false');
    }

    function initTheme() {
      if (state.isDarkMode) {
        document.body.classList.add('dark');
      }
    }

    // =========================================================================
    // 1. Daniel 음성 고정 (다른 음성 제거)
    // =========================================================================
    function getDanielVoice() {
      if (!('speechSynthesis' in window)) return null;
      const voices = window.speechSynthesis.getVoices();
      if (!voices || voices.length === 0) return null;

      const daniel = voices.find(v => (v.name || '').toLowerCase().includes('daniel'));
      if (daniel) return daniel;

      const enMale = voices.find(v => {
        const n = (v.name || '').toLowerCase();
        const l = (v.lang || '').toLowerCase();
        return l.startsWith('en') && (n.includes('guy') || n.includes('andrew') || n.includes('tom') || n.includes('alex') || n.includes('evan'));
      });
      if (enMale) return enMale;

      return voices.find(v => (v.lang || '').toLowerCase().startsWith('en')) || voices[0] || null;
    }

    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = () => { getDanielVoice(); };
    }

    // 2. 발음 선택형 칸 클릭 시 호출 함수 (사용자가 칸 클릭 시 즉시 1.0x로 발음 재생)
    function selectSpeechItem(id, text, autoPlay = false) {
      state.selectedItemId = id;
      state.selectedSpeechText = text;
      document.querySelectorAll('.speech-selectable').forEach(el => {
        if (el.getAttribute('data-speech-id') === id) {
          el.classList.add('selected');
        } else {
          el.classList.remove('selected');
        }
      });
      if (autoPlay && text) {
        speakText(text, 1.0, `select-${id}-1`);
      }
    }

    // 만능문장 안전 음성 재생 (작은따옴표/특수문자 이스케이프 오류 원천 방지)
    function speakMagicItem(id, rate = 1.0) {
      const item = (MAGIC_DATA.items || []).find(it => it.id === id);
      if (item && item.en) {
        speakText(item.en, rate, `magic-${id}-${rate}`);
      }
    }

    // 단어장 안전 음성 재생
    function speakVocabItem(id, rate = 1.0) {
      const item = (VOCAB_DATA.items || []).find(it => it.id === id);
      if (item && item.word) {
        speakText(item.word, rate, `vocab-${id}-${rate}`);
      }
    }

    // 1. 하단 플로팅 바에서 1.0x 또는 0.75x 클릭 시 실행
    function playSelectedRate(rate) {
      if (!state.selectedSpeechText) {
        const firstEl = document.querySelector('.speech-selectable');
        if (firstEl) {
          const id = firstEl.getAttribute('data-speech-id');
          const txt = firstEl.getAttribute('data-speech-text');
          if (id && txt) {
            selectSpeechItem(id, txt);
          }
        }
      }
      if (state.selectedSpeechText) {
        speakText(state.selectedSpeechText, rate, `selected-${rate}`);
        updateRateButtonsUI(rate);
      }
    }

    function updateRateButtonsUI(activeRate) {
      const b10 = document.getElementById('btnFloatingRate10');
      const b075 = document.getElementById('btnFloatingRate075');
      if (b10) b10.classList.toggle('active-playing', activeRate === 1.0 && !!state.playingKey);
      if (b075) b075.classList.toggle('active-playing', activeRate === 0.75 && !!state.playingKey);
    }

    // 독립 정지 함수
    function stopSpeech() {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
      state.playingKey = null;
      updateRateButtonsUI(null);
    }

    function speakText(text, rate = 1.0, key = '') {
      if (!('speechSynthesis' in window)) return;

      if (state.playingKey === key) {
        stopSpeech();
        return;
      }

      window.speechSynthesis.cancel();
      state.playingKey = key;
      updateRateButtonsUI(rate);

      const cleaned = text.replace(/[↗↘↑↓/]/g, ' ').replace(/\s+/g, ' ').trim();
      const utter = new SpeechSynthesisUtterance(cleaned);
      const voice = getDanielVoice();
      if (voice) {
        utter.voice = voice;
        utter.lang = voice.lang || 'en-US';
      } else {
        utter.lang = 'en-US';
      }
      utter.rate = rate;
      utter.pitch = 0.98;

      utter.onend = () => {
        if (state.playingKey === key) {
          state.playingKey = null;
          updateRateButtonsUI(null);
        }
      };
      utter.onerror = () => {
        if (state.playingKey === key) {
          state.playingKey = null;
          updateRateButtonsUI(null);
        }
      };

      window.speechSynthesis.speak(utter);
    }

    function updateCapsuleButtons() {
      document.querySelectorAll('[data-rate-key]').forEach(btn => {
        const k = btn.getAttribute('data-rate-key');
        if (state.playingKey && k === state.playingKey) {
          btn.classList.add('active-playing');
        } else {
          btn.classList.remove('active-playing');
        }
      });
    }

    function escapeHtml(str) {
      return String(str || '')
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }

    // 카테고리에서 파트 접두사(예: 'Part 3 ', '파트3 ') 완벽 제거
    function cleanCategory(cat) {
      if (!cat) return '';
      return String(cat).replace(/^(Part|파트)\s*\d+\s*/i, '').trim();
    }

    // 5 & 6. 배속 캡슐 + 정지 버튼 렌더러
    function renderRateCapsules(text, baseKey) {
      const safe = escapeHtml(text);
      const k1 = `${baseKey}-1.0`;
      const k2 = `${baseKey}-0.75`;
      return `
        <div class="rate-capsule-group">
          <button type="button" class="btn-rate-capsule ${state.playingKey === k1 ? 'active-playing' : ''}"
            data-rate-key="${k1}" data-rate-text="${safe}" data-rate-val="1.0"
            onclick="handleRateClick(this)">
            1.0x
          </button>
          <button type="button" class="btn-rate-capsule ${state.playingKey === k2 ? 'active-playing' : ''}"
            data-rate-key="${k2}" data-rate-text="${safe}" data-rate-val="0.75"
            onclick="handleRateClick(this)">
            0.75x
          </button>
          <button type="button" class="btn-rate-capsule btn-rate-stop" onclick="stopSpeech()" title="음성 정지">
            정지
          </button>
        </div>
      `;
    }

    function handleRateClick(btn) {
      const text = btn.getAttribute('data-rate-text') || '';
      const rate = parseFloat(btn.getAttribute('data-rate-val') || '1.0');
      const key = btn.getAttribute('data-rate-key') || '';
      speakText(text, rate, key);
    }

    // =========================================================================
    // 5. CBT 실시간 카운트다운 타이머 & Beep 사운드
    // =========================================================================
    function playBeepSound(freq = 880, duration = 0.25) {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        gain.gain.setValueAtTime(0.2, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
        osc.start();
        osc.stop(ctx.currentTime + duration);
      } catch (e) {
        console.warn('AudioContext not allowed without user interaction', e);
      }
    }

    // =========================================================================
    // 5. CBT 실시간 카운트다운 타이머 & Beep 사운드 (다중 타이머 인스턴스 지원)
    // =========================================================================
    function playBeepSound(freq = 880, duration = 0.25) {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        gain.gain.setValueAtTime(0.2, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
        osc.start();
        osc.stop(ctx.currentTime + duration);
      } catch (e) {
        console.warn('AudioContext not allowed without user interaction', e);
      }
    }

    const timerRegistry = {
      activeId: null,
      interval: null,
      stage: 'standby', // 'standby' | 'prep' | 'response' | 'ended'
      remaining: 0,
      prepSec: 45,
      respSec: 15
    };

    function resetCbtTimer(timerId, prepSec, respSec) {
      if (timerRegistry.activeId === timerId && timerRegistry.interval) {
        clearInterval(timerRegistry.interval);
        timerRegistry.interval = null;
      }
      timerRegistry.activeId = timerId;
      timerRegistry.stage = 'standby';
      timerRegistry.prepSec = prepSec;
      timerRegistry.respSec = respSec;
      timerRegistry.remaining = prepSec;
      updateCbtTimerUI(timerId);
    }

    function toggleCbtTimer(timerId, prepSec, respSec) {
      // 다른 타이머가 동작 중이었다면 중지 및 리셋
      if (timerRegistry.activeId && timerRegistry.activeId !== timerId && timerRegistry.interval) {
        const prevId = timerRegistry.activeId;
        clearInterval(timerRegistry.interval);
        timerRegistry.interval = null;
        updateCbtTimerUI(prevId);
      }

      if (timerRegistry.activeId === timerId && timerRegistry.interval) {
        // 일시정지
        clearInterval(timerRegistry.interval);
        timerRegistry.interval = null;
        updateCbtTimerUI(timerId);
        return;
      }

      timerRegistry.activeId = timerId;
      timerRegistry.prepSec = prepSec;
      timerRegistry.respSec = respSec;

      if (timerRegistry.stage === 'standby' || timerRegistry.stage === 'ended') {
        if (prepSec > 0) {
          timerRegistry.stage = 'prep';
          timerRegistry.remaining = prepSec;
        } else {
          timerRegistry.stage = 'response';
          timerRegistry.remaining = respSec;
        }
      }

      timerRegistry.interval = setInterval(() => {
        if (timerRegistry.remaining > 0) {
          timerRegistry.remaining--;
          updateCbtTimerUI(timerId);
        } else {
          if (timerRegistry.stage === 'prep') {
            playBeepSound(1000, 0.4); // 삐- 신호음
            if (timerRegistry.respSec > 0) {
              timerRegistry.stage = 'response';
              timerRegistry.remaining = timerRegistry.respSec;
              updateCbtTimerUI(timerId);
            } else {
              // 준비시간만 있는 타이머(예: 표 읽기 45초)
              playBeepSound(587, 0.6); // 종료음
              timerRegistry.stage = 'ended';
              clearInterval(timerRegistry.interval);
              timerRegistry.interval = null;
              updateCbtTimerUI(timerId);
            }
          } else if (timerRegistry.stage === 'response') {
            playBeepSound(587, 0.6); // 종료음
            timerRegistry.stage = 'ended';
            clearInterval(timerRegistry.interval);
            timerRegistry.interval = null;
            updateCbtTimerUI(timerId);
          }
        }
      }, 1000);

      updateCbtTimerUI(timerId);
    }

    function updateCbtTimerUI(timerId) {
      const badge = document.getElementById(`timerStageBadge-${timerId}`);
      const clock = document.getElementById(`timerDigitalClock-${timerId}`);
      const btn = document.getElementById(`btnTimerStart-${timerId}`);
      if (!badge || !clock || !btn) return;

      const isCurrent = timerRegistry.activeId === timerId;
      const stage = isCurrent ? timerRegistry.stage : 'standby';
      const isRunning = isCurrent && !!timerRegistry.interval;
      const remaining = isCurrent ? timerRegistry.remaining : parseInt(clock.getAttribute('data-init-sec') || '45');

      const m = Math.floor(remaining / 60);
      const s = remaining % 60;
      clock.textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;

      if (stage === 'prep') {
        badge.className = 'timer-stage-badge prep';
        badge.innerHTML = '<span class="voice-dot" style="background:#0071E3;"></span> 준비 시간';
        btn.innerHTML = isRunning ? '⏸' : '▶';
        btn.title = isRunning ? '일시정지' : '계속';
      } else if (stage === 'response') {
        badge.className = 'timer-stage-badge response';
        badge.innerHTML = '<span class="voice-dot" style="background:#FF3B30;"></span> 답변 시간';
        btn.innerHTML = isRunning ? '⏸' : '▶';
        btn.title = isRunning ? '일시정지' : '계속';
      } else if (stage === 'ended') {
        badge.className = 'timer-stage-badge standby';
        badge.textContent = timerRegistry.respSec === 0 ? '표 읽기 종료' : '답변 종료';
        btn.innerHTML = '↺';
        btn.title = '다시 시작';
      } else {
        badge.className = 'timer-stage-badge standby';
        const defaultLabel = clock.getAttribute('data-init-badge') || (timerRegistry.respSec === 0 ? '표 읽기 대기 중' : '타이머 대기 중');
        badge.textContent = defaultLabel;
        btn.innerHTML = '▶';
        btn.title = '시작';
      }
    }

    // 하위 호환 함수
    function toggleTimer() {
      toggleCbtTimer('main', state.timerPrepLimit || 45, state.timerResponseLimit || 45);
    }
    function resetTimer(prep, resp) {
      resetCbtTimer('main', prep, resp);
    }

    /* 2 & 3. 안내문구 및 게이지 바가 제거된 깔끔한 CBT 타이머 컴포넌트 */
    function renderCbtTimerCard(prepSec, respSec, timerId = 'main', defaultBadge = '타이머 대기 중') {
      return `
        <div class="cbt-timer-card" data-timer-id="${timerId}">
          <div class="timer-top-line">
            <div class="timer-stage-badge standby" id="timerStageBadge-${timerId}">${defaultBadge}</div>
            <div class="timer-digital-display" id="timerDigitalClock-${timerId}" data-init-sec="${prepSec}" data-init-badge="${defaultBadge}">00:${String(prepSec).padStart(2, '0')}</div>
            <div class="timer-btn-actions">
              <button type="button" class="btn-timer-ctrl" id="btnTimerStart-${timerId}" onclick="toggleCbtTimer('${timerId}', ${prepSec}, ${respSec})" title="시작" aria-label="타이머 시작/일시정지">▶</button>
              <button type="button" class="btn-timer-ctrl" onclick="resetCbtTimer('${timerId}', ${prepSec}, ${respSec})" title="초기화" aria-label="타이머 초기화">↺</button>
            </div>
          </div>
        </div>
      `;
    }

    // =========================================================================
    // 1. 상단 세그먼트 컨트롤 탭 (문항 개수 숫자 뱃지 전면 삭제)
    // =========================================================================
    function renderSegmentedTabs() {
      const tabs = [
        { id: 'part1', label: 'Part 1' },
        { id: 'part2', label: 'Part 2' },
        { id: 'part3', label: 'Part 3' },
        { id: 'part4', label: 'Part 4' },
        { id: 'part5', label: 'Part 5' }
      ];

      const c = document.getElementById('partTabContainer');
      c.innerHTML = tabs.map(t => `
        <button type="button" class="segment-btn ${state.activePart === t.id ? 'active' : ''}"
          onclick="switchPart('${t.id}')">
          <span class="segment-label">${t.label}</span>
        </button>
      `).join('');
    }

    function switchPart(partId) {
      stopSpeech();
      state.activePart = partId;
      state.selectedIndex = 0;
      state.isAnswerOpen = false;
      state.p4AnswerOpenMap = {};
      state.p4QTextOpenMap = {};
      renderSegmentedTabs();
      renderMainViewport();
      updateDrawerContent();
    }

    const PARTS_ORDER = ['part1', 'part2', 'part3', 'part4', 'part5'];

    function getItemsForPart(partId) {
      if (partId === 'part1') return MASTER_DATA.part1;
      if (partId === 'part2') return MASTER_DATA.part2;
      if (partId === 'part3') {
        if (state.part3TypeFilter === 'ALL') return MASTER_DATA.part3;
        return MASTER_DATA.part3.filter(q => q.typeId === state.part3TypeFilter);
      }
      if (partId === 'part4') {
        if (state.part4TableTypeFilter === 'ALL') return MASTER_DATA.part4;
        return MASTER_DATA.part4.filter(s => s.tableTypeId === state.part4TableTypeFilter);
      }
      if (partId === 'part5') return MASTER_DATA.part5;
      return [];
    }

    function getActiveItems() {
      return getItemsForPart(state.activePart);
    }

    function updateFloatingNav() {
      const items = getActiveItems();
      const text = document.getElementById('floatingNavText');
      const btnPrev = document.getElementById('btnFloatingPrev');
      const btnNext = document.getElementById('btnFloatingNext');
      if (!text || !btnPrev || !btnNext) return;

      const cur = state.selectedIndex + 1;
      const total = items.length;
      text.textContent = `${cur} / ${total}`;

      const isFirstOfAll = state.activePart === 'part1' && state.selectedIndex === 0;
      const isLastOfAll = state.activePart === 'part5' && state.selectedIndex >= total - 1;
      btnPrev.disabled = isFirstOfAll;
      btnNext.disabled = isLastOfAll;
    }

    function navPrev() {
      if (state.selectedIndex > 0) {
        selectItem(state.selectedIndex - 1);
      } else {
        const pIdx = PARTS_ORDER.indexOf(state.activePart);
        if (pIdx > 0) {
          const prevPart = PARTS_ORDER[pIdx - 1];
          const prevItems = getItemsForPart(prevPart);
          switchPart(prevPart);
          selectItem(Math.max(0, prevItems.length - 1));
        }
      }
    }

    function navNext() {
      const items = getActiveItems();
      if (state.selectedIndex < items.length - 1) {
        selectItem(state.selectedIndex + 1);
      } else {
        const pIdx = PARTS_ORDER.indexOf(state.activePart);
        if (pIdx < PARTS_ORDER.length - 1) {
          const nextPart = PARTS_ORDER[pIdx + 1];
          switchPart(nextPart);
          selectItem(0);
        }
      }
    }

    function selectItem(idx) {
      stopSpeech();
      state.selectedIndex = idx;
      state.isAnswerOpen = false;
      state.p4AnswerOpenMap = {};
      state.p4QTextOpenMap = {};
      renderMainViewport();
    }

    // =========================================================================
    // 문항 목록 사이드 드로어
    // =========================================================================
    function openDrawer() {
      updateDrawerContent();
      document.getElementById('drawerOverlay').classList.add('active');
      document.getElementById('glassDrawer').classList.add('active');
    }

    function closeDrawer() {
      document.getElementById('drawerOverlay').classList.remove('active');
      document.getElementById('glassDrawer').classList.remove('active');
    }

    function updateDrawerContent() {
      const items = getActiveItems();
      const titleEl = document.getElementById('drawerTitleText');
      titleEl.textContent = `${state.activePart.toUpperCase()} 문항 목록 (${items.length})`;

      const listEl = document.getElementById('drawerListContainer');
      listEl.innerHTML = items.map((it, idx) => {
        const isSel = idx === state.selectedIndex;
        const numLabel = state.activePart === 'part4' ? `Set ${idx + 1}` : `Q${idx + 1}`;
        const badge = it.typeBadge || it.tableTypeBadge || it.category || '';
        return `
          <div class="drawer-q-item ${isSel ? 'active' : ''}" onclick="handleSelectFromDrawer(${idx})">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <strong style="font-size: 13px; color: var(--apple-text);">${escapeHtml(numLabel)}</strong>
              <span class="tag-pill tag-category" style="font-size: 11px;">${escapeHtml(badge)}</span>
            </div>
            <div style="font-size: 13px; color: var(--apple-text-secondary); line-height: 1.35;">
              ${escapeHtml(it.topic || it.title || '')}
            </div>
          </div>
        `;
      }).join('');
    }

    function handleSelectFromDrawer(idx) {
      stopSpeech();
      state.selectedIndex = idx;
      state.isAnswerOpen = false;
      state.p4AnswerOpenMap = {};
      state.p4QTextOpenMap = {};
      closeDrawer();
      renderMainViewport();
    }

    // =========================================================================
    // 모범답안 & 파트4 질문 지문 토글
    // =========================================================================
    function toggleAnswer() {
      state.isAnswerOpen = !state.isAnswerOpen;
      const el = document.getElementById('answerCollapseBox');
      const btn = document.getElementById('btnToggleAnswer');
      if (el && btn) {
        if (state.isAnswerOpen) {
          el.classList.add('show');
          btn.classList.add('opened');
          btn.innerHTML = '<span>모범답안 접기</span>';
        } else {
          el.classList.remove('show');
          btn.classList.remove('opened');
          btn.innerHTML = '<span>모범답안 보기</span>';
        }
      }
    }

    function toggleP4QuestionAnswer(qId) {
      state.p4AnswerOpenMap[qId] = !state.p4AnswerOpenMap[qId];
      const el = document.getElementById(`p4-ans-${qId}`);
      const btn = document.getElementById(`p4-btn-${qId}`);
      if (el && btn) {
        if (state.p4AnswerOpenMap[qId]) {
          el.classList.add('show');
          btn.classList.add('opened');
          btn.innerHTML = '<span>모범답안 접기</span>';
        } else {
          el.classList.remove('show');
          btn.classList.remove('opened');
          btn.innerHTML = '<span>모범답안 보기</span>';
        }
      }
    }

    // 4. 파트 4 질문 숨김/열림 토글
    function toggleP4QuestionText(qId) {
      state.p4QTextOpenMap[qId] = !state.p4QTextOpenMap[qId];
      const el = document.getElementById(`p4-qtext-${qId}`);
      const btn = document.getElementById(`p4-qbtn-${qId}`);
      if (el && btn) {
        if (state.p4QTextOpenMap[qId]) {
          el.classList.add('show');
          btn.classList.add('opened');
          btn.innerHTML = '<span>질문 접기</span>';
        } else {
          el.classList.remove('show');
          btn.classList.remove('opened');
          btn.innerHTML = '<span>질문 보기</span>';
        }
      }
    }

    // =========================================================================
    // 메인 뷰포트 렌더링
    // =========================================================================
    function renderMainViewport() {
      const root = document.getElementById('appMainViewport');
      const items = getActiveItems();
      if (state.selectedIndex >= items.length) state.selectedIndex = 0;
      const cur = items[state.selectedIndex];

      // Part 3 유형 탭 바
      let filterBarHtml = '';
      if (state.activePart === 'part3') {
        filterBarHtml = `
          <div class="sub-segmented-bar">
            <div class="sub-segmented-control" role="tablist">
              ${MASTER_DATA.part3Types.map(t => `
                <button type="button" role="tab" class="sub-segment-btn ${state.part3TypeFilter === t.id ? 'active' : ''}"
                  onclick="setPart3Filter('${t.id}')">
                  ${escapeHtml(t.name)}
                </button>
              `).join('')}
            </div>
          </div>
        `;
      }

      // 7. Part 4 표 속성별 탭 바
      if (state.activePart === 'part4') {
        filterBarHtml = `
          <div class="sub-segmented-bar">
            <div class="sub-segmented-control" role="tablist">
              ${MASTER_DATA.part4TableTypes.map(t => `
                <button type="button" role="tab" class="sub-segment-btn ${state.part4TableTypeFilter === t.id ? 'active' : ''}"
                  onclick="setPart4TableFilter('${t.id}')">
                  ${escapeHtml(t.name)}
                </button>
              `).join('')}
            </div>
          </div>
        `;
      }

      if (!cur) {
        root.innerHTML = `<div class="glass-card"><p>문항이 없습니다.</p></div>`;
        return;
      }

      if (state.activePart === 'part1') {
        root.innerHTML = filterBarHtml + renderPart1Detail(cur, state.selectedIndex, items.length);
        resetTimer(cur.prepTime || 45, cur.responseTime || 45);
      } else if (state.activePart === 'part4') {
        root.innerHTML = filterBarHtml + renderPart4SetDetail(cur, state.selectedIndex, items.length);
        resetTimer(cur.prepTime || 45, 15);
      } else {
        root.innerHTML = filterBarHtml + renderStandardQuestionDetail(cur, state.selectedIndex, items.length);
        resetTimer(cur.prepTime || 45, cur.responseTime || 30);
      }

      updateFloatingNav();

      // 첫 번째 발음 항목 자동 기본 선택
      setTimeout(() => {
        const first = document.querySelector('.speech-selectable');
        if (first) {
          const id = first.getAttribute('data-speech-id');
          const txt = first.getAttribute('data-speech-text');
          if (id && txt) selectSpeechItem(id, txt);
        }
      }, 20);
    }

    function setPart3Filter(typeId) {
      stopSpeech();
      state.part3TypeFilter = typeId;
      state.selectedIndex = 0;
      renderMainViewport();
      updateDrawerContent();
    }

    function setPart4TableFilter(typeId) {
      stopSpeech();
      state.part4TableTypeFilter = typeId;
      state.selectedIndex = 0;
      renderMainViewport();
      updateDrawerContent();
    }

    function cleanEnglishTopic(topic) {
      if (!topic) return '';
      const match = topic.match(/\(([^)]+)\)/);
      if (match && /[a-zA-Z]/.test(match[1])) {
        return match[1].trim();
      }
      return topic.trim();
    }

    // =========================================================================
    // Part 1 렌더링 (전체 지문 맨 위 + 아래로 문장별 끊어 읽기 + 타이머)
    // =========================================================================
    function renderPart1Detail(q, idx, total) {
      const fullText = (q.sentences || []).map(s => s.en).join(' ');

      return `
        <article class="glass-card">
          <!-- 3. 헤더 -->
          <div class="glass-card-header">
            <div class="header-text-group">
              <div class="card-meta-tags">
                <span class="tag-pill tag-part" style="font-size: 11.5px; padding: 3px 9px;">Q${idx + 1}</span>
                <span class="tag-pill tag-time">준비 45초 · 답변 45초</span>
              </div>
              <h2 class="card-title">${escapeHtml(cleanEnglishTopic(q.topic))}</h2>
            </div>
          </div>

          <!-- 4. 전체 지문 제일 위 노출 (클릭 시 발음 선택 및 즉시 재생) -->
          <div class="p1-full-passage-card speech-selectable ${state.selectedItemId === q.id + '-full' ? 'selected' : ''}"
               data-speech-id="${q.id}-full" data-speech-text="${escapeHtml(fullText)}"
               onclick="selectSpeechItem('${q.id}-full', this.getAttribute('data-speech-text'), true)">
            <p class="p1-full-passage-text">${escapeHtml(fullText)}</p>
          </div>

          <!-- 5. 실제 CBT 타이머 (준비 45초 ➔ 삐 ➔ 답변 45초) -->
          ${renderCbtTimerCard(q.prepTime || 45, q.responseTime || 45)}

          <!-- 문장별 끊어 읽기 (클릭 시 발음 선택 및 즉시 재생) -->
          <div style="margin-top: 30px;">
            <h3 style="font-size: 16px; font-weight: 700; color: var(--apple-text); margin-bottom: 12px;">
              문장별 끊어 읽기
            </h3>
            <div class="sentence-block-list">
              ${q.sentences.map((s, sIdx) => `
                <div class="sentence-item-card speech-selectable ${state.selectedItemId === q.id + '-s' + sIdx ? 'selected' : ''}"
                     data-speech-id="${q.id}-s${sIdx}" data-speech-text="${escapeHtml(s.en)}"
                     onclick="selectSpeechItem('${q.id}-s${sIdx}', this.getAttribute('data-speech-text'), true)">
                  <div style="flex: 1;">
                    <span class="sentence-step-badge">문장 ${sIdx + 1}</span>
                    <div class="sentence-en-text">${escapeHtml(s.en)}</div>
                    <div class="sentence-chunk-text">${escapeHtml(s.chunking)}</div>
                    <div class="sentence-ko-text">${escapeHtml(s.ko)}</div>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- 핵심 발음 어휘 (클릭 시 발음 선택 및 즉시 재생) -->
          <div style="margin-top: 28px;">
            <h3 style="font-size: 15px; font-weight: 700; color: var(--apple-text); margin-bottom: 10px;">
              핵심 발음 어휘
            </h3>
            <div class="vocab-capsule-grid">
              ${(q.vocabulary || []).map((v, vIdx) => `
                <div class="vocab-capsule-card speech-selectable ${state.selectedItemId === q.id + '-v' + vIdx ? 'selected' : ''}"
                     data-speech-id="${q.id}-v${vIdx}" data-speech-text="${escapeHtml(v.word)}"
                     onclick="selectSpeechItem('${q.id}-v${vIdx}', this.getAttribute('data-speech-text'), true)">
                  <div>
                    <div>
                      <span class="vocab-word-bold">${escapeHtml(v.word)}</span>
                      <span class="vocab-ipa-subtle">${escapeHtml(v.ipa)}</span>
                    </div>
                    <div class="vocab-mean-subtle">[${escapeHtml(v.pos)}] ${escapeHtml(v.meaning)}</div>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          ${q.readingTips ? `
            <div class="explanation-callout" style="margin-top: 24px;">
              <div class="explanation-title">💡 Part 1 발음 팁</div>
              <div class="explanation-body">${escapeHtml(q.readingTips)}</div>
            </div>
          ` : ''}
        </article>
      `;
    }

    // =========================================================================
    // Part 2, Part 3, Part 5 렌더링
    // 1. 사진 레터박스 제거 / 2. 모범답안 안에 전체 발음 / 3. 네비게이션 고정 / 5. 타이머 / 8. 질문해석 상단
    // =========================================================================
    function renderStandardQuestionDetail(q, idx, total) {
      const fullSentences = (q.sentences || []).map(s => s.en).join(' ');

      return `
        <article class="glass-card">
          <!-- 3. 고정 헤더 -->
          <div class="glass-card-header">
            <div class="header-text-group">
              <div class="card-meta-tags">
                <span class="tag-pill tag-part" style="font-size: 11.5px; padding: 3px 9px;">Q${idx + 1}</span>
                <span class="tag-pill tag-time">준비 ${q.prepTime}초 · 답변 ${q.responseTime}초</span>
              </div>
              <h2 class="card-title">${escapeHtml(cleanEnglishTopic(q.topic))}</h2>
            </div>
          </div>

          <!-- 1. Part 2 사진: 검은 레터박스 없이 카드 너비에 꽉 차게 렌더링 -->
          ${q.part === 2 && q.imageBase64 ? `
            <div class="photo-display-full">
              <img src="${q.imageBase64}" alt="${escapeHtml(cleanEnglishTopic(q.topic))}" />
            </div>
          ` : ''}

          <!-- 8. 질문 프롬프트 (영어 질문만 노출, 클릭 시 발음 즉시 재생) -->
          ${q.question ? `
            <div class="question-prompt-card speech-selectable ${state.selectedItemId === q.id + '-prompt' ? 'selected' : ''}"
                 data-speech-id="${q.id}-prompt" data-speech-text="${escapeHtml(q.question)}"
                 onclick="selectSpeechItem('${q.id}-prompt', this.getAttribute('data-speech-text'), true)">
              <p class="question-prompt-en">${escapeHtml(q.question)}</p>
            </div>
          ` : ''}

          <!-- 5. CBT 타이머 (준비 시간 ➔ 삐 ➔ 답변 시간) -->
          ${renderCbtTimerCard(q.prepTime || 45, q.responseTime || 30)}

          <!-- 2. 모범답안 토글 버튼 -->
          <div style="display: flex; align-items: center; margin-top: 20px;">
            <button type="button" id="btnToggleAnswer" class="btn-toggle-answer ${state.isAnswerOpen ? 'opened' : ''}" onclick="toggleAnswer()">
              <span>${state.isAnswerOpen ? '모범답안 접기' : '모범답안 보기'}</span>
            </button>
          </div>

          <!-- 모범답안 펼침 영역 -->
          <div id="answerCollapseBox" class="answer-collapse-box ${state.isAnswerOpen ? 'show' : ''}">
            <!-- 8. 질문 한국어 해석을 모범답안 맨 위에 배치 -->
            ${q.questionKo ? `
              <div class="question-translation-banner">
                <strong>질문 해석:</strong> ${escapeHtml(q.questionKo)}
              </div>
            ` : ''}

            <!-- 모범답안 헤더 -->
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <h3 style="font-size: 15px; font-weight: 700; color: var(--apple-text);">
                문장별 모범답안
              </h3>
              <button type="button" class="speech-selectable ${state.selectedItemId === q.id + '-all' ? 'selected' : ''}"
                      data-speech-id="${q.id}-all" data-speech-text="${escapeHtml(fullSentences)}"
                      onclick="selectSpeechItem('${q.id}-all', this.getAttribute('data-speech-text'), true)"
                      style="padding: 4px 12px; font-size: 12px; font-weight: 600; border-radius: var(--radius-pill); border: 1px solid var(--apple-blue-border); background: var(--apple-blue-bg); color: var(--apple-blue);">
                전체 모범답안 듣기
              </button>
            </div>

            <!-- 문장 목록 (클릭하여 발음 즉시 재생) -->
            <div class="sentence-block-list">
              ${(q.sentences || []).map((s, sIdx) => `
                <div class="sentence-item-card speech-selectable ${state.selectedItemId === q.id + '-ms' + sIdx ? 'selected' : ''}"
                     data-speech-id="${q.id}-ms${sIdx}" data-speech-text="${escapeHtml(s.en)}"
                     onclick="selectSpeechItem('${q.id}-ms${sIdx}', this.getAttribute('data-speech-text'), true)">
                  <div style="flex: 1;">
                    ${s.step ? `<span class="sentence-step-badge">${escapeHtml(s.step)}</span>` : ''}
                    <div class="sentence-en-text">${escapeHtml(s.en)}</div>
                    <div class="sentence-ko-text">${escapeHtml(s.ko)}</div>
                  </div>
                </div>
              `).join('')}
            </div>

            <!-- 2. 쓰인 만능문장 (적용된 만능문장 ➔ 다른 만능문장 표현으로 변경, 클릭하여 듣기 삭제) -->
            ${q.magicSentences && q.magicSentences.length > 0 ? `
              <div style="margin-top: 24px;">
                <h3 style="font-size: 15px; font-weight: 700; color: var(--apple-text); margin-bottom: 10px;">
                  다른 만능문장 표현
                </h3>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                  ${q.magicSentences.map((m, mIdx) => `
                    <div class="magic-sentence-card speech-selectable ${state.selectedItemId === q.id + '-mg' + mIdx ? 'selected' : ''}"
                         data-speech-id="${q.id}-mg${mIdx}" data-speech-text="${escapeHtml(m.en)}"
                         onclick="selectSpeechItem('${q.id}-mg${mIdx}', this.getAttribute('data-speech-text'), true)">
                      <div>
                        <div class="magic-sentence-en">${escapeHtml(m.en)}</div>
                        <div class="magic-sentence-ko">${escapeHtml(m.ko)}</div>
                        ${m.tip ? `<div class="magic-sentence-tip">💡 ${escapeHtml(m.tip)}</div>` : ''}
                      </div>
                    </div>
                  `).join('')}
                </div>
              </div>
            ` : ''}

            <!-- 핵심 어휘 (클릭하여 발음 즉시 재생) -->
            <div style="margin-top: 24px;">
              <h3 style="font-size: 15px; font-weight: 700; color: var(--apple-text); margin-bottom: 10px;">
                핵심 어휘
              </h3>
              <div class="vocab-capsule-grid">
                ${(q.vocabulary || []).map((v, vIdx) => `
                  <div class="vocab-capsule-card speech-selectable ${state.selectedItemId === q.id + '-vv' + vIdx ? 'selected' : ''}"
                       data-speech-id="${q.id}-vv${vIdx}" data-speech-text="${escapeHtml(v.word)}"
                       onclick="selectSpeechItem('${q.id}-vv${vIdx}', this.getAttribute('data-speech-text'), true)">
                    <div>
                      <div>
                        <span class="vocab-word-bold">${escapeHtml(v.word)}</span>
                        <span class="vocab-ipa-subtle">${escapeHtml(v.ipa)}</span>
                      </div>
                      <div class="vocab-mean-subtle">[${escapeHtml(v.pos)}] ${escapeHtml(v.meaning)}</div>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>

            <!-- 4. 고득점 해설 전략: 밑으로 줄 바꿔서 내용 적기 -->
            ${q.explanation ? `
              <div class="explanation-callout">
                <div class="explanation-title">💡 고득점 해설 전략</div>
                <div class="explanation-body">${escapeHtml(q.explanation)}</div>
              </div>
            ` : ''}
          </div>
        </article>
      `;
    }

    // =========================================================================
    // Part 4 렌더링
    // 4. 질문 지문 숨김 토글 & 지문 내 해석 / 2. 모범답안 내 전체 발음 / 7. 표 세트 연계
    // =========================================================================
    function renderPart4SetDetail(setObj, idx, total) {
      const t = setObj.scheduleTable;

      return `
        <article class="glass-card">
          <!-- 3. 고정 헤더 -->
          <div class="glass-card-header">
            <div class="header-text-group">
              <div class="card-meta-tags">
                <span class="tag-pill tag-time">표 읽기 45초</span>
              </div>
              <h2 class="card-title">Set ${idx + 1} — ${escapeHtml(cleanEnglishTopic(setObj.topic))}</h2>
            </div>
          </div>

          <!-- 표(Schedule Table) 카드 -->
          <div class="part4-table-card">
            <div class="table-top-banner">${escapeHtml(t.headerTitle)}</div>
            <div class="table-meta-pills">
              ${(t.metaInfo || []).map(m => `
                <span><strong>${escapeHtml(m.label)}:</strong> ${escapeHtml(m.value)}</span>
              `).join('')}
            </div>
            <div style="overflow-x: auto;">
              <table class="part4-clean-table">
                <thead>
                  <tr>
                    <th>Time / Date</th>
                    <th>Session / Person</th>
                    <th>Topic / Experience</th>
                    <th>Location / Mode</th>
                    <th>Note / Speaker</th>
                  </tr>
                </thead>
                <tbody>
                  ${(t.rows || []).map(r => `
                    <tr>
                      <td><strong>${escapeHtml(r.date)}</strong></td>
                      <td>${escapeHtml(r.time)}</td>
                      <td><strong>${escapeHtml(r.event)}</strong></td>
                      <td>${escapeHtml(r.location)}</td>
                      <td>${escapeHtml(r.note)}</td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>

          <!-- 3. 일정표 밑: 준비 시간 45초 전용 타이머 세팅 -->
          ${renderCbtTimerCard(45, 0, 'p4-table', '표 읽기 45초')}

          <!-- 3. 표 읽는 타이머 밑 구분선 -->
          <div style="border-top: 1px solid var(--apple-border-subtle); margin: 24px 0 20px 0;"></div>

          <!-- 4 & 5. 표 연계/실제시험처럼 문구 삭제 및 문제 카드 4개 정돈 -->
          <div style="margin-top: 20px;">
            <div style="display: flex; flex-direction: column; gap: 16px;">
              ${setObj.questions.map((q, qIdx) => {
                const isAnsOpen = !!state.p4AnswerOpenMap[q.qId];
                const isQTextOpen = !!state.p4QTextOpenMap[q.qId];
                const fullSentences = (q.sentences || []).map(s => s.en).join(' ');

                return `
                  <div class="p4-lc-question-card" style="border-radius: 18px; padding: 18px 16px; background: rgba(255, 255, 255, 0.95); margin-bottom: 6px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);">
                    <!-- 1. 파트 4 상단: Q{qIdx + 1} 질문듣기 통합 버튼 (좌측) / 질문보기 & 모범답안보기 (우측 밀어서 배치) -->
                    <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; flex-wrap: wrap;">
                      <button type="button" class="speech-selectable ${state.selectedItemId === q.qId + '-prompt' ? 'selected' : ''}"
                              data-speech-id="${q.qId}-prompt" data-speech-text="${escapeHtml(q.question)}"
                              onclick="selectSpeechItem('${q.qId}-prompt', this.getAttribute('data-speech-text'), true)"
                              style="height: 34px; padding: 0 14px; font-size: 12.5px; font-weight: 700; border-radius: var(--radius-pill); border: 1px solid var(--apple-blue-border); background: var(--apple-blue-bg); color: var(--apple-blue); display: inline-flex; align-items: center; justify-content: center; box-sizing: border-box; white-space: nowrap; flex-shrink: 0;">
                        Q${qIdx + 1} 질문듣기
                      </button>
                      <div style="display: flex; align-items: center; gap: 6px; flex-shrink: 0;">
                        <button type="button" id="p4-qbtn-${q.qId}" class="btn-toggle-qtext ${isQTextOpen ? 'opened' : ''}"
                          onclick="toggleP4QuestionText('${q.qId}')">
                          <span>${isQTextOpen ? '질문 접기' : '질문 보기'}</span>
                        </button>
                        <button type="button" id="p4-btn-${q.qId}" class="btn-toggle-qtext ${isAnsOpen ? 'opened' : ''}"
                          onclick="toggleP4QuestionAnswer('${q.qId}')">
                          <span>${isAnsOpen ? '모범답안 접기' : '모범답안 보기'}</span>
                        </button>
                      </div>
                    </div>

                    <!-- 4. [질문 보기] 버튼을 누르면 나타나는 지문 + 해석 (클릭하여 선택 및 재생) -->
                    <div id="p4-qtext-${q.qId}" class="p4-qtext-collapse ${isQTextOpen ? 'show' : ''}">
                      <div class="speech-selectable ${state.selectedItemId === q.qId + '-prompt' ? 'selected' : ''}"
                           data-speech-id="${q.qId}-prompt" data-speech-text="${escapeHtml(q.question)}"
                           onclick="selectSpeechItem('${q.qId}-prompt', this.getAttribute('data-speech-text'), true)"
                           style="padding: 12px 14px; margin-top: 8px; border-radius: var(--radius-md);">
                        <div style="font-size: 16px; font-weight: 700; color: var(--apple-text); line-height: 1.45;">
                          ${escapeHtml(q.question)}
                        </div>
                        <div style="font-size: 13.5px; color: var(--apple-blue); font-weight: 500; margin-top: 6px;">
                          <strong>해석:</strong> ${escapeHtml(q.questionKo)}
                        </div>
                      </div>
                    </div>

                    <!-- 1. 파트 4 문제 타이머 (모범답안 보기 위에 배치) -->
                    <div style="margin-top: 14px;">
                      ${renderCbtTimerCard(3, qIdx >= 2 ? 30 : 15, 'p4-q-' + q.qId, qIdx >= 2 ? '답변 30초' : '답변 15초')}
                    </div>

                    <!-- 모범답안 펼침 영역 -->
                    <div id="p4-ans-${q.qId}" class="answer-collapse-box ${isAnsOpen ? 'show' : ''}">
                      <!-- 8. 모범답안 맨 위에 질문 해석 재배치 -->
                      <div class="question-translation-banner">
                        <strong>질문 해석:</strong> ${escapeHtml(q.questionKo)}
                      </div>

                      <!-- 모범답안 헤더 -->
                      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <h4 style="font-size: 15px; font-weight: 700; color: var(--apple-text);">
                          문장별 모범답안
                        </h4>
                        <button type="button" class="speech-selectable ${state.selectedItemId === q.qId + '-all' ? 'selected' : ''}"
                                data-speech-id="${q.qId}-all" data-speech-text="${escapeHtml(fullSentences)}"
                                onclick="selectSpeechItem('${q.qId}-all', this.getAttribute('data-speech-text'), true)"
                                style="padding: 4px 12px; font-size: 12px; font-weight: 600; border-radius: var(--radius-pill); border: 1px solid var(--apple-blue-border); background: var(--apple-blue-bg); color: var(--apple-blue);">
                          전체 모범답안 듣기
                        </button>
                      </div>

                      <!-- 문장 목록 -->
                      <div class="sentence-block-list">
                        ${(q.sentences || []).map((s, sIdx) => `
                          <div class="sentence-item-card speech-selectable ${state.selectedItemId === q.qId + '-ms' + sIdx ? 'selected' : ''}"
                               data-speech-id="${q.qId}-ms${sIdx}" data-speech-text="${escapeHtml(s.en)}"
                               onclick="selectSpeechItem('${q.qId}-ms${sIdx}', this.getAttribute('data-speech-text'), true)">
                            <div style="flex: 1;">
                              ${s.step ? `<span class="sentence-step-badge">${escapeHtml(s.step)}</span>` : ''}
                              <div class="sentence-en-text">${escapeHtml(s.en)}</div>
                              <div class="sentence-ko-text">${escapeHtml(s.ko)}</div>
                            </div>
                          </div>
                        `).join('')}
                      </div>

                      <!-- 2. 만능문장: 다른 만능문장 표현으로 변경 -->
                      ${q.magicSentences && q.magicSentences.length > 0 ? `
                        <div style="margin-top: 16px;">
                          <h5 style="font-size: 14px; font-weight: 700; color: var(--apple-text); margin-bottom: 8px;">
                            다른 만능문장 표현
                          </h5>
                          <div style="display: flex; flex-direction: column; gap: 8px;">
                            ${q.magicSentences.map((m, mIdx) => `
                              <div class="magic-sentence-card speech-selectable ${state.selectedItemId === q.qId + '-mg' + mIdx ? 'selected' : ''}"
                                   data-speech-id="${q.qId}-mg${mIdx}" data-speech-text="${escapeHtml(m.en)}"
                                   onclick="selectSpeechItem('${q.qId}-mg${mIdx}', this.getAttribute('data-speech-text'), true)">
                                <div>
                                  <div class="magic-sentence-en">${escapeHtml(m.en)}</div>
                                  <div class="magic-sentence-ko">${escapeHtml(m.ko)}</div>
                                  ${m.tip ? `<div class="magic-sentence-tip">💡 ${escapeHtml(m.tip)}</div>` : ''}
                                </div>
                              </div>
                            `).join('')}
                          </div>
                        </div>
                      ` : ''}

                      <!-- 어휘 -->
                      <div class="vocab-capsule-grid" style="margin-top: 16px;">
                        ${(q.vocabulary || []).map((v, vIdx) => `
                          <div class="vocab-capsule-card speech-selectable ${state.selectedItemId === q.qId + '-vv' + vIdx ? 'selected' : ''}"
                               data-speech-id="${q.qId}-vv${vIdx}" data-speech-text="${escapeHtml(v.word)}"
                               onclick="selectSpeechItem('${q.qId}-vv${vIdx}', this.getAttribute('data-speech-text'), true)">
                            <div>
                              <div>
                                <span class="vocab-word-bold">${escapeHtml(v.word)}</span>
                                <span class="vocab-ipa-subtle">${escapeHtml(v.ipa)}</span>
                              </div>
                              <div class="vocab-mean-subtle">[${escapeHtml(v.pos)}] ${escapeHtml(v.meaning)}</div>
                            </div>
                          </div>
                        `).join('')}
                      </div>

                      ${q.explanation ? `
                        <div class="explanation-callout" style="margin-top: 16px;">
                          <div class="explanation-title">💡 답변 팁</div>
                          <div class="explanation-body">${escapeHtml(q.explanation)}</div>
                        </div>
                      ` : ''}
                    </div>
                  </div>
                `;
              }).join('')}
            </div>
          </div>
        </article>
      `;
    }

    // =========================================================================
    // 2. 만능문장 187 & 빈출 단어장 모달
    // =========================================================================
    function toggleVocabModal() {
      state.isVocabModalOpen = !state.isVocabModalOpen;
      const backdrop = document.getElementById('vocabModalBackdrop');
      if (state.isVocabModalOpen) {
        backdrop.classList.add('active');
        updateModalModeButtonsUI();
        renderModalPartFilters();
        renderModalVocabList();
      } else {
        backdrop.classList.remove('active');
        stopSpeech();
      }
    }

    function handleModalBackdropClick(e) {
      if (e.target.id === 'vocabModalBackdrop') {
        toggleVocabModal();
      }
    }

    function setModalMainMode(mode) {
      if (state.modalMainMode === mode) return;
      state.modalMainMode = mode;
      if (state.modalPartFilter !== 'SAVED') {
        state.modalPartFilter = mode === 'magic' ? '2' : '1';
      }
      updateModalModeButtonsUI();
      renderModalPartFilters();
      renderModalVocabList();
    }

    function toggleModalSavedFilter() {
      if (state.modalPartFilter === 'SAVED') {
        state.modalPartFilter = state.modalMainMode === 'magic' ? '2' : '1';
      } else {
        state.modalPartFilter = 'SAVED';
      }
      renderModalPartFilters();
      renderModalVocabList();
    }

    function updateModalModeButtonsUI() {
      const btnMagic = document.getElementById('btnModeMagic');
      const btnVocab = document.getElementById('btnModeVocab');
      if (btnMagic) btnMagic.classList.toggle('active', state.modalMainMode === 'magic');
      if (btnVocab) btnVocab.classList.toggle('active', state.modalMainMode === 'vocab');
    }

    /* 7. 파트 선택 세그먼트 탭: 전체와 저장됨 삭제 & 좌측 북마크 버튼 분리 */
    function renderModalPartFilters() {
      const isMagic = state.modalMainMode === 'magic';
      const magicSavedCount = Object.keys(state.bookmarkedMagicIds).length;
      const vocabSavedCount = Object.keys(state.bookmarkedVocabIds).length;
      const curSavedCount = isMagic ? magicSavedCount : vocabSavedCount;

      // 좌측 북마크 버튼 상태 & 뱃지 숫자 갱신
      const bookmarkBtn = document.getElementById('btnModalBookmarkFilter');
      const countBadge = document.getElementById('modalBookmarkCountBadge');
      if (bookmarkBtn) {
        bookmarkBtn.classList.toggle('active', state.modalPartFilter === 'SAVED');
      }
      if (countBadge) {
        countBadge.textContent = curSavedCount;
      }

      // 파트 선택 탭 (전체와 저장됨 삭제, 파트 탭만 순수하게 배치)
      let filters = [];
      if (isMagic) {
        filters = [
          { id: '2', name: 'Part 2', count: 49 },
          { id: '3', name: 'Part 3', count: 47 },
          { id: '4', name: 'Part 4', count: 38 },
          { id: '5', name: 'Part 5', count: 53 }
        ];
      } else {
        filters = [
          { id: '1', name: 'Part 1', count: 24 },
          { id: '2', name: 'Part 2', count: 24 },
          { id: '3', name: 'Part 3', count: 24 },
          { id: '4', name: 'Part 4', count: 24 },
          { id: '5', name: 'Part 5', count: 24 }
        ];
      }

      const c = document.getElementById('modalPartFilterContainer');
      if (c) {
        c.innerHTML = filters.map(f => `
          <button type="button" role="tab" class="modal-segment-btn ${state.modalPartFilter === f.id ? 'active' : ''}"
            onclick="setModalPartFilter('${f.id}')">
            <span>${f.name}</span>
          </button>
        `).join('');
      }
    }

    function setModalPartFilter(filterId) {
      state.modalPartFilter = filterId;
      renderModalPartFilters();
      renderModalVocabList();
    }

    function handleModalSearch(val) {
      state.modalSearchQuery = val;
      renderModalVocabList();
    }

    function toggleBookmark(id, type) {
      if (type === 'magic') {
        if (state.bookmarkedMagicIds[id]) {
          delete state.bookmarkedMagicIds[id];
        } else {
          state.bookmarkedMagicIds[id] = true;
        }
        localStorage.setItem('toeic_saved_magic_sentences', JSON.stringify(state.bookmarkedMagicIds));
      } else {
        if (state.bookmarkedVocabIds[id]) {
          delete state.bookmarkedVocabIds[id];
        } else {
          state.bookmarkedVocabIds[id] = true;
        }
        localStorage.setItem('toeic_saved_vocab_words', JSON.stringify(state.bookmarkedVocabIds));
      }
      renderModalPartFilters();
      renderModalVocabList();
    }

    function renderModalVocabList() {
      const q = (state.modalSearchQuery || '').trim().toLowerCase();
      const isMagic = state.modalMainMode === 'magic';
      const grid = document.getElementById('modalVocabGrid');

      if (isMagic) {
        const savedCount = Object.keys(state.bookmarkedMagicIds).length;
        const bEl = document.getElementById('modalBookmarkCountBadge');
        if (bEl) bEl.textContent = savedCount;

        const filtered = MAGIC_DATA.items.filter(item => {
          if (state.modalPartFilter === 'SAVED') {
            if (!state.bookmarkedMagicIds[item.id]) return false;
          } else if (state.modalPartFilter !== 'ALL' && String(item.part) !== state.modalPartFilter) {
            return false;
          }
          if (q) {
            return (
              item.en.toLowerCase().includes(q) ||
              item.ko.toLowerCase().includes(q) ||
              item.category.toLowerCase().includes(q) ||
              item.id.toLowerCase().includes(q) ||
              (item.tip || '').toLowerCase().includes(q)
            );
          }
          return true;
        });

        if (filtered.length === 0) {
          grid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 48px 16px; color: var(--apple-text-muted);">
              ${state.modalPartFilter === 'SAVED' ? '저장된 만능문장이 없습니다. 우측 상단 책갈피 아이콘을 눌러 저장해보세요.' : '검색 결과가 없습니다.'}
            </div>
          `;
          return;
        }

        grid.innerHTML = filtered.map(item => {
          const isSaved = !!state.bookmarkedMagicIds[item.id];
          return `
            <div class="vocab-item-card ${isSaved ? 'saved' : ''}">
              <!-- 본문 문장과 북마크 버튼을 같은 줄(같은 선상)에 배치 -->
              <div class="magic-sentence-main-group" style="display: flex; align-items: flex-start; justify-content: space-between; gap: 10px;">
                <div style="display: flex; align-items: flex-start; gap: 10px; flex: 1; min-width: 0;">
                  <button type="button" class="btn-audio-front" onclick="speakMagicItem('${item.id}', 1.0)" title="발음 듣기" aria-label="발음 듣기"
                          style="width: 32px; height: 32px; border-radius: 50%; border: 1px solid var(--apple-blue-border); background: var(--apple-blue-bg); color: var(--apple-blue); display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0; cursor: pointer; margin-top: 2px;">
                    <svg style="width: 15px; height: 15px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                      <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                    </svg>
                  </button>
                  <div style="flex: 1; min-width: 0;">
                    <div class="magic-en-sentence">${escapeHtml(item.en)}</div>
                    <div class="magic-ko-translation">${escapeHtml(item.ko)}</div>
                  </div>
                </div>
                <button type="button" class="btn-bookmark-icon ${isSaved ? 'saved' : ''}" onclick="toggleBookmark('${item.id}', 'magic')" aria-label="저장" title="${isSaved ? '저장 해제' : '저장'}" style="flex-shrink: 0;">
                  <svg viewBox="0 0 24 24" fill="${isSaved ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M19 21l-7-4.5L5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
                  </svg>
                </button>
              </div>

              ${item.tip ? `
                <div class="vocab-exam-tip-box">
                  <span class="tip-icon-label">💡 만능 팁:</span>
                  <span class="tip-content-text">${escapeHtml(item.tip)}</span>
                </div>
              ` : ''}
            </div>
          `;
        }).join('');
      } else {
        // 단어장 모드
        const savedCount = Object.keys(state.bookmarkedVocabIds).length;
        const bEl = document.getElementById('modalBookmarkCountBadge');
        if (bEl) bEl.textContent = savedCount;

        const filtered = VOCAB_DATA.items.filter(item => {
          if (state.modalPartFilter === 'SAVED') {
            if (!state.bookmarkedVocabIds[item.id]) return false;
          } else if (state.modalPartFilter !== 'ALL' && String(item.part) !== state.modalPartFilter) {
            return false;
          }
          if (q) {
            return (
              item.word.toLowerCase().includes(q) ||
              item.meaning.toLowerCase().includes(q) ||
              (item.ipa || '').toLowerCase().includes(q) ||
              item.category.toLowerCase().includes(q) ||
              item.id.toLowerCase().includes(q) ||
              (item.collocation || '').toLowerCase().includes(q) ||
              (item.example || '').toLowerCase().includes(q) ||
              (item.exampleKo || '').toLowerCase().includes(q) ||
              (item.tip || '').toLowerCase().includes(q)
            );
          }
          return true;
        });

        if (filtered.length === 0) {
          grid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 48px 16px; color: var(--apple-text-muted);">
              ${state.modalPartFilter === 'SAVED' ? '저장된 단어가 없습니다. 우측 상단 책갈피 아이콘을 눌러 저장해보세요.' : '검색 결과가 없습니다.'}
            </div>
          `;
          return;
        }

        grid.innerHTML = filtered.map(item => {
          const isSaved = !!state.bookmarkedVocabIds[item.id];
          return `
            <div class="vocab-word-card ${isSaved ? 'saved' : ''}">
              <!-- 표제어/스피커와 북마크 버튼을 같은 줄(같은 선상)에 배치 -->
              <div class="vocab-headword-section" style="display: flex; align-items: center; justify-content: space-between; gap: 8px; width: 100%;">
                <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap; flex: 1; min-width: 0;">
                  <button type="button" class="btn-audio-front" onclick="speakVocabItem('${item.id}', 1.0)" title="발음 듣기" aria-label="발음 듣기"
                          style="width: 32px; height: 32px; border-radius: 50%; border: 1px solid var(--apple-blue-border); background: var(--apple-blue-bg); color: var(--apple-blue); display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0; cursor: pointer;">
                    <svg style="width: 15px; height: 15px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                      <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                    </svg>
                  </button>
                  <span class="vocab-word-text">${escapeHtml(item.word)}</span>
                  <span class="vocab-word-ipa">${escapeHtml(item.ipa)}</span>
                  <span class="vocab-word-pos-tag">${escapeHtml(item.pos)}</span>
                </div>
                <button type="button" class="btn-bookmark-icon ${isSaved ? 'saved' : ''}" onclick="toggleBookmark('${item.id}', 'vocab')" aria-label="저장" title="${isSaved ? '저장 해제' : '저장'}" style="flex-shrink: 0;">
                  <svg viewBox="0 0 24 24" fill="${isSaved ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M19 21l-7-4.5L5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
                  </svg>
                </button>
              </div>

              <!-- 3. 핵심 뜻 -->
              <div class="vocab-meaning-block">
                <div class="vocab-meaning-text">${escapeHtml(item.meaning)}</div>
              </div>

              <!-- 4. 자주 쓰이는 표현 (연어구) -->
              ${item.collocation ? `
                <div class="vocab-collocation-card">
                  <span class="collocation-tag">자주 쓰이는 표현</span>
                  <span class="collocation-phrase">${escapeHtml(item.collocation)}</span>
                </div>
              ` : ''}

              <!-- 5. 실전 기출 예문 -->
              ${item.example ? `
                <div class="vocab-example-block">
                  <div class="example-en-sentence">"${escapeHtml(item.example)}"</div>
                  <div class="example-ko-translation">${escapeHtml(item.exampleKo || '')}</div>
                </div>
              ` : ''}

              <!-- 6. 출제 포인트 및 발음 팁 -->
              ${item.tip ? `
                <div class="vocab-exam-tip-box">
                  <span class="tip-icon-label">💡 기출 팁:</span>
                  <span class="tip-content-text">${escapeHtml(item.tip)}</span>
                </div>
              ` : ''}
            </div>
          `;
        }).join('');
      }
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        if (state.isVocabModalOpen) toggleVocabModal();
        closeDrawer();
      }
    });

    // 초기 실행
    initTheme();
    renderSegmentedTabs();
    renderMainViewport();
  </script>
</body>
</html>
"""

    html_content = (
        html_template
        .replace("__MASTER_JSON__", master_json_str)
        .replace("__MAGIC_JSON__", magic_json_str)
        .replace("__VOCAB_JSON__", vocab_json_str)
    )

    target_path = ROOT / "toeicspk_cbt2026.html"
    target_path.write_text(html_content, encoding="utf-8")
    print(f"✅ 독립 실행형 토익스피킹 CBT HTML 생성 완료: {target_path} ({target_path.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
