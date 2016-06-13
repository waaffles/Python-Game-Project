"""
This class is to support our main character bowser with all his movements and animations
"""

import pygame
from spritesheet import SpriteSheet


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # sprite dimensions
    idle_width = 68.7142857
    idle_length = 71

    walking_width = 93
    walking_length = 85

    punching_width = 97
    punching_length = 90

    death_width = 88
    death_length = 75

    # current images
    current_idle = 0
    current_walk = 0
    current_punch = 0
    current_death = 0

    # number of images in each frame array
    noi_idle = 6
    noi_walking = 15
    noi_punching = 27
    noi_dying = 12

    # This holds all the images for the animated walk/punch left/right
    # of our player
    idle_frames_r = []
    idle_frames_l = []
    walking_frames_l = []
    walking_frames_r = []
    punching_frames_r = []
    punching_frames_l = []
    dying_frames_l = []
    dying_frames_r = []

    # What direction is the player facing?


    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        self.health = 10
        self.direction = "R"
        self.win = pygame.image.load("Assets/Pictures/bowser_win.png").convert_alpha()

        # get images for right idle
        for number in range(0, 7):
            bowser_r_idle_sheet = SpriteSheet('Assets/Pictures/bowser_idle_r.png')
            image = bowser_r_idle_sheet.get_image(number * self.idle_width, 0, self.idle_width, self.idle_length)
            self.idle_frames_r.append(image)
            self.idle_frames_l.append(pygame.transform.flip(image, True, False))

        # get images for right/left walking
        for row in range(0, 3):
            for column in range(0, 6):
                bowser_r_walking_sheet = SpriteSheet('Assets/Pictures/bowser_walking_r.png')
                if row != 2:
                    image = bowser_r_walking_sheet.get_image(
                        column * self.walking_width, row * self.walking_length, self.walking_width, self.walking_length
                    )
                    self.walking_frames_r.append(image)
                    self.walking_frames_l.append(pygame.transform.flip(image, True, False))
                else:
                    if column < 4:
                        image = bowser_r_walking_sheet.get_image(
                            column * self.walking_width, row * self.walking_length, self.walking_width, self.walking_length
                        )
                        self.walking_frames_r.append(image)
                        self.walking_frames_l.append(pygame.transform.flip(image, True, False))

        # get images for right/left facing punching
        for row in range(0, 5):
            for column in range(0, 6):
                bowser_r_punching_sheet = SpriteSheet('Assets/Pictures/bowser_punching_r.png')
                if row != 4:
                    image = bowser_r_punching_sheet.get_image(
                        column * self.punching_width, row * self.punching_length, self.punching_width, self.punching_length
                    )
                    self.punching_frames_r.append(image)
                    self.punching_frames_l.append(pygame.transform.flip(image, True, False))
                else:
                    if column < 4:
                        image = bowser_r_punching_sheet.get_image(
                            column * self.punching_width, row * self.punching_length, self.punching_width, self.punching_length
                        )
                        self.punching_frames_r.append(image)
                        self.punching_frames_l.append(pygame.transform.flip(image, True, False))

        # get images for right/left facing dying
        for row in range(0, 3):
            for column in range(0, 6):
                bowser_r_dying_sheet = SpriteSheet('Assets/Pictures/bowser_death_r.png')
                if row != 2:
                    image = bowser_r_dying_sheet.get_image(
                        column * self.death_width, row * self.death_length, self.death_width, self.death_length
                    )
                    self.dying_frames_r.append(image)
                    self.dying_frames_l.append(pygame.transform.flip(image, True, False))
                else:
                    if column < 1:
                        image = bowser_r_dying_sheet.get_image(
                            column * self.death_width, row * self.death_length, self.death_width, self.death_length
                        )
                        self.dying_frames_r.append(image)
                        self.dying_frames_l.append(pygame.transform.flip(image, True, False))

        # Set the image the player starts with
        self.image = self.idle_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width -= 15
        self.rect.height -= 10
        print(self.rect)

    def idle(self, screen, frame_count):
        if self.direction == "R":
            idle_frames = self.idle_frames_r
        else:
            idle_frames = self.idle_frames_l
        if frame_count % 2 == 0:
                if self.current_idle > self.noi_idle-1:
                    idle_frames.reverse()
                    self.current_idle = 0
                else:
                    self.current_idle += 1
        screen.blit(idle_frames[self.current_idle], (self.rect.x + 15, self.rect.y))

    # Player-controlled movement:
    def go_left(self, screen, frame_count, buildings):
        """ Called when the user hits the left arrow. """
        if self.rect.left > 0:
            self.rect.x -= 3

        b_collide = pygame.sprite.spritecollide(self, buildings, False)
        for collision in b_collide:
            self.rect.left = collision.rect.right

        self.direction = "L"
        if frame_count % 2 == 0:
            if self.current_walk > self.noi_walking-1:
                self.current_walk = 0
            else:
                self.current_walk += 1
        screen.blit(self.walking_frames_l[self.current_walk], (self.rect.x, self.rect.y))

    def go_right(self, screen, frame_count, buildings):
        """ Called when the user hits the right arrow. """
        if self.rect.right < 1024:
            self.rect.x += 3

        b_collide = pygame.sprite.spritecollide(self, buildings, False)
        for collision in b_collide:
            self.rect.right = collision.rect.left

        self.direction = "R"
        if frame_count % 2 == 0:
            if self.current_walk > self.noi_walking-1:
                self.current_walk = 0
            else:
                self.current_walk += 1
        screen.blit(self.walking_frames_r[self.current_walk], (self.rect.x, self.rect.y))

    def go_up(self, screen, frame_count, buildings):
        """ Called when the user hits the left arrow. """
        if self.direction == "R":
            walking_frames = self.walking_frames_r
        else:
            walking_frames = self.walking_frames_l
        if self.rect.top > 0:
            self.rect.y -= 3

        b_collide = pygame.sprite.spritecollide(self, buildings, False)
        for collision in b_collide:
            self.rect.top = collision.rect.bottom

        if frame_count % 2 == 0:
            if self.current_walk > self.noi_walking-1:
                self.current_walk = 0
            else:
                self.current_walk += 1
        screen.blit(walking_frames[self.current_walk], (self.rect.x, self.rect.y))

    def go_down(self, screen, frame_count, buildings):
        """ Called when the user hits the right arrow. """
        if self.direction == "R":
            walking_frames = self.walking_frames_r
        else:
            walking_frames = self.walking_frames_l
        if self.rect.bottom < 800:
            self.rect.y += 3

        b_collide = pygame.sprite.spritecollide(self, buildings, False)
        for collision in b_collide:
            self.rect.bottom = collision.rect.top

        if frame_count % 2 == 0:
            if self.current_walk > self.noi_walking-1:
                self.current_walk = 0
            else:
                self.current_walk += 1
        screen.blit(walking_frames[self.current_walk], (self.rect.x, self.rect.y))

    def punch(self, screen, frame_count):
        if self.direction == "R":
            punching_frames = self.punching_frames_r
        else:
            punching_frames = self.punching_frames_l
        if frame_count % 2 == 0:
            if self.current_punch > self.noi_punching-1:
                self.current_punch = 0
                return False
            else:
                self.current_punch += 1
        screen.blit(punching_frames[self.current_punch], (self.rect.x, self.rect.y))
        return True

    def die(self, screen, frame_count):
        if self.direction == "R":
            dying_frames = self.dying_frames_r
        else:
            dying_frames = self.dying_frames_l
        if frame_count % 2 == 0:
            if self.current_death > self.noi_dying-1:
                self.current_death = 0
                return False
            else:
                self.current_death += 1
        screen.blit(dying_frames[self.current_death], (screen.get_rect().centerx, screen.get_rect().centery))
        return True

    def health_drop(self):
        self.health -= 1
