def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    num1 = float(input('What\'s the first number? '))
    for operation in operations:
        print(operation)

    game_on = 1
    while game_on:
        operation = ''
        while operation not in operations:
            operation = input('Pick an operation ')
        num2 = int(input('What\'s the next number? '))
        result = operations[operation](num1, num2)
        print(f'{num1} {operation} {num2} = {result}\n')
        choice = ''
        print(f'What do you want to do now?\n1. Continue calculating with {result}\n2. Start a new calculation\n3. Exit the calculator')
        while choice not in ['1', '2', '3']:
            choice = input() 
        if choice == '1':
            num1 = result
        elif choice == '2':
            print('\n'*100)
            calculator()
        else:
            print('ttfn')
            exit()

calculator()