import random
import matplotlib.pyplot as plt
import numpy as np

class Card:
    def __init__(self,x):
        if x == "one":
            self.value = 1
        elif x == "two":
            self.value = 2
        elif x == "three":
            self.value = 3
        elif x == "four":
            self.value = 4
        elif x == "five":
            self.value = 5
        elif x == "six":
            self.value = 6
        elif x == "seven":
            self.value = 7
        elif x == "eight":
            self.value = 8
        elif x == "nine":
            self.value = 9
        elif x == "ten" or x == "jack" or x == "queen" or x == "king":
            self.value = 10
        elif x == "ace":
            self.value = 11

    def __str__(self):
        return(str(self.value))

deck = {}

for i in range(4):
    deck[str(0 + 13*i)] = Card("ace") #Ace
    deck[str(1 + 13*i)] = Card("two") #Two
    deck[str(2 + 13*i)] = Card("three") #Three
    deck[str(3 + 13*i)] = Card("four") #Four
    deck[str(4 + 13*i)] = Card("five") #Five
    deck[str(5 + 13*i)] = Card("six") #Six 
    deck[str(6 + 13*i)] = Card("seven") #Seven
    deck[str(7 + 13*i)] = Card("eight") #Eight
    deck[str(8 + 13*i)] = Card("nine") #Nine
    deck[str(9 + 13*i)] = Card("ten") #Ten
    deck[str(10 + 13*i)] = Card("jack") #Jack
    deck[str(11 + 13*i)] = Card("queen") #Queen
    deck[str(12 + 13*i)] = Card("king") #King

    
    

def main():
    card_1 = str(random.randint(0,51))
    card_2 = str(random.randint(1,51))
    while card_1 == card_2:
        card_2 = str(random.randint(1,51))
    value_1 = deck[card_1].value
    value_2 = deck[card_2].value
    value_sum = value_1 + value_2
    if value_sum == 22:
        value_sum = 12
    return(value_sum)

results = np.zeros(10000)
    
for i in range(10000):
    results[i] = main()

prob = np.ones_like(results)/float(len(results))

plt.figure("CSCI 127, Lab 13")
plt.hist(results, bins=np.arange(4,23), align="left", weights=prob)
plt.title("Histogram of BlackJack Hands")
plt.xticks(np.arange(4,22,1))
plt.xlabel("Hand Value")
plt.ylabel("Probability")
plt.grid()
plt.show()
    
    
