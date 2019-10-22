x = "abba"

def count_vowels_recursive(x):
    x = "abba"
    the_sum = 0
    if x[0] == "a":
        the_sum = the_sum + 1 + count_vowels_recursive(x[1:])
    return the_sum

print(count_vowels_recursive(x))






