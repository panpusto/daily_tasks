const smallEnough = require('./small_enough');

test(
    'Returns a boolean value whose value depends on whether all elements of the array are less than or equal to a limit value',
    () => {
        expect(smallEnough([66, 101], 200)).toEqual(true);
        expect(smallEnough([78, 117, 110, 99, 104, 117, 107, 115], 100)).toEqual(false);
        expect(smallEnough([101, 45, 75, 105, 99, 107], 107)).toEqual(true);
        expect(smallEnough([80, 117, 115, 104, 45, 85, 112, 115], 120)).toEqual(true);
    });