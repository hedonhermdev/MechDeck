from mechanics import *

# Body performing projectile motion.

g = Acceleration(0, -10) # Acceleration due to gravity.

# Defining a body.
body1 = Body('b1', 10, Velocity(10, 10), Acceleration(0, 0), Position(0, 0))

# Gravitational force on body.
mg = Force(body1.mass*g.x, body1.mass*g.y)

# Print initial velocity of body.
print(body1.velocity.x, body1.velocity.y)

# Time when body reaches maximum height.
t_hmax = body1.velocity.y / abs(g.y)

# Apply mg on body for time t_max.
body1.apply_force([mg], t_hmax)

# Print final velocity of body.
print(body1.velocity.x, body1.velocity.y)

#Define another force.
f2 = Force(10, 100)

# Apply forces mg and f2 on body for 100sec.
body1.apply_force([mg, f2], 100)

#Again print final velocity of body.
print(body1.velocity.x, body1.velocity.y)
