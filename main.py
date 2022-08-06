from turtle import Turtle, Screen
import random
WIDTH = 500
HEIGHT = 400
screen = Screen()
screen.setup(WIDTH, HEIGHT)
color = screen.textinput("Choose color", "Choose a color for your turtle")

colors = ["blue", "red", "yellow", "purple", "green", "orange"]
turtles = []
positions = [-90,-60,-30,0,30]
on = False  

x = 0
def newTurtle(color, pos):
    tur = Turtle("turtle")
    tur.color(color)
    tur.penup()
    tur.goto(pos)
    return tur

for x in range(5):
    t1 = newTurtle(colors[x], (-240, positions[x]))
    turtles.append(t1)

if color.lower() in colors:
    on = True

while on:
    
    for t in turtles:
        if t.xcor() >= 230:
            on = False
            winner = t.pencolor()
            if winner == color:
                print(f"You win. ")
            else:
                print(f"You loose. The winner is {winner}")
        mov = random.randint(0,10)
        t.forward(mov)
        
        


screen.exitonclick()