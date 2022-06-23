from menu import MENU, profit, resources



#TODO: 4. Check sufficient Resources

#TODO: 1. Prompt User Question
#TODO: 2. Enter while loop to turn on and off machine
#TODO: 3. Print Report

coffee_machine_on = True

while coffee_machine_on:
    user_coffee_selection = input("What type of coffee would you like? (espresso | latte | cappuccino): ").lower()
    if user_coffee_selection == "off":
        coffee_machine_on = False
    elif user_coffee_selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"money ${profit}")
    else:
        drink = MENU[user_coffee_selection]



#TODO: 5. Process Coins

def __process_coins__():
    """Returns total calculated from coins inserted"""
    print("Please insert coins\n")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickel = int(input("How many nickels? ")) * 0.05
    total = (quarters, dimes, nickel)
    return total


#TODO: 6. Check if Transaction was Successful

#TODO: 7. Make Coffee for the Customer