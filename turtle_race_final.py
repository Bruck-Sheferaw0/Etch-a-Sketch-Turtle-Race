from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Winner",'Who do you think will win? Colors are all from the rainbow. Enter a color: ')
colors_list = ["red",'orange','yellow','green','blue','purple']
random.shuffle(colors_list)

all_turtles = []

y_value = -100
for i in range(0,6):     #creating multiple turtle instances
    new_turtles = Turtle(shape='turtle')
    new_turtles.penup()
    new_turtles.color(colors_list[i])
    new_turtles.goto(-235,y_value)
    y_value += 30
    all_turtles.append(new_turtles)

go = True
while go:
    for i in all_turtles:
        i.speed(5)
        i.forward(random.randint(0,10))
        if i.xcor() > 230:
            if user_bet.lower() == i.pencolor():
                print(f"{i.pencolor()} is the winner. You guessed {user_bet}, which won the race!")
            else:
                print(f"{i.pencolor()} is the winner. You guessed {user_bet}, which lost the race!")
            go = False

screen.exitonclick()