# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Anthony Louis Rosenblum
# Last Modified: September 8, 2017 
# ---------------------------------------
# This program calculates a user's college GPA based on Montana State University's grading system.
# It prompts the user to input the number of classes they are taking, their marks in each class, and how many credits each class is worth.
# ---------------------------------------

total_credit = 0
dot_sum = 0
    

while True:
    try:
        num = int(input("Please enter the number of classes you are taking: "))
    except ValueError:
        print("Please enter an integer.")
    else:
        break
        

while num < 1:
    print("You must be taking at least one class.")
    num = int(input("Please enter the number of classes you are taking: "))

    
while num > 7:
    print("You are not allowed to take more than seven classes.")
    num = int(input("Please enter the number of classes you are taking: "))

def translate(x):
    if x == "A":
        z = 4.0
        return z
    if x == "a":
        z = 4.0
        return z
    if x == "A-":
        z = 3.7
        return z
    if x == "a-":
        z = 3.7
        return z
    if x == "B+":
        z = 3.3
        return z
    if x == "b+":
        z = 3.3
        return z
    if x == "B":
        z = 3.0
        return z
    if x == "b":
        z = 3.0
        return z
    if x == "B-":
        z = 2.7
        return z
    if x == "b-":
        z = 2.7
        return z
    if x == "C+":
        z = 2.3
        return z
    if x == "c+":
        z = 2.3
        return z
    if x == "C":
        z = 2.0
        return z
    if x == "c":
        z = 2.0
        return z
    if x == "C-":
        z = 1.7
        return z
    if x == "c-":
        z = 1.7
        return z
    if x == "D+":
        z = 1.3
        return z
    if x == "d+":
        z = 1.3
        return z
    if x == "D":
        z = 1.0
        return z
    if x == "d":
        z = 1.0
        return z
    if x == "F":
        z = 0.0
        return z
    if x == "f":
        z = 0.0
        return z
    
for i in range(num):
    grade = translate(input("Please enter the letter grade you earned for class #" + str(i+1)+ ": "))
    credit = int((input("Please enter the credit value of class #" + str(i+1)+ ": ")))
    total_credit = total_credit + credit
    dot_product = grade * credit
    dot_sum = dot_sum + dot_product


print("Your GPA is: " + str(round(dot_sum/total_credit, 2)))



                                     



    
