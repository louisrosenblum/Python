sentence = input(": ")

x = 6
z = 5

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



print(count_vowels_recursive(sentence))

