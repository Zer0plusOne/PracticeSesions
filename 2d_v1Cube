import pygame
import random
import math

# Inicialización de Pygame
pygame.init()

# Establecer las dimensiones de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Definir las coordenadas de los puntos que conforman el cubo
points = [
    (-50, -50, -50), (50, -50, -50), (50, 50, -50), (-50, 50, -50),
    (-50, -50, 50), (50, -50, 50), (50, 50, 50), (-50, 50, 50)
]

# Definir los bordes que conectan los puntos del cubo
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Definir la función para rotar el cubo alrededor de un eje aleatorio
def rotate(point, angle):
    # Convertir el ángulo a radianes
    angle = angle * math.pi / 180

    # Definir la matriz de rotación
    rotation_matrix = [
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]

    return [
        sum(rotation_matrix[i][j] * point[j] for j in range(3))
        for i in range(3)
    ]

# Definir la función para dibujar el cubo en la pantalla
def draw_cube(points, edges):
    for edge in edges:
        start = points[edge[0]]
        end = points[edge[1]]
        pygame.draw.line(screen, (255, 255, 255), (start[0]+width/2, start[1]+height/2), (end[0]+width/2, end[1]+height/2))

# Definir la función principal
def main():
    # Establecer el ángulo inicial
    angle = 0

    # Bucle principal
    running = True
    while running:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Borrar la pantalla
        screen.fill((0, 0, 0))

        # Rotar el cubo alrededor de un eje aleatorio
        angle += random.randint(1, 2)
        rotated_points = [rotate(point, angle) for point in points]

        # Dibujar el cubo en la pantalla
        draw_cube(rotated_points, edges)

        # Actualizar la pantalla
        pygame.display.flip()

    # Salir de Pygame
    pygame.quit()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
