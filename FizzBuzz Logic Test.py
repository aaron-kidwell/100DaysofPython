for divisible in range(1, 101):
    if divisible % 3 == 0 and divisible % 5 == 0:
        print('FizzBuzz')
    elif divisible % 3 == 0:
        print('Fizz')
    elif divisible % 5 == 0:
        print('Buzz')
    else:
        print(divisible)