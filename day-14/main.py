import art as A
import game_data as G
import random as R
import os

def runGame():
    score = 0
    result = ""
    dataCopy = G.data[:]
    indexA = R.randint(0,len(dataCopy)-1)
    itemA = dataCopy.pop(indexA)
    indexB = R.randint(0,len(dataCopy)-1)
    itemB = dataCopy.pop(indexB)

    while True:
        answer = "A" if itemA['follower_count'] > itemB['follower_count']  else "B"
        print(A.logo)
        print(f"\n\nCompare A: {itemA['name']}, {itemA['description']}, from {itemA['country']}\n\n")
        print(A.vs)
        print(f"\n\nAgainst B: {itemB['name']}, {itemB['description']}, from {itemB['country']}\n\n")
        # print(f"The answer is {answer}.\n{itemA['name']}: {itemA['follower_count']} vs {itemB['name']}: {itemB['follower_count']}")

        userInput = input("Who has more followers? Type 'A' or 'B': ")
        
        # captures wrong entries
        if userInput.isalpha():
            if userInput.upper() != "A" and userInput.upper() != "B":
                result = "wrong"
            else:
                # compares against correct answer only if the input is valid
                if userInput.upper() == answer:
                    result = "right"
                    score += 1
                    print(f"You're {result}. Score: {score}")
                    # break
                else:
                    result = "wrong"
        else:
            result = "wrong"

        # catch-all wrong inputs
        if result == "wrong":
            print(f"Sorry, that's {result}. Final score: {score}")
            break

        # if A was higher, retain it. Otherwise, set A to B then generate a new itemB
        if answer == "B":
            itemA = itemB
        indexB = R.randint(0,len(dataCopy)-1)
        itemB = dataCopy.pop(indexB)

        os.system("cls")
        

if __name__ == "__main__":
    try:
        runGame()
    except KeyboardInterrupt:
        print("\n\nProgram was interrupted.")
    except Exception as e:
        print(e)