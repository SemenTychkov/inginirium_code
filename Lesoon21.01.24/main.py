import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

x = 150
y = 150
i = 250
o =250
direction=1
directionO=1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x = x + direction
    o = o + directionO
    if o>500:
        directionO = -1
    if o < 0:
        directionO = 1
    if x > 500:
        direction = -1
    if x<0:
       direction=1
    win.fill((255,255,255))
    pygame.draw.rect(win,(255,255,0), (x,y,100,150))
    pygame.draw.circle(win, (0, 255, 255), (i, o), 50)
    pygame.display.update()
    pygame.time.delay(10)

