/**
 * TOEIC Speaking Master Trainer (Part 2, Part 3, Part 4) - Apple Glass Edition
 * Exclusively powered by 'Daniel' Voice (British English Male)
 * Real Exam Environment:
 * - PART 2: Photo Description (Q3 & Q4) with 45s Prep / 30s Speaking & Scene Visuals
 * - PART 3: Daily Life Questions (Q5~Q7) with 16 Themes & 15 Magic Formulas
 * - PART 4: Provided Schedule/Document Tables (Q8~Q10) with 45s Reading Timer & Q9 Error Correction
 * - Hidden Korean Question/Photo Translations (Revealed ONLY with Model Answers)
 * - Sentence-level 🔊 audio button right next to each line
 * - Combined Question + Answer Vocabulary & Deep Grammar Breakdown
 */

class ToeicTrainerApp {
  constructor() {
    this.currentPart = 'part3'; // 'part2' | 'part3' | 'part4'
    this.rawData = null;
    this.part2Questions = [];
    this.part3Questions = [];
    this.part4Questions = [];
    this.currentQuestionsList = [];
    this.filteredQuestions = [];
    this.currentIndex = 0;
    this.isAnswerVisible = false;
    this.isExamTimerEnabled = true;

    // Web Speech API - Fixed to Daniel (UK Male)
    this.synth = window.speechSynthesis;
    this.currentUtterance = null;
    this.activeAudioBtn = null;
    this.danielVoice = null;

    // Exam Timer State (Prep -> Response)
    this.timerInterval = null;
    this.timerPhase = 'idle'; // 'idle' | 'prep' | 'response'
    this.timeLeft = 0;
    this.totalPhaseDuration = 0;

    // Part 4 45-Second Table Reading Timer
    this.p4ReadTimerInterval = null;
    this.p4ReadTimeLeft = 45;
    this.isP4ReadTimerRunning = false;

    // Web Audio API for Clean Beep
    this.audioCtx = null;

    this.initElements();
    this.bindEvents();
    this.loadVoices();
    this.loadData();
  }

  initElements() {
    // Bookmark Tabs (Part 2, Part 3, Part 4)
    this.tabPart2 = document.getElementById('tabPart2');
    this.tabPart3 = document.getElementById('tabPart3');
    this.tabPart4 = document.getElementById('tabPart4');

    // Header & Titles
    this.appTitlePart = document.getElementById('appTitlePart');
    this.appTagline = document.getElementById('appTagline');
    this.headerTargetText = document.getElementById('headerTargetText');
    this.voiceTestBtn = document.getElementById('voiceTestBtn');
    this.cheatSheetBtn = document.getElementById('cheatSheetBtn');
    this.examModeToggleBtn = document.getElementById('examModeToggleBtn');
    this.timerStatusText = document.getElementById('timerStatusText');

    // Toolbar Controls
    this.filterLabel = document.getElementById('filterLabel');
    this.setFilter = document.getElementById('setFilter');
    this.currentCardIndexEl = document.getElementById('currentCardIndex');
    this.totalCardCountEl = document.getElementById('totalCardCount');
    this.progressBar = document.getElementById('progressBar');
    this.prevBtn = document.getElementById('prevBtn');
    this.nextBtn = document.getElementById('nextBtn');

    // Main Card Meta
    this.cardPartBadge = document.getElementById('cardPartBadge');
    this.cardSetBadge = document.getElementById('cardSetBadge');
    this.cardQNumBadge = document.getElementById('cardQNumBadge');
    this.cardTimeBadge = document.getElementById('cardTimeBadge');
    this.cardPatternBadge = document.getElementById('cardPatternBadge');

    // ==========================================
    // Part 2 Photo Section Elements
    // ==========================================
    this.part2PhotoArea = document.getElementById('part2PhotoArea');
    this.p2SceneTag = document.getElementById('p2SceneTag');
    this.p2LocationTag = document.getElementById('p2LocationTag');
    this.p2PhotoViewport = document.getElementById('p2PhotoViewport');
    this.p2PhotoSpinner = document.getElementById('p2PhotoSpinner');
    this.p2RealPhotoImg = document.getElementById('p2RealPhotoImg');
    this.p2SceneElements = document.getElementById('p2SceneElements');
    this.p2PointsCard = document.getElementById('p2PointsCard');

    // ==========================================
    // Part 4 Document & Schedule Table
    // ==========================================
    this.part4DocumentArea = document.getElementById('part4DocumentArea');
    this.p4ReadTimerBtn = document.getElementById('p4ReadTimerBtn');
    this.p4ReadTimerLabel = document.getElementById('p4ReadTimerLabel');
    this.p4ReadProgressBarWrap = document.getElementById('p4ReadProgressBarWrap');
    this.p4ReadCountdown = document.getElementById('p4ReadCountdown');
    this.p4ReadBarFill = document.getElementById('p4ReadBarFill');
    this.p4ReadTimerCancelBtn = document.getElementById('p4ReadTimerCancelBtn');

    this.p4TableHeaderTitle = document.getElementById('p4TableHeaderTitle');
    this.p4TableMetaWrap = document.getElementById('p4TableMetaWrap');
    this.p4TableHead = document.getElementById('p4TableHead');
    this.p4TableBody = document.getElementById('p4TableBody');
    this.p4ContextBanner = document.getElementById('p4ContextBanner');
    this.p4ContextText = document.getElementById('p4ContextText');
    this.p4ContextKr = document.getElementById('p4ContextKr');
    this.p4AnswerContextKrBox = document.getElementById('p4AnswerContextKrBox');
    this.p4AnswerContextKrText = document.getElementById('p4AnswerContextKrText');

    // Question Section (Part 3 & Part 4 text questions)
    this.questionBoxSection = document.getElementById('questionBoxSection');
    this.qBoxTag = document.getElementById('qBoxTag');
    this.qBoxExamNote = document.getElementById('qBoxExamNote');
    this.questionText = document.getElementById('questionText');
    this.qSpeakNormalBtn = document.getElementById('qSpeakNormalBtn');
    this.qSpeakSlowBtn = document.getElementById('qSpeakSlowBtn');
    this.qSpeakStopBtn = document.getElementById('qSpeakStopBtn');

    // Timer Section
    this.timerSection = document.getElementById('timerSection');
    this.timerPhaseBadge = document.getElementById('timerPhaseBadge');
    this.timerCountdown = document.getElementById('timerCountdown');
    this.timerProgressFill = document.getElementById('timerProgressFill');
    this.startTimerBtn = document.getElementById('startTimerBtn');
    this.resetTimerBtn = document.getElementById('resetTimerBtn');

    // Toggle Answer Button
    this.toggleAnswerBtn = document.getElementById('toggleAnswerBtn');
    this.toggleIcon = document.getElementById('toggleIcon');
    this.toggleText = document.getElementById('toggleText');
    this.answerSection = document.getElementById('answerSection');

    // Revealed Question/Photo Translation Box (Inside Answer Section)
    this.qTranslationBox = document.getElementById('qTranslationBox');
    this.qTransBadge = document.getElementById('qTransBadge');
    this.answerQuestionKo = document.getElementById('answerQuestionKo');

    // Answer Section Elements
    this.answerLevelBadge = document.getElementById('answerLevelBadge');
    this.structuredSentencesContainer = document.getElementById('structuredSentencesContainer');
    this.vocabSection = document.getElementById('vocabSection');
    this.vocabChipsGrid = document.getElementById('vocabChipsGrid');
    
    // Grammar Points Elements
    this.grammarSection = document.getElementById('grammarSection');
    this.grammarPointsList = document.getElementById('grammarPointsList');

    this.magicSentencesList = document.getElementById('magicSentencesList');
    this.scoreTipText = document.getElementById('scoreTipText');
    this.aSpeakNormalBtn = document.getElementById('aSpeakNormalBtn');
    this.aSpeakSlowBtn = document.getElementById('aSpeakSlowBtn');
    this.aSpeakStopBtn = document.getElementById('aSpeakStopBtn');

    // Modal & Modal Tabs (Part 2, Part 3, Part 4)
    this.cheatSheetModal = document.getElementById('cheatSheetModal');
    this.closeModalBtn = document.getElementById('closeModalBtn');
    this.modalConfirmBtn = document.getElementById('modalConfirmBtn');
    this.modalTabP2 = document.getElementById('modalTabP2');
    this.modalTabP3 = document.getElementById('modalTabP3');
    this.modalTabP4 = document.getElementById('modalTabP4');
    this.modalP2Content = document.getElementById('modalP2Content');
    this.modalP3Content = document.getElementById('modalP3Content');
    this.modalP4Content = document.getElementById('modalP4Content');
  }

