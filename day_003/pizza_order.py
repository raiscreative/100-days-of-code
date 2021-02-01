choice = input('Welcome to Pizza Hot! Do you want to place a new order? y/n\n')
order = 0
if choice.lower().startswith('y'):
    order = 1
else:
    print('Very well then, come another time!')
while order:
    size = input('Would you like a small, medium or large pizza? s/m/l/\n')
    pepperoni = input('Would you like pepperoni on your pizza? y/n\n')
    cheese = input('Would you like extra cheese on your pizza? y/n\n')
    if size.lower().startswith('s'):
        price = 15
        if pepperoni.lower().startswith('y'):
            price += 2 
    elif size.lower().startswith('m'):
        price = 20
        if pepperoni.lower().startswith('y'):
            price += 3
    else:
        price = 25
        if pepperoni.lower().startswith('y'):
            price += 3
    if cheese.lower().startswith('y'):
            price += 1
    print(f'Your pizza is ${price}, please. Enjoy!')