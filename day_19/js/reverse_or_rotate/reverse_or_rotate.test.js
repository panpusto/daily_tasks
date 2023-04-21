const revrot = require('./reverse_or_rotate');

test('Returns reversed or rotated string chunks of size sz', () => {
    expect(revrot('1234', 0)).toEqual('');
    expect(revrot('', 0)).toEqual('');
    expect(revrot('1234', 5)).toEqual('');
    expect(revrot('733049910872815764', 5)).toEqual('330479108928157');
});