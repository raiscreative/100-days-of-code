from termcolor import colored

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


green_field = colored('*', 'green')
empty_field = ' '
for line in picture:
  for pixel in line:
    if pixel:
      print(green_field, end ="")
    else:
      print(empty_field, end ="")
  print('')