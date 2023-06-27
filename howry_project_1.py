"""
The program is a logic puzzle that generates a random three-digit number
and asks the user to guess the correct number using the hints provided.

File Name: howry_project_1.py
Author: Ken Howry
Date: 9.1.23
Course: COMP 1352
Assignment: Project I
Collaborators: N/A
Internet Source: Used for indentifying String Methods: "https://www.w3schools.com/python/python_ref_string.asp"
"""

import random

#making a list of numbers 0-9 & creating the unknown number
def creating_number(num) -> str:
    """
    Description of Function: This function generates the random three-digit number
    Parameters: num: str -- determines the length of the generated number
    Return: str
    """
    #creatinga randomly shuffled list
    numbers = []
    for i in range(10):
        numbers.append(i)
    random.shuffle(numbers)

    #creating unknown number
    unknown_number = ""
    for i in range(num):
        unknown_number += str(numbers[i])
    return unknown_number

def guesses(guess, generated_number) -> str:
    """
    Description of Function: Compares the user input to the actual generated number
    Parameters: guess: str -- the user input
                generated_number: str -- the genearated number
    Return: str
    """
    #if the guess is correct
    if guess == generated_number:
        return "Fermi! Fermi! Fermi!"
    
    hint = []

    #parameters for determing if the output is "Fermi", "Pico", or "Bagels"
    for i in range(len(guess)):
        if guess[i] == generated_number[i]:
            hint.append("Fermi!")
        elif guess[i] in generated_number:
            hint.append("Pico!")
    if len(hint) == 0:
        return "Bagels!"

    hint.sort()
    return ' '.join(hint)

def no_duplicates(checked_input) -> bool:
    """
    Description of Function: This function checks that the user input has no duplicate digits
    Parameters: checked_input: str -- the user input
    Return: bool
    """
    #checking for duplicates in the user input
    for i in range(len(checked_input)):
        count = 0
        for j in range(i+1, len(checked_input)):
            if checked_input[i] == checked_input[j]:
                return False

    return True

#explaining the game to the user
print("This is a number guessing game.")
print("I am thinking of a three-digit number that has no repeated digits.")
print("'Fermi!' is printed for each digit that is guessed correctly and in the right place.")
print("'Pico!' is printed for each digit that is guessed correctly but in the wrong place.")
print("'Bagels!' is printed if there are no correct digits.")
print()

#generating the number for the user to guess
number = creating_number(3)
print("I have thought of a number.")

quit = False
#variable for counting guesses
how_many_guesses = 0

#while loop that repeats until the userm has guessed correctly
while not quit:
    #asking the user for their guess and adding to the number of guesses
    user_guess = input("What is your guess?: ")
    how_many_guesses += 1

    #checking for no duplicates and printing the hints
    if no_duplicates(user_guess) == True:
        print(guesses(user_guess, number))
    #print "Invalid guess..." if the user input contains duplicate digits
    elif no_duplicates(user_guess) == False:
        print("Invalid guess - No duplicate digits")
    
    #response to the correct guess and printing the number of guesses it took
    if guesses(user_guess, number) == "Fermi! Fermi! Fermi!":
        print(f"You got the answer in {how_many_guesses}!")
        quit = True