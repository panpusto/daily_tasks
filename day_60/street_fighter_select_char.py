# Some of you might remember spending afternoons playing Street Fighter 2 in
# some Arcade back in the 90s or emulating it nowadays with the numerous
# emulators for retro consoles.

# Can you solve this kata? Suuure-You-Can!
# UPDATE: a new kata's harder version is available here.

# The Kata
# You'll have to simulate the video game's character selection screen behaviour,
# more specifically the selection grid. Such screen looks like this:

# Screen:
# screen

# Selection Grid Layout in text:
# | Ryu  | E.Honda | Blanka  | Guile   | Balrog | Vega    |
# | Ken  | Chun Li | Zangief | Dhalsim | Sagat  | M.Bison |

# Input
# - the list of game characters in a 2x6 grid;
# - the initial position of the selection cursor (top-left is (0,0));
# - a list of moves of the selection cursor (which are up, down, left, right);

# Output
# the list of characters who have been hovered by the selection cursor after
# all the moves (ordered and with repetition, all the ones after a move, 
# whether successful or not, see tests);

# Rules
# Selection cursor is circular horizontally but not vertically!
# As you might remember from the game, the selection cursor rotates horizontally
# but not vertically; that means that if I'm in the leftmost and I try to go
# left again I'll get to the rightmost (examples: from Ryu to Vega, from Ken
# to M.Bison) and vice versa from rightmost to leftmost.

# Instead, if I try to go further up from the upmost or further down from the
# downmost, I'll just stay where I am located (examples: you can't go lower
# than lowest row: Ken, Chun Li, Zangief, Dhalsim, Sagat and M.Bison in the
# above image; you can't go upper than highest row: Ryu, E.Honda, Blanka,
# Guile, Balrog and Vega in the above image).

# Test
# For this easy version the fighters grid layout and the initial position will
# always be the same in all tests, only the list of moves change.

# Notice: changing some of the input data might not help you.

# Examples
# fighters = [
#   ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#   ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# initial_position = (0,0)
# moves = ['up', 'left', 'right', 'left', 'left']
# then I should get:

# ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog']
# as the characters I've been hovering with the selection cursor during my moves. Notice: Ryu is the first just because it "fails" the first up See test cases for more examples.

# fighters = [
#   ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#   ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# initial_position = (0,0)
# moves = ['right', 'down', 'left', 'left', 'left', 'left', 'right']

# Result:
# ['E.Honda', 'Chun Li', 'Ken', 'M.Bison', 'Sagat', 'Dhalsim', 'Sagat']


# solution
def select_character(fighters: list[str], init_position: tuple[int], moves: list[str]):
    rows = len(fighters)
    cols = len(fighters[0])
    current_position = list(init_position)
    selected_fighters = []

    for move in moves:
        direction = move.lower()

        if direction == 'up':
            current_position[0] = max(0, current_position[0] - 1)
        elif direction == 'down':
            current_position[0] = min(rows - 1, current_position[0] + 1)
        elif direction == 'left':
            current_position[1] = (current_position[1] - 1) % cols
        elif direction == 'right':
            current_position[1] = (current_position[1] + 1) % cols

        selected_fighters.append(fighters[current_position[0]][current_position[1]])

    return selected_fighters

# tests
import unittest

class StreetFighterSelectCharTests(unittest.TestCase):
    fighters = [
        ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
        ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]

    position = 0, 0

    test_cases = [
        ([], []),
        (["left"]*8, ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']),
        (["right"]*8, ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']),
        (["up"]*4, ['Ryu', 'Ryu', 'Ryu', 'Ryu']),
        (["down"]*4, ['Ken', 'Ken', 'Ken', 'Ken']),
        (["down","right","up","left"]*2, ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']),
        (["up","left","down","right"]*2, ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']),
        (["up"]+["left"]*6+["down"]+["right"]*6, ['Ryu', 'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Ken'])
    ]
    def test_create_list_of_selected_characters(self):
        for moves, solution in self.test_cases:
            self.assertEqual(select_character(self.fighters, self.position, moves), solution)


if __name__ == '__main__':
    unittest.main()
