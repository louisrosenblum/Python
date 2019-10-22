import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# CSCI 127, Lab 12
# November 21, 2017
# Anthony Rosenblum
# -----------------------------------------------------

def read_file(name):
    input_file = open(name, "r")
    number_buckets = int(input_file.readline())
    total_counties = int(input_file.readline())

    county_populations = np.zeros([total_counties], dtype="int")
    for county_number in range(total_counties):
        line = input_file.readline().split(",")
        county_populations[county_number] = int(line[1])
    county_populations.sort()
    input_file.close()
    return number_buckets, county_populations
    

# -----------------------------------------------------

def print_summary(averages):
    print("Population Grouping Summary")
    print("---------------------------")
    for grouping in range(len(averages)):
        print("Grouping", grouping + 1, "has a population average of",
              averages[grouping])

# -----------------------------------------------------
# Do not change anything above this line
# -----------------------------------------------------

def calculate_averages(number_buckets, county_populations):
    averages = np.zeros(number_buckets, dtype="int")
    for i in range(number_buckets):
        for w in range(int((len(county_populations)/number_buckets))):
            averages[i] += county_populations[(int((len(county_populations)/number_buckets)) * (i)) + w]
    averages = averages * number_buckets/len(county_populations)
    new_array = np.zeros(number_buckets, dtype = "int32")
    for i in range(len(averages)): 
        new_array[i] = int((averages[i]))
    return new_array
            
        

# -----------------------------------------------------

def graph_summary(averages):
    plt.figure("CSCI 127, Lab 12")
    plt.xlim(1, int(len(averages)))
    plt.xticks(np.arange(1, len(averages) + 1, 1.0))
    plt.ylim(0, averages[(len(averages)-1)] + 10000)
    x = np.zeros(len(averages), dtype="int")
    plt.xlabel("County Groupings")
    plt.ylabel("County Population Average")
    plt.title("Montana County Population Analysis")
    for i in range(len(averages)):
        x[i] = (i+1)
    plt.plot(x,averages, "bh",x,averages, "c--")
    plt.show()
    
                                 

# -----------------------------------------------------

number_buckets, county_populations = read_file("montana-counties.txt")
averages = calculate_averages(number_buckets, county_populations)
print_summary(averages)
graph_summary(averages)
