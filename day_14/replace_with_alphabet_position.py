# Welcome.
#
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.
#
# Example
#
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

# solution
import string
def alphabet_position(text):
    if text.isdigit():
        return ''
    alphabet = string.ascii_lowercase
    alphabet_positions = []
    for char in text.lower().replace(' ', '').translate(str.maketrans('', '', string.punctuation)):
        alphabet_positions.append(alphabet.index(char) + 1)
    return ' '.join(str(num) for num in alphabet_positions)

# tests
import unittest
from random import randint

class ReplaceWithAlphabetBasicTests(unittest.TestCase):
    def test_char_position_in_alphabet(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."),
                           "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."),
                           "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

    def test_digits_as_function_param(self):
        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        self.assertEqual(alphabet_position(number_test), "")

if __name__ == '__main__':
    unittest.main()
