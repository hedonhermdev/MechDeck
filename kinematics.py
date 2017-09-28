from quantities import *
from vectors import *

# from sympy import symbols

origin = Vector(i=0, j=0)
gravity = Vector(i=0, j=-9.8)


# time, position, displacement, velocity, acceleration = symbols('t x s v a')


class Body(object):
    def __init__(self, name=None, position=Vector(i=0, j=0), velocity=Vector(i=0, j=0), acceleration=Vector(i=0, j=0),
                 mass=0):
        self.name = name
        self.mass = mass
        self.position = position  # Initial position of body.
        self.velocity = velocity  # Initial velocity of body.
        self.acceleration = acceleration

    def relative_position(self, body2):
        return vector_diff(self.position, body2.position)

    def relative_velocity(self, body2):
        return vector_diff(self.velocity, body2.position)

    def relative_acceleration(self, body2):
        return vector_diff(self.acceleration, body2.acceleration)
