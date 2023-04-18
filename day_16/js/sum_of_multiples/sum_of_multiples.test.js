const sumMul = require('./sum_of_multiples');

test('Returns sum of all multiples of n below m', () => {
    expect(sumMul(0, 0)).toBe('INVALID');
    expect(sumMul(2, 9)).toBe(20);
    expect(sumMul(4, -7)).toBe('INVALID');
});
