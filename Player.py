import pygame


class Player(object):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x: int = x
        self.y: int = y
        self.vel: int = 5
        self.score: int = 0
        self.width: int = width
        self.height: int = height
        self.walk_count: int = 0
        self.jump_count: int = 10
        self.left: bool = False
        self.right: bool = False
        self.is_jump: bool = False
        self.standing: bool = True
        self.hitbox: set = (self.x + 17, self.y + 11, 29, 52)
        self.char = pygame.image.load('./img/standing.png')
        self.walk_right = [pygame.image.load('./img/R{}.png'.format(i)) \
                           for i in range(1, 10)]
        self.walk_left = [pygame.image.load('./img/L{}.png'.format(i)) \
                          for i in range(1, 10)]

    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                window.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                window.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.right:
                window.blit(self.walk_right[0], (self.x, self.y))
            elif self.left:
                window.blit(self.walk_left[0], (self.x, self.y))
            else:
                window.blit(self.char, (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.is_jump = False
        self.jump_count = 0
        self.x = 60
        self.y = 410
        self.walk_count = 0
        font = pygame.font.SysFont('comicsans', 100)
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()