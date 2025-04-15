// 📦 Khai báo biến tập trung
const centerPanel = document.querySelector(".center-panel");
const validChars = "ABCDEFGH";
const validKeyChars = "01";

const textInputEncrypt = document.getElementById("input-text-encrypt");
const textInputDecrypt = document.getElementById("input-text-decrypt");
const keyInputEncrypt = document.getElementById("encryption-key");
const keyInputDecrypt = document.getElementById("decryption-key");
const encryptResult = document.querySelector("#encrypt-result");
const decryptResult = document.querySelector("#decrypt-result");
const encryptResultSpan = encryptResult.querySelector("span");
const decryptResultSpan = decryptResult.querySelector("span");

const textInputs = [textInputEncrypt, textInputDecrypt];
const keyInputs = [keyInputEncrypt, keyInputDecrypt];

const toEncryptButton = document.querySelector("#to-encrypt-button");
const toDecryptButton = document.querySelector("#to-decrypt-button");

const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    const target = mutation.target;
    if (target.textContent === "") {
      target.classList.add("div-hidden");
    } else {
      target.classList.remove("div-hidden");
    }
  });
});

observer.observe(encryptResult, {
  characterData: true,
  childList: true,
  subtree: true,
});

observer.observe(decryptResult, {
  characterData: true,
  childList: true,
  subtree: true,
});

// 🔠 Validation cho ký tự A–H
textInputs.forEach((input) => {
  input.addEventListener("keydown", function (event) {
    const char = event.key;
    if (char.length === 1 && !validChars.includes(char.toUpperCase())) {
      event.preventDefault();
      showError("Chỉ được nhập các kí tự từ A đến H");
    }
  });

  input.addEventListener("input", function () {
    const filtered = input.value
      .split("")
      .filter((char) => validChars.includes(char.toUpperCase()));
    if (filtered.length < input.value.length) {
      input.value = filtered.join("");
      showError("Chỉ được nhập các kí tự từ A đến H");
    }
    input.value = input.value.toUpperCase();
  });
});

// 🧮 Validation cho key 0–1
keyInputs.forEach((input) => {
  input.addEventListener("keydown", function (event) {
    const char = event.key;
    if (char.length === 1 && !validKeyChars.includes(char)) {
      event.preventDefault();
      showError("Chỉ được nhập ký tự 0 hoặc 1");
    }
  });

  input.addEventListener("input", function () {
    let filtered = input.value
      .split("")
      .filter((char) => validKeyChars.includes(char));

    if (filtered.length < input.value.length) {
      showError("Chỉ được nhập ký tự 0 hoặc 1");
    }

    if (filtered.length > 23) {
      filtered = filtered.slice(0, 23);
      showError("Chỉ nhập tối đa 23 ký tự nhị phân");
    }

    input.value = filtered.join("");
  });
});

// 📢 Hàm hiển thị lỗi
function showError(message) {
  const errorContainer = document.querySelector(".error-container");

  if (!errorContainer) {
    const container = document.createElement("div");
    container.className = "error-container";
    container.style.display = "flex";
    container.style.flexDirection = "column";
    container.style.alignItems = "center";
    container.style.position = "absolute";
    container.style.width = "100%";
    centerPanel.appendChild(container);
  }

  const errorDiv = document.createElement("div");
  errorDiv.className = "error-message";
  errorDiv.textContent = message;
  errorDiv.style.color = "red";
  errorDiv.style.margin = "5px 0";

  document.querySelector(".error-container").appendChild(errorDiv);

  setTimeout(() => {
    errorDiv.remove();
    const container = document.querySelector(".error-container");
    if (container && container.children.length === 0) {
      container.remove();
    }
  }, 5000);
}

// 🔁 Toggle giữa panel mã hóa ⇄ giải mã
[toEncryptButton, toDecryptButton].forEach((button) => {
  button.addEventListener("click", function () {
    document
      .querySelector(".div-left-panel")
      .classList.toggle("div-panel-hide");
    document
      .querySelector(".div-right-panel")
      .classList.toggle("div-panel-hide");
  });
});

toDecryptButton.addEventListener("click", function () {
  if (keyInputEncrypt.value.length === 23) {
    keyInputDecrypt.value = keyInputEncrypt.value;
  }

  if (encryptResultSpan.textContent) {
    const cleanedText = encryptResultSpan.textContent.replace(
      "Kết quả mã hóa: ",
      ""
    );
    textInputDecrypt.value = cleanedText;
  }

  textInputEncrypt.value = "";
  keyInputEncrypt.value = "";
  encryptResultSpan.textContent = "";
});

