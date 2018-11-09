# ifs.py
# Draws a fractral using an iterated function system

import stddraw
import stdrandom
import random

# number of times to run the function
n = 100000

# define vertices of object, (cx[i], cy[i]) gives a vertex
# try different sets of vertices for different fractals

# triangle
cx = [0.000, 1.000, 0.500]
cy = [0.000, 0.000, 0.866]

# define initial x, y values for the point
x = 0.0
y = 0.0

# set scale of window
stddraw.setXscale(-0.1, 1.1)
stddraw.setYscale(-0.1, 1.1)

# set pen radius to smallest possible radius
stddraw.setPenRadius(0)

# run loop n times: choose a random vertex, draw a new point halfway
# between self and new vertex
# edit available choices to draw different fractals
vertex = [0, 1, 2]
for i in range(n):
    r = random.choice(vertex)
    x = (x + cx[r]) / 2.0
    y = (y + cy[r]) / 2.0
    stddraw.point(x, y)

# show the picture
stddraw.show()