height_list = input('Please enter the list of all students\' height\n')
heights = height_list.split()
students = 0
heights_sum = 0
for height in heights:
    students += 1
    heights_sum += int(height)
average_height = round(heights_sum / students)
print(f'The average height is: {average_height}.')