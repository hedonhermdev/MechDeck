from sympy import *
from mpmath import *


def dot_product(vector1, vector2):
    return (vector1.x * vector2.x) + (vector1.y * vector2.y)


class Vector:
    """
    Base class for 2d vectors and vector quantities like position, velocity, acceleration etc.
    """
    def __init__(self, **kwargs):
        i, j, magnitude, angle = None, None, None, None
        if 'i' in kwargs and 'j' in kwargs:
            i = kwargs['i']
            j = kwargs['j']
            magnitude = sqrt(i ** 2 + j ** 2)
            if i != 0:
                angle = atan2(j, i)
            else:
                angle = pi / 2
        elif 'magnitude' in kwargs and 'angle' in kwargs:
            magnitude, angle = kwargs['magnitude'], kwargs['angle']
            i = magnitude * cos(angle)
            j = magnitude * sin(angle)
        attrs = {'i': i, 'j': j, 'magnitude': magnitude, 'angle': angle}
        self.__dict__.update(attrs)

    def unit_vector(self):
        return Vector(i=(self.x/self.magnitude), j=(self.y/self.magnitude))

    def multiply_with_scalar(self, scalar):
        self.i *= scalar
        print('i', self.i)
        self.j *= scalar
        print('j', self.j)

    def orthogonal_component_vector(self, vector_2):
        xv = self.i
        yv = self.j
        print(xv, yv)
        if vector_2 == 'x':
            return Vector(x=xv, y=0)
        elif vector_2 == 'y':
            return Vector(x=0, y=yv)

    def component_on_vector(self, vector2):
        a_, b_ = self.unit_vector(), vector2.unit_vector()
        magnitude = dot_product(a_, b_)
        b_.multiply_with_scalar(magnitude)
        return b_


i_ = Vector(x=1, y=0)  # Unit vector in +ve x direction.
j_ = Vector(x=0, y=1)  # Unit vector in +ve y direction.


def vector_add(*vectors):
    vx = 0
    vy = 0
    for v in vectors:
        if isinstance(v,Vector):
            vx += v.i
            vy += v.j
        else:
            print("The method vector_add can only add vectors.")
    return Vector(i=vx, j=vy)


def vector_diff(*vectors):
    if isinstance(vectors[1], Vector):
        vr = vectors[0]
        for v in vectors[1:]:
            if isinstance(v, Vector):
                v.multiply_with_scalar(-1)
                vr = vector_add(vr, v)
            return vr


# For pretty printing
mp.dps = 15
mp.pretty = True
