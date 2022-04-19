

"""
Inseri
"""

import pygame
from random import choice, random

width, height = 600, 600

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PROJETO')
clock = pygame.time.Clock()

# TODO (5): Var admin da saúde
player_health = 100


# TODO (6): Adição de dados referentes ao HP
controls = {
    'setup': {
        'go_right': 0,
        'go_left': 0,
        'right_pressed': False,
        'left_pressed': False,
        'right': True,
        'left': False,
        'health_label': 'Saúde: ',
        'health': f'{player_health}'
    }
}

speed_variations_left = [*range(0, 11)]
speed_variations_right = [*range(0, 3)]
sizes_variations = [*range(32, 46)]


class Player:
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

    def img_render_admin(self):
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

    def horizontal_setup_right(self, this_much):
        for rectangle in self.idle_right_rectangles:
            rectangle.right += this_much
        for rectangle in self.idle_left_rectangles:
            rectangle.right += this_much
        for rectangle in self.walk_right_rectangles:
            rectangle.right += this_much
        for rectangle in self.walk_left_rectangles:
            rectangle.right += this_much

    def horizontal_setup_left(self, this_much):
        for rectangle_left in self.idle_right_rectangles:
            rectangle_left.left -= this_much
        for rectangle_left in self.idle_left_rectangles:
            rectangle_left.left -= this_much
        for rectangle_left in self.walk_right_rectangles:
            rectangle_left.left -= this_much
        for rectangle_left in self.walk_left_rectangles:
            rectangle_left.left -= this_much

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

    def draw_rect(self):
        for rectangle in self.idle_right_rectangles:
            pygame.draw.rect(screen, 'green', rectangle)
        for rectangle in self.idle_left_rectangles:
            pygame.draw.rect(screen, 'yellow', rectangle)
        for rectangle in self.walk_right_rectangles:
            pygame.draw.rect(screen, 'white', rectangle)
        for rectangle in self.walk_left_rectangles:
            pygame.draw.rect(screen, 'blue', rectangle)

    @staticmethod
    def jump(player_object, this_much):
        player_object.gravity = this_much

    @staticmethod
    def fall(player_object, this_much):
        player_object.gravity += this_much

    def move(self, where, value):
        if where == 'down':
            for player_rectangle in self.idle_right_rectangles:
                player_rectangle.bottom += value
            for player_rectangle in self.idle_left_rectangles:
                player_rectangle.bottom += value
            for player_rectangle in self.walk_right_rectangles:
                player_rectangle.bottom += value
            for player_rectangle in self.walk_left_rectangles:
                player_rectangle.bottom += value

    def ground_interaction(self):

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

    def __init__(self):
        self.is_animating = False
        self.width = 70
        self.height = 70
        self.x = 0
        self.y = 600 - (70 + 61)

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


player = Player()


def exec_player_display_functions():
    player.draw_rect()
    player.draw()
    player.animate()
    player.img_render_admin()


def exec_player_jumping_functions():
    player.move('down', player.gravity)
    player.fall(player, 5)
    player.ground_interaction()


# TODO (7): A var global precisa ser monitorada dentro da função
def player_health_admin(enemy_box, any_player_rectangle_box, source_location, health_penalty):
    global player_health

    is_there_collision = enemy_collision('shell', enemy_box, any_player_rectangle_box)

    # TODO (8): Perda de saúde em caso de colisão
    if is_there_collision:
        player_health -= health_penalty
        print(player_health)
        controls['setup']['health'] = f'{round(player_health)}'  # Atualização da vida na var fonte
        source_location.label = controls['setup']['health']      # Atualização da vida na tela

    # TODO (9): Reinicialização dos pontos
    if player_health <= 0:
        player_health = 100
        controls['setup']['health'] = f'{player_health}'
        source_location.label = controls['setup']['health']


