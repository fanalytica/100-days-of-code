import turtle
import random

drawing = turtle.Turtle()
drawing.shape("arrow")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for side in range(num_sides):
        drawing.right(angle)
        drawing.forward(100)

for shape_side_n in range(3,11):
    drawing.color(random.choice(colors))
    draw_shape(shape_side_n)



screen = turtle.Screen()
screen.exitonclick()