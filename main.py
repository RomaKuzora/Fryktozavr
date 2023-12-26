import sys
import os
import pygame


def spawn_ice(move):  # перенес функцию т.к. она созадвала экземпляры класса в котором
    # находилась и добавляла в левый список так не надо делать
    # у нас есть ice_sprites это группа спрайтов льда и еще добавил чтобы на доске клетка менялась с None на 'ice'
    # чтобы проверять потом по клеткам куда можно идти но что-то пошло не по плану и делайте дальше сами короче
    x = sprite_hero.rect.x // board.cell_size  # смотрим на какой клетке стоял дино
    y = sprite_hero.rect.y // board.cell_size
    if move[0] == 1:  # определяем куда смотрел дино последний раз
        for i in range(x + 1, 20):
            sprite_ice = Ice('ice', 'ice/ice.png', (i * 68, y * 68))
            board.board[y][i] = 'ice'
            for ice in ice_sprites:
                if sprite_ice.rect.colliderect(ice) and sprite_ice is not ice:  # столкновение льда
                    sprite_ice.flag = True
                    break
            if sprite_ice.flag:
                break

    elif move[0] == -1:
        for i in range(x - 1, -1, -1):
            sprite_ice = Ice('ice', 'ice/ice.png', (i * 68, y * 68))
            board.board[y][i] = 'ice'
            for ice in ice_sprites:
                if sprite_ice.rect.colliderect(ice) and sprite_ice is not ice:  # столкновение льда
                    sprite_ice.flag = True
                    break
            if sprite_ice.flag:
                break

    elif move[1] == -1:
        for i in range(y - 1, -1, -1):
            sprite_ice = Ice('ice', 'ice/ice.png', (x * 68, i * 68))
            board.board[i][x] = 'ice'
            for ice in ice_sprites:
                if sprite_ice.rect.colliderect(ice) and sprite_ice is not ice:  # столкновение льда
                    sprite_ice.flag = True
                    break
            if sprite_ice.flag:
                break

    elif move[1] == 1:
        for i in range(y + 1, 12):
            sprite_ice = Ice('ice', 'ice/ice.png', (x * 68, i * 68))
            board.board[i][x] = 'ice'
            for ice in ice_sprites:
                if sprite_ice.rect.colliderect(ice) and sprite_ice is not ice:  # столкновение льда
                    sprite_ice.flag = True
                    break
            if sprite_ice.flag:
                break


def possition(mouse_pos):
    return (mouse_pos[0] + 1) // board.cell_size, (mouse_pos[1] + 1) // board.cell_size


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
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] is None:
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
        # тут нужно сделать проверку на то что куда идет дино нету льда, через board.board там есть по клеткам где лед
        #pos_dino = list(possition((self.rect.x, self.rect.y)))
        #pos_dino[0] += move[0]
        #pos_dino[1] += move[1]

        #if board.board[pos_dino[0]][pos_dino[1]] == 'ice':
         #   print(pos_dino)
         #   go = False
         #  print(*board.board, sep='\n')
          #  print('\n\n')

        if go:
            if move[0] == 1:
                list_anim_right = [load_image('right_anim/right_shag_1.png', colorkey=colorkey),
                                   load_image('right_anim/right_shag_2.png', colorkey=colorkey)]
                self.image = list_anim_right[self.count // 3 - 1]
                if self.rect.right < board.width * board.cell_size:  # для того чтобы не выходил за границы
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
                if self.rect.bottom < board.height * board.cell_size:
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

    def spawn_ice_dino(self, move):
        if move[0] == 1:
            self.image = load_image('right_anim/right_break_or_place_ice.png', colorkey=colorkey)
        elif move[0] == -1:
            self.image = load_image('left_anim/left_break_or_place_ice.png', colorkey=colorkey)
        elif move[1] == 1:
            self.image = load_image('front_anim/front_break_or_place_ice.png', colorkey=colorkey)
        elif move[1] == -1:
            self.image = load_image('back_anim/back_break_or_place_ice.png', colorkey=colorkey)


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
    board = Board(20, 12)
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
    smotrit_y = (1, 0)
    smotrit_x = (1, 0)
    count = 0
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
                count = 10
                if move:
                    shagg = 1
                else:
                    shagg = 0
                spawn_ice(smotrit)
        if count != 0:
            sprite_hero.spawn_ice_dino(smotrit)
            speed = 0
            count -= 1
        else:
            speed = v // fps
        if move:
            if count != 0:
                sprite_hero.spawn_ice_dino(smotrit)
            else:
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
            if count != 0:
                sprite_hero.spawn_ice_dino(smotrit)
            else:
                sprite_hero.static_animation(smotrit)
        clock.tick(fps)
        screen.fill((0, 0, 0))
        board.render(screen)
        all_sprites.draw(screen)
        ice_sprites.draw(screen)
        fruit_sprites.draw(screen)
        pygame.display.flip()
