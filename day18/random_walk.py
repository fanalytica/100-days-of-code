import turtle as t
import random

drawing = t.Turtle()
drawing.width(5)
drawing.speed(10)
t.colormode(255)

def random_color() -> tuple [int,int,int]:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0,90,180,270]


def random_walk(no_walks):
    for walk in range(no_walks):
        dir = random.choice(directions)
        drawing.color(random_color())
        drawing.setheading(dir)
        drawing.forward(20)

random_walk(200)

screen = t.Screen()
screen.exitonclick()