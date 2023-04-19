const evaporator = require('./deodorant_evaporator');

test('Returns number of days when deodorant is useful', () => {
    expect(evaporator(10,10,10)).toBe(22);
    expect(evaporator(10,10,5)).toBe(29);
});
