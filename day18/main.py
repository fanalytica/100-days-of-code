import turtle

drawing = turtle.Turtle()
drawing.shape("arrow")
drawing.color("blue")

for _ in range(20):
    drawing.forward(10)
    drawing.up()
    drawing.forward(10)
    drawing.down()





screen = turtle.Screen()
screen.exitonclick()