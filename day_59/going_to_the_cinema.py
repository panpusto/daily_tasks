# My friend John likes to go to the cinema. He can choose between system A
# and system B.

# System A : he buys a ticket (15 dollars) every time
# System B : he buys a card (500 dollars) and a first ticket for 0.90 times
# the ticket price, then for each additional ticket he pays 0.90 times the
# price paid for the previous ticket.
    
# Example:
# If John goes to the cinema 3 times:
# System A : 15 * 3 = 45
# System B : 500 + 15 * 0.90 + (15 * 0.90) * 0.90 + (15 * 0.90 * 0.90) * 0.90 ( = 536.5849999999999,
# no rounding for each ticket)
# John wants to know how many times he must go to the cinema so that the final
# result of System B, when rounded up to the next dollar, will be cheaper
# than System A.

# The function movie has 3 parameters: card (price of the card), ticket
# (normal price of a ticket), perc (fraction of what he paid for the previous
# ticket) and returns the first n such that

# ceil(price of System B) < price of System A.

# More examples:
# movie(500, 15, 0.9) should return 43 
#     (with card the total price is 634, with tickets 645)
# movie(100, 10, 0.95) should return 24 
#     (with card the total price is 235, with tickets 240)


# solution
import math

def movie(card: int, ticket: int, perc: float) -> int:
    system_A = 0
    system_B = card
    tix_cost_in_sys_B = ticket
    tickets_num = 0

    while system_A <= math.ceil(system_B):
        system_A += ticket
        tix_cost_in_sys_B *= perc
        system_B += tix_cost_in_sys_B
        tickets_num += 1
    
    return tickets_num


# tests
import unittest

class MovieCostTests(unittest.TestCase):
    test_cases = [
        ((500, 15, 0.9), 43),
        ((100, 10, 0.95), 24),
        ((0, 10, 0.95), 2),
        ((250, 20, 0.9), 21),
        ((500, 20, 0.9), 34),
        ((2500, 20, 0.9), 135),
    ]

    def test_calculate_number_of_tickets(self):
        for tested, expected in self.test_cases:
            self.assertEqual(movie(tested[0], tested[1], tested[2]), expected)


if __name__ == '__main__':
    unittest.main()
