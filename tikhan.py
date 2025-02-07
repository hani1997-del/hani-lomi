import math
import turtle

t = turtle.Turtle()
turtle.speed(15000)
turtle.bgcolor("black")

def corazon(k):
    return 15 * math.sin(k) ** 3

def corazon1(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

for i in range(600):
    t.goto(corazon1(i) * 20, corazon(i) * 20)
    for j in range(5):
        t.color('red')


t.color("gold")
t.penup()
t.goto(0, 0)
t.pendown()
t.write("I LOVE YOU", align="center", font=("arial", 30, "bold"))

t.hideturtle()
turtle.done()