class Enemy:

    def animate(self):
        self.is_animating = True

    def draw(self):
        if self.enemy_name == 'shell_purple':
            screen.blit(
                self.shell_purple_surfaces[int(self.current_sprite)],
                self.shell_purple_rectangles[int(self.current_sprite)]
            )
        elif self.enemy_name == 'shell_green':
            screen.blit(
                self.shell_green_surfaces[int(self.current_sprite)],
                self.shell_green_rectangles[int(self.current_sprite)]
            )

    def update(self):
        self.current_sprite += random()

        if self.enemy_name == 'shell_purple':

            if int(self.current_sprite) >= len(self.shell_purple_surfaces):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.shell_purple_surfaces[int(self.current_sprite)]
                self.image_rect = self.shell_purple_rectangles[int(self.current_sprite)]

        elif self.enemy_name == 'shell_green':

            if int(self.current_sprite) >= len(self.shell_green_surfaces):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.shell_green_surfaces[int(self.current_sprite)]
                self.image_rect = self.shell_green_rectangles[int(self.current_sprite)]

    def move(self, direction, this_speed):
        if direction == 'left' and self.enemy_name == 'shell_purple':
            for rect in self.shell_purple_rectangles:
                rect.left -= this_speed
        elif direction == 'right' and self.enemy_name == 'shell_purple':
            for rect in self.shell_purple_rectangles:
                rect.right += this_speed

        if direction == 'left' and self.enemy_name == 'shell_green':
            for rect in self.shell_green_rectangles:
                rect.left -= this_speed
        elif direction == 'right' and self.enemy_name == 'shell_green':
            for rect in self.shell_green_rectangles:
                rect.right += this_speed

    def img_into_surface(self, which_one):
        if which_one == 'shell_purple':
            self.shell_purple_surfaces = [
                pygame.transform.scale(pygame.image.load('assets\\shells\\purple\\purple_shell_1_tr.gif').convert_alpha(), (self.enemy_width, self.enemy_height)),
                pygame.transform.scale(pygame.image.load('assets\\shells\\purple\\purple_shell_2_tr.gif').convert_alpha(), (self.enemy_width, self.enemy_height)),
                pygame.transform.scale( pygame.image.load('assets\\shells\\purple\\purple_shell_3_tr.gif').convert_alpha(), (self.enemy_width, self.enemy_height)),
                pygame.transform.scale( pygame.image.load('assets\\shells\\purple\\purple_shell_4_tr.gif').convert_alpha(), (self.enemy_width, self.enemy_height))
            ]
        elif which_one == 'shell_green':
            self.shell_green_surfaces = [
                pygame.transform.scale(pygame.image.load('assets\\shells\\green\\green_shell_1_tr.gif').convert_alpha(), (self.enemy_width, self.enemy_height)),
                pygame.transform.scale(pygame.image.load('assets\\shells\\green\\green_shell_2_tr.gif').convert_alpha(), (self.enemy_width, self.enemy_height)),
                pygame.transform.scale(pygame.image.load('assets\\shells\\green\\green_shell_3_tr.gif').convert_alpha(), (self.enemy_width, self.enemy_height)),
                pygame.transform.scale(pygame.image.load('assets\\shells\\green\\green_shell_4_tr.gif').convert_alpha(), (self.enemy_width, self.enemy_height))
            ]

    def surface_into_rectangle(self, which_one):
        if which_one == 'shell_purple':
            self.shell_purple_rectangles = [
                self.shell_purple_surfaces[0].get_rect(topleft=(self.x, self.y)),
                self.shell_purple_surfaces[1].get_rect(topleft=(self.x, self.y)),
                self.shell_purple_surfaces[2].get_rect(topleft=(self.x, self.y)),
                self.shell_purple_surfaces[3].get_rect(topleft=(self.x, self.y)),
            ]
        elif which_one == 'shell_green':
            self.shell_green_rectangles = [
                self.shell_green_surfaces[0].get_rect(topleft=(self.x, self.y)),
                self.shell_green_surfaces[1].get_rect(topleft=(self.x, self.y)),
                self.shell_green_surfaces[2].get_rect(topleft=(self.x, self.y)),
                self.shell_green_surfaces[3].get_rect(topleft=(self.x, self.y)),
            ]

    def set_main_surface_and_rectangle(self, which_one):
        if which_one == 'shell_purple':
            self.image = self.shell_purple_surfaces[self.current_sprite]
            self.image_rect = self.shell_purple_rectangles[self.current_sprite]
        elif which_one == 'shell_green':
            self.image = self.shell_green_surfaces[self.current_sprite]
            self.image_rect = self.shell_green_rectangles[self.current_sprite]

    def __init__(self, enemy_name, enemy_width, enemy_height, random_location=False, location=0):
        self.is_animating = False
        self.enemy_name = enemy_name
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.main_surface_top_height = 61
        self.y = 600 - (self.enemy_height + self.main_surface_top_height)

        self.shell_purple_surfaces = []
        self.shell_green_surfaces = []
        self.shell_purple_rectangles = []
        self.shell_green_rectangles = []

        self.image = None
        self.image_rect = None

        self.shell_locations_x = [*range(700, 2001)]
        self.current_sprite = 0

        if enemy_name == 'shell_purple':
            Enemy.img_into_surface(self, 'shell_purple')

            if not random_location:
                self.x = choice(self.shell_locations_x)
                Enemy.surface_into_rectangle(self, 'shell_purple')
                Enemy.set_main_surface_and_rectangle(self, 'shell_purple')

            else:
                self.x = location
                Enemy.surface_into_rectangle(self, 'shell_purple')
                Enemy.set_main_surface_and_rectangle(self, 'shell_purple')

        elif enemy_name == 'shell_green':
            Enemy.img_into_surface(self, 'shell_green')

            if not random_location:
                self.x = choice(self.shell_locations_x)
                Enemy.surface_into_rectangle(self, 'shell_green')
                Enemy.set_main_surface_and_rectangle(self, 'shell_green')
            else:
                self.x = location
                Enemy.surface_into_rectangle(self, 'shell_green')
                Enemy.set_main_surface_and_rectangle(self, 'shell_green')


