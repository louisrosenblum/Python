import math

for i in range(712945618142, 712945619142):
    z = 0
    while z == 0:
        for w in range(2,int((math.sqrt(i)) + 1)):
            if i%w == 0 and w != i:
                z = 1
        if z == 0:
            print(i)
            z = 1
            
       

        
    

print("Done!")
