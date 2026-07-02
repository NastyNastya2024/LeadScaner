(function () {
  var body = document.body;
  var MD_URL = body.getAttribute('data-doc-src') || 'FINANCIAL_MODEL.md';
  var contentEl = document.getElementById('model-content');
  var statusEl = document.getElementById('model-status');
  var tocEl = document.getElementById('model-toc');
  var menuToggle = document.querySelector('.menu-toggle');
  var sidebar = document.getElementById('model-nav');
  var mobileNavQuery = window.matchMedia('(max-width: 960px)');

  function slugify(text) {
    return text
      .replace(/\*\*/g, '')
      .trim()
      .toLowerCase()
      .replace(/[^\p{L}\p{N}\s-]/gu, '')
      .replace(/\s+/g, '-')
      .replace(/-+/g, '-');
  }

  function closeMobileNav() {
    if (!sidebar || !menuToggle) return;
    sidebar.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('nav-open');
  }

  function openMobileNav() {
    if (!sidebar || !menuToggle) return;
    sidebar.classList.add('open');
    menuToggle.setAttribute('aria-expanded', 'true');
    document.body.classList.add('nav-open');
  }

  if (menuToggle && sidebar) {
    menuToggle.addEventListener('click', function () {
      if (sidebar.classList.contains('open')) closeMobileNav();
      else openMobileNav();
    });

    sidebar.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        if (a.getAttribute('href') && a.getAttribute('href').charAt(0) === '#') closeMobileNav();
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMobileNav();
    });

    document.addEventListener('click', function (e) {
      if (!mobileNavQuery.matches || !sidebar.classList.contains('open')) return;
      if (sidebar.contains(e.target) || menuToggle.contains(e.target)) return;
      closeMobileNav();
    });

    mobileNavQuery.addEventListener('change', function () {
      if (!mobileNavQuery.matches) closeMobileNav();
    });
  }

  function assignHeadingIds(root) {
    root.querySelectorAll('h2, h3, h4').forEach(function (h) {
      if (!h.id) h.id = slugify(h.textContent);
    });
  }

  function buildToc(root) {
    if (!tocEl) return;
    var items = [];
    root.querySelectorAll('h2, h3').forEach(function (h) {
      if (!h.id) return;
      items.push({
        id: h.id,
        text: h.textContent.replace(/\*\*/g, '').trim(),
        level: h.tagName === 'H2' ? 2 : 3
      });
    });

    tocEl.innerHTML = '';
    items.forEach(function (item) {
      var li = document.createElement('li');
      if (item.level === 3) li.className = 'model-toc-h3';
      var a = document.createElement('a');
      a.href = '#' + item.id;
      a.textContent = item.text;
      li.appendChild(a);
      tocEl.appendChild(li);
    });

    if (!items.length) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          tocEl.querySelectorAll('a').forEach(function (link) {
            link.classList.toggle('active', link.getAttribute('href') === '#' + entry.target.id);
          });
        });
      },
      { rootMargin: '-30% 0px -60% 0px', threshold: 0 }
    );

    items.forEach(function (item) {
      var el = document.getElementById(item.id);
      if (el) observer.observe(el);
    });
  }

  function renderMermaid(root) {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize({ startOnLoad: false, theme: 'neutral', securityLevel: 'loose' });

    root.querySelectorAll('pre code.language-mermaid').forEach(function (code) {
      var pre = code.parentElement;
      var div = document.createElement('div');
      div.className = 'mermaid';
      div.textContent = code.textContent;
      pre.replaceWith(div);
    });

    mermaid.run({ nodes: root.querySelectorAll('.mermaid') });
  }

  function showError(message) {
    if (statusEl) {
      statusEl.hidden = false;
      statusEl.classList.add('model-status-error');
      statusEl.textContent = message;
    }
    if (contentEl) contentEl.hidden = true;
  }

  function showContent(html) {
    if (!contentEl) return;
    contentEl.innerHTML = html;
    var firstH1 = contentEl.querySelector('h1');
    if (firstH1) firstH1.remove();
    assignHeadingIds(contentEl);
    buildToc(contentEl);
    renderMermaid(contentEl);
    if (statusEl) statusEl.hidden = true;
    contentEl.hidden = false;
  }

  if (typeof marked !== 'undefined') {
    marked.setOptions({ gfm: true, breaks: false, headerIds: false, mangle: false });
  }

  var loadingText = statusEl ? statusEl.textContent : '';

  fetch(MD_URL)
    .then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.text();
    })
    .then(function (md) {
      if (typeof marked === 'undefined') {
        showError('Markdown renderer failed to load.');
        return;
      }
      showContent(marked.parse(md));
    })
    .catch(function () {
      showError(document.documentElement.lang === 'en'
        ? 'Could not load ' + MD_URL
        : 'Не удалось загрузить ' + MD_URL);
      if (statusEl && loadingText) statusEl.textContent = loadingText;
    });
})();
