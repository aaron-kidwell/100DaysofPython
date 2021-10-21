#My Password Generator Project
import random
#Create lists with potential letters, numbers, and symbols for user to call from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#Collect inputs
print("Welcome to Aaron's PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Randomize the letters, numbers, and symbols by amount
randomletters = random.sample(letters, nr_letters)
randomnumbers = random.sample(numbers, nr_numbers)
randomsymbols = random.sample(symbols, nr_symbols)
#add random list together
password = randomletters + randomnumbers + randomsymbols
#first take the length of the password variable, then use random to scramble amount
randomize = len(password)
newpass = random.sample(password, randomize)
randomize = ''.join(newpass)
#print new password
print(randomize)
