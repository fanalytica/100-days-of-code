import turtle as t
import random

drawing = t.Turtle()
drawing.width(5)
drawing.speed(10)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0,90,180,270]


def random_walk(no_walks):
    for walk in range(no_walks):
        dir = random.choice(directions)
        color = random.choice(colors)
        drawing.color(color)
        drawing.setheading(dir)
        drawing.forward(20)

random_walk(50)

screen = t.Screen()
screen.exitonclick()