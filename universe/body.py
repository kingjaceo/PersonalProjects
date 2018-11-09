# body.py
# Used by universe.py
import stddraw
import vector
from picture import Picture


class Body:

    # Construct a new Body object whose position is given
    # by the Vector object r, whose velocity is given by the
    # Vector object v, and whose mass is given by mass.
    def __init__(self, r, v, mass, name=None, radius=0.0125):
        self._r = r         # Position
        self._v = v         # Velocity
        self._mass = mass   # Mass
        self._name = name
        self._radius = radius # Radius

    # Move self by applying the force specified by the Vector
    # object f for the number of seconds specified by the float
    # dt.
    def move(self, f, dt):
        a = f.scale(1.0 / self._mass) # acceleration (Vector object)
        self._v = self._v + (a.scale(dt))
        self._r = self._r + (self._v.scale(dt))

    # Return the force between Body objects self and other
    def force_from(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magnitude)

    # Draw self to canvas
    def draw(self):
        location = 'space_files\\' + self._name
        stddraw.picture(Picture(location), self._r[0], self._r[1])
        stddraw.point(self._r[0], self._r[1])

def _main():
    earth = Body(vector.Vector([5, 5]), vector.Vector([0, 1]), 12)
    print(earth._r[0])
    stddraw.setXscale(0, 10)
    stddraw.setYscale(0, 10)
    earth.draw()
    stddraw.show()


if __name__ == '__main__':
	main()