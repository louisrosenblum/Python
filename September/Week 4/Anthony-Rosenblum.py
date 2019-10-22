# --------------------------------------
# CSCI 127, Lab 3
# September 19, 2017
# Your Name
# --------------------------------------

z = 0

def count_vowels(sentence):
    a = sentence.count("a")
    e = sentence.count("e")
    i = sentence.count("i")
    o = sentence.count("o")
    u = sentence.count("u")
    return (a+e+i+o+u)
       
        

def count_vowels_iterative(sentence):
    a_ = 0
    e_ = 0
    i_ = 0
    o_ = 0
    u_ = 0
    for i in range(len(sentence)):
        if "a" == sentence[i]:
            a_ = a_ + 1
        elif "e" == sentence[i]:
            e_ = e_ + 1
        elif "i" == sentence[i]:
            i_ = i_ + 1
        elif "o" == sentence[i]:
            o_ = o_ + 1
        elif "u" == sentence[i]:
            u_ = u_ + 1
        else:
            continue
    return (a_ + e_ + i_ + o_ + u_)
        

def count_vowels_recursive(sentence):
    the_sum = 0
    if sentence == "":
        return the_sum
    elif sentence[0] == "a":
        the_sum = the_sum + 1 + count_vowels_recursive(sentence[1:])
    elif sentence[0] == "e":
        the_sum = the_sum + 1 + count_vowels_recursive(sentence[1:])
    elif sentence[0] == "i":
        the_sum = the_sum + 1 + count_vowels_recursive(sentence[1:])
    elif sentence[0] == "o":
        the_sum = the_sum + 1 + count_vowels_recursive(sentence[1:])
    elif sentence[0] == "u":
        the_sum = the_sum + 1 + count_vowels_recursive(sentence[1:])
    else:
        the_sum = the_sum + count_vowels_recursive(sentence[1:])   
    return the_sum

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence to evaluate: ")
        sentence = sentence.lower()     # convert to lowercase
        print()
        print("Number of vowels using count     =", count_vowels(sentence))
        print("Number of vowels using iteration =", count_vowels_iterative(sentence))
        print("Number of vowels using recursion =", count_vowels_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
