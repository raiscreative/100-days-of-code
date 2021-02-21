import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic_message():
    message = input('What do you have to say? Speak clearly! ').upper()
    try:
        phonetic_message = [nato_dict[char] for char in message]
    except KeyError:
        print('Please use only characters from the alphabet.')
        generate_phonetic_message()
    else:
        print(phonetic_message)

generate_phonetic_message()