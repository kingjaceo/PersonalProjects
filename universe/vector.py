# vector.py
# used in universe.py
import math
import stdarray


class Vector:
    def __init__(self, a):
        # a[:] makes a 'defensive copy' of the array a
        self._coords = a[:]  # coordinates of the vector
        self._n = len(a)  # dimension of the vector

    # Adds one vector (other) to the vector (self)
    def __add__(self, other):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] + other._coords[i]
        return Vector(result)

    # Subtracts one vector (other) from the vector (self)
    def __sub__(self, other):
        return self.__add__(other.scale(-1))

    def __neg__(self):
        return self.scale(-1)

    # Returns the dot product of two vectors
    def dot(self, other):
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    # Returns a scaled version of the vector
    def scale(self, alpha):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] * alpha
        return Vector(result)

    # Returns a unit vector pointing in the direction of the vector
    def direction(self): return self.scale(1.0 / abs(self))

    # Returns the ith coordinate of the vector
    def __getitem__(self, i): return self._coords[i]

    # Return the magnitude of the vector
    def __abs__(self): return math.sqrt(self.dot(self))

    # Returns the dimension of the vector
    def __len__(self): return self._n

    # Returns string representation of vector
    def __str__(self): return str(self._coords)