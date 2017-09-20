from math import sqrt, atan, sin, cos


class Vector:
    """
    Base class for vector quantities like position, velocity, acceleration etc.
    """

    def __init__(self, **kwargs):
        x, y, magnitude, angle = None, None, None, None
        if 'x' in kwargs and 'y' in kwargs:
            print(kwargs)
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


def vector_add(*args):
    vx = 0
    vy = 0
    for v in args:
        vx += v.x
        vy += v.y
    return Vector(x=vx, y=vy)

