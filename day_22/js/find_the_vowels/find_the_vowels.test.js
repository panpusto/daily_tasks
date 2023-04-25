const vowelIndices = require('./find_the_vowels');

test('Returns vowel indices', () => {
    expect(vowelIndices("mmm")).toEqual([]);
    expect(vowelIndices("apple")).toEqual([1,5]);
    expect(vowelIndices("super")).toEqual([2,4]);
    expect(vowelIndices("orange")).toEqual([1,3,6]);
    expect(vowelIndices("supercalifragilisticexpialidocious")).toEqual([2,4,7,9,12,14,16,19,21,24,25,27,29,31,32,33]);
});