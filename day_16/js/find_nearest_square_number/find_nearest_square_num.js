// Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.
// For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121,
// since 111 is closer to 121, the square of 11, than 100, the square of 10.
// If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

// solution
const nearestSq = (n) => {
    if (Number.isInteger(Math.sqrt(n))) {
        return n
    } else {
        let num = Math.sqrt(n);
        if (Math.abs(Math.pow(Math.ceil(num), 2) - n) > Math.abs(Math.pow(Math.floor(num), 2) - n)) {
            return Math.pow(Math.floor(num), 2)
        } else {
            return Math.pow(Math.ceil(num), 2)
        }
    } 
};

module.exports = nearestSq;
