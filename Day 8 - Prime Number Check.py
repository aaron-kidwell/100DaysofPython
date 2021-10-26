# Day 8/100 Prime Number Check
print('\nWelcome to Aaron''s Prime Number Check!\n')
print(''' ________________________ 
|  ____________________  |
| | PRIME NUMBER CHECK | |
| |____________________| |
|________________________|''')




def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
         print('\nThis IS a prime number.\n')
    else:
         print('\nThis is NOT a prime number.\n')


n = int(input("\nCheck a number: "))
prime_checker(number=n)



