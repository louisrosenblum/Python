import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# November 14, 2017
# Anthony Louis Rosenblum
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Yahtzee:

    def __init__(self):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(6).roll()
        return(self.rolls)

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(7, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts
    def is_it_yahtzee(self):
        if 5 in self.count_outcomes():
            print("YAHTZEE")
            print(self.count_outcomes())
            return(True)
        else:
            return(False)
    def is_it_full_house(self):
        if 3 and 2 and not 1 in self.count_outcomes():
            print("FULL HOUSE")
            print(self.count_outcomes())
            return(True)
        else:
            return(False)
    def is_it_large_straight(self):
        if (self.count_outcomes()[1] == 1 and self.count_outcomes()[2] == 1 and self.count_outcomes()[3] == 1 and self.count_outcomes()[4] == 1 and self.count_outcomes()[5] == 1) or (self.count_outcomes()[2] == 1 and self.count_outcomes()[3] == 1 and self.count_outcomes()[4] == 1 and self.count_outcomes()[5] == 1 and self.count_outcomes()[6] == 1):
            print("LARGE STRAIGHT")
            print(self.count_outcomes())
            return(True)
        else:
            return(False)

# -------------------------------------------------
        
def main(how_many):

    yahtzees = 0
    full_houses = 0
    large_straights = 0
    game = Yahtzee()

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_yahtzee():
            yahtzees += 1
        elif game.is_it_full_house():
            full_houses += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of Yahtzees:", yahtzees)
    print("Yahtzee Percent:", "{:.2f}%\n".format(yahtzees * 100 / how_many))
    print("Number of Full Houses:", full_houses)
    print("Full House Percent:", "{:.2f}%\n".format(full_houses * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Large Straight Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------

main(5000)
    
        
