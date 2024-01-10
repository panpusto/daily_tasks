import unittest
from mexican_wave import wave

test_cases = [
    ("hello", ["Hello", "hEllo", "heLlo", "helLo", "hellO"]),
    ("codewars", ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]),
    ("", []),
    ("two words", ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]),
    (" gap ", [" Gap ", " gAp ", " gaP "]),
    ("a       b    ", ["A       b    ", "a       B    "]),
    ("this is a few words", ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"])
]


class MexicanWaveTests(unittest.TestCase):
    def test_mexican_wave(self):
        for tested, expected in test_cases:
            self.assertEqual(wave(tested), expected)


if __name__ == '__main__':
    unittest.main()
    