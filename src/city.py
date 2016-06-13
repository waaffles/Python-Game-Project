import pygame
import random


class Building(pygame.sprite.Sprite):

    def __init__(self, x, y, width, length, colors):
        super().__init__()
        self.health = 3
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.colors = colors
        self.rect = pygame.Rect(
            self.x, self.y + self.length - (self.width/2), self.width + (self.width/3.5), self.width/2
        )

    def draw(self, screen):

        bottom_x = self.x + self.width
        bottom_y = self.y + self.length

        # Draw front of building
        pygame.draw.rect(
            screen,
            self.colors['front'],
            [
                self.x,
                self.y,
                self.width,
                self.length
            ]
        )

        # Draw top of building
        pygame.draw.polygon(
            screen,
            self.colors['top'],
            [
                [self.x, self.y],
                [self.x + (self.width/2), self.y - (self.width/2)],
                [self.x + (self.width/2) + self.width, self.y - (self.width/2)],
                [self.x + self.width, self.y]
            ]
        )

        # Draw side of building
        pygame.draw.polygon(
            screen,
            self.colors['side'],
            [
                [bottom_x, bottom_y],
                [bottom_x, self.y],
                [bottom_x + (self.width/2), self.y - (self.width/2)],
                [bottom_x + (self.width/2), bottom_y - (self.width/2)],
            ]
        )
        self.draw_windows(screen, self.x)

    def draw_windows(self, screen, new_self_x):
        for index in range(0, 3):
            pygame.draw.rect(
                screen,
                self.colors['windows'],
                [
                    new_self_x+(23*index+9),
                    self.y+20,
                    self.width/9,
                    self.width/9
                ]
            )
            for index2 in range(1, 7):
                pygame.draw.rect(
                    screen,
                    self.colors['windows'],
                    [
                        new_self_x+(23*index+9),
                        self.y+(20*index2),
                        self.width/9,
                        self.width/9
                    ]
                )

    def set_x(self, x):
        self.x = x

    def drop_health(self):
        self.health -= 1


class Street:

    def __init__(self, x, y, width, length, colors):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.colors = colors

    def draw(self, screen):
        for number in range(1, 5):
            new_y = self.y * 5/4 * number
            pygame.draw.rect(
                screen,
                self.colors['street'],
                [
                    self.x,
                    new_y,
                    self.width,
                    self.length
                ]
            )
            # self.__draw_roof(screen)
            diag_y = (self.y + self.length) * 1.5 * (number + 1)
            pygame.draw.polygon(
                screen,
                self.colors['street'],
                [
                    ([diag_y, 0]),
                    ([diag_y + self.length, 0]),
                    ([diag_y - (self.length * 33) + self.length, (self.x + (self.width/2))*2]),
                    ([diag_y - (self.length * 33), (self.x + (self.width/2))*2])
                ]
            )


class Tree:

    def __init__(self, x, y, source):
        self.x = x
        self.y = y
        self.tree = pygame.image.load(source).convert_alpha()

    def draw(self, screen):

        for number in range(1, 5):
            new_x = self.x * number
            if number == 1:
                screen.blit(self.tree, (new_x, self.y * number))
            if number == 2:
                screen.blit(self.tree, (new_x + 70, self.y * number - 113))
