const calculateYears = require('./money_money_money');

test('Returns number of years to achive desired profit', () => {
    expect(calculateYears(1000, 0.05, 0.18, 1100)).toBe(3);
    expect(calculateYears(1000,0.01625,0.18,1200)).toBe(14);
    expect(calculateYears(1000,0.05,0.18,1000)).toBe(0);
});