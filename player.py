from enum import Enum

import pygame

import config


class Move(Enum):
    RIGHT = 1
    LEFT = 2
    STAND = 3


class Player(pygame.sprite.Sprite):
    _MAX_JUMP_COUNT = 10
    _MAX_WALK_COUNT = 27

    _JUMP_SPEED = 0.3
    _FALL_SPEED = 0.15
    _MOVE_SPEED = 5

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)

        self._walk_count = 0
        self.jump_count = 10

        self.image_stand = pygame.image.load("./img/standing.png")
        self.walk_right = [
            pygame.image.load("./img/R{}.png".format(i)) for i in range(1, 10)
        ]
        self.walk_left = [
            pygame.image.load("./img/L{}.png".format(i)) for i in range(1, 10)
        ]

        self.is_jump = False
        self.is_falling = True
        self.move = Move.STAND
        self.image = self.image_stand
        self.rect = self.image.get_rect()
        self.rect.center = (
            config.Config.display_width / 2,
            config.Config.display_height / 2,
        )

    @property
    def walk_count(self):
        return self._walk_count

    @walk_count.setter
    def walk_count(self, new):
        if new >= self._MAX_WALK_COUNT:
            self._walk_count = 0
            return
        self._walk_count = new

    def update(self) -> None:
        self._detect_moving_command()

        match self.move:
            case Move.LEFT:
                self._move_left()
            case Move.RIGHT:
                self._move_right()
            case _:
                self._stop_moving()

        if self.is_jump:
            self._jump()
        elif self.is_falling:
            self._fall()

    def _detect_moving_command(self):
        keys = pygame.key.get_pressed()

        # jump
        if keys[pygame.K_SPACE]:
            self.is_jump = True

        # moving by x
        if keys[pygame.K_LEFT]:
            self.move = Move.LEFT
        elif keys[pygame.K_RIGHT]:
            self.move = Move.RIGHT
        else:
            self.move = Move.STAND

    def _jump(self):
        if self.jump_count > 0:
            self.rect.move_ip(0, -(self.jump_count**2) * self._JUMP_SPEED)
            self.jump_count -= 1
        else:
            self.jump_count = self._MAX_JUMP_COUNT
            self.is_jump = False

    def _move_right(self):
        self.image = self.walk_right[self.walk_count // 3]
        self.rect.move_ip(+self._MOVE_SPEED, 0)
        self.walk_count += 1

    def _move_left(self):
        self.image = self.walk_left[self.walk_count // 3]
        self.rect.move_ip(-self._MOVE_SPEED, 0)
        self.walk_count += 1

    def _fall(self):
        self.rect.move_ip(0, +(self.jump_count**2) * self._FALL_SPEED)

    def _stop_moving(self):
        self.image = self.image_stand
        self.walk_count = 0
