const deleteNth = require('./delete_occurences_of_elem_in_arr');

test('Returns array contains each element at most N times', () => {
    expect(deleteNth([20,37,20,21], 1)).toEqual([20,37,21]);
    expect(deleteNth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3)).toEqual([1, 1, 3, 3, 7, 2, 2, 2]);
});
