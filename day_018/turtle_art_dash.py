from turtle import Turtle

amy = Turtle()
amy.shape('turtle')
amy.color('purple')

for _ in range(15):
    amy.forward(10)
    amy.penup()
    amy.forward(10)
    amy.pendown()