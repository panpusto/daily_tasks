# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant substrings. Consonants are any letters
# of the alphabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels.
#  We get: "z o d ia cs"

# The consonant substrings are: "z", "d" and "cs" and the values are z = 26,
# d = 4 and cs = 3 + 19 = 22. The highest is 26.
# solve("zodiacs") = 26

# For the word "strength", solve("strength") = 57
# -- The consonant substrings are: "str" and "ngth" with values
# "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. 
# The highest is 57.

# solution 
import string

def solve(s):
    alphabet = string.ascii_lowercase
    consonants = set(alphabet) - set('aeiou')
    result_arr = []
    current_sum = 0

    for char in s:
        if char in consonants:
            current_sum += alphabet.index(char) + 1
        else:
            result_arr.append(current_sum)
            current_sum = 0
    
    return max(result_arr)


# tests
import unittest

class ConsonantValueBasicTests(unittest.TestCase):
    def test_max_consonant_value(self):
        self.assertEqual(solve("zodiac"),26)
        self.assertEqual(solve("chruschtschov"),80)
        self.assertEqual(solve("khrushchev"),38)
        self.assertEqual(solve("strength"),57)
        self.assertEqual(solve("catchphrase"),73)
        self.assertEqual(solve("twelfthstreet"),103)
        self.assertEqual(solve("mischtschenkoana"),80)


if __name__ == '__main__':
    unittest.main()
