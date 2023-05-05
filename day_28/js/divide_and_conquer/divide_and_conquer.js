// Given a mixed array of number and string representations of integers,
// add up the non-string integers and subtract the total of the string integers.
// Return as a number.

// solution
const divCon = (x) => {

    const numSum = x
        .filter(el => typeof el == 'number')
        .reduce((a, b) => a + b, 0);
    
    const strSum = x
        .filter(el => typeof el == 'string')
        .reduce((a, b) => +a + +b, 0);
    
    return numSum - strSum;
};


module.exports = divCon;