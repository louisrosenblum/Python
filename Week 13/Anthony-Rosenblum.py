file = open("batting.txt", "r")

import numpy as np

class Person:
    def __init__(self,first,last):
        self.first_name = first
        self.last_name = last

    def get_first(self):
        return self.first_name
    def get_last(self):
        return self.last_name

class Batter(Person):
    def __init__(self, first, last, position):
        Person.__init__(self,first,last)
        self.position = position
        self.at_bats = 0
        self.hits = 0
        self.avg = str("0.000")

    def get_position(self):
        return self.position
    def set_at_bats(self, x):
        self.at_bats = self.at_bats + int(x)
    def set_hits(self, x):
        self.hits = self.hits + int(x)
    def set_avg(self):
        self.avg = round((self.hits)/(self.at_bats),3)

    def __str__(self):
        p = str(self.first_name) + " " + str(self.last_name) +"(" + str(self.position) + ") "
        return str(p.ljust(25) + str(self.avg) + " (" + str(self.hits) + " for " + str(self.at_bats) + ")")

class All_Batters:
    def __init__(self, names):
        self.batters = np.array(names)


w = []
players = {}
for i in file:
    z = i.split(",")
    z[len(z)-1] = z[len(z)-1].replace("\n","")
    w.append(z)

num = int(w[0][0])

for i in range(num):
    players[str(w[i+1][1])] = Batter(str(w[i+1][0]),str(w[i+1][1]),str(w[i+1][2]))

row_1 = list(players.keys())

final = All_Batters(row_1)

def print_players(x):
    if x == 0:
        a = "Player"
        b = "Batting Average"
        c = a.ljust(25) + b
        print(c)
        print("----------------------------------------")
        for i in final.batters:
            print(players[i])
        print("")
    if x != 0:
        a = "Player"
        b = "Batting Average"
        c = a.ljust(25) + b
        print(c)
        print("----------------------------------------")
        for i in final.batters:
            players[i].set_avg()
            print(players[i])
        print("")

print_players(0)

for i in range(len(w) - num -1):
    if w[i+num+1][1] in players:
        players[w[i+num+1][1]].set_at_bats(w[i+num+1][3])
        players[w[i+num+1][1]].set_hits(w[i+num+1][4])
##    print(w[i+num+1])

print_players(1)


    
