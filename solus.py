import turtle

# set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

#creat a turtle for drawing
pen = turtle.Turtle()
pen.speed(1000)
pen.color("red")

# function to draw a flower
def draw_flower():
    for _ in range(36):
        pen.begin_fill()
        pen.circle(100,60)
        pen.left(120)
        pen.circle(100,60)
        pen.end_fill()
        pen.left(10)

        # pen.forward(50)
        # pen.right(45)
        # pen.forward(50)
        # pen.right(135)
        # pen.forward(50)
        # pen.right(45)
        # pen.right(50)
        # pen.right(170)

# move the turtle to a center of the screen
pen.penup()
pen.goto(0, -150)
pen.pendown()

# draw the bigger flower
draw_flower()

# # move the turtle to another position
# pen.penup()
# pen.goto(100, 0)
# pen.pendown()

# draw the second flower
#draw_flower()

# move the turtle to write the text
pen.penup()
pen.goto(0, -50)
pen.pendown()
pen.color("gold")
pen.write("HANI BOY", align="center", font=("Arial", 24, "bold"))

# hide the turtle and display the result
pen.hideturtle()
turtle.done()

