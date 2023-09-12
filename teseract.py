import itertools
import pygame
import numpy as np

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Definición de los puntos del tesseract
points = []
for i, j, k, l in itertools.product(range(2), range(2), range(2), range(2)):
    point = [i, j, k, l]
    points.append(point)

# Definición de las caras del tesseract
faces = [
    (0, 1, 3, 2),
    (0, 2, 6, 4),
    (0, 4, 5, 1),
    (1, 5, 7, 3),
    (2, 3, 7, 6),
    (4, 6, 7, 5)
]

# Definición de los colores de las caras
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
]

# Función para rotar los puntos del tesseract en los 3 ejes
def rotate(points, angle):
    rotation_matrix_x = np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])

    rotation_matrix_y = np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])

    rotation_matrix_z = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

    rotated_points = []
    for point in points:
        rotated_point = np.dot(rotation_matrix_x, np.dot(rotation_matrix_y, np.dot(rotation_matrix_z, point)))
        rotated_points.append(rotated_point)

    return rotated_points

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tesseract")

# Ángulo de rotación inicial
angle = 0

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujado del tesseract
    screen.fill((0, 0, 0))
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    for face, color in zip(faces, colors):
        point_list = []
        for vertex_index in face:
            vertex = points[vertex_index]
            rotated_vertex = rotate(vertex, angle)
            x = rotated_vertex[0] * 75 + center_x
            y = rotated_vertex[1] * 75 + center_y
            point_list.append((x, y))
        pygame.draw.polygon(screen, color, point_list)

    # Actualización del ángulo de rotación
    angle += 0.01

    # Actualización de la pantalla
    pygame.display.update()

# Salida del programa
pygame.quit()
