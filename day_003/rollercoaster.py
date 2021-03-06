import random

print('Hello! Welcome to the Rollercoaster!')
game_on = 1
while game_on:
    choice = input('Would you like a ride? y/n')
    if choice.lower().startswith('n'):
        print('Come another time, then! Have a nice day!')
        exit()
    else: 
        print('Great choice!\nLet us check your height first!')
        height = random.randint(50, 200)
        if height < 120:
            print('Sorry. You need to grow taller before you can ride the rollercoaster. Have a nice day!')
            exit()
        else:
            print('Congratulations, you are hight enough to ride the rollercoaster!')
            age = int(input('How old are you?\n'))
            if 45 <= age <= 55:
                price = 0
                print('Have fun and enjoy life, this rollercoaster ride is free!')
            elif age <= 12:
                price = 5
            elif age < 18:
                price = 7
            else:
                price = 12
            print(f'The ticket is ${price}')
            photo = input('Do you want a photo taken? y/n\n')
            if photo.lower().startswith('y'):
                price += 3
                print(f'Thank you. The ticket is ${price}')
            pay = input('Do you want to buy a ticket now? y/n')
            if pay.lower().startswith('n'):
                print('Very well then, please come another time. Have a nice day.')
                game_on = 0
            else: print('Thank you! Have a great ride!')