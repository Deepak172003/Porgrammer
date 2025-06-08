let userScore = 0;
    let computerScore = 0;

    const choices = document.querySelectorAll(".choice");
    const playerScoreDisplay = document.getElementById("player-score-value");
    const computerScoreDisplay = document.getElementById("computer-score-value");
    const message = document.getElementById("msg");

    const getComputerChoice = () => {
      const options = ["stone", "paper", "scissor"];
      const randomIndex = Math.floor(Math.random() * options.length);
      return options[randomIndex];
    };

    const playGame = (userChoice) => {
      const compChoice = getComputerChoice();

      if (userChoice === compChoice) {
        message.textContent = "It's a tie!";
        return;
      }

      let userWins =
        (userChoice === "stone" && compChoice === "scissor") ||
        (userChoice === "paper" && compChoice === "stone") ||
        (userChoice === "scissor" && compChoice === "paper");

      if (userWins) {
        userScore++;
        playerScoreDisplay.textContent = userScore;
        message.textContent = `You Win! ${userChoice} beats ${compChoice}`;
      } else {
        computerScore++;
        computerScoreDisplay.textContent = computerScore;
        message.textContent = `Computer Wins! ${compChoice} beats ${userChoice}`;
      }
    };
    choices.forEach((choice) => {
      choice.addEventListener("click", () => {
        const userChoice = choice.getAttribute("id");
        playGame(userChoice);
      });
    });
