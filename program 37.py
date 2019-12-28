#program to make star sprial with turtle(graphics)
import turtle

spiral=turtle.Turtle()

for i in range(50):
    spiral.forward(i*10)
    spiral.right(144)

turtle.done()