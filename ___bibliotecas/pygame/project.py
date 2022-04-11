

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
"""

import pygame
from random import choice
from collections import namedtuple


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

controls = {
    'setup': {
        'go_right': 0,
        'go_left': 0
    }
}

Images = namedtuple("Images", [
    'intro', 'background', 'hills', 'mario_world_surface', 'wolf', 'shell'
])

image_paths = Images(
    'assets\\players\\wolf_intro.png',
    'assets\\landscapes\\background.png',
    'assets\\landscapes\\hills.png',
    'assets\\surfaces\\mario_world_surface.png',
    'assets\\players\\wolf_idle_right_single_tr.png',
    'assets\\shells\\shell_cyan_single_tr.gif'
)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Teste')
clock = pygame.time.Clock()
game_active = None


# ALTERNATIVOS
def ink():
    from random import choice
    colors = [*range(0, 256)]
    red, green, blue = choice(colors), choice(colors), choice(colors)
    return red, green, blue


def text_generator():
    values = [*range(1, 10)]
    vowels = ['a', 'e', 'i', 'o', 'u']
    return f'{choice(vowels)}{choice(values)}{choice(vowels)}{choice(values)}{choice(vowels)}{choice(values)}'


def x_or_y_generator(horizontal=False, vertical=False):
    x = [*range(0, width + 1)]
    y = [*range(0, height + 1)]

    if horizontal:
        return choice(x)
    elif vertical:
        return choice(y)


# IMPORTANTES
def events_watcher_in_game():
    global controls
    for event in pygame.event.get():
        # Fechar o jogo ao apertar no "X"d
        if event.type == pygame.QUIT:
            exit(0)

        # Localização do mouse ao mexer
        if event.type == pygame.MOUSEMOTION:
            print('')  # print(event.pos)

        # Tecla apertada sem soltar
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('')  # print('Há uma tecla sendo pressionada')

        # Tecla solta
        if event.type == pygame.MOUSEBUTTONUP:
            print('')  # print('Uma tecla foi solta')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                controls['setup']['go_right'] = 10
            if event.key == pygame.K_a:
                controls['setup']['go_left'] = 10
            if event.key == pygame.K_w and player_rect.bottom >= height - surface_height:
                # No loop de animação o valor vai modificando
                player.gravity = -35
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                controls['setup']['go_right'] = 0
            if event.key == pygame.K_a:
                controls['setup']['go_left'] = 0


def events_watcher_for_intro():
    global game_active
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_active = True


def which_mouse_button():
    action = pygame.mouse.get_pressed()
    if action[0]:
        print('Botão <-')
    elif action[1]:
        print('Botão do centro')
    elif action[2]:
        print('Botão ->')


def score_counter(reset_engine):

    the_score = pygame.time.get_ticks() + reset_engine
    the_score_admin = pygame.time.get_ticks()
    current_score = round(the_score - the_score_admin)

    the_text = Language(None, 33, f'Score: [ {current_score} ]', ink(), 10, 10)
    the_text.text_config()
    the_text.rect()
    the_text.draw()


# ARMAZENAMENTO DE OBJETOS
landscapes = []
texts = []


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

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.gravity = 0
        self.image_rect = None


class Enemy:

    def rect(self):
        self.image_rect = pygame.transform.scale(self.image, (self.custom_width, self.custom_height)).get_rect(topleft=(self.x, self.y))
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


class Platform:

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y


class Language:

    def text_config(self):
        self.text_setup = pygame.font.Font(self.font_family, self.font_size)
        self.text_setup2 = self.text_setup.render(self.label, False, self.color)

    def rect(self):
        self.text_rect = self.text_setup2.get_rect(topleft=(self.x, self.y))

    def rect_into_rect(self):
        pygame.draw.rect(screen, 'darkcyan', self.text_rect)

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


texts.append(Language(None, 50, 'GAME OVER', ink(), 200, 200))
texts.append(Language(None, 20, 'Pressione ESC para continuar', ink(), 200, 250))

LanguageTuple = namedtuple('LanguageTuple', ['game_over', 'game_over_instruction'])
written_content = LanguageTuple(*texts)

landscapes.append(Landscape(image_paths.background, 0, 0))
landscapes.append(Landscape(image_paths.hills, 0, 0))

surface = Platform(image_paths.mario_world_surface, bottom_left_x, bottom_right_y - surface_height)
player = Player(image_paths.wolf, bottom_left_x, bottom_right_y - (player_height + surface_height))
shell_cyan = Enemy(image_paths.shell, bottom_right_x, bottom_right_y - (shell_height + surface_height), shell_width, shell_height)

player_rect = player.rect()
shell_cyan_rect = shell_cyan.rect()

line1 = Line(ink(), 0, 0, 600, 600, 10)
ellipse1 = Ellipse(ink(), 50, 200, 100, 100)


def introduction():
    screen.fill('#222222')
    intro = pygame.image.load(image_paths.intro).convert_alpha()
    intro_rect = intro.get_rect(topleft=(200, 200))
    screen.blit(intro, intro_rect)


# MÉTODOS DE CONFIGURAÇÃO (APÓS CRIAR OBJETOS)
def text_setup():

    text_index_counter = 0
    while text_index_counter < 50:
        texts.append(Language(None,
                              50,
                              text_generator(),
                              'red',
                              x_or_y_generator(True, False),
                              x_or_y_generator(False, True))
                     )
        text_index_counter += 1
        # text = Language(None, 50, 'Pygame', 'red', 100, 100)


def text_display():
    for index in texts:
        index.text_config()
        index.rect()
        # index.rect_into_rect()
        # index.draw()
    # choice(texts).draw()


text_setup()


# LOOP PRINCIPAL
while True:

    if game_active:

        # DETECTOR DE AÇÕES/EVENTOS
        events_watcher_in_game()

        "RECURSOS"
        # which_mouse_button()

        "RASCUNHOS DE FORMAS"
        # line1.draw(True)
        # ellipse1.draw()

        # VALORES INCREMENTÁVEIS
        player.gravity += 4.4
        score_admin += 0.06

        # IMAGENS PRIMÁRIAS
        for landscape in landscapes:
            landscape.draw()

        # CONFIGURAR TODOS OS TEXTOS DENTRO DE UMA VAR
        text_display()

        # GERENCIAMENTO DE PONTUAÇÃO
        score_counter(score_admin)

        surface.draw()

        # CRIAÇÃO
        player.rect_into_rect()
        player.draw()

        # MOVIMENTOS
        player.move('down', player.gravity)
        player.move('right', controls['setup']['go_right'])
        player.move('left', controls['setup']['go_left'])

        # GERENCIAMENTO
        player.reset_right(width, player_width_global)
        player.ground_interaction(height, surface_height)  # Em caso de problema, mover para o final

        # CRIAÇÃO
        shell_cyan.rect_into_rect()
        shell_cyan.draw_custom()

        # MOVIMENTO
        shell_cyan.move('left', 1)

        # CONGELAMENTO DOS FRAMES
        if shell_cyan_rect.colliderect(player_rect):
            game_active = False

        "RECURSOS TESTADOS"
        # player.location_with_mouse_hover()
        # print(player.collision_horizontal(shell_cyan_rect))

    # Quando o jogo parar
    if game_active is False:
        text_display()
        written_content.game_over.draw()
        written_content.game_over_instruction.draw()

        # Voltar ao jogo
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                controls['setup']['go_right'] = 0
                controls['setup']['go_left'] = 0
                player.gravity = 0
                player_rect.top = 0
                player_rect.left = 0
                score_admin = 0
                game_active = True

    if game_active is None:
        introduction()
        events_watcher_for_intro()

    pygame.display.update()
    clock.tick(60)
