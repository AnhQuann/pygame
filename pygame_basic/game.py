import pygame

# 1. Init
pygame.init()

# 2. Setup game window
# list => can change, mutable
# tuple => can not change, immutable
size = (600, 800)
canvas = pygame.display.set_mode(size)

# 3. Clock
clock = pygame.time.Clock()
loop = True

# 4.1 Load Image
player_image_1 = pygame.image.load('player1.png')
player_image_2 = pygame.image.load('player2.png')

x1 = 100
y1 = 200

x2 = 500
y2 = 200
while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]: y1 -= 5
    if pressed[pygame.K_s]: y1 += 5
    if pressed[pygame.K_a]: x1 -= 5
    if pressed[pygame.K_d]: x1 += 5

    # if pressed[pygame.K_UP]: y2 -= 5
    # if pressed[pygame.K_DOWN]: y2 += 5
    # if pressed[pygame.K_LEFT]: x2 -= 5
    # if pressed[pygame.K_RIGHT]: x2 += 5

    (x2, y2) = pygame.mouse.get_pos()

    # clear canvas
    canvas.fill((255, 0, 0))

    # draw image
    canvas.blit(player_image_1, (x1, y1))
    canvas.blit(player_image_2, (x2, y2))

    clock.tick(60)
    pygame.display.flip() #back buffer
