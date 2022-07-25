import pygame

from config import config
from GameExceptions import (BlockNotFoundError, BulletNotFoundError,
                            EnemyNotFoundError)


class Map(object):
    def __init__(self, x: int, y: int):
        self.background = pygame.image.load("./img/bg.jpg")
        self.font = pygame.font.SysFont("comicsans", 30, True)
        self.x: int = x
        self.y: int = y
        self.hero = None
        self.bullets = []
        self.blocks = []
        self.emenies = []

    def load(self):
        pygame.display.set_caption("Main Game")
        music = pygame.mixer.music.load("./mic/main.mp3")
        pygame.mixer.music.play(-1)

    def add_hero(self, hero):
        self.hero = hero

    def add_enemy(self, enemy):
        self.emenies.append(enemy)

    def add_bullet(self, bulet):
        self.bullets.append(bulet)

    def add_block(self, block):
        self.blocks.append(block)

    def remove_block(self, block):
        try:
            self.blocks.pop(self.blocks.index(block))
        except:
            raise BlockNotFoundError

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

        if self.hero.x > config.map_move_x_border_right:
            self.x += self.hero.x - config.map_move_x_border_right
            self.hero.x = config.map_move_x_border_right

        if self.x > 0 and self.hero.x < config.map_move_x_border_left:
            self.x += self.hero.x - config.map_move_x_border_left
            self.hero.x = config.map_move_x_border_left

        text = self.font.render(
            "x: {}, y: {}, dx: {}, dy: {}".format(
                self.hero.x, self.hero.y, self.x, self.y
            ),
            1,
            (0, 0, 0),
        )
        window.blit(text, (0, 50))

        text = self.font.render("Score: {}".format(self.hero.score), 1, (0, 0, 0))
        window.blit(text, (1150, 10))

        if self.emenies:
            for enemy in self.emenies:
                enemy.draw(window)
        if self.bullets:
            for bullet in self.bullets:
                bullet.draw(window)
        if self.blocks:
            for block in self.blocks:
                block.move(self.x, self.y)
                block.draw(window)
        if self.hero:
            self.hero.draw(window)
        pygame.display.update()
