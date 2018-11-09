# universe.py
from vector import Vector
from body import Body
from picture import Picture
import stddraw
from instream import InStream


class Universe:
    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.readInt()
        r = instream.readFloat()
        stddraw.setXscale(-r, r)
        stddraw.setYscale(-r, r)
        self._bodies = []
        for i in range(n):
            rx = instream.readFloat()
            ry = instream.readFloat()
            vx = instream.readFloat()
            vy = instream.readFloat()
            mass = instream.readFloat()
            name = instream.readString()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            b = Body(r, v, mass, name)
            print('Body created!')
            self._bodies.append(b)

    def increase_time(self, dt):
        net_forces = []
        for b in self._bodies:
            bodies = self._bodies[:]
            net_force = Vector([0, 0])
            bodies.remove(b)
            for other in bodies:
                net_force = net_force + b.force_from(other)
            net_forces.append(net_force)

        for i in range(len(self._bodies)):
            self._bodies[i].move(net_forces[i], dt)

    def draw(self):
        for b in self._bodies:
            b.draw()

# some options: 8star-rotation.txt, binaryStars.txt, planets.txt, or anything in space_files
# space_files data provided by Robert Sedgewick, Kevin Wayne, and Robert Dondero from their book Introduction to Programming with Python
universe = Universe('space_files\\binaryStars.txt')

# adjust dt to adjust speed of simulation
t = 0
dt = 10000
T = 100000
while True:
    universe.increase_time(dt)
    stddraw.clear()
    stddraw.picture(Picture('space_files\\starfield.jpg'), 0, 0)
    universe.draw()
    stddraw.show(1)
    t += dt

