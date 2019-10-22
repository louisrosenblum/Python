
sat = 0
sun = 1
mon = 2
tue = 3
wed = 4
thu = 5
fri = 6

m = 0

for i in range(50):
    if i%4 == 0:
        m = m + 366%7

    else:
        m = m + 365%7

m = m%7

print(m)
        
        
