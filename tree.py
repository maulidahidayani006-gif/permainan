import turtle
import random

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.title("Fractal Tree Python")
screen.tracer(2, 25)  

# Turtle untuk pohon
tree = turtle.Turtle()
tree.speed(0)
tree.left(90)
tree.penup()
tree.goto(0, -300)
tree.pendown()
tree.hideturtle()

# Turtle untuk salju
snow = turtle.Turtle()
snow.hideturtle()
snow.penup()
snow.speed(0)

# Fungsi warna random untuk bunga/buah
def random_color():
    colors = ["red", "yellow", "blue", "green", "orange", "cyan", "magenta"]
    return random.choice(colors)

# Fungsi gambar salju
def draw_snow():
    for _ in range(150):
        x = random.randint(-450, 450)
        y = random.randint(-350, 350)
        size = random.randint(2, 5)
        snow.goto(x, y)
        snow.dot(size, "white")

# Fungsi gambar pohon
def draw_tree(branch_lenght):
    if branch_lenght > 8:
        if branch_lenght > 40:
            tree.pencolor("red")
            tree.pensize(branch_lenght / 10)
        elif branch_lenght > 20:
            tree.pencolor("orange")
            tree.pensize(branch_lenght / 15)
        else:
            tree.pencolor("lightgreen")
            tree.pensize(2)

        tree.forward(branch_lenght)
        angle = random.randint(15, 30)

        tree.right(angle)
        draw_tree(branch_lenght - random.randint(10, 15))

        tree.left(angle * 2)
        draw_tree(branch_lenght - random.randint(10, 15))

        tree.right(angle)
        tree.backward(branch_lenght)
    else:
        tree.dot(8, random_color())

draw_snow()

draw_tree(100)

turtle.done()
input("Tekan Enter untuk keluar ...")