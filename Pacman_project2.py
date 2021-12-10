'''
Instructions:

Click Run!
'''

#Ghost Template:
#   a115_ghost_maze.py
import turtle as trtl
import turtle as trtl2
import turtle as trtl3
import random as rand

trtl.speed(0)
wn = trtl.Screen()
wn.bgcolor("black")
#-------------------maze and turtle config variables-----------------
screen_h = 600
screen_w = 600
startx = 0
starty = 0
turtle_scale = 1.5
#Timer and Scoreboard
timer = 99
counter_interval = 1000 
timer_up = False
score = 0
score_writer = trtl2.Turtle()
counter =  trtl3.Turtle()
font_setup = ("Arial", 20, "normal")
#---------------------------GHOST COMMANDS---------------------------

#-----name input
gamer_name=input("What's your name, gamer?")

#----- init screen

trtl.setup(width=screen_w, height=screen_h)
blinky_image = "1.Blinky(Red).gif"
trtl.addshape(blinky_image)

#----- init ghost
blinky = trtl.Turtle(shape=blinky_image)
blinky.hideturtle()
blinky.pencolor("blue")
blinky.penup()
blinky.setheading(90)
blinky.turtlesize(turtle_scale, turtle_scale)
blinky.goto(startx, starty)
blinky.speed(2)
blinky.showturtle()

#----- init screen

trtl.setup(width=screen_w, height=screen_h)
inky_image = "1.Inky(Teal).gif"
trtl.addshape(inky_image)

#----- init ghost
inky = trtl.Turtle(shape=inky_image)
inky.hideturtle()
inky.penup()
inky.setheading(90)
inky.turtlesize(turtle_scale, turtle_scale)
inky.goto(startx, starty)
inky.speed(2)
inky.showturtle()

#----- init screen

trtl.setup(width=screen_w, height=screen_h)
pinky_image = "1.Pinky(Pink).gif"
trtl.addshape(pinky_image)

#----- init ghost
pinky = trtl.Turtle(shape=pinky_image)
pinky.hideturtle()
pinky.penup()
pinky.setheading(90)
pinky.turtlesize(turtle_scale, turtle_scale)
pinky.goto(startx + 5, starty)
pinky.speed(2)
pinky.showturtle()

#----- init screen

trtl.setup(width=screen_w, height=screen_h)
clyde_image = "1.Clyde(Orange).gif"
trtl.addshape(clyde_image)

#----- init ghost
clyde = trtl.Turtle(shape=clyde_image)
clyde.hideturtle()
clyde.pencolor("blue")
clyde.penup()
clyde.setheading(90)
clyde.turtlesize(turtle_scale, turtle_scale)
clyde.goto(startx, starty)
clyde.speed(2)
clyde.showturtle()

# array of ghosts
ghosts = [blinky, inky, pinky, clyde]

#Create Pacman

pac_closed = "3.Pacman_closed.gif"
pac_open = "3.Pacman_open.gif"
pac_up = "3.Pacman_up.gif"
pac_up_closed = "3.Pacman_up_closed.gif"
pac_down = "3.Pacman_down.gif"
pac_down_closed = "3.Pacman_down_closed.gif"

trtl.addshape(pac_open)
trtl.addshape(pac_closed)
trtl.addshape(pac_up)
trtl.addshape(pac_up_closed)
trtl.addshape(pac_down)
trtl.addshape(pac_down_closed)
PACMAN = trtl.Turtle(shape=pac_closed)

PACMAN.color("white")
#create Food dots
dot = "dot.gif"
trtl.addshape(dot)
DOT = trtl.Turtle(shape=dot)


# countdown function
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    wn.bgpic("gameover.gif")
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# update and display the score
def update_score():
  global score
  score = score + 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

#===========================DRAW DOTS==========================
pacman_pos = []
collision_length = 15

dots = []
DOT.speed(0)
def add_dot():
    dot_clone = DOT.clone()
    dots.append(dot_clone)


def add_dot_amount(amount):
    for i in range(amount):
        DOT.forward(20)
        add_dot()

def draw_dots():  
  DOT.penup()
  DOT.setheading(0)
  DOT.setpos(-205, 0)

  add_dot_amount(6)
  DOT.left(90)
  add_dot_amount(8)
  DOT.right(90)
  add_dot_amount(12)
  DOT.forward(5)
  DOT.right(90)
  add_dot_amount(18)
  DOT.backward(290)
  DOT.left(90)
  add_dot_amount(5)
  DOT.setpos(-85, 0)

  DOT.right(90)
  add_dot_amount(8)
  DOT.left(90)
  add_dot_amount(3)
  DOT.left(90)
  add_dot_amount(9)
  DOT.left(90)
  add_dot_amount(2)
  DOT.backward(40)
  DOT.right(90)
  add_dot_amount(6)
  DOT.backward(225)
  DOT.right(90)
  add_dot_amount(6)
  DOT.forward(10)
  DOT.left(90)
  add_dot_amount(10)
  add_dot_amount(1)
  DOT.forward(40)
  add_dot_amount(1)


draw_dots()

#===========================FUNCTIONS=========================

