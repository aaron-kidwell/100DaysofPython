# this is a common script logic test with a range from 1, 100
# the goal is to print every number divisible by 3 with Fizz
#print every number divisible by 3 and 5 with FizzBuzz
#print every number divisible by 5 with Buzz
#while still printing all other numbers


for divisible in range(1, 101):
    if divisible % 3 == 0 and divisible % 5 == 0:
        print('FizzBuzz')
    elif divisible % 3 == 0:
        print('Fizz')
    elif divisible % 5 == 0:
        print('Buzz')
    else:
        print(divisible)