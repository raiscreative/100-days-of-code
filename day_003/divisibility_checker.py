print('Welcome to the divisibility checker!')
game_on = 1
while game_on:
    first = int(input('Type a large number, more than 3 digits,please.\n'))
    second = int(input('Now type a number between 2 and 25.'))
    if first % second == 0:
        print(f'{first} is perfectly divisible with {second}.')
    else:
        print(f'{first} is not perfectly divisible with {second}.')
    choice = input('Do you want to play again? (y/n)')
    if choice.lower().startswith('n'):
        game_on = 0