  bindEvents() {
    // Bookmark Tabs Switching
    this.tabPart2.addEventListener('click', () => this.switchPart('part2'));
    this.tabPart3.addEventListener('click', () => this.switchPart('part3'));
    this.tabPart4.addEventListener('click', () => this.switchPart('part4'));

    // Navigation
    this.prevBtn.addEventListener('click', () => this.navigate(-1));
    this.nextBtn.addEventListener('click', () => this.navigate(1));
    this.setFilter.addEventListener('change', (e) => this.filterBySet(e.target.value));

    // Answer Toggle
    this.toggleAnswerBtn.addEventListener('click', () => this.toggleAnswer());

    // Speech Controls - Question
    this.qSpeakNormalBtn.addEventListener('click', () => this.speakQuestion(1.0, this.qSpeakNormalBtn));
    this.qSpeakSlowBtn.addEventListener('click', () => this.speakQuestion(0.75, this.qSpeakSlowBtn));
    this.qSpeakStopBtn.addEventListener('click', () => this.stopSpeaking());

    // Speech Controls - Answer (Full)
    this.aSpeakNormalBtn.addEventListener('click', () => this.speakFullAnswer(1.0, this.aSpeakNormalBtn));
    this.aSpeakSlowBtn.addEventListener('click', () => this.speakFullAnswer(0.75, this.aSpeakSlowBtn));
    this.aSpeakStopBtn.addEventListener('click', () => this.stopSpeaking());

    // Daniel Voice Preview
    this.voiceTestBtn.addEventListener('click', () => this.testDanielVoice());

    // Exam Standard Timer
    this.startTimerBtn.addEventListener('click', () => this.handleTimerStart());
    this.resetTimerBtn.addEventListener('click', () => this.resetTimer());
    this.examModeToggleBtn.addEventListener('click', () => this.toggleExamMode());

    // Part 4 45s Reading Timer
    this.p4ReadTimerBtn.addEventListener('click', () => this.toggleP4ReadTimer());
    this.p4ReadTimerCancelBtn.addEventListener('click', () => this.stopP4ReadTimer());

    // Modal Cheat Sheet
    this.cheatSheetBtn.addEventListener('click', () => this.openModal());
    this.closeModalBtn.addEventListener('click', () => this.closeModal());
    this.modalConfirmBtn.addEventListener('click', () => this.closeModal());
    this.cheatSheetModal.addEventListener('click', (e) => {
      if (e.target === this.cheatSheetModal) this.closeModal();
    });

    // Modal Part Tabs
    this.modalTabP2.addEventListener('click', () => this.switchModalTab('part2'));
    this.modalTabP3.addEventListener('click', () => this.switchModalTab('part3'));
    this.modalTabP4.addEventListener('click', () => this.switchModalTab('part4'));

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => this.handleKeyDown(e));

