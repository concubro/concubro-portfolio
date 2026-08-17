(() => {
  const root = document.documentElement;
  const failsafeMs = 2200;
  const staggerMs = 18;
  const maxDelayMs = 216;
  const animationMs = 220;
  let items = [];
  let revealed = false;

  root.style.backgroundColor = "#e0ddca";

  if (!document.fonts || typeof document.fonts.load !== "function") return;

  root.classList.add("font-arrival-pending");

  const markItems = () => {
    const main = document.querySelector("body > main");
    const footer = document.querySelector("body > footer");

    if (!main) return;

    if (document.body.classList.contains("home-page")) {
      items = [...main.children].flatMap((item) =>
        item.matches("nav") ? [...item.querySelectorAll(":scope > ul > li")] : item,
      );
    } else {
      const header = main.querySelector(":scope > header");
      const article = main.querySelector(":scope > article");
      items = [header, ...(article ? article.children : [])].filter(Boolean);
    }

    if (footer) items.push(footer);

    items.forEach((item, index) => {
      item.classList.add("font-arrival-item");
      item.style.setProperty(
        "--font-arrival-delay",
        `${Math.min(index * staggerMs, maxDelayMs)}ms`,
      );
    });
  };

  const reveal = () => {
    if (revealed) return;
    revealed = true;
    markItems();

    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        root.classList.remove("font-arrival-pending");
        root.classList.add("font-arrival-ready");

        window.setTimeout(() => {
          root.classList.remove("font-arrival-ready");
          root.style.removeProperty("background-color");
          items.forEach((item) => {
            item.classList.remove("font-arrival-item");
            item.style.removeProperty("--font-arrival-delay");
          });
        }, animationMs + maxDelayMs + 100);
      });
    });
  };

  const failsafe = window.setTimeout(reveal, failsafeMs);

  window.addEventListener(
    "DOMContentLoaded",
    () => {
      markItems();

      Promise.allSettled([
        document.fonts.load('200 1em "Raleway"'),
        document.fonts.load('400 1em "Raleway"'),
        document.fonts.load('400 1em "Playfair Display"'),
        document.fonts.load('italic 400 1em "Playfair Display"'),
      ])
        .then(() => document.fonts.ready)
        .then(() => {
          window.clearTimeout(failsafe);
          reveal();
        }, reveal);
    },
    { once: true },
  );
})();
