(function () {
  var navLinks = document.querySelectorAll('.sidebar-nav a');
  var sections = [];

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
