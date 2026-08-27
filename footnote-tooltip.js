(() => {
  const footnotes = [...document.querySelectorAll(".inline-footnote")];

  const close = (footnote, blur = false) => {
    footnote.classList.remove("is-open");
    footnote.querySelector(".inline-footnote-tip")?.setAttribute("aria-hidden", "true");

    const trigger = footnote.querySelector(".inline-footnote-trigger");
    if (blur && document.activeElement === trigger) trigger.blur();
  };

  footnotes.forEach((footnote) => {
    const trigger = footnote.querySelector(".inline-footnote-trigger");
    const tip = footnote.querySelector(".inline-footnote-tip");
    if (!trigger || !tip) return;

    trigger.addEventListener("click", () => {
      const willOpen = !footnote.classList.contains("is-open");
      footnotes.forEach((item) => close(item));

      if (willOpen) {
        footnote.classList.add("is-open");
        tip.setAttribute("aria-hidden", "false");
      } else {
        close(footnote, true);
      }
    });

    footnote.addEventListener("focusout", (event) => {
      if (!footnote.contains(event.relatedTarget)) close(footnote);
    });
  });

  document.addEventListener("pointerdown", (event) => {
    footnotes.forEach((footnote) => {
      if (!footnote.contains(event.target)) close(footnote, true);
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") footnotes.forEach((footnote) => close(footnote, true));
  });
})();
