const UI_VERSION = "2.0.0";
const MAX_HISTORY_ITEMS = 10;
const STORAGE_KEY = "smart_calculator_ui_history";

const num1Input = document.getElementById("num1");
const num2Input = document.getElementById("num2");
const operationInput = document.getElementById("operation");
const resultEl = document.getElementById("result");
const historyList = document.getElementById("historyList");

const calculateBtn = document.getElementById("calculateBtn");
const swapBtn = document.getElementById("swapBtn");
const clearHistoryBtn = document.getElementById("clearHistoryBtn");

function loadHistory() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return [];
  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

function saveHistory(items) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
}

function renderHistory() {
  const items = loadHistory();
  historyList.innerHTML = "";

  if (items.length === 0) {
    const li = document.createElement("li");
    li.className = "empty";
    li.textContent = "No history yet.";
    historyList.appendChild(li);
    return;
  }

  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    historyList.appendChild(li);
  });
}

function getInputs() {
  const a = parseFloat(num1Input.value);
  const b = parseFloat(num2Input.value);

  if (Number.isNaN(a) || Number.isNaN(b)) {
    return { error: "Please enter both numbers." };
  }

  return { a, b, op: operationInput.value };
}

function calculate() {
  const input = getInputs();
  if (input.error) {
    resultEl.textContent = `Result: ${input.error}`;
    resultEl.className = "error";
    return;
  }

  const { a, b, op } = input;
  let result;
  let equation;

  switch (op) {
    case "add":
      result = a + b;
      equation = `${a} + ${b}`;
      break;
    case "sub":
      result = a - b;
      equation = `${a} - ${b}`;
      break;
    case "mul":
      result = a * b;
      equation = `${a} × ${b}`;
      break;
    case "div":
      if (b === 0) {
        resultEl.textContent = "Result: Cannot divide by zero.";
        resultEl.className = "error";
        return;
      }
      result = a / b;
      equation = `${a} ÷ ${b}`;
      break;
    case "percent":
      result = (a * b) / 100;
      equation = `${b}% of ${a}`;
      break;
    default:
      resultEl.textContent = "Result: Unknown operation.";
      resultEl.className = "error";
      return;
  }

  const display = `${equation} = ${result}`;
  resultEl.textContent = `Result: ${result}`;
  resultEl.className = "ok";

  const history = loadHistory();
  if (!history.includes(display)) {
    history.unshift(display);
    saveHistory(history.slice(0, MAX_HISTORY_ITEMS));
  }

  renderHistory();
}

function swapInputs() {
  const tmp = num1Input.value;
  num1Input.value = num2Input.value;
  num2Input.value = tmp;
}

function clearHistory() {
  localStorage.removeItem(STORAGE_KEY);
  renderHistory();
  resultEl.textContent = "Result: History cleared.";
  resultEl.className = "ok";
}

calculateBtn.addEventListener("click", calculate);
swapBtn.addEventListener("click", swapInputs);
clearHistoryBtn.addEventListener("click", clearHistory);

renderHistory();
console.log(`Smart Calculator UI loaded (v${UI_VERSION})`);
