import pygame

import config


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(config.Colors.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (
            config.Config.display_width / 2,
            100 + config.Config.display_height / 2,
        )
