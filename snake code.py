import turtle as trtl

wn = trtl.Screen()
turtle = trtl.Turtle()
food_balls = trtl.Turtle()
pacman = "pacman.gif"
turtle.turtlesize(1)
wn.addshape(pacman)
turtle.shape(pacman)
turtle.penup()

food_balls.fillcolor("red")
food_balls.begin_fill()
food_balls.circle(15)
food_balls.end_fill()
def move_right():
    turtle.setheading(0)
    turtle.forward(25)


def move_up():
    turtle.setheading(90)
    turtle.forward(25)


def move_left():
    turtle.setheading(180)
    turtle.forward(25)


def move_down():
    turtle.setheading(270)
    turtle.forward(25)



wn.onkeypress(move_right, "d")
wn.onkeypress(move_up, "w")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_down, "s")
wn.listen()
wn.exitonclick()
