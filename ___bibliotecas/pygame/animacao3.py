

import pygame
from random import choice, random

width, height = 600, 600

# <code=1>
controls = {
    'setup': {
        'go_right': 0,
        'go_left': 0,
        'right_pressed': False,
        'left_pressed': False,
        'right': True,
        'left': False
    }
}


# SETUP PRINCIPAL DO PYGAME
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PROJETO')
clock = pygame.time.Clock()


class Player:

    def draw(self):
        if controls['setup']['right_pressed']:
            screen.blit(
                pygame.transform.scale(self.walk_right_surfaces[self.current_sprite], (self.width, self.height)),
                self.walk_right_rectangles[self.current_sprite]
            )

        if not controls['setup']['right_pressed'] and controls['setup']['right']:
            screen.blit(
                pygame.transform.scale(self.idle_right_surfaces[self.current_sprite], (self.width, self.height)),
                self.idle_right_rectangles[self.current_sprite]
            )

        if controls['setup']['left_pressed']:
            screen.blit(
                pygame.transform.scale(self.walk_left_surfaces[self.current_sprite], (self.width, self.height)),
                self.walk_left_rectangles[self.current_sprite]
            )

        # <code=8>
        if not controls['setup']['left_pressed'] and controls['setup']['left']:
            screen.blit(
                pygame.transform.scale(self.idle_left_surfaces[self.current_sprite], (self.width, self.height)),
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

        # <code=7>
        if not controls['setup']['left_pressed']:
            if self.current_sprite >= len(self.idle_left_surfaces):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.idle_left_surfaces[self.current_sprite]
                self.image_rect = self.idle_left_rectangles[self.current_sprite]

    def move(self, where, value):
        if where == 'up':
            self.image_rect.top -= value
        elif where == 'right':
            self.image_rect.right += value
        elif where == 'down':
            self.image_rect.bottom += value
        elif where == 'left':
            self.image_rect.left -= value

    "------------------------------------------------------- 6 -------------------------------------------------------"
    def idle_at_right(self):
        return self.idle_right_rectangles

    def idle_at_left(self):
        return self.idle_left_rectangles

    def right(self):
        return self.walk_right_rectangles

    def left(self):
        return self.walk_left_rectangles

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

    def __init__(self):
        self.is_animating = False
        self.width = 70
        self.height = 70
        self.x = 0
        self.y = 600 - (70 + 61)

        # <code=3>
        self.idle_right_surfaces = [
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_1_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_1_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_1_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_2_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_3_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_4_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_5_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_6_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_right\\wolf_idle_right_7_tr.png').convert_alpha(),
        ]
        self.idle_left_surfaces = [
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_1_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_1_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_1_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_2_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_3_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_4_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_5_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_6_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\idle_left\\wolf_idle_left_7_tr.png').convert_alpha(),
        ]
        self.walk_right_surfaces = [
            pygame.image.load('assets\\players\\walk_right\\walk_right_1_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_right\\walk_right_2_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_right\\walk_right_3_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_right\\walk_right_4_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_right\\walk_right_5_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_right\\walk_right_6_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_right\\walk_right_7_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_right\\walk_right_8_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_right\\walk_right_9_tr.png').convert_alpha(),
        ]
        self.walk_left_surfaces = [
            pygame.image.load('assets\\players\\walk_left\\walk_left_1_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_left\\walk_left_2_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_left\\walk_left_3_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_left\\walk_left_4_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_left\\walk_left_5_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_left\\walk_left_6_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_left\\walk_left_7_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_left\\walk_left_8_tr.png').convert_alpha(),
            pygame.image.load('assets\\players\\walk_left\\walk_left_9_tr.png').convert_alpha(),
        ]

        # <code=4>
        self.idle_right_rectangles = [
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

        # <code=5>
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


# TODO=1
class Enemy:

    def animate(self):
        self.is_animating = True

    def draw(self):
        screen.blit(
            pygame.transform.scale(self.shell_purple_surfaces[int(self.current_sprite)], (self.width, self.height)),
            self.shell_purple_rectangles[int(self.current_sprite)]
        )

    def update(self):
        self.current_sprite += random()
        print(self.current_sprite)

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
        self.y = 600 - (32 + 61)
        self.modular_counter = 0
        self.modular = 1_000_000

        self.shell_purple_surfaces = [
            pygame.image.load('assets\\shells\\purple\\purple_shell_1_tr.gif').convert_alpha(),
            pygame.image.load('assets\\shells\\purple\\purple_shell_2_tr.gif').convert_alpha(),
            pygame.image.load('assets\\shells\\purple\\purple_shell_3_tr.gif').convert_alpha(),
            pygame.image.load('assets\\shells\\purple\\purple_shell_4_tr.gif').convert_alpha(),
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
# TODO=1


player = Player()
shell_purple = Enemy()

while True:
    screen.fill('#222222')

    for event_in_game in pygame.event.get():

        if event_in_game.type == pygame.KEYDOWN:

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

    player.draw()
    player.animate()
    player.update()

    # TODO=2
    shell_purple.draw()
    shell_purple.animate()
    shell_purple.update()
    shell_purple.move('left', choice([*range(0, 11)]))
    shell_purple.move('right', choice([*range(0, 11)]))
    # TODO=2

    pygame.display.update()
    clock.tick(20)
