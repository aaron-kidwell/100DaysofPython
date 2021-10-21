# this is my tip calculator which uses simple formulas to calulate tip percentages.

# welcome message
print("Welcome to Aaron's tip calculator!\n\n")

# prompt user for their total bill, how many ways it is split, and the tip percentage.
asktotal_bill = input('What is the total of the bill? ')
asksplit_bill = input('How many people are sharing the bill? ')
asktip = input('What percentage tip would you like to give? ')
# turn the inputs into floats that can be used for calculations
total_bill = float(asktotal_bill)
split_bill = float(asksplit_bill)
tip = float(asktip)
# formula for converting tip percentages
tip_convert = tip / 100 + 1 
# calculating the users share of the bill with the inclusion of a tip
new_total = total_bill / split_bill * tip_convert
# printing the output
print(' Your share of the bill is $' + str(round(new_total, 2)) + '.')
