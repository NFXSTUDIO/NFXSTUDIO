function calculateFactorials() {
  const numberInput = document.getElementById("numberInput");
  const factorialTable = document.getElementById("factorialTable");
  const tableBody = factorialTable.querySelector("tbody");

  const n = parseInt(numberInput.value);

  tableBody.innerHTML = ""; // Clear previous table content

  for (let i = 1; i <= n; i++) {
    const factorial = calculateFactorial(i);
    const row = document.createElement("tr");
    row.innerHTML = `<td>${i}</td><td>${factorial}</td>`;
    tableBody.appendChild(row);
  }
}

function calculateFactorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * calculateFactorial(n - 1);
  }
}