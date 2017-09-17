# Classes for force, acceleration, velocity.
class Force:
    __slots__ = ['x', 'y', 'magnitude']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (self.x ** 2 + self.y ** 2) ** (1 / 2)


class Acceleration:
    __slots__ = ['x', 'y', 'magnitude']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (self.x ** 2 + self.y ** 2) ** (1 / 2)


class Velocity:
    __slots__ = ['x', 'y', 'magnitude']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (self.x ** 2 + self.y ** 2) ** (1 / 2)


class Position:
    __slots__ = ['x', 'y', 'magnitude']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (self.x ** 2 + self.y ** 2) ** (1 / 2)


# Class for defining a body.
class Body(object):
    def __init__(self, name, mass, velocity, acceleration, position):
        self.name = name
        self.mass = mass
        self.position = position
        self.acceleration = acceleration
        self.velocity = velocity
        self.forces = []

    def displace_body(self, acceleration, time):
        disp_x = (self.velocity.x * time) + (acceleration.x * (time**2)/2)
        disp_y = (self.velocity.y * time) + (acceleration.y * (time**2)/2)
        self.position.x += disp_x
        self.position.y += disp_y
        self.position.magnitude = (self.position.x ** 2 + self.position.y ** 2) ** (1 / 2)
        return disp_x, disp_y

    def accelerate(self, acceleration, time):
        self.velocity.x += acceleration.x * time
        self.velocity.y += acceleration.y * time

    def apply_force(self, force_list, time):
        f_net_x = sum([f.x for f in force_list])
        f_net_y = sum([f.y for f in force_list])
        self.acceleration.x = f_net_x / self.mass
        self.acceleration.y = f_net_y / self.mass
        self.acceleration.magnitude = (self.acceleration.x ** 2 + self.acceleration.y ** 2) ** (1 / 2)
        self.displace_body(self.acceleration, time)
        self.accelerate(self.acceleration, time)

