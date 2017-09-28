import kinematics as k
import vectors as v
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['backend'] = "Qt4Agg"

vel = v.Vector(i=10, j=0)
body1 = k.Body('body1', k.origin, vel, v.Vector(i=100, j=0))

time = np.linspace(1, 10, 100)

pos = []


def calc_position(t):
    return body1.velocity.i * t + 0.5 * body1.acceleration.i * t**2

for t in time:
    position = calc_position(t)
    pos.append(position)
print(time)
print(pos)

plt.plot(time, pos, 'r--')
plt.xlabel('Time')
plt.ylabel('Position')
plt.savefig('foo.png')
#plt.show()
