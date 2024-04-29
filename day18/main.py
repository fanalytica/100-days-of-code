import turtle

drawing = turtle.Turtle()
drawing.shape("arrow")
drawing.color("blue")

for sides in range(3,20):
    angle = 360/sides
    for side in range(sides):
        drawing.right(angle)
        drawing.forward(100)





screen = turtle.Screen()
screen.exitonclick()