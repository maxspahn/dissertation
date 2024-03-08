import numpy as np
import matplotlib.pyplot as plt

def f(x, y, goal):
    return 1.0 * np.sin(np.sqrt(x ** 2 + y ** 2)) + 0.5 * np.sqrt((x-goal[0])**2 + (y-goal[1])**2)

x = np.linspace(0, 6, 30)
y = np.linspace(0, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y, [3.5, 2.4])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.grid(False)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z');
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_frame_on(False)
ax.axis('off')
plt.savefig('potential_field.svg', bbox_inches='tight', pad_inches=0)
