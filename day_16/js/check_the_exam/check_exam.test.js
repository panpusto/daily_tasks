const checkExam = require('./check_exam');
test('Returns valid number of total points', () => {
    expect(checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"])).toBe(6);
    expect(checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""])).toBe(7);
    expect(checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"])).toBe(16);
    expect(checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"])).toBe(0);
});

// run jest for testing
