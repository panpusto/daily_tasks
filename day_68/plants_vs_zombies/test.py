import unittest

from plants_vs_zombies import count_moves


test_cases = [
	[
		[
			'2       ',
			'  S     ',
			'21  S   ',
			'13      ',
			'2 3     '],
		[[0,4,28],[1,1,6],[2,0,10],[2,4,15],[3,2,16],[3,3,13]]],
	[
		[
			'11      ',
			' 2S     ',
			'11S     ',
			'3       ',
			'13      '],
		[[0,3,16],[2,2,15],[2,1,16],[4,4,30],[4,2,12],[5,0,14],[7,3,16],[7,0,13]]],
	[
		[
			'12        ',
			'3S        ',
			'2S        ',
			'1S        ',
			'2         ',
			'3         '],
		[[0,0,18],[2,3,12],[2,5,25],[4,2,21],[6,1,35],[6,4,9],[8,0,22],[8,1,8],[8,2,17],[10,3,18],[11,0,15],[12,4,21]]],
	[
		[
			'12      ',
			'2S      ',
			'1S      ',
			'2S      ',
			'3       '],
		[[0,0,15],[1,1,18],[2,2,14],[3,3,15],[4,4,13],[5,0,12],[6,1,19],[7,2,11],[8,3,17],[9,4,18],[10,0,15],[11,4,14]]],
	[
		[
			'1         ',
			'SS        ',
			'SSS       ',
			'SSS       ',
			'SS        ',
			'1         '],
		[[0,2,16],[1,3,19],[2,0,18],[4,2,21],[6,3,20],[7,5,17],[8,1,21],[8,2,11],[9,0,10],[11,4,23],[12,1,15],[13,3,22]]]
]

example_solutions = [10, 12, 20, 19, None]


class PlantsVsZombiesTests(unittest.TestCase):
    def test_count_moves_to_penetrates_defenses(self):
        for test in range(len(test_cases)):
            self.assertEqual(count_moves(test_cases[test][0], test_cases[test][1]), example_solutions[test])


if __name__ == '__main__':
    unittest.main()
