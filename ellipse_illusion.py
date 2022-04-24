# multiple ellipses illusion
import turtle


# background specs
wn = turtle.Screen()
wn.bgcolor("black")

# turtle specs
ellipse = turtle.Turtle()
ellipse.color("white")
ellipse.hideturtle()


def ellipse_draw(rad):
    for i in range(2):
        ellipse.circle(rad, 90)
        ellipse.circle(rad//2, 90)


color_tray = ["Violet", "Red", "Pink", "Orange", "Yellow", "White", "Green", "Pink", "Blue"]
n = len(color_tray)
angle = 10
val = 0
ellipse.speed(50)


for i in range(36):
    if val == n-1:
        val = 0
    else:
        val += 1
    ellipse.color(color_tray[val])
    ellipse.seth(-angle)
    ellipse_draw(100)
    angle += 10


turtle.done()
