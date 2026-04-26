function calculate() {
    let a = parseFloat(document.getElementById("num1").value);
    let b = parseFloat(document.getElementById("num2").value);
    let op = document.getElementById("operation").value;

    let result;

    if (op === "add") result = a + b;
    else if (op === "sub") result = a - b;
    else if (op === "mul") result = a * b;
    else if (op === "div") {
        if (b === 0) {
            result = "Cannot divide by zero";
        } else {
            result = a / b;
        }
    }

    document.getElementById("result").innerText = "Result: " + result;
      }
