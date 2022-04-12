

"""
DESENHAR RETÃNGULO
    rectangle = pygame.Surface((10, 10))
    rectangle.fill('Blue')

    NO LOOP
        screen.blit(rectangle, (0, 0))

NOMEMCLATURA DAS TECLAS
    pygame
    Constant      ASCII   Description
    ---------------------------------
    K_BACKSPACE   \b      backspace
    K_TAB         \t      tab
    K_CLEAR               clear
    K_RETURN      \r      return
    K_PAUSE               pause
    K_ESCAPE      ^[      escape
    K_SPACE               space
    K_EXCLAIM     !       exclaim
    K_QUOTEDBL    "       quotedbl
    K_HASH        #       hash
    K_DOLLAR      $       dollar
    K_AMPERSAND   &       ampersand
    K_QUOTE               quote
    K_LEFTPAREN   (       left parenthesis
    K_RIGHTPAREN  )       right parenthesis
    K_ASTERISK    *       asterisk
    K_PLUS        +       plus sign
    K_COMMA       ,       comma
    K_MINUS       -       minus sign
    K_PERIOD      .       period
    K_SLASH       /       forward slash
    K_0           0       0
    K_1           1       1
    K_2           2       2
    K_3           3       3
    K_4           4       4
    K_5           5       5
    K_6           6       6
    K_7           7       7
    K_8           8       8
    K_9           9       9
    K_COLON       :       colon
    K_SEMICOLON   ;       semicolon
    K_LESS        <       less-than sign
    K_EQUALS      =       equals sign
    K_GREATER     >       greater-than sign
    K_QUESTION    ?       question mark
    K_AT          @       at
    K_LEFTBRACKET [       left bracket
    K_BACKSLASH   \       backslash
    K_RIGHTBRACKET ]      right bracket
    K_CARET       ^       caret
    K_UNDERSCORE  _       underscore
    K_BACKQUOTE   `       grave
    K_a           a       a
    K_b           b       b
    K_c           c       c
    K_d           d       d
    K_e           e       e
    K_f           f       f
    K_g           g       g
    K_h           h       h
    K_i           i       i
    K_j           j       j
    K_k           k       k
    K_l           l       l
    K_m           m       m
    K_n           n       n
    K_o           o       o
    K_p           p       p
    K_q           q       q
    K_r           r       r
    K_s           s       s
    K_t           t       t
    K_u           u       u
    K_v           v       v
    K_w           w       w
    K_x           x       x
    K_y           y       y
    K_z           z       z
    K_DELETE              delete
    K_KP0                 keypad 0
    K_KP1                 keypad 1
    K_KP2                 keypad 2
    K_KP3                 keypad 3
    K_KP4                 keypad 4
    K_KP5                 keypad 5
    K_KP6                 keypad 6
    K_KP7                 keypad 7
    K_KP8                 keypad 8
    K_KP9                 keypad 9
    K_KP_PERIOD   .       keypad period
    K_KP_DIVIDE   /       keypad divide
    K_KP_MULTIPLY *       keypad multiply
    K_KP_MINUS    -       keypad minus
    K_KP_PLUS     +       keypad plus
    K_KP_ENTER    \r      keypad enter
    K_KP_EQUALS   =       keypad equals
    K_UP                  up arrow
    K_DOWN                down arrow
    K_RIGHT               right arrow
    K_LEFT                left arrow
    K_INSERT              insert
    K_HOME                home
    K_END                 end
    K_PAGEUP              page up
    K_PAGEDOWN            page down
    K_F1                  F1
    K_F2                  F2
    K_F3                  F3
    K_F4                  F4
    K_F5                  F5
    K_F6                  F6
    K_F7                  F7
    K_F8                  F8
    K_F9                  F9
    K_F10                 F10
    K_F11                 F11
    K_F12                 F12
    K_F13                 F13
    K_F14                 F14
    K_F15                 F15
    K_NUMLOCK             numlock
    K_CAPSLOCK            capslock
    K_SCROLLOCK           scrollock
    K_RSHIFT              right shift
    K_LSHIFT              left shift
    K_RCTRL               right control
    K_LCTRL               left control
    K_RALT                right alt
    K_LALT                left alt
    K_RMETA               right meta
    K_LMETA               left meta
    K_LSUPER              left Windows key
    K_RSUPER              right Windows key
    K_MODE                mode shift
    K_HELP                help
    K_PRINT               print screen
    K_SYSREQ              sysrq
    K_BREAK               break
    K_MENU                menu
    K_POWER               power
    K_EURO                Euro
    K_AC_BACK             Android back button

RASCUNHO
    # MÉTODOS DE CONFIGURAÇÃO (APÓS CRIAR OBJETOS)
    # def text_setup():
    #
    #     text_index_counter = 0
    #     while text_index_counter < 50:
    #         texts.append(Language(None,
    #                               50,
    #                               text_generator(),
    #                               'red',
    #                               x_or_y_generator(True, False),
    #                               x_or_y_generator(False, True))
    #                      )
    #         text_index_counter += 1
            # text = Language(None, 50, 'Pygame', 'red', 100, 100)
"""

