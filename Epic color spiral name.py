import tkinter as tk
import turtle
root = tk.Tk()
turtle.color("blue")
turtle.shape("turtle")
turtle.pencolor("blue")
turtle.speed(0)
sides = 6
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.Screen().bgcolor("black")
your_name = turtle.textinput("Enter your name","What is your name")
for x in range (0,200):
    turtle.pencolor(colors[ x % sides ])
    turtle.penup()
    turtle.forward(((x * 3 )/ sides) + x + 5)
    turtle.pendown()
    turtle.write(your_name, font = ("Comic Sans", int((x + 4) / 4), "bold") )
    turtle.left(360 / sides + 1)
    turtle.width(x*sides/100)
