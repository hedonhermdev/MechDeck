import kinematics as k
from mpmath import radians
import matplotlib.pyplot as plt
import numpy as np

proj = k.ProjectileMotionBody('Cannon', 100, radians(90))

tf = float(proj.time_of_flight)

time_range = np.linspace(0, tf, 1024)

position_arr = [proj.calc_position_at_time(t).magnitude for t in time_range]

plt.plot(time_range, position_arr)
plt.title("Position-Time Graph for %s" % proj.name)
plt.xlabel('Time')
plt.ylabel('Position')
#plt.savefig('x-t_graph.png')
plt.show()
