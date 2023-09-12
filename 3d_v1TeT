import pygame
import math
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetrahedron")

# Define the vertices of the tetrahedron
vertices = [
    (0, 100, 0), # Top vertex
    (0, 0, -100), # Bottom front vertex
    (-100, 0, 0), # Bottom left vertex
    (100, 0, 0) # Bottom right vertex
]

# Define the edges of the tetrahedron
edges = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (2, 3),
    (3, 1)
]

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define the rotation speed
rotation_speed = 0.0001

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(white)

    # Rotate the tetrahedron
    for i, vertex in enumerate(vertices):
        x, y, z = vertex

        # Rotate around the Y-axis
        x, z = x * math.cos(rotation_speed) + z * math.sin(rotation_speed), -x * math.sin(rotation_speed) + z * math.cos(rotation_speed)
        vertices[i] = (x, y, z)

    # Draw the edges
    for edge in edges:
        start, end = edge
        pygame.draw.line(screen, black, (vertices[start][0] + size[0] / 2, size[1] / 2 - vertices[start][1]), 
                             (vertices[end][0] + size[0] / 2, size[1] / 2 - vertices[end][1]), 2)


    # Update the screen
    pygame.display.flip()


