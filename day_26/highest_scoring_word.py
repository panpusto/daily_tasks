# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.


# solution
import string

def high(x):
    alphabet = string.ascii_lowercase 
    highest_score = 0
    highest_word = ''

    for word in x.split():
        result = 0
        for letter in word:
            result += (alphabet.index(letter) + 1)
        
        if result > highest_score:
            highest_score = result
            highest_word = word

    return highest_word
        

# tests
import unittest

class HighestScoreBasicTests(unittest.TestCase):
    def test_highest_scoring_word(self):
        self.assertEqual(high('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(high('what time are we climbing up the volcano'), 'volcano')
        self.assertEqual(high('take me to semynak'), 'semynak')
        self.assertEqual(high('aa b'), 'aa')
        self.assertEqual(high('b aa'), 'b')
        self.assertEqual(high('bb d'), 'bb')
        self.assertEqual(high('d bb'), 'd')
        self.assertEqual(high("aaa b"), "aaa")


if __name__ == '__main__':
    unittest.main()
