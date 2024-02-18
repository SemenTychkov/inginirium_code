
import pygame

class Circl:
    def __init__(self, collor,x, y, rad):
        self.collor=collor
        self.x = x
        self.y = y
        self.rad = rad
        self.is_jump=False
        self.jump_counter = 15

    def draw(self):
            pygame.draw.circle(win, self.collor, (self.x, self.y), self.rad)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                self.x -= 3
        if keys[pygame.K_RIGHT]:
                self.x += 3
        if keys[pygame.K_UP]:
                self.y -= 3
        if keys[pygame.K_DOWN]:
                self.y += 3

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_jump= True
        if self.is_jump:
            if self.jump_counter>= -15:
                self.y -= self.jump_counter
                self.jump_counter-=2
            else:
                self.jump_counter= 15
                self.is_jump =False


FPS =60
clock = pygame.time.Clock()

pygame.init()
width=500
height=500
win= pygame.display.set_mode((width,height))
x=250
y=250
print('Cirkl')
Cirkl=Circl((255,255,0),0,0,30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    win.fill((255,255,255))

    Cirkl.draw()
    Cirkl.move_by_keys()
    Cirkl.jump()
    pygame.display.update()
    clock.tick(FPS)
    print(clock.get_fps())