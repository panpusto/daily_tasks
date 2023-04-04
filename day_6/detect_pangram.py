# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
# Ignore numbers and punctuation.

# solution
import string
import unittest


def is_pangram(text):
    alphabet = set(string.ascii_lowercase)
    return set(str(text).lower()) >= alphabet


# tests
class DetectPangramTests(unittest.TestCase):
    def test_str_in_pangram(self):
        self.assertEqual(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
    
    def test_is_not_string(self):
        self.assertEqual(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)


if __name__ == '__main__':
    unittest.main()
