import sys
import os
import pygame

flag_redact = False
score = 0
LEVEL = None
flag_cherry = False
flag_limon = False


def terminate():
    pygame.quit()
    sys.exit()


def number(volumm):
    num1, num2 = 0, 0
    if volumm == 0.1:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/one.png", colorkeys=(255, 255, 255))
    elif volumm == 0.2:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/two.png", colorkeys=(255, 255, 255))
    elif volumm == 0.3:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/three.png", colorkeys=(255, 255, 255))
    elif volumm == 0.4:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/four.png", colorkeys=(255, 255, 255))
    elif volumm == 0.5:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/five.png", colorkeys=(255, 255, 255))
    elif volumm == 0.6:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/six.png", colorkeys=(255, 255, 255))
    elif volumm == 0.7:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/seven.png", colorkeys=(255, 255, 255))
    elif volumm == 0.8:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/eight.png", colorkeys=(255, 255, 255))
    elif volumm == 0.9:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/nine.png", colorkeys=(255, 255, 255))
    elif volumm == 1:
        num1 = load_image("start_windiws/numberss/one.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
    elif volumm == 0:
        num1 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
        num2 = load_image("start_windiws/numberss/zero.png", colorkeys=(255, 255, 255))
    return num1, num2


def start_screen():
    global volume, flag_redact, personalization, LEVEL, volum_effects, score
    fon = pygame.transform.scale(load_image('start_windiws/start_okno.png'), (68 * 20, 68 * 10 + 80))
    screen.blit(fon, (0, 0))
    skin_now = open("volume.txt")
    volum = 0.5
    volum_effects = 0
    for ii in skin_now:
        ii = ii.split(';')
        volum = float(ii[0])
        volume = float(ii[1])
        volum_effects = float(ii[2])
    skin_now.close()
    pygame.mixer.music.load('Start_menu_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volum)
    all_sett = pygame.sprite.Group()
    setting = load_image("start_windiws/settings.png", colorkeys=(255, 255, 255))
    settings = pygame.sprite.Sprite(all_sett)
    settings.image = setting
    settings.rect = settings.image.get_rect()
    settings.rect.x += 300
    settings.rect.y -= 750
    personal = load_image("personal/personal.png", colorkeys=(255, 255, 255))
    perso = pygame.sprite.Sprite(all_sett)
    perso.image = personal
    perso.rect = perso.image.get_rect()
    perso.rect.x += 280
    perso.rect.y -= 750
    lef = load_image("personal/left.png", colorkeys=(255, 255, 255))
    left = pygame.sprite.Sprite(all_sett)
    left.image = lef
    left.rect = left.image.get_rect()
    left.rect.x += 460
    left.rect.y -= 410
    rig = load_image("personal/right.png", colorkeys=(255, 255, 255))
    right = pygame.sprite.Sprite(all_sett)
    right.image = rig
    right.rect = right.image.get_rect()
    right.rect.x += 860
    right.rect.y -= 410
    plus1 = load_image("start_windiws/plus.png", colorkeys=(255, 255, 255))
    plus_1 = pygame.sprite.Sprite(all_sett)
    plus_1.image = plus1
    plus_1.rect = plus_1.image.get_rect()
    plus_1.rect.x += 800
    plus_1.rect.y = -380
    minus1 = load_image("start_windiws/minus.png", colorkeys=(255, 255, 255))
    minus_1 = pygame.sprite.Sprite(all_sett)
    minus_1.image = minus1
    minus_1.rect = minus_1.image.get_rect()
    minus_1.rect.x += 500
    minus_1.rect.y = -380
    plus2 = load_image("start_windiws/plus.png", colorkeys=(255, 255, 255))
    plus_2 = pygame.sprite.Sprite(all_sett)
    plus_2.image = plus2
    plus_2.rect = plus_2.image.get_rect()
    plus_2.rect.x += 800
    plus_2.rect.y = -260
    minus2 = load_image("start_windiws/minus.png", colorkeys=(255, 255, 255))
    minus_2 = pygame.sprite.Sprite(all_sett)
    minus_2.image = minus2
    minus_2.rect = minus_2.image.get_rect()
    minus_2.rect.x += 500
    minus_2.rect.y = -260
    plus3 = load_image("start_windiws/plus.png", colorkeys=(255, 255, 255))
    plus_3 = pygame.sprite.Sprite(all_sett)
    plus_3.image = plus3
    plus_3.rect = plus_3.image.get_rect()
    plus_3.rect.x += 800
    plus_3.rect.y = -140
    minus3 = load_image("start_windiws/minus.png", colorkeys=(255, 255, 255))
    minus_3 = pygame.sprite.Sprite(all_sett)
    minus_3.image = minus3
    minus_3.rect = minus_3.image.get_rect()
    minus_3.rect.x += 500
    minus_3.rect.y = -140
    num_2 = pygame.sprite.Sprite(all_sett)
    num1, num2 = number(volum)
    num_2.image = num2
    num_2.rect = num_2.image.get_rect()
    num_2.rect.x += 675
    num_2.rect.y = -380
    num_1 = pygame.sprite.Sprite(all_sett)
    num_1.image = num1
    num_1.rect = num_1.image.get_rect()
    num_1.rect.x += 625
    num_1.rect.y = -380
    num1, num2 = number(volume)
    num_3 = pygame.sprite.Sprite(all_sett)
    num_3.image = num2
    num_3.rect = num_3.image.get_rect()
    num_3.rect.x += 675
    num_3.rect.y = -260
    num_4 = pygame.sprite.Sprite(all_sett)
    num_4.image = num1
    num_4.rect = num_4.image.get_rect()
    num_4.rect.x += 625
    num_4.rect.y = -260
    num1, num2 = number(volum_effects)
    num_5 = pygame.sprite.Sprite(all_sett)
    num_5.image = num2
    num_5.rect = num_5.image.get_rect()
    num_5.rect.x += 675
    num_5.rect.y = -140
    num_6 = pygame.sprite.Sprite(all_sett)
    num_6.image = num1
    num_6.rect = num_6.image.get_rect()
    num_6.rect.x += 625
    num_6.rect.y = -140
    flaa = False
    fla = False
    flag_na_click = True
    flaagg = False
    flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8, flag_9, flag_10, flag_11, flag_12, flag_13, flag_14 \
        = True, True, True, True, True, True, True, True, True, True, True, True, True, True
    din = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
    dinos_list = ['default_dino', 'pink_dino', 'purple_dino', 'red_dino']
    a = open('personalization.txt')
    skin_now = a.read()
    ff = 0
    dd = 0
    if skin_now == 'default_dino':
        din = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
    elif skin_now == 'pink_dino':
        din = load_image(f"personal/dinop.png", colorkeys=(255, 255, 255))
    elif skin_now == 'purple_dino':
        din = load_image(f"personal/dinopu.png", colorkeys=(255, 255, 255))
    elif skin_now == 'red_dino':
        din = load_image(f"personal/dinor.png", colorkeys=(255, 255, 255))
    for len_dino in range(len(dinos_list)):
        if dinos_list[len_dino] == skin_now:
            try:
                ff = dinos_list[len_dino + 1]
            except IndexError:
                ff = dinos_list[0]
            try:
                dd = dinos_list[len_dino - 1]
            except IndexError:
                dd = dinos_list[-1]
    a.close()
    dino = pygame.sprite.Sprite(all_sett)
    dino.image = din
    dino.rect = dino.image.get_rect()
    dino.rect.x += 620
    dino.rect.y -= 420
    din2 = load_image("personal/dinop.png", colorkeys=(255, 255, 255))
    if ff == 'default_dino':
        din2 = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
    elif ff == 'pink_dino':
        din2 = load_image(f"personal/dinop.png", colorkeys=(255, 255, 255))
    elif ff == 'purple_dino':
        din2 = load_image(f"personal/dinopu.png", colorkeys=(255, 255, 255))
    elif ff == 'red_dino':
        din2 = load_image(f"personal/dinor.png", colorkeys=(255, 255, 255))
    dino2 = pygame.sprite.Sprite(all_sett)
    dino2.image = din2
    dino2.rect = dino2.image.get_rect()
    dino2.rect.x = -40
    dino2.rect.y -= 1020
    din3 = load_image("personal/dinop.png", colorkeys=(255, 255, 255))
    if dd == 'default_dino':
        din3 = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
    elif dd == 'pink_dino':
        din3 = load_image(f"personal/dinop.png", colorkeys=(255, 255, 255))
    elif dd == 'purple_dino':
        din3 = load_image(f"personal/dinopu.png", colorkeys=(255, 255, 255))
    elif dd == 'red_dino':
        din3 = load_image(f"personal/dinor.png", colorkeys=(255, 255, 255))
    dino3 = pygame.sprite.Sprite(all_sett)
    dino3.image = din3
    dino3.rect = dino2.image.get_rect()
    dino3.rect.x = -40
    dino3.rect.y -= 1020
    flaaag = False
    count_pashalka = 0
    pashalka = pygame.sprite.Group()
    pasg2 = load_image("personal/dinod.png", colorkeys=(255, 255, 255))
    if skin_now == 'default_dino':
        pasg2 = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
    elif skin_now == 'pink_dino':
        pasg2 = load_image(f"personal/dinop.png", colorkeys=(255, 255, 255))
    elif skin_now == 'purple_dino':
        pasg2 = load_image(f"personal/dinopu.png", colorkeys=(255, 255, 255))
    elif skin_now == 'red_dino':
        pasg2 = load_image(f"personal/dinor.png", colorkeys=(255, 255, 255))
    pash2 = pygame.sprite.Sprite(pashalka)
    pash2.image = pasg2
    pash2.rect = pash2.image.get_rect()
    pash2.rect.x = -150
    pash2.rect.y = 630
    pasg = load_image("start_windiws/pashalka.png", colorkeys=(255, 255, 255))
    pash = pygame.sprite.Sprite(pashalka)
    pash.image = pasg
    pash.rect = pash.image.get_rect()
    pash.rect.x = -150
    pash.rect.y = 630
    while True:
        if flaa:
            fon = pygame.transform.scale(load_image('start_windiws/start_okno.png'), (68 * 20, 68 * 10 + 80))
            screen.blit(fon, (0, 0))
            if flaa and settings.rect.y != -150:
                settings.rect.y += 25
                plus_1.rect.y += 25
                minus_1.rect.y += 25
                minus_2.rect.y += 25
                plus_2.rect.y += 25
                minus_3.rect.y += 25
                plus_3.rect.y += 25
                num_2.rect.y += 25
                num_1.rect.y += 25
                num_3.rect.y += 25
                num_4.rect.y += 25
                num_5.rect.y += 25
                num_6.rect.y += 25
            else:
                skin_now = open("volume.txt")
                for ii in skin_now:
                    ii = ii.split(';')
                    volum = float(ii[0])
                    volume = float(ii[1])
                    volum_effects = float(ii[2])
                skin_now.close()
                num1, num2 = number(volum)
                num_1.image = num1
                num_2.image = num2
                num1, num2 = number(volume)
                num_3.image = num2
                num_4.image = num1
                num1, num2 = number(volum_effects)
                num_5.image = num2
                num_6.image = num1
                for event1 in pygame.event.get():
                    pressed1 = pygame.mouse.get_pressed()
                    if event1.type == pygame.QUIT:
                        terminate()
                    if event1.type == pygame.MOUSEMOTION:
                        if 1030 > event1.pos[0] > 980 and 150 > event1.pos[1] > 100:
                            setting = load_image("start_windiws/settings_close.png", colorkeys=(255, 255, 255))
                            settings.image = setting
                            if flag_5:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_5 = False
                        elif 550 > event1.pos[0] > 495 and 260 > event1.pos[1] > 240:
                            minus1 = load_image("start_windiws/minus_pick.png", colorkeys=(255, 255, 255))
                            minus_1.image = minus1
                            if flag_6:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_6 = False
                        elif 850 > event1.pos[0] > 800 and 270 > event1.pos[1] > 215:
                            plus1 = load_image("start_windiws/plus_pick.png", colorkeys=(255, 255, 255))
                            plus_1.image = plus1
                            if flag_7:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_7 = False
                        elif 550 > event1.pos[0] > 495 and 370 > event1.pos[1] > 355:
                            minus2 = load_image("start_windiws/minus_pick.png", colorkeys=(255, 255, 255))
                            minus_2.image = minus2
                            if flag_8:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_8 = False
                        elif 850 > event1.pos[0] > 800 and 390 > event1.pos[1] > 335:
                            plus2 = load_image("start_windiws/plus_pick.png", colorkeys=(255, 255, 255))
                            plus_2.image = plus2
                            if flag_9:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_9 = False
                        elif 550 > event1.pos[0] > 495 and 490 > event1.pos[1] > 475:
                            minus3 = load_image("start_windiws/minus_pick.png", colorkeys=(255, 255, 255))
                            minus_3.image = minus3
                            if flag_10:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_10 = False
                        elif 850 > event1.pos[0] > 800 and 510 > event1.pos[1] > 455:
                            plus3 = load_image("start_windiws/plus_pick.png", colorkeys=(255, 255, 255))
                            plus_3.image = plus3
                            if flag_11:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_11 = False
                        else:
                            minus1 = load_image("start_windiws/minus.png", colorkeys=(255, 255, 255))
                            minus_1.image = minus1
                            plus1 = load_image("start_windiws/plus.png", colorkeys=(255, 255, 255))
                            plus_1.image = plus1
                            minus2 = load_image("start_windiws/minus.png", colorkeys=(255, 255, 255))
                            minus_2.image = minus2
                            plus2 = load_image("start_windiws/plus.png", colorkeys=(255, 255, 255))
                            plus_2.image = plus2
                            minus3 = load_image("start_windiws/minus.png", colorkeys=(255, 255, 255))
                            minus_3.image = minus3
                            plus3 = load_image("start_windiws/plus.png", colorkeys=(255, 255, 255))
                            plus_3.image = plus3
                            setting = load_image("start_windiws/settings.png", colorkeys=(255, 255, 255))
                            settings.image = setting
                            flag_5, flag_6, flag_7, flag_8, flag_9, flag_10, flag_11 \
                                = True, True, True, True, True, True, True
                    if event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 1030 > event1.pos[0] > 980 and 150 > \
                            event1.pos[1] > 100:
                        flaa = False
                        sound = pygame.mixer.Sound('zvuk_settings_close.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        break
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 550 > event1.pos[0] > 495 \
                            and 260 > event1.pos[1] > 240:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        if volum > 0:
                            volum -= 0.1
                            volum = round(volum, 1)
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 850 > event1.pos[0] > 800 \
                            and 270 > event1.pos[1] > 215:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        if volum < 1:
                            volum += 0.1
                            volum = round(volum, 1)
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 550 > event1.pos[0] > 495 \
                            and 370 > event1.pos[1] > 355:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        if volume > 0:
                            volume -= 0.1
                            volume = round(volume, 1)
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 850 > event1.pos[0] > 800 \
                            and 390 > event1.pos[1] > 335:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        if volume < 1:
                            volume += 0.1
                            volume = round(volume, 1)
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 550 > event1.pos[0] > 495 \
                            and 490 > event1.pos[1] > 475:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        if volum_effects > 0:
                            volum_effects -= 0.1
                            volum_effects = round(volum_effects, 1)
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 850 > event1.pos[0] > 800 \
                            and 510 > event1.pos[1] > 455:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        if volum_effects < 1:
                            volum_effects += 0.1
                            volum_effects = round(volum_effects, 1)
                    skin_now = open("volume.txt", 'w')
                    skin_now.write(f'{volum};{volume};{volum_effects}')
                    skin_now.close()
        elif fla:
            fon = pygame.transform.scale(load_image('start_windiws/start_okno.png'), (68 * 20, 68 * 10 + 80))
            screen.blit(fon, (0, 0))
            if fla and perso.rect.y != -100:
                perso.rect.y += 25
                left.rect.y += 25
                right.rect.y += 25
                dino.rect.y += 25
            else:
                for event1 in pygame.event.get():
                    pressed1 = pygame.mouse.get_pressed()
                    if event1.type == pygame.QUIT:
                        terminate()
                    elif event1.type == pygame.MOUSEMOTION:
                        if 1055 > event1.pos[0] > 1005 and 150 > event1.pos[1] > 100:
                            personal = load_image("personal/personal_close.png", colorkeys=(255, 255, 255))
                            perso.image = personal
                            if flag_12:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_12 = False
                        elif 525 > event1.pos[0] > 475 and 340 > event1.pos[1] > 240:
                            lef = load_image("personal/left_pick.png", colorkeys=(255, 255, 255))
                            left.image = lef
                            if flag_13:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_13 = False
                        elif 930 > event1.pos[0] > 880 and 340 > event1.pos[1] > 240:
                            rig = load_image("personal/right_pick.png", colorkeys=(255, 255, 255))
                            right.image = rig
                            if flag_14:
                                sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                                sound.set_volume(volum_effects)
                                sound.play()
                                flag_14 = False
                        else:
                            flag_12, flag_13, flag_14 = True, True, True
                            rig = load_image("personal/right.png", colorkeys=(255, 255, 255))
                            right.image = rig
                            lef = load_image("personal/left.png", colorkeys=(255, 255, 255))
                            left.image = lef
                            personal = load_image("personal/personal.png", colorkeys=(255, 255, 255))
                            perso.image = personal
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 1055 > event1.pos[0] > 1005 \
                            and 150 > event1.pos[1] > 100:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        perso.rect.y = - 750
                        left.rect.y = -410
                        right.rect.y = -410
                        dino.rect.y = -420
                        dino2.rect.x = -40
                        dino2.rect.y -= 1020
                        dino3.rect.x = -40
                        dino3.rect.y -= 1020
                        fla = False
                        a = open('personalization.txt')
                        personalization = a.read()
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 525 > event1.pos[0] > 475 \
                            and 340 > event1.pos[1] > 240 and flag_na_click:
                        flag_na_click = False
                        dino2.rect.x = 820
                        dino2.rect.y = 230
                        flaaag = True
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                    elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0] and 930 > event1.pos[0] > 880 \
                            and 340 > event1.pos[1] > 240 and flag_na_click:
                        dino3.rect.x = 420
                        dino3.rect.y = 230
                        flaagg = True
                        flag_na_click = False
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                if flaaag and dino2.rect.x != 620:
                    dino.rect.x -= 20
                    dino2.rect.x -= 20
                elif flaagg and dino3.rect.x != 620:
                    dino3.rect.x += 20
                    dino.rect.x += 20
                elif flaaag and dino2.rect.x == 620 or flaagg and dino3.rect.x:
                    dino.rect.x = 620
                    dino2.rect.x = -40
                    dino2.rect.y -= 1020
                    dino3.rect.x = -40
                    dino3.rect.y -= 1020
                    a = open('personalization.txt', 'w')
                    if flaaag:
                        a.write(ff)
                    elif flaagg:
                        a.write(dd)
                    a.close()
                    a = open('personalization.txt')
                    skin_now = a.read()
                    ff = 0
                    flag_na_click = True
                    pasg2 = load_image("personal/dinod.png", colorkeys=(255, 255, 255))
                    if skin_now == 'default_dino':
                        din = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
                        pasg2 = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
                    elif skin_now == 'pink_dino':
                        din = load_image(f"personal/dinop.png", colorkeys=(255, 255, 255))
                        pasg2 = load_image(f"personal/dinop.png", colorkeys=(255, 255, 255))
                    elif skin_now == 'purple_dino':
                        din = load_image(f"personal/dinopu.png", colorkeys=(255, 255, 255))
                        pasg2 = load_image(f"personal/dinopu.png", colorkeys=(255, 255, 255))
                    elif skin_now == 'red_dino':
                        din = load_image(f"personal/dinor.png", colorkeys=(255, 255, 255))
                        pasg2 = load_image(f"personal/dinor.png", colorkeys=(255, 255, 255))
                    pash2.image = pasg2
                    for ii in range(len(dinos_list)):
                        if dinos_list[ii] == skin_now:
                            try:
                                ff = dinos_list[ii + 1]
                            except IndexError:
                                ff = dinos_list[0]
                            try:
                                dd = dinos_list[ii - 1]
                            except IndexError:
                                dd = dinos_list[-1]
                    a.close()
                    din2 = load_image("personal/dinop.png", colorkeys=(255, 255, 255))
                    if ff == 'default_dino':
                        din2 = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
                    elif ff == 'pink_dino':
                        din2 = load_image(f"personal/dinop.png", colorkeys=(255, 255, 255))
                    elif ff == 'purple_dino':
                        din2 = load_image(f"personal/dinopu.png", colorkeys=(255, 255, 255))
                    elif ff == 'red_dino':
                        din2 = load_image(f"personal/dinor.png", colorkeys=(255, 255, 255))
                    din3 = load_image("personal/dinop.png", colorkeys=(255, 255, 255))
                    if dd == 'default_dino':
                        din3 = load_image(f"personal/dinod.png", colorkeys=(255, 255, 255))
                    elif dd == 'pink_dino':
                        din3 = load_image(f"personal/dinop.png", colorkeys=(255, 255, 255))
                    elif dd == 'purple_dino':
                        din3 = load_image(f"personal/dinopu.png", colorkeys=(255, 255, 255))
                    elif dd == 'red_dino':
                        din3 = load_image(f"personal/dinor.png", colorkeys=(255, 255, 255))
                    dino3.image = din3
                    dino2.image = din2
                    dino.image = din
                    flaaag = False
                    flaagg = False

        elif flaa is False and fla is False:
            if flaa is False and settings.rect.y != -750:
                settings.rect.y -= 600
                plus_1.rect.y = -380
                minus_1.rect.y = -380
                minus_2.rect.y = -260
                plus_2.rect.y = -260
                plus_3.rect.y = -140
                minus_3.rect.y = -140
                num_2.rect.y = - 380
                num_1.rect.y = -380
                num_3.rect.y = -260
                num_4.rect.y = -260
                num_5.rect.y = -140
                num_6.rect.y = -140
            for event1 in pygame.event.get():
                pashalka.draw(screen)
                pressed1 = pygame.mouse.get_pressed()
                if event1.type == pygame.QUIT:
                    terminate()
                elif event1.type == pygame.MOUSEMOTION:
                    if 519 < event1.pos[0] < 838 and 126 < event1.pos[1] < 217 and count_pashalka != 10:
                        count_pashalka = 0
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno_play.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        if flag_1:
                            sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                            sound.set_volume(volum_effects)
                            sound.play()
                        flag_1, flag_2, flag_3, flag_4 = False, True, True, True
                        screen.blit(fon, (0, 0))
                    elif 470 < event1.pos[0] < 894 and 236 < event1.pos[1] < 323 and count_pashalka != 10:
                        count_pashalka = 0
                        if flag_2:
                            sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                            sound.set_volume(volum_effects)
                            sound.play()
                        flag_1, flag_2, flag_3, flag_4 = True, False, True, True
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno_redactor.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        screen.blit(fon, (0, 0))
                    elif 449 < event1.pos[0] < 938 and 342 < event1.pos[1] < 400 and count_pashalka != 10:
                        count_pashalka = 0
                        if flag_3:
                            sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                            sound.set_volume(volum_effects)
                            sound.play()
                        flag_1, flag_2, flag_3, flag_4 = True, True, False, True
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno_person.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        screen.blit(fon, (0, 0))
                    elif 981 < event1.pos[0] < 1036 and 386 < event1.pos[1] < 441 and count_pashalka != 10:
                        count_pashalka = 0
                        if flag_4:
                            sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                            sound.set_volume(volum_effects)
                            sound.play()
                        flag_1, flag_2, flag_3, flag_4 = True, True, True, False
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno_setting.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        screen.blit(fon, (0, 0))
                    else:
                        flag_1, flag_2, flag_3, flag_4 = True, True, True, True
                        fon = pygame.transform.scale(load_image('start_windiws/start_okno.png'),
                                                     (68 * 20, 68 * 10 + 80))
                        screen.blit(fon, (0, 0))
                    if count_pashalka == 10 and pash2.rect.x == 1400:
                        count_pashalka = 0
                elif event1.type == pygame.MOUSEBUTTONDOWN and pressed1[0]:
                    if 519 < event1.pos[0] < 838 and 126 < event1.pos[1] < 217 and count_pashalka != 10:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        pygame.mixer.music.stop()
                        a = open('personalization.txt')
                        personalization = a.read()
                        a.close()
                        flag_redact = False
                        level = choose_level(volum_effects, volum)
                        LEVEL = level
                        start_level(level)
                        return
                    elif 470 < event1.pos[0] < 894 and 236 < event1.pos[1] < 323 and count_pashalka != 10:
                        sound = pygame.mixer.Sound('zvuk_click.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        a = open('personalization.txt')
                        personalization = a.read()
                        a.close()
                        pygame.mixer.music.stop()
                        flag_redact = True
                        return  # начинаем игру
                    elif 449 < event1.pos[0] < 938 and 342 < event1.pos[1] < 400 and count_pashalka != 10:
                        sound = pygame.mixer.Sound('zvuk_settings.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                        fla = True
                    elif 981 < event1.pos[0] < 1036 and 386 < event1.pos[1] < 441 \
                            and flaa is False and count_pashalka != 10:
                        if flaa is False:
                            sound = pygame.mixer.Sound('zvuk_settings.mp3')
                            sound.set_volume(volum_effects)
                            sound.play()
                            flaa = True
                    elif 500 < event1.pos[0] < 864 and 30 < event1.pos[1] < 90 and count_pashalka != 10:
                        count_pashalka += 1
                        if count_pashalka == 10:
                            pash.rect.x = 150
                            pash.rect.y = 650
                            pash2.rect.x = 0
                            pash2.rect.y = 630
            if count_pashalka == 10 and pash2.rect.x != 1400:
                pash2.rect.x += 10
                pash.rect.x += 10
        screen.blit(fon, (0, 0))
        pashalka.draw(screen)
        all_sett.draw(screen)
        pygame.mixer.music.set_volume(volum)
        pygame.display.flip()
        clock.tick(fps)


def game_lose():
    pass


def game_win():
    print(123)


def choose_level(volume_effects, volum):
    pygame.font.init()
    flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8, flag_9, flag_10 \
        = True, True, True, True, True, True, True, True, True, True
    pygame.mixer.music.load('zvuk_level.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volum)
    fon = pygame.transform.scale(load_image('start_windiws/level.png'), (68 * 20, 68 * 10 + 80))
    screen.blit(fon, (0, 0))
    while True:
        pressed3 = pygame.mouse.get_pressed()  # проверка какая кнопка мыши нажата
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                terminate()
            elif event2.type == pygame.MOUSEMOTION:
                if 272 > event2.pos[0] > 113 and 290 > event2.pos[1] > 113:
                    fon = pygame.transform.scale(load_image('start_windiws/level1.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_1:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_1 = False
                elif 360 < event2.pos[0] < 528 and 290 > event2.pos[1] > 113:
                    fon = pygame.transform.scale(load_image('start_windiws/level2.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_2:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_2 = False
                elif 600 < event2.pos[0] < 768 and 290 > event2.pos[1] > 113:
                    fon = pygame.transform.scale(load_image('start_windiws/level3.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_3:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_3 = False
                elif 840 < event2.pos[0] < 1008 and 290 > event2.pos[1] > 113:
                    fon = pygame.transform.scale(load_image('start_windiws/level4.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_4:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_4 = False
                elif 1080 < event2.pos[0] < 1248 and 290 > event2.pos[1] > 113:
                    fon = pygame.transform.scale(load_image('start_windiws/level5.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_5:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_5 = False
                elif 120 < event2.pos[0] < 288 and 450 < event2.pos[1] < 618:
                    fon = pygame.transform.scale(load_image('start_windiws/level6.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_6:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_6 = False
                elif 360 < event2.pos[0] < 528 and 450 < event2.pos[1] < 618:
                    fon = pygame.transform.scale(load_image('start_windiws/level7.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_7:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_7 = False
                elif 600 < event2.pos[0] < 768 and 450 < event2.pos[1] < 618:
                    fon = pygame.transform.scale(load_image('start_windiws/level8.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_8:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_8 = False
                elif 840 < event2.pos[0] < 1008 and 450 < event2.pos[1] < 618:
                    fon = pygame.transform.scale(load_image('start_windiws/level9.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_9:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_9 = False
                elif 1080 < event2.pos[0] < 1248 and 450 < event2.pos[1] < 618:
                    fon = pygame.transform.scale(load_image('start_windiws/level10.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    if flag_10:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volume_effects)
                        sound.play()
                        flag_10 = False
                else:
                    fon = pygame.transform.scale(load_image('start_windiws/level.png'), (68 * 20, 68 * 10 + 80))
                    screen.blit(fon, (0, 0))
                    flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8, flag_9, flag_10 \
                        = True, True, True, True, True, True, True, True, True, True
            elif event2.type == pygame.MOUSEBUTTONDOWN and pressed3:
                if 272 > event2.pos[0] > 113 and 290 > event2.pos[1] > 113:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_1.txt'
                elif 360 < event2.pos[0] < 528 and 290 > event2.pos[1] > 113:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_2.txt'
                elif 600 < event2.pos[0] < 768 and 290 > event2.pos[1] > 113:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_3.txt'
                elif 840 < event2.pos[0] < 1008 and 290 > event2.pos[1] > 113:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_4.txt'
                elif 1080 < event2.pos[0] < 1248 and 290 > event2.pos[1] > 113:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_5.txt'
                elif 120 < event2.pos[0] < 288 and 450 < event2.pos[1] < 618:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_6.txt'
                elif 360 < event2.pos[0] < 528 and 450 < event2.pos[1] < 618:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_7.txt'
                elif 600 < event2.pos[0] < 768 and 450 < event2.pos[1] < 618:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_8.txt'
                elif 840 < event2.pos[0] < 1008 and 450 < event2.pos[1] < 618:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_9.txt'
                elif 1080 < event2.pos[0] < 1248 and 450 < event2.pos[1] < 618:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volume_effects)
                    sound.play()
                    return 'level_10.txt'
            elif event2.type == pygame.KEYDOWN and event2.key == pygame.K_ESCAPE:
                start_screen()
                pygame.mixer.music.load('music_redactor.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(volume)
                return
        pygame.display.flip()
        clock.tick(fps)


def spawn_ice(last_move):  # перенес функцию т.к. она созадвала экземпляры класса в котором
    break_ice_flag = False
    xx = sprite_hero.rect.x // board.cell_size  # смотрим на какой клетке стоял дино
    yy = sprite_hero.rect.y // board.cell_size
    if last_move[0] == 1:  # определяем куда смотрел дино последний раз
        for ii in range(xx + shagg + 1, 20):
            if board.board[yy][xx + shagg + 1] == 'ice' or \
                    board.board[yy][xx + shagg] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and (not board.board[yy][ii] and not board.board[yy][ii - 1]) \
                    or not break_ice_flag and board.board[yy][ii] == 'ice' \
                    or board.board[yy][ii] == 'block' or (move and board.board[yy][ii - 1] == 'block'):
                break
            if not break_ice_flag and not (move and board.board[yy][ii - 1] == 'block'
                                           or board.board[yy][ii] == 'block'):  # убрал спавн лишнего спрайта
                ice_list.append((yy, ii))  # запоминаем на каих координатах ставим  лёд
            elif board.board[yy][ii] == 'ice' and break_ice_flag or \
                    board.board[yy][ii - 1] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:  # проверки на фрукты и лед перед идущим и стоящим героем
                    if (ii, yy) == possition((ices.rect.x, ices.rect.y)) and not fruit_list[yy][ii]:
                        board.board[yy][ii] = None
                        ices.kill_ice()
                    if (ii - 1, yy) == possition((ices.rect.x, ices.rect.y)) and move and not fruit_list[yy][ii - 1]:
                        board.board[yy][ii - 1] = None
                        ices.kill_ice()
                    if (ii, yy) == possition((ices.rect.x, ices.rect.y)) and fruit_list[yy][ii]:
                        board.board[yy][ii] = None
                        ices.kill_ice()
                        Fruit(fruit_list[yy][ii], f'fruct/{fruit_list[yy][ii]}_in_ice.png',
                              (ii * 68, yy * 68), True, True)
                    if (ii - 1, yy) == possition((ices.rect.x, ices.rect.y)) and move and fruit_list[yy][ii - 1]:
                        board.board[yy][ii - 1] = None
                        ices.kill_ice()
                        Fruit(fruit_list[yy][ii - 1], f'fruct/{fruit_list[yy][ii - 1]}_in_ice.png',
                              ((ii - 1) * 68, yy * 68), True, True)

    elif last_move[0] == -1:
        for ii in range(xx - 1, -1, -1):
            if board.board[yy][xx - 1] == 'ice' or \
                    board.board[yy][xx] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and (not board.board[yy][ii] and not board.board[yy][ii + 1]) \
                    or not break_ice_flag and board.board[yy][ii] == 'ice' \
                    or board.board[yy][ii] == 'block' or (move and board.board[yy][ii + 1] == 'block'):
                break
            if not break_ice_flag and not (move and board.board[yy][ii + 1] == 'block'
                                           or board.board[yy][ii] == 'block'):  # убрал спавн лишнего спрайта
                ice_list.append((yy, ii))  # запоминаем на каих координатах ставим  лёд
            elif board.board[yy][ii] == 'ice' and break_ice_flag or \
                    board.board[yy][ii + 1] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:  # проверки на фрукты и лед перед идущим и стоящим героем
                    if (ii, yy) == possition((ices.rect.x, ices.rect.y)) and not fruit_list[yy][ii]:
                        board.board[yy][ii] = None
                        ices.kill_ice()
                    if (ii + 1, yy) == possition((ices.rect.x, ices.rect.y)) and move and not fruit_list[yy][ii + 1]:
                        board.board[yy][ii + 1] = None
                        ices.kill_ice()
                    if (ii, yy) == possition((ices.rect.x, ices.rect.y)) and fruit_list[yy][ii]:
                        board.board[yy][ii] = None
                        ices.kill_ice()
                        Fruit(fruit_list[yy][ii], f'fruct/{fruit_list[yy][ii]}_in_ice.png',
                              (ii * 68, yy * 68), True, True)

                    if (ii + 1, yy) == possition((ices.rect.x, ices.rect.y)) and move and fruit_list[yy][ii + 1]:
                        board.board[yy][ii + 1] = None
                        ices.kill_ice()
                        Fruit(fruit_list[yy][ii + 1], f'fruct/{fruit_list[yy][ii + 1]}_in_ice.png',
                              ((ii + 1) * 68, yy * 68), True, True)

    elif last_move[1] == -1:
        for ii in range(yy - 1, -1, -1):
            if board.board[yy - 1][xx] == 'ice' or \
                    board.board[yy][xx] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            # проверка столкновения льда и столкновения ломания (жесть какая-то)
            if break_ice_flag and (not board.board[ii][xx] and not board.board[ii + 1][xx]) \
                    or not break_ice_flag and board.board[ii][xx] == 'ice' \
                    or board.board[ii][xx] == 'block' or (move and board.board[ii + 1][xx] == 'block'):
                break
            if not break_ice_flag and not (move and board.board[ii][xx] == 'block'
                                           or board.board[ii][xx] == 'block'):  # убрал спавн лишнего спрайта
                ice_list.append((ii, xx))  # запоминаем на каих координатах ставим  лёд
            elif board.board[ii][xx] == 'ice' and break_ice_flag or \
                    board.board[ii + 1][xx] == 'ice' and break_ice_flag:  # проверка на ломание
                for ices in ice_sprites:  # проверки на фрукты и лед перед идущим и стоящим героем
                    if (xx, ii) == possition((ices.rect.x, ices.rect.y)) and not fruit_list[ii][xx]:
                        board.board[ii][xx] = None
                        ices.kill_ice()
                    if (xx, ii + 1) == possition((ices.rect.x, ices.rect.y)) and move and not fruit_list[ii][xx]:
                        board.board[ii + 1][xx] = None
                        ices.kill_ice()
                    if (xx, ii) == possition((ices.rect.x, ices.rect.y)) and fruit_list[ii][xx]:
                        board.board[ii][xx] = None
                        ices.kill_ice()
                        Fruit(fruit_list[ii][xx], f'fruct/{fruit_list[ii][xx]}_in_ice.png',
                              (xx * 68, ii * 68), True, True)
                    if (xx, ii + 1) == possition((ices.rect.x, ices.rect.y)) and move and fruit_list[ii][xx]:
                        board.board[ii + 1][xx] = None
                        ices.kill_ice()
                        Fruit(fruit_list[ii + 1][xx], f'fruct/{fruit_list[ii + 1][xx]}_in_ice.png',
                              (xx * 68, (ii + 1) * 68), True, True)

    elif last_move[1] == 1:
        for ii in range(yy + shagg + 1, 12):
            if yy == 9 or yy == 8 and move:
                break
            if board.board[yy + shagg + 1][xx] == 'ice' or \
                    board.board[yy + shagg][xx] == 'ice':  # проверка что хотим ломать
                break_ice_flag = True
            try:
                # проверка столкновения льда и столкновения ломания (жесть какая-то)
                if break_ice_flag and (not board.board[ii][xx] and not board.board[ii - 1][xx]) \
                        or not break_ice_flag and board.board[ii][xx] == 'ice' \
                        or board.board[ii][xx] == 'block' or (move and board.board[ii - 1][xx] == 'block'):
                    break
                if not break_ice_flag and not (move and board.board[ii][xx] == 'block'
                                               or board.board[ii][xx] == 'block'):  # убрал спавн лишнего спрайта
                    ice_list.append((ii, xx))  # запоминаем на каих координатах ставим  лёд
                elif board.board[ii][xx] == 'ice' and break_ice_flag or \
                        board.board[ii - 1][xx] == 'ice' and break_ice_flag:  # проверка на ломание
                    for ices in ice_sprites:  # проверки на фрукты и лед перед идущим и стоящим героем
                        if (xx, ii) == possition((ices.rect.x, ices.rect.y)) and not fruit_list[ii][xx]:
                            board.board[ii][xx] = None
                            ices.kill_ice()
                        if (xx, ii - 1) == possition((ices.rect.x, ices.rect.y)) and move and not fruit_list[ii][xx]:
                            board.board[ii - 1][xx] = None
                            ices.kill_ice()
                        if (xx, ii) == possition((ices.rect.x, ices.rect.y)) and fruit_list[ii][xx]:
                            board.board[ii][xx] = None
                            ices.kill_ice()
                            Fruit(fruit_list[ii][xx], f'fruct/{fruit_list[ii][xx]}_in_ice.png',
                                  (xx * 68, ii * 68), True, False)
                        if (xx, ii - 1) == possition((ices.rect.x, ices.rect.y)) and move and fruit_list[ii][xx]:
                            board.board[ii + 1][xx] = None
                            ices.kill_ice()
                            Fruit(fruit_list[ii + 1][xx], f'fruct/{fruit_list[ii + 1][xx]}_in_ice.png',
                                  (xx * 68, (ii - 1) * 68), True, False)
            except IndexError:
                pass


def possition(mouse_pos):
    return mouse_pos[0] // board.cell_size, mouse_pos[1] // board.cell_size


def load_image(name, colorkeys=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkeys is not None:
        image = image.convert()
        image.set_colorkey(colorkeys)
    else:
        image = image.convert_alpha()
    return image


move_map = {pygame.K_w: (0, -1), pygame.K_s: (0, 1), pygame.K_a: (-1, 0), pygame.K_d: (1, 0)}
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
        if flag_redact:
            for yy in range(len(self.board)):
                for xx in range(len(self.board[0])):
                    if self.board[yy][xx] is None:
                        pygame.draw.rect(screen_1, (0, 0, 0),
                                         (xx * self.cell_size, yy * self.cell_size, self.cell_size,
                                          self.cell_size),
                                         width=1)
                    if self.board[yy][xx] == 'route':
                        pygame.draw.rect(screen_1, pygame.Color('red'),
                                         (xx * self.cell_size, yy * self.cell_size, self.cell_size,
                                          self.cell_size),
                                         width=10)


class Unit(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite):
        super().__init__(all_sprites)
        self.image = load_image(name_sprite, colorkeys=(255, 255, 255))
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
        global score, flag_cherry, flag_limon, text4
        if self.count == 12:
            self.count = 0
        self.count += 1

        for fruits in fruit_sprites:
            if self.rect.colliderect(fruits):
                fruits.kill_fruit()
                fruit_list[fruits.rect.y // 68][fruits.rect.x // 68] = None
                if fruits.name == 'banana':
                    score += 1
                elif fruits.name == 'cherry':
                    score += 2
                elif fruits.name == 'limon':
                    score += 3
                if flag_redact:
                    score = 0
                text4 = my_font.render(f'Очки: {score}', False, pygame.Color('red'))
            else:
                fruits.static_animation()
        if [fruits.name for fruits in fruit_sprites].count('banana') == 0 and not flag_cherry:
            with open(LEVEL, 'r') as level_files:
                counts = 0
                for string in level_files:
                    if counts == 4:
                        eval_string = eval(string)
                        for fff in eval_string:
                            if fff[2] == 'cherry':
                                Fruit(fff[2], 'fruct/cherry.png', (fff[0], fff[1]), True, True)
                    counts += 1
                flag_cherry = True
        elif [fruits.name for fruits in fruit_sprites].count('cherry') == 0 and flag_cherry and not flag_limon:
            with open(LEVEL, 'r') as level_files:
                counts = 0
                for string in level_files:
                    if counts == 4:
                        eval_string = eval(string)
                        for fff in eval_string:
                            if fff[2] == 'limon':
                                Fruit(fff[2], 'fruct/limon.png', (fff[0], fff[1]), True, True)
                    counts += 1
                flag_limon = True
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
            list_anim_right = [load_image(f'{personalization}/right_anim/right_shag_1.png', colorkeys=colorkey),
                               load_image(f'{personalization}/right_anim/right_shag_2.png', colorkeys=colorkey)]
            self.image = list_anim_right[self.count // 6 - 1]
            if self.rect.right < board.width * board.cell_size:  # для того чтобы не выходил за границы
                self.rect.x += speeda
        elif last_move[0] == -1:
            list_anim_left = [load_image(f'{personalization}/left_anim/left_shag_1.png', colorkeys=colorkey),
                              load_image(f'{personalization}/left_anim/left_shag_2.png', colorkeys=colorkey)]
            self.image = list_anim_left[self.count // 6 - 1]
            if self.rect.left > 0:
                self.rect.x -= speeda

        elif last_move[1] == 1:
            list_anim_up = [load_image(f'{personalization}/front_anim/front_shag_1.png', colorkeys=colorkey),
                            load_image(f'{personalization}/front_anim/front_shag_2.png', colorkeys=colorkey)]
            self.image = list_anim_up[self.count // 6 - 1]
            if self.rect.bottom < (board.height * board.cell_size):
                self.rect.y += speeda

        elif last_move[1] == -1:
            list_anim_down = [load_image(f'{personalization}/back_anim/back_shag_1.png', colorkeys=colorkey),
                              load_image(f'{personalization}/back_anim/back_shag_2.png', colorkeys=colorkey)]
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

        for fruits in fruit_sprites:
            if self.rect.colliderect(fruits):
                fruits.kill_fruit()
                fruit_list[fruits.rect.y // 68][fruits.rect.x // 68] = None
            else:
                fruits.static_animation()
        self.count_static += 1
        if last_move[0] == 1:
            list_anim_right = [load_image(f'{personalization}/right_anim/right_stoit_1.png', colorkeys=colorkey),
                               load_image(f'{personalization}/right_anim/right_stoit_2.png', colorkeys=colorkey)]
            self.image = list_anim_right[self.count_static // 12 - 1]

        elif last_move[0] == -1:
            list_anim_left = [load_image(f'{personalization}/left_anim/left_stoit_1.png', colorkeys=colorkey),
                              load_image(f'{personalization}/left_anim/left_stoit_2.png', colorkeys=colorkey)]
            self.image = list_anim_left[self.count_static // 12 - 1]

        elif last_move[1] == 1:
            list_anim_down = [load_image(f'{personalization}/front_anim/front_stoit_1.png', colorkeys=colorkey),
                              load_image(f'{personalization}/front_anim/front_stoit_2.png', colorkeys=colorkey)]
            self.image = list_anim_down[self.count_static // 12 - 1]

        elif last_move[1] == -1:
            list_anim_up = [load_image(f'{personalization}/back_anim/back_stoit_1.png', colorkeys=colorkey),
                            load_image(f'{personalization}/back_anim/back_stoit_2.png', colorkeys=colorkey)]
            self.image = list_anim_up[self.count_static // 12 - 1]

    def spawn_ice_dino(self, last_move):
        if last_move[0] == 1:
            self.image = load_image(f'{personalization}/right_anim/right_break_or_place_ice.png', colorkeys=colorkey)
        elif last_move[0] == -1:
            self.image = load_image(f'{personalization}/left_anim/left_break_or_place_ice.png', colorkeys=colorkey)
        elif last_move[1] == 1:
            self.image = load_image(f'{personalization}/front_anim/front_break_or_place_ice.png', colorkeys=colorkey)
        elif last_move[1] == -1:
            self.image = load_image(f'{personalization}/back_anim/back_break_or_place_ice.png', colorkeys=colorkey)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name_sprite):
        super().__init__(enemy_sprites)
        self.image = load_image(name_sprite, colorkeys=(255, 255, 255))
        self.rect = self.image.get_rect()
        self.count = 0
        self.count_static = 0
        self.route = []
        self.index = 0
        self.number = 1

    def set_posittion(self, event_pos):
        self.rect.x, self.rect.y = event_pos[0] * board.cell_size, event_pos[1] * board.cell_size

    def animation(self, last_move, go=True):
        if self.count_static == 48:
            self.count_static = 0
        self.count_static += 1

        if last_move[0] == 1:
            list_anim_right = [load_image('vrag/right_vrag.png', colorkeys=colorkey),
                               load_image('vrag/right_vrag_2.png', colorkeys=colorkey)]
            self.image = list_anim_right[self.count_static // 24 - 1]
            if go:
                self.rect.x += speed

        elif last_move[0] == -1:
            list_anim_left = [load_image('vrag/left_vrag.png', colorkeys=colorkey),
                              load_image('vrag/left_vrag_2.png', colorkeys=colorkey)]
            self.image = list_anim_left[self.count_static // 24 - 1]
            if go:
                self.rect.x -= speed

        elif last_move[1] == 1:
            list_anim_down = [load_image('vrag/front_vrag.png', colorkeys=colorkey),
                              load_image('vrag/front_vrag_2.png', colorkeys=colorkey)]
            self.image = list_anim_down[self.count_static // 24 - 1]
            if go:
                self.rect.y += speed

        elif last_move[1] == -1:
            list_anim_up = [load_image('vrag/back_vrag.png', colorkeys=colorkey),
                            load_image('vrag/back_vrag_2.png', colorkeys=colorkey)]
            self.image = list_anim_up[self.count_static // 24 - 1]
            if go:
                self.rect.y -= speed

    def go_go_zeppely(self):
        try:
            if self.index == len(self.route):
                self.index = 0
            xx = self.route[self.index][0] * cell_size - self.rect.x
            yy = self.route[self.index][1] * cell_size - self.rect.y
            if xx > 0:
                xx = 1
            if yy > 0:
                yy = 1
            if yy < 0:
                yy = -1
            if xx < 0:
                xx = -1
            last_move = (xx, yy)
            if self.route[self.index][0] * board.cell_size == self.rect.x and self.route[self.index][1] \
                    * board.cell_size == self.rect.y:
                self.index += self.number
            else:
                self.animation(last_move)
        except IndexError:
            pass
        try:
            if self.number == 1:
                if board.board[self.route[self.index + 1][1]][self.route[self.index + 1][0]] in ['block', 'ice']:
                    self.number *= -1
            elif self.number == -1:
                if board.board[self.route[self.index - 1][1]][self.route[self.index - 1][0]] in ['block', 'ice']:
                    self.number *= -1
        except IndexError:
            pass

    def set_route(self, list_clicks):
        self.route = list_clicks


class Fruit(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite, event_pos, can_eat, not_eat):
        super().__init__(fruit_sprites)
        self.count = 0
        self.image = load_image(name_sprite, colorkeys=colorkey)
        self.rect = self.image.get_rect()
        self.name = name_person
        self.eat_fruct = pygame.mixer.Sound('звук поедания фрукта.mpeg')
        self.eat_fruct.set_volume(0.3)
        self.rect.x, self.rect.y = [xx * board.cell_size for xx in possition(event_pos)]
        self.can_eat = can_eat
        self.not_eat = not_eat

    def static_animation(self):  # банан двигается
        list_anim_right = list()
        if self.count == 24:
            self.count = 0
        self.count += 1
        if self.name == 'banana':
            list_anim_right = [load_image('fruct/banana.png', colorkeys=colorkey),
                               load_image('fruct/banana2.png', colorkeys=colorkey)]
        elif self.name == 'cherry':
            list_anim_right = [load_image('fruct/cherry.png', colorkeys=colorkey),
                               load_image('fruct/cherry2.png', colorkeys=colorkey)]
        elif self.name == 'limon':
            list_anim_right = [load_image('fruct/limon.png', colorkeys=colorkey),
                               load_image('fruct/limon_2.png', colorkeys=colorkey)]
        self.image = list_anim_right[self.count // 12 - 1]

    def kill_fruit(self):
        if self.can_eat:
            fruit_sprites.remove(self)
            if self.not_eat and not board.board[self.rect.y // 68][self.rect.x // 68] and \
                    fruit_list[self.rect.y // 68][self.rect.x // 68]:
                sound = pygame.mixer.Sound('звук поедания фрукта.mpeg')
                sound.set_volume(volum_effects)
                sound.play()


class Ice(pygame.sprite.Sprite):
    def __init__(self, name_person, name_sprite, event_pos):
        super().__init__(ice_sprites)
        self.count = 0
        self.flag = False
        self.image = load_image(name_sprite, colorkeys=colorkey)
        self.rect = self.image.get_rect()
        self.name = name_person
        self.rect.x, self.rect.y = [xx * board.cell_size for xx in possition(event_pos)]
        try:
            board.board[possition(event_pos)[1]][possition(event_pos)[0]] = 'ice'
        except IndexError:
            if self.rect.y == 680 and not flag_redact:
                ice_sprites.remove(self)

    def ice_animation(self):  # сделайте анимацию появления я хз как
        if self.count == 12:
            self.count = 0
        self.count += 1
        list_anim_right = [load_image('ice/ice.png', colorkeys=colorkey),
                           load_image('ice/ice.png', colorkeys=colorkey)]
        self.image = list_anim_right[self.count // 6 - 1]

    def kill_ice(self):
        ice_sprites.remove(self)


class IronBlock(pygame.sprite.Sprite):
    def __init__(self, name_sprite, event_pos):
        super().__init__(iron_block_sprites)
        self.image = load_image(name_sprite, colorkeys=colorkey)
        self.rect = self.image.get_rect()
        self.name = 'block'
        self.rect.x, self.rect.y = [xx * board.cell_size for xx in possition(event_pos)]
        try:
            board.board[possition(event_pos)[1]][possition(event_pos)[0]] = 'block'
        except IndexError:
            if self.rect.x == 3 * cell_size and self.rect.y == 680 and not flag_redact:
                iron_block_sprites.remove(self)

    def kill_block(self):
        iron_block_sprites.remove(self)


def start_level(level):
    global sprite_hero, ice_sprites, iron_block_sprites, enemy_sprites, fruit_sprites, score
    global sprite_ice, sprite_iron_block, sprite_banana, sprite_cherry, enemy_sprite
    score = 0
    ice_sprites = pygame.sprite.Group()
    iron_block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    fruit_sprites = pygame.sprite.Group()
    with open(level, 'r') as level_files:
        counts = 0
        for string in level_files:
            eval_string = eval(string)
            if counts == 0:
                sprite_hero.rect.x, sprite_hero.rect.y = eval_string
            elif counts == 1:
                for ii in eval_string:
                    Ice('ice', 'ice/ice.png', ii)
            elif counts == 2:
                for bb in eval_string:
                    IronBlock('block/block.png', bb)
            elif counts == 3:
                for ee in eval_string:
                    enemy_1 = Enemy('vrag/front_vrag.png')
                    enemy_1.set_posittion((ee[0] // cell_size, ee[1] // cell_size))
                    enemy_1.set_route(ee[2])
            elif counts == 4:
                for ff in eval_string:
                    if ff[2] == 'banana':
                        Fruit(ff[2], 'fruct/banana.png', (ff[0], ff[1]), True, True)
            counts += 1
    return


def pause():
    pygame.font.init()
    fon = pygame.transform.scale(load_image('pause_fon.jpg'), (68 * 20, 68 * 10 + 80))
    screen.blit(fon, (0, 0))
    pauses = pygame.sprite.Group()
    pausee = load_image("pause.png", colorkeys=(255, 255, 255))
    paus = pygame.sprite.Sprite(pauses)
    paus.image = pausee
    paus.rect = paus.image.get_rect()
    paus.rect.x = 0
    paus.rect.y = 0
    flag_1, flag_2 = True, True
    while True:
        pressed3 = pygame.mouse.get_pressed()  # проверка какая кнопка мыши нажата
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                terminate()
            elif event2.type == pygame.MOUSEMOTION:
                if 865 > event2.pos[0] > 481 and 179 > event2.pos[1] > 93:
                    pausee = load_image("pause_next.png", colorkeys=(255, 255, 255))
                    paus.image = pausee
                    if flag_1:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                    flag_1 = False
                elif 865 > event2.pos[0] > 481 and 413 > event2.pos[1] > 327:
                    pausee = load_image("pause_exit.png", colorkeys=(255, 255, 255))
                    paus.image = pausee
                    if flag_2:
                        sound = pygame.mixer.Sound('zvuk_navedenie.mp3')
                        sound.set_volume(volum_effects)
                        sound.play()
                    flag_2 = False
                else:
                    pausee = load_image("pause.png", colorkeys=(255, 255, 255))
                    paus.image = pausee
                    flag_1, flag_2 = True, True
            elif event2.type == pygame.MOUSEBUTTONDOWN and pressed3:
                if 865 > event2.pos[0] > 481 and 179 > event2.pos[1] > 93:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volum_effects)
                    sound.play()
                    return False
                elif 865 > event2.pos[0] > 481 and 413 > event2.pos[1] > 327:
                    sound = pygame.mixer.Sound('zvuk_click.mp3')
                    sound.set_volume(volum_effects)
                    sound.play()
                    return True
        pauses.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    cell_size = 68
    size = wight, height = 68 * 20, 68 * 10 + 80
    screen = pygame.display.set_mode(size)
    board = Board(20, 10)
    pygame.display.set_caption('Фруктозавр')
    pygame.display.set_icon(load_image('default_dino/left_anim/left_shag_1.png'))
    running = True
    volume = 0.5
    volum_effects = 0.5
    all_sprites = pygame.sprite.Group()
    cursoro = pygame.sprite.Group()
    sprite_hero = Unit('hero', 'default_dino/right_anim/right_stoit_1.png')

    ice_sprites = pygame.sprite.Group()
    fruit_sprites = pygame.sprite.Group()
    iron_block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()

    surface = load_image('pole.png')
    rect = surface.get_rect(center=(wight // 2, height // 2))

    fps = 60
    v = 120
    speed = v // fps
    personalization = 'default_dino'
    start_screen()

    fruit_list = [[None] * (wight // 68) for _ in range(height // 68 - 1)]
    smotrit = (1, 0)
    smotrit_y = (1, 0)
    smotrit_x = (1, 0)
    count = 0
    ice_list = []
    flag_of_move = False
    dlina_ice_list = 0
    flag = False
    last_pos_dino = 0, 0
    cursor_image = load_image("ice_cursor.png")
    cursor = pygame.sprite.Sprite(cursoro)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()
    my_font = pygame.font.SysFont('Throne and Libert', 30)
    if flag_redact:
        sprite_ice = Ice('ice', 'ice/ice.png', (0, cell_size * 10))
        sprite_banana = Fruit('banana', 'fruct/banana.png', (cell_size, cell_size * 10), False, False)
        sprite_cherry = Fruit('cherry', 'fruct/cherry.png', (cell_size * 2, cell_size * 10), False, False)
        sprite_limon = Fruit('limon', 'fruct/limon.png', (cell_size * 3, cell_size * 10), False, False)
        sprite_iron_block = IronBlock('block/block.png', (cell_size * 4, cell_size * 10))
        enemy_sprite = Enemy('vrag/front_vrag.png')
        enemy_sprite.rect.x, enemy_sprite.rect.y = cell_size * 5, cell_size * 10
        pygame.font.init()
        text1 = my_font.render('save', False, pygame.Color('red'))
        text2 = my_font.render('refresh', False, pygame.Color('red'))
        text3 = my_font.render('my_level', False, pygame.Color('red'))
        pygame.mixer.music.load('music_redactor.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume)
    else:
        text4 = my_font.render(f'Очки: {score}', False, pygame.Color('red'))
        pygame.mixer.music.load('level_music.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume)
    flag_of_list_click = False
    flaag = True
    _enemy_ = None
    list_click = []
    flag_na_music = True
    while running:
        keys = pygame.key.get_pressed()
        move = sprite_hero.get_move()
        for event in pygame.event.get():
            pressed = pygame.mouse.get_pressed()  # проверка какая кнопка мыши нажата
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:  # нужно релаизовать чтобы за мышкой следовал спрай, который мы выбрали
                if flag == 'banana':
                    cursor_image = load_image("banana_cursor.png")
                    cursor.image = cursor_image
                    pygame.mouse.set_visible(False)
                    cursor.rect.topleft = event.pos
                elif flag == 'cherry':
                    cursor_image = load_image("cherry_cursor.png")
                    cursor.image = cursor_image
                    pygame.mouse.set_visible(False)
                    cursor.rect.topleft = event.pos
                elif flag == 'ice':
                    cursor_image = load_image("ice_cursor.png")
                    cursor.image = cursor_image
                    pygame.mouse.set_visible(False)
                    cursor.rect.topleft = event.pos
                elif flag == 'block':
                    cursor_image = load_image("block_cursor.png")
                    cursor.image = cursor_image
                    pygame.mouse.set_visible(False)
                    cursor.rect.topleft = event.pos
                elif flag == 'limon':
                    cursor_image = load_image("limon_cursor.png")
                    cursor.image = cursor_image
                    pygame.mouse.set_visible(False)
                    cursor.rect.topleft = event.pos
                elif flag == 'enemy':
                    cursor_image = load_image("vrag_cursor.png")
                    cursor.image = cursor_image
                    pygame.mouse.set_visible(False)
                    cursor.rect.topleft = event.pos
                else:
                    cursor_image = load_image("cursor.png")
                    cursor.image = cursor_image
                    pygame.mouse.set_visible(True)
                    cursor.rect.topleft = 1400, 800
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if flag_redact:
                    pygame.mouse.set_visible(True)
                    cursor.rect.topleft = 1400, 800
                    flag = None
                    flag_na_music = True
                    start_screen()
                else:
                    pygame.mixer.music.pause()
                    if pause():
                        flag_na_music = True
                        cursor.rect.topleft = 1400, 800
                        pygame.mouse.set_visible(True)
                        start_screen()
                        flag = None
                    else:
                        pygame.mixer.music.unpause()
                        flag_na_music = False
                if flag_redact:
                    text1 = my_font.render('save', False, pygame.Color('red'))
                    text2 = my_font.render('refresh', False, pygame.Color('red'))
                    text3 = my_font.render('my_level', False, pygame.Color('red'))
                    sprite_ice = Ice('ice', 'ice/ice.png', (0, cell_size * 10))
                    sprite_banana = Fruit('banana', 'fruct/banana.png', (cell_size, cell_size * 10), False, True)
                    sprite_cherry = Fruit('cherry', 'fruct/cherry.png', (cell_size * 2, cell_size * 10), False, True)
                    sprite_limon = Fruit('limon', 'fruct/limon.png', (cell_size * 3, cell_size * 10), False, True)
                    sprite_iron_block = IronBlock('block/block.png', (cell_size * 4, cell_size * 10))
                    enemy_sprite = Enemy('vrag/front_vrag.png')
                    enemy_sprite.rect.x, enemy_sprite.rect.y = cell_size * 5, cell_size * 10
                    pygame.font.init()
                    pygame.mixer.music.load('music_redactor.mp3')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(volume)
                    board.board = [[None] * board.width for _ in range(board.height)]
                    fruit_list = [[None] * (wight // 68) for _ in range(height // 68 - 1)]
                    sprite_hero.rect.x, sprite_hero.rect.y = 0, 0
                    ice_sprites = pygame.sprite.Group()
                    iron_block_sprites = pygame.sprite.Group()
                    enemy_sprites = pygame.sprite.Group()
                    fruit_sprites = pygame.sprite.Group()
                    sprite_ice = Ice('ice', 'ice/ice.png', (0, cell_size * 10))
                    sprite_banana = Fruit('banana', 'fruct/banana.png', (cell_size, cell_size * 10), False,
                                          True)
                    sprite_cherry = Fruit('cherry', 'fruct/cherry.png', (cell_size * 2, cell_size * 10), False,
                                          True)
                    sprite_limon = Fruit('limon', 'fruct/limon.png', (cell_size * 3, cell_size * 10), False,
                                         True)
                    sprite_iron_block = IronBlock('block/block.png', (cell_size * 4, cell_size * 10))
                    enemy_sprite = Enemy('vrag/front_vrag.png')
                    enemy_sprite.rect.x, enemy_sprite.rect.y = cell_size * 5, cell_size * 10
                else:
                    text4 = my_font.render(f'Очки: {score}', False, pygame.Color('red'))
                    if flag_na_music:
                        pygame.mixer.music.load('level_music.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(volume)
            if event.type == pygame.MOUSEBUTTONDOWN and pressed[0]:
                if flag_redact:
                    if flag_of_list_click and possition(event.pos)[1] != 10:
                        try:
                            list_click.append(possition(event.pos))
                            board.board[possition(event.pos)[1]][possition(event.pos)[0]] = 'route'
                            if possition(event.pos) == possition((_enemy_.rect.x, _enemy_.rect.y)):
                                flag_of_list_click = False
                                _enemy_.set_route(list_click)
                                list_click = []
                                _enemy_ = None
                                for y in range(len(board.board)):
                                    for x in range(len(board.board[y])):
                                        if board.board[y][x] == 'route':
                                            board.board[y][x] = None
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
                            flag = 'limon'
                        elif possition(event.pos) == (4, 10):
                            flag = 'block'
                        elif possition(event.pos) == (5, 10):
                            flag = 'enemy'
                        elif possition(event.pos) == (18, 10):
                            # level_list.append(
                            #   [sprite_hero, ice_sprites, iron_block_sprites, enemy_sprites, fruit_sprites])
                            with open(f'level_1.txt', 'w+') as level_file:
                                hero = (sprite_hero.rect.x, sprite_hero.rect.y)
                                ice = []
                                for i in ice_sprites:
                                    if i != sprite_ice:
                                        ice.append((i.rect.x, i.rect.y))
                                block = []
                                for b in iron_block_sprites:
                                    if b != sprite_iron_block:
                                        block.append((b.rect.x, b.rect.y))
                                enemy = []
                                for e in enemy_sprites:
                                    if e != enemy_sprite:
                                        enemy.append((e.rect.x, e.rect.y, e.route))
                                fruit = []
                                for f in fruit_sprites:
                                    if f != sprite_cherry and f != sprite_banana and f != sprite_limon:
                                        fruit.append((f.rect.x, f.rect.y, f.name))
                                level_file.write(f'{hero}\n{ice}\n{block}\n{enemy}\n{fruit}')
                        elif possition(event.pos) == (19, 10):
                            board.board = [[None] * board.width for _ in range(board.height)]
                            fruit_list = [[None] * (wight // 68) for _ in range(height // 68 - 1)]
                            sprite_hero.rect.x, sprite_hero.rect.y = 0, 0
                            ice_sprites = pygame.sprite.Group()
                            iron_block_sprites = pygame.sprite.Group()
                            enemy_sprites = pygame.sprite.Group()
                            fruit_sprites = pygame.sprite.Group()
                            sprite_ice = Ice('ice', 'ice/ice.png', (0, cell_size * 10))
                            sprite_banana = Fruit('banana', 'fruct/banana.png', (cell_size, cell_size * 10), False,
                                                  False)
                            sprite_cherry = Fruit('cherry', 'fruct/cherry.png', (cell_size * 2, cell_size * 10), False,
                                                  False)
                            sprite_limon = Fruit('limon', 'fruct/limon.png', (cell_size * 3, cell_size * 10), False,
                                                 False)
                            sprite_iron_block = IronBlock('block/block.png', (cell_size * 4, cell_size * 10))
                            enemy_sprite = Enemy('vrag/front_vrag.png')
                            enemy_sprite.rect.x, enemy_sprite.rect.y = cell_size * 5, cell_size * 10
            if event.type == pygame.MOUSEBUTTONDOWN and pressed[2]:
                if flag_redact:
                    if flag == 'banana' and possition(event.pos)[1] != 10 \
                            and not board.board[event.pos[1] // 68][event.pos[0] // 68]:
                        if not fruit_list[event.pos[1] // 68][event.pos[0] // 68]:
                            fruit_list[event.pos[1] // 68][event.pos[0] // 68] = 'banana'
                            Fruit('banana', 'fruct/banana.png', (event.pos[0], event.pos[1]), True, True)
                        else:
                            for fruct in fruit_sprites:
                                if possition(event.pos) == possition((fruct.rect.x, fruct.rect.y)):
                                    fruit_list[possition(event.pos)[1]][possition(event.pos)[0]] = None
                                    fruct.kill_fruit()

                    elif flag == 'limon' and possition(event.pos)[1] != 10 \
                            and not board.board[event.pos[1] // 68][event.pos[0] // 68]:
                        if not fruit_list[event.pos[1] // 68][event.pos[0] // 68]:
                            fruit_list[event.pos[1] // 68][event.pos[0] // 68] = 'limon'
                            Fruit('limon', 'fruct/limon.png', (event.pos[0], event.pos[1]), True, True)
                        else:
                            for fruct in fruit_sprites:
                                if possition(event.pos) == possition((fruct.rect.x, fruct.rect.y)):
                                    fruit_list[possition(event.pos)[1]][possition(event.pos)[0]] = None
                                    fruct.kill_fruit()
                    elif flag == 'cherry' and possition(event.pos)[1] != 10 \
                            and not board.board[event.pos[1] // 68][event.pos[0] // 68]:
                        if not fruit_list[event.pos[1] // 68][event.pos[0] // 68]:
                            fruit_list[event.pos[1] // 68][event.pos[0] // 68] = 'cherry'
                            Fruit('cherry', 'fruct/cherry.png', (event.pos[0], event.pos[1]), True, True)
                        else:
                            for fruct in fruit_sprites:
                                if possition(event.pos) == possition((fruct.rect.x, fruct.rect.y)):
                                    fruit_list[possition(event.pos)[1]][possition(event.pos)[0]] = None
                                    fruct.kill_fruit()
                    elif flag == 'ice':
                        if (event.pos[0] // cell_size) != (sprite_hero.rect.x // cell_size) \
                                or (event.pos[1] // cell_size) != (sprite_hero.rect.y // cell_size):
                            try:
                                if not board.board[event.pos[1] // 68][event.pos[0] // 68]:
                                    if fruit_list[event.pos[1] // 68][event.pos[0] // 68]:
                                        for fruit in fruit_sprites:
                                            if possition(event.pos) == possition((fruit.rect.x, fruit.rect.y)):
                                                board.board[event.pos[1] // 68][event.pos[0] // 68] = 'ice'
                                                fruit.kill_fruit()
                                        Ice('ice',
                                            f'fruct/{fruit_list[event.pos[1] // 68][event.pos[0] // 68]}_in_ice.png',
                                            event.pos)  # нужно название фрукта вставить
                                        board.board[event.pos[1] // 68][event.pos[0] // 68] = 'ice'
                                    else:
                                        Ice('ice', 'ice/ice.png', event.pos)
                                        board.board[event.pos[1] // 68][event.pos[0] // 68] = 'ice'
                                else:
                                    for ice in ice_sprites:
                                        if possition(event.pos) == possition((ice.rect.x, ice.rect.y)) \
                                                and fruit_list[possition(event.pos)[1]][possition(event.pos)[0]]:
                                            ice.kill_ice()
                                            board.board[event.pos[1] // 68][event.pos[0] // 68] = None

                                            if fruit_list[possition(event.pos)[1]][possition(event.pos)[0]]:
                                                Fruit(fruit_list[event.pos[1] // 68][event.pos[0] // 68],
                                                      f'fruct/{fruit_list[event.pos[1] // 68][event.pos[0] // 68]}.png',
                                                      event.pos, True, True)
                                        elif possition(event.pos) == possition((ice.rect.x, ice.rect.y)):
                                            board.board[event.pos[1] // 68][event.pos[0] // 68] = None
                                            ice.kill_ice()
                            except IndexError:
                                pass
                    elif flag == 'block':
                        if possition(event.pos) != possition((sprite_hero.rect.x, sprite_hero.rect.y)) and \
                                not fruit_list[event.pos[1] // 68][event.pos[0] // 68]:
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
        if dlina_ice_list != 0:
            board.board[ice_list[len(ice_list) - dlina_ice_list][0]][ice_list[len(ice_list) - dlina_ice_list][1]] \
                = 'ice'  # тоже самое что и board.board[y][i] или board.board[i][y] в spawn_ice
            if fruit_list[ice_list[len(ice_list) - dlina_ice_list][0]][ice_list[len(ice_list) - dlina_ice_list][1]]:
                for fruct in fruit_sprites:
                    if fruit_list[ice_list[len(ice_list) - dlina_ice_list][0]][ice_list[len(ice_list)
                                                                                        - dlina_ice_list][1]] \
                            and possition((fruct.rect.x, fruct.rect.y)) == (ice_list[len(ice_list)
                                                                                     - dlina_ice_list][1],
                                                                            ice_list[len(ice_list) - dlina_ice_list][
                                                                                0]):
                        fruct.kill_fruit()
                        chtoto = len(ice_list) - dlina_ice_list
                        sprite_ice = Ice('ice',
                                         f'fruct/{fruit_list[ice_list[chtoto][0]][ice_list[chtoto][1]]}_in_ice.png',
                                         (ice_list[len(ice_list) - dlina_ice_list][1] * 68,
                                          ice_list[len(ice_list) - dlina_ice_list][0] * 68))
            else:
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
            if flag_redact:
                if enemy != enemy_sprite:
                    enemy.go_go_zeppely()
                    if enemy.rect.colliderect(sprite_hero):
                        game_lose()
            else:
                enemy.go_go_zeppely()
                if enemy.rect.colliderect(sprite_hero):
                    game_lose()
        screen.fill((255, 255, 255))
        if flag_redact:
            enemy_sprite.animation((0, 1), go=False)
            screen.blit(load_image('save.png'), (18 * cell_size, 10 * cell_size))
            screen.blit(text1, (18 * cell_size + 5, int(10.8 * cell_size)))
            screen.blit(load_image('restart.png'), (19 * cell_size, 10 * cell_size))
            screen.blit(text2, (19 * cell_size, int(10.8 * cell_size)))
            screen.blit(load_image('my_level.png'), (17 * cell_size, 10 * cell_size))
            screen.blit(text3, (16.7 * cell_size, int(10.8 * cell_size)))
        else:
            screen.blit(surface, rect)
            screen.blit(text4, (15 * cell_size, 10 * cell_size))
        cursoro.draw(screen)
        clock.tick(fps)
        board.render(screen)
        all_sprites.draw(screen)
        ice_sprites.draw(screen)
        fruit_sprites.draw(screen)
        iron_block_sprites.draw(screen)
        enemy_sprites.draw(screen)
        pygame.display.flip()
