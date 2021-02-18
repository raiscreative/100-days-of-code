import random

num_students = int(input('How many students are there? '))
students = [input('Student: ') for _ in range(num_students)]

students_scores = {student: random.randint(1, 100) for student in students}

for student in students_scores:
    print(f'{student} has got a score of {students_scores[student]} points.')

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)