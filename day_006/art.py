from termcolor import colored

for i in range(1, 11):
    if i % 2 == 0:
        print(colored(u'\u2B24' + ' ', 'green') * i)
    else:
        print(colored(u'\u2B24' + ' ', 'red') * i)

