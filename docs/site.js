document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-language-select]').forEach((select) => {
    select.addEventListener('change', () => {
      const target = select.value;
      if (target) window.location.href = target;
    });
  });
});
