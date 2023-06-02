# Filter the number

# Oh, no! The number has been mixed up with the text. Your goal is to retrieve
# the number from the text, can you return the number back to
# its original state?

# Task
# Your task is to return a number from a string.

# Details
# You will be given a string of numbers and letters mixed up, you have to
# return all the numbers in that string in the order they occur.

# solution
def filter_string(string):
    return int(''.join([i for i in string if i.isdigit()]))


# tests
import unittest

class FilteringString(unittest.TestCase):
    def test_filter_numbers(self):
        self.assertEqual(filter_string("123"), 123)
        self.assertEqual(filter_string("a1b2c3"), 123)
        self.assertEqual(filter_string("aa1bb2cc3dd"), 123)
        self.assertEqual(filter_string("aa 112 3dd"), 1123)
        self.assertEqual(filter_string("11bb2c23c3"), 112233)


if __name__ == '__main__':
    unittest.main()
