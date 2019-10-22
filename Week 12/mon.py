import numpy as np
import random

x = []
for i in range(10):
    v = random.randint(1,100)
    x.append(v)
    
y = np.array(x)
print(y)

z = []
for i in range(5):
    z.append(y[2*i + 1])

w = np.array(z)
print(w)

a = []
for i in range(10):
    a.append(y[9-i])

k = np.array(a)
print(k)

x = []
for i in range(5):
    z = []
    for i in range(5):
        z.append(random.randint(1,100))
    x.append(z)

p = np.array(x)
print(p)
        
    
