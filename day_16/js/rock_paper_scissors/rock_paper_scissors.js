// Let's play! You have to return which player won! 
// In case of a draw return Draw!.

// Examples(Input1, Input2 --> Output):
// "scissors", "paper" --> "Player 1 won!"
// "scissors", "rock" --> "Player 2 won!"
// "paper", "paper" --> "Draw!"

// solution
const rps = (p1, p2) => {
    const rules = {
        scissors: 'paper',
        paper: 'rock',
        rock: 'scissors'
    };

    if (p1 === p2) {
        return 'Draw!'
    } else {
        return `Player ${rules[p1] === p2 ? 1 : 2} won!`
    }
};

module.exports = rps;
