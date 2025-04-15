const encryptForm = document.getElementById("encryption-form");
const decryptForm = document.getElementById("decryption-form");

const API_URL = "http://127.0.0.1:8000/api/Tiny-A51";

let encryptDetails = "";
let decryptDetails = "";

encryptForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const inputText = document.getElementById("input-text-encrypt").value.trim();
  const key = document.getElementById("encryption-key").value.trim();

  if (inputText === "" || key.length !== 23 || /[^01]/.test(key)) {
    showError("Vui lòng nhập đầy đủ kí tự và khóa hợp lệ (23 ký tự 0/1)");
    return;
  }

  const requestBody = {
    plain_text: inputText,
    key: key,
    type: "encrypt",
  };

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });

    const data = await response.json();

    if (!response.ok) throw data.detail || "Có lỗi xảy ra";

    const resultText =
      inputText.length === 1 ? data.encrypted_character : data.encrypted_string;

    document.querySelector("#encrypt-result span").textContent = resultText;
    document.getElementById("encrypt-result").classList.remove("div-hidden");

    encryptDetails = data.process_details || "";
    document.getElementById("encrypt-show").classList.remove("div-hidden");
  } catch (err) {
    showError("Lỗi khi mã hóa: " + (err.message || err));
  }
});

// Giải mã
decryptForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const inputText = document.getElementById("input-text-decrypt").value.trim();
  const key = document.getElementById("decryption-key").value.trim();

  if (inputText === "" || key.length !== 23 || /[^01]/.test(key)) {
    showError("Vui lòng nhập đầy đủ kí tự và khóa hợp lệ (23 ký tự 0/1)");
    return;
  }

  const requestBody = {
    plain_text: inputText,
    key: key,
    type: "decrypt",
  };

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });

    const data = await response.json();

    if (!response.ok) throw data.detail || "Có lỗi xảy ra";

    const resultText =
      inputText.length === 1 ? data.decrypted_character : data.decrypted_string;

    document.querySelector("#decrypt-result span").textContent = resultText;
    document.getElementById("decrypt-result").classList.remove("div-hidden");

    decryptDetails = data.process_details || "";
    document.getElementById("decrypt-show").classList.remove("div-hidden");
  } catch (err) {
    showError("Lỗi khi giải mã: " + (err.message || err));
  }
});
