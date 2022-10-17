# Turtle co-ordinate system

from turtle import Turtle, Screen
import random

game_is_on = False
screen = Screen()
user_bet = screen.textinput(title='Make a bet',prompt='Select the colour of the turtle which you wish to bet on?: ')
# print(user_bet)

screen.setup(width=500, height=400)
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtle_names = ['bun','cutie', 'dumbo', 'flashy','heman','jack','tim']

for i in range(0,7):
    turtle_names[i] = Turtle(shape='turtle')
    turtle_names[i].color(colors[i])
    turtle_names[i].penup()
    turtle_names[i].goto(x=-230,y=(i*35-105))   # value of y is arranged such that three turtles are
    # above three turtles are below horizon and one at middle with 35 spacing

if user_bet:
    game_is_on = True

while game_is_on:
    for turtle in turtle_names:
        if turtle.xcor() > 230:
            game_is_on = False
            if user_bet == turtle.pencolor():
                print(f"You've won. {turtle.pencolor()} turtle is the winner")
            else:
                print(f"You've lost. {turtle.pencolor()} turtle is the winner")
        turtle.forward(random.randint(0,10))

turtle_score = {}

for turtle in turtle_names:
    score = turtle.xcor()
    turtle_score[turtle.pencolor()] = score

sorted_score = {k: v for k, v in sorted(turtle_score.items(), key=lambda item: item[1], reverse=True)}

print('-------Leader board-------')
print('Position     ','Turtle color')
p = 1
for k in sorted_score.keys():
    print(p,'           ',k)
    p += 1

# import operator
# sorted_score = sorted(turtle_score.items(), key=operator.itemgetter(1))
# print(sorted_score)

screen.exitonclick()