import pygame
from random import choice


def to_do_or_try():
    """
    Implementar saúde (levar danos ao invés de GAME OVER)
    Zerar a lista de inimigos quando atravessam a tela <-
    """


game_active = None

score_admin = 0

width, height = 600, 600

bottom_left_x = 0
bottom_right_x = 600
bottom_right_y = 600

player_height = 70
player_width_global = 70

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
        'continue': 'Pressione ESC para voltar ao MENU'
    }
}

controls = {
    'setup': {
        'go_right': 0,
        'go_left': 0
    }
}

# ARMAZENAMENTO DE OBJETOS
landscapes = []
texts_for_fail = []
texts_for_intro = []
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

    out_of_canvas = [*range(width + 100, 17_000 + 1)]
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

    global controls, enemies, game_active, score_admin

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

            # Localização do mouse ao mexer
            if event_in_game.type == pygame.MOUSEMOTION:
                print('')  # print(event.pos)

            # Tecla apertada sem soltar
            if event_in_game.type == pygame.MOUSEBUTTONDOWN:
                print('')  # print('Há uma tecla sendo pressionada')

            # Tecla solta
            if event_in_game.type == pygame.MOUSEBUTTONUP:
                print('')  # print('Uma tecla foi solta')

            if event_in_game.type == pygame.KEYDOWN:
                if event_in_game.key == pygame.K_d:
                    controls['setup']['go_right'] = 10
                if event_in_game.key == pygame.K_a:
                    controls['setup']['go_left'] = 10
                if event_in_game.key == pygame.K_w and player_rect.bottom >= height - surface_height:
                    # No loop de animação o valor vai modificando
                    player.gravity = -50

            if event_in_game.type == pygame.KEYUP:
                if event_in_game.key == pygame.K_d:
                    controls['setup']['go_right'] = 0
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

                # if player.ground_interaction(height, surface_height)


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
        self.image_rect = self.image.get_rect(topleft=(self.x, self.y))
        return self.image_rect

    def rect_into_rect(self):
        pygame.draw.rect(screen, ink(), self.image_rect)

    def draw(self):
        screen.blit(self.image, self.image_rect)

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

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.gravity = 0
        self.image_rect = None


def score_at_danger(target_box, the_player_rectangle):
    global score_admin

    for enemy_rect in target_box:
        if the_player_rectangle.right - enemy_rect.right in [*range(20, 41)]:
            score_admin += 1


def back_onto_surface(player_image, this_much):
    player_image.gravity += this_much


player = Player(images['setup']['player'], bottom_left_x, bottom_right_y - (player_height + surface_height))
player_rect = player.rect()


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
        screen.blit(pygame.transform.scale(self.image, (36, 32)), self.image_rect)

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


def enemy_collision(target_box, player_rectangle):
    global game_active

    for enemy_rect in target_box:
        if enemy_rect.colliderect(player_rectangle):
            game_active = False


enemy_create(enemies, enemies_rect, 100)


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
add_into(texts_for_fail, Language(None, 50, texts['setup']['cease'], ink(), 200, 200))
add_into(texts_for_fail, Language(None, 20, texts['setup']['continue'], ink(), 200, 250))


def text_display(scenario):
    if scenario == 'intro':
        for index in texts_for_intro:
            index.text_config()
            index.rect()
            index.rect_into_rect()
    elif scenario == 'in_game':
        pass
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


line1 = Line(ink(), 0, 0, 600, 600, 10)
ellipse1 = Ellipse(ink(), 50, 200, 100, 100)


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

        score_at_danger(enemies_rect, player_rect)
        score_counter(score_admin)
        back_onto_surface(player, 4.4)

        surface.draw()

        # player.rect_into_rect()
        player.draw()
        player.move('down', player.gravity)
        player.move('right', controls['setup']['go_right'])
        player.move('left', controls['setup']['go_left'])
        player.reset_right(width, player_width_global)
        player.ground_interaction(height, surface_height)  # Em caso de problema, mover para o final

        enemy_display(enemies)
        enemy_collision(enemies_rect, player_rect)

    # GAME OVER
    if game_active is False:
        events_watcher('fail')
        text_display('fail')
        texts_for_fail[0].draw()
        texts_for_fail[1].draw()

    pygame.display.update()
    clock.tick(30)
