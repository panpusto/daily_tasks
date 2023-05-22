const numberToPower = require('./power');

test('Integers raised to power', () => {
    expect(numberToPower(4, 2)).toEqual(16);
    expect(numberToPower(10, 4)).toEqual(10000);
    expect(numberToPower(10, 0)).toEqual(1);
    expect(numberToPower(31, 7)).toEqual(27512614111);
});
  
test("Floats raised to a power", () =>{
    expect(numberToPower(14.5, 9)).toEqual(28334269484.11914, 1e-9);
    expect(numberToPower(Math.PI, 2)).toEqual(9.869604401089358, 1e-9);
    expect(numberToPower(Math.PI/2, 14)).toEqual(556.7731434176238, 1e-9);
});