    // Web Speech Voices changed event
    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = () => this.loadVoices();
    }
  }

  // ==========================================
  // Exclusively Match & Lock to 'Daniel' Voice
  // ==========================================
  loadVoices() {
    if (!('speechSynthesis' in window)) return;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return;

    const daniel = voices.find(v => v.name.toLowerCase().includes('daniel'));
    if (daniel) {
      this.danielVoice = daniel;
      return;
    }

    const fallbackMale = voices.find(v => (v.name.includes('Eddy') || v.name.includes('Reed') || v.name.includes('Alex')) && v.lang.startsWith('en'));
    this.danielVoice = fallbackMale || voices.find(v => v.lang.startsWith('en')) || voices[0];
  }

  testDanielVoice() {
    this.stopSpeaking();
    let testText = "Hello! I am Daniel, your dedicated British voice coach.";
    if (this.currentPart === 'part2') {
      testText = "Hello! Let's describe this picture step by step using Jenny's 4-step formula!";
    } else if (this.currentPart === 'part3') {
      testText = "Hello! Ready to practice TOEIC Speaking Part 3 with Jenny's magic sentences?";
    } else {
      testText = "Hello! Let's analyze the schedule and answer Part 4 questions with confidence!";
    }
    this.speakRawText(testText, 1.0, this.voiceTestBtn);
  }

  // ==========================================
  // Load Master Dataset
  // ==========================================
  async loadData() {
    try {
      if (window.TOEIC_MASTER_DATA) {
        this.rawData = window.TOEIC_MASTER_DATA;
      } else {
        const res = await fetch('data.json');
        if (!res.ok) throw new Error('data.json fetch failed');
        this.rawData = await res.json();
      }

      this.processData();
      this.switchPart('part3'); // Default to Part 3
    } catch (err) {
      console.error('Error loading data:', err);
      this.questionText.innerHTML = `<span style="color:red;">데이터를 불러오는 중 오류가 발생했습니다: ${err.message}</span>`;
    }
  }

  processData() {
    // 1. Process Part 2 Photo Questions
    if (this.rawData.part2) {
      this.part2Questions = this.rawData.part2.map(q => ({
        ...q,
        part: 'part2',
        setId: q.setId || q.setNumber || 1,
        setNumber: q.setId || q.setNumber || 1,
        qNumber: q.qNumber || q.questionNumber || 'Question 3 / 4',
        prepTime: q.prepTime || 45,
        responseTime: q.responseTime || 30
      }));
    }

    // 2. Process Part 3 Questions with ID normalization
    if (this.rawData.part3) {
      this.part3Questions = this.rawData.part3.map(q => {
        const sid = q.setId || q.setNumber || 1;
        const qnum = q.qNumber || q.questionNumber || 'Question 5';
        return {
          ...q,
          part: 'part3',
          setId: sid,
          setNumber: sid,
          qNumber: qnum,
          questionNumber: qnum
        };
      });
    }

    // 3. Process Part 4 Sets into individual questions
    if (this.rawData.part4) {
      const flattenedP4 = [];
      this.rawData.part4.forEach(setObj => {
        const sid = setObj.setNumber || 1;
        setObj.questions.forEach((q, idx) => {
          const qnum = q.qNumber || q.questionNumber || `Question ${8 + idx}`;
          flattenedP4.push({
            ...q,
            part: 'part4',
            setId: sid,
            setNumber: sid,
            qNumber: qnum,
            questionNumber: qnum,
            setTitle: setObj.title,
            topic: setObj.topic,
            context: setObj.context,
            context_kr: setObj.context_kr,
            table: setObj.table,
            qIndexInSet: idx + 1
          });
        });
      });
      this.part4Questions = flattenedP4;
    }
  }

  // ==========================================
  // Switch Bookmark: Part 2 ↔ Part 3 ↔ Part 4
  // ==========================================
  switchPart(partName) {
    this.currentPart = partName;
    this.stopSpeaking();
    this.resetTimer();
    this.stopP4ReadTimer();
    this.hideAnswer();

    // Reset Bookmark Tabs active state
    this.tabPart2.classList.toggle('active', partName === 'part2');
    this.tabPart3.classList.toggle('active', partName === 'part3');
    this.tabPart4.classList.toggle('active', partName === 'part4');

    if (partName === 'part2') {
      this.appTitlePart.textContent = 'Part 2 실전 트레이너';
      this.appTagline.textContent = '사진 묘사하기 (Q3~Q4) · 45초 준비 / 30초 답변 · 시계토끼 4단계 만능공식';
      this.headerTargetText.textContent = 'Target: 120 ~ 140점 (IM3 - IH) · 파트 2 실전 수험서';
      this.cardPartBadge.textContent = 'PART 2';
      this.cardPartBadge.style.background = 'rgba(52, 199, 89, 0.15)';
      this.cardPartBadge.style.color = '#1b7a36';

      this.part2PhotoArea.style.display = 'flex';
      this.part4DocumentArea.style.display = 'none';
      this.questionBoxSection.style.display = 'none'; // Part 2 uses photo frame as the main question view

      this.currentQuestionsList = this.part2Questions;
      this.populateFilterOptions('part2');
    } else if (partName === 'part3') {
      this.appTitlePart.textContent = 'Part 3 실전 트레이너';
      this.appTagline.textContent = '일상 질문 답하기 (Q5~Q7) · 시계토끼 15대 만능문장 · 문법 분석 & 단어장 완비';
      this.headerTargetText.textContent = 'Target: 120 ~ 140점 (IM3 - IH) · 파트 3 실전 수험서';
      this.cardPartBadge.textContent = 'PART 3';
      this.cardPartBadge.style.background = 'rgba(0, 113, 227, 0.12)';
      this.cardPartBadge.style.color = 'var(--apple-blue)';

      this.part2PhotoArea.style.display = 'none';
      this.part4DocumentArea.style.display = 'none';
      this.questionBoxSection.style.display = 'flex';

      this.currentQuestionsList = this.part3Questions;
      this.populateFilterOptions('part3');
    } else {
      this.appTitlePart.textContent = 'Part 4 실전 트레이너';
      this.appTagline.textContent = '제공된 정보(표/일정표) 보고 답하기 (Q8~Q10) · 45초 표 읽기 실전 훈련 · 오류정정 만능공식';
      this.headerTargetText.textContent = 'Target: 120 ~ 140점 (IM3 - IH) · 파트 4 실전 수험서';
      this.cardPartBadge.textContent = 'PART 4';
      this.cardPartBadge.style.background = 'rgba(175, 82, 222, 0.12)';
      this.cardPartBadge.style.color = 'var(--apple-purple)';

      this.part2PhotoArea.style.display = 'none';
      this.part4DocumentArea.style.display = 'flex';
      this.questionBoxSection.style.display = 'flex';

      this.currentQuestionsList = this.part4Questions;
      this.populateFilterOptions('part4');
    }

    this.filteredQuestions = [...this.currentQuestionsList];
    this.currentIndex = 0;
    this.renderCurrentCard();
  }

  // ==========================================
  // Populate Filter: 14 Part 2 Scenes, 16 Part 3 Themes, 8 Part 4 Sets
  // ==========================================
  populateFilterOptions(part) {
    this.setFilter.innerHTML = '';

    if (part === 'part2') {
      this.filterLabel.textContent = '사진 세트 (26개 기출 실사 사진 전체 선택):';
      const allOpt = document.createElement('option');
      allOpt.value = 'all';
      allOpt.textContent = `🖼️ 전체 26세트 (Set 1 ~ 26)`;
      this.setFilter.appendChild(allOpt);

      this.part2Questions.forEach(q => {
        const opt = document.createElement('option');
        opt.value = String(q.setId || q.setNumber);
        opt.textContent = q.setTitle;
        this.setFilter.appendChild(opt);
      });
    } else if (part === 'part3') {
      this.filterLabel.textContent = '주제 세트 (16개 테마 전체 선택):';
      const allOpt = document.createElement('option');
      allOpt.value = 'all';
      allOpt.textContent = `📚 전체 48문항 (Set 1 ~ 16)`;
      this.setFilter.appendChild(allOpt);

      const setsMap = new Map();
      this.part3Questions.forEach(q => {
        const sid = q.setId || q.setNumber;
        if (sid && !setsMap.has(sid)) {
          setsMap.set(sid, q.setTitle);
        }
      });

      const sortedKeys = Array.from(setsMap.keys()).sort((a, b) => Number(a) - Number(b));
      sortedKeys.forEach(sid => {
        const opt = document.createElement('option');
        opt.value = String(sid);
        opt.textContent = setsMap.get(sid);
        this.setFilter.appendChild(opt);
      });
    } else {
      this.filterLabel.textContent = '표/일정표 세트 (8개 표 전체 선택):';
      const allOpt = document.createElement('option');
      allOpt.value = 'all';
      allOpt.textContent = `📑 전체 24문항 (Set 1 ~ 8)`;
      this.setFilter.appendChild(allOpt);

      if (this.rawData.part4) {
        this.rawData.part4.forEach(setObj => {
          const opt = document.createElement('option');
          opt.value = String(setObj.setNumber);
          opt.textContent = `${setObj.title}`;
          this.setFilter.appendChild(opt);
        });
      }
    }
  }

  filterBySet(val) {
    this.stopSpeaking();
    this.resetTimer();
    this.stopP4ReadTimer();
    this.hideAnswer();

    if (val === 'all') {
      this.filteredQuestions = [...this.currentQuestionsList];
    } else {
      const targetId = parseInt(val, 10);
      this.filteredQuestions = this.currentQuestionsList.filter(q => {
        const sid = q.setId || q.setNumber;
        return Number(sid) === targetId;
      });
    }

    this.currentIndex = 0;
    this.renderCurrentCard();
  }

  // ==========================================
  // Card Rendering Logic
  // ==========================================
  renderCurrentCard() {
    if (!this.filteredQuestions || this.filteredQuestions.length === 0) {
      this.questionText.textContent = "표시할 문제가 없습니다.";
      return;
    }

    const q = this.filteredQuestions[this.currentIndex];

    // Counter & Progress Bar
    this.currentCardIndexEl.textContent = this.currentIndex + 1;
    this.totalCardCountEl.textContent = this.filteredQuestions.length;
    const progressPct = ((this.currentIndex + 1) / this.filteredQuestions.length) * 100;
    this.progressBar.style.width = `${progressPct.toFixed(1)}%`;

    // Badges
    this.cardSetBadge.textContent = `Set ${q.setId || q.setNumber}`;
    this.cardQNumBadge.textContent = q.qNumber || q.questionNumber;
    this.cardTimeBadge.textContent = this.currentPart === 'part2' ? `준비 45초 / 답변 30초` : `답변 ${q.responseTime}초`;
    this.cardPatternBadge.textContent = q.keyPattern || (this.currentPart === 'part2' ? '장소/인물/사물 4단계 공식' : (this.currentPart === 'part3' ? '의문사 공식' : '표 정보 전달'));

    // Render Part 2 Photo Scene if in Part 2 Mode
    if (this.currentPart === 'part2') {
      this.renderPart2Photo(q);
      this.qTransBadge.textContent = '💡 사진 한국어 상황 상세 묘사';
      this.answerQuestionKo.textContent = q.photoDescriptionKr || q.questionTranslation || '';
      if (this.p2PointsCard) this.p2PointsCard.style.display = 'block';
      if (this.p4AnswerContextKrBox) this.p4AnswerContextKrBox.style.display = 'none';
    } else if (this.currentPart === 'part4' && q.table) {
      this.renderPart4Table(q);
      this.qTransBadge.textContent = '💡 질문 한국어 해석';
      this.renderFormattedQuestion(q);
      this.answerQuestionKo.textContent = q.questionTranslation || '';
      if (this.p2PointsCard) this.p2PointsCard.style.display = 'none';
      if (this.p4AnswerContextKrBox) {
        if (q.context_kr) {
          this.p4AnswerContextKrBox.style.display = 'block';
          if (this.p4AnswerContextKrText) this.p4AnswerContextKrText.textContent = q.context_kr;
        } else {
          this.p4AnswerContextKrBox.style.display = 'none';
        }
      }
    } else {
      // Part 3
      this.qTransBadge.textContent = '💡 질문 한국어 해석';
      this.renderFormattedQuestion(q);
      this.answerQuestionKo.textContent = q.questionTranslation || '';
      if (this.p2PointsCard) this.p2PointsCard.style.display = 'none';
      if (this.p4AnswerContextKrBox) this.p4AnswerContextKrBox.style.display = 'none';
    }

    // Render Model Answer Components
    this.renderStructuredAnswer(q);
    this.renderVocabulary(q);
    this.renderGrammarPoints(q);
    this.renderMagicSentences(q);
    this.scoreTipText.textContent = q.scoreTip || '핵심 문장을 당황하지 않고 또렷하게 전달하세요.';

    // Hide answer section by default on question change
    this.hideAnswer();
    this.resetTimer();
  }

  // ==========================================
  // Part 2 Photo Scene Visual Rendering (실제 시험 실사 사진)
  // ==========================================
  renderPart2Photo(q) {
    const scene = q.photoScene || {};
    this.p2SceneTag.textContent = `📸 EXAM PHOTO SCENE #${q.setId || q.setNumber}: ${scene.category || '기출 사진'}`;
    this.p2LocationTag.textContent = `Location: ${scene.locationEn || 'in the picture'}`;

    // Real Photo Image URL
    const imageUrl = q.imageUrl || "https://images.unsplash.com/photo-1578916171728-46686eac8d58?auto=format&fit=crop&w=1200&q=80";

    if (this.p2PhotoSpinner && this.p2RealPhotoImg) {
      this.p2PhotoSpinner.style.display = 'flex';
      this.p2PhotoSpinner.textContent = '📸 고화질 실사 시험 사진 로딩 중...';
      this.p2RealPhotoImg.style.display = 'none';

      this.p2RealPhotoImg.onload = () => {
        this.p2PhotoSpinner.style.display = 'none';
        this.p2RealPhotoImg.style.display = 'block';
      };

      this.p2RealPhotoImg.onerror = () => {
        this.p2PhotoSpinner.textContent = `📸 ${q.setTitle} (사진 로딩 완료)`;
        this.p2PhotoSpinner.style.display = 'flex';
      };

      this.p2RealPhotoImg.src = imageUrl;
    }

    // Key scene elements breakdown
    this.p2SceneElements.innerHTML = '';
    const tags = scene.tags || [];
    tags.forEach(tag => {
      const pill = document.createElement('div');
      pill.className = 'p2-key-element-pill';
      pill.innerHTML = `<strong>POINT:</strong> <span>${tag}</span>`;
      this.p2SceneElements.appendChild(pill);
    });
  }

  renderPart4Table(q) {
    const table = q.table;
    this.p4TableHeaderTitle.textContent = table.headerTitle || 'Schedule / Document';

    this.p4TableMetaWrap.innerHTML = '';
    if (table.metaInfo && table.metaInfo.length > 0) {
      table.metaInfo.forEach(item => {
        const pill = document.createElement('div');
        pill.className = 'meta-tag-pill';
        pill.innerHTML = `<strong>${item.label}:</strong> <span>${item.value}</span>`;
        this.p4TableMetaWrap.appendChild(pill);
      });
    }

    if (table.rows && table.rows.length > 0) {
      const firstRow = table.rows[0];
      const keys = Object.keys(firstRow);

      this.p4TableHead.innerHTML = `<tr>${keys.map(k => `<th>${this.formatTableColumnName(k)}</th>`).join('')}</tr>`;

      this.p4TableBody.innerHTML = table.rows.map(row => {
        const isCancelled = row.isCancelled || (row.activity && row.activity.includes('CANCELLED'));
        const rowStyle = isCancelled ? 'style="text-decoration: line-through; opacity: 0.6;"' : '';
        return `<tr ${rowStyle}>${keys.map(k => `<td>${row[k] || '-'}</td>`).join('')}</tr>`;
      }).join('');
    } else {
      this.p4TableHead.innerHTML = '';
      this.p4TableBody.innerHTML = '';
    }

    if (q.context) {
      this.p4ContextBanner.style.display = 'flex';
      this.p4ContextText.textContent = q.context;
      if (this.p4ContextKr) this.p4ContextKr.textContent = q.context_kr || '';
    } else {
      this.p4ContextBanner.style.display = 'none';
    }
  }

  formatTableColumnName(key) {
    const map = {
      time: 'Time (시간)',
      session: 'Session / Topic (세션명)',
      topic: 'Topic (주제)',
      speaker: 'Speaker / Host (강연자)',
      presenter: 'Presenter (발표자)',
      location: 'Location (장소)',
      room: 'Room (회의실)',
      destination: 'Destination (장소)',
      activity: 'Activity (내용)',
      guide: 'Guide (안내)',
      department: 'Department (부서)',
      interviewer: 'Interviewer (면접관)',
      candidate: 'Candidate (지원자)',
      doctor: 'Doctor (담당의)',
      specialty: 'Specialty (진료과)',
      status: 'Status / Hours (진료시간/상태)'
    };
    return map[key.toLowerCase()] || (key.charAt(0).toUpperCase() + key.slice(1));
  }

  renderFormattedQuestion(q) {
    const rawQuestion = q.question;
    const parts = rawQuestion.split('\n');

    let html = '';
    parts.forEach(line => {
      const trimmed = line.trim();
      if (!trimmed) return;

      if (trimmed.startsWith('- Option') || trimmed.startsWith('Option') || trimmed.startsWith('•')) {
        html += `<div class="question-option-chip">${trimmed}</div>`;
      } else {
        html += `<div class="question-line">${trimmed}</div>`;
      }
    });

    this.questionText.innerHTML = html;
  }

  // ==========================================
  // Render Model Answer with Inline Speaker (🔊) Button
  // ==========================================
  renderStructuredAnswer(q) {
    this.structuredSentencesContainer.innerHTML = '';

    let enLines = (q.answer || '').split('\n').map(l => l.trim()).filter(l => l.length > 0);
    let koLines = (q.answerTranslation || '').split('\n').map(l => l.trim()).filter(l => l.length > 0);

    // Fallback: If answer is a single paragraph with multiple sentences, split automatically
    if (enLines.length === 1 && (enLines[0].match(/\.\s+[A-Z]/g) || []).length > 0) {
      const splitEn = enLines[0].match(/[^.!?]+[.!?]+(\s+|$)/g) || [enLines[0]];
      enLines = splitEn.map(s => s.trim()).filter(s => s.length > 0);
    }
    if (koLines.length === 1 && (koLines[0].match(/\.\s+/g) || []).length > 0) {
      const splitKo = koLines[0].match(/[^.!?]+[.!?]+(\s+|$)/g) || [koLines[0]];
      koLines = splitKo.map(s => s.trim()).filter(s => s.length > 0);
    }

    enLines.forEach((enLine, idx) => {
      const koLine = koLines[idx] || '';

      const row = document.createElement('div');
      row.className = 'sentence-card';

      row.innerHTML = `
        <div class="sentence-body">
          <div class="sentence-en-row">
            <span class="sentence-num-badge">${idx + 1}</span>
            <p class="sentence-en">${enLine}</p>
            <button class="btn-sentence-speaker" title="Daniel 목소리로 ${idx + 1}번 문장 발음 듣기 (쉐도잉)">🔊</button>
          </div>
          <p class="sentence-ko">${koLine}</p>
        </div>
      `;

      const speakerBtn = row.querySelector('.btn-sentence-speaker');
      speakerBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.speakRawText(enLine, 1.0, speakerBtn);
      });

      this.structuredSentencesContainer.appendChild(row);
    });
  }

  // ==========================================
  // Render Vocabulary (Question/Photo + Answer Combined)
  // ==========================================
  renderVocabulary(q) {
    this.vocabChipsGrid.innerHTML = '';
    const vocabList = q.vocabulary || [];

    if (vocabList.length === 0) {
      this.vocabSection.style.display = 'none';
      return;
    }

    this.vocabSection.style.display = 'block';

    vocabList.forEach(item => {
      const chip = document.createElement('div');
      chip.className = 'vocab-chip';

      const isQuestionSource = item.source && (item.source.includes('문제') || item.source.includes('사진'));
      const sourceBadgeClass = isQuestionSource ? 'source-q' : 'source-a';
      const sourceBadgeText = item.source || (this.currentPart === 'part2' ? '사진 필수' : '문제 필수');

      chip.innerHTML = `
        <div class="vocab-top">
          <div style="display: flex; align-items: center; gap: 6px;">
            <span class="vocab-word">${item.word}</span>
            <span class="vocab-source-badge ${sourceBadgeClass}">${sourceBadgeText}</span>
          </div>
          <span class="vocab-pos">${item.pos || '어휘'}</span>
        </div>
        <div class="vocab-ipa-row">
          <span class="vocab-ipa">${item.ipa || ''}</span>
          <button class="btn-vocab-speak" title="${item.word} Daniel 발음 듣기">🔊</button>
        </div>
        <div class="vocab-meaning">${item.meaning}</div>
      `;

      const speakBtn = chip.querySelector('.btn-vocab-speak');
      speakBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.speakRawText(item.word, 0.9, speakBtn);
      });

      this.vocabChipsGrid.appendChild(chip);
    });
  }

  // ==========================================
  // Render Grammar & Sentence Structure Points
  // ==========================================
  renderGrammarPoints(q) {
    if (!this.grammarPointsList) return;
    this.grammarPointsList.innerHTML = '';
    const points = q.grammarPoints || [];

    if (points.length === 0) {
      if (this.grammarSection) this.grammarSection.style.display = 'none';
      return;
    }

    if (this.grammarSection) this.grammarSection.style.display = 'block';

    points.forEach(item => {
      const card = document.createElement('div');
      card.className = 'grammar-point-card';
      card.innerHTML = `
        <div class="grammar-point-title">💡 ${item.title}</div>
        <div class="grammar-point-desc">${item.explanation}</div>
      `;
      this.grammarPointsList.appendChild(card);
    });
  }

  renderMagicSentences(q) {
    this.magicSentencesList.innerHTML = '';
    const list = q.magicSentences || [];

    if (list.length === 0) {
      const li = document.createElement('li');
      li.className = 'magic-point-item';
      li.textContent = '기본 템플릿을 차분하게 적용하여 답변하세요.';
      this.magicSentencesList.appendChild(li);
      return;
    }

    list.forEach(item => {
      const li = document.createElement('li');
      li.className = 'magic-point-item';
      li.innerHTML = `<strong>${item}</strong>`;
      this.magicSentencesList.appendChild(li);
    });
  }

  // ==========================================
  // Part 4: 45-Second Table Reading Timer
  // ==========================================
  toggleP4ReadTimer() {
    if (this.isP4ReadTimerRunning) {
      this.stopP4ReadTimer();
    } else {
      this.startP4ReadTimer();
    }
  }

  startP4ReadTimer() {
    this.stopSpeaking();
    this.stopP4ReadTimer();

    this.isP4ReadTimerRunning = true;
    this.p4ReadTimeLeft = 45;
    this.p4ReadProgressBarWrap.style.display = 'flex';
    this.p4ReadTimerBtn.classList.add('running');
    this.p4ReadTimerLabel.textContent = '45초 읽는 중... (클릭 시 정지)';
    this.p4ReadCountdown.textContent = '45';
    this.p4ReadBarFill.style.width = '100%';

    this.speakRawText("You will have 45 seconds to read the schedule.", 1.0);

    this.p4ReadTimerInterval = setInterval(() => {
      this.p4ReadTimeLeft--;
      this.p4ReadCountdown.textContent = this.p4ReadTimeLeft;
      const pct = (this.p4ReadTimeLeft / 45) * 100;
      this.p4ReadBarFill.style.width = `${pct}%`;

      if (this.p4ReadTimeLeft <= 0) {
        clearInterval(this.p4ReadTimerInterval);
        this.p4ReadTimerInterval = null;
        this.isP4ReadTimerRunning = false;
        this.p4ReadTimerBtn.classList.remove('running');
        this.p4ReadTimerLabel.textContent = '45초 표 읽기 실전 타이머';
        this.p4ReadProgressBarWrap.style.display = 'none';

        this.playBeep(880, 0.4);
        setTimeout(() => {
          this.speakRawText("45 seconds are up. Now answer Question 8.", 1.0);
        }, 500);
      }
    }, 1000);
  }

  stopP4ReadTimer() {
    if (this.p4ReadTimerInterval) {
      clearInterval(this.p4ReadTimerInterval);
      this.p4ReadTimerInterval = null;
    }
    this.isP4ReadTimerRunning = false;
    this.p4ReadTimerBtn.classList.remove('running');
    this.p4ReadTimerLabel.textContent = '45초 표 읽기 실전 타이머';
    this.p4ReadProgressBarWrap.style.display = 'none';
  }

  // ==========================================
  // Standard Question Timer (Part 2: 45s->30s / Part 3,4: 3s->15s/30s)
  // ==========================================
  handleTimerStart() {
    if (this.timerPhase !== 'idle') {
      this.resetTimer();
      return;
    }

    const q = this.filteredQuestions[this.currentIndex];
    const prepSeconds = q.prepTime || (this.currentPart === 'part2' ? 45 : 3);
    const responseSeconds = q.responseTime || (this.currentPart === 'part2' ? 30 : 15);

    this.startTimerPhase('prep', prepSeconds, () => {
      this.playBeep(880, 0.35);

      setTimeout(() => {
        if (this.currentPart === 'part2') {
          this.speakRawText("Begin speaking now.", 1.0);
        }

        this.startTimerPhase('response', responseSeconds, () => {
          this.playBeep(440, 0.2);
          setTimeout(() => this.playBeep(440, 0.3), 250);
          this.timerPhaseBadge.textContent = '답변 종료';
          this.timerPhaseBadge.className = 'timer-phase-badge done';
          this.startTimerBtn.textContent = '🔄 다시 시작';
          this.timerPhase = 'idle';
        });
      }, 400);
    });
  }

  startTimerPhase(phase, duration, onComplete) {
    this.timerPhase = phase;
    this.timeLeft = duration;
    this.totalPhaseDuration = duration;

    if (phase === 'prep') {
      this.timerPhaseBadge.textContent = `준비 시간 (${duration}초)`;
      this.timerPhaseBadge.className = 'timer-phase-badge prep';
      this.startTimerBtn.textContent = '⏸️ 준비 중...';
      this.startTimerBtn.classList.add('active-prep');
    } else {
      this.timerPhaseBadge.textContent = `답변 시간 (${duration}초)`;
      this.timerPhaseBadge.className = 'timer-phase-badge response';
      this.startTimerBtn.textContent = '🎙️ 말하기 답변 중...';
      this.startTimerBtn.classList.remove('active-prep');
      this.startTimerBtn.classList.add('active-response');
    }

    this.resetTimerBtn.style.display = 'inline-block';
    this.updateTimerDisplay();

    if (this.timerInterval) clearInterval(this.timerInterval);

    this.timerInterval = setInterval(() => {
      this.timeLeft--;
      this.updateTimerDisplay();

      if (this.timeLeft <= 0) {
        clearInterval(this.timerInterval);
        this.timerInterval = null;
        if (onComplete) onComplete();
      }
    }, 1000);
  }

  updateTimerDisplay() {
    this.timerCountdown.textContent = Math.max(0, this.timeLeft);
    const pct = this.totalPhaseDuration > 0
      ? (this.timeLeft / this.totalPhaseDuration) * 100
      : 0;
    this.timerProgressFill.style.width = `${pct}%`;
  }

  resetTimer() {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }
    this.timerPhase = 'idle';

    const q = this.filteredQuestions[this.currentIndex];
    const defaultPrep = q ? (q.prepTime || (this.currentPart === 'part2' ? 45 : 3)) : (this.currentPart === 'part2' ? 45 : 3);
    const defaultResp = q ? (q.responseTime || 30) : 30;

    this.timeLeft = defaultPrep;
    this.totalPhaseDuration = defaultPrep;

    this.timerPhaseBadge.textContent = '준비 시간';
    this.timerPhaseBadge.className = 'timer-phase-badge prep';
    this.timerCountdown.textContent = String(defaultPrep);
    this.timerProgressFill.style.width = '100%';
    this.startTimerBtn.textContent = `▶️ 실전 카운트다운 시작 (${defaultPrep}초 ➡️ ${defaultResp}초 답변)`;
    this.startTimerBtn.className = 'btn-timer-glow play';
    this.resetTimerBtn.style.display = 'none';
  }

  toggleExamMode() {
    this.isExamTimerEnabled = !this.isExamTimerEnabled;
    this.timerSection.style.display = this.isExamTimerEnabled ? 'flex' : 'none';
    this.examModeToggleBtn.classList.toggle('active', this.isExamTimerEnabled);
    this.timerStatusText.textContent = this.isExamTimerEnabled ? 'ON' : 'OFF';
  }

  playBeep(freq = 880, duration = 0.3) {
    try {
      if (!this.audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        this.audioCtx = new AudioContext();
      }
      if (this.audioCtx.state === 'suspended') {
        this.audioCtx.resume();
      }
      const osc = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, this.audioCtx.currentTime);

      gain.gain.setValueAtTime(0.15, this.audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.audioCtx.currentTime + duration);

      osc.connect(gain);
      gain.connect(this.audioCtx.destination);

      osc.start();
      osc.stop(this.audioCtx.currentTime + duration);
    } catch (e) {
      console.warn('Web Audio beep error:', e);
    }
  }

  // ==========================================
  // Model Answer & Hidden Question/Photo Translation Toggle
  // ==========================================
  toggleAnswer() {
    if (this.isAnswerVisible) {
      this.hideAnswer();
    } else {
      this.showAnswer();
    }
  }

  showAnswer() {
    this.isAnswerVisible = true;
    this.answerSection.style.display = 'block';
    this.toggleAnswerBtn.setAttribute('aria-expanded', 'true');
    this.toggleIcon.textContent = '🙈';
    this.toggleText.textContent = '모범답안 & 문제해석 닫기';
    this.toggleAnswerBtn.classList.add('active');
  }

  hideAnswer() {
    this.isAnswerVisible = false;
    this.answerSection.style.display = 'none';
    this.toggleAnswerBtn.setAttribute('aria-expanded', 'false');
    this.toggleIcon.textContent = '👁️';
    this.toggleText.textContent = '모범답안 & 문제해석 보기';
    this.toggleAnswerBtn.classList.remove('active');
    this.stopSpeaking();
  }

  // ==========================================
  // Web Speech API Integration (Exclusively Daniel)
  // ==========================================
  speakQuestion(rate = 1.0, btnElement = null) {
    const q = this.filteredQuestions[this.currentIndex];
    if (!q) return;
    const textToSpeak = this.currentPart === 'part2'
      ? "In this part of the test, you will describe the picture on your screen in as much detail as you can. You will have 45 seconds to prepare your response. Then you will have 30 seconds to speak about the picture."
      : q.question;
    this.speakRawText(textToSpeak, rate, btnElement);
  }

  speakFullAnswer(rate = 1.0, btnElement = null) {
    const q = this.filteredQuestions[this.currentIndex];
    if (!q) return;
    this.speakRawText(q.answer, rate, btnElement);
  }

  speakRawText(text, rate = 1.0, btnElement = null) {
    if (!('speechSynthesis' in window)) {
      alert('이 브라우저는 음성 합성(Speech Synthesis)을 지원하지 않습니다.');
      return;
    }

    this.stopSpeaking();

    const cleanText = text
      .replace(/\(.*?\)/g, '')
      .replace(/\[.*?\]/g, '')
      .replace(/[•\-\*]/g, ' ')
      .trim();

    if (!cleanText) return;

    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.rate = rate;
    utterance.pitch = 1.0;

    if (this.danielVoice) {
      utterance.voice = this.danielVoice;
      utterance.lang = this.danielVoice.lang;
    } else {
      utterance.lang = 'en-GB';
    }

    if (btnElement) {
      this.activeAudioBtn = btnElement;
      btnElement.classList.add('speaking');
    }

    utterance.onend = () => {
      this.clearSpeakingState();
    };

    utterance.onerror = () => {
      this.clearSpeakingState();
    };

    this.currentUtterance = utterance;
    window.speechSynthesis.speak(utterance);
    this.showStopButtons();
  }

  stopSpeaking() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    this.clearSpeakingState();
  }

  clearSpeakingState() {
    if (this.activeAudioBtn) {
      this.activeAudioBtn.classList.remove('speaking');
      this.activeAudioBtn = null;
    }
    this.hideStopButtons();
    this.currentUtterance = null;
  }

  showStopButtons() {
    this.qSpeakStopBtn.style.display = 'inline-flex';
    this.aSpeakStopBtn.style.display = 'inline-flex';
  }

  hideStopButtons() {
    this.qSpeakStopBtn.style.display = 'none';
    this.aSpeakStopBtn.style.display = 'none';
  }

  // ==========================================
  // Navigation
  // ==========================================
  navigate(direction) {
    this.stopSpeaking();
    this.resetTimer();
    this.stopP4ReadTimer();
    this.hideAnswer();

    const newIndex = this.currentIndex + direction;
    if (newIndex >= 0 && newIndex < this.filteredQuestions.length) {
      this.currentIndex = newIndex;
      this.renderCurrentCard();
      this.scrollToTop();
    }
  }

  scrollToTop() {
    const card = document.getElementById('practiceCard');
    if (card) {
      card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  // ==========================================
  // Cheat Sheet Modal & Internal Tab Switch (Part 2, 3, 4)
  // ==========================================
  openModal() {
    this.stopSpeaking();
    this.cheatSheetModal.style.display = 'flex';
    document.body.style.overflow = 'hidden';

    this.switchModalTab(this.currentPart);
  }

  closeModal() {
    this.cheatSheetModal.style.display = 'none';
    document.body.style.overflow = '';
  }

  switchModalTab(part) {
    this.modalTabP2.classList.toggle('active', part === 'part2');
    this.modalTabP3.classList.toggle('active', part === 'part3');
    this.modalTabP4.classList.toggle('active', part === 'part4');

    this.modalP2Content.style.display = part === 'part2' ? 'block' : 'none';
    this.modalP3Content.style.display = part === 'part3' ? 'block' : 'none';
    this.modalP4Content.style.display = part === 'part4' ? 'block' : 'none';
  }

  // ==========================================
  // Keyboard Shortcuts
  // ==========================================
  handleKeyDown(e) {
    if (['INPUT', 'SELECT', 'TEXTAREA'].includes(e.target.tagName)) return;

    switch (e.key) {
      case 'ArrowLeft':
        e.preventDefault();
        this.navigate(-1);
        break;
      case 'ArrowRight':
        e.preventDefault();
        this.navigate(1);
        break;
      case ' ':
        e.preventDefault();
        this.toggleAnswer();
        break;
      case '1':
        e.preventDefault();
        this.speakQuestion(1.0, this.qSpeakNormalBtn);
        break;
      case '2':
        e.preventDefault();
        this.speakQuestion(0.75, this.qSpeakSlowBtn);
        break;
      case '3':
        e.preventDefault();
        this.speakFullAnswer(1.0, this.aSpeakNormalBtn);
        break;
      case '4':
        e.preventDefault();
        this.speakFullAnswer(0.75, this.aSpeakSlowBtn);
        break;
      case 'Escape':
        this.stopSpeaking();
        this.closeModal();
        break;
    }
  }
}

// Instantiate on DOM load
window.addEventListener('DOMContentLoaded', () => {
  window.toeicApp = new ToeicTrainerApp();
});
