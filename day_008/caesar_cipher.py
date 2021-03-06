alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
def caesar(message, shift, direction):
    new_message = ''
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_position = position + shift
            else:
                new_position = position - shift
            new_letter = alphabet[new_position]
            new_message += new_letter
        else:
            new_message += char
    return new_message
    
game_on = 1
while game_on:
    direction = ''
    while direction not in ['encode', 'decode']:
        direction = input('Do you want to encode or decode a message? Type encode/decode\n')
    message = input('What is your message?\n').lower()
    shift = int(input('What is the shift?\n'))
    shift = shift % 25
    new_message = caesar(message, shift, direction)
    print(f'The {direction}d message is {new_message}.')
    choice = input('Do you want to run again? yes/no\n')
    if choice.lower().startswith('n'):
        game_on = 0