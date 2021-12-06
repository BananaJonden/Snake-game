'''
Instructions:

Click Run!
'''

#Ghost Template:
#   a115_ghost_maze.py
import turtle as trtl
import random as rand

trtl.speed(0)
wn = trtl.Screen()
wn.bgcolor("black")
#-------------------maze and turtle config variables-----------------
screen_h = 400
screen_w = 420
startx = 0
starty = 0
turtle_scale = 1.5

#---------------------------GHOST COMMANDS---------------------------
#------ red ghost commands

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
PACMAN_UP = trtl.Turtle(shape=pac_up)
PACMAN.color("white")


#create dotmaker2000
dot = "dot.gif"
trtl.addshape(dot)
DOT = trtl.Turtle(shape=dot)

#===========================DRAW DOTS==========================
pacman_pos = [] # array of tuples representing all of pacmans positions. Ghosts will follow this.
collision_length = 10

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

def ghost_path_one(ghost, offset=0):
    ghost.setheading(0)
    ghost_tp(-200 - offset, 0, ghost)
    ghost_jump(115 + offset, ghost)
    ghost.left(90)
    ghost_jump(160, ghost)
    ghost.right(90)
    ghost_jump(245, ghost)
    ghost.right(90)
    ghost_jump(70, ghost)
    ghost.left(90)
    ghost_jump(60, ghost)

def ghost_tp(x, y, ghost):
  ghost.penup()
  ghost.speed(4)
  ghost.setpos(x, y)
  ghost.pendown()
  
def ghost_jump(distance, ghost):
    ghost.penup()

    for i in range(int(distance/2)):
      ghost.forward(2)

    ghost.pendown()

#--------------------pacman jumps---------------------
def pac_jump(distance, ghost, pos):
    PACMAN.speed(0)
    PACMAN.penup()

    for i in range(int(distance/2)):
        pacman_pos.append((PACMAN.xcor()-20, PACMAN.ycor()))

        if i % 10 >= 4:
            PACMAN.shape(pac_open)
        elif i % 10 <= 5:
            PACMAN.shape(pac_closed)
        PACMAN.forward(2)

        for dot in dots:
          if abs(PACMAN.xcor() - dot.xcor()) <= collision_length and abs(PACMAN.ycor() - dot.ycor()) <= collision_length:
            dot.hideturtle()

        pos += 1

          
    PACMAN.pendown()

    return pos

def pac_up_jump(distance, ghost, pos):
    PACMAN.speed(0)
    PACMAN.penup()

    for i in range(int(distance/2)):
        pacman_pos.append((PACMAN.xcor(), PACMAN.ycor()-20))

        if i % 10 >= 4:
            PACMAN.shape(pac_up)
        elif i % 10 <= 5:
            PACMAN.shape(pac_up_closed)
        PACMAN.forward(2)

        for dot in dots:
          if abs(PACMAN.xcor() - dot.xcor()) <= collision_length and abs(PACMAN.ycor() - dot.ycor()) <= collision_length:
            dot.hideturtle()

        pos += 1

          
    PACMAN.pendown()

    return pos

def pac_down_jump(distance, ghost, pos):
    PACMAN.speed(0)
    PACMAN.penup()

    for i in range(int(distance/2)):
        pacman_pos.append((PACMAN.xcor(), PACMAN.ycor()+20))

        if i % 10 >= 4:
            PACMAN.shape(pac_down)
        elif i % 10 <= 5:
            PACMAN.shape(pac_down_closed)
        PACMAN.forward(2)

        for dot in dots:
          if abs(PACMAN.xcor() - dot.xcor()) <= collision_length and abs(PACMAN.ycor() - dot.ycor()) <= collision_length:
            dot.hideturtle()

        pos += 1

          
    PACMAN.pendown()

    return pos

def pac_tp(x, y):
    PACMAN.penup()
    PACMAN.hideturtle()
    PACMAN.setpos(x, y)
    PACMAN.showturtle()
    PACMAN.pendown()

def move_right():
    PACMAN.setheading(0)
    PACMAN.forward(25)


def move_up():
    PACMAN.setheading(90)
    PACMAN.forward(25)


def move_left():
    PACMAN.setheading(180)
    PACMAN.forward(25)


