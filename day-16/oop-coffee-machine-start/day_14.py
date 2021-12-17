"""
    2021-12-17 2:35AM
        I'm having issues with updating the money variable for every transaction.
"""
emoji = r"""    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/
"""
banner = """
    __   ___   _____  _____    ___    ___      ___ ___   ____     __  __ __  ____  ____     ___ 
   /  ] /   \ |     ||     |  /  _]  /  _]    |   |   | /    |   /  ]|  |  ||    ||    \   /  _]
  /  / |     ||   __||   __| /  [_  /  [_     | _   _ ||  o  |  /  / |  |  | |  | |  _  | /  [_ 
 /  /  |  O  ||  |_  |  |_  |    _]|    _]    |  \_/  ||     | /  /  |  _  | |  | |  |  ||    _]
/   \_ |     ||   _] |   _] |   [_ |   [_     |   |   ||  _  |/   \_ |  |  | |  | |  |  ||   [_ 
\     ||     ||  |   |  |   |     ||     |    |   |   ||  |  |\     ||  |  | |  | |  |  ||     |
 \____| \___/ |__|   |__|   |_____||_____|    |___|___||__|__| \____||__|__||____||__|__||_____|
                                                                                                
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def takeOrder(coffeeType):
    """
    coffeType here is either "espresso", "latte", or "cappuccino"
    Asks for coin inputs (penny 0.01, nickel 0.05, dime 0.1, quarter 0.25)
    If the money is enough, computes for the change, updates the money supply, and deducts from the resources.
    Otherwise, it should refund the whole amount.
    Returns the True if the money is enough, False otherwise.
    """
    print("Please insert coins.")
    pennies = int(input("How many pennies? "))
    nickels = int(input("How many nickels? "))
    dimes = int(input("How many dimes? "))
    quarters = int(input("How many quarters? "))
    totalInput = 0.01*pennies + 0.05*nickels + 0.1*dimes + 0.25*quarters
    change = totalInput - MENU[coffeeType]["cost"]
    change = round(change,2)
    moneyEnough = True if change >= 0 else False

    if moneyEnough:
        for ingredient, amountNeeded in MENU[coffeeType]["ingredients"].items():
            resources[ingredient] = resources[ingredient] - amountNeeded
        global money
        money += MENU[coffeeType]["cost"]
        print(f"\nHere's your {coffeeType}. Enjoy!")
        print(f"Here is your ${change} in change.")
    else:
        print("Sorry that's not enough money. Money Refunded")
    return moneyEnough

def enoughResources(coffeeType):
    """
    coffeType here is either "espresso", "latte", or "cappuccino"
    This function will check the resources available.
    """
    enough = True
    for ingredient, amountNeeded in MENU[coffeeType]["ingredients"].items():
        if resources[ingredient] < amountNeeded:
            enough = False
            print(f"Sorry, there is not enough {ingredient}.")

    return enough

def processCommand(userInput):
    commands = ("report",["espresso","latte","cappuccino"])
    if any(userInput in i for i in commands):
        if userInput == "report":
            for item, supply in resources.items():
                print(f"{item}: {supply}")
            print(f"money: ${money}")
        else:
            if enoughResources(userInput):
                takeOrder(userInput)
    else:
        print(f"I don't know what you mean by \"{userInput}\". Please try again.")
    return

def run():
    poweredOn = True
    print(banner,emoji)
    while poweredOn:
        userCommand = input("\nWhat would you like? (espresso/latte/cappuccino): ")
        if userCommand == "off":
            print("\nCome again next time!")
            poweredOn = False
        else:
            processCommand(userCommand)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("Program interrupted.")
    except Exception as e:
        print(e)