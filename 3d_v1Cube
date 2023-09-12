import pygame
import math
import sys

# Define los colores RGB
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Inicializa Pygame
pygame.init()

# Crea la ventana
dimensiones = (400, 400)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Cubo 3D")

# Define las coordenadas de los vértices del cubo
vertices = [
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, 1],
    [1, -1, 1]
]

# Define las conexiones entre los vértices para formar las caras del cubo
caras = [
    [0, 1, 2, 3],
    [0, 4, 5, 1],
    [1, 5, 6, 2],
    [2, 6, 7, 3],
    [3, 7, 4, 0],
    [4, 7, 6, 5]
]

# Definir el punto de vista de la cámara
camara = [0, 0, -5]
angulo = 0

# Bucle principal
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Limpia la pantalla
    pantalla.fill(BLANCO)

    # Dibuja el cubo en la pantalla
    for cara in caras:
        puntos = []
        for vertice in cara:
            # Calcula la posición del vértice en el espacio 3D
            x = vertices[vertice][0]
            y = vertices[vertice][1]
            z = vertices[vertice][2]

            # Rota el cubo en el eje y
            x, z = x * math.cos(angulo) + z * math.sin(angulo), z * math.cos(angulo) - x * math.sin(angulo)

            # Calcula la posición del vértice en la pantalla
            f = 200 / (camara[2] + z)
            x, y = int(x * f + 200), int(-y * f + 200)
            puntos.append([x, y])

        # Dibuja la cara del cubo en la pantalla
        pygame.draw.polygon(pantalla, NEGRO, puntos, 1)

    # Actualiza la pantalla
    pygame.display.flip()

    # Rota el cubo en el eje y
    angulo += 0.0005

# Cierra Pygame
pygame.quit()


