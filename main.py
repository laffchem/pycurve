from progress1bar import ProgressBar
import pandas as pd
import time
import math
import os
from art import art
from instructions import instructions

program_running = True


# Function to clear the console
def clear():
    if os.name == 'nt':
        clear_screen = os.system('cls')
    else:
        clear_screen = os.system('clear')
    return clear_screen

# Instructions & Input method
def program():
    print(art)
    print(instructions)    

    # Collects all the input information
    input_path = input("Provide the input file name. Ensure it is in the 'files' folder.\
 The .csv is already added, just type the name.\n")
    output_path = input("Provide the output filename --> example: 'per6'\
 The .csv is already added, just type the name.\n")
    column_name = input("Provide the csv column name exactly\n")
    method = input("Choose '1' for square root curve, '2' for max score curve, or '3' for a 10 point bump.\n")

    # Dataframe import from csv
    grades = pd.read_csv(f"files/{input_path}.csv")
    orig = grades[column_name]
    new_grades = []

    # Sqrt Curve
    def square_curve():
        for grade in orig:
            new_grade = round(math.sqrt(grade) * 10, 2)
            new_grades.append(new_grade)


    highest = max(orig)

    # Determines the amount to add to all scores
    def modifier(grade):
        if grade >= 90 and grade <= 100:
            curved_mod = (100 - grade)
        elif grade >= 80 and grade < 90:
            curved_mod = (90 - grade)
        elif grade >= 70 and grade < 80:
            curved_mod = (80 - grade)
        elif grade >= 60 and grade < 70:
            curved_mod = (70 - grade)
        else:
            curved_mod = (60 - grade)
        return curved_mod


    # Adds the modifier to the original score
    def max_curve(curved_mod):
        for grade in orig:
            curved_grade = (grade + curved_mod)
            new_grades.append(curved_grade)


    # 10 point curve function
    def ten_point():
        for grade in orig:
            curved_grade = (grade + 10)
            new_grades.append(curved_grade)


    # Gets user input to curve the grades
    if method == "1":
        square_curve()
    elif method == "2":
        max_curve(modifier(highest))
    elif method == "3":
        ten_point()
    else:
        print("Error! Incorrect Input ---> Rerun the program")
        clear            
        quit()
    clear

# Progress bar because why the hell not!
    with ProgressBar() as pb:
        pb.total = len(orig)
        for _ in range(pb.total):
            #simulates calculations and stuff
            pb.count +=1
            time.sleep(0.09)

    grades['curved'] = new_grades

    grades.to_csv(f"curved_grades/{output_path}.csv")

# The function to check if user would like to go again.
def go_again():
    curve_again = input("Would you like to do another exam? Type 'y' or 'n'.\n").lower()
    return curve_again


# Running the actual program
program()

while program_running:
    try_again = go_again()
    if try_again == "y":
        clear()
        program()
    elif try_again == "n":
        clear()
        print("Thank you for using pycurve!")
        program_running = False





        

  

    