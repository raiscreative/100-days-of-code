username = input('Username: ')
password = 'a'
password_confirm = 'b'
while len(password) < 6:
    print('Your password needs to be at least 6 characters long.')
    password = input('Password: ')
    while not password == password_confirm:
        password_confirm = input('Pasword confirm: ')

hidden_password = '*' * len(password)
print(f'{username}, your password {hidden_password} is {len(password)} characters long.')
