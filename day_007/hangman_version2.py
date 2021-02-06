import random

from hangman_wordlist import word_list
from hangman_art import logo, stages

def get_word():
    word = random.choice(word_list).upper()
    return word

word = get_word()
practical_word = list(word)

hidden_word = []
for char in word:
    hidden_word.append('_')


#print(word)
#print(hidden_word)

attempts = 0
max_attempts = 6

print(logo)
playGame = input('Are you ready to play?\n')
if playGame.lower()[0] == 'y':
    game_on = 1
else:
    game_on = 0


while game_on:
    print(f'You have {max_attempts - attempts} attempts remaining.')
    

    word_to_guess = ' '.join(hidden_word)

    print('Word to guess:\n')
    print(word_to_guess)

    guess = input('Please guess a letter\n').upper()

    if guess in practical_word:
        for i in range(len(practical_word)):
            letter = practical_word[i]
            if letter == guess:
                hidden_word[i] = practical_word[i]
                practical_word[i] = '_'

    else:
        attempts += 1

    if all('_' == letter for letter in practical_word):
        print('Congrats! You won!')
        game_on = 0
        
    if attempts >= max_attempts:
        print('You lost! Better luck next time!')
        game_on = 0

    print(stages[max_attempts - attempts])
