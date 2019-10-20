"""
A Simple Blackjack game
"""

__author__ = 'Tyler Souza'

import random

# opening statement
print("Welcome to blackjack. Let's play \n")


class Deal(object):
    """
    Deals cards to player.
    """

    def __init__(self):
        self.card1 = random.randint(1, 11)
        self.card2 = random.randint(1, 11)
        self.sum_cards = self.card1 + self.card2
        print("Card1: %d \nCard2: %d" % self.card1, self.card2)
        print("Sum of deal cards: %d" % self.sum_cards)

        # Checks if deal cards are over or under 21
        if self.sum_cards > 21:
            print("You lose!")

        elif self.sum_cards == 21:
            print("Perfect! You win!")

    def decider(self):
        """
        decider method that checks if the player stays or hits.
        """
        # TODO: I Think this shuld be defined in __init__
        self.hitcard = random.randint(1, 11)
        if self.sum_cards < 21:
            dec = input("Do you want to hit? (Yes or no?)")

            if dec == 'yes'.lower():
                print("You have selected hit")
                after_hit = self.hitcard + self.sum_cards
                print("Sum after hit: %d" % after_hit)

                # if current_hand is less than 21. Shall you hit again?

                if after_hit < 21:
                    current_hand = after_hit
                    dec2 = input("Shall you hit again? yes or no?")
                    if dec2 == 'yes'.lower():
                        print("You have selected to hit again")
                        hit2 = self.hitcard + after_hit
                        print("Sum after second hit: %d" % hit2)

                    elif dec2 == 'no'.lower():
                        print("Not willing to take the risk?")
                        print("Current hand: %d" % current_hand)

                # if hand is of 21. Display losing statment
                if after_hit > 21:
                    print("Uh oh! You lose")

                elif after_hit == 21:
                    print("Woohoo! you won!")

            # player decides to stand
            elif dec == 'no'.lower():
                print("You have decided to stand")
                print("Current Hand: %d" % self.sum_cards)


def main():
    """
    Run the game.
    """
    deal = Deal()
    deal.decider()


if __name__ == '__main__':
    main()
