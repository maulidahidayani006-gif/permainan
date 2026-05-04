import turtle
import time
import math

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("heart")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(3)
pen.color("red")


# ANIMATION
def heart():
    pen.penup()
    pen.goto(-350, 0)
    pen.pendown()

    points = [
        (-300, 0), (-250, 0), (-220, 0),
        (-200, 60), (-180, -80), (-160, 100),
        (-140, 0), (-100, 0), (-50, 0),
        (-30, 40), (-10, -40), (10, 0),
        (350, 0)
    ]

    for x, y in points:
        pen.goto(x, y)
        time.sleep(0.5)


# FORM
def draw_teks_heart():
    pen.clear()
    pen.color("red")

    words = []

    # RUMUS
    for t in range(0, 360, 8):
        x = 16 * math.sin(math.radians(t)) ** 3
        y = (
            13 * math.cos(math.radians(t))
            - 5 * math.cos(math.radians(2 * t))
            - 2 * math.cos(math.radians(3 * t))
            - math.cos(math.radians(4 * t))
        )
        # SCALE
        x *= 18
        y *= 18

        words.append((x, y))

    # TAMPILAN
    for x, y in words:
        pen.penup()
        pen.goto(x, y)
        pen.write(
            "I Love You",
            align="center",
            font=("Arial", 10, "bold")
        )
        time.sleep(0.10)

    # MIDDLE
    pen.goto(0, -20)
    pen.color("red")
    pen.write(
        "I LOVE YOU",
        align="center",
        font=("Arial", 28, "bold")
    )


heart()
time.sleep(1)
draw_teks_heart()

turtle.done()