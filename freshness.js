(() => {
  const dayMs = 24 * 60 * 60 * 1000;
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  document.querySelectorAll(".index-item[data-published]").forEach((item) => {
    const published = new Date(`${item.dataset.published}T00:00:00`);

    if (Number.isNaN(published.getTime())) return;

    const ageInDays = (today - published) / dayMs;

    if (ageInDays < 0 || ageInDays >= 30) return;

    item.classList.add("index-item--fresh");
    const label = item.querySelector(".index-fresh");

    if (label) {
      label.textContent = "new";
      label.hidden = false;
    }
  });
})();
