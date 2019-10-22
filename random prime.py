import random



## To create a prime number of a certain length, replace the "1" with a minimum number number

for i in range(100):
    x = random.randint(1000000,1000000000)
    z = 0
    for w in range(2,x):
        if x%w == 0 and w != x:
            z = z + 1
    if z < 1:
        print(x)
       



print("Done!")
