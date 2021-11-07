#DAy 16/100 Revisiting coffee machine with object oriented programming.

#import classes and methods
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#assigning objects to variables
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine.report()
coffee_maker.report()
is_on = True
#while loop for machine to run until 'off' while managing resources/payment/dispensing coffee
while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? {options}: ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

