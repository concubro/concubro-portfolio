const finePointer = window.matchMedia(
  "(hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)",
);

const items = [...document.querySelectorAll(".index-item")];
const interestDelay = 440;
const movementTolerance = 8;

function setEnhancementState() {
  document.documentElement.classList.toggle("underprint-ready", finePointer.matches);

  if (!finePointer.matches) {
    items.forEach((item) => item.classList.remove("underprint-active", "underprint-fallback"));
    return;
  }

  refreshEligibility();
}

function refreshEligibility() {
  if (!finePointer.matches) return;

  for (const item of items) {
    item.classList.remove("underprint-fallback");

    const link = item.querySelector(".index-link");
    const metadata = item.querySelector(".index-meta");
    const lineHeight = Number.parseFloat(getComputedStyle(link).lineHeight);
    const linkRect = link.getBoundingClientRect();
    const metadataWidth = metadata.getBoundingClientRect().width;
    const roomToRight = document.documentElement.clientWidth - linkRect.right - 16;
    const titleWraps = linkRect.height > lineHeight * 1.4;

    item.classList.toggle(
      "underprint-fallback",
      titleWraps || metadataWidth + 4 > roomToRight,
    );
  }
}

for (const item of items) {
  let interestTimer;
  let anchorX = 0;
  let anchorY = 0;

  const cancelInterest = () => {
    window.clearTimeout(interestTimer);
  };

  const beginInterest = (x, y) => {
    cancelInterest();
    anchorX = x;
    anchorY = y;
    interestTimer = window.setTimeout(() => {
      item.classList.add("underprint-active");
    }, interestDelay);
  };

  item.addEventListener("pointerenter", (event) => {
    if (finePointer.matches) beginInterest(event.clientX, event.clientY);
  });

  item.addEventListener("pointermove", (event) => {
    if (!finePointer.matches || item.classList.contains("underprint-active")) return;

    if (Math.hypot(event.clientX - anchorX, event.clientY - anchorY) > movementTolerance) {
      beginInterest(event.clientX, event.clientY);
    }
  });

  item.addEventListener("pointerleave", () => {
    cancelInterest();
    item.classList.remove("underprint-active");
  });

  item.addEventListener("focusin", () => {
    cancelInterest();
    item.classList.add("underprint-active");
  });

  item.addEventListener("focusout", () => {
    item.classList.remove("underprint-active");
  });
}

finePointer.addEventListener("change", setEnhancementState);
window.addEventListener("resize", refreshEligibility);
setEnhancementState();
document.fonts?.ready.then(refreshEligibility);
