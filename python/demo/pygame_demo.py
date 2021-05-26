import pygame

scrnWidth = 500
scrnHeight = 500
win = pygame.display.set_mode((scrnWidth, scrnHeight))
pygame.display.set_caption("First Game!")

# player properties
x = 50
y = 425
width = 40
height = 60
vel = 10

isJump = False
jumpCount = 10


def redrawWindow():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 200, 0), (x, y, width, height))
    pygame.display.update()


# main loop
run = True
while run:

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 502 - width - vel:
        x += vel
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 502 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    redrawWindow()
