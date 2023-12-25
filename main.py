import sys
import os
import pygame


def possition(mouse_pos):
    return mouse_pos[0] // board.cell_size, mouse_pos[1] // board.cell_size


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
        self.cell_size = 68

    def set_view(self, cell_size):
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] is None:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), width=1)


class Unit(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite):  # нужный init для отсутсвия ошибок по PEP 8
        super().__init__(all_sprites)
        self.image = load_image(name_sprite, colorkey=(255, 255, 255))
        self.rect = self.image.get_rect()
        self.name = name_person
        self.count = 0
        self.count_static = 0

    def get_move(self):
        for key in move_map:
            if keys[key]:
                move = move_map[key]
                return move

    def animation(self, move):
        if self.count == 6:
            self.count = 0
        self.count += 1

        for fruit in fruit_sprites:
            if self.rect.colliderect(fruit):
                fruit.kill_fruit()
            else:
                fruit.static_animation()

        go = True

        for ice in ice_sprites:
            first = ice.rect.x < self.rect.x + move[0] * 2 < ice.rect.x + ice.rect.width and ice.rect.y < self.rect.y + \
                    move[1] * 2 < ice.rect.y + ice.rect.height
            second = ice.rect.x < self.rect.x + self.rect.width + move[
                0] * 2 < ice.rect.x + ice.rect.width and ice.rect.y < self.rect.y + self.rect.height + move[
                         1] * 2 < ice.rect.y + ice.rect.height
            if first or second:
                go = False

        if go:
            if move[0] == 1:
                list_anim_right = [load_image('right_anim/right_shag_1.png', colorkey=colorkey),
                                   load_image('right_anim/right_shag_2.png', colorkey=colorkey)]
                self.image = list_anim_right[self.count // 3 - 1]
                if self.rect.right < board.height * board.cell_size:  # для того чтобы не выходил за границы
                    self.rect.x += speed
            elif move[0] == -1:
                list_anim_left = [load_image('left_anim/left_shag_1.png', colorkey=colorkey),
                                  load_image('left_anim/left_shag_2.png', colorkey=colorkey)]
                self.image = list_anim_left[self.count // 3 - 1]
                if self.rect.left > 0:
                    self.rect.x -= speed

            elif move[1] == 1:
                list_anim_up = [load_image('front_anim/front_shag_1.png', colorkey=colorkey),
                                load_image('front_anim/front_shag_2.png', colorkey=colorkey)]
                self.image = list_anim_up[self.count // 3 - 1]
                if self.rect.bottom < board.width * board.cell_size:
                    self.rect.y += speed

            elif move[1] == -1:
                list_anim_down = [load_image('back_anim/back_shag_1.png', colorkey=colorkey),
                                  load_image('back_anim/back_shag_2.png', colorkey=colorkey)]
                self.image = list_anim_down[self.count // 3 - 1]
                if self.rect.top > 0:
                    self.rect.y -= speed

    def static_animation(self, move):
        if self.count_static == 12:
            self.count_static = 0

        for fruit in fruit_sprites:
            if self.rect.colliderect(fruit):
                fruit.kill_fruit()
            else:
                fruit.static_animation()
        self.count_static += 1
        if move[0] == 1:
            list_anim_right = [load_image('right_anim/right_stoit_1.png', colorkey=colorkey),
                               load_image('right_anim/right_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_right[self.count_static // 6 - 1]

        elif move[0] == -1:
            list_anim_left = [load_image('left_anim/left_stoit_1.png', colorkey=colorkey),
                              load_image('left_anim/left_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_left[self.count_static // 6 - 1]

        elif move[1] == 1:
            list_anim_down = [load_image('front_anim/front_stoit_1.png', colorkey=colorkey),
                              load_image('front_anim/front_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_down[self.count_static // 6 - 1]

        elif move[1] == -1:
            list_anim_up = [load_image('back_anim/back_stoit_1.png', colorkey=colorkey),
                            load_image('back_anim/back_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_up[self.count_static // 6 - 1]


class Fruit(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite, event_pos):  # нужный init для отсутсвия ошибок по PEP 8
        super().__init__(fruit_sprites)
        self.count = 0
        self.image = load_image(name_sprite, colorkey=colorkey)
        self.rect = self.image.get_rect()
        self.name = name_person
        self.eat_fruct = pygame.mixer.Sound('звук поедания фрукта.mpeg')
        self.eat_fruct.set_volume(0.3)
        self.rect.x, self.rect.y = [x * board.cell_size for x in possition(event_pos)]

    def static_animation(self):  # банан двигается
        if self.count == 12:
            self.count = 0
        self.count += 1
        list_anim_right = [load_image('fruct/banana.png', colorkey=colorkey),
                           load_image('fruct/banana2.png', colorkey=colorkey)]
        self.image = list_anim_right[self.count // 6 - 1]

    def kill_fruit(self):
        fruit_sprites.remove(self)
        self.eat_fruct.play()


class Ice(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite, event_pos):
        super().__init__(ice_sprites)
        self.count = 0
        self.flag = False
        self.image = load_image(name_sprite, colorkey=(255, 255, 255))
        self.rect = self.image.get_rect()
        self.name = name_person
        self.rect.x, self.rect.y = [x * board.cell_size for x in possition(event_pos)]

    def spawn_ice(self, move):
        if move[0] == 1:  # определяем куда смотрел дино последний раз
            x = (sprite_hero.rect.x // cell_size)  # смотрим на какой клетке стоял дино
            y = (sprite_hero.rect.y // cell_size)
            for i in range(x + 1, 20):
                sprite_ice = Ice('ice', 'ice/ice.png', (i * 68, y * 68))  # размещаем лёд
                for ice in ice_list:
                    if sprite_ice.rect.colliderect(ice):  # столкновение льда
                        self.flag = True
                        break
                if self.flag:
                    break
                ice_list.append(sprite_ice)  # добавляем в список

        elif move[0] == -1:
            x = (sprite_hero.rect.x // cell_size)
            y = (sprite_hero.rect.y // cell_size)
            for i in range(x - 1, -1, -1):
                sprite_ice = Ice('ice', 'ice/ice.png', (i * 68, y * 68))
                for ice in ice_list:
                    if sprite_ice.rect.colliderect(ice):  # столкновение льда
                        self.flag = True
                        break
                if self.flag:
                    break
                ice_list.append(sprite_ice)

        elif move[1] == -1:
            x = (sprite_hero.rect.x // cell_size)
            y = (sprite_hero.rect.y // cell_size)
            for i in range(y - 1, -1, -1):
                sprite_ice = Ice('ice', 'ice/ice.png', (x * 68, i * 68))
                for ice in ice_list:
                    if sprite_ice.rect.colliderect(ice):  # столкновение льда
                        self.flag = True
                        break
                if self.flag:
                    break
                ice_list.append(sprite_ice)

        elif move[1] == 1:
            x = (sprite_hero.rect.x // cell_size)
            y = (sprite_hero.rect.y // cell_size)
            for i in range(y + 1, 12):
                sprite_ice = Ice('ice', 'ice/ice.png', (x * 68, i * 68))
                for ice in ice_list:
                    if sprite_ice.rect.colliderect(ice):  # столкновение льда
                        self.flag = True
                        break
                if self.flag:
                    break
                ice_list.append(sprite_ice)

    def ice_animation(self):  # сделайте анимацию появления я хз как
        if self.count == 12:
            self.count = 0
        self.count += 1
        list_anim_right = [load_image('ice/ice.png', colorkey=colorkey),
                           load_image('ice/ice.png', colorkey=colorkey)]
        self.image = list_anim_right[self.count // 6 - 1]


if __name__ == '__main__':
    pygame.init()
    cell_size = 68
    size = wight, height = 68 * 20, 68 * 12
    screen = pygame.display.set_mode(size)
    board = Board(12, 20)
    pygame.display.set_caption('Фруктозавр')
    running = True

    all_sprites = pygame.sprite.Group()
    sprite_hero = Unit('hero', 'right_anim/right_stoit_1.png')

    ice_sprites = pygame.sprite.Group()
    fruit_sprites = pygame.sprite.Group()

    volume = 1  # значение от 0 до 1
    pygame.mixer.music.load('Звук в уровне.mp3')  # загрузили
    pygame.mixer.music.play(-1)  # бесконечное повторение мелодии
    pygame.mixer.music.set_volume(volume)  # изменить громкость

    fps = 30
    v = 250
    speed = v // fps
    clock = pygame.time.Clock()
    smotrit = (1, 0)
    ice_list = []
    smotrit_y = (1, 0)
    smotrit_x = (1, 0)
    while running:
        keys = pygame.key.get_pressed()
        move = sprite_hero.get_move()
        for event in pygame.event.get():
            pressed = pygame.mouse.get_pressed()  # проверка какая кнопка мыши нажата
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and pressed[0]:  # спавн бананчика
                sprite_banan = Fruit('banan', 'fruct/banana.png', event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # Спавн льда на пробел
                sprite_ice = Ice('ice', 'ice/ice.png', (-1, 0))
                sprite_ice.spawn_ice(smotrit)
        if move:
            sprite_hero.animation(move)
            smotrit = move
            if move[0] != 0:
                smotrit_x = move
            if move[1] != 0:
                smotrit_y = move
        else:
            x = sprite_hero.rect.x // cell_size
            y = sprite_hero.rect.y // cell_size
            if sprite_hero.rect.x % cell_size > 4:
                sprite_hero.animation(smotrit_x)
            if sprite_hero.rect.y % cell_size > 4:
                sprite_hero.animation(smotrit_y)
            sprite_hero.static_animation(smotrit)
        clock.tick(fps)
        screen.fill((0, 0, 0))
        board.render(screen)

        all_sprites.draw(screen)
        ice_sprites.draw(screen)
        fruit_sprites.draw(screen)
        pygame.display.flip()
