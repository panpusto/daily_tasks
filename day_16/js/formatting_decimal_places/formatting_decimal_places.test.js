const twoDecimalPlaces = require('./formatting_decimal_places');

test('Round input number to two decimal places', () => {
    expect(twoDecimalPlaces(4.659725356)).toBe(4.66);
    expect(twoDecimalPlaces(173735326.3783732637948948)).toBe(173735326.38);
    expect(twoDecimalPlaces(4.653725356)).toBe(4.65);
});
