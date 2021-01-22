import pygame


class Emeny(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 3
        self.walk_right = [pygame.image.load('./img/R{}E.png'.format(i)) \
                           for i in range(1, 12)]
        self.walk_left = [pygame.image.load('./img/L{}E.png'.format(i)) \
                          for i in range(1, 12)]

    def draw(self, window):
        self.move()
        if self.walk_count + 1 >= 33:
            self.walk_count = 0
        if self.vel > 0:
            window.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            window.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0