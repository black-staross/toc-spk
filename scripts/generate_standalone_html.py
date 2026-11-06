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

    master_json_str = json.dumps(master_data, ensure_ascii=False)
    magic_json_str = json.dumps(magic_data, ensure_ascii=False)

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
      background: radial-gradient(circle at 15% 15%, #FFFFFF 0%, #F5F5F7 60%, #EBEBF0 100%);
      background-attachment: fixed;
      color: var(--apple-text);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
      padding-bottom: 90px;
    }

    /* iOS 리퀴드 글래스 헤더 */
    .apple-header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.78);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border-bottom: 1px solid var(--apple-border-subtle);
      transition: background 0.3s ease;
    }

    .header-inner {
      max-width: 1240px;
      margin: 0 auto;
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    /* 다크모드 테마 스타일 */
    body.dark {
      --apple-bg: #000000;
      --apple-bg-subtle: #121214;
      --apple-card-bg: rgba(28, 28, 30, 0.88);
      --apple-card-solid: #1C1C1E;
      --apple-card-inner: rgba(44, 44, 46, 0.7);
      --apple-border: rgba(255, 255, 255, 0.14);
      --apple-border-subtle: rgba(255, 255, 255, 0.08);
      --apple-text: #F5F5F7;
      --apple-text-secondary: #A1A1A6;
      --apple-text-muted: #6E6E73;
      --apple-blue: #0A84FF;
      --apple-blue-hover: #409CFF;
      --apple-blue-bg: rgba(10, 132, 255, 0.18);
      --apple-blue-border: rgba(10, 132, 255, 0.4);
      background: radial-gradient(circle at 15% 15%, #1C1C1E 0%, #0D0D0E 60%, #000000 100%) !important;
      background-attachment: fixed !important;
      color: #F5F5F7 !important;
    }
    body.dark .apple-header {
      background: rgba(20, 20, 22, 0.82) !important;
      border-bottom-color: rgba(255, 255, 255, 0.1) !important;
    }
    body.dark .apple-segmented-bar {
      background: rgba(20, 20, 22, 0.8) !important;
      border-bottom-color: rgba(255, 255, 255, 0.08) !important;
    }
    body.dark .segmented-control {
      background: rgba(255, 255, 255, 0.08) !important;
      border-color: rgba(255, 255, 255, 0.08) !important;
    }
    body.dark .segment-btn.active {
      background: rgba(255, 255, 255, 0.18) !important;
      color: #FFFFFF !important;
    }
    body.dark .glass-card {
      background: rgba(28, 28, 30, 0.85) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4) !important;
    }
    body.dark .p1-full-passage-card {
      background: rgba(38, 38, 42, 0.95) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .floating-bottom-bar {
      background: rgba(28, 28, 30, 0.92) !important;
      border-color: rgba(255, 255, 255, 0.16) !important;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5) !important;
    }
    body.dark .part4-clean-table thead tr {
      background: #2C2C2E !important;
      color: #F5F5F7 !important;
    }
    body.dark .part4-clean-table tbody tr {
      background: #1C1C1E !important;
      color: #F5F5F7 !important;
    }
    body.dark .part4-clean-table tbody tr:hover {
      background: rgba(255, 255, 255, 0.04) !important;
    }
    body.dark .table-meta-pills {
      background: #242426 !important;
      border-color: rgba(255, 255, 255, 0.08) !important;
      color: #A1A1A6 !important;
    }
    body.dark .glass-drawer {
      background: rgba(28, 28, 30, 0.95) !important;
      border-right-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .vocab-modal-window {
      background: rgba(28, 28, 30, 0.96) !important;
      border-color: rgba(255, 255, 255, 0.15) !important;
    }
    body.dark .vocab-search-input {
      background: rgba(44, 44, 46, 0.8) !important;
      border-color: rgba(255, 255, 255, 0.15) !important;
      color: #F5F5F7 !important;
    }
    body.dark .question-prompt-card {
      background: rgba(38, 38, 42, 0.9) !important;
      border-color: rgba(255, 255, 255, 0.1) !important;
    }
    body.dark .p4-lc-question-card {
      background: rgba(38, 38, 42, 0.8) !important;
      border-color: rgba(255, 255, 255, 0.1) !important;
    }
    body.dark .btn-circle-nav {
      background: rgba(44, 44, 46, 0.8) !important;
      color: #F5F5F7 !important;
      border-color: rgba(255, 255, 255, 0.15) !important;
    }
    body.dark .btn-floating-drawer,
    body.dark .btn-floating-nav {
      color: #F5F5F7 !important;
    }
    body.dark .btn-floating-drawer {
      background: rgba(255, 255, 255, 0.08) !important;
      border-color: rgba(255, 255, 255, 0.12) !important;
    }
    body.dark .btn-floating-drawer:hover {
      background: rgba(255, 255, 255, 0.15) !important;
    }
    body.dark .tag-time {
      background: rgba(255, 255, 255, 0.1) !important;
      color: #A1A1A6 !important;
    }

    .brand-title-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* 3. 다크모드 iOS 슬라이딩 스위치 토글 (시인성 극대화) */
    .theme-switch {
      position: relative;
      width: 62px;
      height: 32px;
      border-radius: var(--radius-pill);
      background: #E5E5EA;
      border: 1px solid rgba(0, 0, 0, 0.12);
      cursor: pointer;
      padding: 0;
      outline: none;
      display: inline-flex;
      align-items: center;
      transition: background 0.28s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.28s ease, box-shadow 0.28s ease, transform 0.18s ease;
      box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
      user-select: none;
      -webkit-user-select: none;
      flex-shrink: 0;
    }
    .theme-switch:hover {
      transform: scale(1.04);
    }
    body.dark .theme-switch {
      background: var(--apple-blue);
      border-color: rgba(10, 132, 255, 0.6);
      box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2), 0 0 14px rgba(10, 132, 255, 0.4);
    }
    .theme-switch-track-icons {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 7px;
      font-size: 11px;
      pointer-events: none;
    }
    .theme-switch-track-icons .track-sun {
      opacity: 0;
      transition: opacity 0.2s ease;
      color: rgba(255, 255, 255, 0.85);
    }
    body.dark .theme-switch-track-icons .track-sun {
      opacity: 0.85;
    }
    .theme-switch-track-icons .track-moon {
      opacity: 0.55;
      transition: opacity 0.2s ease;
      color: #3C3C43;
    }
    body.dark .theme-switch-track-icons .track-moon {
      opacity: 0;
    }
    .theme-switch-thumb {
      position: absolute;
      left: 3px;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #FFFFFF;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.22), 0 0 1px rgba(0, 0, 0, 0.15);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      line-height: 1;
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), background 0.28s ease;
      pointer-events: none;
    }
    body.dark .theme-switch-thumb {
      transform: translateX(30px);
      background: #FFFFFF;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35);
    }

    .brand-main-title {
      font-size: 18px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--apple-text);
    }

    /* 제목 옆 단어장 토글 버튼 */
    .btn-vocab-toggle {
      background: rgba(0, 113, 227, 0.08);
      color: var(--apple-blue);
      border: 1px solid var(--apple-blue-border);
      border-radius: var(--radius-pill);
      padding: 6px 14px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .btn-vocab-toggle:hover {
      background: rgba(0, 113, 227, 0.16);
      transform: scale(1.02);
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

    /* iOS 세그먼트 컨트롤 탭 */
    .apple-segmented-bar {
      max-width: 1240px;
      margin: 18px auto 0;
      padding: 0 24px;
    }

    .segmented-control {
      display: flex;
      background: rgba(0, 0, 0, 0.05);
      padding: 4px;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(0, 0, 0, 0.04);
      overflow-x: auto;
      gap: 3px;
    }

    .segment-btn {
      flex: 1;
      min-width: 130px;
      background: transparent;
      border: none;
      border-radius: var(--radius-pill);
      padding: 9px 16px;
      font-size: 14px;
      font-weight: 600;
      color: var(--apple-text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
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

    /* 메인 뷰포트 레이아웃 */
    .main-viewport {
      max-width: 1040px;
      margin: 24px auto 100px;
      padding: 0 24px;
    }

    /* 리퀴드 글래스 메인 카드 */
    .glass-card {
      background: var(--apple-card);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--apple-border);
      border-radius: var(--radius-lg);
      padding: 32px;
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
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 10px;
    }

    .timer-stage-badge {
      font-size: 12px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      letter-spacing: -0.01em;
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
      font-family: 'JetBrains Mono', monospace;
      font-size: 24px;
      font-weight: 700;
      color: var(--apple-text);
      font-variant-numeric: tabular-nums;
      letter-spacing: -0.02em;
    }

    .timer-btn-actions {
      display: flex;
      gap: 6px;
      align-items: center;
    }

    .btn-timer-ctrl {
      background: #FFFFFF;
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-pill);
      padding: 5px 13px;
      font-size: 12px;
      font-weight: 600;
      color: var(--apple-text);
      cursor: pointer;
      box-shadow: var(--apple-shadow-sm);
      transition: all 0.16s ease;
    }
    .btn-timer-ctrl:hover {
      background: #F8F8FA;
      border-color: var(--apple-border-strong);
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
      padding: 5px 14px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.16s ease;
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
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      padding: 6px 13px;
      border-radius: var(--radius-pill);
      transition: all 0.16s ease;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    .btn-floating-drawer:hover {
      background: rgba(0, 0, 0, 0.1);
      border-color: rgba(0, 0, 0, 0.15);
    }

    .btn-floating-nav {
      background: transparent;
      border: none;
      color: var(--apple-text);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      padding: 5px 10px;
      border-radius: var(--radius-pill);
      transition: background 0.16s ease;
    }
    .btn-floating-nav:hover:not(:disabled) {
      background: rgba(0, 0, 0, 0.06);
    }
    .btn-floating-nav:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }

    .floating-nav-info {
      font-size: 12px;
      font-weight: 600;
      color: var(--apple-text-secondary);
      border-left: 1px solid var(--apple-border-subtle);
      border-right: 1px solid var(--apple-border-subtle);
      padding: 0 12px;
      font-variant-numeric: tabular-nums;
    }

    .btn-floating-stop {
      background: var(--apple-red-bg);
      color: var(--apple-red);
      border: 1px solid var(--apple-red-border);
      border-radius: var(--radius-pill);
      padding: 5px 12px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.16s ease;
    }
    .btn-floating-stop:hover {
      background: rgba(255, 59, 48, 0.2);
    }

    /* 1. 하단 플로팅 바 배속 토글 버튼 (1.0x, 0.75x) */
    .btn-floating-rate {
      background: rgba(0, 113, 227, 0.08);
      border: 1px solid var(--apple-blue-border);
      color: var(--apple-blue);
      font-size: 12px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.18s ease;
    }
    .btn-floating-rate:hover {
      background: var(--apple-blue);
      color: #FFFFFF;
      transform: scale(1.05);
    }
    .btn-floating-rate.active-playing {
      background: var(--apple-blue) !important;
      color: #FFFFFF !important;
      box-shadow: 0 0 12px rgba(0, 113, 227, 0.5);
      animation: pulseRate 1.4s infinite;
    }
    @keyframes pulseRate {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.04); opacity: 0.85; }
    }

    /* 2. 파트 3, 4 유형 및 속성 필터 바 (가독성 & 린 디자인 강화) */
    .filter-chips-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 22px;
      padding: 6px 12px;
      background: rgba(255, 255, 255, 0.7);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-pill);
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.03);
    }
    body.dark .filter-chips-row {
      background: rgba(28, 28, 30, 0.7);
      border-color: rgba(255, 255, 255, 0.1);
    }

    .filter-chips-label {
      font-size: 12px;
      font-weight: 700;
      color: var(--apple-text-secondary);
      padding: 0 4px 0 4px;
      letter-spacing: -0.01em;
      user-select: none;
    }

    .chip-filter-btn {
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--apple-border);
      color: var(--apple-text);
      font-size: 13px;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      white-space: nowrap;
      user-select: none;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }
    .chip-filter-btn:hover:not(.active) {
      background: #FFFFFF;
      border-color: var(--apple-blue-border);
      color: var(--apple-blue);
      transform: translateY(-1px);
    }
    .chip-filter-btn.active {
      background: var(--apple-blue) !important;
      color: #FFFFFF !important;
      border-color: var(--apple-blue) !important;
      font-weight: 700;
      box-shadow: 0 3px 10px rgba(0, 113, 227, 0.35) !important;
      transform: translateY(-1px);
    }
    body.dark .chip-filter-btn {
      background: rgba(44, 44, 46, 0.85);
      border-color: rgba(255, 255, 255, 0.14);
      color: #E5E5EA;
    }
    body.dark .chip-filter-btn:hover:not(.active) {
      background: rgba(58, 58, 60, 0.95);
      border-color: rgba(255, 255, 255, 0.3);
      color: #FFFFFF;
    }
    body.dark .chip-filter-btn.active {
      background: #0A84FF !important;
      color: #FFFFFF !important;
      border-color: #0A84FF !important;
      box-shadow: 0 3px 12px rgba(10, 132, 255, 0.45) !important;
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
      border-radius: var(--radius-lg);
      width: 980px;
      max-width: 95vw;
      height: 85vh;
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

    .vocab-modal-header {
      padding: 20px 26px;
      border-bottom: 1px solid var(--apple-border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }

    .vocab-search-input {
      padding: 8px 14px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--apple-border-strong);
      background: rgba(255, 255, 255, 0.85);
      font-size: 13px;
      min-width: 260px;
      outline: none;
    }

    .vocab-modal-body {
      flex: 1;
      overflow-y: auto;
      padding: 20px 26px;
    }

    .vocab-grid-cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
      gap: 12px;
    }

    @media (max-width: 600px) {
      .vocab-grid-cards {
        grid-template-columns: 1fr;
      }
    }

    .vocab-item-card {
      background: rgba(255, 255, 255, 0.85);
      border: 1px solid var(--apple-border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 10px;
      transition: border-color 0.16s ease;
    }

    .vocab-item-card.memorized {
      background: rgba(52, 199, 89, 0.08);
      border-color: rgba(52, 199, 89, 0.35);
    }

    .btn-mem-toggle {
      background: transparent;
      border: 1px solid var(--apple-border-strong);
      border-radius: var(--radius-pill);
      padding: 3px 9px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      color: var(--apple-text-secondary);
    }

    .btn-mem-toggle.checked {
      background: var(--apple-emerald);
      color: #FFFFFF;
      border-color: var(--apple-emerald);
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
      .theme-switch {
        width: 52px;
        height: 28px;
      }
      .theme-switch-thumb {
        width: 20px;
        height: 20px;
        font-size: 11px;
        left: 3px;
      }
      body.dark .theme-switch-thumb {
        transform: translateX(25px);
      }
      .theme-switch-track-icons {
        padding: 0 6px;
        font-size: 10px;
      }
      .brand-main-title {
        font-size: 15px;
        letter-spacing: -0.03em;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .btn-vocab-toggle {
        padding: 5px 10px;
        font-size: 12px;
        gap: 4px;
        flex-shrink: 0;
      }

      /* 세그먼트 컨트롤 탭 */
      .apple-segmented-bar {
        padding: 0 10px;
        margin-top: 8px;
      }
      .segmented-control {
        padding: 3px;
        gap: 2px;
        scrollbar-width: none;
        -ms-overflow-style: none;
      }
      .segmented-control::-webkit-scrollbar {
        display: none;
      }
      .segment-btn {
        min-width: auto;
        padding: 6px 10px;
        font-size: 12px;
        gap: 5px;
      }
      .segment-count {
        font-size: 10px;
        padding: 1px 5px;
      }

      /* 메인 뷰포트 & 카드 */
      .main-viewport {
        padding: 0 12px;
        margin: 14px auto 110px;
      }
      .filter-chips-row {
        gap: 6px;
        padding: 5px 8px;
        margin-bottom: 16px;
        overflow-x: auto;
        flex-wrap: nowrap;
        scrollbar-width: none;
        -ms-overflow-style: none;
      }
      .filter-chips-row::-webkit-scrollbar {
        display: none;
      }
      .chip-filter-btn {
        padding: 5px 11px;
        font-size: 12px;
      }
      .glass-card {
        padding: 16px;
        border-radius: 20px;
      }
      .glass-card-header {
        flex-direction: column;
        align-items: stretch;
        gap: 12px;
        padding-bottom: 14px;
        margin-bottom: 16px;
      }
      .header-card-nav {
        width: 100%;
        display: flex;
        justify-content: space-between;
      }
      .btn-circle-nav {
        flex: 1;
        justify-content: center;
        padding: 8px 12px;
      }
      .card-title-lg {
        font-size: 18px;
        line-height: 1.35;
      }

      /* Part 1 전체 지문 & 문장 카드 */
      .p1-full-passage-card {
        padding: 16px;
        margin-bottom: 18px;
        border-radius: 16px;
      }
      .p1-passage-text {
        font-size: 16px;
        line-height: 1.55;
      }
      .sentence-item-card {
        padding: 14px;
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
      }
      .sentence-en-text {
        font-size: 15px;
      }
      .vocab-grid {
        grid-template-columns: 1fr;
        gap: 8px;
      }

      /* Part 2 사진 영역 */
      .part2-hero-image-wrap {
        max-height: 300px;
        border-radius: 16px;
        margin-bottom: 18px;
      }
      .part2-hero-image {
        max-height: 300px;
        object-fit: cover;
      }

      /* Part 4 표(Table) 영역 (가로 스크롤 보장) */
      .part4-table-card {
        padding: 12px;
        border-radius: 16px;
        margin-bottom: 18px;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }
      .part4-clean-table {
        min-width: 480px;
        font-size: 12px;
      }
      .part4-clean-table th,
      .part4-clean-table td {
        padding: 8px 10px;
      }

      /* CBT 실전 타이머 */
      .cbt-timer-card {
        padding: 16px;
        flex-direction: column;
        text-align: center;
        gap: 14px;
        border-radius: 18px;
      }
      .timer-meta-group {
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 8px;
      }
      .timer-digits-box {
        font-size: 26px;
        padding: 4px 14px;
      }
      .timer-btn-group {
        width: 100%;
        display: flex;
        justify-content: center;
      }
      .btn-timer-action {
        flex: 1;
        justify-content: center;
        padding: 9px 16px;
      }

      /* 하단 고정 플로팅 바 (모바일 엄지손가락 최적화) */
      .floating-bottom-bar {
        bottom: max(22px, env(safe-area-inset-bottom, 22px));
        width: calc(100% - 20px);
        max-width: 440px;
        padding: 5px 8px;
        gap: 3px;
        justify-content: space-between;
      }
      .btn-floating-drawer {
        padding: 6px 9px;
        font-size: 11px;
      }
      .btn-floating-nav {
        padding: 6px 7px;
        font-size: 12px;
      }
      .floating-nav-info {
        padding: 0 4px;
        font-size: 11px;
      }
      .btn-floating-stop {
        padding: 6px 8px;
        font-size: 11px;
      }
      .btn-floating-rate {
        padding: 6px 7px;
        font-size: 11px;
      }
      .floating-divider {
        margin: 0 1px !important;
      }

      /* 문항 목록 드로어 */
      .drawer-panel {
        width: 88vw;
        max-width: 340px;
      }
      .drawer-header {
        padding: 16px 18px;
      }
      .drawer-body {
        padding: 12px 14px;
      }

      /* 단어장 모달 */
      .vocab-modal-card {
        width: 95vw;
        max-height: 92vh;
        border-radius: 20px;
      }
      .vocab-modal-header {
        padding: 16px 18px;
      }
      .vocab-modal-body {
        padding: 14px;
      }
      .vocab-grid-cards {
        grid-template-columns: 1fr;
        gap: 10px;
      }
    }
  </style>
</head>
<body>

  <!-- 상단 글래스 헤더 -->
  <header class="apple-header">
    <div class="header-inner">
      <div class="brand-title-wrap">
        <!-- 3. 다크모드 iOS 슬라이딩 스위치 토글 (상단 맨 왼쪽 ETS CBT MASTER 대신 배치) -->
        <button type="button" class="theme-switch" id="themeSwitch" onclick="toggleDarkMode()" title="다크/라이트 모드 전환" aria-label="다크 모드 전환">
          <div class="theme-switch-track-icons">
            <span class="track-sun">☀️</span>
            <span class="track-moon">🌙</span>
          </div>
          <div class="theme-switch-thumb" id="themeThumb">☀️</div>
        </button>
        <h1 class="brand-main-title">토익스피킹 기출 마스터</h1>
      </div>

      <div class="header-actions">
        <!-- 4. 오른쪽 상단에 단어장 배치 (모바일 축약 지원) -->
        <button type="button" class="btn-vocab-toggle" onclick="toggleVocabModal()">
          <span>📖</span>
          <span class="btn-text-full"> 시계토끼 만능문장 187</span>
          <span class="btn-text-short"> 만능문장</span>
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
    <button type="button" class="btn-floating-drawer" onclick="openDrawer()">
      <span>☰</span>
      <span class="btn-text-full"> 문항 목록</span>
      <span class="btn-text-short"> 목록</span>
    </button>
    <div class="floating-divider" style="width: 1px; height: 16px; background: rgba(127,127,127,0.25); margin: 0 2px;"></div>
    <button type="button" class="btn-floating-nav" id="btnFloatingPrev" onclick="navPrev()">
      <span class="btn-text-full">← 이전</span>
      <span class="btn-text-short">←</span>
    </button>
    <span class="floating-nav-info" id="floatingNavText">1 / 10</span>
    <button type="button" class="btn-floating-nav" id="btnFloatingNext" onclick="navNext()">
      <span class="btn-text-full">다음 →</span>
      <span class="btn-text-short">→</span>
    </button>
    <div class="floating-divider" style="width: 1px; height: 16px; background: rgba(127,127,127,0.25); margin: 0 2px;"></div>
    <button type="button" class="btn-floating-stop" id="btnFloatingStop" onclick="stopSpeech()">
      <span>⏹</span>
      <span class="btn-text-full"> 정지</span>
    </button>
    <button type="button" class="btn-floating-rate" id="btnFloatingRate10" onclick="playSelectedRate(1.0)">1.0x</button>
    <button type="button" class="btn-floating-rate" id="btnFloatingRate075" onclick="playSelectedRate(0.75)">0.75x</button>
  </aside>

  <!-- 문항 목록 리퀴드 글래스 사이드 드로어 -->
  <div class="drawer-overlay" id="drawerOverlay" onclick="closeDrawer()"></div>
  <aside class="glass-drawer" id="glassDrawer" aria-label="문항 목록">
    <div class="drawer-header">
      <span class="drawer-title" id="drawerTitleText">문항 목록</span>
      <button type="button" class="btn-drawer-close" onclick="closeDrawer()">✕</button>
    </div>
    <div class="drawer-scroll-body" id="drawerListContainer"></div>
  </aside>

  <!-- 시계토끼 만능문장 187 리퀴드 글래스 모달 -->
  <div class="vocab-modal-backdrop" id="vocabModalBackdrop" onclick="handleModalBackdropClick(event)">
    <div class="vocab-modal-window" onclick="event.stopPropagation()">
      <div class="vocab-modal-header">
        <div>
          <h2 style="font-size: 18px; font-weight: 700; color: var(--apple-text);">🐰 시계토끼 만능문장 187 단어장</h2>
          <p style="font-size: 12.5px; color: var(--apple-text-secondary); margin-top: 2px;">
            Part 2~5 완벽 구성 · 원어민 Daniel 음성 고정 · 암기 완료: <strong id="modalMemCount">0</strong> / 187개
          </p>
        </div>
        <div style="display: flex; gap: 8px; align-items: center;">
          <input type="search" class="vocab-search-input" id="modalVocabSearch" placeholder="표현, 한국어 뜻 검색..." oninput="handleModalSearch(this.value)" />
          <button type="button" class="btn-drawer-close" onclick="toggleVocabModal()">✕</button>
        </div>
      </div>
      <div style="padding: 12px 26px; border-bottom: 1px solid var(--apple-border-subtle); display: flex; gap: 6px; flex-wrap: wrap;" id="modalPartFilterContainer"></div>
      <div class="vocab-modal-body">
        <div class="vocab-grid-cards" id="modalVocabGrid"></div>
      </div>
    </div>
  </div>

  <script>
    const MASTER_DATA = __MASTER_JSON__;
    const MAGIC_DATA = __MAGIC_JSON__; // Part 2~5 순수 187개

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
      modalPartFilter: 'ALL',
      modalSearchQuery: '',
      memorizedIds: JSON.parse(localStorage.getItem('toeic_memorized_187') || '{}'),
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

    // 3. 다크모드 iOS 스위치 토글 함수
    function toggleDarkMode() {
      state.isDarkMode = !state.isDarkMode;
      document.body.classList.toggle('dark', state.isDarkMode);
      const thumb = document.getElementById('themeThumb');
      if (thumb) thumb.textContent = state.isDarkMode ? '🌙' : '☀️';
      localStorage.setItem('toeic_dark_mode', state.isDarkMode ? 'true' : 'false');
    }

    function initTheme() {
      if (state.isDarkMode) {
        document.body.classList.add('dark');
        const thumb = document.getElementById('themeThumb');
        if (thumb) thumb.textContent = '🌙';
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

    // 2. 발음 선택형 칸 클릭 시 호출 함수
    function selectSpeechItem(id, text) {
      state.selectedItemId = id;
      state.selectedSpeechText = text;
      document.querySelectorAll('.speech-selectable').forEach(el => {
        if (el.getAttribute('data-speech-id') === id) {
          el.classList.add('selected');
        } else {
          el.classList.remove('selected');
        }
      });
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

    function resetTimer(prepSec = null, respSec = null) {
      if (state.timerInterval) {
        clearInterval(state.timerInterval);
        state.timerInterval = null;
      }
      if (prepSec !== null) state.timerPrepLimit = prepSec;
      if (respSec !== null) state.timerResponseLimit = respSec;

      state.timerStage = 'standby';
      state.timerTotalSeconds = state.timerPrepLimit;
      state.timerRemainingSeconds = state.timerPrepLimit;
      updateTimerUI();
    }

    function toggleTimer() {
      if (state.timerInterval) {
        // 일시정지
        clearInterval(state.timerInterval);
        state.timerInterval = null;
        updateTimerUI();
        return;
      }

      if (state.timerStage === 'standby' || state.timerStage === 'ended') {
        state.timerStage = 'prep';
        state.timerTotalSeconds = state.timerPrepLimit;
        state.timerRemainingSeconds = state.timerPrepLimit;
      }

      state.timerInterval = setInterval(() => {
        if (state.timerRemainingSeconds > 0) {
          state.timerRemainingSeconds--;
          updateTimerUI();
        } else {
          // 스테이지 전환
          if (state.timerStage === 'prep') {
            playBeepSound(1000, 0.4); // 삐- 신호음
            state.timerStage = 'response';
            state.timerTotalSeconds = state.timerResponseLimit;
            state.timerRemainingSeconds = state.timerResponseLimit;
            updateTimerUI();
          } else if (state.timerStage === 'response') {
            playBeepSound(587, 0.6); // 종료음
            state.timerStage = 'ended';
            clearInterval(state.timerInterval);
            state.timerInterval = null;
            updateTimerUI();
          }
        }
      }, 1000);

      updateTimerUI();
    }

    function updateTimerUI() {
      const badge = document.getElementById('timerStageBadge');
      const clock = document.getElementById('timerDigitalClock');
      const progress = document.getElementById('timerProgressFill');
      const btn = document.getElementById('btnTimerStart');
      const info = document.getElementById('timerInfoCaption');
      if (!badge || !clock || !progress || !btn || !info) return;

      const m = Math.floor(state.timerRemainingSeconds / 60);
      const s = state.timerRemainingSeconds % 60;
      clock.textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;

      const pct = state.timerTotalSeconds > 0
        ? Math.max(0, Math.min(100, (state.timerRemainingSeconds / state.timerTotalSeconds) * 100))
        : 0;
      progress.style.width = `${pct}%`;

      if (state.timerStage === 'prep') {
        badge.className = 'timer-stage-badge prep';
        badge.innerHTML = '<span class="voice-dot" style="background:#0071E3;"></span> 준비 시간';
        progress.style.backgroundColor = 'var(--apple-blue)';
        btn.textContent = state.timerInterval ? '⏸ 일시정지' : '▶ 계속';
        info.innerHTML = `준비 시간 ${state.timerRemainingSeconds}초 남음 ➔ 종료 시 비프음 후 답변 시간(${state.timerResponseLimit}초) 자동 전환`;
      } else if (state.timerStage === 'response') {
        badge.className = 'timer-stage-badge response';
        badge.innerHTML = '<span class="voice-dot" style="background:#FF3B30;"></span> 답변 시간 (Speak Now)';
        progress.style.backgroundColor = 'var(--apple-red)';
        btn.textContent = state.timerInterval ? '⏸ 일시정지' : '▶ 계속';
        info.innerHTML = `🎙️ 답변 시간 진행 중! (${state.timerRemainingSeconds}초 남음)`;
      } else if (state.timerStage === 'ended') {
        badge.className = 'timer-stage-badge standby';
        badge.textContent = '답변 종료 (Time Over)';
        progress.style.backgroundColor = 'var(--apple-text-muted)';
        btn.textContent = '↺ 다시 시작';
        info.innerHTML = '시험 시간이 종료되었습니다. 초기화 후 다시 연습해 보세요.';
      } else {
        badge.className = 'timer-stage-badge standby';
        badge.textContent = '타이머 대기 중';
        progress.style.backgroundColor = 'var(--apple-blue)';
        btn.textContent = '▶ 시작';
        info.innerHTML = `준비 ${state.timerPrepLimit}초 ➔ 삐(Beep) ➔ 답변 ${state.timerResponseLimit}초`;
      }
    }

    function renderCbtTimerCard(prepSec, respSec) {
      return `
        <div class="cbt-timer-card">
          <div class="timer-top-line">
            <div class="timer-stage-badge standby" id="timerStageBadge">타이머 대기 중</div>
            <div class="timer-digital-display" id="timerDigitalClock">00:${String(prepSec).padStart(2, '0')}</div>
            <div class="timer-btn-actions">
              <button type="button" class="btn-timer-ctrl" id="btnTimerStart" onclick="toggleTimer()">▶ 시작</button>
              <button type="button" class="btn-timer-ctrl" onclick="resetTimer(${prepSec}, ${respSec})">↺ 초기화</button>
            </div>
          </div>
          <div class="timer-progress-track">
            <div class="timer-progress-fill" id="timerProgressFill" style="width: 100%;"></div>
          </div>
          <div class="timer-info-caption" id="timerInfoCaption">
            준비 ${prepSec}초 ➔ 삐(Beep) ➔ 답변 ${respSec}초
          </div>
        </div>
      `;
    }

    // =========================================================================
    // 상단 세그먼트 컨트롤 탭 & 하단 네비게이션
    // =========================================================================
    function renderSegmentedTabs() {
      const totalP4Q = MASTER_DATA.part4.reduce((acc, s) => acc + (s.questions ? s.questions.length : 0), 0);
      const tabs = [
        { id: 'part1', fullLabel: 'Part 1 지문 읽기', shortLabel: 'Part 1', count: MASTER_DATA.part1.length },
        { id: 'part2', fullLabel: 'Part 2 사진 묘사', shortLabel: 'Part 2', count: MASTER_DATA.part2.length },
        { id: 'part3', fullLabel: 'Part 3 질문 응답', shortLabel: 'Part 3', count: MASTER_DATA.part3.length },
        { id: 'part4', fullLabel: 'Part 4 표 정보 안내', shortLabel: 'Part 4', count: `${MASTER_DATA.part4.length}세트` },
        { id: 'part5', fullLabel: 'Part 5 의견 제시', shortLabel: 'Part 5', count: MASTER_DATA.part5.length }
      ];

      const c = document.getElementById('partTabContainer');
      c.innerHTML = tabs.map(t => `
        <button type="button" class="segment-btn ${state.activePart === t.id ? 'active' : ''}"
          onclick="switchPart('${t.id}')">
          <span class="btn-text-full">${t.fullLabel}</span>
          <span class="btn-text-short">${t.shortLabel}</span>
          <span class="segment-count">${t.count}</span>
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

    function getActiveItems() {
      if (state.activePart === 'part1') return MASTER_DATA.part1;
      if (state.activePart === 'part2') return MASTER_DATA.part2;
      if (state.activePart === 'part3') {
        if (state.part3TypeFilter === 'ALL') return MASTER_DATA.part3;
        return MASTER_DATA.part3.filter(q => q.typeId === state.part3TypeFilter);
      }
      if (state.activePart === 'part4') {
        if (state.part4TableTypeFilter === 'ALL') return MASTER_DATA.part4;
        return MASTER_DATA.part4.filter(s => s.tableTypeId === state.part4TableTypeFilter);
      }
      if (state.activePart === 'part5') return MASTER_DATA.part5;
      return [];
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
      btnPrev.disabled = state.selectedIndex === 0;
      btnNext.disabled = state.selectedIndex >= total - 1;
    }

    function navPrev() {
      if (state.selectedIndex > 0) {
        selectItem(state.selectedIndex - 1);
      }
    }

    function navNext() {
      const items = getActiveItems();
      if (state.selectedIndex < items.length - 1) {
        selectItem(state.selectedIndex + 1);
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
        const numLabel = it.qNum || it.setNum || `Item ${idx+1}`;
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
          btn.innerHTML = '<span>모범답안 접기 ▲</span>';
        } else {
          el.classList.remove('show');
          btn.classList.remove('opened');
          btn.innerHTML = '<span>모범답안 보기 ▼</span>';
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
          btn.innerHTML = '<span>모범답안 접기 ▲</span>';
        } else {
          el.classList.remove('show');
          btn.classList.remove('opened');
          btn.innerHTML = '<span>모범답안 보기 ▼</span>';
        }
      }
    }

    // 4. 파트 4 질문 지문 숨김/열림 토글
    function toggleP4QuestionText(qId) {
      state.p4QTextOpenMap[qId] = !state.p4QTextOpenMap[qId];
      const el = document.getElementById(`p4-qtext-${qId}`);
      const btn = document.getElementById(`p4-qbtn-${qId}`);
      if (el && btn) {
        if (state.p4QTextOpenMap[qId]) {
          el.classList.add('show');
          btn.classList.add('opened');
          btn.innerHTML = '<span>질문 지문 접기 ▲</span>';
        } else {
          el.classList.remove('show');
          btn.classList.remove('opened');
          btn.innerHTML = '<span>질문 지문 보기 ▼</span>';
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

      // Part 3 유형 필터
      let filterBarHtml = '';
      if (state.activePart === 'part3') {
        filterBarHtml = `
          <div class="filter-chips-row">
            <span class="filter-chips-label">유형</span>
            ${MASTER_DATA.part3Types.map(t => `
              <button type="button" class="chip-filter-btn ${state.part3TypeFilter === t.id ? 'active' : ''}"
                onclick="setPart3Filter('${t.id}')">
                ${escapeHtml(t.name)}
              </button>
            `).join('')}
          </div>
        `;
      }

      // 7. Part 4 표 속성별 필터
      if (state.activePart === 'part4') {
        filterBarHtml = `
          <div class="filter-chips-row">
            <span class="filter-chips-label">표 속성</span>
            ${MASTER_DATA.part4TableTypes.map(t => `
              <button type="button" class="chip-filter-btn ${state.part4TableTypeFilter === t.id ? 'active' : ''}"
                onclick="setPart4TableFilter('${t.id}')">
                ${escapeHtml(t.name)}
              </button>
            `).join('')}
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

    // =========================================================================
    // Part 1 렌더링 (전체 지문 맨 위 + 아래로 문장별 끊어 읽기 + 타이머)
    // =========================================================================
    function renderPart1Detail(q, idx, total) {
      const fullText = (q.sentences || []).map(s => s.en).join(' ');

      return `
        <article class="glass-card">
          <!-- 3. 제목이 길어도 우측에 딱 고정되는 헤더 -->
          <div class="glass-card-header">
            <div class="header-text-group">
              <div class="card-meta-tags">
                <span class="tag-pill tag-category">${escapeHtml(q.category)}</span>
                <span class="tag-pill tag-time">준비 45초 · 답변 45초</span>
              </div>
              <h2 class="card-title">${escapeHtml(q.qNum)} — ${escapeHtml(q.topic)}</h2>
            </div>
            <div class="card-nav-controls">
              <button type="button" class="btn-circle-nav" ${idx === 0 ? 'disabled' : ''} onclick="selectItem(${idx - 1})">← 이전</button>
              <button type="button" class="btn-circle-nav" ${idx >= total - 1 ? 'disabled' : ''} onclick="selectItem(${idx + 1})">다음 →</button>
            </div>
          </div>

          <!-- 4. 전체 지문 제일 위 노출 (클릭 시 발음 선택) -->
          <div class="p1-full-passage-card speech-selectable ${state.selectedItemId === q.id + '-full' ? 'selected' : ''}"
               data-speech-id="${q.id}-full" data-speech-text="${escapeHtml(fullText)}"
               onclick="selectSpeechItem('${q.id}-full', this.getAttribute('data-speech-text'))">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
              <span style="font-size: 13px; font-weight: 700; color: var(--apple-text-secondary); text-transform: uppercase; letter-spacing: 0.04em;">
                전체 지문 (Full Passage) · 클릭하여 선택
              </span>
            </div>
            <p class="p1-full-passage-text">${escapeHtml(fullText)}</p>
          </div>

          <!-- 5. 실제 CBT 타이머 (준비 45초 ➔ 삐 ➔ 답변 45초) -->
          ${renderCbtTimerCard(q.prepTime || 45, q.responseTime || 45)}

          <!-- 문장별 끊어 읽기 (클릭 시 발음 선택) -->
          <div style="margin-top: 30px;">
            <h3 style="font-size: 16px; font-weight: 700; color: var(--apple-text); margin-bottom: 12px;">
              문장별 끊어 읽기 (클릭하여 선택 후 하단에서 재생)
            </h3>
            <div class="sentence-block-list">
              ${q.sentences.map((s, sIdx) => `
                <div class="sentence-item-card speech-selectable ${state.selectedItemId === q.id + '-s' + sIdx ? 'selected' : ''}"
                     data-speech-id="${q.id}-s${sIdx}" data-speech-text="${escapeHtml(s.en)}"
                     onclick="selectSpeechItem('${q.id}-s${sIdx}', this.getAttribute('data-speech-text'))">
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

          <!-- 핵심 발음 어휘 (클릭 시 발음 선택) -->
          <div style="margin-top: 28px;">
            <h3 style="font-size: 15px; font-weight: 700; color: var(--apple-text); margin-bottom: 10px;">
              핵심 발음 어휘 (클릭하여 선택)
            </h3>
            <div class="vocab-capsule-grid">
              ${(q.vocabulary || []).map((v, vIdx) => `
                <div class="vocab-capsule-card speech-selectable ${state.selectedItemId === q.id + '-v' + vIdx ? 'selected' : ''}"
                     data-speech-id="${q.id}-v${vIdx}" data-speech-text="${escapeHtml(v.word)}"
                     onclick="selectSpeechItem('${q.id}-v${vIdx}', this.getAttribute('data-speech-text'))">
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
              <strong>💡 Part 1 발음 팁:</strong> ${escapeHtml(q.readingTips)}
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
                <span class="tag-pill tag-category">${escapeHtml(q.typeBadge || q.category || '')}</span>
                <span class="tag-pill tag-time">준비 ${q.prepTime}초 · 답변 ${q.responseTime}초</span>
              </div>
              <h2 class="card-title">${escapeHtml(q.qNum)} — ${escapeHtml(q.topic)}</h2>
            </div>
            <div class="card-nav-controls">
              <button type="button" class="btn-circle-nav" ${idx === 0 ? 'disabled' : ''} onclick="selectItem(${idx - 1})">← 이전</button>
              <button type="button" class="btn-circle-nav" ${idx >= total - 1 ? 'disabled' : ''} onclick="selectItem(${idx + 1})">다음 →</button>
            </div>
          </div>

          <!-- 1. Part 2 사진: 검은 레터박스 없이 카드 너비에 꽉 차게 렌더링 -->
          ${q.part === 2 && q.imageBase64 ? `
            <div class="photo-display-full">
              <img src="${q.imageBase64}" alt="${escapeHtml(q.topic)}" />
            </div>
          ` : ''}

          <!-- 8. 질문 프롬프트 (영어 질문만 노출, 클릭 시 발음 선택) -->
          ${q.question ? `
            <div class="question-prompt-card speech-selectable ${state.selectedItemId === q.id + '-prompt' ? 'selected' : ''}"
                 data-speech-id="${q.id}-prompt" data-speech-text="${escapeHtml(q.question)}"
                 onclick="selectSpeechItem('${q.id}-prompt', this.getAttribute('data-speech-text'))">
              <div class="question-prompt-header">
                <span class="prompt-tag-title">QUESTION PROMPT · 클릭하여 선택</span>
              </div>
              <p class="question-prompt-en">${escapeHtml(q.question)}</p>
            </div>
          ` : ''}

          <!-- 5. CBT 타이머 (준비 시간 ➔ 삐 ➔ 답변 시간) -->
          ${renderCbtTimerCard(q.prepTime || 45, q.responseTime || 30)}

          <!-- 2. 모범답안 토글 버튼 -->
          <div style="display: flex; align-items: center; margin-top: 20px;">
            <button type="button" id="btnToggleAnswer" class="btn-toggle-answer ${state.isAnswerOpen ? 'opened' : ''}" onclick="toggleAnswer()">
              <span>${state.isAnswerOpen ? '모범답안 접기 ▲' : '모범답안 보기 ▼'}</span>
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
                문장별 모범답안 (클릭하여 선택 후 하단에서 재생)
              </h3>
              <button type="button" class="speech-selectable ${state.selectedItemId === q.id + '-all' ? 'selected' : ''}"
                      data-speech-id="${q.id}-all" data-speech-text="${escapeHtml(fullSentences)}"
                      onclick="selectSpeechItem('${q.id}-all', this.getAttribute('data-speech-text'))"
                      style="padding: 4px 12px; font-size: 12px; font-weight: 600; border-radius: var(--radius-pill); border: 1px solid var(--apple-blue-border); background: var(--apple-blue-bg); color: var(--apple-blue);">
                전체 모범답안 선택
              </button>
            </div>

            <!-- 문장 목록 (클릭하여 발음 선택) -->
            <div class="sentence-block-list">
              ${(q.sentences || []).map((s, sIdx) => `
                <div class="sentence-item-card speech-selectable ${state.selectedItemId === q.id + '-ms' + sIdx ? 'selected' : ''}"
                     data-speech-id="${q.id}-ms${sIdx}" data-speech-text="${escapeHtml(s.en)}"
                     onclick="selectSpeechItem('${q.id}-ms${sIdx}', this.getAttribute('data-speech-text'))">
                  <div style="flex: 1;">
                    ${s.step ? `<span class="sentence-step-badge">${escapeHtml(s.step)}</span>` : ''}
                    <div class="sentence-en-text">${escapeHtml(s.en)}</div>
                    <div class="sentence-ko-text">${escapeHtml(s.ko)}</div>
                  </div>
                </div>
              `).join('')}
            </div>

            <!-- 쓰인 만능문장 (클릭하여 발음 선택) -->
            ${q.magicSentences && q.magicSentences.length > 0 ? `
              <div style="margin-top: 24px;">
                <h3 style="font-size: 15px; font-weight: 700; color: var(--apple-text); margin-bottom: 10px;">
                  적용된 만능문장 표현 (클릭하여 선택)
                </h3>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                  ${q.magicSentences.map((m, mIdx) => `
                    <div class="magic-sentence-card speech-selectable ${state.selectedItemId === q.id + '-mg' + mIdx ? 'selected' : ''}"
                         data-speech-id="${q.id}-mg${mIdx}" data-speech-text="${escapeHtml(m.en)}"
                         onclick="selectSpeechItem('${q.id}-mg${mIdx}', this.getAttribute('data-speech-text'))">
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

            <!-- 핵심 어휘 (클릭하여 발음 선택) -->
            <div style="margin-top: 24px;">
              <h3 style="font-size: 15px; font-weight: 700; color: var(--apple-text); margin-bottom: 10px;">
                핵심 어휘 (클릭하여 선택)
              </h3>
              <div class="vocab-capsule-grid">
                ${(q.vocabulary || []).map((v, vIdx) => `
                  <div class="vocab-capsule-card speech-selectable ${state.selectedItemId === q.id + '-vv' + vIdx ? 'selected' : ''}"
                       data-speech-id="${q.id}-vv${vIdx}" data-speech-text="${escapeHtml(v.word)}"
                       onclick="selectSpeechItem('${q.id}-vv${vIdx}', this.getAttribute('data-speech-text'))">
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

            <!-- 해설 -->
            ${q.explanation ? `
              <div class="explanation-callout">
                <strong>💡 고득점 해설 전략:</strong> ${escapeHtml(q.explanation)}
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
                <span class="tag-pill tag-category">${escapeHtml(setObj.tableTypeBadge)}</span>
                <span class="tag-pill tag-time">표 읽기 45초 · 연계 문제 ${setObj.questions.length}문항</span>
              </div>
              <h2 class="card-title">${escapeHtml(setObj.setNum)} — ${escapeHtml(setObj.topic)}</h2>
            </div>
            <div class="card-nav-controls">
              <button type="button" class="btn-circle-nav" ${idx === 0 ? 'disabled' : ''} onclick="selectItem(${idx - 1})">← 이전 표</button>
              <button type="button" class="btn-circle-nav" ${idx >= total - 1 ? 'disabled' : ''} onclick="selectItem(${idx + 1})">다음 표 →</button>
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

          <!-- 5. 표 읽기 45초 타이머 -->
          ${renderCbtTimerCard(setObj.prepTime || 45, 15)}

          <!-- 7. 같은 표의 문제들을 엮어서 순차적으로 나열 -->
          <div style="margin-top: 32px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <h3 style="font-size: 17px; font-weight: 700; color: var(--apple-text);">
                표 연계 문제 (Questions ${setObj.questions.length}문항)
              </h3>
              <span style="font-size: 12px; color: var(--apple-text-secondary);">
                🎧 실제 시험처럼 질문을 귀로 먼저 듣고 연습하세요
              </span>
            </div>

            <div style="display: flex; flex-direction: column; gap: 20px;">
              ${setObj.questions.map((q, qIdx) => {
                const isAnsOpen = !!state.p4AnswerOpenMap[q.qId];
                const isQTextOpen = !!state.p4QTextOpenMap[q.qId];
                const fullSentences = (q.sentences || []).map(s => s.en).join(' ');

                return `
                  <div class="p4-lc-question-card">
                    <!-- 4. 파트 4 상단: 질문 선택 버튼 + 질문 지문 보기 토글 버튼 -->
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                      <div style="display: flex; align-items: center; gap: 8px;">
                        <span class="tag-pill tag-part" style="font-size: 11px;">${escapeHtml(q.qNum)}</span>
                        <span style="font-size: 13px; font-weight: 600; color: var(--apple-text-secondary);">${escapeHtml(q.topic)}</span>
                      </div>
                      <div style="display: flex; align-items: center; gap: 8px;">
                        <button type="button" class="speech-selectable ${state.selectedItemId === q.qId + '-prompt' ? 'selected' : ''}"
                                data-speech-id="${q.qId}-prompt" data-speech-text="${escapeHtml(q.question)}"
                                onclick="selectSpeechItem('${q.qId}-prompt', this.getAttribute('data-speech-text'))"
                                style="padding: 5px 13px; font-size: 12px; font-weight: 700; border-radius: var(--radius-pill); border: 1px solid var(--apple-blue-border); background: var(--apple-blue-bg); color: var(--apple-blue);">
                          질문듣기
                        </button>
                        <button type="button" id="p4-qbtn-${q.qId}" class="btn-toggle-qtext ${isQTextOpen ? 'opened' : ''}"
                          onclick="toggleP4QuestionText('${q.qId}')">
                          <span>${isQTextOpen ? '질문 지문 접기 ▲' : '질문 지문 보기 ▼'}</span>
                        </button>
                      </div>
                    </div>

                    <!-- 4. [질문 보기] 버튼을 누르면 나타나는 지문 + 해석 (클릭하여 선택 가능) -->
                    <div id="p4-qtext-${q.qId}" class="p4-qtext-collapse ${isQTextOpen ? 'show' : ''}">
                      <div class="speech-selectable ${state.selectedItemId === q.qId + '-prompt' ? 'selected' : ''}"
                           data-speech-id="${q.qId}-prompt" data-speech-text="${escapeHtml(q.question)}"
                           onclick="selectSpeechItem('${q.qId}-prompt', this.getAttribute('data-speech-text'))"
                           style="padding: 12px 14px; margin-top: 8px; border-radius: var(--radius-md);">
                        <div style="font-size: 16px; font-weight: 700; color: var(--apple-text); line-height: 1.45;">
                          ${escapeHtml(q.question)}
                        </div>
                        <div style="font-size: 13.5px; color: var(--apple-blue); font-weight: 500; margin-top: 6px;">
                          <strong>해석:</strong> ${escapeHtml(q.questionKo)}
                        </div>
                      </div>
                    </div>

                    <!-- 모범답안 토글 버튼 (밖에는 버튼만 위치) -->
                    <div style="display: flex; align-items: center; margin-top: 16px;">
                      <button type="button" id="p4-btn-${q.qId}" class="btn-toggle-answer ${isAnsOpen ? 'opened' : ''}"
                        onclick="toggleP4QuestionAnswer('${q.qId}')">
                        <span>${isAnsOpen ? '모범답안 접기 ▲' : '모범답안 보기 ▼'}</span>
                      </button>
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
                          문장별 모범답안 (클릭하여 선택)
                        </h4>
                        <button type="button" class="speech-selectable ${state.selectedItemId === q.qId + '-all' ? 'selected' : ''}"
                                data-speech-id="${q.qId}-all" data-speech-text="${escapeHtml(fullSentences)}"
                                onclick="selectSpeechItem('${q.qId}-all', this.getAttribute('data-speech-text'))"
                                style="padding: 4px 12px; font-size: 12px; font-weight: 600; border-radius: var(--radius-pill); border: 1px solid var(--apple-blue-border); background: var(--apple-blue-bg); color: var(--apple-blue);">
                          전체 모범답안 선택
                        </button>
                      </div>

                      <!-- 문장 목록 -->
                      <div class="sentence-block-list">
                        ${(q.sentences || []).map((s, sIdx) => `
                          <div class="sentence-item-card speech-selectable ${state.selectedItemId === q.qId + '-ms' + sIdx ? 'selected' : ''}"
                               data-speech-id="${q.qId}-ms${sIdx}" data-speech-text="${escapeHtml(s.en)}"
                               onclick="selectSpeechItem('${q.qId}-ms${sIdx}', this.getAttribute('data-speech-text'))">
                            <div style="flex: 1;">
                              ${s.step ? `<span class="sentence-step-badge">${escapeHtml(s.step)}</span>` : ''}
                              <div class="sentence-en-text">${escapeHtml(s.en)}</div>
                              <div class="sentence-ko-text">${escapeHtml(s.ko)}</div>
                            </div>
                          </div>
                        `).join('')}
                      </div>

                      <!-- 만능문장 -->
                      ${q.magicSentences && q.magicSentences.length > 0 ? `
                        <div style="margin-top: 16px;">
                          <div style="display: flex; flex-direction: column; gap: 8px;">
                            ${q.magicSentences.map((m, mIdx) => `
                              <div class="magic-sentence-card speech-selectable ${state.selectedItemId === q.qId + '-mg' + mIdx ? 'selected' : ''}"
                                   data-speech-id="${q.qId}-mg${mIdx}" data-speech-text="${escapeHtml(m.en)}"
                                   onclick="selectSpeechItem('${q.qId}-mg${mIdx}', this.getAttribute('data-speech-text'))">
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
                               onclick="selectSpeechItem('${q.qId}-vv${vIdx}', this.getAttribute('data-speech-text'))">
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
                          <strong>💡 답변 팁:</strong> ${escapeHtml(q.explanation)}
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
    // 2. 단어장 모달
    // =========================================================================
    function toggleVocabModal() {
      state.isVocabModalOpen = !state.isVocabModalOpen;
      const backdrop = document.getElementById('vocabModalBackdrop');
      if (state.isVocabModalOpen) {
        backdrop.classList.add('active');
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

    function renderModalPartFilters() {
      const filters = [
        { id: 'ALL', label: `전체 (187)` },
        { id: '2', label: 'Part 2 사진묘사 (49)' },
        { id: '3', label: 'Part 3 질문응답 (47)' },
        { id: '4', label: 'Part 4 표정보 (38)' },
        { id: '5', label: 'Part 5 의견제시 (53)' }
      ];

      const c = document.getElementById('modalPartFilterContainer');
      c.innerHTML = filters.map(f => `
        <button type="button" class="chip-filter-btn ${state.modalPartFilter === f.id ? 'active' : ''}"
          onclick="setModalPartFilter('${f.id}')">
          ${f.label}
        </button>
      `).join('');
    }

    function setModalPartFilter(partId) {
      state.modalPartFilter = partId;
      renderModalPartFilters();
      renderModalVocabList();
    }

    function handleModalSearch(val) {
      state.modalSearchQuery = val;
      renderModalVocabList();
    }

    function toggleMemorize(id) {
      if (state.memorizedIds[id]) {
        delete state.memorizedIds[id];
      } else {
        state.memorizedIds[id] = true;
      }
      localStorage.setItem('toeic_memorized_187', JSON.stringify(state.memorizedIds));
      renderModalVocabList();
    }

    function renderModalVocabList() {
      const q = (state.modalSearchQuery || '').trim().toLowerCase();
      const filtered = MAGIC_DATA.items.filter(item => {
        if (state.modalPartFilter !== 'ALL' && String(item.part) !== state.modalPartFilter) return false;
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

      const memCount = Object.keys(state.memorizedIds).length;
      document.getElementById('modalMemCount').textContent = memCount;

      const grid = document.getElementById('modalVocabGrid');
      grid.innerHTML = filtered.map(item => {
        const isMem = !!state.memorizedIds[item.id];
        return `
          <div class="vocab-item-card ${isMem ? 'memorized' : ''}">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span class="tag-pill tag-part" style="font-size: 11px;">Part ${item.part}</span>
                  <span style="font-size: 12px; font-weight: 700; color: var(--apple-blue);">${item.id}</span>
                  <span style="font-size: 12px; font-weight: 600; color: var(--apple-text-muted);">${escapeHtml(item.category)}</span>
                </div>
                <button type="button" class="btn-mem-toggle ${isMem ? 'checked' : ''}" onclick="toggleMemorize('${item.id}')">
                  ${isMem ? '✓ 암기완료' : '암기 체크'}
                </button>
              </div>
              <div style="font-size: 15.5px; font-weight: 700; color: var(--apple-text); line-height: 1.4;">${escapeHtml(item.en)}</div>
              <div style="font-size: 13.5px; color: var(--apple-text-secondary); margin-top: 3px;">${escapeHtml(item.ko)}</div>
              ${item.tip ? `<div style="font-size: 11.5px; color: var(--apple-amber); margin-top: 6px;">💡 ${escapeHtml(item.tip)}</div>` : ''}
            </div>
            <div style="display: flex; justify-content: flex-end; padding-top: 8px; border-top: 1px solid var(--apple-border-subtle); gap: 6px;">
              <button type="button" class="btn-floating-rate" onclick="speakText('${escapeHtml(item.en)}', 1.0, 'v-${item.id}-1')">1.0x</button>
              <button type="button" class="btn-floating-rate" onclick="speakText('${escapeHtml(item.en)}', 0.75, 'v-${item.id}-075')">0.75x</button>
            </div>
          </div>
        `;
      }).join('');
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

    html_content = html_template.replace("__MASTER_JSON__", master_json_str).replace("__MAGIC_JSON__", magic_json_str)

    target_path = ROOT / "toeicspk_cbt2026.html"
    target_path.write_text(html_content, encoding="utf-8")
    print(f"✅ 독립 실행형 토익스피킹 CBT HTML 생성 완료: {target_path} ({target_path.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
