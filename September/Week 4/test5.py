def fuckyou(x):
    total = 0
    if x[0] == "1":
        total = total + 1 + fuckyou(x[1:])
    else:
        total = total + fuckyou(x[1:])
    return total

print(fuckyou(105010501))
