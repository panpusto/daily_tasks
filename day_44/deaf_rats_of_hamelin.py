# Story

# The Pied Piper has been enlisted to play his magical tune and coax all the
# rats out of town.
# But some of the rats are deaf and are going the wrong way!

# Kata Task
# How many deaf rats are there?

# Legend
# P = The Pied Piper
# O~ = Rat going left
# ~O = Rat going right

# Example
# ex1 ~O~O~O~O P has 0 deaf rats
# ex2 P O~ O~ ~O O~ has 1 deaf rat
# ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

# solution
def count_deaf_rats(town):
    town_repl = town.replace(' ', '')
    p_idx = town_repl.find('P')
    
    left = town_repl[:p_idx]
    right = town_repl[p_idx + 1:]

    deaf_left = sum(1 for i in range(0, len(left), 2) if left[i:i+2] == 'O~')
    deaf_right = sum(1 for i in range(0, len(right), 2) if right[i:i+2] == '~O')

    return deaf_left + deaf_right


# tests
import unittest

class CountDeafRatsTests(unittest.TestCase):
    def test_count_deaf_rats(self):
        self.assertEqual(count_deaf_rats("~O~O~O~O P"), 0)
        self.assertEqual(count_deaf_rats("P O~ O~ ~O O~"), 1)
        self.assertEqual(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)


if __name__ == '__main__':
    unittest.main()
    