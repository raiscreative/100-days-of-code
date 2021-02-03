import random


rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_art = [rock_art, paper_art, scissors_art]
for art in game_art: 
    print (art)

game_on = 1
while game_on:
    choice = input('Ready to play the game? y/n\n')
    if choice.lower().startswith('n'):
        game_on = 0
        break
    print('Make your move:\n1.Rock\n2.Paper\n3.Scissors\n')
    player = ''
    while player not in [1, 2, 3]:
        player = int(input('Type 1, 2 or 3 to play\n'))
    print('You played:\n')
    print(game_art[player - 1])
    computer = random.randint(1, 3)
    print('Computer plays:\n')
    print(game_art[computer - 1])
    if player == computer:
        print('It\'s a draw.')
    elif (player == 1 and computer == 2) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print('You win!')
    else:
        print('You lose!')