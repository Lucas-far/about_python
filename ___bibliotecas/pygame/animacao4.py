

"""
Configuração de um inimigo
"""

import pygame
from random import choice, random

width, height = 600, 600

controls = {
    'setup': {
        'go_right': 0,
        'go_left': 0,
        'right_pressed': False,
        'left_pressed': False,
        'right': True,
        'left': False,
    }
}

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PROJETO')
clock = pygame.time.Clock()


class Player:
    """
    for rectangle in self.idle_right_rectangles:
        pass
    for rectangle in self.idle_left_rectangles:
        pass
    for rectangle in self.walk_right_rectangles:
        pass
    for rectangle in self.walk_left_rectangles:
        pass
    """

    def draw(self):
        if controls['setup']['right_pressed']:
            screen.blit(
                self.walk_right_surfaces[self.current_sprite],
                self.walk_right_rectangles[self.current_sprite]
            )

        if not controls['setup']['right_pressed'] and controls['setup']['right']:
            screen.blit(
                self.idle_right_surfaces[self.current_sprite],
                self.idle_right_rectangles[self.current_sprite]
            )

        if controls['setup']['left_pressed']:
            screen.blit(
                self.walk_left_surfaces[self.current_sprite],
                self.walk_left_rectangles[self.current_sprite]
            )

        if not controls['setup']['left_pressed'] and controls['setup']['left']:
            screen.blit(
                self.idle_left_surfaces[self.current_sprite],
                self.idle_left_rectangles[self.current_sprite]
            )

    def animate(self):
        self.is_animating = True

    def update(self):
        self.current_sprite += 1

        if controls['setup']['right_pressed']:
            if self.current_sprite >= len(self.walk_right_surfaces):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.walk_right_surfaces[self.current_sprite]
                self.image_rect = self.walk_right_rectangles[self.current_sprite]

        if not controls['setup']['right_pressed']:
            if self.current_sprite >= len(self.idle_right_surfaces):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.idle_right_surfaces[self.current_sprite]
                self.image_rect = self.idle_right_rectangles[self.current_sprite]

        if controls['setup']['left_pressed']:
            if self.current_sprite >= len(self.walk_left_surfaces):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.walk_left_surfaces[self.current_sprite]
                self.image_rect = self.walk_left_rectangles[self.current_sprite]

        if not controls['setup']['left_pressed']:
            if self.current_sprite >= len(self.idle_left_surfaces):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.idle_left_surfaces[self.current_sprite]
                self.image_rect = self.idle_left_rectangles[self.current_sprite]

    def horizontal_setup_right(self):
        for rectangle in self.idle_right_rectangles:
            rectangle.right += 10
        for rectangle in self.idle_left_rectangles:
            rectangle.right += 10
        for rectangle in self.walk_right_rectangles:
            rectangle.right += 10
        for rectangle in self.walk_left_rectangles:
            rectangle.right += 10

    def horizontal_setup_left(self):
        for rectangle_left in self.idle_right_rectangles:
            rectangle_left.right -= 10
        for rectangle_left in self.idle_left_rectangles:
            rectangle_left.right -= 10
        for rectangle_left in self.walk_right_rectangles:
            rectangle_left.right -= 10
        for rectangle_left in self.walk_left_rectangles:
            rectangle_left.right -= 10

    @staticmethod
    def idle_right_setup():
        controls['setup']['right_pressed'] = False
        controls['setup']['right'] = True
        controls['setup']['left'] = False

    @staticmethod
    def idle_left_setup():
        controls['setup']['left_pressed'] = False
        controls['setup']['right'] = False
        controls['setup']['left'] = True

    @staticmethod
    def walk_right_setup():
        controls['setup']['right_pressed'] = True
        controls['setup']['right'] = True
        controls['setup']['left'] = False

    @staticmethod
    def walk_left_setup():
        controls['setup']['left_pressed'] = True
        controls['setup']['right'] = False
        controls['setup']['left'] = True

    @staticmethod
    def back_onto_surface(player_object, this_much):
        player_object.gravity += this_much

    def move(self, where, value):
        if where == 'up':
            pass
        elif where == 'right':
            pass
        elif where == 'down':
            for rectangle in self.idle_right_rectangles:
                rectangle.bottom += value
            for rectangle in self.idle_left_rectangles:
                rectangle.bottom += value
            for rectangle in self.walk_right_rectangles:
                rectangle.bottom += value
            for rectangle in self.walk_left_rectangles:
                rectangle.bottom += value
        elif where == 'left':
            pass

    def ground_interaction(self):
        """
        ============================================== idle right ==============================================
        Posição do retângulo  || {rectangle.bottom}
        Posição do chão       || {600 - 61}
        Subtração das duas    || {rectangle.bottom - (600 - 61)}
        """

        # Um personagem precisa estar dentro de algo:  canvas
        # Um personagem precisa estar pousado em algo: superfície
        # Valores variáveis de acordo com as imagens usadas no projeto
        canvas_height = 600
        surface_height = 61
        box = set([])

        for rectangle in self.idle_right_rectangles:
            if rectangle.bottom >= (canvas_height - surface_height):
                box.add(True)
                self.gravity = 0
                rectangle.bottom = canvas_height - surface_height
        for rectangle in self.idle_left_rectangles:
            if rectangle.bottom >= (canvas_height - surface_height):
                box.add(True)
                self.gravity = 0
                rectangle.bottom = canvas_height - surface_height
        for rectangle in self.walk_right_rectangles:
            if rectangle.bottom >= (canvas_height - surface_height):
                box.add(True)
                self.gravity = 0
                rectangle.bottom = canvas_height - surface_height
        for rectangle in self.walk_left_rectangles:
            if rectangle.bottom >= (canvas_height - surface_height):
                box.add(True)
                self.gravity = 0
                rectangle.bottom = canvas_height - surface_height

        if box == {True, True, True, True}:
            return True

    def draw_rect(self):
        for rectangle in self.idle_right_rectangles:
            pygame.draw.rect(screen, 'green', rectangle)
        for rectangle in self.idle_left_rectangles:
            pygame.draw.rect(screen, 'yellow', rectangle)
        for rectangle in self.walk_right_rectangles:
            pygame.draw.rect(screen, 'white', rectangle)
        for rectangle in self.walk_left_rectangles:
            pygame.draw.rect(screen, 'blue', rectangle)

    def __init__(self):
        self.is_animating = False
        self.width = 70
        self.height = 70
        self.x = 0
        self.y = 600 - (70 + 61)
        self.idle_bottom = 644
        self.walk_bottom = 629

        self.gravity = 0

        self.idle_right_surfaces = [
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_1_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_1_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_1_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_2_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_3_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_4_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_5_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_6_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_7_tr.png').convert_alpha(), (self.width, self.height))
        ]
        self.idle_left_surfaces = [
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_1_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_1_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_1_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_2_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_3_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_4_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_5_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_6_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_7_tr.png').convert_alpha(), (self.width, self.height))
        ]
        self.walk_right_surfaces = [
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_1_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_2_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_3_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_4_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_5_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_6_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_7_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_8_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_right\\walk_right_9_tr.png').convert_alpha(), (self.width, self.height))
        ]
        self.walk_left_surfaces = [
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_1_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_2_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_3_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_4_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_5_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_6_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_7_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_8_tr.png').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\players\\walk_left\\walk_left_9_tr.png').convert_alpha(), (self.width, self.height))
        ]

        self.idle_right_rectangles = [
            # pygame.transform.scale(self.walk_right_surfaces[self.current_sprite], (self.width, self.height))
            self.idle_right_surfaces[0].get_rect(topleft=(self.x, self.y)),
            self.idle_right_surfaces[1].get_rect(topleft=(self.x, self.y)),
            self.idle_right_surfaces[2].get_rect(topleft=(self.x, self.y)),
            self.idle_right_surfaces[3].get_rect(topleft=(self.x, self.y)),
            self.idle_right_surfaces[4].get_rect(topleft=(self.x, self.y)),
            self.idle_right_surfaces[5].get_rect(topleft=(self.x, self.y)),
            self.idle_right_surfaces[6].get_rect(topleft=(self.x, self.y)),
            self.idle_right_surfaces[7].get_rect(topleft=(self.x, self.y)),
            self.idle_right_surfaces[8].get_rect(topleft=(self.x, self.y)),
        ]
        self.idle_left_rectangles = [
            self.idle_left_surfaces[0].get_rect(topleft=(self.x, self.y)),
            self.idle_left_surfaces[1].get_rect(topleft=(self.x, self.y)),
            self.idle_left_surfaces[2].get_rect(topleft=(self.x, self.y)),
            self.idle_left_surfaces[3].get_rect(topleft=(self.x, self.y)),
            self.idle_left_surfaces[4].get_rect(topleft=(self.x, self.y)),
            self.idle_left_surfaces[5].get_rect(topleft=(self.x, self.y)),
            self.idle_left_surfaces[6].get_rect(topleft=(self.x, self.y)),
            self.idle_left_surfaces[7].get_rect(topleft=(self.x, self.y)),
            self.idle_left_surfaces[8].get_rect(topleft=(self.x, self.y)),
        ]
        self.walk_right_rectangles = [
            self.walk_right_surfaces[0].get_rect(topleft=(self.x, self.y)),
            self.walk_right_surfaces[1].get_rect(topleft=(self.x, self.y)),
            self.walk_right_surfaces[2].get_rect(topleft=(self.x, self.y)),
            self.walk_right_surfaces[3].get_rect(topleft=(self.x, self.y)),
            self.walk_right_surfaces[4].get_rect(topleft=(self.x, self.y)),
            self.walk_right_surfaces[5].get_rect(topleft=(self.x, self.y)),
            self.walk_right_surfaces[6].get_rect(topleft=(self.x, self.y)),
            self.walk_right_surfaces[7].get_rect(topleft=(self.x, self.y)),
            self.walk_right_surfaces[8].get_rect(topleft=(self.x, self.y))
        ]
        self.walk_left_rectangles = [
            self.walk_left_surfaces[0].get_rect(topleft=(self.x, self.y)),
            self.walk_left_surfaces[1].get_rect(topleft=(self.x, self.y)),
            self.walk_left_surfaces[2].get_rect(topleft=(self.x, self.y)),
            self.walk_left_surfaces[3].get_rect(topleft=(self.x, self.y)),
            self.walk_left_surfaces[4].get_rect(topleft=(self.x, self.y)),
            self.walk_left_surfaces[5].get_rect(topleft=(self.x, self.y)),
            self.walk_left_surfaces[6].get_rect(topleft=(self.x, self.y)),
            self.walk_left_surfaces[7].get_rect(topleft=(self.x, self.y)),
            self.walk_left_surfaces[8].get_rect(topleft=(self.x, self.y))
        ]

        self.current_sprite = 0

        if controls['setup']['right_pressed']:
            self.image = self.walk_right_surfaces[self.current_sprite]
            self.image_rect = self.walk_right_rectangles[self.current_sprite]

        if not controls['setup']['right_pressed']:
            self.image = self.idle_right_surfaces[self.current_sprite]
            self.image_rect = self.idle_right_rectangles[self.current_sprite]

        if controls['setup']['left_pressed']:
            self.image = self.walk_left_surfaces[self.current_sprite]
            self.image_rect = self.walk_left_rectangles[self.current_sprite]

        if not controls['setup']['left_pressed']:
            self.image = self.idle_left_surfaces[self.current_sprite]
            self.image_rect = self.idle_left_rectangles[self.current_sprite]


