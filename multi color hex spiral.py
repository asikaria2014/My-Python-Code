import tkinter as tk
import turtle
root = tk.Tk()
turtle.color("blue")
turtle.shape("turtle")
turtle.pencolor("blue")
turtle.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.Screen().bgcolor("black")
for x in range (0,1250):
    turtle.pencolor(colors[ x % 6 ])
    turtle.forward(x)
    turtle.left(61)
