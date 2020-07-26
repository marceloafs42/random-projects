## this is a simple script to vizualize a little bit of gradient descent

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from sympy import Symbol, Function, diff, lambdify, sin, sqrt

## we use sympy to deal with the f(x, y) function, using symbolic math
x = Symbol("x")
y = Symbol("y")

f = Function("f")(x, y)
f = sin(sqrt(x**2 + y**2)) ##defines function
lam_f = lambdify((x, y), f)

fx = diff(f, x)
lam_fx = lambdify((x, y), fx)
fy = diff(f, y)
lam_fy = lambdify((x, y), fy)


## we start at some random point, and then use gradient descent
x0 = [1.5]
y0 = [-1.5]
alpha = 0.2

i = 0
while(i < 100):
    x0.append(x0[i] - alpha*lam_fx(x0[i], y0[i]))
    y0.append(y0[i] - alpha*lam_fy(x0[i - 1], y0[i]))
    i = i + 1

#######
# plot surface
z0 = [lam_f(x0[i], y0[i]) for i in range(len(x0))]

fig, axes = plt.subplots()
ax = Axes3D(fig)

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = lam_f(X, Y)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='Greens', edgecolor='none', alpha = 0.2)

ax.scatter(x0, y0, z0, s = 200, c = 'r', cmap = 'Greens', marker='*', alpha = 1)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

#######
# plot contour

pos = [1, 0, 1, 1]
axes.set_position(pos)

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = lam_f(X, Y)

axes.contour(X, Y, Z)
axes.scatter(x0, y0, c = 'r', marker = 'x')

plt.show()