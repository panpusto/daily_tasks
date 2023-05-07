const errorPrinter = require('./errors_printer');

let test_string = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz';
test('Returns number of not available letters in string', () => {
    expect(errorPrinter(test_string)).toEqual('3/56');
});