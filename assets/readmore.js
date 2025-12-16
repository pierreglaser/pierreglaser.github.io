document.querySelectorAll('.toggle-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const card = btn.closest('.blog-card');
    const summary = card.querySelector('.summary');
    const dots = summary.querySelector('.dots');
    const more = summary.querySelector('.more');

    if (more.classList.contains('hidden')) {
      more.classList.remove('hidden');
      dots.classList.add('hidden');
      btn.textContent = 'Read less';
    } else {
      more.classList.add('hidden');
      dots.classList.remove('hidden');
      btn.textContent = 'Read more';
    }
  });
});
