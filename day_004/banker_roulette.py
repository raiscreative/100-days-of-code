import random

names = input('Please enter the names of all people who participate, separated by commas.\n')
name_list = names.split(', ')
#print(name_list)
num = random.randint(0, len(name_list) - 1)
winner = name_list[num]
print(f'{winner} will pay the bill.')