# Given a string "abc" and assuming that each letter in the string has a value
# equal to its position in the alphabet, our string will have a value of
# 1 + 2 + 3 = 6. This means that: a = 1, b = 2, c = 3 ....z = 26.

# You will be given a list of strings and your task will be to return the
# values of the strings as explained above multiplied by the position of
# that string in the list. For our purpose, position begins with 1.

# nameValue ["abc","abc abc"] should return [6,24] because of
# [ 6 * 1, 12 * 2 ]. Note how spaces are ignored.

# "abc" has a value of 6, while "abc abc" has a value of 12. Now, the value
# at position 1 is multiplied by 1 while the value at position 2 is 
# multiplied by 2.

# Input will only contain lowercase characters and spaces.


# solution
from string import ascii_lowercase as alphabet

def words_values(text: str) -> list[int]:
    return [
        sum(alphabet.index(char) + 1 for char in word if char.isalpha()) * (idx + 1) 
        for idx, word in enumerate(text)
    ]


# tests
import unittest


class WordsValuesTests(unittest.TestCase):
    def test_calculate_words_values(self):
        test_cases = [
            (["codewars","abc","xyz"], [88,12,225]),
            (["abc abc","abc abc","abc","abc"], [12,24,18,24]),
            (["abc","abc","abc","abc"], [6,12,18,24]),
            (["abcdefghijklmnopqrstuvwxyz","stamford bridge","haskellers"] , [351,282,330]),
            (["i love coding","better than pizza","i got this"], [115,382,321]),
            (["mercury","venus","earth mars","jupiter saturn","uranus neptune"], [103, 162, 309, 768, 945]),
            (["a cup","some tea","more coffee","one glass"], [41, 156, 273, 368]),
            (["a","e","i","o","u","the end"], [1, 10, 27, 60, 105, 336]),
            (["coding","better pizza","i got this too"], [52, 296, 471]),
        ]
        for tested, expected in test_cases:
            self.assertEqual(words_values(tested), expected)


if __name__ == '__main__':
    unittest.main()
