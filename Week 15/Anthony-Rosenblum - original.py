import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

info = pd.read_csv("buildings.csv")

df = pd.DataFrame(data = info)

n = 0
y = 0

for i in df["Historic Building"]:
    if i == "N":
        n = n + 1
    elif i=="Y":
        y = y + 1
        
total = n + y

n = n/total * 100
y = y/total * 100

labels = ("Historic Buildings", "Non-Historic Buildings")


plt.figure("Building Construction-Date Distribution")
plt.title
plt.hist(df["Year Built"], bins=np.arange(1900,2030,10))
plt.xticks(np.arange(1900, 2020, 10))
plt.xlabel("Decade")
plt.ylabel("Count")



plt.figure("Historic Building Prevelance")
plt.title
plt.pie([n,y], labels=labels)
plt.show()
