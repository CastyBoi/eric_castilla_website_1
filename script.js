// ---- Nav: solid background after scrolling past hero ----
const nav = document.querySelector('.site-nav');
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('nav.links');

const setNavState = () => {
  if (!nav) return;
  nav.classList.toggle('scrolled', window.scrollY > 40);
};
setNavState();
window.addEventListener('scroll', setNavState, { passive: true });

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });
  navLinks.querySelectorAll('a').forEach((a) =>
    a.addEventListener('click', () => navLinks.classList.remove('open'))
  );
}

// ---- Scroll-reveal for anything with .reveal ----
const revealEls = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  revealEls.forEach((el) => io.observe(el));
} else {
  revealEls.forEach((el) => el.classList.add('in-view'));
}

// ---- Project filter tabs ----
const filterBtns = document.querySelectorAll('.filter-btn');
const cards = document.querySelectorAll('.project-grid .card');

filterBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    filterBtns.forEach((b) => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;

    cards.forEach((card) => {
      const tags = (card.dataset.tags || '').split(',');
      const show = filter === 'all' || tags.includes(filter);
      card.style.display = show ? '' : 'none';
    });
  });
});

// ---- Footer year ----
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();
