from turtle import Turtle
import random

amy = Turtle()

colours = [
    'MediumVioletRed', 
    'OrangeRed', 
    'SlateBlue', 
    'Orchid', 
    'Gold', 
    'Aquamarine', 
    'DarkCyan', 
    'Crimson',
    'Cyan',
    'DeepPink',
    'DarkMagenta',
    'Salmon',
]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        amy.forward(100)
        amy.right(angle)

for shape_sides in range(3, 11):
    amy.color(random.choice(colours))
    draw_shape(shape_sides)