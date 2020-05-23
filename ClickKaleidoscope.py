#ClickKaleidoscope.py
import random
import turtle
t = turtle.Pen()
angle = t.heading()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", 
          "white", "gray"]
def draw_kaleido(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    sides = random.randint(3,9)        
    thick = random.randint(1,6)         
    t.width(thick)
    angle = t.heading()
    angle = t.heading()
    draw_spiral(x,y, size)
    draw_spiral(-x,y, size)   
    draw_spiral(-x,-y, size)
    draw_spiral(x,-y, size)
def draw_spiral(x,y, size):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.setheading(180-angle)
    for m in range(size):
        t.forward(m*2)
        t.left(92)
turtle.onscreenclick(draw_kaleido)

