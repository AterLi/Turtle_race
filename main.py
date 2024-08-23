from turtle import Turtle, Screen
import random


screen = Screen()
game_on= True

choose = screen.textinput(title="Choose the winner", prompt="Choose the turtle: ")
print(choose)
colors = ["red", "orange", "yellow", "green", "purple"]
turtles_positions = [200, 100, 0, -100, -200]
all_turtles = []

for i in range(len(colors)):
    timy = Turtle(shape="turtle")
    timy.penup()
    timy.color(colors[i])
    timy.setposition(x= -380, y=turtles_positions[i])
    all_turtles.append(timy)



while game_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(7, 20))
        if turtle.xcor() > 360:
            the_winner = turtle.pencolor()
            game_on = False
            if the_winner == choose:
                print(f"Your bet won, the winner color is {the_winner}")
            else:
                print(f"Your bet lost, the winner is {the_winner}")







screen.exitonclick()
