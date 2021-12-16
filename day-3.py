print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, L\n").upper()
add_pepperoni = input("Do you want pepperoni? Y, N\n").upper()
extra_cheese = input("Do you want extra cheese? Y, N\n").upper()
total = 0
# print(size,add_pepperoni,extra_cheese)
if size == "S":
    total += 15
elif size == "M":
    total += 20
else:
    total += 25

if add_pepperoni == "Y":
    total += 2
    if size != "S":
        total += 1

if extra_cheese == "Y":
    total += 1

print(f"Your total bill is ${total}.")