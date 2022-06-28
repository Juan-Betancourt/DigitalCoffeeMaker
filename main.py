from menu import MENU, resources

profit = 0


def __sufficient_coffee_resources__(order_ingredients):
    """Returns True when order can be made, False if there are insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def __process_coins__():
    """Returns total calculated from coins inserted"""
    print("\nThe cost of special brewed coffee\nEspresso $1.50 | Latte $2.50 | Cappuccino $3.00")
    print("\nPlease insert coins")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    total = quarters + dimes + nickels
    return total


def __check_successful_transaction__(money_dispense, drink_price):
    """Return True if payment is accepted, or False if there are insufficient funds"""
    if money_dispense >= drink_price:
        change = round(money_dispense - drink_price, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_price
        return True
    else:
        print(f"Sorry, those were insufficient funds. Money refunded")
        return False


def __make_coffee__(drink_name, order_ingredients):
    """Deduct the required ingredients from the available resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


coffee_machine_on = True

while coffee_machine_on:
    user_coffee_selection = input("What type of coffee would you like? (Espresso | Latte | Cappuccino): ").lower()
    if user_coffee_selection == "off":
        coffee_machine_on = False
    elif user_coffee_selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"Money ${profit}")
    else:
        drink = MENU[user_coffee_selection]
        if __sufficient_coffee_resources__(drink["ingredients"]):
            payment = __process_coins__()
            if __check_successful_transaction__(payment, drink["cost"]):
                __make_coffee__(user_coffee_selection, drink["ingredients"])
