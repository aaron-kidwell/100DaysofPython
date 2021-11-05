#Day 15/100 Python Coffee Machine

#import the coffee data that includes menu and resources of the machine
from coffee_data import MENU, resources
resources['money'] = 0
wallet_total = 0
enough_resources = True

#for loop to run until the coffee machine runs out of resources.
while enough_resources:
    ask_coffee = input("What would you like? (Espresso/ Latte/ Cappuccino): ")
    ask_coffee = ask_coffee.lower()

    #prints the total resources
    if ask_coffee == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
        enough_resources = False

    #powers the machine off
    if ask_coffee == 'off':
        print("Powering Off...")
        enough_resources = False

    #insert american coins and add to the wallet total
    def money_insert():
        
        if enough_resources:
            global wallet_total
            print("Please insert coins.")
            quarters = float(input("Number of Quarters to insert: "))
            dimes = float(input("Number of Dimes to insert: "))    
            nickels = float(input("Number of Nickels to insert: "))
            pennies = float(input("Number of Pennies to insert: "))
            quarters = quarters * .25
            dimes = dimes * .10  
            nickels = nickels * .05
            pennies = pennies * .01
            wallet_total = quarters + dimes + nickels + pennies
            resources['money'] = wallet_total
            return wallet_total

    #resource check and deduction for the specific coffee user chooses
    def resource_check(coffee):
        global enough_resources
        
        if coffee == 'espresso':
            if resources['water'] >= 50 and resources['coffee'] >= 18:
                resources['water'] = resources['water'] - 50
                resources['coffee'] = resources['coffee'] - 18            

            else:
                enough_resources = False
                print('Sorry, there is not enough resources for this.')            
              
        elif coffee == 'latte':            
            if resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
                resources['water'] = resources['water'] - 200
                resources['milk'] = resources['milk'] - 150
                resources['coffee'] = resources['coffee'] - 24    

            else:
                enough_resources = False
                print('Sorry, there is not enough resources for this.')     

        elif coffee == 'cappuccino':
            if resources['water'] >= 250 and resources['coffee'] >= 24 and resources['milk'] >= 100:
                resources['water'] = resources['water'] - 250
                resources['coffee'] = resources['coffee'] - 24
                resources['milk'] = resources['milk'] - 100           

            else:
                enough_resources = False
                print('Sorry, there is not enough resources for this.')            

         #send the requested coffee to resource check, to see if there are enough ingredients
    resource_check(ask_coffee)
    money_insert()

    #dispenses the coffee is conditions of cost and resources are met, otherwise refunds money
    def dispense_coffee():
        global wallet_total, enough_resources

        if enough_resources == True and MENU[ask_coffee]['cost'] <= wallet_total:        
            print(f"Here is your {ask_coffee} ☕. Enjoy!")

            if wallet_total > MENU[ask_coffee]['cost'] and enough_resources:
                wallet_total = wallet_total - MENU[ask_coffee]['cost']
                resources['money'] = MENU[ask_coffee]['cost']
                print(f"Here is ${wallet_total} in change.")
        
        elif MENU[ask_coffee]['cost'] > wallet_total and enough_resources:
            print("Sorry, that's not enough money. Money refunded.")
            enough_resources = False  

    if ask_coffee != 'off' and ask_coffee != 'report':
        dispense_coffee()