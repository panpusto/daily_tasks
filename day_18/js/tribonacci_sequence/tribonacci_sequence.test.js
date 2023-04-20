const tribonacci = require('./tribonacci_sequence');

test('Returns array in which each subsequent element is the sum of the previous three', () => {
    expect(tribonacci([1,1,1], 10)).toEqual([1,1,1,3,5,9,17,31,57,105]);
    expect(tribonacci([0,0,1], 10)).toEqual([0,0,1,1,2,4,7,13,24,44]);
    expect(tribonacci([0,1,1], 10)).toEqual([0,1,1,2,4,7,13,24,44,81]);
    expect(tribonacci([1,0,0], 10)).toEqual([1,0,0,1,1,2,4,7,13,24]);
    expect(tribonacci([0,0,0], 10)).toEqual([0,0,0,0,0,0,0,0,0,0]);
    expect(tribonacci([1,2,3], 10)).toEqual([1,2,3,6,11,20,37,68,125,230]);
    expect(tribonacci([3,2,1], 10)).toEqual([3,2,1,6,9,16,31,56,103,190]);
    expect(tribonacci([1,1,1], 1)).toEqual([1]);
    expect(tribonacci([300,200,100], 0)).toEqual([]);
});
