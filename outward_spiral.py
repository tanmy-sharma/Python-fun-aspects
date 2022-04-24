# outward spiral
import turtle

# background Specs
wn = turtle.Screen()
wn.bgcolor("black")

# spiral specifications
spiral = turtle.Turtle()
spiral.color("white")

size = 10  # size of the first line drawn

while size != 200:
    for i in range(2):
        spiral.forward(size)
        spiral.left(90)
    size += 10


turtle.done()
