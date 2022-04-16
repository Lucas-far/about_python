

"""
DESENHAR RETÃNGULO
    rectangle = pygame.Surface((10, 10))
    rectangle.fill('Blue')

    NO LOOP
        screen.blit(rectangle, (0, 0))

FORMATOS DESENHADOS
    line = Line(ink(), 0, 0, 600, 600, 10)
    ellipse = Ellipse(ink(), 50, 200, 100, 100)

EVENTOS DE MOUSE
    # Localização do mouse ao mexer
    if event_in_game.type == pygame.MOUSEMOTION:
        print(event.pos)

    # Tecla apertada sem soltar
    if event_in_game.type == pygame.MOUSEBUTTONDOWN:
        print('Há uma tecla sendo pressionada')

    # Tecla solta
    if event_in_game.type == pygame.MOUSEBUTTONUP:
        print('Uma tecla foi solta')
"""

import pygame
from random import choice


def to_do_or_try():
    """

    """


game_active = None

score_admin = 0

width, height = 600, 600

bottom_left_x = 0
bottom_right_x = 600
bottom_right_y = 600

player_health = 100  # TODO <
player_height = 70
player_width_global = 70
player_live_location = 0

shell_width = 36
shell_height = 32
surface_height = 61

enemy_speed = [*range(0, 8)]

shell_types = ('shell_cyan', 'shell_green', 'shell_mud', 'shell_violet', 'shell_yellow')

images = {
    'setup': {
        'cover': 'assets\\players\\wolf_intro.png',
        'main_background': 'assets\\landscapes\\background.png',
        'landscape_hill': 'assets\\landscapes\\hills.png',
        'main_surface': 'assets\\surfaces\\mario_world_surface.png',
        'player': 'assets\\players\\wolf_idle_right_single_tr.png',
        'shell_cyan': 'assets\\shells\\shell_cyan_single_tr.gif',
        'shell_green': 'assets\\shells\\shell_green_single_tr.gif',
        'shell_mud': 'assets\\shells\\shell_mud_single_tr.gif',
        'shell_violet': 'assets\\shells\\shell_violet_single_tr.gif',
        'shell_yellow': 'assets\\shells\\shell_yellow_single_tr.gif'
    }
}

texts = {
    'setup': {
        'launch': 'JOGAR',
        'cease': 'GAME OVER',
        'continue': 'Pressione ESC para voltar ao MENU',
        # TODO <
        'health_label': 'Saúde: ',
        'health': f'{player_health}',
    }
}

controls = {
    'setup': {
        'go_right': 0,
        'go_left': 0
    }
}

player_moves = {
    'setup': {
        'walk_right_frame_1': 'assets\\players\\pygame\\walk_right_pic_1.png',
        'walk_right_frame_2': 'assets\\players\\pygame\\walk_right_pic_2.png',
        'walk_right_frame_3': 'assets\\players\\pygame\\walk_right_pic_3.png',
        'walk_right_frame_4': 'assets\\players\\pygame\\walk_right_pic_4.png',
        'walk_right_frame_5': 'assets\\players\\pygame\\walk_right_pic_5.png',
        'walk_right_frame_6': 'assets\\players\\pygame\\walk_right_pic_6.png',
        'walk_right_frame_7': 'assets\\players\\pygame\\walk_right_pic_7.png',
        'walk_right_frame_8': 'assets\\players\\pygame\\walk_right_pic_8.png',
        'walk_right_frame_9': 'assets\\players\\pygame\\walk_right_pic_9.png',
    }
}

# ARMAZENAMENTO DE OBJETOS
landscapes = []
texts_for_intro = []
texts_for_in_game = []
texts_for_fail = []
enemies = []
enemies_rect = []

# SETUP PRINCIPAL DO PYGAME
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PROJETO')
clock = pygame.time.Clock()


# UTILIDADES

def ink():
    from random import choice
    colors = [*range(0, 256)]
    red, green, blue = choice(colors), choice(colors), choice(colors)
    return red, green, blue


