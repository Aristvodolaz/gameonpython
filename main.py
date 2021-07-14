import time
import random
import pygame
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
icon = pygame.image.load("ic.jpg")
pygame.display.set_icon(icon)

wheat=(245, 222, 179)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0,158,255)
red = (255, 11, 92)
light_red = (188, 0, 47)
yellow = (255, 241, 107)
light_yellow = (255, 242, 133)
green = (111, 255, 101)
light_green = (190, 255, 116)


clock = pygame.time.Clock()
tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5
ground_height = 35
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("Yu Mincho Demibold", 85)
vsmallfont = pygame.font.SysFont("Yu Mincho Demibold", 25)


def score(score):
    text = smallfont.render("Счет: " + str(score), True, white)
    gameDisplay.blit(text, [0, 0])


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "vsmall":
        textSurface = vsmallfont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="vsmall"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


def tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x - 27, y - 2),
                       (x - 26, y - 5),
                       (x - 25, y - 8),
                       (x - 23, y - 12),
                       (x - 20, y - 14),
                       (x - 18, y - 15),
                       (x - 16, y - 17),
                       (x - 13, y - 19),
                       (x - 11, y - 21)
                       ]

    pygame.draw.circle(gameDisplay, blue, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, blue, (x - tankHeight, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay, blue, (x, y), possibleTurrets[turPos], turretWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 15, y + 20), wheelWidth)
    return possibleTurrets[turPos]

def rival_tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x + 27, y - 2),
                       (x + 26, y - 5),
                       (x + 25, y - 8),
                       (x + 23, y - 12),
                       (x + 20, y - 14),
                       (x + 18, y - 15),
                       (x + 15, y - 17),
                       (x + 13, y - 19),
                       (x + 11, y - 21)
                       ]

    pygame.draw.circle(gameDisplay, blue, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, blue, (x - tankHeight, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay, blue, (x, y), possibleTurrets[turPos], turretWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 15, y + 20), wheelWidth)
    return possibleTurrets[turPos]

def game_controls():
    gcont = True
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        message_to_screen("Управление", white, -100, size="large")
        message_to_screen("Огонь: пробел", wheat, -30)
        message_to_screen("Перемещение дула: вверх или вниз стрелками", wheat, 10)
        message_to_screen("Перемещение танка: влево или вправо стрелками", wheat, 50)
        message_to_screen("Удерживайте D для повышения % мощности выстрела или А для понижения % ", wheat, 140)
        message_to_screen("Пауза: P", wheat, 90)
        button("Играть", 150, 500, 100, 50, green, light_green, action="play")
        button("Основное", 350, 500, 100, 50, yellow, light_yellow, action="main")
        button("Выход", 550, 500, 100, 50, red, light_red, action="quit")
        pygame.display.update()
        clock.tick(15)

def button(text, x, y, width, height, inactive_color, active_color, action=None,size=" "):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "main":
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)

def pause():
    paused = True
    message_to_screen("Пауза", white, -100, size="large")
    message_to_screen("Нажмите С, чтобы продолжить игру или Q для выхода из нее", wheat, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

def barrier(x_location, random_Height, barrier_width):
    pygame.draw.rect(gameDisplay, green, [x_location, display_height - random_Height, barrier_width, random_Height])

def explosion(x, y, size=50):
    burst_up = True
    while burst_up:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        startPoint = x, y
        colorChoices = [red, light_red, yellow, light_yellow]
        magnitude = 1

        while magnitude < size:
            burst_up_bit_x = x + random.randrange(-1 * magnitude, magnitude)
            burst_up_bit_y = y + random.randrange(-1 * magnitude, magnitude)
            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0, 4)], (burst_up_bit_x, burst_up_bit_y),
                               random.randrange(1, 5))
            magnitude += 1
            pygame.display.update()
            clock.tick(100)
        burst_up = False

