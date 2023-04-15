# Create a function that accepts a list/array and a number n,
# and returns a list/array of the first n elements from the list/array.

# solution
def take(arr,n):
    return arr[:n]

# tests
import unittest

class TakeFirstBasicTests(unittest.TestCase):
    def test_take_first_n_elements(self):
        self.assertEquals(take([0, 1, 2, 3, 4, 5], 3), [0, 1, 2])
        self.assertEquals(take([10, 21, 45], 1), [10])

if __name__ == '__main__':
    unittest.main()
