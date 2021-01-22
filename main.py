import pygame
from Emeny import Emeny
from Gun import Gun
from Player import Player

pygame.init()

screen_size = (500, 500)
window = pygame.display.set_mode(screen_size)

pygame.display.set_caption("First Game")
background = pygame.image.load('./img/bg.jpg')
clock = pygame.time.Clock()

run = True
bullets = []

def redraw_game_window():
    window.blit(background, (0,0))
    hero.draw(window)
    goblin.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

hero = Player(300, 410, 64, 64)
goblin = Emeny(100, 410, 64, 64, 450)

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if len(bullets) < 5:
            if hero.last_move == "right":
                facing = 1
            else:
                facing = -1
            bullets.append(Gun(round(hero.x+hero.width//2),
                               round(hero.y+hero.height//2),
                               3, (255, 0, 0), facing))
    if keys[pygame.K_LEFT] and hero.x > hero.vel:
        hero.left = True
        hero.right = False
        hero.x -= hero.vel
        hero.last_move = "left"
        hero.standing = False
    elif keys[pygame.K_RIGHT] and hero.x < screen_size[0] - hero.width - hero.vel:
        hero.left = False
        hero.right = True
        hero.x += hero.vel
        hero.last_move = "right"
        hero.standing = False
    else:
        hero.standing = True
        hero.walk_count = 0

    if not hero.is_jump:
        if keys[pygame.K_SPACE]:
            hero.is_jump = True
    else:
        hero.right = False
        hero.left = False
        hero.standing = True
        hero.walk_count = 0

        if hero.jump_count >= -10:
            neg = 1
            if hero.jump_count < 0:
                neg = -1
            hero.y -= neg *(hero.jump_count ** 2) * 0.5
            hero.jump_count -= 1
        else:
            hero.is_jump = False
            hero.jump_count = 10

    redraw_game_window()

pygame.quit()

