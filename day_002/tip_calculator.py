print('Welcome to the tip calculator.')
total = round(float(input('What is the total bill? \n$')), 2)
print('What percentage tip would you like to give?\nPlease enter the corresponding letter\na) 0\nb) 10\nc) 12\nd) 15')
choice = input()
if choice.lower() == 'a':
    bill = total
    print(f'No tip. OK then, your bill remains ${bill}.')
elif choice.lower() == 'b':
    bill = round(total * 1.1, 2)
    print(f'10% tip. Thank you for that. Your bill is now ${bill}.')
elif choice.lower() == 'c':
    bill = round(total * 1.12, 2)
    print(f'12% tip. Thank you for that. Your bill is now ${bill}.')
elif choice.lower() == 'd':
    bill = round(total * 1.15, 2)
    print(f'15% tip. So generous, thank you very much. Your bill is now ${bill}.')
else:
    print('Poor thing, you don\'t know how to read.\nNo charge, you need to invest in your education!')
    exit()

people = int(input('How many people to split the bill?\n'))
pay = round(bill/people, 2)
print(f'Each person should pay ${pay:.2f}. Come again.')