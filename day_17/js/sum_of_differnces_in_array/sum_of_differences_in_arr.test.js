const sumOfDifferences = require('./sum_of_differences_in_arr');

test('Returns sum of differences in array', () => {
    expect(sumOfDifferences([1, 2, 10])).toEqual(9);
    expect(sumOfDifferences([-3, -2, -1])).toEqual(2);
});
