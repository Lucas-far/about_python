
"""
<code=1>
<code=2>
<code=3>
<code=4>
<code=5>
<code=6>
<code=7>
<code=8>

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

player_live_location = player_location(player_rect)
"""

import pygame

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

player_live_location = None


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
            if self.current_sprite >= len(self.walk_right):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.walk_right_surfaces[self.current_sprite]
                self.image_rect = self.walk_right_rectangles[self.current_sprite]

        if not controls['setup']['right_pressed']:
            if self.current_sprite >= len(self.idle_right):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.idle_right_surfaces[self.current_sprite]
                self.image_rect = self.idle_right_rectangles[self.current_sprite]

        if controls['setup']['left_pressed']:
            if self.current_sprite >= len(self.walk_left):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.image = self.walk_left_surfaces[self.current_sprite]
                self.image_rect = self.walk_left_rectangles[self.current_sprite]

        # <code=7>
        if not controls['setup']['left_pressed']:
            if self.current_sprite >= len(self.idle_left):
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

    def player_rect(self):
        return self.image_rect

    def idle_at_right(self):
        return self.idle_right_rectangles

    def right(self):
        return self.walk_right_rectangles

    # <code=6>
    def idle_at_left(self):
        return self.idle_left_rectangles

    def left(self):
        return self.walk_left_rectangles

    def __init__(self):
        self.is_animating = False
        self.width = 70
        self.height = 70
        self.x = 0
        self.y = 600 - (70 + 61)

        # <code=2>
        self.idle_left = (
            'assets\\players\\idle_left\\wolf_idle_left_1_tr.png',
            'assets\\players\\idle_left\\wolf_idle_left_1_tr.png',
            'assets\\players\\idle_left\\wolf_idle_left_1_tr.png',
            'assets\\players\\idle_left\\wolf_idle_left_2_tr.png',
            'assets\\players\\idle_left\\wolf_idle_left_3_tr.png',
            'assets\\players\\idle_left\\wolf_idle_left_4_tr.png',
            'assets\\players\\idle_left\\wolf_idle_left_5_tr.png',
            'assets\\players\\idle_left\\wolf_idle_left_6_tr.png',
            'assets\\players\\idle_left\\wolf_idle_left_7_tr.png',
        )

        # <code=3>
        self.idle_left_surfaces = [
            pygame.image.load(self.idle_left[0]).convert_alpha(),
            pygame.image.load(self.idle_left[1]).convert_alpha(),
            pygame.image.load(self.idle_left[2]).convert_alpha(),
            pygame.image.load(self.idle_left[3]).convert_alpha(),
            pygame.image.load(self.idle_left[4]).convert_alpha(),
            pygame.image.load(self.idle_left[5]).convert_alpha(),
            pygame.image.load(self.idle_left[6]).convert_alpha(),
            pygame.image.load(self.idle_left[7]).convert_alpha(),
            pygame.image.load(self.idle_left[8]).convert_alpha(),
        ]

        # <code=4>
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

        self.idle_right = (
            'assets\\players\\idle_right\\wolf_idle_right_1_tr.png',
            'assets\\players\\idle_right\\wolf_idle_right_1_tr.png',
            'assets\\players\\idle_right\\wolf_idle_right_1_tr.png',
            'assets\\players\\idle_right\\wolf_idle_right_2_tr.png',
            'assets\\players\\idle_right\\wolf_idle_right_3_tr.png',
            'assets\\players\\idle_right\\wolf_idle_right_4_tr.png',
            'assets\\players\\idle_right\\wolf_idle_right_5_tr.png',
            'assets\\players\\idle_right\\wolf_idle_right_6_tr.png',
            'assets\\players\\idle_right\\wolf_idle_right_7_tr.png',
        )

        self.idle_right_surfaces = [
            pygame.image.load(self.idle_right[0]).convert_alpha(),
            pygame.image.load(self.idle_right[1]).convert_alpha(),
            pygame.image.load(self.idle_right[2]).convert_alpha(),
            pygame.image.load(self.idle_right[3]).convert_alpha(),
            pygame.image.load(self.idle_right[4]).convert_alpha(),
            pygame.image.load(self.idle_right[5]).convert_alpha(),
            pygame.image.load(self.idle_right[6]).convert_alpha(),
            pygame.image.load(self.idle_right[7]).convert_alpha(),
            pygame.image.load(self.idle_right[8]).convert_alpha(),
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

        self.walk_right = (
            'assets\\players\\walk_right\\walk_right_1_tr.png',
            'assets\\players\\walk_right\\walk_right_2_tr.png',
            'assets\\players\\walk_right\\walk_right_3_tr.png',
            'assets\\players\\walk_right\\walk_right_4_tr.png',
            'assets\\players\\walk_right\\walk_right_5_tr.png',
            'assets\\players\\walk_right\\walk_right_6_tr.png',
            'assets\\players\\walk_right\\walk_right_7_tr.png',
            'assets\\players\\walk_right\\walk_right_8_tr.png',
            'assets\\players\\walk_right\\walk_right_9_tr.png'
        )

        self.walk_right_surfaces = [
            pygame.image.load(self.walk_right[0]).convert_alpha(),
            pygame.image.load(self.walk_right[1]).convert_alpha(),
            pygame.image.load(self.walk_right[2]).convert_alpha(),
            pygame.image.load(self.walk_right[3]).convert_alpha(),
            pygame.image.load(self.walk_right[4]).convert_alpha(),
            pygame.image.load(self.walk_right[5]).convert_alpha(),
            pygame.image.load(self.walk_right[6]).convert_alpha(),
            pygame.image.load(self.walk_right[7]).convert_alpha(),
            pygame.image.load(self.walk_right[8]).convert_alpha(),
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

        self.walk_left = (
            'assets\\players\\walk_left\\walk_left_1_tr.png',
            'assets\\players\\walk_left\\walk_left_2_tr.png',
            'assets\\players\\walk_left\\walk_left_3_tr.png',
            'assets\\players\\walk_left\\walk_left_4_tr.png',
            'assets\\players\\walk_left\\walk_left_5_tr.png',
            'assets\\players\\walk_left\\walk_left_6_tr.png',
            'assets\\players\\walk_left\\walk_left_7_tr.png',
            'assets\\players\\walk_left\\walk_left_8_tr.png',
            'assets\\players\\walk_left\\walk_left_9_tr.png'
        )

        self.walk_left_surfaces = [
            pygame.image.load(self.walk_left[0]).convert_alpha(),
            pygame.image.load(self.walk_left[1]).convert_alpha(),
            pygame.image.load(self.walk_left[2]).convert_alpha(),
            pygame.image.load(self.walk_left[3]).convert_alpha(),
            pygame.image.load(self.walk_left[4]).convert_alpha(),
            pygame.image.load(self.walk_left[5]).convert_alpha(),
            pygame.image.load(self.walk_left[6]).convert_alpha(),
            pygame.image.load(self.walk_left[7]).convert_alpha(),
            pygame.image.load(self.walk_left[8]).convert_alpha(),
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

        # <code=5>
        if not controls['setup']['left_pressed']:
            self.image = self.idle_left_surfaces[self.current_sprite]
            self.image_rect = self.idle_left_rectangles[self.current_sprite]


player = Player()
player_rect = player.player_rect()


while True:
    screen.fill('#222222')

    # for event_in_game in pygame.event.get():
    #
    #     if event_in_game.type == pygame.KEYDOWN:
    #         if event_in_game.key == pygame.K_d:
    #             controls['setup']['right_pressed'] = True
    #             controls['setup']['go_right'] += 10
    #             for rectangle in player.right():
    #                 rectangle.right += controls['setup']['go_right']
    #             # player_rect.right += controls['setup']['go_right']
    #
    #     if event_in_game.type == pygame.KEYUP:
    #         if event_in_game.key == pygame.K_d:
    #             controls['setup']['right_pressed'] = False
    #             controls['setup']['go_right'] = 0
    #
    # if controls['setup']['right_pressed']:
    #     player.animate()
    #     player.update()

    for event_in_game in pygame.event.get():
        if event_in_game.type == pygame.KEYDOWN:
            if event_in_game.key == pygame.K_d:
                controls['setup']['right_pressed'] = True
                controls['setup']['right'] = True
                controls['setup']['left'] = False
            if event_in_game.key == pygame.K_a:
                controls['setup']['left_pressed'] = True
                controls['setup']['right'] = False
                controls['setup']['left'] = True

        if event_in_game.type == pygame.KEYUP:
            if event_in_game.key == pygame.K_d:
                controls['setup']['right_pressed'] = False
                controls['setup']['right'] = True
                controls['setup']['left'] = False
            if event_in_game.key == pygame.K_a:
                controls['setup']['left_pressed'] = False
                controls['setup']['right'] = False
                controls['setup']['left'] = True

    if controls['setup']['right_pressed']:
        for rectangle in player.right():
            rectangle.right += 10
        for rectangle in player.idle_at_right():
            rectangle.right += 10
        for rectangle in player.left():
            rectangle.left += 10
        for rectangle in player.idle_at_left():
            rectangle.left += 10

    if controls['setup']['left_pressed']:
        for rectangle in player.right():
            rectangle.right -= 10
        for rectangle in player.idle_at_right():
            rectangle.right -= 10
        for rectangle in player.left():
            rectangle.left -= 10
        for rectangle in player.idle_at_left():
            rectangle.left -= 10

    player.draw()
    player.animate()
    player.update()
    pygame.display.update()
    clock.tick(20)
