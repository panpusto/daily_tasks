const descendingOrder = require('./descending_order');

test('Returns biggest possible integer', () => {
    expect(descendingOrder(0)).toEqual(0);
    expect(descendingOrder(1)).toEqual(1);
    expect(descendingOrder(111)).toEqual(111);
    expect(descendingOrder(15)).toEqual(51);
    expect(descendingOrder(1021)).toEqual(2110);
    expect(descendingOrder(123456789)).toEqual(987654321);
});
