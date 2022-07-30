import pygame

import config
from block import Block
from player import Move, Player

pygame.init()
window = pygame.display.set_mode(
    (config.Config.display_width, config.Config.display_height)
)
pygame.display.set_caption("Circle Sprite")


player = Player()
player_sprites = pygame.sprite.GroupSingle()
player_sprites.add(player)

brick = Block()
brick_sprites = pygame.sprite.Group()
brick_sprites.add(brick)

clock = pygame.time.Clock()
run = True

background = pygame.image.load("./img/bg.jpg")

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(background, (0, 0))

    if pygame.sprite.spritecollide(player, brick_sprites, False):
        player.is_falling = False
    else:
        player.is_falling = True

    window.fill(config.Colors.SKY_BLUE)
    player_sprites.draw(window)
    player_sprites.update()

    brick_sprites.draw(window)

    pygame.display.flip()

    # Clamp FPS
    clock.tick_busy_loop(60)

pygame.quit()
