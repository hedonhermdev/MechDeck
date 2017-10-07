from vectors import *

origin = Vector(i=0, j=0)
g = Vector(i=0, j=-9.8)

t, x, y, s, v, a = sp.symbols('t x y  s v a')


class Body(object):
    """
    Base class for defining a body performing motion.
    """

    def __init__(self, name, position=origin, velocity=Vector(i=0, j=0), acceleration=Vector(i=0, j=0),
                 mass=None):
        self.name = name
        self.mass = mass
        self.position = position  # Initial position of body.
        self.velocity = velocity  # Initial velocity of body.
        self.acceleration = acceleration
        self.effective_velocity = self.velocity
        self.effective_acceleration = self.acceleration
        self.attrs = {}

    def relative_position(self, body2):
        return vector_diff(self.position, body2.position)

    def relative_velocity(self, body2):
        return vector_diff(self.velocity, body2.velocity)

    def relative_acceleration(self, body2):
        return vector_diff(self.acceleration, body2.acceleration)

    def restrict_motion_along(self, line_vector):
        # FIXME
        self.effective_acceleration = self.acceleration.component_along_vector(line_vector)
        self.effective_velocity = self.velocity.component_along_vector(line_vector)


class OneDMotionBody(Body):
    """
    Class for defining bodies performing one dimensional motion. 
    """

    def __init__(self, name, p=0, v=0, a=0, mass=0, **kwargs):
        Body.__init__(self, name=name, position=Vector(magnitude=p, angle=0), velocity=Vector(magnitude=v, angle=0),
                      acceleration=Vector(magnitude=a, angle=0), mass=mass)

    def motion_attr_func(self, **kwargs):
        attr_funcs = {}

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

        if 'velocity_position_function' in kwargs:
            attr_funcs['acceleration_position'] = None

        self.attrs = attr_funcs
        return attr_funcs


class ProjectileMotionBody(Body):
    def __init__(self, name, speed=0, angle=0, position=origin):
        Body.__init__(self, name=name, position=position, velocity=Vector(magnitude=speed, angle=angle), acceleration=g)
        self.attrs['sx-t'] = self.velocity.i * t
        self.attrs['sy-t'] = self.velocity.j * t + 0.5 * g.j * (t ** 2)  # s = ut + 1/2 at^2
        self.attrs['vx-t'] = self.velocity.i
        self.attrs['vy-t'] = self.velocity.j + g.j * t
        self.time_of_flight = 2 * self.velocity.j / abs(g.j)
        self.horizontal_range = self.velocity.i * self.time_of_flight
    def calc_position_at_time(self, time):
        x = self.attrs['sx-t'].subs(t, time)
        y = self.attrs['sy-t'].subs(t, time)
        return vector_add(Vector(i=x, j=y), self.position)
