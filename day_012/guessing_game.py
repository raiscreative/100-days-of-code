import random
choice = input('Welcome to the guessing game!\nChoose your game level:\n1. Easy\n2. Medium\n3. Hard\n')
if choice == '1':
    max_num = 10
    guesses = 4
elif choice == '2':
    max_num = 100
    guesses = 6
else:
    max_num = 1000
    guesses = 10

print(f'Your goal is to guess a number between 1 and {max_num}. You have {guesses} guesses.')
num_chosen = random.randint(1, max_num)
guess = -1
while guess != num_chosen and guesses >=1:
    guess = int(input(f'Go ahead. Make a guess. Still {guesses} guesses left.\n'))
    guesses -= 1
    if guess > num_chosen:
        if guesses == 0:
            print('You\'re out of guesses, mate! You lose! Better luck next time!')
        else:
            print('Too large. Try a smaller number.')
    elif guess < num_chosen:
        if guesses == 0:
            print('You\'re out of guesses, mate! You lose! Better luck next time!')
        else:
            print('Too small. Try a larger number.')
    else: 
        print('Good job. You guessed the number and won the game!')
