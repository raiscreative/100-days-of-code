line = 'How are you doing?'
print (line)
line = input()
while not line.lower().startswith('stop copying me'):
    print(line)
    line = input()
print('ok you win!')

    
