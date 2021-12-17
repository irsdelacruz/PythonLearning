def run():
    cmaker = CoffeeMaker()
    mmachine = MoneyMachine()
    mainMenu = Menu()
    print(banner,emoji)
    poweredOn = True
    while poweredOn:
        choice = input(f"What would you like? ({mainMenu.get_items()}) ")
        if choice == "off":
            poweredOn = False
        elif choice == "report":
            cmaker.report()
            mmachine.report()
        else:
            order = mainMenu.find_drink(choice)
            if order:
                if cmaker.is_resource_sufficient(order):
                    paymentSufficient = mmachine.make_payment(order.cost)
                    if paymentSufficient:
                        cmaker.make_coffee(order)

if __name__ == "__main__":
    try:
        from menu import Menu, MenuItem
        from coffee_maker import CoffeeMaker
        from money_machine import MoneyMachine
        from day_14 import banner, emoji
        run()
    except KeyboardInterrupt:
        print("Program interrupted.")
    except Exception as e:
        print(e)

# mainMenu = Menu()
# machine = CoffeeMaker()
# choice = "latte"
# order = mainMenu.find_drink(choice) 
# orderCost = order.cost
# orderIngredients = order.ingredients 
# # print(f"The cost of {c}")
# machine.report()
# machine.make_coffee(order)
# machine.report()
# machine.make_coffee(mainMenu.find_drink("espresso"))
# machine.report()
# machine.make_coffee(mainMenu.find_drink("espresso"))
# machine.report()
# print(machine.is_resource_sufficient(order))