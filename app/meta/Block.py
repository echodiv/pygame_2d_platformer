import pygame


class Block(object):
    def __init__(self, x:int, y:int, height:int, width:int) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, self.height, self.width)
        # self.background = background

    def move(self, delta_x: int, delta_y: int) -> None:
        self.hitbox = (self.x - delta_x,
                       self.y - delta_y,
                       self.height, self.width)

    def draw(self, window) -> None:
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)