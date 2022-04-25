import turtle

wn = turtle.Screen()
wn.bgcolor("black")

spiral = turtle.Turtle()
num = 10
spiral.speed(100)
spiral.color("white")

for i in range(100):
    spiral.circle(num, 180)
    num += 10

turtle.done()
