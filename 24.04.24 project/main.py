import random

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Mario.png')
        self.image = self.image.convert_alpha()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 5
        if keys[pygame.K_DOWN]:
            self.rect.top += 5
        if keys[pygame.K_LEFT]:
            self.rect.left -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.left += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.image = self.image.convert_alpha()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
pygame.init()
width = 800

height = 500
win = pygame.display.set_mode((width, height))

background = pygame.image.load('1641243530_1-abrakadabra-fun-p-fon-igri-mario-1.jpg')

background = pygame.transform.scale(background, (width, height))


all_sprites = pygame.sprite.Group()


player = Player()

enemy_sprites = pygame.sprite.Group()

all_sprites.add(player)
for i in range(10):
    enemy = Enemy()
    enemy.rect.left = random.randint(0, width - enemy.rect.width)
    enemy_sprites.add(enemy)

FPS = 60
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




    hits = pygame.sprite.spritecollide(player, enemy_sprites, True)

    win.fill((255, 255, 255))
    win.blit(background,(0, 0))
    all_sprites.draw(win)
    enemy_sprites.draw(win)


    all_sprites.update()
    enemy_sprites.update()



    pygame.display.update()
    clock.tick(FPS)