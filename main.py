import pygame

pygame.init()

screen_size = (500, 500)
window = pygame.display.set_mode(screen_size)

pygame.display.set_caption("First Game")

walk_right = [pygame.image.load('./img/R1.png'),
              pygame.image.load('./img/R2.png'),
              pygame.image.load('./img/R3.png'),
              pygame.image.load('./img/R4.png'),
              pygame.image.load('./img/R5.png'),
              pygame.image.load('./img/R6.png'),
              pygame.image.load('./img/R7.png'),
              pygame.image.load('./img/R8.png'),
              pygame.image.load('./img/R9.png'),]

walk_left = [pygame.image.load('./img/L1.png'),
             pygame.image.load('./img/L2.png'),
             pygame.image.load('./img/L3.png'),
             pygame.image.load('./img/L4.png'),
             pygame.image.load('./img/L5.png'),
             pygame.image.load('./img/L6.png'),
             pygame.image.load('./img/L7.png'),
             pygame.image.load('./img/L8.png'),
             pygame.image.load('./img/L9.png'),]

background = pygame.image.load('./img/bg.jpg')
char = pygame.image.load('./img/standing.png')

clock = pygame.time.Clock()

x = 150
y = 350
width = 64
height = 64
vel = 5
left = False
right = False
walk_count = 0


is_jump = False
jump_count = 10
run = True

def redraw_game_window():
    global walk_count
    window.blit(background, (0,0))
    if walk_count + 1 >= 27:
        walk_count = 0

    if left:
        window.blit(walk_left[walk_count//3], (x, y))
        walk_count += 1

    elif right:
        window.blit(walk_right[walk_count//3], (x, y))
        walk_count += 1

    else:
        window.blit(char, (x, y))

    pygame.display.update()

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        left = True
        right = False
        x -= vel

    elif keys[pygame.K_RIGHT] and x < screen_size[0] - width - vel:
        left = False
        right = True
        x += vel

    else:
        right = False
        left = False
        walk_count = 0

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True

    else:
        right = False
        left = False
        walk_count = 0

        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= neg *(jump_count ** 2) * 0.5
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    redraw_game_window()


pygame.quit()

