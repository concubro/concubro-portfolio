const falseEdgeCapable = window.matchMedia(
  "(hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)",
);

const falseEdge = document.createElement("div");
falseEdge.className = "false-edge";
falseEdge.setAttribute("aria-hidden", "true");
document.body.append(falseEdge);

let coolingDown = false;

window.addEventListener(
  "wheel",
  (event) => {
    if (coolingDown || !falseEdgeCapable.matches || event.deltaY < 12) return;

    const atDocumentEnd =
      Math.ceil(window.scrollY + window.innerHeight) >= document.documentElement.scrollHeight;

    if (!atDocumentEnd) return;

    coolingDown = true;
    falseEdge.classList.add("false-edge--seen");
    falseEdge.addEventListener(
      "animationend",
      () => {
        falseEdge.classList.remove("false-edge--seen");
        window.setTimeout(() => {
          coolingDown = false;
        }, 900);
      },
      { once: true },
    );
  },
  { passive: true },
);
