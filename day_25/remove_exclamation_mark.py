# Description:
# Remove all exclamation marks from the end of sentence.
#
# Examples:
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi! Hi"
# remove("Hi") === "Hi"


# solution 1
def remove(s):
    while s[-1] == '!':
        s = s[:-1]
        remove(s)
    return s


# solution 2
# def remove(s):
#     return s.rstrip('!')

# tests
import unittest

class RemoveMarkBasicTests(unittest.TestCase):
    def test_remove_exclamation_mark_from_the_end(self):
        self.assertEqual(remove("Hi!"), "Hi")
        self.assertEqual(remove("Hi!!!"), "Hi")
        self.assertEqual(remove("!Hi"), "!Hi")
        self.assertEqual(remove("!Hi!"), "!Hi")
        self.assertEqual(remove("Hi! Hi!"), "Hi! Hi")
        self.assertEqual(remove("Hi"), "Hi")


if __name__ == '__main__':
    unittest.main()
