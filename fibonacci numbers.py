z = [0,1]

for i in range(200): 
    z.append(z[i] + z[i+1])

print(z)