def text_generator():
    values = [*range(1, 10)]
    vowels = ['a', 'e', 'i', 'o', 'u']
    return f'{choice(vowels)}{choice(values)}{choice(vowels)}{choice(values)}{choice(vowels)}{choice(values)}'


def x_or_y_generator(canvas_width, canvas_height, horizontal=False, vertical=False):
    x = [*range(0, canvas_width + 1)]
    y = [*range(0, canvas_height + 1)]

    if horizontal:
        return choice(x)
    elif vertical:
        return choice(y)


def random_background(random, chosen_color):
    if random:
        return screen.fill(ink())
    return screen.fill(chosen_color)


def canvas_location_random():
    from random import choice

    # out_of_canvas = [*range(width + 100, 1_200 + 1)]
    out_of_canvas = [*range(width + 50, width + 50 + 1000)]
    return choice(out_of_canvas)


def which_mouse_button():
    action = pygame.mouse.get_pressed()
    if action[0]:
        print('Botão <-')
    elif action[1]:
        print('Botão do centro')
    elif action[2]:
        print('Botão ->')


def add_into(object_box, new_object):
    object_box.append(new_object)


# IMPORTANTES

def events_watcher(context_type):

    global controls, enemies, game_active, score_admin, player, player_rect, player_live_location

    if context_type == 'intro':
        mouse_left_click_pressed = pygame.mouse.get_pressed()[0]

        for event_intro in pygame.event.get():

            if event_intro.type == pygame.QUIT:
                exit(0)

            # Iniciar o jogo (sair da tela de entrada)
            if mouse_left_click_pressed \
                    and event_intro.pos[0] in element_dimension('play_button')[0] \
                    and event_intro.pos[1] in element_dimension('play_button')[1]:
                game_active = True

    elif context_type == 'in_game':
        for event_in_game in pygame.event.get():

            if event_in_game.type == pygame.QUIT:
                exit(0)

            if event_in_game.type == pygame.KEYDOWN:

                if event_in_game.key == pygame.K_d:
                    controls['setup']['go_right'] = 10

                    # TESTE
                    # player = player_walk_right_surfaces[1]
                    # player_rect = player_walk_right_rects[1]
                    # player_location_update(player_rect, player_live_location)
                    # print('-------------------------------------------------------------------------', player)
                    # print('-------------------------------------------------------------------------', player_rect)
                    # test_counter, counter_end = 0, 9
                    # while test_counter < counter_end:
                    #     player = player_walk_right_surfaces[test_counter]
                    #     player_rect = player_walk_right_rects[test_counter]
                    #     player_location_update(player_rect, player_live_location)
                    #     print('-------------------------------------------------------------------------', test_counter)
                    #     print('-------------------------------------------------------------------------', player)
                    #     print('-------------------------------------------------------------------------', player_rect)
                    #     test_counter += 1
                    # test_counter -= counter_end

                if event_in_game.key == pygame.K_a:
                    controls['setup']['go_left'] = 10

                if event_in_game.key == pygame.K_w and player_rect.bottom >= height - surface_height:
                    # No loop de animação o valor vai modificando
                    player.gravity = -50

            if event_in_game.type == pygame.KEYUP:
                if event_in_game.key == pygame.K_d:
                    controls['setup']['go_right'] = 0

                    # TESTE
                    # player = player_backup
                    # player_rect = player_rect_backup
                    # player_location_update(player_rect, player_live_location)

                if event_in_game.key == pygame.K_a:
                    controls['setup']['go_left'] = 0

    elif context_type == 'fail':

        for event_fail in pygame.event.get():

            if event_fail.type == pygame.QUIT:
                exit(0)

            if event_fail.type == pygame.KEYUP and event_fail.key == pygame.K_ESCAPE:
                game_active = None
                controls['setup']['go_right'] = 0
                controls['setup']['go_left'] = 0
                player.gravity = 0
                player_rect.top = 0
                player_rect.left = 0
                score_admin = 0


