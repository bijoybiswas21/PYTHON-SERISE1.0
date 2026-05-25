import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("lightblue")
screen.title("Lord Ganesh Sketch")

# Create turtle object
pen = turtle.Turtle()
pen.speed(0)

def draw_circle(x, y, radius, color, fill=True):
    """Draw a filled circle"""
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
    pen.circle(radius)
    if fill:
        pen.end_fill()

# Draw Ganesh body parts

# Head (circle)
draw_circle(0, 100, 80, "yellow", True)

# Left Ear
draw_circle(-60, 160, 35, "yellow", True)

# Right Ear
draw_circle(60, 160, 35, "yellow", True)

# Body (rectangle-like)
pen.penup()
pen.goto(-50, 20)
pen.pendown()
pen.color("orange")
pen.pensize(2)
pen.begin_fill()
for _ in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(120)
    pen.right(90)
pen.end_fill()

# Left Arm circle
draw_circle(-80, 50, 30, "yellow", True)
pen.penup()
pen.goto(-80, 50)
pen.pendown()
pen.color("black")
pen.pensize(3)
pen.goto(-120, 30)

# Right Arm circle
draw_circle(80, 50, 30, "yellow", True)
pen.penup()
pen.goto(80, 50)
pen.pendown()
pen.color("black")
pen.pensize(3)
pen.goto(120, 30)

# Left Leg circle
draw_circle(-50, -100, 25, "yellow", True)
pen.penup()
pen.goto(-50, -60)
pen.pendown()
pen.color("black")
pen.pensize(3)
pen.goto(-50, -130)

# Right Leg circle
draw_circle(50, -100, 25, "yellow", True)
pen.penup()
pen.goto(50, -60)
pen.pendown()
pen.color("black")
pen.pensize(3)
pen.goto(50, -130)

# Trunk (curved)
pen.penup()
pen.goto(20, 50)
pen.pendown()
pen.color("black")
pen.pensize(8)
pen.setheading(270)
pen.circle(30, 180)
pen.circle(20, 180)

# Eyes
draw_circle(-25, 120, 8, "black", True)
draw_circle(25, 120, 8, "black", True)

# Nose
pen.penup()
pen.goto(0, 100)
pen.pendown()
pen.color("black")
pen.pensize(3)
pen.goto(0, 85)

# Mouth (smile)
pen.penup()
pen.goto(-20, 80)
pen.pendown()
pen.color("black")
pen.pensize(2)
pen.setheading(0)
pen.circle(20, 180)

# Tilak (mark on forehead)
draw_circle(0, 150, 5, "red", True)

# Crescent on head
pen.penup()
pen.goto(0, 180)
pen.pendown()
pen.color("gold")
pen.pensize(3)
pen.setheading(0)
pen.circle(15, 180)

# Add some decorative dots
pen.pensize(2)
pen.color("red")
for x in range(-60, 70, 30):
    draw_circle(x, -140, 3, "red", True)

pen.hideturtle()
turtle.done()
