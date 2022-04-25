import turtle

# background specs
wn = turtle.Screen()
wn.bgcolor("black")

# turtle specs
spi = turtle.Turtle()

color_tray = ["yellow", "purple", "green", "pink", "white", "red"]
n = len(color_tray)
spi.speed(100)

for i in range(300):
    spi.color(color_tray[i % n])
    spi.forward(i)
    spi.width(i // 100)
    spi.left(59)


turtle.done()
