import pygame
import sys
from pygame.locals import *
from city import *
from car import Car
from bowser import Player

def main():
    pygame.init()
    fps = 30  # 30 frames per second
    fps_clock = pygame.time.Clock()

    # Keep score of buildings destroyed
    bscore = 0

    # timer
    font = pygame.font.Font(None, 25)
    frame_count = 0
    frame_rate = 30

    # load bg track
    music = pygame.mixer.music
    music.load('Assets/Audio/city_background.mp3')
    music.play(-1)

    game_won = False
    game_over = False

    # load sounds
    punch_sound = pygame.mixer.Sound('Assets/Audio/punch.ogg')
    traffic_sound = pygame.mixer.Sound('Assets/Audio/traffic_jam.ogg')
    blast = pygame.mixer.Sound('Assets/Audio/blast.ogg')
    hurt = pygame.mixer.Sound('Assets/Audio/hurt.ogg')

    # Code to create the initial window
    window_size = (1024, 800)
    screen = pygame.display.set_mode(window_size)

    # set the title of the window
    pygame.display.set_caption("City")

    # load cars
    cars = pygame.sprite.Group()
    cars.add(Car(0, 385, 'right', 5, 'Assets/Pictures/white_car_r.png'))
    cars.add(Car(30, 575, 'right', 4, 'Assets/Pictures/white_car_r.png'))
    cars.add(Car(300, 385, 'right', 5, 'Assets/Pictures/white_car_r.png'))
    cars.add(Car(450, 575, 'right', 4, 'Assets/Pictures/white_car_r.png'))
    cars.add(Car(612, 198, 'right', 5, 'Assets/Pictures/white_car_r.png'))
    cars.add(Car(13, 198, 'right', 4, 'Assets/Pictures/white_car_r.png'))
    cars.add(Car(700, 370, 'left', 5, 'Assets/Pictures/white_car_l.png'))
    cars.add(Car(250, 560, 'left', 4, 'Assets/Pictures/white_car_l.png'))
    cars.add(Car(175, 370, 'left', 5, 'Assets/Pictures/white_car_l.png'))
    cars.add(Car(360, 560, 'left', 4, 'Assets/Pictures/white_car_l.png'))
    cars.add(Car(175, 185, 'left', 5, 'Assets/Pictures/white_car_l.png'))
    cars.add(Car(400, 185, 'left', 4, 'Assets/Pictures/white_car_l.png'))
    cars.add(Car(527, 0, 'down', 5, 'Assets/Pictures/white_car_d.png'))
    cars.add(Car(327, 200, 'down', 4, 'Assets/Pictures/white_car_d.png'))
    cars.add(Car(30, 800, 'up', 5, 'Assets/Pictures/white_car_u.png'))
    cars.add(Car(1030, 45, 'down', 4, 'Assets/Pictures/white_car_d.png'))

    # load buildings

    # load Bowser
    bowser = Player(50, 50)

    # load tree
    tree = Tree(305, 300, 'Assets/Pictures/small_trees.png')

    # Set of Colors
    grass = pygame.Color(51, 102, 0)

    street = pygame.Color(32, 32, 32)
    white = pygame.Color(255, 255, 255)

    # Building Colors
    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)
    dark_gray = pygame.Color(96, 96, 96)
    medium_gray = pygame.Color(160, 160, 160)
    light_gray = pygame.Color(192, 192, 192)
    chocolate = pygame.Color(210, 105, 30)
    sandy_brown = pygame.Color(244, 164, 96)
    tan = pygame.Color(210, 180, 140)
    light_slate_gray = pygame.Color(92, 108, 124)
    light_steel_blue = pygame.Color(119, 136, 153)
    lavender = pygame.Color(230, 230, 250)
    yellow = pygame.Color(255, 255, 0)
    red = pygame.Color(225, 51, 51)
    tomato = pygame.Color(255, 102, 102)
    coral = pygame.Color(255, 153, 153)

    # Fill background with grass color
    screen.fill(grass)

    building_colors = {
        'colors1':
            {
                'front': dark_gray,
                'side': medium_gray,
                'top': light_gray,
                'windows': yellow
            },
        'colors2':
            {
                'front': chocolate,
                'side': sandy_brown,
                'top': tan,
                'windows': yellow
            },
        'colors3':
            {
                'front': light_slate_gray,
                'side': light_steel_blue,
                'top': lavender,
                'windows': yellow
            },
        'colors4':
            {
                'front': red,
                'side': tomato,
                'top': coral,
                'windows': yellow
            }
    }

    colors_for_street = {'street': street, 'lines': white}

    # building details
    bwidth = 75
    bheight = 150
    row1_y = 180
    row2_y = 360
    row3_y = 540
    buildings = []
    building_row1 = []
    building_row1.append(Building(363.75, row1_y, bwidth, bheight, building_colors['colors1']))
    building_row1.append(Building(633.75, row1_y, bwidth, bheight, building_colors['colors2']))
    building_row1.append(Building(903.75, row1_y, bwidth, bheight, building_colors['colors3']))
    building_tbottom_y1 = row1_y + bheight - bwidth/2
    building_bottom_y1 = row1_y + bheight

    building_row2 = []
    building_row2.append(Building(187.5, row2_y, bwidth, bheight, building_colors['colors4']))
    building_row2.append(Building(457.5, row2_y, bwidth, bheight, building_colors['colors1']))
    building_row2.append(Building(727.5, row2_y, bwidth, bheight, building_colors['colors2']))
    building_tbottom_y2 = row2_y + bheight - bwidth/2
    building_bottom_y2 = row2_y + bheight

    building_row3 = []
    building_row3.append(Building(11.25, row3_y, bwidth, bheight, building_colors['colors3']))
    building_row3.append(Building(281.25, row3_y, bwidth, bheight, building_colors['colors4']))
    building_row3.append(Building(551.25, row3_y, bwidth, bheight, building_colors['colors1']))
    building_tbottom_y3 = row3_y + bheight - bwidth/2
    building_bottom_y3 = row3_y + bheight

    street = Street(0, 150, 1024, 30, colors_for_street)
    street.draw(screen)

    for building in building_row1:
        buildings.append(building)
        building.draw(screen)
    for building in building_row2:
        buildings.append(building)
        building.draw(screen)
    for building in building_row3:
        buildings.append(building)
        building.draw(screen)

    idle = True
    move_up = False
    move_down = False
    move_right = False
    move_left = False
    punch = False
    death = False
    sound_counter = 0

    font1 = pygame.font.Font('Assets/Font/Bowser.ttf', 120)
    text1 = font1.render("Bowser's Revenge", True, (255, 0, 0))
    textRect1 = text1.get_rect()
    textRect1.centerx = screen.get_rect().centerx
    textRect1.y = 5
    screen.blit(text1, textRect1)

    # Add “Press <Enter> To Play”
    font2 = pygame.font.Font('Assets/Font/Bowser.ttf', 30)
    text2 = font2.render("Move bowser with <arrow> keys. Punch with <space> key."
                         " Press <Enter> To Play", True, (255, 255, 255))
    textRect2 = text2.get_rect()
    textRect2.centerx = screen.get_rect().centerx
    textRect2.y = 110
    screen.blit(text2, textRect2)

    total_buildings = len(buildings)

    # Update the screen
    pygame.display.update()

    # Wait for enter to be pressed
    # The user can also quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    break

    while True:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()

        total_seconds = frame_count // frame_rate

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        # set the text for timer
        font3 = pygame.font.Font('Assets/Font/Bowser.ttf', 30)
        clock = font3.render(output_string, True, (0, 0, 0))

        # set text for score
        lives_string = "Lives Left: %d" % bowser.health
        building_score = "Buildings left: %d" % (total_buildings - bscore)
        font4 = pygame.font.Font('Assets/Font/Bowser.ttf', 20)
        health_display = font4.render(lives_string, True, (0, 0, 0))
        bscore_display = font4.render(building_score, True, (0, 0, 0))

        # randomly play traffic sound
        if frame_count is not 0 and frame_count % 800 == 0:
            traffic_sound.play()
        # draw background grass
        screen.fill(grass)

        # draw timer
        screen.blit(clock, [20, 20])
        screen.blit(health_display, [880, 20])
        screen.blit(bscore_display, [845, 35])

        street.draw(screen)

        # draw cars group
        for car in cars:
            car.draw(screen)

        ###################
        # Monitor keyboard events
        pressed = pygame.key.get_pressed()

        # bowser key events
        if punch or death is False:
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    idle = False
                    move_right = True
                if event.key == K_LEFT:
                    idle = False
                    move_left = True
                if event.key == K_UP:
                    idle = False
                    move_up = True
                if event.key == K_DOWN:
                    idle = False
                    move_down = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    idle = True
                    move_right = False
                if event.key == K_LEFT:
                    idle = True
                    move_left = False
                if event.key == K_UP:
                    idle = True
                    move_up = False
                if event.key == K_DOWN:
                    idle = True
                    move_down = False

        if pressed[K_SPACE]:
            idle = False
            move_right = False
            move_left = False
            move_down = False
            move_up = False
            punch = True

        if bowser.health is 0:
            death = True

        # Controls bowsers movements incuding being idle, moving, and punching
        # All of bowsers drawings occur here
        if idle:
            bowser.idle(screen, frame_count)

        if move_right:
            move_left = False
            bowser.go_right(screen, frame_count, buildings)

        if move_left:
            move_right = False
            bowser.go_left(screen, frame_count, buildings)

        if move_down:
            move_up = False
            bowser.go_down(screen, frame_count, buildings)

        if move_up:
            move_down = False
            bowser.go_up(screen, frame_count, buildings)

        if punch:
            collide = False
            loop = 0
            # check if colliding with building rect
            for building in buildings:
                if bowser.rect.right == building.rect.left or bowser.rect.left == building.rect.right:
                    if sound_counter < 1:
                        punch_sound.play(0)
                        sound_counter += 1
                    punch = bowser.punch(screen, frame_count)
                    if punch is False:
                        sound_counter = 0
                        idle = True
                        building.drop_health()
                        if building.health is 0:
                            bscore += 1
                            buildings.remove(building)
                else:
                    if loop < 1:
                        punch = bowser.punch(screen, frame_count)
                        if punch is False:
                            sound_counter = 0
                            idle = True
                loop += 1

        for car in cars:
            collision = bowser.rect.colliderect(car.rect)
            if collision:
                bowser.health_drop()
                hurt.play()
                blast.play()
                car.explode(screen)
                source = dir_car_check(car.direction)
                cars.add(Car(car.ox, car.oy, car.direction, car.speed, source))
                cars.remove(car)

         # draw buildings
        for building in buildings:
            building.draw(screen)

        tree.draw(screen)

        if death:
            screen.fill(black)
            death = bowser.die(screen, frame_count)
            if death is False:
                game_over = True

        if bscore is total_buildings:
            screen.fill(white)
            game_won = True

        pygame.display.update()  # Update the display when all events have been processed
        frame_count += 1
        fps_clock.tick(fps)

        while game_over:
            screen.fill(black)
            font4 = pygame.font.Font('Assets/Font/Bowser.ttf', 100)
            dead = font4.render("GAME OVER", True, (255, 255, 255))
            deadRect = dead.get_rect()
            deadRect.centerx = screen.get_rect().centerx
            screen.blit(dead, deadRect)
            screen.blit(bowser.dying_frames_r[-1], (screen.get_rect().centerx, screen.get_rect().centery))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over = False
                        return
        while game_won:
            timer = "Time: {0:02}:{1:02}".format(minutes, seconds)
            screen.fill(white)
            font5 = pygame.font.Font('Assets/Font/Bowser.ttf', 100)
            win = font5.render("YOU WIN!!! %s" % timer, True, (0, 0, 0))
            deadRect = win.get_rect()
            deadRect.centerx = screen.get_rect().centerx
            screen.blit(win, deadRect)
            screen.blit(bowser.win, (screen.get_rect().centerx, screen.get_rect().centery))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_won = False
                        return

def dir_car_check(direction):
    if direction is "right":
        return "Assets/Pictures/white_car_r.png"
    elif direction is "left":
        return "Assets/Pictures/white_car_l.png"
    elif direction is "up":
        return "Assets/Pictures/white_car_u.png"
    elif direction is "down":
        return "Assets/Pictures/white_car_d.png"

if __name__ == "__main__":
    main()
