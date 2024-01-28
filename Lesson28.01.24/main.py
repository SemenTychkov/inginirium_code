import pygame

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width,height))

xCircle = width / 2
yCircle = height / 2
cx = width / 2
cy = height / 2
color =(0,255,255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if  keys[pygame.K_LEFT]:
        xCircle-=5
    elif  keys[pygame.K_RIGHT]:
        xCircle+=5
    elif  keys[pygame.K_UP]:
        yCircle-=5
    elif  keys[pygame.K_DOWN]:
        yCircle+=5
    else:
        xCircle = width / 2
        yCircle = height / 2
    if xCircle >cx + 150:
       color = (255,255,0)
    elif xCircle <cx - 150:
       color = (255,255,0)
    elif yCircle >cy + 150:
       color = (255,255,0)
    elif yCircle < cy - 150:
           color = (255, 255, 0)
    else:
        



    win.fill((25,200,50))
    pygame.draw.circle(win,color,(xCircle,yCircle),30)
    pygame.display.update()
    pygame.time.delay(10)