# TODO = 1
speed_variations_left = [*range(0, 11)]
speed_variations_right = [*range(0, 3)]


# TODO = 1
class Enemy:

    def animate(self):
        self.is_animating = True

    def draw(self):
        screen.blit(
            self.shell_purple_surfaces[int(self.current_sprite)],
            self.shell_purple_rectangles[int(self.current_sprite)]
        )

    def update(self):
        self.current_sprite += random()

        if int(self.current_sprite) >= len(self.shell_purple_surfaces):
            self.current_sprite = 0
            self.is_animating = False
        else:
            self.image = self.shell_purple_surfaces[int(self.current_sprite)]
            self.image_rect = self.shell_purple_rectangles[int(self.current_sprite)]

    def move(self, direction, this_speed):
        if direction == 'left':
            for rect in self.shell_purple_rectangles:
                rect.left -= this_speed
        elif direction == 'right':
            for rect in self.shell_purple_rectangles:
                rect.right += this_speed

    def __init__(self):
        self.is_animating = False
        self.width = 36
        self.height = 32
        self.x = 400
        self.main_surface_top_height = 61
        self.y = 600 - (self.height + self.main_surface_top_height)

        self.shell_purple_surfaces = [
            pygame.transform.scale(pygame.image.load('assets\\shells\\purple\\purple_shell_1_tr.gif').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\shells\\purple\\purple_shell_2_tr.gif').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\shells\\purple\\purple_shell_3_tr.gif').convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('assets\\shells\\purple\\purple_shell_4_tr.gif').convert_alpha(), (self.width, self.height))
        ]

        self.shell_purple_rectangles = [
            self.shell_purple_surfaces[0].get_rect(topleft=(self.x, self.y)),
            self.shell_purple_surfaces[1].get_rect(topleft=(self.x, self.y)),
            self.shell_purple_surfaces[2].get_rect(topleft=(self.x, self.y)),
            self.shell_purple_surfaces[3].get_rect(topleft=(self.x, self.y)),
        ]

        self.current_sprite = 0

        self.image = self.shell_purple_surfaces[self.current_sprite]
        self.image_rect = self.shell_purple_rectangles[self.current_sprite]


