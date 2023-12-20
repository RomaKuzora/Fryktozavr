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
        self.board = [[None] * width for _ in range(height)]
        self.cell_size = 50

    def set_view(self, cell_size):
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] is None:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), width=1)
                elif self.board[x][y].name == 'hero':
                    self.board[x][y].rect.x, self.board[x][
                        y].rect.y = x * self.cell_size, y * self.cell_size


class Unit(pygame.sprite.Sprite):
    def init(self, name_person, name_sprite, x, y):
        super().__init__(all_sprites)
        self.image = load_image(name_sprite)
        self.rect = sprite_hero.image.get_rect()
        self.x, self.y = x, y
        self.name = name_person

    def go_down(self, board):
        if self.y + 1 < board.height:
            board.board[self.x][self.y + 1] = board.board[self.x][self.y]
            board.board[self.x][self.y] = None
            self.y += 1

    def go_up(self, board):
        if self.y - 1 >= 0:
            board.board[self.x][self.y - 1] = board.board[self.x][self.y]
            board.board[self.x][self.y] = None
            self.y -= 1

    def go_left(self, board):
        if self.x - 1 >= 0:
            board.board[self.x - 1][self.y] = board.board[self.x][self.y]
            board.board[self.x][self.y] = None
            self.x -= 1

    def go_right(self, board):
        if self.x + 1 < board.width:
            board.board[self.x + 1][self.y] = board.board[self.x][self.y]
            board.board[self.x][self.y] = None
            self.x += 1


if __name__ == '__main__':
    pygame.init()

    size = wight, height = 800, 800
    screen = pygame.display.set_mode(size)
    board = Board(16, 16)
    pygame.display.set_caption('Фруктозавр')
    running = True

    all_sprites = pygame.sprite.Group()
    sprite_hero = Unit()
    board.board[0][0] = sprite_hero
    sprite_hero.init('hero', 'shag_levo.png', 0, 0)

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if keys[115]:
                sprite_hero.go_down(board)
            if keys[119]:
                sprite_hero.go_up(board)
            if keys[97]:
                sprite_hero.go_left(board)
            if keys[100]:
                sprite_hero.go_right(board)

        clock.tick(30)
        screen.fill((0, 0, 0))
        board.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
