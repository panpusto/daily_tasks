# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

# solution
import unittest

def count(s):
    if not s:
        return {}
    chars_dict = {}
    for char in [i for i in s]:
        chars_dict[char] = s.count(char)
    print(chars_dict)
    return chars_dict


# tests
class CountFuncTests(unittest.TestCase):
    def test_count_func(self):
        self.assertEqual(count('aba'), {'a': 2, 'b': 1})
        self.assertEqual(count(''), {})
        self.assertEqual(count('aa'), {'a' : 2})
        self.assertEqual(count('aabb'), {'b' : 2, 'a' : 2})


if __name__ == '__main__':
    unittest.main()