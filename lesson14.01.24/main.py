import pygame

pygame.init()
win = pygame.display.set_mode((500,500))
x=10
y=10
w =100
h =100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (255,255,255)
    win.fill(color)
    color = (25, 10, 0)
    win.fill(color)
    pygame.draw.line(win, (255, 255, 255), (0, 0), (500, 500), 10)
    pygame.draw.line(win, (255, 255, 255), (500, 0), (0, 500), 10)
    pygame.draw.circle(win, (255, 0, 0), (250, 250), 50)

    pygame.draw.rect(win, (255,255,0), (0,0,150,100))
    pygame.draw.line(win, (0, 255, 255), (0, 0), (100, 100) ,5)
    pygame.draw.circle(win, (255, 0, 0), (200, 200), 50)
    pygame.draw.lines(win, (0, 0, 0),True, ((200, 200), (300, 150),(300,250)), 10)
    pygame.draw.polygon(win, (0, 0, 0), [(0, 100), (100, 50),(100, 150)],False)



    pygame.display.update()







