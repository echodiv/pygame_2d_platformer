import pygame
from GameExceptions import EnemyNotFoundError, BulletNotFoundError

class Map(object):
    def __init__(self, x: int, y: int):
        self.background = pygame.image.load('./img/bg.jpg')
        self.font = pygame.font.SysFont('comicsans', 30, True)
        self.x = x
        self.y = y
        self.emenies = []
        self.hero = None
        self.bullets = []

    def load(self):
        pygame.display.set_caption("Main Game")
        music = pygame.mixer.music.load('./mic/main.mp3')
        pygame.mixer.music.play(-1)

    def add_hero(self, hero):
        self.hero = hero

    def add_enemy(self, enemy):
        self.emenies.append(enemy)

    def add_bullet(self, bulet):
        self.bullets.append(bulet)

    def remove_enemy(self, enemy):
        try:
            self.emenies.pop(self.emenies.index(enemy))
        except IndexError:
            raise EnemyNotFoundError

    def remove_bullet(self, enemy):
        try:
            self.bullets.pop(self.bullets.index(enemy))
        except IndexError:
            raise BulletNotFoundError

    def draw(self, window):
        window.blit(self.background, (0, 0))
        text = self.font.render('Score: {}'.format(self.hero.score), 1, (0, 0, 0))
        window.blit(text, (390, 10))

        if self.emenies:
            for enemy in self.emenies:
                enemy.draw(window)
        if self.bullets:
            for bullet in self.bullets:
                bullet.draw(window)
        if self.hero:
            self.hero.draw(window)
        pygame.display.update()

