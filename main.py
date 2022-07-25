import pygame
from config import config
from Collision import Collision
from Enemy import Enemy
from app.Ground import Earth
from Gun import Gun
from Player import Player
from Map import Map

pygame.init()

screen_size = (config.display_width, config.display_height)
window = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

run = True
map = Map(0, 0)
# map.load()
# map.add_enemy(Enemy(100, 630, 64, 64, 450))
map.add_hero(Player(50, 630, 64, 64))
map.add_block(Earth(200, 590, 100, 100))
shoot_loop = 0

while run:
    clock.tick(27)
    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in map.bullets:
        for enemy in map.emenies:
            if not enemy.visible:
                map.remove_enemy(enemy)
            if Collision.bullet_and_target(bullet, enemy):
                enemy.hit()
                map.hero.score += 1
                map.remove_bullet(bullet)
        if bullet.x < 1280 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            map.remove_bullet(bullet)

    for block in map.blocks:
        if Collision.hero_on_block(block, map.hero) and not map.hero.is_jump:
            map.hero.y = block.hitbox[1] - 52
            map.hero.faling = False
        else:
            map.hero.faling = True
        if Collision.hero_under_block(block, map.hero):
            pass
        if Collision.hero_and_left_border_of_block(block, map.hero):
            pass
        if Collision.hero_and_right_border_of_block(block, map.hero):
            pass

        for bullet in map.bullets:
            if Collision.bullet_and_target(bullet, block):
                map.remove_bullet(bullet)

    for enemy in map.emenies:
        if Collision.enemy_attack(enemy, map.hero):
            text = map.font.render('-5', 1, (255, 0, 0))
            window.blit(text, (250 - (text.get_width() / 2), 200))
            map.hero.score -= 5
            map.hero.hit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f] and shoot_loop == 0:
        if map.hero.left:
            facing = -1
        else:
            facing = 1
        if len(map.bullets) < 5:
            map.add_bullet(Gun(round(map.hero.x+map.hero.width//2),
                               round(map.hero.y+map.hero.height//2),
                               3, (255, 0, 0), facing))
        shoot_loop = 1

    if keys[pygame.K_LEFT] and map.hero.x > map.hero.vel:
        map.hero.move_left()
    elif keys[pygame.K_RIGHT] and map.hero.x < screen_size[0] - map.hero.width - map.hero.vel:
        map.hero.move_right()
    else:
        map.hero.standing = True
        map.hero.walk_count = 0

    if not map.hero.is_jump:
        if keys[pygame.K_SPACE]:
            map.hero.is_jump = True
            map.hero.right = False
            map.hero.left = False
            map.hero.walk_count = 0
    else:
        if map.hero.jump_count >= 0:
            neg = 1
            map.hero.y -= neg *(map.hero.jump_count ** 2) * 0.5
            map.hero.jump_count -= 1
        else:
            map.hero.is_jump = False
            map.hero.jump_count = 10
            map.hero.faling = True
    map.draw(window)

pygame.quit()