def element_dimension(element_name):
    if element_name == 'play_button':
        return range(200, 321), range(395, 426)


def score_counter(reset_engine):

    the_score = pygame.time.get_ticks() + reset_engine
    the_score_admin = pygame.time.get_ticks()
    current_score = round(the_score - the_score_admin)

    the_text = Language(None, 33, f'Score: [ {current_score} ]', ink(), 10, 10)
    the_text.text_config()
    the_text.rect()
    the_text.draw()


class Player:

    def rect(self):
        self.image_rect = pygame.transform.scale(self.image, (self.custom_width, self.custom_height)).get_rect(topleft=(self.x, self.y))
        return self.image_rect

    def rect_into_rect(self):
        pygame.draw.rect(screen, ink(), self.image_rect)

    def draw(self):
        screen.blit(self.image, self.image_rect)

    def draw_custom(self):
        screen.blit(pygame.transform.scale(self.image, (self.custom_width, self.custom_height)), self.image_rect)

    def move(self, where, value):
        if where == 'up':
            self.image_rect.top -= value
        elif where == 'right':
            self.image_rect.right += value
        elif where == 'down':
            self.image_rect.bottom += value
        elif where == 'left':
            self.image_rect.left -= value

    def stop(self):
        self.image_rect.top = 0
        self.image_rect.right = 0
        self.image_rect.bottom = 0
        self.image_rect.left = 0

    def reset_right(self, canvas_width, player_width):
        # Excedendo canto ->: resurgir no canto <-
        if self.image_rect.right > canvas_width + player_width:
            self.image_rect.left = -player_width + 30

    def collision_horizontal(self, target_rect):
        return self.image_rect.colliderect(target_rect)

    def location_with_mouse_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.image_rect.collidepoint(mouse_pos):
            print(mouse_pos)

    def ground_interaction(self, canvas_height, the_surface_height):
        if self.image_rect.bottom >= canvas_height - the_surface_height:
            self.gravity = 0
            self.image_rect.bottom = canvas_height - the_surface_height
            return True

    def landscape_motion(self):
        pass

    def __init__(self, image, x, y, custom_width, custom_height):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.custom_width = custom_width
        self.custom_height = custom_height
        self.gravity = 0
        self.image_rect = None

        self.walk_right_sprites = (
            'assets\\players\\pygame\\walk_right_pic_1.png',
            'assets\\players\\pygame\\walk_right_pic_2.png',
            'assets\\players\\pygame\\walk_right_pic_3.png',
            'assets\\players\\pygame\\walk_right_pic_4.png',
            'assets\\players\\pygame\\walk_right_pic_5.png',
            'assets\\players\\pygame\\walk_right_pic_6.png',
            'assets\\players\\pygame\\walk_right_pic_7.png',
            'assets\\players\\pygame\\walk_right_pic_8.png',
            'assets\\players\\pygame\\walk_right_pic_9.png'
        )

        self.walk_right_surfaces = [
            pygame.image.load(self.walk_right_sprites[0]).convert_alpha(),
            pygame.image.load(self.walk_right_sprites[1]).convert_alpha(),
            pygame.image.load(self.walk_right_sprites[2]).convert_alpha(),
            pygame.image.load(self.walk_right_sprites[3]).convert_alpha(),
            pygame.image.load(self.walk_right_sprites[4]).convert_alpha(),
            pygame.image.load(self.walk_right_sprites[5]).convert_alpha(),
            pygame.image.load(self.walk_right_sprites[6]).convert_alpha(),
            pygame.image.load(self.walk_right_sprites[7]).convert_alpha(),
            pygame.image.load(self.walk_right_sprites[8]).convert_alpha(),
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
            self.walk_right_surfaces[8].get_rect(topleft=(self.x, self.y)),
        ]


player = Player(images['setup']['player'], bottom_left_x, bottom_right_y - (player_height + surface_height), 70, 70)
player_backup = Player(images['setup']['player'], bottom_left_x, bottom_right_y - (player_height + surface_height), 70, 70)
player_rect = player.rect()
player_rect_backup = player_backup.rect()

