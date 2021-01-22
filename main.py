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
music = pygame.mixer.music.load('./mic/main.mp3')
pygame.mixer.music.play(-1)

score = 0
bullets = []
emenies = []
font = pygame.font.SysFont('comicsans', 30, True)
hero = Player(300, 410, 64, 64)
emenies.append(Emeny(100, 410, 64, 64, 450))
shoot_loop = 0

def redraw_game_window():
    window.blit(background, (0,0))
    text = font.render('Score: {}'.format(score), 1, (0,0,0))
    window.blit(text, (390, 10))
    hero.draw(window)
    if emenies:
        for emeny in emenies:
            emeny.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

while run:
    clock.tick(27)
    if emenies:
        for emeny in emenies:
            if hero.hitbox[1] < emeny.hitbox[1] + emeny.hitbox[3] \
                    and hero.hitbox[1] + hero.hitbox[3] > emeny.hitbox[1]:
                if hero.hitbox[0] + hero.hitbox[2] > emeny.hitbox[0] \
                        and hero.hitbox[0] < emeny.hitbox[0] + emeny.hitbox[2]:
                    hero.hit(window)
                    score -= 5
    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if emenies:
            for emeny in emenies:
                if bullet.y - bullet.radius < emeny.hitbox[1] + emeny.hitbox[3] \
                    and bullet.y + bullet.radius > emeny.hitbox[1]:
                    if bullet.x + bullet.radius > emeny.hitbox[0] \
                        and bullet.x - bullet.radius < emeny.hitbox[0] + emeny.hitbox[2]:
                        emeny.hit()
                        if not emeny.visible:
                            emenies.pop(emenies.index(emeny))
                        score += 1
                        bullets.pop(bullets.index(bullet))
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f] and shoot_loop == 0:
        if hero.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Gun(round(hero.x+hero.width//2),
                               round(hero.y+hero.height//2),
                               3, (255, 0, 0), facing))
        shoot_loop = 1

    if keys[pygame.K_LEFT] and hero.x > hero.vel:
        hero.left = True
        hero.right = False
        hero.x -= hero.vel
        hero.standing = False
    elif keys[pygame.K_RIGHT] and hero.x < screen_size[0] - hero.width - hero.vel:
        hero.left = False
        hero.right = True
        hero.x += hero.vel
        hero.standing = False
    else:
        hero.standing = True
        hero.walk_count = 0

    if not hero.is_jump:
        if keys[pygame.K_SPACE]:
            hero.is_jump = True
            hero.right = False
            hero.left = False
            hero.walk_count = 0
    else:
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

