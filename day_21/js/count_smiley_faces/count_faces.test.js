const { countSmileys, countSmileyRegex } = require('./count_faces');

test('[if statements] Returns number of smiley faces in array', () => {
    expect(countSmileys([])).toEqual(0);
    expect(countSmileys([':D',':~)',';~D',':)'])).toEqual(4);
    expect(countSmileys([':)',':(',':D',':O',':;'])).toEqual(2);
    expect(countSmileys([';]', ':[', ';*', ':$', ';-D'])).toEqual(1);
});

test('[regex func] Returns number of smiley faces in array', () => {
    expect(countSmileyRegex([])).toEqual(0);
    expect(countSmileyRegex([':D',':~)',';~D',':)'])).toEqual(4);
    expect(countSmileyRegex([':)',':(',':D',':O',':;'])).toEqual(2);
    expect(countSmileyRegex([';]', ':[', ';*', ':$', ';-D'])).toEqual(1);
});