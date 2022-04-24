# inward spiral
import turtle

# background Specs
wn = turtle.Screen()
wn.bgcolor("black")

# spiral specifications
spiral = turtle.Turtle()
spiral.color("white")
spiral.penup()
spiral.goto(-100, -100)
spiral.pendown()

size = 200  # size of the first line drawn

while size != 0:
    for i in range(2):
        spiral.forward(size)
        spiral.right(90)
    size -= 10


turtle.done()
