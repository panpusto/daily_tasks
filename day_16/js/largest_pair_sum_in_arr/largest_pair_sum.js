// Given a sequence of numbers, find the largest pair sum in the sequence.

// For example

// [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
// [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
// Input sequence contains minimum two elements and every element is an integer.

// solution
const largestPairSum = (numbers) => {
    sorted_nums = numbers.sort((a, b) => a - b);
    len = sorted_nums.length
    
    return sorted_nums[len - 1] + sorted_nums[len - 2]
};

module.exports = largestPairSum;
