# An anagram is the result of rearranging the letters of a word to 
# produce a new word (see wikipedia).

# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams
# of each other; return false otherwise.

# Examples
# "foefet" is an anagram of "toffee"
# "Buckethead" is an anagram of "DeathCubeK"


# solution
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


# tests
import unittest

class AnagramBasicTests(unittest.TestCase):
    def test_words_are_anagrams(self):
        self.assertEqual(is_anagram("foefet", "toffee"), True)
        self.assertEqual(is_anagram("Buckethead", "DeathCubeK"), True)
        self.assertEqual(is_anagram("Twoo", "WooT"), True)
    
    def test_words_are_not_anagrams(self):
        self.assertEqual(is_anagram("dumble", "bumble"), False)
        self.assertEqual(is_anagram("ound", "round"), False)
        self.assertEqual(is_anagram("apple", "pale"), False)


if __name__ == '__main__':
    unittest.main()
