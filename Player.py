import pygame

from config import config


class Player(object):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.img_x = x - 17
        self.img_y = y - 11
        self.y = y
        self.vel = 5
        self.score = 0
        self.width = width
        self.faling = True
        self.height = height
        self.walk_count = 0
        self.jump_count = 10
        self.left = False
        self.right = False
        self.is_jump = False
        self.standing = True
        self.hitbox = (self.x, self.y, 29, 52)
        self.char = pygame.image.load("./img/standing.png")
        self.walk_right = [
            pygame.image.load("./img/R{}.png".format(i)) for i in range(1, 10)
        ]
        self.walk_left = [
            pygame.image.load("./img/L{}.png".format(i)) for i in range(1, 10)
        ]

    def move_left(self) -> None:
        self.left = True
        self.right = False
        self.standing = False
        self.x -= self.vel

    def move_right(self) -> None:
        self.right = True
        self.left = False
        self.standing = False
        self.x += self.vel

    def move_up(self) -> None:
        pass

    def move_down(self) -> None:
        pass

    def draw(self, window):
        self.img_x = self.x - 17
        self.img_y = self.y - 11
        if self.faling:
            self.y += config.gravitation
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                window.blit(
                    self.walk_left[self.walk_count // 3], (self.img_x, self.img_y)
                )
                self.walk_count += 1
            elif self.right:
                window.blit(
                    self.walk_right[self.walk_count // 3], (self.img_x, self.img_y)
                )
                self.walk_count += 1
        else:
            if self.right:
                window.blit(self.walk_right[0], (self.img_x, self.img_y))
            elif self.left:
                window.blit(self.walk_left[0], (self.img_x, self.img_y))
            else:
                window.blit(self.char, (self.img_x, self.img_y))
        self.hitbox = (self.x, self.y, 29, 52)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.is_jump = False
        self.jump_count = 0
        self.x = 60
        self.y = 630
        self.walk_count = 0
        font = pygame.font.SysFont("comicsans", 100)
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
