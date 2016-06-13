import pygame


class Car(pygame.sprite.Sprite):

    car_list = pygame.sprite.Group()

    def __init__(self, x, y, direction, speed, source):
        super().__init__()
        self.x = self.ox = x
        self.y = self.oy = y
        self.speed = speed
        self.direction = direction
        self.car = pygame.image.load(source).convert_alpha()
        self.explosion = pygame.image.load("Assets/Pictures/fireball.png").convert_alpha()
        self.rect = self.car.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width -= 8
        self.rect.height -= 8

    def draw(self, screen):
        self.change_x(self.speed)
        screen.blit(self.car, (self.x, self.y))

    def explode(self, screen):
        screen.blit(self.explosion, (self.x-10, self.y-10))

    def change_x(self, inc):
        if self.direction == 'left':
            self.x -= inc
            self.rect.x = self.x
            if self.x < -30:
                self.x = 1040
                self.rect.x = self.x
        if self.direction == 'right':
            self.x += inc
            self.rect.x = self.x
            if self.x > 1040:
                self.x = -30
                self.rect.x = self.x
        if self.direction == 'down':
            self.x -= inc * .97
            self.y += inc
            self.rect.x = self.x
            self.rect.y = self.y
            if self.y > 830 or self.x < -30:
                if self.ox < 530:
                    self.x = 527
                    self.y = 0
                if 530 < self.ox < 1000:
                    self.x = 699
                    self.y = 0
                if 1000 < self.ox < 1200:
                    self.x = 1030
                    self.y = 45
        if self.direction == 'up':
            self.x += inc * .97
            self.y -= inc
            self.rect.x = self.x
            self.rect.y = self.y
            if self.y < -30 or self.x > 1040:
                if self.ox < 31:
                    self.x = 30
                    self.y = 800
                if 31 < self.ox < 200:
                    self.x = 699
                    self.y = 0
                if 700 < self.ox < 800:
                    self.x = 699
                    self.y = 20

    def get_car(self):
        return self.car


