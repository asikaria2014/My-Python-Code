import tkinter as tk
import turtle
root = tk.Tk()
turtle.color("red")
turtle.shape("turtle")
turtle.pencolor("red")
turtle.speed(0)
#turtle.Screen().bgcolor("red")
for x in range (0,800):
    turtle.circle(x)
    turtle.left(91)