player = Player()
shell_purple = Enemy()  # TODO = 1

while True:
    screen.fill('#222222')

    for event_in_game in pygame.event.get():

        if event_in_game.type == pygame.QUIT:
            exit(0)

        if event_in_game.type == pygame.KEYDOWN:

            if event_in_game.key == pygame.K_w and player.ground_interaction():
                player.gravity = -50

            if event_in_game.key == pygame.K_d:
                player.walk_right_setup()

            if event_in_game.key == pygame.K_a:
                player.walk_left_setup()

        if event_in_game.type == pygame.KEYUP:

            if event_in_game.key == pygame.K_d:
                player.idle_right_setup()

            if event_in_game.key == pygame.K_a:
                player.idle_left_setup()

    if controls['setup']['right_pressed']:
        player.horizontal_setup_right()

    if controls['setup']['left_pressed']:
        player.horizontal_setup_left()

    player.draw_rect()
    player.draw()
    player.animate()
    player.update()

    player.move('down', player.gravity)
    player.back_onto_surface(player, 5)
    player.ground_interaction()

    # TODO = 2
    shell_purple.draw()
    shell_purple.animate()
    shell_purple.update()
    shell_purple.move('left', choice(speed_variations_left) * random())
    shell_purple.move('right', choice(speed_variations_right) * random())
    # TODO = 2

    pygame.display.update()
    clock.tick(20)
