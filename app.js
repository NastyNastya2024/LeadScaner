(function () {
  var navLinks = document.querySelectorAll('.sidebar-nav a');
  var sections = [];
  var menuToggle = document.querySelector('.menu-toggle');
  var sidebar = document.getElementById('site-nav');
  var mobileNavQuery = window.matchMedia('(max-width: 960px)');

  navLinks.forEach(function (link) {
    var id = link.getAttribute('href');
    if (id && id.charAt(0) === '#') {
      var el = document.querySelector(id);
      if (el) sections.push({ id: id.slice(1), el: el });
    }
  });

  function setActive(id) {
    navLinks.forEach(function (link) {
      link.classList.toggle('active', link.getAttribute('href') === '#' + id);
    });
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

  function toggleMobileNav() {
    if (!sidebar || !menuToggle) return;
    if (sidebar.classList.contains('open')) {
      closeMobileNav();
    } else {
      openMobileNav();
    }
  }

  if (menuToggle && sidebar) {
    menuToggle.addEventListener('click', toggleMobileNav);

    navLinks.forEach(function (link) {
      link.addEventListener('click', closeMobileNav);
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

  if (sections.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) setActive(entry.target.id);
        });
      },
      { rootMargin: '-40% 0px -50% 0px', threshold: 0 }
    );
    sections.forEach(function (s) { observer.observe(s.el); });
    setActive(sections[0].id);
  }
})();
