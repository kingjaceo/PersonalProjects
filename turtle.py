# turtle.py
# classic turtle graphics
import stddraw
import math


class Turtle:
    # Create a turtle at (x, y) facing angle degrees counter-clockwise
    # from the x-axis.
    def __init__(self, x, y, angle):
        self._x = x
        self._y = y
        self._angle = angle

    # Rotate self counter-clockwise by delta degrees.
    def turn_left(self, delta):
        self._angle += delta

    # Move self forward. Distance = step. Draw a line tracing
    # the path.
    def go_forward(self, step):
        oldx = self._x
        oldy = self._y
        self._x += step * math.cos(math.radians(self._angle))
        self._y += step * math.sin(math.radians(self._angle))
        stddraw.line(oldx, oldy, self._x, self._y)


# Create a Turtle object and use to draw polygons.
def main():
    n = 1000
    t = Turtle(0.5, 0, 180 / n)
    step_size = math.sin(math.radians(180 / n))
    for i in range(n):
        t.go_forward(step_size)
        t.turn_left(360 / n)
        stddraw.show(10)
    stddraw.show()

if __name__ == '__main__':
    main()
