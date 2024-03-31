import random

import pygame

pygame.init()

width, height = 500, 500

win = pygame.display.set_mode((width, height))


class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('ing.png')
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect()
        self.health = 10

    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        global background_x,background_x2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 5
        elif keys[pygame.K_DOWN]:
            self.rect.top += 5
        elif keys[pygame.K_LEFT]:
            self.rect.left -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.left += 5



class Enemy(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('b.webp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.right = width
        self.health = 10

    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.top -= 5
        elif keys[pygame.K_s]:
            self.rect.top += 5
        elif keys[pygame.K_a]:
            self.rect.left -= 5
        elif keys[pygame.K_d]:
            self.rect.left += 5


all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

enemy_sprites = pygame.sprite.Group()
enemy = Enemy(enemy_sprites)

FPS = 60
clock = pygame.time.Clock()

background_image = pygame.image.load('fon.png')
background_image = pygame.transform.scale(background_image,(width,height))

background_x =0

background_image2 = pygame.image.load('fon.png')
background_image2 = pygame.transform.scale(background_image,(width,height))

background_x2 =width
background_speed =4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    background_x -= 4
    background_x2 -= 4


    win.blit(background_image,(background_x,0))
    win.blit(background_image2, (background_x2, 0))
    if background_x2==0:
        background_x= width
    if background_x==0:
        background_x2=width

    all_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.draw(win)
    enemy_sprites.update()
    hits = pygame.sprite.spritecollide(player,enemy_sprites,False)
    if len(hits) > 0:
        hits[0].health -=1
        hits[0].rect.left = random.randint(0,width - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, height - hits[0].rect.height)
        if hits[0].health <= 0:
            enemy_sprites.remove(hits[0])
        print(hits[0].health)




    pygame.display.update()
    clock.tick(FPS)
