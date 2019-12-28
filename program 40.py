#program to draw a polygon with turtle(graphics).
import turtle

polygon=turtle.Turtle()

my_num_sides=int(input('enter the side-->'))
my_side_length=int(input('enter the length of the side >>'))
my_angle=360.0/my_num_sides

for i in range(my_num_sides):
    polygon.forward(my_side_length)
    polygon.right(my_angle)

turtle.done()