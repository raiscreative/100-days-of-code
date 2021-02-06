import random

from higher_lower_art import logo, vs
from higher_lower_data import data


def get_random_account():
    return random.choice(data)


def display_accounts(account_a, account_b):
    print('Compare:')
    print(f"A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(vs)
    print(f"B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")


def guess_right(guess):
    if account_a['follower_count'] > account_b['follower_count']: 
        right_guess = 'a'
    else:
        right_guess = 'b'
    return guess == right_guess


print(logo)
score = 0
game_on = 1
account_a = get_random_account()
account_b = get_random_account()

while game_on:
    account_a = account_b
    account_b = get_random_account()

    while account_b == account_a:
        account_b = random.choice(data)

    display_accounts(account_a, account_b)

    guess = input('Who has more likes? A/B\n').lower()

    print('\n'*100)
    print(logo)

    if guess_right(guess): 
        score += 1
        print(f'You\'re right! Current score: {score}.')
    else: 
        print(f'Sorry, that\'s wrong. Final score: {score}.')
        game_on = 0