player_walk_right_surfaces = []
player_walk_right_rects = []

# walk_right_counter = 0
# walk_right_frames = 9
# player_walk_right_surfaces2, player_walk_right_rects2 = player.animation_walk_right()
# print(player_walk_right_surfaces2)
# print(player_walk_right_rects2)


# TODO <
def player_health_admin(source_location, health_penalty):
    global game_active, player_health

    # Perda de saúde em caso de colisão
    print(enemy_collision('shell', enemies_rect, player_rect))
    if enemy_collision('shell', enemies_rect, player_rect):
        player_health -= health_penalty
        print(player_health)
        texts['setup']['health'] = f'{round(player_health)}'  # Atualização da vida na var fonte
        source_location.label = texts['setup']['health']      # Atualização da vida na tela

    # Reinicialização dos pontos
    if player_health <= 0:
        player_health = 100
        texts['setup']['health'] = f'{player_health}'
        source_location.label = texts['setup']['health']
        game_active = False


def score_at_danger(target_box, the_player_rectangle):
    global score_admin

    for enemy_rect in target_box:
        if the_player_rectangle.right - enemy_rect.right in [*range(20, 41)]:
            score_admin += 1


def back_onto_surface(player_image, this_much):
    player_image.gravity += this_much


def player_walk_right_config(image_box, rectangle_box, amount):
    surface_counter = 0
    while surface_counter < amount:
        image_box.append(
            Player(player_moves['setup'][f'walk_right_frame_{surface_counter + 1}'],
                   bottom_left_x, bottom_right_y - (player_height + surface_height), 70, 70
                   ))
        surface_counter += 1

    rectangle_counter = 0
    while rectangle_counter < amount:
        rectangle_box.append(image_box[rectangle_counter].rect())
        rectangle_counter += 1


def player_location(target_player_rect):

    temp_locations = [
        target_player_rect.top,
        target_player_rect.right,
        target_player_rect.bottom,
        target_player_rect.left,

        target_player_rect.centerx,
        target_player_rect.centery,

        target_player_rect.center,

        target_player_rect.midtop,
        target_player_rect.midright,
        target_player_rect.midbottom,
        target_player_rect.midleft,

        target_player_rect.topleft,
        target_player_rect.topright,
        target_player_rect.bottomleft,
        target_player_rect.bottomright
    ]

    return temp_locations


def player_location_update(chosen_player_rectangle, location_box):
    chosen_player_rectangle.top = location_box[0]
    chosen_player_rectangle.right = location_box[1]
    chosen_player_rectangle.bottom = location_box[2]
    chosen_player_rectangle.left = location_box[3]
    chosen_player_rectangle.centerx = location_box[4]
    chosen_player_rectangle.centery = location_box[5]
    chosen_player_rectangle.center = location_box[6]
    chosen_player_rectangle.midtop = location_box[7]
    chosen_player_rectangle.midright = location_box[8]
    chosen_player_rectangle.midbottom = location_box[9]
    chosen_player_rectangle.midleft = location_box[10]
    chosen_player_rectangle.topleft = location_box[11]
    chosen_player_rectangle.topright = location_box[12]
    chosen_player_rectangle.bottomleft = location_box[13]
    chosen_player_rectangle.bottomright = location_box[14]


player_walk_right_config(player_walk_right_surfaces, player_walk_right_rects, 9)


