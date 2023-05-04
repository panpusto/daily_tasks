# Every time your spies see a new ship enter the dock, they will create a new
# ship object based on their observations:

# draft - an estimate of the ship's weight based on how low it is in the wate
# crew - the count of crew on board
# Titanic = Ship(15, 10)
# Task

# You have access to the ship "draft" and "crew". "Draft" is the total ship
# weight and "crew" is the number of humans on the ship.

# Each crew member adds 1.5 units to the ship draft. If after removing the
# weight of the crew, the draft is still more than 20, then the ship is worth
# looting. Any ship weighing that much must have a lot of booty!

# Add the method
# is_worth_it
# to decide if the ship is worthy to loot. For example:

# Titanic.is_worth_it()
# False
# Good luck and may you find GOOOLD!

# solution
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20


# tests
import unittest

class ShipBasicTests(unittest.TestCase):
    def test_ship_not_worth_to_loot(self):
        emptyShip = Ship(15, 10)
        self.assertEqual(emptyShip.is_worth_it(), False)
    
    def test_ship_worth_to_loot(self):
        richShip = Ship(60, 10)
        self.assertEqual(richShip.is_worth_it(), True)


if __name__ == '__main__':
    unittest.main()
