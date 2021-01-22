import pygame


class Gun():
    def __init__(self, x: int, y: int, radius: int, color: set, facing: str) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
