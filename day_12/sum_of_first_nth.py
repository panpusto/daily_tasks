# Task:
# Your task is to write a function which returns the sum of following series upto nth term(parameter).
#
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
# You need to round the answer to 2 decimal places and return it as String.
# If the given value is 0 then it should return 0.00
# You will only be given Natural Numbers as arguments.
#
# Examples:(Input --> Output)
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

# solution
def series_sum(n):
    if n == 0 or n == 1:
        return '{:.2f}'.format(n)
    else:
        n -= 1
        sum_list = [1]
        while n > 0:
            x = 1 / float(n * 3 + 1)
            sum_list.append(x)
            n -= 1
        return '{:.2f}'.format(sum(sum_list))




# tests
import unittest

class SeriesSumBasicTests(unittest.TestCase):
    def test_series_sum_func(self):
        self.assertEqual(series_sum(1), "1.00")
        self.assertEqual(series_sum(2), "1.25")
        self.assertEqual(series_sum(3), "1.39")


if __name__ == '__main__':
    unittest.main()
