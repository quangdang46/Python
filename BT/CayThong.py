import turtle
import random

bg = turtle.Screen()
bg.bgcolor("dark blue")

ornament_list = ["light blue", "maroon", "purple", "silver", "white", "yellow", "magenta"]


def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(100)

tina.penup()
tina.goto(0, 0)
tina.color("green")
tina.begin_fill()
tina.fillcolor("green")
tina.pensize(8)
tina.pendown()
tina.goto(100, 0)
tina.penup()
tina.end_fill()

tina.goto(100, 0)
tina.pendown()
tina.color("green")
tina.begin_fill()
tina.fillcolor("green")
tina.goto(0, 75)
tina.goto(-100, 0)
tina.forward(100)
tina.goto(125, -65)
tina.goto(-125, -65)
tina.goto(0, 0)
tina.penup()
tina.end_fill()

tina.goto(0, 75)
tina.pendown()
tina.color("green")
tina.begin_fill()
tina.fillcolor("green")
tina.goto(50, 75)
tina.goto(0, 120)
tina.goto(-50, 75)
tina.goto(0, 75)
tina.penup()
tina.end_fill()

tina.goto(0, -90)
tina.pendown()
tina.color("brown")
tina.begin_fill()
tina.fillcolor("brown")
tina.goto(20, -90)
tina.left(90)
tina.forward(20)
tina.left(90)
tina.forward(40)
tina.left(90)
tina.forward(20)
tina.left(90)
tina.forward(20)
tina.penup()
tina.end_fill()

for i in range(18):
    tina.penup()
    x = random.randint(-75, 75)
    y = random.randint(-65, 120)
    size = random.randint(1, 10)
    colors = (random.choice(ornament_list))
    tina.goto(x, y)
    tina.pendown()
    draw_circle(tina, colors, size, x, y)
    tina.penup()

    tina.goto(250, -250)

turtle.mainloop()
