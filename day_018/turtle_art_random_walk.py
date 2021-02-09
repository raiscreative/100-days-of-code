import turtle
import random

amy = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
amy.pensize(15)
amy.speed('fastest')

for _ in range(200):
    amy.color(random_color())
    amy.forward(30)
    amy.setheading(random.choice(directions))