class Enemy:

    def rect(self):
        self.image_rect = pygame.transform.scale(self.image, (self.custom_width, self.custom_height)).get_rect(topleft=(self.x, self.y))
        return self.image_rect

    def rect_custom(self):
        self.image_rect = pygame.transform.rotozoom(self.image, 90, 2).get_rect(topleft=(self.x, self.y))
        return self.image_rect

    def rect_into_rect(self):
        pygame.draw.rect(screen, ink(), self.image_rect)

    def draw(self):
        screen.blit(self.image, self.image_rect)

    def draw_custom(self):
        screen.blit(pygame.transform.scale(self.image, (self.custom_width, self.custom_height)), self.image_rect)

    def move(self, where, value):
        if where == 'up':
            self.image_rect.top -= value
        elif where == 'right':
            self.image_rect.right += value
        elif where == 'down':
            self.image_rect.bottom += value
        elif where == 'left':
            self.image_rect.left -= value

    def stop(self):
        self.image_rect.top = 0
        self.image_rect.right = 0
        self.image_rect.bottom = 0
        self.image_rect.left = 0

    def __init__(self, image, x, y, custom_width, custom_height):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.custom_width = custom_width
        self.custom_height = custom_height
        self.image_rect = None


def enemy_create(image_box, rectangle_box, amount):
    enemy_counter = 0
    while enemy_counter < amount:
        image_box.append(
            Enemy(images['setup'][choice(shell_types)], canvas_location_random(), 600 - (32 + 61), 36, 32)
        )
        enemy_counter += 1

    enemy_rect_counter = 0
    while enemy_rect_counter < amount:
        rectangle_box.append(image_box[enemy_rect_counter].rect())
        enemy_rect_counter += 1


def enemy_display(target_box):
    for enemy in target_box:
        # enemy.rect_into_rect()
        enemy.draw_custom()
        enemy.move('left', choice(enemy_speed))


def enemy_collision(enemy_name, enemy_rect_box, player_rectangle):
    global game_active

    if enemy_name:
        for enemy_rect in enemy_rect_box:
            if enemy_rect.colliderect(player_rectangle):
                return True  # Perda de saúde


def enemy_removal_and_renewal(enemy_type, respawn_point, image_box, rectangle_box, counter, amount):
    if enemy_type == 'shell':
        for enemy_rect in rectangle_box:
            if enemy_rect.left < respawn_point:
                counter -= 1
                # print(counter)
            if counter == 0:
                counter += amount
                image_box.clear()
                rectangle_box.clear()
                enemy_create(image_box, rectangle_box, amount)


enemy_create(enemies, enemies_rect, 1)  # Relação: enemy_removal_and_renewal() [ par3 ]


class Image:

    def rect(self):
        self.image_rect = self.image.get_rect(topleft=(self.x, self.y))
        return self.image_rect

    def rect_into_rect(self):
        pygame.draw.rect(screen, ink(), self.image_rect)

    def draw(self):
        screen.blit(self.image, self.image_rect)

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.image_rect = None


class Line:
    def draw(self, chaser):
        """
        p1 = local / p2 = cor / p3 arg1 = x / p3 arg2 = y / p5 = espessura
        Sobre p4: se for passado as dimensões do canvas, uma linha \ é desenhada de uma ponta da tela a outra
        Sobre p4 arg1: quanto menor, mais próxima da <- a linha \ fica
        Sobre p4 arg2: quanto menor, mais próximo do topo a linha \ fica
        """
        if chaser:
            pygame.draw.line(screen, self.color, (self.x, self.y), pygame.mouse.get_pos(), self.thickness)
        else:
            pygame.draw.line(screen, self.color, (self.x, self.y), (self.x_width, self.y_height), self.thickness)

    def __init__(self, color, x, y, x_width, y_height, thickness):
        self.color = color
        self.x = x
        self.y = y
        self.x_width = x_width
        self.y_height = y_height
        self.thickness = thickness


class Ellipse:

    def draw(self):
        pygame.draw.ellipse(screen, self.color, pygame.Rect((self.x, self.y, self.ellipse_width, self.ellipse_height)))

    def __init__(self, color, x, y, ellipse_width, ellipse_height):
        self.color = color
        self.x = x
        self.y = y
        self.ellipse_width = ellipse_width
        self.ellipse_height = ellipse_height


class Rectangle:

    def draw(self):
        pass


class Landscape:

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y


add_into(landscapes, Landscape(images['setup']['main_background'], 0, 0))
add_into(landscapes, Landscape(images['setup']['landscape_hill'], 0, 0))


