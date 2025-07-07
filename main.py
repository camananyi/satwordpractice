import pandas as pd
import matplotlib.pyplot as plt
import math
import random

# Read a CSV file
df = pd.read_csv('words.csv')

# print(df.describe)
# print(df.head)

# Learn function
def learn(word):
    print("Your word to learn:")
    for col_name, value in word.items():
        if col_name == "date" :
            continue
        else:
            print(f"{col_name}: {value}")

# Handles the user input
def newWord():
    user_input = input("Do you want the next word? ").lower()
    if user_input == "yes":
        random_index = random.randint(0, len(df) - 1)
        learn(df.loc[random_index])
        return True
    elif user_input == "no":
        print("Okay, stopping now.")
        return False
    else:
        print("Only 'yes' or 'no'.")
        return True  

learnPractice = input("Do you want to learn or practice today? ")
if learnPractice == "learn":
    # learn loop loop
    lalive = True
    while lalive:
        lalive = newWord()
