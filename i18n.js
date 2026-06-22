(function () {
  var STORAGE_KEY = 'leadscaper-lang';
  var currentLang = localStorage.getItem(STORAGE_KEY) || 'ru';
  var strings = {};

  function localeBase() {
    return document.body.classList.contains('tool-page') ? '../locales/' : 'locales/';
  }

  function get(obj, path) {
    return path.split('.').reduce(function (o, k) {
      return o && o[k] !== undefined ? o[k] : null;
    }, obj);
  }

  function applyLang(lang) {
    document.documentElement.lang = lang;
    currentLang = lang;
    localStorage.setItem(STORAGE_KEY, lang);

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var val = get(strings, el.getAttribute('data-i18n'));
      if (val == null) return;
      if (el.getAttribute('data-i18n-html') === 'true') {
        el.innerHTML = val;
      } else {
        el.textContent = val;
      }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
      var val = get(strings, el.getAttribute('data-i18n-placeholder'));
      if (val != null) el.setAttribute('placeholder', val);
    });

    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {
      var key = el.getAttribute('data-i18n-aria');
      if (!key) return;
      var val = get(strings, key);
      if (val != null) el.setAttribute('aria-label', val);
    });

    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    var titleKey = document.body.getAttribute('data-title-i18n');
    if (titleKey) {
      var t = get(strings, titleKey);
      if (t) document.title = t;
    } else if (strings.meta && strings.meta.title) {
      document.title = strings.meta.title;
    }

    document.querySelectorAll('[data-i18n-open]').forEach(function (openBtn) {
      var source = openBtn.getAttribute('data-source') || 'GitHub';
      var tpl = get(strings, 'ui.openOn') || 'Open on {source} →';
      openBtn.textContent = tpl.replace('{source}', source);
    });

    var slug = document.body.getAttribute('data-tool-slug');
    if (slug && strings.toolsPage && strings.toolsPage[slug]) {
      var tp = strings.toolsPage[slug];
      var roleEl = document.querySelector('[data-i18n-tool-role]');
      if (roleEl && tp.role) roleEl.textContent = tp.role;
      var layerEl = document.querySelector('[data-i18n-tool-layer]');
      if (layerEl && tp.layerName) {
        var n = layerEl.getAttribute('data-layer') || '';
        var layerTpl = (strings.ui && strings.ui.layerLabel) || 'Layer {n} · {name}';
        layerEl.textContent = layerTpl.replace('{n}', n).replace('{name}', tp.layerName);
      }
    }
  }

  function loadLang(lang) {
    return fetch(localeBase() + lang + '.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        strings = data;
        applyLang(lang);
      });
  }

  function initSwitcher() {
    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var lang = btn.getAttribute('data-lang');
        if (lang !== currentLang) loadLang(lang);
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initSwitcher();
    loadLang(currentLang);
  });

  window.LeadScaperI18n = { loadLang: loadLang, getLang: function () { return currentLang; } };
})();
