#Day 10/100 Calculator
from art import logo
print(logo)

#Addition
def add(n1, n2):
    return n1 + n2   
#Subtraction
def subtract(n1, n2):
    return n1 - n2
#Multiplication
def multiply(n1, n2):
    return n1 * n2
#Division
def divide(n1, n2):
    return n1 / n2

#dictionary of operations
operations = {
'+': add,
'-': subtract,
'*': multiply,
'/': divide
}

def calculator(): #recursive function
    num1 = float(input('What is the first number: '))
    #print all operators
    for operator in operations:
        print(operator) 
    resume = True
    #while loop for calculating answer continously, see line 40,41
    while resume:
        operation_choice = input('Choose an operation from the operators above: ')
        num2 = float(input('What is the next number: '))
        operator_function = operations[operation_choice]
        answer = operator_function(num1, num2)
        print(f'{num1} {operation_choice} {num2} = {answer}')

        if input(f"Would you like to continue calculating {answer}? Type 'yes' to continue, or 'new' to start a new calculation: ") == 'yes':
            #if further calculation needed num1 var becomes the answer
            num1 = answer        
        else:
            #ending for loop and back recursive
            resume = False
            calculator()
#initialize calculator function
calculator()