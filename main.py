import sys
import os
import pygame


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('start_windiws/start_okno.png'), (68 * 20, 68 * 10 + 80))
    screen.blit(fon, (0, 0))
    volum = 0.5
    pygame.mixer.music.load('Start_menu_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volum)
    all_sett = pygame.sprite.Group()
    setting = load_image("start_windiws/settings.png", colorkey=(255, 255, 255))
    settings = pygame.sprite.Sprite(all_sett)
    settings.image = setting
    settings.rect = settings.image.get_rect()
    settings.rect.x += 300
    settings.rect.y -= 750
    flaa = False
    flag_1, flag_2, flag_3, flag_4, flag_5 = True, True, True, True, True
    while True:
        if flaa:
            fon = pygame.transform.scale(load_image('start_windiws/start_okno.png'), (68 * 20, 68 * 10 + 80))
            screen.blit(fon, (0, 0))
            if flaa and settings.rect.y != -150:
                settings.rect.y += 25
            else:
                for event1 in pygame.event.get():
                    pressed1 = pygame.mouse.get_pressed()
                    if event1.type == pygame.QUIT:
                        terminate()
                    if event1.type == pygame.MOUSEMOTION:
                        if 1030 > event1.pos[0] > 980 and 150 > event1.pos[1] > 100:
                            setting = load_image("start_windiws/settings_close.png", colorkey=(255, 255, 255))
                            settings.image = setting
                            if flag_5:
                                pygame.mixer.Sound('zvuk_navedenie.mp3').play()
                                flag_5 = False
                        else:
                            setting = load_image("start_windiws/settings.png", colorkey=(255, 255, 255))
                            settings.image = setting
                            flag_5 = True
                    if event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 1030 > event1.pos[0] > 980 and 150 > \
                            event1.pos[1] > 100:
                        flaa = False
                        pygame.mixer.Sound('zvuk_settings_close.mp3').play()
                        break
        if flaa is False:
            if flaa is False and settings.rect.y != -750:
                settings.rect.y -= 600
            for event1 in pygame.event.get():
                pressed1 = pygame.mouse.get_pressed()
                if event1.type == pygame.QUIT:
                    terminate()
                if event1.type == pygame.MOUSEMOTION:
                    if 519 < event1.pos[0] < 838 and 126 < event1.pos[1] < 217:
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno_play.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        if flag_1:
                            pygame.mixer.Sound('zvuk_navedenie.mp3').play()
                        flag_1, flag_2, flag_3, flag_4 = False, True, True, True
                        screen.blit(fon, (0, 0))
                    elif 470 < event1.pos[0] < 894 and 236 < event1.pos[1] < 323:
                        if flag_2:
                            pygame.mixer.Sound('zvuk_navedenie.mp3').play()
                        flag_1, flag_2, flag_3, flag_4 = True, False, True, True
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno_redactor.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        screen.blit(fon, (0, 0))
                    elif 449 < event1.pos[0] < 938 and 342 < event1.pos[1] < 400:
                        if flag_3:
                            pygame.mixer.Sound('zvuk_navedenie.mp3').play()
                        flag_1, flag_2, flag_3, flag_4 = True, True, False, True
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno_person.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        screen.blit(fon, (0, 0))
                    elif 981 < event1.pos[0] < 1036 and 386 < event1.pos[1] < 441:
                        if flag_4:
                            pygame.mixer.Sound('zvuk_navedenie.mp3').play()
                        flag_1, flag_2, flag_3, flag_4 = True, True, True, False
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno_setting.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        screen.blit(fon, (0, 0))
                    else:
                        flag_1, flag_2, flag_3, flag_4 = True, True, True, True
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        screen.blit(fon, (0, 0))
                if event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 519 < event1.pos[0] < 838 \
                        and 126 < event1.pos[1] < 217:
                    pygame.mixer.Sound('zvuk_click.mp3').play()
                if event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 470 < event1.pos[0] < 894 \
                        and 236 < event1.pos[1] < 323:
                    pygame.mixer.Sound('zvuk_click.mp3').play()
                    pygame.mixer.music.stop()
                    return  # начинаем игру
                if event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 449 < event1.pos[0] < 938 \
                        and 342 < event1.pos[1] < 400:
                    pygame.mixer.Sound('zvuk_click.mp3').play()
                if event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 981 < event1.pos[0] < 1036 \
                        and 386 < event1.pos[1] < 441 and flaa is False:
                    if flaa is False:
                        pygame.mixer.Sound('zvuk_settings.mp3').play()
                        flaa = True
        all_sett.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def game_lose():
    pass


def game_win():
    pass


def spawn_ice(last_move):  # перенес функцию т.к. она созадвала экземпляры класса в котором
    break_ice_flag = False
    xx = sprite_hero.rect.x // board.cell_size  # смотрим на какой клетке стоял дино
    yy = sprite_hero.rect.y // board.cell_size
    if last_move[0] == 1:  # определяем куда смотрел дино последний раз
        for i in range(xx + shagg + 1, 20):
            if board.board[yy][xx + shagg + 1] == 'ice' or \
                    board.board[yy][xx + shagg] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and (not board.board[yy][i] and not board.board[yy][i - 1]) \
                    or not break_ice_flag and board.board[yy][i] == 'ice' \
                    or board.board[yy][i] == 'block' or (move and board.board[yy][i - 1] == 'block'):
                break
            if not break_ice_flag and not (move and board.board[yy][i - 1] == 'block'
                                           or board.board[yy][i] == 'block'):  # убрал спавн лишнего спрайта
                ice_list.append((yy, i))  # запоминаем на каих координатах ставим  лёд
            elif board.board[yy][i] == 'ice' and break_ice_flag or \
                    board.board[yy][i - 1] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:
                    if i == (ices.rect.x // 68) and yy == (ices.rect.y // 68):
                        board.board[yy][i] = None
                        ices.kill_ice()
                    if i - 1 == (ices.rect.x // 68) and yy == (ices.rect.y // 68) and move:
                        board.board[yy][i - 1] = None
                        ices.kill_ice()

    elif last_move[0] == -1:
        for i in range(xx - 1, -1, -1):
            if board.board[yy][xx - 1] == 'ice' or \
                    board.board[yy][xx] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and (not board.board[yy][i] and not board.board[yy][i + 1]) \
                    or not break_ice_flag and board.board[yy][i] == 'ice' \
                    or board.board[yy][i] == 'block' or (move and board.board[yy][i + 1] == 'block'):
                break
            if not break_ice_flag and not (move and board.board[yy][i + 1] == 'block'
                                           or board.board[yy][i] == 'block'):  # убрал спавн лишнего спрайта
                ice_list.append((yy, i))  # запоминаем на каих координатах ставим  лёд
            elif board.board[yy][i] == 'ice' and break_ice_flag or \
                    board.board[yy][i + 1] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:
                    if i == (ices.rect.x // 68) and yy == (ices.rect.y // 68):
                        board.board[yy][i] = None
                        ices.kill_ice()
                    if i + 1 == (ices.rect.x // 68) and yy == (ices.rect.y // 68) and move:
                        board.board[yy][i + 1] = None
                        ices.kill_ice()

    elif last_move[1] == -1:
        for i in range(yy - 1, -1, -1):
            if board.board[yy - 1][xx] == 'ice' or \
                    board.board[yy][xx] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and (not board.board[i][xx] and not board.board[i + 1][xx]) \
                    or not break_ice_flag and board.board[i][xx] == 'ice' \
                    or board.board[i][xx] == 'block' or (move and board.board[i + 1][xx] == 'block'):
                break
            if not break_ice_flag and not (move and board.board[i][xx] == 'block'
                                           or board.board[i][xx] == 'block'):  # убрал спавн лишнего спрайта
                ice_list.append((i, xx))  # запоминаем на каих координатах ставим  лёд
            elif board.board[i][xx] == 'ice' and break_ice_flag or \
                    board.board[i + 1][xx] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:
                    if xx == (ices.rect.x // 68) and i == (ices.rect.y // 68):
                        board.board[i][xx] = None
                        ices.kill_ice()
                    if xx == (ices.rect.x // 68) and i + 1 == (ices.rect.y // 68) and move:
                        board.board[i + 1][xx] = None
                        ices.kill_ice()

    elif last_move[1] == 1:
        for i in range(yy + shagg + 1, 12):
            if yy == 9 or yy == 8 and move:
                break
            if board.board[yy + shagg + 1][xx] == 'ice' or \
                    board.board[yy + shagg][xx] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            try:
                # проверка столкновения льда и столкновения ломания (жесть какая-то)
                if break_ice_flag and (not board.board[i][xx] and not board.board[i - 1][xx]) \
                        or not break_ice_flag and board.board[i][xx] == 'ice' \
                        or board.board[i][xx] == 'block' or (move and board.board[i - 1][xx] == 'block'):
                    break
                if not break_ice_flag and not (move and board.board[i][xx] == 'block'
                                               or board.board[i][xx] == 'block'):  # убрал спавн лишнего спрайта
                    ice_list.append((i, xx))  # запоминаем на каих координатах ставим  лёд
                elif board.board[i][xx] == 'ice' and break_ice_flag or \
                        board.board[i - 1][xx] == 'ice' and break_ice_flag:  # проверка на ломание
                    for ices in ice_sprites:
                        if xx == (ices.rect.x // 68) and i == (ices.rect.y // 68):
                            board.board[i][xx] = None
                            ices.kill_ice()
                        if xx == (ices.rect.x // 68) and i - 1 == (ices.rect.y // 68):
                            board.board[i - 1][xx] = None
                            ices.kill_ice()
            except IndexError:
                pass


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
    def __init__(self, width, heightt):
        self.width = width
        self.height = heightt
        self.board = [[None] * width for _ in range(heightt)]
        self.cell_size = 68

    def set_view(self, cell_cize):
        self.cell_size = cell_cize

    def render(self, screen_1):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] is None:
                    pygame.draw.rect(screen_1, (0, 0, 0),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size,
                                      self.cell_size),
                                     width=1)
                if self.board[y][x] == 'route':
                    pygame.draw.rect(screen_1, pygame.Color('red'),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size,
                                      self.cell_size),
                                     width=10)


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
            list_anim_right = [load_image('default_dino/right_anim/right_shag_1.png', colorkey=colorkey),
                               load_image('default_dino/right_anim/right_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_right[self.count // 6 - 1]
            if self.rect.right < board.width * board.cell_size:  # для того чтобы не выходил за границы
                self.rect.x += speeda
        elif last_move[0] == -1:
            list_anim_left = [load_image('default_dino/left_anim/left_shag_1.png', colorkey=colorkey),
                              load_image('default_dino/left_anim/left_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_left[self.count // 6 - 1]
            if self.rect.left > 0:
                self.rect.x -= speeda

        elif last_move[1] == 1:
            list_anim_up = [load_image('default_dino/front_anim/front_shag_1.png', colorkey=colorkey),
                            load_image('default_dino/front_anim/front_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_up[self.count // 6 - 1]
            if self.rect.bottom < (board.height * board.cell_size):
                self.rect.y += speeda

        elif last_move[1] == -1:
            list_anim_down = [load_image('default_dino/back_anim/back_shag_1.png', colorkey=colorkey),
                              load_image('default_dino/back_anim/back_shag_2.png', colorkey=colorkey)]
            self.image = list_anim_down[self.count // 6 - 1]
            if self.rect.top > 0:
                self.rect.y -= speeda
        if speeda != 0:
            return last_pos, flag1
        else:
            return last_pos_dino, flag1

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
            list_anim_right = [load_image('default_dino/right_anim/right_stoit_1.png', colorkey=colorkey),
                               load_image('default_dino/right_anim/right_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_right[self.count_static // 12 - 1]

        elif last_move[0] == -1:
            list_anim_left = [load_image('default_dino/left_anim/left_stoit_1.png', colorkey=colorkey),
                              load_image('default_dino/left_anim/left_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_left[self.count_static // 12 - 1]

        elif last_move[1] == 1:
            list_anim_down = [load_image('default_dino/front_anim/front_stoit_1.png', colorkey=colorkey),
                              load_image('default_dino/front_anim/front_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_down[self.count_static // 12 - 1]

        elif last_move[1] == -1:
            list_anim_up = [load_image('default_dino/back_anim/back_stoit_1.png', colorkey=colorkey),
                            load_image('default_dino/back_anim/back_stoit_2.png', colorkey=colorkey)]
            self.image = list_anim_up[self.count_static // 12 - 1]

    def spawn_ice_dino(self, last_move):
        if last_move[0] == 1:
            self.image = load_image('default_dino/right_anim/right_break_or_place_ice.png', colorkey=colorkey)
        elif last_move[0] == -1:
            self.image = load_image('default_dino/left_anim/left_break_or_place_ice.png', colorkey=colorkey)
        elif last_move[1] == 1:
            self.image = load_image('default_dino/front_anim/front_break_or_place_ice.png', colorkey=colorkey)
        elif last_move[1] == -1:
            self.image = load_image('default_dino/back_anim/back_break_or_place_ice.png', colorkey=colorkey)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name_sprite):
        super().__init__(enemy_sprites)
        self.image = load_image(name_sprite, colorkey=(255, 255, 255))
        self.rect = self.image.get_rect()
        self.count = 0
        self.count_static = 0
        self.route = []
        self.index = 0

    def set_posittion(self, event_pos):
        self.rect.x, self.rect.y = event_pos[0] * board.cell_size, event_pos[1] * board.cell_size

    def animation(self, last_move, go=True):
        if self.count_static == 48:
            self.count_static = 0
        self.count_static += 1

        if last_move[0] == 1:
            list_anim_right = [load_image('vrag/right_vrag.png', colorkey=colorkey),
                               load_image('vrag/right_vrag_2.png', colorkey=colorkey)]
            self.image = list_anim_right[self.count_static // 24 - 1]
            if go:
                self.rect.x += speed

        elif last_move[0] == -1:
            list_anim_left = [load_image('vrag/left_vrag.png', colorkey=colorkey),
                              load_image('vrag/left_vrag_2.png', colorkey=colorkey)]
            self.image = list_anim_left[self.count_static // 24 - 1]
            if go:
                self.rect.x -= speed

        elif last_move[1] == 1:
            list_anim_down = [load_image('vrag/front_vrag.png', colorkey=colorkey),
                              load_image('vrag/front_vrag_2.png', colorkey=colorkey)]
            self.image = list_anim_down[self.count_static // 24 - 1]
            if go:
                self.rect.y += speed

        elif last_move[1] == -1:
            list_anim_up = [load_image('vrag/back_vrag.png', colorkey=colorkey),
                            load_image('vrag/back_vrag_2.png', colorkey=colorkey)]
            self.image = list_anim_up[self.count_static // 24 - 1]
            if go:
                self.rect.y -= speed

    def go_go_zeppely(self):
        try:
            if self.index == len(self.route):
                self.index = 0
            x = self.route[self.index][0] * cell_size - self.rect.x
            y = self.route[self.index][1] * cell_size - self.rect.y
            if x > 0:
                x = 1
            if y > 0:
                y = 1
            if y < 0:
                y = -1
            if x < 0:
                x = -1
            last_move = (x, y)
            if self.route[self.index][0] * board.cell_size == self.rect.x and self.route[self.index][
                1] * board.cell_size == self.rect.y:
                self.index += 1
            else:
                self.animation(last_move)
        except Exception:
            pass
        try:
            if board.board[self.route[self.index][1]][self.route[self.index][0]] == 'ice':
                self.route.reverse()
                self.index = 0
        except IndexError:
            pass

    def set_route(self, list_click):
        self.route = list_click


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
        list_anim_right = list()
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

    def kill_block(self):
        iron_block_sprites.remove(self)


if __name__ == '__main__':
    pygame.init()
    cell_size = 68
    size = wight, height = 68 * 20, 68 * 10 + 80
    screen = pygame.display.set_mode(size)
    board = Board(20, 10)
    pygame.display.set_caption('Фруктозавр')
    running = True

    all_sprites = pygame.sprite.Group()
    sprite_hero = Unit('hero', 'default_dino/right_anim/right_stoit_1.png')

    ice_sprites = pygame.sprite.Group()
    fruit_sprites = pygame.sprite.Group()
    iron_block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    cursor = pygame.sprite.Group()

    fps = 60
    v = 120
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
    enemy_sprite = Enemy('vrag/front_vrag.png')
    enemy_sprite.rect.x, enemy_sprite.rect.y = cell_size * 4, cell_size * 10

    start_screen()
    flag_of_list_click = False
    volume = 0.5  # значение от 0 до 1
    pygame.mixer.music.load('Звук в уровне.mp3')  # загрузили
    pygame.mixer.music.play(-1)  # бесконечное повторение мелодии
    pygame.mixer.music.set_volume(volume)  # изменить громкость
    flaag = True
    _enemy_ = None
    list_click = []
    while running:
        keys = pygame.key.get_pressed()
        move = sprite_hero.get_move()
        for event in pygame.event.get():
            pressed = pygame.mouse.get_pressed()  # проверка какая кнопка мыши нажата
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:  # нужно релаизовать чтобы за мышкой следовал спрай, который мы выбрали
                if flag == 'banana':
                    pass
                elif flag == 'cherry':
                    pass
                elif flag == 'ice':
                    pass
                elif flag == 'block':
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN and pressed[0]:
                if flag_of_list_click and possition(event.pos)[1] != 10:
                    try:
                        list_click.append(possition(event.pos))
                        board.board[possition(event.pos)[1]][possition(event.pos)[0]] = 'route'
                        if possition(event.pos) == possition((_enemy_.rect.x, _enemy_.rect.y)):
                            flag_of_list_click = False
                            _enemy_.set_route(list_click)
                            list_click = []
                            _enemy_ = None
                    except Exception:
                        pass
                else:
                    if possition(event.pos) == (1, 10):
                        flag = 'banana'
                    elif possition(event.pos) == (0, 10):
                        flag = 'ice'
                    elif possition(event.pos) == (2, 10):
                        flag = 'cherry'
                    elif possition(event.pos) == (3, 10):
                        flag = 'block'
                    elif possition(event.pos) == (4, 10):
                        flag = 'enemy'
            if event.type == pygame.MOUSEBUTTONDOWN and pressed[2]:
                if flag == 'banana' and possition(event.pos)[1] != 10:
                    Fruit('banana', 'fruct/banana.png', event.pos, True)
                elif flag == 'cherry' and possition(event.pos)[1] != 10:
                    Fruit('cherry', 'fruct/cherry.png', event.pos, True)
                elif flag == 'ice':
                    if (event.pos[0] // cell_size) != (sprite_hero.rect.x // cell_size) \
                            or (event.pos[1] // cell_size) != (sprite_hero.rect.y // cell_size):
                        try:
                            if not board.board[event.pos[1] // 68][event.pos[0] // 68]:
                                Ice('ice', 'ice/ice.png', event.pos)
                                board.board[event.pos[1] // 68][event.pos[0] // 68] = 'ice'
                            else:
                                for ice in ice_sprites:
                                    if event.pos[1] // 68 == (ice.rect.y // 68) and \
                                            event.pos[0] // 68 == (ice.rect.x // 68):
                                        board.board[event.pos[1] // 68][event.pos[0] // 68] = None
                                        ice.kill_ice()
                        except IndexError:
                            pass
                elif flag == 'block':
                    if (event.pos[0] // cell_size) != (sprite_hero.rect.x // cell_size) \
                            or (event.pos[1] // cell_size) != (sprite_hero.rect.y // cell_size):
                        try:
                            if board.board[event.pos[1] // 68][event.pos[0] // 68] != 'block':
                                IronBlock('block/block.png', event.pos)
                                board.board[event.pos[1] // 68][event.pos[0] // 68] = 'block'
                            else:
                                for block in iron_block_sprites:
                                    if event.pos[1] // 68 == (block.rect.y // 68) and \
                                            event.pos[0] // 68 == (block.rect.x // 68):
                                        board.board[event.pos[1] // 68][event.pos[0] // 68] = None
                                        block.kill_block()
                        except IndexError:
                            pass
                elif flag == 'enemy':
                    if (event.pos[0] // cell_size) != (sprite_hero.rect.x // cell_size) \
                            or (event.pos[1] // cell_size) != (sprite_hero.rect.y // cell_size):
                        try:
                            if board.board[event.pos[1] // 68][event.pos[0] // 68] != 'block':
                                enemy_ = Enemy('vrag/front_vrag.png')
                                enemy_.set_posittion(possition(event.pos))
                                _enemy_ = enemy_
                                flag_of_list_click = True
                        except IndexError:
                            pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and count == 0:  # Спавн льда на пробел
                ice_list = []
                if move or flag_of_move:
                    if flaag:

                        shagg = 1
                    else:
                        shagg = 0
                else:
                    shagg = 0
                spawn_ice(smotrit)
                count = dlina_ice_list = len(ice_list)
        enemy_sprite.animation((0, 1), go=False)
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
                last_pos_dino, flaag = sprite_hero.animation(move)
            smotrit = move
            if move[0] != 0:
                smotrit_x = move
            if move[1] != 0:
                smotrit_y = move
        else:
            x = sprite_hero.rect.x // cell_size
            y = sprite_hero.rect.y // cell_size
            if sprite_hero.rect.x % cell_size != 0:
                if sprite_hero.rect.x % cell_size == speed // 2:
                    speed = 1
                last_pos_dino, flaag = sprite_hero.animation(smotrit_x)
                flag_of_move = True
            elif sprite_hero.rect.y % cell_size != 0:
                if sprite_hero.rect.x % cell_size == 1:
                    speed = 1
                last_pos_dino, flaag = sprite_hero.animation(smotrit_y)
                flag_of_move = True
            else:
                speed = v // fps
                flag_of_move = False
            if count != 0:
                sprite_hero.spawn_ice_dino(smotrit)
            else:
                sprite_hero.static_animation(smotrit)
        for enemy in enemy_sprites:
            if enemy != enemy_sprite:
                enemy.go_go_zeppely()
                if enemy.rect.colliderect(sprite_hero):
                    print(1)
                    game_lose()
        clock.tick(fps)
        screen.fill((255, 255, 255))
        board.render(screen)
        all_sprites.draw(screen)
        ice_sprites.draw(screen)
        fruit_sprites.draw(screen)
        iron_block_sprites.draw(screen)
        enemy_sprites.draw(screen)
        pygame.display.flip()
