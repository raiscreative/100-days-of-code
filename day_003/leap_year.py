print('Welcome to the Leap Year Calculator')
game_on = 1
while game_on:
    year = int(input('What year do you want to check?\n'))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year.')
            else:
                print(f'{year} is not a leap year.')
        else:
            print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')