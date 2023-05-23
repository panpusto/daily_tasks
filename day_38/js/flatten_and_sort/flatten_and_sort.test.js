const { flattenAndSort, flattenAndSort2 } = require('./flatten_and_sort');

test('Returns flatten and sorted array', () => {
    expect(flattenAndSort([[]])).toEqual([]);
    expect(flattenAndSort([[], []])).toEqual([]);
    expect(flattenAndSort([[], [1]])).toEqual([1]);
    expect(flattenAndSort([[], [], [], [2], [], [1]])).toEqual([1, 2]);
    expect(flattenAndSort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    expect(flattenAndSort([[1, 3, 5], [100], [2, 4, 6]])).toEqual([1, 2, 3, 4, 5, 6, 100]);
    expect(flattenAndSort([[111, 999], [222], [333], [444], [888], [777], [666], [555]])).toEqual([111, 222, 333, 444, 555, 666, 777, 888, 999]);
});

test('Returns flatten and sorted array - func2', () => {
    expect(flattenAndSort2([[]])).toEqual([]);
    expect(flattenAndSort2([[], []])).toEqual([]);
    expect(flattenAndSort2([[], [1]])).toEqual([1]);
    expect(flattenAndSort2([[], [], [], [2], [], [1]])).toEqual([1, 2]);
    expect(flattenAndSort2([[3, 2, 1], [7, 9, 8], [6, 4, 5]])).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    expect(flattenAndSort2([[1, 3, 5], [100], [2, 4, 6]])).toEqual([1, 2, 3, 4, 5, 6, 100]);
    expect(flattenAndSort2([[111, 999], [222], [333], [444], [888], [777], [666], [555]])).toEqual([111, 222, 333, 444, 555, 666, 777, 888, 999]);
});