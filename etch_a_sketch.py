from turtle import Turtle, Screen

user = Turtle()
screen = Screen()


def move_forward():
    user.forward(10)
def move_backward():
    user.backward(10)
def move_left():
    user.right(10)
def move_right():
    user.left(10)
def clears():
    user.clear()
    user.penup()
    user.home()
    user.pendown()
screen.listen()

screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='a',fun=move_left)
screen.onkey(key='d',fun=move_right)
screen.onkey(key='c',fun=clears)
screen.exitonclick()