# PATHWAY should be 30 pixels wide

pos = 0

def ghost_box():
    trtl.penup()
    trtl.setposition(0,-35)
    trtl.pendown()
    trtl.color("black")
    trtl.setheading(0)
    trtl.fillcolor("black")
    trtl.begin_fill()     
    for i in range(2):
      trtl.forward(75)
      trtl.left(90)
      trtl.forward(150)
      trtl.left(90)
      trtl.penup()
      trtl.end_fill()

    trtl.penup()
    trtl.setposition(75,30)
    trtl.pendown()
    trtl.color("black")
    trtl.fillcolor("black")
    trtl.begin_fill()
    for i in range(2):
      trtl.forward(20)
      trtl.left(90)
      trtl.forward(20)
      trtl.left(90)
    trtl.end_fill()

# ---------------------GHOST MOVEMENT--------------------

def ghost_tp(x, y, ghost):
  ghost.penup()
  ghost.speed(4)
  ghost.setpos(x, y)
  ghost.pendown()

# ---------------------PACMAN MOVEMENT--------------------
def pac_tp(x, y):
    PACMAN.penup()
    PACMAN.hideturtle()
    PACMAN.setpos(x, y)
    PACMAN.showturtle()
    PACMAN.pendown()

def move_right():
    PACMAN.setheading(0)
    PACMAN.forward(15)
    for dot in dots:
      if abs(PACMAN.xcor() - dot.xcor()) <= collision_length and abs(PACMAN.ycor() - dot.ycor()) <= collision_length:
        dot.hideturtle()

def move_up():
    PACMAN.setheading(90)
    PACMAN.forward(15)
    for dot in dots:
      if abs(PACMAN.xcor() - dot.xcor()) <= collision_length and abs(PACMAN.ycor() - dot.ycor()) <= collision_length:
        dot.hideturtle()

def move_left():
    PACMAN.setheading(180)
    PACMAN.forward(15)
    for dot in dots:
       if abs(PACMAN.xcor() - dot.xcor()) <= collision_length and abs(PACMAN.ycor() - dot.ycor()) <= collision_length:
        dot.hideturtle()

def move_down():
    PACMAN.setheading(270)
    PACMAN.forward(15)
    for dot in dots:
      if abs(PACMAN.xcor() - dot.xcor()) <= collision_length and abs(PACMAN.ycor() - dot.ycor()) <= collision_length:
        dot.hideturtle()
  
# ---------------------drawing map--------------------
def long_rect():
    trtl.color("blue")
    trtl.begin_fill()
    for i in range(2):
        trtl.forward(400)
        trtl.left(90)
        trtl.forward(25)
        trtl.left(90)
    trtl.end_fill()


def rect(l, w):
    trtl.color("blue")
    trtl.fillcolor("blue")
    trtl.begin_fill()
    for i in range(2):
        trtl.forward(l)
        trtl.left(90)
        trtl.forward(w)
        trtl.left(90)
    trtl.end_fill()

def tp(x, y):
    trtl.penup()
    trtl.setpos(x, y)
    trtl.pendown()

def tofront(ghost):
  ghost.forward(0)
def startghosts():
  blinky.showturtle()
  clyde.showturtle()
  inky.showturtle()
  pinky.showturtle()
  ghost_tp(37.5, 0, inky)
  
  inky.stamp()
  
  ghost_tp(37.5, 25, pinky)
  
  pinky.stamp()
  
  ghost_tp(37.5, 50, clyde)
  
  clyde.stamp()
  
  ghost_tp(37.5, 75, blinky)
  
  blinky.stamp()

blinky.showturtle()
clyde.showturtle()
inky.showturtle()
pinky.showturtle()


def init_boxes():
    # bottom_left
    tp(-200, -200)
    rect(100, 185)

    # top_left
    tp(-200, 15)
    rect(100, 185)

    # border_top
    tp(-200, 175)
    long_rect()

    # right_top
    tp(175, 105)
    rect(25, 95)

    # right_bottom
    tp(175, -200)
    rect(25, 275)

    # big_bottom
    tp(-15, -200)
    rect(160, 100)

    # obs_bottom
    tp(-70, -145)
    rect(25, 150)

    # obs_top
    tp(-70, 35)
    rect(25, 110)

    #  border_bottom
    tp(-100, -200)
    rect(85, 25)

    # barrier_right
    tp(120, -100)
    rect(25, 175 + 70)

    # ghost_container
    tp(-15, -70)
    rect(105, 215)

    ghost_box()

    startghosts()

    trtl.hideturtle()
PACMAN.penup()
PACMAN.setposition(-200,0)




#===========================DRAW BOXES==========================

init_boxes()

inky.showturtle()
blinky.showturtle()
clyde.showturtle()
pinky.showturtle()
startghosts()
#--------------------MAIN PACMAN----------------------

PACMAN.penup()
PACMAN.setposition(-200,0)
#-------------------Onkeypresses----------------------

wn.onkeypress(move_right, "d")
wn.onkeypress(move_up, "w")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_down, "s")
wn.listen()
wn.exitonclick()
wn.mainloop()