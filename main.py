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


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    color = pygame.Color('black')
                elif self.board[y][x] == 1:
                    color = pygame.Color('blue')
                pygame.draw.rect(screen, color,
                                 (x * self.cell_size, y * self.cell_size, self.cell_size,
                                  self.cell_size))
                pygame.draw.rect(screen, pygame.Color('white'),
                                 (x * self.cell_size, y * self.cell_size, self.cell_size,
                                  self.cell_size), width=1)

    def make_ice(self):
        for y in range(self.height):
            for x in range(self.width):
                if 0 <= x <= 1 or 0 <= y <= 1:
                    self.board[y][x] = 1
                if self.width - 2 <= x <= self.width - 1 or self.height - 2 <= y <= self.height - 1:
                    self.board[y][x] = 1


class Unit(pygame.sprite.Sprite):
    def init(self):
        super().__init__()
        self.image = load_image("IceCream.png")
        self.rect = sprite_hero.image.get_rect()
        self.rect.x, self.rect.y = 130, 130

    def go(self, board, direction):
        # эта функция для проверки того может ли герой пойти в клетку или нет вдруг в той клетке лед
        value = (0, 0)
        if direction == 'left':
            value = (-25, 0)
        elif direction == 'right':
            value = (25, 0)
        elif direction == 'up':
            value = (0, 25)
        elif direction == 'down':
            value = (0, -25)
        # создание значения на которое будме менять координаты х и у
        x = (self.rect.x + 30) // board.cell_size
        y = (self.rect.y + 30) // board.cell_size
        # координаты клетки в которой герой
        self.rect.x += value[0]
        self.rect.y += value[1]


if __name__ == '__main__':
    pygame.init()

    size = wight, height = 800, 800
    screen = pygame.display.set_mode(size)
    board = Board(16, 16)
    pygame.display.set_caption('Bad Icecream')
    running = True

    all_sprites = pygame.sprite.Group()
    sprite_hero = Unit()
    sprite_hero.init()
    all_sprites.add(sprite_hero)
    # спрайт героя

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False

            elif keys[115]:
                sprite_hero.go(board, 'up')
            elif keys[119]:
                sprite_hero.go(board, 'down')
            elif keys[97]:
                sprite_hero.go(board, 'left')
            elif keys[100]:
                sprite_hero.go(board, 'right')
            # проверка на движение
        clock.tick(30)
        screen.fill((0, 0, 0))
        board.make_ice()
        board.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