def landscape_display(target_box):
    for scenario in target_box:
        scenario.draw()


class Platform:

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y


surface = Platform(images['setup']['main_surface'], bottom_left_x, bottom_right_y - surface_height)


class Language:

    def text_config(self):
        self.text_setup = pygame.font.Font(self.font_family, self.font_size)
        self.text_setup2 = self.text_setup.render(self.label, False, self.color)

    def rect(self):
        self.text_rect = self.text_setup2.get_rect(topleft=(self.x, self.y))

    def rect_into_rect(self):
        pygame.draw.rect(screen, 'black', self.text_rect)

    def draw(self):
        screen.blit(self.text_setup2, (self.x, self.y))

    def __init__(self, font_family, font_size, label, color, x, y):
        self.font_family = font_family
        self.font_size = font_size
        self.label = label
        self.color = color
        self.x = x
        self.y = y
        self.color_random = ink()
        self.text_setup = None
        self.text_setup2 = None
        self.text_rect = None


# BOTÃO / interação = text_display() + TextsForIntro + written_content_when_intro
add_into(texts_for_intro, Language(None, 50, texts['setup']['launch'], ink(), 200, 395))
# TODO <
add_into(texts_for_in_game, Language(None, 40, texts['setup']['health_label'], ink(), 10, 50))
add_into(texts_for_in_game, Language(None, 40, texts['setup']['health'], ink(), 150, 50))
add_into(texts_for_fail, Language(None, 50, texts['setup']['cease'], ink(), 200, 200))
add_into(texts_for_fail, Language(None, 20, texts['setup']['continue'], ink(), 200, 250))


def text_display(scenario):
    if scenario == 'intro':
        for index in texts_for_intro:
            index.text_config()
            index.rect()
            index.rect_into_rect()

    elif scenario == 'in_game':
        for index in texts_for_in_game:
            index.text_config()
            index.rect()
            # index.rect_into_rect()

    elif scenario == 'fail':
        for index in texts_for_fail:
            index.text_config()
            index.rect()
            index.rect_into_rect()


def intro_display():
    # Desenho do lobo na tela
    intro = Image(images['setup']['cover'], 200, 200)
    intro.rect()
    intro.rect_into_rect()
    intro.draw()
    # Desenho do botão: JOGAR
    texts_for_intro[0].draw()


# obstacle_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(obstacle_timer, 900)

while True:

    # JOGO NÃO INICIADO
    if game_active is None:
        events_watcher('intro')
        random_background(False, '#222222')
        text_display('intro')
        intro_display()

    # JOGO EM ANDAMENTO
    if game_active:

        landscape_display(landscapes)

        events_watcher('in_game')

        text_display('in_game')
        texts_for_in_game[0].draw()
        texts_for_in_game[1].draw()

        player_health_admin(texts_for_in_game[1], 0.25)  # TODO <
        score_at_danger(enemies_rect, player_rect)
        score_counter(score_admin)
        back_onto_surface(player, 4.4)

        surface.draw()

        # player.rect_into_rect()
        player.draw_custom()
        player.move('down', player.gravity)
        player.move('right', controls['setup']['go_right'])
        player.move('left', controls['setup']['go_left'])
        player.reset_right(width, player_width_global)
        player.ground_interaction(height, surface_height)  # Em caso de problema, mover para o final

        # print('-------------------------------------------------------------------------------------------------------')
        player_live_location = player_location(player_rect)
        # print(player_live_location)
        # print('-------------------------------------------------------------------------------------------------------')

        # Criação: enemy_create() [ fora do loop + chamado no loop ]
        enemy_display(enemies)
        enemy_removal_and_renewal('shell', -100, enemies, enemies_rect, 1, 1)  # relação com: enemy_create()
        enemy_collision('shell', enemies_rect, player_rect)

    # GAME OVER
    if game_active is False:
        events_watcher('fail')
        text_display('fail')
        texts_for_fail[0].draw()
        texts_for_fail[1].draw()

    pygame.display.update()
    clock.tick(30)
