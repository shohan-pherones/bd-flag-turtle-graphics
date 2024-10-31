import turtle

screen = turtle.Screen()
screen.title("Flag of Bangladesh")
screen.setup(width=800, height=500)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)

def draw_rectangle():
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.color("#006a4e")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

def draw_circle():
    t.penup()
    t.goto(0, -60)
    t.pendown()
    t.color("#f42a41")
    t.begin_fill()
    t.circle(60)
    t.end_fill()

draw_rectangle()
draw_circle()

t.hideturtle()
turtle.done()