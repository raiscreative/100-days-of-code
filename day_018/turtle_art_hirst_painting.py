import turtle 
import random

turtle.colormode(255)
amy = turtle.Turtle()
amy.speed("fastest")
amy.penup()
amy.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
amy.setheading(225)
amy.forward(300)
amy.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    amy.dot(20, random.choice(color_list))
    amy.forward(50)

    if dot_count % 10 == 0:
        amy.setheading(90)
        amy.forward(50)
        amy.setheading(180)
        amy.forward(500)
        amy.setheading(0)
