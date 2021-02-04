picture = [
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0]
]

def print_field(picture):
  treasure = '🟥'
  field = '🟩'
  i = 1
  print('  A  B  C  D  E  F  G')
  for line in picture:
    print(i, end = '')
    i += 1
    for pixel in line:
      if pixel:
        print(treasure, end ="")
      else:
        print(field, end ="")
    print('')


print_field(picture)
print('Hello. \nHere\'s a great place to hide the treasure.\nPick a field. (e.g. A1)')
position = input()
print(f'You chose {position}. Are you sure?')
is_sure = ''
is_sure = input()
while not is_sure.lower().startswith('y'):
  print('Pick another field.')
  position = input()
  print(f'You chose {position}. Are you sure?')
  is_sure = input()


columns = 'ABCDEFG'
column = columns.index(position[0].upper())
row = int(position[1]) - 1
picture[row][column] = '1'

print('Here\'s a map to your treasure:')
print_field(picture)