shell_types = ['shell_purple', 'shell_green']
shell_amount = 10
shell_box = []


def make_enemy(enemy_type, enemy_object_box, end_point, enemy_type_box, location, x):
    counter = 0

    if enemy_type == 'shell' and not location:
        while counter < end_point:
            enemy_object_box.append(Enemy(
                choice(enemy_type_box), choice(sizes_variations), choice(sizes_variations),
            ))
            counter += 1

    if enemy_type == 'shell' and location:
        while counter < end_point:
            enemy_object_box.append(Enemy(
                choice(enemy_type_box), choice(sizes_variations), choice(sizes_variations), True, x
            ))
            counter += 1


def enemy_collision(enemy_name, enemy_rect_box, any_player_rectangle):
    """
    EXEMPLO:
        enemy_collision('shell', shell_box, player.idle_right_rectangles)
    """
    if enemy_name == 'shell':
        for each_shell in enemy_rect_box:
            for rectangle in any_player_rectangle:
                if each_shell.image_rect.colliderect(rectangle):
                    return True


def exec_enemy_class_functions(which_enemy, enemy_box):
    if which_enemy == 'shell':
        for shell in enemy_box:
            shell.draw()
            shell.animate()
            shell.update()
            shell.move('left', choice(speed_variations_left) * random())
            shell.move('right', choice(speed_variations_right) * random())


def events_watcher(scenario):
    if scenario == 'player_movement':

        for event_in_game in pygame.event.get():
            if event_in_game.type == pygame.QUIT:
                exit(0)
            if event_in_game.type == pygame.KEYDOWN:

                if event_in_game.key == pygame.K_w and player.ground_interaction():
                    player.jump(player, -50)
                if event_in_game.key == pygame.K_d:
                    player.walk_right_setup()
                if event_in_game.key == pygame.K_a:
                    player.walk_left_setup()
            if event_in_game.type == pygame.KEYUP:
                if event_in_game.key == pygame.K_d:
                    player.idle_right_setup()
                if event_in_game.key == pygame.K_a:
                    player.idle_left_setup()


make_enemy('shell', shell_box, shell_amount, shell_types, False, None)
make_enemy('shell', shell_box, 1, shell_types, True, 400)


# TODO (1): Classe para inserção de conteúdos de texto na tela (que podem variar)
class Book:

    def set_font(self):
        self.the_font = pygame.font.Font(self.font_family, self.font_size)

    def set_text(self):
        self.text = self.the_font.render(self.label, False, self.color)

    def set_rect(self):
        self.text_rect = self.text.get_rect(topleft=(self.x, self.y))

    def set_rect_into_rect(self):
        pygame.draw.rect(screen, self.background_color, self.text_rect)

    def draw(self):
        screen.blit(self.text, (self.x, self.y))

    def __init__(self, font_family, font_size, label, color, x, y, background_color, background=False):
        self.font_family = font_family
        self.font_size = font_size
        self.label = label
        self.color = color
        self.x = x
        self.y = y

        self.the_font = None
        self.text = None
        self.text_rect = None

        self.background = background
        if self.background:
            self.background_color = background_color


# TODO (3): Função para exibir conteúdos de texto referentes ao HP no canvas
def display_text_by_scenario(scenario, text_box):
    if scenario == 'in_game':
        for each_text in text_box:
            each_text.set_font()
            each_text.set_text()
            each_text.set_rect()
            each_text.set_rect_into_rect()
            each_text.draw()


# TODO (2): Criação dos conteúdos de texto referentes ao HP
texts_for_in_game = [
    Book(None, 40, controls['setup']['health_label'], 'white', 10, 50, 'black', True),
    Book(None, 40, controls['setup']['health'], 'white', 150, 50, 'black', True)
]


while True:
    screen.fill('#222222')

    events_watcher('player_movement')

    if controls['setup']['right_pressed']:
        player.horizontal_setup_right(10)
    if controls['setup']['left_pressed']:
        player.horizontal_setup_left(10)

    display_text_by_scenario('in_game', texts_for_in_game)  # TODO (4)

    player_health_admin(shell_box, player.idle_right_rectangles, texts_for_in_game[1], 0.25)  # TODO (10)

    exec_player_display_functions()

    exec_player_jumping_functions()

    print(enemy_collision('shell', shell_box, player.idle_right_rectangles))

    exec_enemy_class_functions('shell', shell_box)

    pygame.display.update()
    clock.tick(20)
