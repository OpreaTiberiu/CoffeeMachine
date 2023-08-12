from data import MENU, resources
from art import logo

instance_resource = resources
coffee_machine_profit = 0
coffee_emoji = "☕"


def print_report():
    print(f"Water: {instance_resource['water']}ml")
    print(f"Milk: {instance_resource['milk']}ml")
    print(f"Coffee: {instance_resource['coffee']}ml")
    print(f"Money: ${coffee_machine_profit}")


def request_money(money_required):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = calculate_total(quarters, dimes, nickels, pennies)

    if total < money_required:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > money_required:
        print(f"Here is ${round(total - money_required, 2)} dollars in change.")
    return True


def calculate_total(quarters, dimes, nickels, pennies):
    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01


def make_coffee(coffe_type, current_resources):
    if "water" in MENU[coffe_type]["ingredients"].keys():
        if current_resources["water"] >= MENU[coffe_type]["ingredients"]["water"]:
            current_resources["water"] -= MENU[coffe_type]["ingredients"]["water"]
        else:
            print("Sorry there is not enough water")
            return False
    if "milk" in MENU[coffe_type]["ingredients"].keys():
        if current_resources["milk"] >= MENU[coffe_type]["ingredients"]["milk"]:
            current_resources["milk"] -= MENU[coffe_type]["ingredients"]["milk"]
        else:
            print("Sorry there is not enough milk")
            return False
    if "coffee" in MENU[coffe_type]["ingredients"].keys():
        if current_resources["coffee"] >= MENU[coffe_type]["ingredients"]["coffee"]:
            current_resources["coffee"] -= MENU[coffe_type]["ingredients"]["coffee"]
        else:
            print("Sorry there is not enough coffee")
            return False
    return True


print(logo)
machine_working = True
while machine_working:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input in MENU.keys():
        temp_resources = instance_resource.copy()
        if make_coffee(user_input, temp_resources):
            if request_money(MENU[user_input]["cost"]):
                instance_resource = temp_resources
                coffee_machine_profit += MENU[user_input]["cost"]
                print(f"Here is your {user_input}")
    elif user_input == "off":
        print("Stopping the coffee machine...")
        break
    elif user_input == "report":
        print_report()
    else:
        print(f"We do not have {user_input}. Try again...")
