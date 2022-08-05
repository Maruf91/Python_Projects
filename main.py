import random
import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

colors = ["medium spring green","orange","medium slate blue","magenta","cyan"]
def st_line():
    for _ in range(10):
        t.color("red")
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()


def shape_draw(side):
    angle = 360/side
    for _ in range(side):
        st_line()
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    tim.width(3)
    shape_draw(shape_side)

screen = t.Screen()
screen.exitonclick()


