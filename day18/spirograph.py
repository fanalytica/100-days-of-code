import turtle as t
import random

drawing = t.Turtle()
drawing.speed('fastest')
t.colormode(255)
# drawing.shape('circle')
# drawing.shapesize(5,5)
RADIUS = 40

def random_color() -> tuple [int,int,int]:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b


def draw_spirograph(no_circles):
    angle = 360/no_circles
    for circle in range(no_circles):
        drawing.color(random_color())
        drawing.circle(radius=RADIUS)
        drawing.setheading(angle*circle)

draw_spirograph(40)

screen = t.Screen()
screen.exitonclick()