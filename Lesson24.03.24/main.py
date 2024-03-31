import pygame

pygame.init()

width, height = 500,500

win = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('ing.png')
        self.image = pygame.transform.scale(self.image,(120,80))
        self.rect = self.image.get_rect()

    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
             self.rect.top -=5
        elif keys[pygame.K_DOWN]:
             self.rect.top +=5
        elif keys[pygame.K_LEFT]:
            self.rect.left -=5
        elif keys[pygame.K_RIGHT]:
            self.rect.left +=5

class Enemy(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('b.webp')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.right=width

    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
             self.rect.top -=5
        elif keys[pygame.K_s]:
             self.rect.top +=5
        elif keys[pygame.K_a]:
            self.rect.left -=5
        elif keys[pygame.K_d]:
            self.rect.left +=5


enemy_sprites = pygame.sprite.Group()
enemy= Enemy(enemy_sprites)
all_sprites= pygame.sprite.Group()
player=Player(all_sprites)
FPS= 60
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit()
    win.fill((255,255,255))
    all_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.draw(win)
    enemy_sprites.update()

    if player.rect.left<enemy.rect.right and \
             player.rect.top< enemy.rect.bottom and\
             player.rect.bottom< enemy.rect.top and\
             player.rect.right< enemy.rect.left:
                 print('столкновение')

    hits = pygame.sprite.spritecollide(player,enemy_sprites,False)
    if len(hits) > 0:
        print('столкнавение')

    pygame.display.update()
    clock.tick(FPS)