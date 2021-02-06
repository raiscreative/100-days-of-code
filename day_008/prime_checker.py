def prime_checker(number):
    is_prime = True
    for i in range (2, number//2):
        if number % i == 0:
            is_prime = False
    return is_prime

number = int(input('Welcome to the Prime Checker!\nProvide a number to check: '))

is_prime = prime_checker(number)
if is_prime:
    print(f'{number} is a prime number.')
else: 
    print(f'{number} is not a prime number.')