// Your task is to sum the differences between consecutive pairs in the array in descending order.
// Example
// [2, 1, 10]  -->  9
// In descending order: [10, 2, 1]
// Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

// solution
const sumOfDifferences = (arr) => {
    arr.sort((a, b) => b - a);
    let result = 0;
    
    for (let i = 0; i < arr.length - 1; i++) {
        let subtraction = arr[i] - arr[i + 1];
        result += subtraction;
    };

    return result;
};


module.exports = sumOfDifferences;
