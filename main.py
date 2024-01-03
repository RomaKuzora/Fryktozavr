import sys
import os
import pygame


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['Заставка',
                  'Вывод построчно',
                  "здесь нужно писать правила игры и тд",
                  'нажмите любую кнопку чтобы начать игру']
    fon = pygame.transform.scale(load_image('ice/ice.png'), (68 * 20, 68 * 10 + 80))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                terminate()
            elif event1.type == pygame.KEYDOWN or \
                    event1.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)


def spawn_ice(last_move):  # перенес функцию т.к. она созадвала экземпляры класса в котором
    break_ice_flag = False
    # находилась и добавляла в левый список так не надо делать
    # у нас есть ice_sprites это группа спрайтов льда и еще добавил чтобы на доске клетка менялась с None на 'ice'
    # чтобы проверять потом по клеткам куда можно идти но что-то пошло не по плану и делайте дальше сами короче
    xx = sprite_hero.rect.x // board.cell_size  # смотрим на какой клетке стоял дино
    yy = sprite_hero.rect.y // board.cell_size
    if last_move[0] == 1:  # определяем куда смотрел дино последний раз
        for i in range(xx + shagg + 1, 20):
            if board.board[yy][xx + shagg + 1] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and not board.board[yy][i] or not break_ice_flag and board.board[yy][i] == 'ice' \
                    or board.board[yy][i] == 'block':
                break
            if board.board[yy][i] != 'ice' and not break_ice_flag:  # убрал спавн лишнего спрайта
                ice_list.append((yy, i))  # запоминаем на каих координатах ставим  лёд
            elif board.board[yy][i] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:
                    if i == (ices.rect.x // 68) and yy == (ices.rect.y // 68):
                        board.board[yy][i] = None
                        ices.kill_ice()

    elif last_move[0] == -1:
        for i in range(xx - 1, -1, -1):
            if board.board[yy][xx - 1] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and not board.board[yy][i] or not break_ice_flag and board.board[yy][i] == 'ice' \
                    or board.board[yy][i] == 'block':
                break
            if board.board[yy][i] != 'ice' and not break_ice_flag:  # убрал спавн лишнего спрайта
                ice_list.append((yy, i))  # запоминаем на каих координатах ставим  лёд
            elif board.board[yy][i] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:
                    if i == (ices.rect.x // 68) and yy == (ices.rect.y // 68):
                        board.board[yy][i] = None
                        ices.kill_ice()

    elif last_move[1] == -1:
        for i in range(yy - 1, -1, -1):
            if board.board[yy - 1][xx] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and not board.board[i][xx] or not break_ice_flag and board.board[i][xx] == 'ice' \
                    or board.board[i][xx] == 'block':
                break
            if board.board[i][xx] != 'ice' and not break_ice_flag:  # убрал спавн лишнего спрайта
                ice_list.append((i, xx))  # запоминаем на каих координатах ставим  лёд
            elif board.board[i][xx] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:
                    if xx == (ices.rect.x // 68) and i == (ices.rect.y // 68):
                        board.board[i][xx] = None
                        ices.kill_ice()

    elif last_move[1] == 1:
        for i in range(yy + shagg + 1, 12):
            if yy == 9:
                break
            if board.board[yy + shagg + 1][xx] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            try:
                # проверка столкновения льда и столкновения ломания (жесть какая-то)
                if break_ice_flag and not board.board[i][xx] or not break_ice_flag and board.board[i][xx] == 'ice' \
                        or board.board[i][xx] == 'block':
                    break
                if board.board[i][xx] != 'ice' and not break_ice_flag:  # убрал спавн лишнего спрайта
                    ice_list.append((i, xx))  # запоминаем на каих координатах ставим  лёд
                elif board.board[i][xx] == 'ice' and break_ice_flag:  # проверка на ломание
                    for ices in ice_sprites:
                        if xx == (ices.rect.x // 68) and i == (ices.rect.y // 68):
                            board.board[i][xx] = None
                            ices.kill_ice()
            except IndexError:
                pass


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
    def __init__(self, width, heightt):
        self.width = width
        self.height = heightt
        self.board = [[None] * width for _ in range(heightt)]
        self.cell_size = 68

    def set_view(self, cell_cize):
        self.cell_size = cell_cize

    def render(self, screen_1):
        for yy in range(len(self.board)):
            for xx in range(len(self.board[yy])):
                if self.board[yy][xx] is None:
                    pygame.draw.rect(screen_1, (0, 0, 0),
                                     (xx * self.cell_size, yy * self.cell_size, self.cell_size,
                                      self.cell_size),
                                     width=1)


class Unit(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite):
        super().__init__(all_sprites)
        self.image = load_image(name_sprite, colorkey=(255, 255, 255))
        self.rect = self.image.get_rect()
        self.name = name_person
        self.count = 0
        self.count_static = 0

    def get_move(self):
        for key in move_map:
            if keys[key]:
                move_last = move_map[key]
                return move_last

    def animation(self, last_move):
        if self.count == 12:
            self.count = 0
        self.count += 1

        for fruit in fruit_sprites:
            if self.rect.colliderect(fruit):
                fruit.kill_fruit()
            else:
                fruit.static_animation()
        last_pos = self.rect.x, self.rect.y
        flag1, flag2 = True, True
        speeda = speed
        for iice in ice_sprites:
            if self.rect.colliderect(iice):
                speeda = 0
                flag1 = False
                self.rect.x = last_pos_dino[0]
                self.rect.y = last_pos_dino[1]
                break
        for iron in iron_block_sprites:
            if self.rect.colliderect(iron):
                speeda = 0
                flag2 = False
                self.rect.x = last_pos_dino[0]
                self.rect.y = last_pos_dino[1]
                break
        if flag1 and flag2:
            speeda = speed

        if last_move[0] == 1:
            list_anim_right = [load_image('right_anim/right_shag_1.png', colorkey=colorkey),
                               load_image('right_anim/right_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_right[self.count // 6 - 1]
            if self.rect.right < board.width * board.cell_size:  # для того чтобы не выходил за границы
                self.rect.x += speeda
        elif last_move[0] == -1:
            list_anim_left = [load_image('left_anim/left_shag_1.png', colorkey=colorkey),
                              load_image('left_anim/left_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_left[self.count // 6 - 1]
            if self.rect.left > 0:
                self.rect.x -= speeda

        elif last_move[1] == 1:
            list_anim_up = [load_image('front_anim/front_shag_1.png', colorkey=colorkey),
                            load_image('front_anim/front_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_up[self.count // 6 - 1]
            if self.rect.bottom < (board.height * board.cell_size):
                self.rect.y += speeda

        elif last_move[1] == -1:
            list_anim_down = [load_image('back_anim/back_shag_1.png', colorkey=colorkey),
                              load_image('back_anim/back_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_down[self.count // 6 - 1]
            if self.rect.top > 0:
                self.rect.y -= speeda
        if speeda != 0:
            return last_pos
        else:
            return last_pos_dino

    def static_animation(self, last_move):
        if self.count_static == 24:
            self.count_static = 0

        for fruit in fruit_sprites:
            if self.rect.colliderect(fruit):
                fruit.kill_fruit()
            else:
                fruit.static_animation()
        self.count_static += 1
        if last_move[0] == 1:
            list_anim_right = [load_image('right_anim/right_stoit_1.png', colorkey=colorkey),
                               load_image('right_anim/right_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_right[self.count_static // 12 - 1]

        elif last_move[0] == -1:
            list_anim_left = [load_image('left_anim/left_stoit_1.png', colorkey=colorkey),
                              load_image('left_anim/left_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_left[self.count_static // 12 - 1]

        elif last_move[1] == 1:
            list_anim_down = [load_image('front_anim/front_stoit_1.png', colorkey=colorkey),
                              load_image('front_anim/front_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_down[self.count_static // 12 - 1]

        elif last_move[1] == -1:
            list_anim_up = [load_image('back_anim/back_stoit_1.png', colorkey=colorkey),
                            load_image('back_anim/back_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_up[self.count_static // 12 - 1]

    def spawn_ice_dino(self, last_move):
        if last_move[0] == 1:
            self.image = load_image('right_anim/right_break_or_place_ice.png', colorkey=colorkey)
        elif last_move[0] == -1:
            self.image = load_image('left_anim/left_break_or_place_ice.png', colorkey=colorkey)
        elif last_move[1] == 1:
            self.image = load_image('front_anim/front_break_or_place_ice.png', colorkey=colorkey)
        elif last_move[1] == -1:
            self.image = load_image('back_anim/back_break_or_place_ice.png', colorkey=colorkey)


class Fruit(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite, event_pos, can_eat):
        super().__init__(fruit_sprites)
        self.count = 0
        self.image = load_image(name_sprite, colorkey=colorkey)
        self.rect = self.image.get_rect()
        self.name = name_person
        self.eat_fruct = pygame.mixer.Sound('звук поедания фрукта.mpeg')
        self.eat_fruct.set_volume(0.3)
        self.rect.x, self.rect.y = [xx * board.cell_size for xx in possition(event_pos)]
        self.can_eat = can_eat

    def static_animation(self):  # банан двигается
        if self.count == 24:
            self.count = 0
        self.count += 1
        if self.name == 'banana':
            list_anim_right = [load_image('fruct/banana.png', colorkey=colorkey),
                               load_image('fruct/banana2.png', colorkey=colorkey)]
        elif self.name == 'cherry':
            list_anim_right = [load_image('fruct/cherry.png', colorkey=colorkey),
                               load_image('fruct/cherry2.png', colorkey=colorkey)]
        self.image = list_anim_right[self.count // 12 - 1]

    def kill_fruit(self):
        if self.can_eat:
            fruit_sprites.remove(self)
            self.eat_fruct.play()


class Ice(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite, event_pos):
        super().__init__(ice_sprites)
        self.count = 0
        self.flag = False
        self.image = load_image(name_sprite, colorkey=colorkey)
        self.rect = self.image.get_rect()
        self.name = name_person
        self.rect.x, self.rect.y = [xx * board.cell_size for xx in possition(event_pos)]

    def ice_animation(self):  # сделайте анимацию появления я хз как
        if self.count == 12:
            self.count = 0
        self.count += 1
        list_anim_right = [load_image('ice/ice.png', colorkey=colorkey),
                           load_image('ice/ice.png', colorkey=colorkey)]
        self.image = list_anim_right[self.count // 6 - 1]

    def kill_ice(self):
        ice_sprites.remove(self)


class IronBlock(pygame.sprite.Sprite):
    def __init__(self, name_sprite, event_pos):
        super().__init__(iron_block_sprites)
        self.image = load_image(name_sprite, colorkey=colorkey)
        self.rect = self.image.get_rect()
        self.name = 'block'
        self.rect.x, self.rect.y = [xx * board.cell_size for xx in possition(event_pos)]


if __name__ == '__main__':
    pygame.init()
    cell_size = 68
    size = wight, height = 68 * 20, 68 * 10 + 80
    screen = pygame.display.set_mode(size)
    board = Board(20, 10)
    pygame.display.set_caption('Фруктозавр')
    running = True

    all_sprites = pygame.sprite.Group()
    sprite_hero = Unit('hero', 'right_anim/right_stoit_1.png')

    ice_sprites = pygame.sprite.Group()
    fruit_sprites = pygame.sprite.Group()
    iron_block_sprites = pygame.sprite.Group()

    volume = 0.5  # значение от 0 до 1
    pygame.mixer.music.load('Звук в уровне.mp3')  # загрузили
    pygame.mixer.music.play(-1)  # бесконечное повторение мелодии
    pygame.mixer.music.set_volume(volume)  # изменить громкость

    fps = 60
    v = 160
    speed = v // fps
    clock = pygame.time.Clock()
    smotrit = (1, 0)
    smotrit_y = (1, 0)
    smotrit_x = (1, 0)
    count = 0
    ice_list = []
    flag_of_move = False
    dlina_ice_list = 0
    flag = False
    last_pos_dino = 0, 0
    sprite_ice = Ice('ice', 'ice/ice.png', (0, cell_size * 10))
    sprite_banana = Fruit('banana', 'fruct/banana.png', (cell_size, cell_size * 10), False)
    sprite_cherry = Fruit('cherry', 'fruct/cherry.png', (cell_size * 2, cell_size * 10), False)
    sprite_iron_block = IronBlock('block/block.png', (cell_size * 3, cell_size * 10))
    start_screen()
    while running:
        keys = pygame.key.get_pressed()
        move = sprite_hero.get_move()
        for event in pygame.event.get():
            pressed = pygame.mouse.get_pressed()  # проверка какая кнопка мыши нажата
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and pressed[0]:
                if possition(event.pos) == possition((sprite_banana.rect.x, sprite_banana.rect.y)):
                    flag = 'banana'
                elif possition(event.pos) == possition((sprite_ice.rect.x, sprite_ice.rect.y)):
                    flag = 'ice'
                elif possition(event.pos) == possition((sprite_cherry.rect.x, sprite_cherry.rect.y)):
                    flag = 'cherry'
                elif possition(event.pos) == possition((sprite_iron_block.rect.x, sprite_iron_block.rect.y)):
                    flag = 'block'
            if event.type == pygame.MOUSEBUTTONDOWN and pressed[2]:
                if flag == 'banana':
                    Fruit('banana', 'fruct/banana.png', event.pos, True)
                elif flag == 'cherry':
                    Fruit('cherry', 'fruct/cherry.png', event.pos, True)
                elif flag == 'ice':
                    try:
                        if not board.board[event.pos[1] // 68][event.pos[0] // 68]:
                            Ice('ice', 'ice/ice.png', event.pos)
                            board.board[event.pos[1] // 68][event.pos[0] // 68] = 'ice'
                    except IndexError:
                        pass
                elif flag == 'block':
                    try:
                        if board.board[event.pos[1] // 68][event.pos[0] // 68] != 'block':
                            IronBlock('block/block.png', event.pos)
                            board.board[event.pos[1] // 68][event.pos[0] // 68] = 'block'
                    except IndexError:
                        pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and count == 0:  # Спавн льда на пробел
                ice_list = []
                if move or flag_of_move:
                    shagg = 1
                else:
                    shagg = 0
                spawn_ice(smotrit)
                count = dlina_ice_list = len(ice_list)

        if dlina_ice_list != 0:
            board.board[ice_list[len(ice_list) - dlina_ice_list][0]][ice_list[len(ice_list) - dlina_ice_list][1]] \
                = 'ice'  # тоже самое что и board.board[y][i] или board.board[i][y] в spawn_ice
            sprite_ice = Ice('ice', 'ice/ice.png', (ice_list[len(ice_list) - dlina_ice_list][1] * 68,
                                                    ice_list[len(ice_list) - dlina_ice_list][0] * 68))
            for ice in ice_sprites:
                if sprite_ice.rect.colliderect(ice) and sprite_ice is not ice:  # столкновение льда
                    dlina_ice_list = 1
                    break
            dlina_ice_list -= 1
        if count != 0:
            move = None
            sprite_hero.spawn_ice_dino(smotrit)
            speed = 0
            count -= 1
        else:
            speed = v // fps
        if move:
            if count != 0:
                sprite_hero.spawn_ice_dino(smotrit)
            else:
                last_pos_dino = sprite_hero.animation(move)
            smotrit = move
            if move[0] != 0:
                smotrit_x = move
            if move[1] != 0:
                smotrit_y = move
        else:
            x = sprite_hero.rect.x // cell_size
            y = sprite_hero.rect.y // cell_size
            if sprite_hero.rect.x % cell_size > 4:
                last_pos_dino = sprite_hero.animation(smotrit_x)
                flag_of_move = True
            elif sprite_hero.rect.y % cell_size > 4:
                last_pos_dino = sprite_hero.animation(smotrit_y)
                flag_of_move = True
            else:
                flag_of_move = False
            if count != 0:
                sprite_hero.spawn_ice_dino(smotrit)
            else:
                sprite_hero.static_animation(smotrit)
        clock.tick(fps)
        screen.fill((255, 255, 255))
        board.render(screen)
        all_sprites.draw(screen)
        ice_sprites.draw(screen)
        fruit_sprites.draw(screen)
        iron_block_sprites.draw(screen)
        pygame.display.flip()