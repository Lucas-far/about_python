

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


# ÁREA DE ATUALIZAÇÃO DO CANVAS
while True:
    screen.fill('#222222')

    for event_in_game in pygame.event.get():
        if event_in_game.type == pygame.QUIT:
            exit(0)

    pygame.display.update()
    clock.tick(20)
