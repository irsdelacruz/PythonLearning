# 100 days of code project
import random as R
import os

def startGame():
    welcomeText = """
    
 /$$   /$$ /$$           /$$                                 /$$                                                  
| $$  | $$|__/          | $$                                | $$                                                  
| $$  | $$ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$       | $$        /$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$ 
| $$$$$$$$| $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$      | $$       /$$__  $$| $$ | $$ | $$ /$$__  $$ /$$__  $$
| $$__  $$| $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/      | $$      | $$  \ $$| $$ | $$ | $$| $$$$$$$$| $$  \__/
| $$  | $$| $$| $$  | $$| $$  | $$| $$_____/| $$            | $$      | $$  | $$| $$ | $$ | $$| $$_____/| $$      
| $$  | $$| $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$            | $$$$$$$$|  $$$$$$/|  $$$$$/$$$$/|  $$$$$$$| $$      
|__/  |__/|__/ \____  $$|__/  |__/ \_______/|__/            |________/ \______/  \_____/\___/  \_______/|__/      
               /$$  \ $$                                                                                          
              |  $$$$$$/                                                                                          
               \______/                                                                                           
"""
    print(welcomeText)
    print("Try to guess the number I have in mind before you run out of lives!")
    gameMode = input("Choose which mode: 'easy' or 'hard'\n")
    livesCount = 10 if gameMode == 'easy' else 5
    secretNumber = R.randint(1,100)
    numberGuessed = False
    print("I am thinking of an integer from 1 to 100.")
    while numberGuessed == False:
        print(f"You have {livesCount} guesses left.")
        # print(f". number = {secretNumber}\n")
        playerGuess = input("What do you think is it? ")
        while not(playerGuess.isnumeric()):
                playerGuess = input("Please enter an integer: ")
        playerGuess = int(playerGuess)
        if playerGuess == secretNumber:
            numberGuessed = True
            print(f"That's right! The number was {secretNumber}.")
        else:
            hint = "high" if playerGuess > secretNumber else "low"
            print(f"Your guess was too {hint}. Try again.")
            livesCount -= 1
            if livesCount == 0:
                print(f"Oops, you've ran out of guesses! The number was {secretNumber}.")
                break
    return

if __name__ == "__main__":
    try:
        while True:
            os.system("cls")
            startGame()
            repeat = input("Would you like to play again? Type 'y' or 'n'\n").lower()
            if repeat == 'n':
                break
        print("See you next time!")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. See you next time!")