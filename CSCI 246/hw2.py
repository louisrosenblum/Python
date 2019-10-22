m = 0

for i in range(12):
    for k in range(30):
        m = (i * 0.25) + (0.1 * (k)) + (0.01 * (50 - i - (k)))
        if m >= 2.95 and m <=3.05:
            print("q" + str(i))
            print("p" + str((50 - i - (k))))
            print("d" + str((k)))
            print(m)
            print()
    
    
