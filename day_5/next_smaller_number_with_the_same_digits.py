# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# For example:

# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing, for Rust: return None), 
# when there is no smaller number that contains the same digits. 
# Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.
# The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."


# solution
import unittest

def next_smaller(n):
    numbers = [int(num) for num in str(n)]
    next_smallest = float("-inf")
    nsc = float("-inf")
    position = len(numbers) - 1
    if(len(numbers) == 1 or numbers == sorted(numbers)):
        return -1
    
    # first number that's greater than previous digit => x
    for i in range(len(numbers)-1, 0, -1):
        if(numbers[i] < numbers[i - 1]):
            position -= 1
            break
        position -= 1
            
    # next smallest number starting from x+1 to the end of the list
    for i in range(position, len(numbers)):
        if(numbers[i] < numbers[position] and numbers[i] > next_smallest):
            next_smallest = numbers[i]
            nsc = i

    # swap x and the next smallest number
    numbers[position], numbers[nsc] = numbers[nsc], numbers[position]

    # sort from the index where you found x+1 to the end of the list
    numbers2 = numbers[position + 1:]
    numbers2.sort(reverse = True)
    for i in range(len(numbers2)):
        numbers[i + position + 1] = numbers2[i]
    numbers = [str(x) for x in numbers]
    result = "".join(numbers)
    
    return int(result) if result[0] != '0' else -1
    

# tests
class NextSmallerTests(unittest.TestCase):
    def test_next_smaller_method(self):
        self.assertEqual(next_smaller(907), 790)
        self.assertEqual(next_smaller(531), 513)
        self.assertEqual(next_smaller(135), -1)
        self.assertEqual(next_smaller(2071), 2017)
        self.assertEqual(next_smaller(414), 144)
        self.assertEqual(next_smaller(123456798), 123456789)
        self.assertEqual(next_smaller(123456789), -1)
        self.assertEqual(next_smaller(1234567908), 1234567890)


if __name__ == '__main__':
    unittest.main()