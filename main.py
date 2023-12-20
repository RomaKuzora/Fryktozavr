import sys
import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


move_map = {pygame.K_w: (0, -1),
            pygame.K_s: (0, 1),
            pygame.K_a: (-1, 0),
            pygame.K_d: (1, 0)}
colorkey = (255, 255, 255)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.cell_size = 34

    def set_view(self, cell_size):
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] is None:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), width=1)


class Unit(pygame.sprite.Sprite):
    def init(self, name_person, name_sprite):
        super().__init__(all_sprites)
        self.image = load_image(name_sprite, colorkey=(255, 255, 255))
        self.rect = self.image.get_rect()
        self.name = name_person
        self.count = 0

    def get_move(self):
        for key in move_map:
            if keys[key]:
                move = move_map[key]
                return move

    def animation(self, move):
        if self.count == 6:
            self.count = 0
        self.count += 1
        if move[0] == 1:
            list_anim_right = [load_image('right_anim/right_shag_1.png', colorkey=colorkey),
                               load_image('right_anim/right_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_right[self.count // 3 - 1]
            self.rect.x += speed
        elif move[0] == -1:
            list_anim_left = [load_image('left_anim/left_shag_1.png', colorkey=colorkey),
                              load_image('left_anim/left_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_left[self.count // 3 - 1]
            self.rect.x -= speed

        elif move[1] == 1:
            list_anim_up = [load_image('front_anim/front_shag_1.png', colorkey=colorkey),
                            load_image('front_anim/front_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_up[self.count // 3 - 1]
            self.rect.y += speed
            # тут очень нам надо чтобы вы сделали анимацию похода вниз

        elif move[1] == -1:
            list_anim_down = [load_image('back_anim/back_shag_1.png', colorkey=colorkey),
                              load_image('back_anim/back_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_down[self.count // 3 - 1]
            self.rect.y -= speed

    def static_animation(self, move):
        if self.count == 6:
            self.count = 0
        self.count += 1
        if move[0] == 1:
            list_anim_right = [load_image('right_anim/right_stoit_1.png', colorkey=colorkey),
                               load_image('right_anim/right_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_right[self.count // 3 - 1]

        elif move[0] == -1:
            list_anim_left = [load_image('left_anim/left_stoit_1.png', colorkey=colorkey),
                              load_image('left_anim/left_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_left[self.count // 3 - 1]

        elif move[1] == 1:
            list_anim_down = [load_image('front_anim/front_stoit_1.png', colorkey=colorkey),
                              load_image('front_anim/front_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_down[self.count // 3 - 1]

        elif move[1] == -1:
            list_anim_up = [load_image('back_anim/back_stoit_1.png', colorkey=colorkey),
                            load_image('back_anim/back_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_up[self.count // 3 - 1]



if __name__ == '__main__':
    pygame.init()

    size = wight, height = 68 * 12, 68 * 12
    screen = pygame.display.set_mode(size)
    board = Board(12 * 2, 12 * 2)
    pygame.display.set_caption('Фруктозавр')
    running = True

    all_sprites = pygame.sprite.Group()
    sprite_hero = Unit()
    sprite_hero.init('hero', 'right_anim/right_stoit_1.png')

    fps = 30
    v = 100
    speed = v // fps
    clock = pygame.time.Clock()
    smotrit = 1, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        move = sprite_hero.get_move()
        if move:
            sprite_hero.animation(move)
            smotrit = move
        else:
            sprite_hero.static_animation(smotrit)
        clock.tick(fps)
        screen.fill((0, 0, 0))
        board.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
