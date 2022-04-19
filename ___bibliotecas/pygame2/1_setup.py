

"""
Configuração do ambiente Pygame
"""

import pygame

width, height = 600, 600

# SETUP PRINCIPAL DO PYGAME
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PROJETO')
clock = pygame.time.Clock()

while True:
    screen.fill('#222222')

    pygame.display.update()
    clock.tick(20)
