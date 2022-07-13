import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red', 'green', 'blue', 'yellow', 'orange', 'grey', 'purple', 'pink'])


# this is for defining how the shapes are supposed to be formed
def circle(size, angle, forw):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(forw)
    circle(size + 5, angle + 1, forw + 5)  # the is the recursion effect of calling a function in a function


t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle(50, 40, 0)

ti.sleep(2)
t.hideturtle()
