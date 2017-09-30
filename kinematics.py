from vectors import *
import sympy as sp

origin = Vector(i=0, j=0)
gravity = Vector(i=0, j=-9.8)

t, s, v, a = sp.symbols('t s v a')


class Body(object):
    """
    Base class for defining a body performing motion.
    """

    def __init__(self, name, position=Vector(i=0, j=0), velocity=Vector(i=0, j=0), acceleration=Vector(i=0, j=0),
                 mass=0):
        self.name = name
        self.mass = mass
        self.position = position  # Initial position of body.
        self.velocity = velocity  # Initial velocity of body.
        self.acceleration = acceleration
        self.attr_funcs = {}

    def relative_position(self, body2):
        return vector_diff(self.position, body2.position)

    def relative_velocity(self, body2):
        return vector_diff(self.velocity, body2.position)

    def relative_acceleration(self, body2):
        return vector_diff(self.acceleration, body2.acceleration)


class OneDMotionBody(Body):
    """
    Class for defining bodies performing one dimensional motion. 
    """

    def __init__(self, name, p_i=0, v_i=0, a_i=0, mass=0, **kwargs):
        Body.__init__(self, name=name, position=Vector(i=p_i, j=0), velocity=Vector(i=v_i, j=0),
                      acceleration=Vector(i=a_i, j=0), mass=mass)

    def motion_attr_func(self, **kwargs):
        attr_funcs = {
            'displacement_time': None,
            'velocity_time': None,
            'acceleration_time': None
        }
        if 'displacement_time_function' in kwargs:
            attr_funcs['displacement_time'] = kwargs['displacement_time_function']
            attr_funcs['velocity_time'] = sp.diff(attr_funcs['displacement_time'], t)
            attr_funcs['acceleration_time'] = sp.diff(attr_funcs['displacement_time'], t, t)
        if 'velocity_time_function' in kwargs:
            attr_funcs['velocity_time'] = kwargs['velocity_time_function']
            attr_funcs['acceleration_time'] = sp.diff(attr_funcs['velocity_time'], t)
            attr_funcs['displacement_time'] = sp.integrate(attr_funcs['velocity_time'], t)

        if 'acceleration_time_function' in kwargs:
            attr_funcs['acceleration_time'] = kwargs['acceleration_time_function']
            attr_funcs['velocity_time'] = sp.integrate(attr_funcs['acceleration_time'], t)
            attr_funcs['displacement_time'] = sp.integrate(attr_funcs['velocity_time'], t)
        self.attr_funcs = attr_funcs
        return attr_funcs
