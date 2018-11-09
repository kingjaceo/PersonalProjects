# bouncing_ball.py
# Simulates and draws a bouncing ball stuck in the window
import stddraw
import stdrandom

x = stdrandom.uniformFloat(-1, 1)
y = stdrandom.uniformFloat(-1, 1)
vx = 0.0015
vy = 0.0023
r = .05

stddraw.setXscale(-1.1, 1.1)
stddraw.setYscale(-1.1, 1.1)

while True:
    if abs(x + vx) + r > 1.0:
        vx = -vx
    if abs(y + vy) + r > 1.0:
        vy = -vy
    x += vx
    y += vy

    stddraw.clear()
    stddraw.filledCircle(x, y, r)
    stddraw.show(0)