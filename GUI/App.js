document.querySelectorAll("#decrypt-button").forEach((button) => {
  button.addEventListener("click", function () {
    document
      .querySelector(".div-left-panel")
      .classList.toggle("div-panel-hide");
    document
      .querySelector(".div-right-panel")
      .classList.toggle("div-panel-hide");
  });
});
const createCMatrixEffect = (canvas) => {
  const ctx = canvas.getContext("2d");

  canvas.width = canvas.parentElement.offsetWidth;
  canvas.height = canvas.parentElement.offsetHeight;

  const fontSize = 16;
  const columns = canvas.width / fontSize;
  const drops = Array(Math.floor(columns)).fill(1);

  const draw = () => {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0F0";
    ctx.font = `${fontSize}px monospace`;

    drops.forEach((y, x) => {
      const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
      const text = chars.charAt(
        Math.floor(Math.random() * chars.length)
      );
      ctx.fillText(text, x * fontSize, y * fontSize);

      if (y * fontSize > canvas.height && Math.random() > 0.975) {
        drops[x] = 0;
      }
      drops[x]++;
    });
  };

  setInterval(draw, 50);
};

const bodyCanvas = document.createElement("canvas");
bodyCanvas.style.position = "fixed";
bodyCanvas.style.top = 0;
bodyCanvas.style.left = 0;
bodyCanvas.style.zIndex = -1;
document.body.appendChild(bodyCanvas);
createCMatrixEffect(bodyCanvas);