def fireShell(x_y, tankx, tanky, turPos, shot_power, x_location, barrier_width, random_Height, rival_Tank_X, rival_Tank_Y):
    fire = True
    damage = 0
    startingShell = list(x_y)
    print("Огонь!", x_y)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
        startingShell[0] -= (12 - turPos) * 2
        startingShell[1] += int(
            (((startingShell[0] - x_y[0]) * 0.015 / (shot_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))
        if startingShell[1] > display_height - ground_height:
            print("Последнее пробитие:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Урон:", hit_x, hit_y)
            if rival_Tank_X + 10 > hit_x > rival_Tank_X - 10:
                print("Критическое попадание!")
                damage = 25
            elif rival_Tank_X + 15 > hit_x > rival_Tank_X - 15:
                print("Сильный выстрел!")
                damage = 18
            elif rival_Tank_X + 25 > hit_x > rival_Tank_X - 25:
                print("Средний выстрел")
                damage = 10
            elif rival_Tank_X + 35 > hit_x > rival_Tank_X - 35:
                print("Легкий выстрел")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= x_location + barrier_width
        check_x_2 = startingShell[0] >= x_location
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - random_Height

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Последнее пробитие:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Урон:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False
        pygame.display.update()
        clock.tick(60)
    return damage

def e_fireShell(x_y, tankx, tanky, turPos, shot_power, x_location, barrier_width, random_Height, ptank_x, ptank_y):
    damage = 0
    flowPower = 1
    power_found = False
    while not power_found:
        flowPower += 1
        if flowPower > 100:
            power_found = True
        fire = True
        start_Shell = list(x_y)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            start_Shell[0] += (12 - turPos) * 2
            start_Shell[1] += int(
                (((start_Shell[0] - x_y[0]) * 0.015 / (flowPower / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

            if start_Shell[1] > display_height - ground_height:
                hit_x = int((start_Shell[0] * display_height - ground_height) / start_Shell[1])
                hit_y = int(display_height - ground_height)

                if ptank_x + 15 > hit_x > ptank_x - 15:
                    print("цель достигнута!")
                    power_found = True
                fire = False

            check_x_1 = start_Shell[0] <= x_location + barrier_width
            check_x_2 = start_Shell[0] >= x_location
            check_y_1 = start_Shell[1] <= display_height
            check_y_2 = start_Shell[1] >= display_height - random_Height

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((start_Shell[0]))
                hit_y = int(start_Shell[1])
                fire = False

    fire = True
    start_Shell = list(x_y)
    print("Огонь!", x_y)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay, red, (start_Shell[0], start_Shell[1]), 5)

        start_Shell[0] += (12 - turPos) * 2
        shot_power = random.randrange(int(flowPower * 0.90), int(flowPower * 1.10))

        start_Shell[1] += int(
            (((start_Shell[0] - x_y[0]) * 0.015 / (shot_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if start_Shell[1] > display_height - ground_height:
            print("последние проибите:", start_Shell[0], start_Shell[1])
            hit_x = int((start_Shell[0] * display_height - ground_height) / start_Shell[1])
            hit_y = int(display_height - ground_height)
            print("Урон:", hit_x, hit_y)

            if ptank_x + 10 > hit_x > ptank_x - 10:
                print("Критический урон!")
                damage = 25
            elif ptank_x + 15 > hit_x > ptank_x - 15:
                print("Серьезный урон!")
                damage = 18
            elif ptank_x + 25 > hit_x > ptank_x - 25:
                print("Средний урон")
                damage = 10
            elif ptank_x + 35 > hit_x > ptank_x - 35:
                print("Легкий урон")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = start_Shell[0] <= x_location + barrier_width
        check_x_2 = start_Shell[0] >= x_location

        check_y_1 = start_Shell[1] <= display_height
        check_y_2 = start_Shell[1] >= display_height - random_Height

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Последние пробитие:", start_Shell[0], start_Shell[1])
            hit_x = int((start_Shell[0]))
            hit_y = int(start_Shell[1])
            print("Урон:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage

def power(level):
    text = smallfont.render("Мощность: " + str(level) + "%", True, wheat)
    gameDisplay.blit(text, [display_width / 2, 0])

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Добро пожаловать в танки!", white, -120, size="large")
        button("Играть", 150, 500, 100, 50, wheat, light_green, action="play",size="vsmall")
        button("Управление", 350, 500, 100, 50, wheat, light_yellow, action="controls",size="vsmall")
        button("Выход", 550, 500, 100, 50, wheat, light_red, action="quit",size="vsmall")
        pygame.display.update()

        clock.tick(15)
def game_over():
    game_over = True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        message_to_screen("Вы проиграли", white, -120, size="large")
        message_to_screen("Ты пал честью храбрых", wheat, -30)
        button("Играть снова", 150, 600, 150, 50, wheat, light_green, action="play")
        button("Управление", 350, 600, 100, 50, wheat, light_yellow, action="controls")
        button("Выход", 550, 600, 100, 50, wheat, light_red, action="quit")
        pygame.display.update()
        clock.tick(15)

def you_win():
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        message_to_screen("Ты победил!", white, -100, size="large")
        message_to_screen("Это было невероятно!", wheat, -30)
        button("играть снова", 150, 600, 150, 50, wheat, light_green, action="play")
        button("управление", 350, 600, 100, 50, wheat, light_yellow, action="controls")
        button("выход", 550, 600, 100, 50, wheat, light_red, action="quit")
        pygame.display.update()
        clock.tick(15)


def health_bars(player_health, rival_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red
    if rival_health > 75:
        rival_health_color = green
    elif rival_health > 50:
        rival_health_color = yellow
    else:
        rival_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, rival_health_color, (20, 25, rival_health, 25))


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 30
    player_health = 100
    rival_health = 100
    barrier_width = 50
    main_Tank_X = display_width * 0.9
    mainTankY = display_height * 0.9
    tank_Move = 0
    flowTurPos = 0
    change_tur = 0
    rival_Tank_X = display_width * 0.1
    rival_Tank_Y = display_height * 0.9
    fire_power = 50
    power_change = 0
    x_location = (display_width / 2) + random.randint(-0.1 * display_width, 0.1 * display_width)
    random_Height = random.randrange(display_height * 0.1, display_height * 0.6)

    while not gameExit:
        if gameOver == True:
            message_to_screen("Игра окончена!", red, -50, size="large")
            message_to_screen("Нажмите С, чтобы играть снова или Q для выхода из игры", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tank_Move = -5
                elif event.key == pygame.K_RIGHT:
                    tank_Move = 5
                elif event.key == pygame.K_UP:
                    change_tur = 1
                elif event.key == pygame.K_DOWN:
                    change_tur = -1
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_SPACE:
                    damage = fireShell(shot, main_Tank_X, mainTankY, flowTurPos, fire_power, x_location, barrier_width,
                                       random_Height, rival_Tank_X, rival_Tank_Y)
                    rival_health -= damage

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):

                        if display_width * 0.3 > rival_Tank_X > display_width * 0.03:
                            if possibleMovement[moveIndex] == "f":
                                rival_Tank_X += 5
                            elif possibleMovement[moveIndex] == "r":
                                rival_Tank_X -= 5

                            gameDisplay.fill(black)
                            health_bars(player_health, rival_health)
                            shot = tank(main_Tank_X, mainTankY, flowTurPos)
                            rival_shot = rival_tank(rival_Tank_X, rival_Tank_Y, 8)
                            fire_power += power_change
                            power(fire_power)
                            barrier(x_location, random_Height, barrier_width)
                            gameDisplay.fill(green,
                                             rect=[0, display_height - ground_height, display_width, ground_height])
                            pygame.display.update()

                            clock.tick(FPS)

                    damage = e_fireShell(rival_shot, rival_Tank_X, rival_Tank_Y, 8, 50, x_location, barrier_width,
                                         random_Height, main_Tank_X, mainTankY)
                    player_health -= damage
                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tank_Move = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    change_tur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0

        main_Tank_X += tank_Move
        flowTurPos += change_tur

        if flowTurPos > 8:
            flowTurPos = 8
        elif flowTurPos < 0:
            flowTurPos = 0

        if main_Tank_X - (tankWidth / 2) < x_location + barrier_width:
            main_Tank_X += 5

        gameDisplay.fill(black)
        health_bars(player_health, rival_health)
        shot = tank(main_Tank_X, mainTankY, flowTurPos)
        rival_shot = rival_tank(rival_Tank_X, rival_Tank_Y, 8)

        fire_power += power_change
        if fire_power > 100:
            fire_power = 100
        elif fire_power < 1:
            fire_power = 1

        power(fire_power)
        barrier(x_location, random_Height, barrier_width)
        gameDisplay.fill(green, rect=[0, display_height - ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        elif rival_health < 1:
            you_win()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()