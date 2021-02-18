import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')



nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

message = input('What do you have to say? Speak clearly! ').upper()
phonetic_message = [nato_dict[char] for char in message]
print(phonetic_message)