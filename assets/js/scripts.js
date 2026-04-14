/* ══════════════════════════════════════
   EWaste Kochi — Main Scripts
   Intersection Observer Reveals + FAQ
   + Sticky Header + Mobile Menu
══════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {

  /* ── INTERSECTION OBSERVER REVEAL ── */
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('on');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.07, rootMargin: '0px 0px -20px 0px' });
  document.querySelectorAll('.rev, .rev-left, .rev-right').forEach(el => observer.observe(el));

  /* ── STICKY HEADER SHADOW ── */
  const header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', () => {
      header.classList.toggle('scrolled', window.scrollY > 50);
    }, { passive: true });
  }

  /* ── SMOOTH SCROLL ── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        document.querySelector('.mob-menu')?.classList.remove('open');
      }
    });
  });

  /* ── FAQ ACCORDION ── */
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });

  /* ── MOBILE MENU ── */
  const ham = document.querySelector('.hamburger');
  const mob = document.querySelector('.mob-menu');
  if (ham && mob) {
    ham.addEventListener('click', () => mob.classList.toggle('open'));
    document.addEventListener('click', e => {
      if (!ham.contains(e.target) && !mob.contains(e.target)) {
        mob.classList.remove('open');
      }
    });
  }

});

/* ── CONTACT FORM HANDLER ── */
function submitQuote(btn) {
  btn.textContent = '✓ Request Sent — We\'ll call you within 1 hour';
  btn.style.background = 'var(--primary-dark)';
  btn.disabled = true;
}
