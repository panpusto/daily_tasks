# Create a function that returns the name of the winner in a fight between two fighters.
# Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.
# Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.
# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
# Your function also receives a third argument, a string, with the name of the fighter that attacks first.

# Example:
#   declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"

#   Lew attacks Harry; Harry now has 3 health.
#   Harry attacks Lew; Lew now has 6 health.
#   Lew attacks Harry; Harry now has 1 health.
#   Harry attacks Lew; Lew now has 2 health.
#   Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
import unittest

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


# solution
def declare_winner(fighter1, fighter2, first_attacker):
    winner = ''
    if fighter1.name == first_attacker:
      p1 = fighter1
      p2 = fighter2
    else:
      p1 = fighter2
      p2 = fighter1
      
    while p1.health > 0 or p2.health > 0:
      p2.health -= p1.damage_per_attack
      if p2.health < 0:
        print(f'{p1.name} attacks {p2.name}: {p2.name} now has {p2.health} and is dead. {p1.name} wins.')
        winner += p1.name
        break
      else:
        print(f'{p1.name} attacks {p2.name}; {p2.name} now has {p2.health} health')
      
      p1.health -= p2.damage_per_attack
      if p1.health <= 0:
        print(f'{p2.name} attacks {p1.name}: {p1.name} now has {p1.health} and is dead. {p2.name} wins.')
        winner += p2.name
        break
      else:
        print(f'{p2.name} attacks {p1.name}; {p1.name} now has {p1.health} health')
      

    return winner

# tests
class TestPrime(unittest.TestCase):
   def test_case_1(self):
      self.assertTrue(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")

   def test_case_2(self):
      self.assertTrue(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")

   def test_case_3(self):
      self.assertTrue(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")

   def test_case_4(self):
      self.assertTrue(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")

   def test_case_5(self):
      self.assertTrue(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")

   def test_case_6(self):
      self.assertTrue(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")


if __name__=='__main__':
	unittest.main()