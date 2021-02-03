import random

letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
#print(letters)
numbers = '0 1 2 3 4 5 6 7 8 9'.split()
chars = '! @ # $ % ^ & * ( ) _ +'.split()
num_letters = int(input('How many letters you want in your password? '))
num_numbers = int(input('How many numbers you want in your password? '))
num_chars = int(input('How many special characters you want in your password? '))

def generate_password(num_letters, num_numbers, num_chars):
    password = []
    for i in range(1, num_letters + 1):
        password.append(random.choice(letters))
    for j in range(1, num_numbers + 1):
        password.append(random.choice(numbers))
    for k in range(1, num_chars + 1):
        password.append(random.choice(chars))
    #print(password)
    random.shuffle(password)
    #print(password)
    password = ''.join(password)
    print(f'Your unique password is: {password}')

generate_password(num_letters, num_numbers, num_chars)