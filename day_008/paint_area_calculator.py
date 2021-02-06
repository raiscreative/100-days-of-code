import math

def paint_area_calculator(height, width, coverage):
    cans = math.ceil(height*width/coverage)
    return cans

height = int(input('The height of the wall: '))
width = int(input('The width of the wall: '))
coverage = 5

cans = paint_area_calculator(height, width, coverage)
print(f'You\'ll need {cans} cans of paint.')