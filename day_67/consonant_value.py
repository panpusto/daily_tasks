# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant substrings. Consonants are any letters
# of the alphabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels. 
# We get: "z o d ia cs"

# -- The consonant substrings are: "z", "d" and "cs" and the values
# are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
# solve("zodiacs") = 26

# For the word "strength", solve("strength") = 57
# -- The consonant substrings are: "str" and "ngth" with values 
# "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

###############################################################################

# solution
from string import ascii_lowercase as alphabet

def count_consonant(text: str) -> str:
    consonants = set(alphabet) - set('aeiou')
    total_subs = []
    current_total = 0

    for char in text:
        if char in consonants:
            current_total += alphabet.index(char) + 1
        else:
            total_subs.append(current_total)
            current_total = 0
    
    if current_total:
        total_subs.append(current_total)

    return max(total_subs)


# tests
import unittest

class CountConsonants(unittest.TestCase):
    test_cases = [
        ("cozy", 51),
        ("xyzzy", 126),
        ("zodiac", 26),
        ("chruschtschov", 80),
        ("khrushchev", 38),
        ("strength", 57),
        ("catchphrase", 73),
        ("twelfthstreet", 103),
        ("mischtschenkoana", 80),
    ]

    def test_max_value_of_consonant_substring(self):
        for tested, expected in self.test_cases:
            self.assertEqual(count_consonant(tested), expected)


if __name__ == '__main__':
    unittest.main()
