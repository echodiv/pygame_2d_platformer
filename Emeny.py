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
        self.vel: int = 3
        self.health: int = 10
        self.visible: bool = True
        self.hitbox: set = (self.x+17, self.y+2, 31, 57)
        self.walk_right = [pygame.image.load('./img/R{}E.png'.format(i)) \
                           for i in range(1, 12)]
        self.walk_left = [pygame.image.load('./img/L{}E.png'.format(i)) \
                          for i in range(1, 12)]
        self.hit_sound = pygame.mixer.Sound('./mic/punch.wav')

    def draw(self, window):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0
            if self.vel > 0:
                window.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                window.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1]-20, 50, 10))
            pygame.draw.rect(window, (0,255,0), (self.hitbox[0], self.hitbox[1]-20, 50-(5*(10-self.health)), 10))
            self.hitbox = (self.x+17, self.y+2, 31, 57)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

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

    def hit(self):
        self.hit_sound.play()
        if self.health > 0:
            self.health -= 1;
        else:
            self.visible = False
