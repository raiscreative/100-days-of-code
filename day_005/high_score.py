score_list = input('Please enter the list of all students\' score\n')
scores = score_list.split()
high_score = -100
for score in scores:
    score = int(score)
    if score > high_score:
        high_score = score
print(f'The highest score in the class is {high_score}.')