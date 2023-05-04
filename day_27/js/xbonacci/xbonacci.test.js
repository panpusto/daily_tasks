const xbonacci = require('./xbonacci');

test('Returns n number sequence from initial signature where each following element is sum of the n previous elements', () => {
    expect(xbonacci([0,1],10)).toEqual([0,1,1,2,3,5,8,13,21,34]);
    expect(xbonacci([1,1],10)).toEqual([1,1,2,3,5,8,13,21,34,55]);
    expect(xbonacci([0,0,0,0,1],10)).toEqual([0,0,0,0,1,1,2,4,8,16]);
    expect(xbonacci([1,0,0,0,0,0,1],10)).toEqual([1,0,0,0,0,0,1,2,3,6]);
    expect(xbonacci([1,0,0,0,0,0,0,0,0,0],20)).toEqual([1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256]);
});
