const predictAge = require('./predict_your_age');

test('Returns predicted age', () => {
    expect(predictAge(65, 60, 75, 55, 60, 63, 64, 45)).toBe(86);
});