toEncryptButton.addEventListener("click", function () {
  if (keyInputDecrypt.value.length === 23) {
    keyInputEncrypt.value = keyInputDecrypt.value;
  }

  if (decryptResultSpan.textContent) {
    const cleanedText = decryptResultSpan.textContent.replace(
      "Kết quả giải mã: ",
      ""
    );
    textInputEncrypt.value = cleanedText;
  }

  textInputDecrypt.value = "";
  keyInputDecrypt.value = "";
  decryptResultSpan.textContent = "";
});

// 🧽 Reset kết quả khi input thay đổi
textInputEncrypt.addEventListener(
  "input",
  () => (encryptResultSpan.textContent = "")
);
keyInputEncrypt.addEventListener(
  "input",
  () => (encryptResultSpan.textContent = "")
);
textInputDecrypt.addEventListener(
  "input",
  () => (decryptResultSpan.textContent = "")
);
keyInputDecrypt.addEventListener(
  "input",
  () => (decryptResultSpan.textContent = "")
);

// 🌧️ Matrix Effect
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
      const text = chars.charAt(Math.floor(Math.random() * chars.length));
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

const glitchEffectDuration = 5000;

let idleTimer = null;
let glitchInterval = null;

const isIdle = () => {
  const hasInput =
    textInputEncrypt.value ||
    textInputDecrypt.value ||
    keyInputEncrypt.value ||
    keyInputDecrypt.value;

  const hasOutput =
    encryptResultSpan.textContent || decryptResultSpan.textContent;

  return !hasInput && !hasOutput;
};

const resetGlitchEffect = () => {
  clearInterval(glitchInterval);
  glitchInterval = null;

  const logo = document.querySelector(".bouncing-logo");
  if (logo) {
    logo.remove();
  }
};

const getBrightColor = () => {
  const hue = Math.random() * 360;
  return `hsl(${hue}, 100%, 70%)`;
};

const startGlitchEffect = () => {
  // Ngừa trường hợp bị gọi nhiều lần
  if (document.querySelector(".bouncing-logo")) return;

  const logo = document.createElement("div");
  logo.className = "bouncing-logo";
  logo.textContent = "NO SIGNAL";
  logo.style.cssText = `
    position: absolute;
    padding: 20px;
    background: transparent;
    color: #00FF00;
    font-family: 'Courier New', monospace;
    font-size: 24px;
    font-weight: bold;
    user-select: none;
    text-shadow: 0 0 10px rgba(0, 255, 0, 0.5), 0 0 20px rgba(0, 255, 0, 0.7);
    white-space: nowrap;
    overflow: hidden;
  `;
  centerPanel.appendChild(logo);

  let posX = 0;
  let posY = 0;
  let dirX = 2;
  let dirY = 2;

  const maxX = 620;
  const maxY = 440;

  glitchInterval = setInterval(() => {
    // Nếu không còn idle nữa thì dừng hiệu ứng liền
    if (!isIdle()) {
      resetGlitchEffect();
      return;
    }

    posX += dirX;
    posY += dirY;

    if (posX + 310 >= maxX || posX + 310 <= 0) {
      dirX *= -1;
      logo.style.color = getBrightColor();
    }

    if (posY + 220 >= maxY || posY + 220 <= 0) {
      dirY *= -1;
      logo.style.color = getBrightColor();
    }

    logo.style.transform = `translate(${posX}px, ${posY}px)`;
  }, 50);
};

const handleIdleEffect = () => {
  clearTimeout(idleTimer);

  if (!isIdle()) {
    resetGlitchEffect(); // Dừng ngay nếu đang hoạt động
    return;
  }

  idleTimer = setTimeout(() => {
    if (isIdle()) {
      startGlitchEffect();
    }
  }, glitchEffectDuration);
};

["input", "change"].forEach((event) => {
  [
    textInputEncrypt,
    textInputDecrypt,
    keyInputEncrypt,
    keyInputDecrypt,
  ].forEach((element) => {
    element.addEventListener(event, handleIdleEffect);
  });
});

// Gọi lần đầu
handleIdleEffect();
