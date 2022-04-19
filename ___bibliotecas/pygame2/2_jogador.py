

"""
Configuração do jogador e animação
"""

import pygame

width, height = 600, 600

# SETUP PRINCIPAL DO PYGAME
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PROJETO')
clock = pygame.time.Clock()


class Player:

    def rectangle_into_rectangle(self, ink):
        for rectangle in self.rect:
            pygame.draw.rect(screen, ink, rectangle)

    def draw(self):
        screen.blit(
            self.surf[self.current_sprite],
            self.rect[self.current_sprite]
        )

    # TODO: animação (parte 2)
    def animate(self):
        self.is_animating = True

    # TODO: animação (parte 3)
    def render_each_frame(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.surf):
            self.current_sprite = 0
            self.is_animating = False

        else:
            self.image = self.surf[self.current_sprite]
            self.image_rectangle = self.rect[self.current_sprite]

    def __init__(self, pl_width, pl_height, x, y, image_list):
        self.width = pl_width
        self.height = pl_height
        self.x = x
        self.y = y
        self.image_list = image_list
        self.gravity = 0
        self.current_sprite = 0
        self.img = []
        self.surf = []
        self.rect = []

        # TODO: animação (parte 1)
        self.is_animating = False
        self.image = None
        self.image_rectangle = None

        for image in self.image_list:
            self.img.append(pygame.image.load(image).convert_alpha())
        for surface in self.img:
            self.surf.append(pygame.transform.scale(surface, (self.width, self.height)))
        for surface in self.surf:
            self.rect.append(surface.get_rect(topleft=(self.x, self.y)))


player_img = [
    'assets\\idle_right\\wolf_idle_right_1_tr.png', 'assets\\idle_right\\wolf_idle_right_1_tr.png',
    'assets\\idle_right\\wolf_idle_right_1_tr.png', 'assets\\idle_right\\wolf_idle_right_2_tr.png',
    'assets\\idle_right\\wolf_idle_right_3_tr.png', 'assets\\idle_right\\wolf_idle_right_4_tr.png',
    'assets\\idle_right\\wolf_idle_right_5_tr.png', 'assets\\idle_right\\wolf_idle_right_6_tr.png',
    'assets\\idle_right\\wolf_idle_right_7_tr.png'
]
player = Player(70, 70, 0, 600 - (70 + 61), player_img)

while True:
    screen.fill('#222222')

    player.rectangle_into_rectangle((255, 0, 64))
    player.draw()
    player.render_each_frame()

    pygame.display.update()
    clock.tick(20)
