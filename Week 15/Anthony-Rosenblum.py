# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 6: Emergency Data
# Anthony Louis Rosenblum
# Last Modified: December 8, 2017 
# ---------------------------------------
# This program creates two matplotlib graphs from a DataFrame generated from a .csv file on Montana State University Emergency and Disaster Information.
# 
# ---------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

info = pd.read_csv("buildings.csv") # Read CSV file 

df = pd.DataFrame(data = info) # Convert to DataFrame object

n = 0
y = 0

for i in df["Historic Building"]: # Count Ys and Ns in DataFrame
    if i == "N":
        n = n + 1
    elif i=="Y":
        y = y + 1
        
total = n + y

n = n/total * 100 # Calculate percentages for pie chart
y = y/total * 100

labels = ("Historic Buildings", "Non-Historic Buildings")


plt.figure("Building Construction-Date Distribution") # Generate Histogram from Dataframe
plt.title("Building Construction-Date Distribution")
plt.hist(df["Year Built"], bins=np.arange(1900,2030,10))
plt.xticks(np.arange(1900, 2020, 10))
plt.xlabel("Decade")
plt.ylabel("Count")



plt.figure("Historic Building Prevelance") # Generate pie chart from calculations off Dataframe
plt.title("Historic Building Prevelance")
plt.pie([n,y], labels=labels, autopct="%1.00f%%")
plt.show()
