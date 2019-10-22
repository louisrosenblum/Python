w = ""

txt = open("poker.in.txt", "r")

def flush(z):
    if z[0][1] == z[1][1] and z[1][1] == z[2][1]:
        return True
    else:
        return False

def three_of_a_kind(z):
    if z[0][0] == z[1][0] and z[1][0] == z[2][0]:
        return True
    else:
        return False

def two_of_a_kind(z):
    if z[0][0] == z[1][0] and z[1][0] != z[2][0]:
        return True
    elif z[1][0] == z[2][0] and z[0][0] != z[1][0]:
        return True
    elif z[0][0] == z[2][0] and z[0][0] != z[1][0]:
        return True
    else:
        return False

def nothing(z):
    if z[0][0] != z[1][0] and z[1][0] != z[2][0] and z[0][0] != z[2][0] and z[0][1] != z[1][1] and z[1][1] != z[2][1] and z[0][0] != z[2][0]:
        return True
    else:
        return False

def print_hand(x,y):
    output_file = open(y, "w")
    print("Poker Hand")
    print("----------")
    print("Card 1: " + str(x[0][0]).title() + " of " + str(x[0][1]).title())
    print("Card 2: "+ str(x[1][0].title()) + " of " + str(x[1][1]).title())
    print("Card 3: "+ str(x[2][0].title()) + " of " + str(x[2][1]).title())
    print("")

def evaluate(x,y):
    output_file = open(y, "w")
    if flush(x) == True:
        w = "FLUSH"
    else:
        pass
    if three_of_a_kind(x) == True:
        w = "THREE OF A KIND"
    else:
        pass
    if two_of_a_kind(x) == True:
        w = "TWO OF A KIND"
    else:
        pass
    if nothing(x) == True:
        w = "NOTHING"
    else:
        pass
    print("Poker Hand Evaluation: " + str(w))
    print("")


          
## --------------------------------------
## Do not change anything below this line
## --------------------------------------

def main(input_file, output_file, cards_in_hand):    
    poker_input = open(input_file, "r")

    for hand in poker_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0], hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list, output_file)
        evaluate(hand_as_list, output_file)

# --------------------------------------

main("poker.in.txt", "poker.out", 3)
