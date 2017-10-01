import kinematics as k
import vectors as v
import sympy as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

vel = v.Vector(i=10, j=0)
body1 = k.OneDMotionBody('body1', 10)

body1.motion_attr_func(displacement_time_function=(k.t**3)/3)

print(body1.attr_funcs)


def calc_position_at_time(time):
    return body1.attr_funcs['displacement_time'].subs(k.t, time)


def calc_velocity_at_time(time):
    return body1.attr_funcs['velocity_time'].subs(k.t, time)


def calc_acceleration_at_time(time):
    return body1.attr_funcs['acceleration_time'].subs(k.t, time)


time_arr = np.linspace(0, 100, 100)

disp_arr = []
for time in time_arr:
    d = body1.position.i + calc_position_at_time(time)
    disp_arr.append(d)

print(disp_arr)

vel_arr = []
for time in time_arr:
    v = calc_velocity_at_time(time)
    vel_arr.append(v)

print(vel_arr)

acc_arr = []
for time in time_arr:
    a = calc_acceleration_at_time(time)
    acc_arr.append(a)

print(acc_arr)

# Position-Time graph
plt.plot(time_arr, disp_arr)
plt.xlabel('Time')
plt.ylabel('Position')
plt.savefig('x-t_graph.png')
plt.show()

#Velocity-Time graph
plt.plot(time_arr, vel_arr)
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.savefig('v-t_graph.png')
plt.show()

#Acceleration-Time graph
plt.plot(time_arr, acc_arr)
plt.xlabel('Time')
plt.ylabel('Acceleration')
plt.savefig('a-t_graph.png')
plt.show()
