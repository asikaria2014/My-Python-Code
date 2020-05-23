#ArrowDraw.py
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
#t.turtlecolor("blue")
t.pencolor("white")
drawing_length = 20
t.turtlesize(2,2,2)
def up():
    t.forward(50)
def left():
    t.left(15)
def right():
    t.right(15)
def widen():
    t.width(t.width() + 2)
def thinen():
    t.width(t.width() - 2)
def move(x, y):
    #t.penup()
    t.setpos(x, y)
    #t.pendown()
def redpen():
    t.pencolor("red")
def orangepen():
    t.pencolor("orange")
def yellowpen():
    t.pencolor("yellow")
def greenpen():
    t.pencolor("green")
def bluepen():
    t.pencolor("blue")
def purplepen():
    t.pencolor("purple")

turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(widen, "w")
turtle.onkeypress(thinen, "t")
turtle.onkeypress(redpen, "r")
turtle.onkeypress(orangepen, "o")
turtle.onkeypress(yellowpen, "y")
turtle.onkeypress(greenpen, "g")
turtle.onkeypress(bluepen, "b")
turtle.onkeypress(purplepen, "p")
turtle.listen()
turtle.onscreenclick(move)
