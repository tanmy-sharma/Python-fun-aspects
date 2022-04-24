import turtle

# screen specs
wn = turtle.Screen()
wn.bgcolor("black")

# turtle specs
octagon = turtle.Turtle()
octagon.pencolor("white")
octagon.hideturtle()
octagon.pensize(5)

for j in range(6):
    for i in range(6):
        octagon.forward(100)
        octagon.left(60)
    octagon.left(60)

turtle.done()
