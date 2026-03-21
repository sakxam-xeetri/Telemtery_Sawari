(function () {
  'use strict';

  /* ===== HERO SEARCH ===== */
  var heroSearchBtn = document.getElementById('hero-search-btn');
  var heroFrom = document.getElementById('hero-from');
  var heroTo = document.getElementById('hero-to');
  if (heroSearchBtn && heroFrom && heroTo) {
    heroSearchBtn.addEventListener('click', function () {
      var from = heroFrom.value.trim();
      var to = heroTo.value.trim();
      if (from && to) {
        window.location.href = 'index.php?from=' + encodeURIComponent(from) + '&to=' + encodeURIComponent(to);
      } else {
        window.location.href = 'index.php';
      }
    });
    // Enter key support
    [heroFrom, heroTo].forEach(function (input) {
      input.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') heroSearchBtn.click();
      });
    });
  }

  /* ===== PAGE LOADER ===== */
  var loader = document.getElementById('pageLoader');
  if (loader) {
    window.addEventListener('load', function () {
      setTimeout(function () { loader.classList.add('loaded'); }, 300);
      setTimeout(function () { loader.remove(); }, 900);
    });
  }

  /* ===== NAVBAR SCROLL ===== */
  var navbar = document.querySelector('.navbar');
  var hero = document.getElementById('hero');
  if (navbar && hero) {
    var onScroll = function () {
      navbar.classList.toggle('scrolled', window.scrollY > hero.offsetHeight - 80);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ===== MOBILE MENU ===== */
  var mobileToggle = document.getElementById('mobile-toggle');
  var navLinks = document.getElementById('nav-links');
  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', function () {
      navLinks.classList.toggle('active');
      var icon = mobileToggle.querySelector('i');
      if (icon) {
        icon.className = navLinks.classList.contains('active')
          ? 'fa-solid fa-xmark' : 'fa-solid fa-bars';
      }
    });
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        closeMobileMenu();
      });
    });
  }

  var mobileBackdrop = document.getElementById('mobileBackdrop');
  function closeMobileMenu() {
    if (navLinks) navLinks.classList.remove('active');
    if (mobileBackdrop) mobileBackdrop.classList.remove('visible');
    var icon = mobileToggle ? mobileToggle.querySelector('i') : null;
    if (icon) icon.className = 'fa-solid fa-bars';
  }
  if (mobileToggle && navLinks) {
    var origClick = mobileToggle.onclick;
    mobileToggle.addEventListener('click', function () {
      if (mobileBackdrop) {
        mobileBackdrop.classList.toggle('visible', navLinks.classList.contains('active'));
      }
    });
  }
  if (mobileBackdrop) {
    mobileBackdrop.addEventListener('click', closeMobileMenu);
  }

  /* ===== SCROLL REVEAL ===== */
  (function initReveal() {
    var els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    var observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el, i) {
      el.style.transitionDelay = Math.min(i * 50, 300) + 'ms';
      observer.observe(el);
    });
  })();

  /* ===== STATS COUNTER ===== */
  (function initCounters() {
    var counters = document.querySelectorAll('.stat-number[data-target]');
    if (!counters.length) return;
    var observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        obs.unobserve(entry.target);
        var el = entry.target;
        var target = parseInt(el.getAttribute('data-target'), 10);
        var duration = 1600;
        var start = performance.now();
        function tick(now) {
          var elapsed = now - start;
          var progress = Math.min(elapsed / duration, 1);
          var eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.round(eased * target);
          if (progress < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (c) { observer.observe(c); });
  })();

  /* ===== SCROLL PROGRESS BAR ===== */
  var progressBar = document.getElementById('scrollProgress');
  function updateProgress() {
    if (!progressBar) return;
    var scrollTop = window.scrollY;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.width = pct + '%';
  }
  window.addEventListener('scroll', updateProgress, { passive: true });

  /* ===== ACTIVE NAV LINK ===== */
  var sections = document.querySelectorAll('section[id]');
  var navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');
  function updateActiveNav() {
    var scrollY = window.scrollY + 120;
    sections.forEach(function (section) {
      var top = section.offsetTop;
      var height = section.offsetHeight;
      var id = section.getAttribute('id');
      if (scrollY >= top && scrollY < top + height) {
        navAnchors.forEach(function (a) {
          a.classList.toggle('active', a.getAttribute('href') === '#' + id);
        });
      }
    });
  }
  window.addEventListener('scroll', updateActiveNav, { passive: true });

  /* ===== BACK TO TOP ===== */
  var backToTop = document.getElementById('backToTop');
  function updateBackToTop() {
    if (!backToTop) return;
    backToTop.classList.toggle('visible', window.scrollY > 600);
  }
  window.addEventListener('scroll', updateBackToTop, { passive: true });
  if (backToTop) {
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ===== HERO TYPED TEXT ===== */
  (function initTypedText() {
    var el = document.getElementById('heroTyped');
    if (!el) return;
    var phrases = ['with confidence.', 'smarter.', 'like a local.', 'effortlessly.'];
    var current = 0;
    var charIndex = phrases[0].length;
    var isDeleting = false;
    var delay = 2500;

    function tick() {
      var phrase = phrases[current];
      if (!isDeleting) {
        charIndex++;
        el.textContent = phrase.substring(0, charIndex);
        if (charIndex === phrase.length) {
          isDeleting = false;
          setTimeout(function () { isDeleting = true; tick(); }, delay);
          return;
        }
        setTimeout(tick, 60);
      } else {
        charIndex--;
        el.textContent = phrase.substring(0, charIndex);
        if (charIndex === 0) {
          isDeleting = false;
          current = (current + 1) % phrases.length;
          setTimeout(tick, 300);
          return;
        }
        setTimeout(tick, 35);
      }
    }
    setTimeout(function () { isDeleting = true; tick(); }, 3000);
  })();

  /* ===== GALLERY LIGHTBOX ===== */
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxClose = document.getElementById('lightboxClose');

  document.querySelectorAll('.gallery-item').forEach(function (item) {
    item.addEventListener('click', function () {
      var img = this.querySelector('img');
      if (img && lightbox && lightboxImg) {
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt;
        lightbox.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  function closeLightbox() {
    if (lightbox) {
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
    }
  }
  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightbox) {
    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox) closeLightbox();
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && lightbox && lightbox.classList.contains('open')) {
      closeLightbox();
    }
  });

  /* ===== PARALLAX HERO ===== */
  var heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
    window.addEventListener('scroll', function () {
      var scroll = window.scrollY;
      if (scroll < window.innerHeight) {
        heroBg.style.transform = 'translateY(' + (scroll * 0.3) + 'px)';
      }
    }, { passive: true });
  }

  /* ===== CHAT ===== */
  var chatLog = document.getElementById('chat-log');
  var chatForm = document.getElementById('chat-form');
  var chatInput = document.getElementById('chat-input');
  var chatSend = document.getElementById('chat-send');

  var SYSTEM_PROMPT = "You are Sawari, a practical assistant for Kathmandu Valley public transit.\n\nYou can help with:\n- Bus and micro routes around Kathmandu, Lalitpur, and Bhaktapur\n- Common stop names and transfer suggestions\n- Fare guidance in Nepali context\n\nGuidelines:\n- Be concise and direct\n- If unsure, say so and suggest opening the full Sawari navigator\n- Keep most responses under 140 words";
  var messages = [{ role: 'system', content: SYSTEM_PROMPT }];

  function escapeHtml(str) {
    var d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
  }

  function addMessage(role, text) {
    if (!chatLog) return;
    var row = document.createElement('div');
    row.className = 'chat-msg ' + role;

    var avatar = document.createElement('div');
    avatar.className = 'chat-avatar';
    avatar.innerHTML = role === 'assistant'
      ? '<i class="fa-solid fa-bus"></i>'
      : '<i class="fa-solid fa-user"></i>';

    var bubble = document.createElement('div');
    bubble.className = 'chat-bubble';
    bubble.innerHTML = escapeHtml(text).replace(/\n/g, '<br>');

    row.appendChild(avatar);
    row.appendChild(bubble);
    chatLog.appendChild(row);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  function addTypingIndicator() {
    if (!chatLog) return;
    var row = document.createElement('div');
    row.className = 'chat-msg assistant';
    row.id = 'typing-indicator';
    var avatar = document.createElement('div');
    avatar.className = 'chat-avatar';
    avatar.innerHTML = '<i class="fa-solid fa-bus"></i>';
    var bubble = document.createElement('div');
    bubble.className = 'chat-bubble chat-typing';
    bubble.innerHTML = '<span></span><span></span><span></span>';
    row.appendChild(avatar);
    row.appendChild(bubble);
    chatLog.appendChild(row);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  function removeTypingIndicator() {
    var el = document.getElementById('typing-indicator');
    if (el) el.remove();
  }

  async function sendMessage(userText) {
    addMessage('user', userText);
    messages.push({ role: 'user', content: userText });
    chatInput.value = '';
    chatInput.disabled = true;
    chatSend.disabled = true;
    addTypingIndicator();

    try {
      var res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + GROQ_API_KEY
        },
        body: JSON.stringify({
          model: 'llama-3.3-70b-versatile',
          messages: messages.slice(-10),
          max_tokens: 420,
          temperature: 0.6
        })
      });
      removeTypingIndicator();
      if (!res.ok) throw new Error('API ' + res.status);
      var data = await res.json();
      var reply = (data.choices && data.choices[0] && data.choices[0].message)
        ? data.choices[0].message.content
        : 'I could not generate an answer right now.';
      messages.push({ role: 'assistant', content: reply });
      addMessage('assistant', reply);
    } catch (err) {
      removeTypingIndicator();
      addMessage('assistant', 'Chat is currently unavailable. Please open the navigator for route planning.');
      console.error(err);
    } finally {
      chatInput.disabled = false;
      chatSend.disabled = false;
      chatInput.focus();
    }
  }

  if (chatForm && chatInput) {
    chatForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var text = chatInput.value.trim();
      if (text) sendMessage(text);
    });
  }

  /* ===== EXAMPLE QUERY CHIPS ===== */
  document.querySelectorAll('.ask-example').forEach(function (chip) {
    chip.addEventListener('click', function () {
      var query = this.getAttribute('data-query');
      if (query && chatInput) {
        chatInput.value = query;
        chatInput.focus();
        sendMessage(query);
      }
    });
  });

  /* ===== SUGGESTION FORM ===== */
  var suggestForm = document.getElementById('suggest-form');
  var suggestMessage = document.getElementById('suggest-message');
  var suggestChars = document.getElementById('suggest-chars');
  var suggestSubmit = document.getElementById('suggest-submit');
  var suggestFeedback = document.getElementById('suggest-feedback');

  if (suggestMessage && suggestChars) {
    suggestMessage.addEventListener('input', function () {
      suggestChars.textContent = String(this.value.length);
    });
  }

  if (suggestForm && suggestMessage && suggestSubmit && suggestFeedback) {
    suggestForm.addEventListener('submit', async function (e) {
      e.preventDefault();
      var nameInput = document.getElementById('suggest-name');
      var categoryInput = document.getElementById('suggest-category');
      var name = nameInput ? nameInput.value.trim() || 'Anonymous' : 'Anonymous';
      var category = categoryInput ? categoryInput.value : 'general';
      var message = suggestMessage.value.trim();

      if (!message || message.length < 10) {
        showFeedback('Please write at least 10 characters.', 'error');
        return;
      }

      suggestSubmit.disabled = true;
      suggestSubmit.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting';

      try {
        var res = await fetch('backend/handlers/suggestions.php', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name: name, category: category, message: message })
        });
        var data = await res.json();
        if (!res.ok) throw new Error(data.error || 'Submission failed');

        suggestForm.reset();
        suggestChars.textContent = '0';
        var note = data.task
          ? ' A task was extracted for admin review.'
          : ' Your input has been queued for manual review.';
        showFeedback('Thank you for helping improve Sawari.' + note, 'success');
      } catch (err) {
        showFeedback(err.message || 'Something went wrong.', 'error');
        console.error(err);
      } finally {
        suggestSubmit.disabled = false;
        suggestSubmit.innerHTML = '<i class="fa-solid fa-paper-plane"></i> Submit Suggestion';
      }
    });
  }

  function showFeedback(msg, type) {
    if (!suggestFeedback) return;
    suggestFeedback.textContent = msg;
    suggestFeedback.className = 'suggest-feedback ' + type;
    suggestFeedback.style.display = 'block';
    setTimeout(function () { suggestFeedback.style.display = 'none'; }, 8000);
  }
})();
