# Turtle co-ordinate system

from turtle import Turtle, Screen

screen = Screen()
user_bet = screen.textinput(title='Make a bet',prompt='Select the colour of the turtle which you wish to bet on?: ')
# print(user_bet)

screen.setup(width=500, height=400)
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtle_names = ['bun','cutie', 'dumbo', 'flashy','heman','jack','tim']

for i in range(0,7):
    turtle_names[i] = Turtle(shape='turtle')

for i in range(0,7):
    turtle_names[i].color(colors[i])
    turtle_names[i].penup()
    turtle_names[i].goto(x=-230,y=(i*35-105))   # value of y is arranged such that three turtles are
    # above three turtles are below horizon and one at middle with 35 spacing

screen.exitonclick()
