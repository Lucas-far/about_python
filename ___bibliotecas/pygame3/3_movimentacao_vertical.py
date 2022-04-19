

"""
Exibir imagens, animar e configurar movimentação horizontal
"""

import pygame

width, height = 600, 600

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PROJETO')
clock = pygame.time.Clock()


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

    # TODO:
    @staticmethod
    def jump(player_object, this_much):
        player_object.gravity = this_much

    # TODO: Controlar a queda do jogador após a tecla K ser pressionada (do - p/ +)
    @staticmethod
    def fall(player_object, this_much):
        player_object.gravity += this_much

    # TODO: Atualizar o retângulo dos grupos de sprites de forma linear
    def move(self, where, value):
        if where == 'down':
            for rectangle in self.idle_right_rectangles:
                rectangle.bottom += value
            for rectangle in self.idle_left_rectangles:
                rectangle.bottom += value
            for rectangle in self.walk_right_rectangles:
                rectangle.bottom += value
            for rectangle in self.walk_left_rectangles:
                rectangle.bottom += value

    # TODO: Adicionar "True" em uma lista e retornar "True" cada vez que o jogador "saltar"
    def ground_interaction(self):

        canvas_height = 600
        surface_height = 61
        box = set([])

        # TODO: O valor de gravidade (self.gravity) é inicialmente 0
        # TODO: Quando a tecla W é pressionada, a gravidade é alterada por: Player.jump()
        # TODO: E por último, volta a zera nas condições abaixo (simulação de queda)
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

        self.gravity = 0  # TODO: Controle do salto

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
    # TODO: Configuração do salto
    player.move('down', player.gravity)
    player.fall(player, 5)
    player.ground_interaction()


def events_watcher(scenario):
    if scenario == 'player_movement':

        for event_in_game in pygame.event.get():
            if event_in_game.type == pygame.QUIT:
                exit(0)
            if event_in_game.type == pygame.KEYDOWN:
                # TODO: Adição da condição para o salto ("and" impede salto enquanto no ar)
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


while True:
    screen.fill('#222222')

    events_watcher('player_movement')

    if controls['setup']['right_pressed']:
        player.horizontal_setup_right(10)
    if controls['setup']['left_pressed']:
        player.horizontal_setup_left(10)

    exec_player_display_functions()

    # TODO: Execução da função que carrega as funções de classe referentes ao salto do jogador
    exec_player_jumping_functions()

    pygame.display.update()
    clock.tick(20)
