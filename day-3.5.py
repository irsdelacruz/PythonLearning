# Love Calculator

print("Welcome to the Love Calculator")
name1 = input("What is your name?\n").upper()
name2 = input("What is their name?\n").upper()
combined = name1+name2

comp = ("TRUE","LOVE")
score = ''
for word in comp:
    tmpscore = 0
    for char in word:
        tmpscore += combined.count(char)
    score += str(tmpscore)

score = int(score)
dispResult = f"Your score is {score}"

if score < 10 or score > 90:
    dispResult += ", you go together like coke and mentos."
elif score > 40 and score < 50:
    dispResult += ", you are alright together."
else:
    dispResult += "."

print(dispResult)