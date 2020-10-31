# Coffee Machine - Stage 1
# Coffee Machine - Stage 2
# Coffee Machine - Stage 3
# Coffee Machine - Stage 4
# Coffee Machine - Stage 5
# Coffee Machine - Stage 6
# Add GIT

import math


# global variables
class CoffeeMachine:

    def __init__(self):
        self.state = {"money": 550, "water": 400, "milk": 540, "beans": 120, "cups": 9}
        self.bought = None
        self.option = None
        self.enough_resources = None
        self.type_of_coffee = None

    def take_money(self):
        print(f"I gave you ${self.state['money']}")
        self.state['money'] = 0

    def machine_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.state['water']} of water")
        print(f"{self.state['milk']} of milk")
        print(f"{self.state['beans']} of coffee beans")
        print(f"{self.state['cups']} of disposable cups")
        print(f"{self.state['money']} of money")

    def fill_machine(self):
        add_water = int(input("Write how many ml of water do you want to add:\n"))
        add_milk = int(input("Write how many ml of milk do you want to add:\n"))
        add_coffee = int(input("Write how many grams of coffee beans do you want to add:\n"))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.state['water'] += add_water
        self.state['milk'] += add_milk
        self.state['beans'] += add_coffee
        self.state['cups'] += add_cups

    def is_enough(self, water, milk, coffee, cups):
        self.enough_resources = False
        water_enough = True if self.state['water'] >= water else False
        milk_enough = True if self.state['milk'] >= milk else False
        coffee_enough = True if self.state['beans'] >= coffee else False
        cups_enough = True if self.state['cups'] >= cups else False
        if water_enough and milk_enough and coffee_enough and cups_enough:
            self.enough_resources = True
            print("I have enough resources, making you a coffee!")
        elif not water_enough:
            print("Sorry, not enough water!")
        elif not milk_enough:
            print("Sorry, not enough milk!")
        elif not coffee_enough:
            print("Sorry, not enough coffee beans!")
        elif not cups_enough:
            print("Sorry, not enough disposable cups!")
        else:
            print('Sorry, not enough resources')
        return self.enough_resources

    def set_ingredients(self, water, milk, coffee, cups, money):
        self.state['water'] += water
        self.state['milk'] += milk
        self.state['beans'] += coffee
        self.state['cups'] += cups
        self.state['money'] += money

    def buy_coffee(self):
        self.bought = False
        self.type_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.type_of_coffee == '1':
            if self.is_enough(250, 0, 16, 1):
                self.set_ingredients(-250, 0, -16, -1, 4)
                self.bought = True
        elif self.type_of_coffee == '2':
            if self.is_enough(350, 75, 20, 1):
                self.set_ingredients(-350, -75, -20, -1, 7)
                self.bought = True
        elif self.type_of_coffee == '3':
            if self.is_enough(200, 100, 12, 1):
                self.set_ingredients(-200, -100, -12, -1, 6)
                self.bought = True
        elif self.type_of_coffee == 'back':
            self.bought = False
        return self.bought

    def init_option(self):
        self.option = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        return self.option

    def machine_run(self):
        while True:
            opt = self.init_option()
            if opt == 'buy':
                self.buy_coffee()
            elif opt == 'fill':
                self.fill_machine()
            elif opt == 'take':
                self.take_money()
            elif opt == 'remaining':
                self.machine_state()
            elif opt == 'exit':
                break

small_coffee = CoffeeMachine()
small_coffee.machine_run()




