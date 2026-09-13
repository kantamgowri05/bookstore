// Scroll animation for sections
document.addEventListener("scroll", () => {
  document.querySelectorAll(".section").forEach(section => {
    const rect = section.getBoundingClientRect();
    if (rect.top < window.innerHeight - 50) {
      section.classList.add("visible");
    }
  });
});

// Add fade-in effect
const style = document.createElement("style");
style.innerHTML = `
  .section {
    opacity: 0;
    transform: translateY(40px);
    transition: all 0.8s ease;
  }
  .section.visible {
    opacity: 1;
    transform: translateY(0);
  }
`;
document.head.appendChild(style);
