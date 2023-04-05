# A hero is on his way to the castle to complete his mission. 
# However, he's been told that the castle is surrounded with a couple of powerful dragons!
# Each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.
# Assuming he's gonna grab a specific given number of bullets and move forward 
# to fight another specific given number of dragons, will he survive?
# Return True if yes, False otherwise :)


# solution
import unittest

def hero(bullets, dragons):
    return bullets // 2 >= dragons


# tests
class HeroTest(unittest.TestCase):
    def test_hero_func(self):
        self.assertEqual(hero(10, 5), True)
        self.assertEqual(hero(7, 4), False)
        self.assertEqual(hero(4, 5), False)
        self.assertEqual(hero(100, 40), True)
        self.assertEqual(hero(1500, 751), False)
        self.assertEqual(hero(0, 1), False)


if __name__ == '__main__':
    unittest.main()
    