def move_down():
    PACMAN.setheading(270)
    PACMAN.forward(25)


#------------------Pacman paths--------------------
# Goes from left to right exits FINISHED
'''
def path_one(pos):
    PACMAN.setheading(0)    
    pac_tp(-200, 0)
    pos = pac_jump(115, blinky, pos)
    PACMAN.left(90)
    pos = pac_up_jump(160, blinky, pos)
    PACMAN.right(90)
    pos = pac_jump(248.5,blinky, pos)
    PACMAN.right(90)
    pos = pac_down_jump(70, blinky, pos)
    PACMAN.left(90)
    pos = pac_jump(62.5,blinky, pos)

    return pos

#Left hole to bottom hole
def path_two(pos):
    PACMAN.setheading(0)
    pac_tp(-200, 0)
    pos = pac_jump(115, blinky, pos)
    PACMAN.right(90)
    pos = pac_down_jump(160, blinky, pos)
    PACMAN.left(90)
    pos = pac_jump(60, blinky, pos)
    PACMAN.left(90)
    pos = pac_up_jump(75, blinky, pos)
    PACMAN.right(90)
    pos = pac_jump(130, blinky, pos)
    PACMAN.left(90)
    pos = pac_up_jump(245, blinky, pos)
    PACMAN.right(90)
    pac_jump(58, blinky, pos)
    PACMAN.right(90)
    pos = pac_down_jump(370, blinky, pos)

    return pos


# Goes from entrance but takes snakey path to right exit

def path_three(pos):
    PACMAN.setheading(0)
    pac_tp(-200, 0)
    pos = pac_jump(115, blinky, pos)
    PACMAN.left(90)
    pos = pac_up_jump(20, blinky, pos)
    PACMAN.right(90)
    pos = pac_jump(60, blinky, pos)
    PACMAN.left(90)
    pos = pac_up_jump(140, blinky, pos)
    PACMAN.right(90)
    pos = pac_jump(185, blinky, pos)
    PACMAN.right(90)
    pos = pac_down_jump(70, blinky, pos)
    PACMAN.left(90)
    pos = pac_jump(65, blinky, pos)

    return pos


def path_four(pos):
    PACMAN.setheading(0)
    pac_tp(160, -210)
    PACMAN.left(90)
    pos = pac_up_jump(370, blinky, pos)
    PACMAN.left(90)
    pos = pac_jump(245, blinky, pos)
    PACMAN.left(90)
    pos = pac_down_jump(140, blinky, pos)
    PACMAN.left(90)
    pos = pac_jump(55, blinky, pos)
    PACMAN.right(90)
    pos = pac_down_jump(180, blinky, pos)
    PACMAN.right(90)
    pos = pac_jump(55, blinky, pos)
    PACMAN.right(90)
    pos = pac_up_jump(160, blinky, pos)
    PACMAN.left(90)
    pos = pac_jump(120, blinky, pos)

    return pos
'''
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
  ghost_tp(37.5, 26, pinky)
  pinky.stamp()
  ghost_tp(37.5, 49.5, clyde)
  clyde.stamp()
  ghost_tp(37.5, 75, blinky)
  blinky.stamp()

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





#===========================DRAW BOXES==========================
init_boxes()
inky.showturtle()
blinky.showturtle()
clyde.showturtle()
pinky.showturtle()
startghosts()
#--------------------MAIN PACMAN/GHOST LOOP----------------------
last = 0
'''
while True:
  num = rand.randrange(1, 4)
  #num =2
  while num == last:
    num = rand.randrange(1, 4)

  last = num
  if num == 1:
    print("Path one")
    pos = path_one(pos)
  elif num == 2:
    print("Path two")
    pos = path_two(pos)
  elif num == 3:
    print("Path three")
    pos = path_three(pos)
  elif num == 4:
    print("Path four")
    pos = path_four(pos)

  for dot in dots:
    if dot.isvisible():
      continue

    dot.showturtle()

  pos = 0
  pacman_pos.clear()

'''
wn.onkeypress(move_right, "d")
wn.onkeypress(move_up, "w")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_down, "s")
wn.listen()
wn.exitonclick()
wn.mainloop()