from turtle import Turtle, Screen

amy = Turtle()
screen = Screen()


def move_forwards():
    amy.forward(10)

def move_backwards():
    amy.backward(10)

def turn_left():
    new_heading = amy.heading() + 10
    amy.setheading(new_heading)

def turn_right():
    new_heading = amy.heading() - 10
    amy.setheading(new_heading)

def clear():
    amy.clear()
    amy.penup()
    amy.home()
    amy.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
