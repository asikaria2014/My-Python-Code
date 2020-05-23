import tkinter as tk
import turtle
root = tk.Tk()
turtle.color("blue")
turtle.shape("turtle")
turtle.pensize(10)
turtle.pencolor("blue")
turtle.speed(0)
turtle.Screen().bgcolor("red")





def sfv():
    turtle.right(30)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(30)

def sfa():
    for z in range(0, 4):
        turtle.forward(90)
        sfv()
        turtle.backward(30)
    turtle.backward(240)
        
def sf():
    for k in range(0, 360):
        sfa()
        turtle.right(1)
sf()
    

    
    
    


