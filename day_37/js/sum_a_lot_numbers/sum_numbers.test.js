const { sumNumbers, sumNumbersLoop } = require('./sum_numbers');

test('Returns sums of numbers in range n', () => {
    expect(sumNumbers(100)).toEqual(5050);
    expect(sumNumbers(300)).toEqual(45150);
    expect(sumNumbers(50000)).toEqual(1250025000);
    expect(sumNumbers('n')).toEqual(false);
    expect(sumNumbers()).toEqual(false);
    expect(sumNumbers(3.14)).toEqual(false);
    expect(sumNumbers(0)).toEqual(false);
    expect(sumNumbers(-10)).toEqual(false); 
});

test('Returns sums of numbers (loop) in range n', () => {
    expect(sumNumbersLoop(100)).toEqual(5050);
    expect(sumNumbersLoop(300)).toEqual(45150);
    expect(sumNumbersLoop(50000)).toEqual(1250025000);
    expect(sumNumbersLoop('n')).toEqual(false);
    expect(sumNumbersLoop()).toEqual(false);
    expect(sumNumbersLoop(3.14)).toEqual(false);
    expect(sumNumbersLoop(0)).toEqual(false);
    expect(sumNumbersLoop(-10)).toEqual(false); 
});