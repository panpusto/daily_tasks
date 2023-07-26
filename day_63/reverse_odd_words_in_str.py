# Reverse every other word in a given string, then return the string. Throw away
# any leading or trailing whitespace, while ensuring there is exactly one space
# between each word. Punctuation marks should be treated as if they are a part
# of the word in this kata.

###############################################################################

# solution
def reverse_alternate(text: str) -> str:
    wordlist = text.split()
    new_list = []

    for word in wordlist:
        if wordlist.index(word) % 2 == 0:
            new_list.append(word)
        else:
            new_list.append(word[::-1])
    
    return ' '.join(new_list)


# tests
import unittest

class ReverseAlternateTests(unittest.TestCase):
    test_cases = [
        ("Did it work?", "Did ti work?"),
        ("I really hope it works this time...", "I yllaer hope ti works siht time..."),
        ("Reverse this string, please!", "Reverse siht string, !esaelp"),
        ("Have a beer", "Have a beer"),
        ("   ", ""),
        ("This is not a test ", "This si not a test"),
        ("This       is a  test ", "This si a tset"),
    ]

    def test_reverse_alternate(self):
        for tested, expected in self.test_cases:
            self.assertEqual(reverse_alternate(tested), expected)


if __name__ == '__main__':
    unittest.main()
