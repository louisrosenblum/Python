import numpy as np
import random
import math

roll = random.randint(1, 6)
rolls = np.zeros(5, dtype=np.int16)

for x in range(1000):
    for i in range(len(rolls)):
        rolls[i] = random.randint(1, 6)
    if (sum(rolls) >= 7 and sum(rolls) <= 28 and sum(rolls) != 10) and (rolls[0] == rolls[1] or rolls[0] == rolls[2] or rolls[0] == rolls[3] or rolls[0] == rolls[4]) and (rolls[1] == rolls[0] or rolls[1] == rolls[2] or rolls[1] == rolls[3] or rolls[1] == rolls[4]) and (rolls[2] == rolls[0] or rolls[2] == rolls[1] or rolls[2] == rolls[3] or rolls[2] == rolls[4]) and (rolls[3] == rolls[0] or rolls[3] == rolls[1] or rolls[3] == rolls[2] or rolls[3] == rolls[4]) and (rolls[4] == rolls[0] or rolls[4] == rolls[1] or rolls[4] == rolls[2] or rolls[4] == rolls[3]):
        print(rolls)
        print(sum(rolls))
    


