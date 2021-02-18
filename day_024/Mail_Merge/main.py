PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt') as f:
    names = f.readlines()


with open('Input/Letters/starting_letter.txt') as f:
    letter = f.read()
    for name in names:
        stripped_name = name.strip()
        personalized_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as new_letter:
            new_letter.write(personalized_letter)