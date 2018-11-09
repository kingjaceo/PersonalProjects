# sin_wave.py
# drawing a simple trig function with stddraw
import stddraw
import math

sample = 20000
x0 = 0
y0 = 0

stddraw.setXscale(-0.5, 2 * math.pi + 0.5)
stddraw.setYscale(-2.5,2.5)

for n in range(sample):
    x = ((n - 1) * 2 * math.pi) / sample
    y = math.sin(4*x) + math.sin(20*x)
    stddraw.line(x0, y0, x, y)
    x0 = x
    y0 = y

stddraw.show()