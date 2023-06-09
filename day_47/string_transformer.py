# Given a string, return a new string that has transformed based on the input:
# Change case of every character, ie. lower case to upper case, upper case
# to lower case.
# Reverse the order of words from the input.
# Note: You will have to handle multiple spaces, and leading/trailing spaces.

# For example:

# "Example Input" ==> "iNPUT eXAMPLE"
# You may assume the input only contain English alphabet and spaces.


# solution
def string_transformer(s):
    transformed_words = [
        word.swapcase() for word in reversed(s.split(' ')) if word != ' '
    ]
    return ' '.join(transformed_words)
          


# tests
import unittest

class TransformStringTests(unittest.TestCase):
    def test_string_transform(self):
        self.assertEqual(string_transformer("Example string"), "STRING eXAMPLE")
        self.assertEqual(string_transformer("Example Input"), "iNPUT eXAMPLE")
        self.assertEqual(string_transformer("To be OR not to be That is the Question"), "qUESTION THE IS tHAT BE TO NOT or BE tO")
        self.assertEqual(string_transformer(""), "")
        self.assertEqual(string_transformer("You Know When  THAT  Hotline Bling"), "bLING hOTLINE  that  wHEN kNOW yOU")
        self.assertEqual(string_transformer(" A b C d E f G "), " g F e D c B a ")
    

if __name__ == '__main__':
    unittest.main()
