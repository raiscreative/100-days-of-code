game_on = 1
while game_on:
    print('Welcome to the BMI Calculator! Keep healthy!')
    choice = input('Do you want to check your BMI? y/n')
    if choice.lower().startswith('n'):
        print('Very well then, take care!')
        exit()
    height = float(input('What is your height in m?\n'))
    weight = int(input('What is your weight in kg?\n'))
    print(
        f'You are {height}m height and {weight}kg.'
    )
    bmi = round(weight / height**2)
    if bmi < 18.5:
        print(f'Your BMI is {bmi}. You are underweight.')
    elif bmi < 25:
        print(f'Your BMI is {bmi}. You have a normal weight.')
    elif bmi < 30:
        print(f'Your BMI is {bmi}. You are overweight.')
    elif bmi < 35:
        print(f'Your BMI is {bmi}. You are obese.')
    else:
        print(f'Your BMI is {bmi}. You are clinically obese.')