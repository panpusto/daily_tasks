const nearestSq = require('./find_nearest_square_num');
test('Returns nearest square number', () => {
    expect(nearestSq(1)).toBe(1);
    expect(nearestSq(2)).toBe(1);
    expect(nearestSq(10)).toBe(9);
    expect(nearestSq(111)).toBe(121);
    expect(nearestSq(9999)).toBe(10000);
});
