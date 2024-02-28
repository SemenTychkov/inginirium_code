import  pygame
import  random

GRAY = [70] * 3
BLACK = [0] * 3
WHITE = [255] * 3
W, H = 500, 500



pygame.init()
win = pygame.display.set_mode((W, H))
object_to_draw = ''

win.fill((255, 255, 255))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        object_to_draw = 'krug'
    if keys[pygame.K_q]:
        object_to_draw = 'kvadrat'
    if object_to_draw == 'krug':
        pygame.draw.circle(win,random.choices(range(256),k=3),(x , y) , 30)
    if object_to_draw == 'kvadrat':
        pygame.draw.rect(win,random.choices(range(256),k=3),(x , y ,60 ,60))
    if keys[pygame.K_SPACE]:
        exit()

    pygame.display.update()

    pygame.time.delay(20)