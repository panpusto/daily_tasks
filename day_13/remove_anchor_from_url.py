# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

# solution
import re

def remove_url_anchor(url):
    return re.sub('#.+$', '', url)

# tests
import unittest

class RemoveURLAnchorBasicTests(unittest.TestCase):
    def test_remove_anchor(self):
        self.assertEqual(remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
        self.assertEqual(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
        self.assertEqual(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")


if __name__ == '__main__':
    unittest.main()
