# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Pokedex
# Anthony Louis Rosenblum
# Last Modified: 
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------
import string

def printMenu():
    print("1. Print Pokedex")
    print("2. Lookup Pokemon by Name")
    print("3. Lookup Pokemon by Number")
    print("4. Print Number of Pokemon")
    print("5. Print Total Hit Points of All Pokemon")
    print("6. Quit")
    print("")

def printPokedex(x):
    print("The Pokedex")
    for i in x:
        if len(x[i]) == 3:
            print("-----------")
            print("Number:" + str(i) +", Name: " + str(x[i][0])+ ", HP: " + str(x[i][1]) + ", Type: " + str(x[i][2]))
        
        elif len(x[i]) == 4:
            print("-----------")
            print("Number:" + str(i) +", Name: " + str(x[i][0])+ ", HP: " + str(x[i][1]) + ", Type: " + str(x[i][2] + " and " + str(x[i][3])))
    print("-----------")
    print("End Pokedex")
    print("")

    
name_list = []
def lookupByName(x,y):
    for i in x: 
        name_list.append(x[i][0])
        if x[i][0] == y:
            if len(x[i]) == 3:
                print("Number:" + str(i) +", Name: " + str(x[i][0])+ ", HP: " + str(x[i][1]) + ", Type: " + str(x[i][2]))
            elif len(x[i]) == 4:
                print("Number:" + str(i) +", Name: " + str(x[i][0])+ ", HP: " + str(x[i][1]) + ", Type: " + str(x[i][2] + " and " + str(x[i][3])))
    if y not in name_list:
        print("The pokemon named " + str(y) + " does not exist")
    print("")

            

def lookupByNumber(x,y):
    for i in x:
        if (i) == y:
            if len(x[i]) == 3:
                print("Number:" + str(i) +", Name: " + str(x[i][0])+ ", HP: " + str(x[i][1]) + ", Type: " + str(x[i][2]))
            elif len(x[i]) == 4:
                print("Number:" + str(i) +", Name: " + str(x[i][0])+ ", HP: " + str(x[i][1]) + ", Type: " + str(x[i][2] + " and " + str(x[i][3])))
    if y > len(x):
        print("Error: Pokemon number " + str(y) + " does not exist")
    elif y < 1:
        print("Error: Pokemon number " + str(y) + " does not exist")
    print("")

def howManyPokemon(x):
    z = 0
    for i in x:
        z = z + 1
    w = str(z)
    print("There are " + w + " different Pokemon")
    print("")
    

def howManyHitPoints(x):
    z = 0
    for i in x:
        z = z + x[i][1]
    w = str(z)
    print("The total number of hit points for all Pokemon is " + w)
    print("")

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def createPokedex(filename):
    pokedex = {}
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        pokedex[index] = [pokelist.pop(0)]          # name
        pokedex[index] += [int(pokelist.pop(0))]    # hit points
        pokedex[index] += [pokelist.pop(0)]         # type
        if len(pokelist) == 1:
            pokedex[index] += [pokelist.pop(0)]     # optional second type

    file.close()
    return pokedex

# ---------------------------------------

def getChoice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = createPokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        printMenu()
        choice = getChoice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            printPokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ")
            name = name.capitalize()
            lookupByName(pokedex, name)
        elif choice == 3:
            number = getChoice(1, 1000, "Enter a Pokemon number: ")
            lookupByNumber(pokedex, number)
        elif choice == 4:
            howManyPokemon(pokedex)
        elif choice == 5:
            howManyHitPoints(pokedex)
    print("Thank you.  Goodbye!")

# ---------------------------------------

main()
