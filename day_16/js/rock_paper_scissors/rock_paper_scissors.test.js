const rps = require('./rock_paper_scissors');

test("Returns player who won", () => {
    const getMsg = (num) => `Player ${num} won!`;

    // player 1 win
    expect(rps('rock', 'scissors')).toBe(getMsg(1));
    expect(rps('scissors', 'paper')).toBe(getMsg(1));
    expect(rps('paper', 'rock')).toBe(getMsg(1));

    // player 2 win
    expect(rps('scissors', 'rock')).toBe(getMsg(2));
    expect(rps('paper', 'scissors')).toBe(getMsg(2));
    expect(rps('rock', 'paper')).toBe(getMsg(2));

    // draw
    expect(rps('rock', 'rock')).toBe('Draw!');
    expect(rps('scissors', 'scissors')).toBe('Draw!');
    expect(rps('paper', 'paper')).toBe('Draw!');
});