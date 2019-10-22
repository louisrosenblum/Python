

def translate(x):
    if x == "A":
        z = 4.0
        return z
    if x == "a":
        z = 4.0
        return z
    if x == "A-":
        z = 3.7
        return z
    if x == "a-":
        z = 3.7
        return z
    if x == "B+":
        z = 3.3
        return z
    if x == "b+":
        z = 3.3
        return z
    if x == "B":
        z = 3.0
        return z
    if x == "b":
        z = 3.0
        return z
    if x == "B-":
        z = 2.7
        return z
    if x == "b-":
        z = 2.7
        return z
    if x == "C+":
        z = 2.3
        return z
    if x == "c+":
        z = 2.3
        return z
    if x == "C":
        z = 2.0
        return z
    if x == "c":
        z = 2.0
        return z
    if x == "C-":
        z = 1.7
        return z
    if x == "c-":
        z = 1.7
        return z
    if x == "D+":
        z = 1.3
        return z
    if x == "d+":
        z = 1.3
        return z
    if x == "D":
        z = 1.0
        return z
    if x == "d":
        z = 1.0
        return z
    if x == "F":
        z = 0.0
        return z
    if x == "f":
        z = 0.0
        return z


result = translate(input("Please enter a letter: "))
print(result)
        
