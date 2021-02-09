import turtle
import random

amy = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        amy.color(random_color())
        amy.circle(100)
        amy.setheading(amy.heading() + size_of_gap)

draw_spirograph(5)

