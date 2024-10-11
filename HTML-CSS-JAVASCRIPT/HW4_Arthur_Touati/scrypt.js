const appleQuantityInput = document.getElementById("appleQuantity");
const orangeQuantityInput = document.getElementById("orangeQuantity");
const bananaQuantityInput = document.getElementById("bananaQuantity");
const totalCostElement = document.getElementById("totalCost");

appleQuantityInput.addEventListener("input", validateInput);
orangeQuantityInput.addEventListener("input", validateInput);
bananaQuantityInput.addEventListener("input", validateInput);

function validateInput(event) {
  const input = event.target;
  const value = parseInt(input.value);

  if (isNaN(value) || value < 0 || value > 99) {
    input.value = "";
    alert("Please enter a valid number between 0 and 99.");
  } else {
    calculateTotal();
  }
}

function calculateTotal() {
  const appleQuantity = parseInt(appleQuantityInput.value) || 0;
  const orangeQuantity = parseInt(orangeQuantityInput.value) || 0;
  const bananaQuantity = parseInt(bananaQuantityInput.value) || 0;

  const appleCost = appleQuantity * 0.69;
  const orangeCost = orangeQuantity * 0.59;
  const bananaCost = bananaQuantity * 0.49;

  const totalCost = appleCost + orangeCost + bananaCost;
  const tax = totalCost * 0.0775;
  const finalTotal = totalCost + tax;

  totalCostElement.textContent = `Your total cost is $${finalTotal.toFixed(2)}`;

  return false; // Prevent form submission
}