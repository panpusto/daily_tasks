# Count the number of occurrences of each character and return it as a
# (list of tuples) in order of appearance. For empty output return
# (an empty list).

# Consult the solution set-up for the exact data structure implementation
# depending on your language.

# Example:
# ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]


# solution
from collections import Counter

def ordered_count(inp):
    return list(Counter(inp).items())


# tests
import unittest

class OrderedCountBasicTests(unittest.TestCase):
    def test_create_ordered_list_with_counted_elements(self):
        expected_result = [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
        self.assertEqual(ordered_count('abracadabra'), expected_result)
        expected_result = [
            ('C', 1), ('o', 1), ('d', 1),
            ('e', 1), (' ', 1), ('W', 1),
            ('a', 1), ('r', 1), ('s', 1)
            ]
        self.assertEqual(ordered_count('Code Wars'), expected_result)


if __name__ == '__main__':
    unittest.main()