# Since I love gaming so much I tried to make a
# snake game using turtle as it's interesting to make


# we need turtle for the graphics of the game
import turtle
# we need random for the random spawning of food in the game
import random
# of course we need to specify when happens what and what speed
import time


# declaring default values
high_score = 0
# delay will basically provide with the speed of different things 
# so we can increase delay to lessen the speed of the game
delay = 0.1
curr_score = 0


# now we will be making a background for the game
# The high score should be there at one corner of the game
# The current score should be there at the other corner of the game

bk = turtle.Screen()
bk.bgcolor("blue")

# let's set the dimensions of the game
bk.title("Snake Game")
bk.setup(width=700, height=700)
bk.tracer(0)


# let's make a boundary for the game
bound = turtle.Turtle()
bound.color("black")
bound.penup()
bound.hideturtle()
bound.goto(-360, 360)
bound.pendown()
bound.width(100)
for i in range(4):
    bound.forward(720)
    bound.right(90)

# we need to make a body for the snake
# let's make its head a circle and rest of the body a square
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
# now we have a circle at the center of the game just there stopped for the time being

# we need to now make food for the snake
# food should come in various size and shapes
food = turtle.Turtle()
food.shape(random.choice(["square", "circle", "triangle"]))
food.color(random.choice(["orange", "pink", "red"]))
# since food should randomly spawn but not move so this
food.speed(0)
food.penup()
food.goto(0, 100)


# now we will declare the writing of the score board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))


# now let's define functions to control the snake
# we will be using the normal keys to do this
# w for forward
# a for left
# d for right
# s for backwards
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


bk.listen()
bk.onkeypress(go_up, "w")
bk.onkeypress(go_down, "s")
bk.onkeypress(go_right, "d")
bk.onkeypress(go_left, "a")

# snake's body
segment = []

# main gameplay
while True:
    bk.update()
    # the following is the termination condition
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.direction = "Stop"
        head.goto(0, 0)
        for s in segment:
            s.goto(1000, 1000)
        segment.clear()
        curr_score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(curr_score, high_score), align="center",
                  font=("candara", 24, "bold"))
    # the following is the normal game condition
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # adding a segment to snakes body as it eats food
        new_segment = turtle.Turtle()
        new_segment.color("red")
        new_segment.shape("square")
        new_segment.speed(0)
        new_segment.penup()
        segment.append(new_segment)
        delay -= 0.01
        curr_score += 10
        if curr_score > high_score:
            high_score = curr_score
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(curr_score, high_score), align="center",
                  font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for i in range(len(segment)-1, 0, -1):
        x = segment[i-1].xcor()
        y = segment[i-1].ycor()
        segment[i].goto(x, y)

    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)
    movement()

    for i in segment:
        if i.distance(head) < 20:
            time.sleep(20)
            head.goto(0, 0)
            head.direction = "Stop"
            for s in segment:
                s.goto(1000, 1000)
            segment.clear()
            curr_score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {}  High Score : {}".format(curr_score, high_score), align="center",
                      font=("candara", 24, "bold"))

    time.sleep(delay)

wn.mainloop()
