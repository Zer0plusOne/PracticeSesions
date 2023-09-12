import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_sphere(radius, n):
    phi, theta = np.linspace(0, np.pi, n), np.linspace(0, 2 * np.pi, n)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return x, y, z

# Generar una esfera con radio 1 y 50 puntos
x, y, z = generate_sphere(1, 50)

# Crear una figura en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la esfera
ax.plot_surface(x, y, z, color='blue')

# Mostrar la figura
plt.show()
