let secretNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

function checkGuess() {
  let guess = parseInt(document.getElementById("guessInput").value);
  let result = document.getElementById("result");

  attempts++;

  if (guess < secretNumber) {
    result.innerHTML = "Too Low ⬇️";
  } else if (guess > secretNumber) {
    result.innerHTML = "Too High ⬆️";
  } else {
    result.innerHTML = `🎉 Correct! You guessed in ${attempts} attempts`;
  }
}
