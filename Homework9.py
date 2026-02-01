import turtle
my_wn = turtle.Screen().bgcolor("Cyan")
my_wn = turtle.Screen().screensize(700, 700)
square = turtle.Turtle()
num_sides = 4
side_length = 320
angle = 320 / num_sides
for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)