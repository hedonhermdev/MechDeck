
# Classes for force, acceleration, velocity.
class Force:
    __slots__ = ['x', 'y', 'magnitude']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (self.x**2 + self.y**2)**(1/2)

class Acceleration:
    __slots__ = ['x', 'y', 'magnitude']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (self.x**2 + self.y**2)**(1/2)


class Velocity:
    __slots__ = ['x', 'y', 'magnitude']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (self.x**2 + self.y**2)**(1/2)


class Position:
    __slots__ = ['x', 'y', 'magnitude']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (self.x**2 + self.y**2)**(1/2)


g = Acceleration(0, -10)  # Gravitational acceleration


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
        disp_x = acceleration.x * (time ** 2) / 2
        disp_y = acceleration.y * (time ** 2) / 2
        self.position.x += disp_x
        self.position.y += disp_y
        self.position.magnitude = (self.position.x**2 + self.position.y**2)**(1/2)

    def accelerate(self, acceleration, time):
        self.velocity.x += acceleration.x * time
        self.velocity.y += acceleration.y * time

    def apply_force(self, force_list, time):
        f_net_x = sum([f.x for f in force_list])
        f_net_y = sum([f.y for f in force_list])
        self.acceleration.x = f_net_x/self.mass
        self.acceleration.y = f_net_y/self.mass
        self.acceleration.magnitude = (self.acceleration.x**2 + self.acceleration.y**2)**(1/2)
        self.displace_body(self.acceleration, time)
        self.displace_body(self.acceleration, time)

if __name__ == '__main__':
    body1 = Body('b1', 10, Velocity(0, 0), Acceleration(0, 0), Position(5, 0))
    forces = [Force(-1, -1), Force(1, -1)]
    body1.apply_force(forces, 1)
    print(body1.acceleration.magnitude, body1.position.x, body1.position.y)

