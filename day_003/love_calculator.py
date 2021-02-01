print('Welcome to the Love Calculator!\n')
game_on = 1
choice = input('Are you ready to find your destiny? y/n \n')
if choice.lower().startswith('n'):
    print('Bye bye, then. Come when you are prepared.')
    game_on = 0
while game_on:
    your_name = input('Please tell us your name\n')
    their_name = input('Please tell us the name of your beloved\n')
    names = (your_name + their_name).lower()
    true_score = 0
    for character in names:
        if character in 'true':
            true_score += 1
    love_score = 0
    for character in names:
        if character in 'love':
            love_score += 1
    score = int(str(true_score) + str(love_score))
    if score < 10 or score > 90:
        print(f'Your score is {score}, you go together like coke and menthos.')
    elif 40 <= score <= 50:
        print(f'Your score is {score}, you are alright together.')
    else:
        print(f'Your score is {score}.')