"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import sys

def intialize_variables():
    random_number = random.randint(1,10)
    return random_number
    
def start_game():
    
    highscore = sys.maxsize
    attempts = 0
    random_number = intialize_variables() 
    print(random_number)
    answer = True
    while answer:
          
        try:
        
            number_guessed = input("Pick a number between 1 and 10:  ")
            number_guessed = int(number_guessed)
            if number_guessed > 10:
                print("Invalid. Try a number less than 10")
            elif number_guessed > random_number:
                print("Try a lower number")
                attempts += 1
                continue
            elif number_guessed < random_number:
                print("Try a higher number")
                attempts += 1
                continue
            elif number_guessed == random_number:
                print("CORRECT!! You Got it")
                attempts += 1
                print("It took you {} attempts to guess".format(attempts))
                highscore = min(highscore,attempts)
                print("Your score: {}".format(attempts))
                answer = replay_game(highscore)
                if answer:
                    attempts = 0
                    random_number = intialize_variables()
                    print(random_number)
        
        except ValueError:
            
            print("Invalid input..Please enter an integer")
            continue
            
def replay_game(highscore):
    
    replay_game_choices = ["y", "n"]
    continue_game = None
    
    while continue_game not in replay_game_choices:
    
        continue_game = input("Would you like to play again? [y]es or [n]o: ")
         
        if continue_game == "y":
            print("The minimum attempts taken to guess so far is: {} ".format(highscore))
            return True       
        
        elif continue_game == "n":
            print("---------------------")
            print("Thank you for playing")
            print("---------------------")
            return False
            
        else:
            print("Invalid input.")
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    try:
        print("------------------------------------")
        print("Welcome to the number guessing game!")
        print("------------------------------------")
        start_game()
    except KeyboardInterrupt:
        print(" \nOOPS..The game ended unfortunately")
