import tkinter as tk
import turtle
root = tk.Tk()
turtle.color("blue")
turtle.shape("turtle")
turtle.pencolor("blue")
turtle.speed(0)
turtle.Screen().bgcolor("red")
for x in range (0,800):
    turtle.forward(x)
    turtle.left(90)
