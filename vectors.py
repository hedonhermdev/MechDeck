from sympy import *
from mpmath import *

# Fro pretty printing
mp.dps = 15
mp.pretty = True


class Vector:
    """
    Base class for vector quantities like position, velocity, acceleration etc.
    """

    def __init__(self, **kwargs):
        x, y, magnitude, angle = None, None, None, None
        if 'x' in kwargs and 'y' in kwargs:
            x = kwargs['x']
            y = kwargs['y']
            magnitude = sqrt(x ** 2 + y ** 2)
            angle = atan(y / x)
        elif 'magnitude' in kwargs and 'angle' in kwargs.items():
            magnitude, angle = kwargs['magnitude'], kwargs['angle']
            x = magnitude * cos(angle)
            y = magnitude * sin(angle)
        attrs = {'x': x, 'y': y, 'magnitude': magnitude, 'angle': angle}
        self.__dict__.update(attrs)

    def multiply_with_scalar(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.magnitude *= scalar

    def parallel_unit_vector(self):
        return Vector(x = cos(self.angle), y= sin(self.angle))


# Vector operations.
def vector_add(*args):
    vx = 0
    vy = 0
    for v in args:
        vx += v.x
        vy += v.y
    return Vector(x=vx, y=vy)


def dot_product(vector1, vector2):
    return vector1.x * vector2.x + vector1.y + vector2.y


