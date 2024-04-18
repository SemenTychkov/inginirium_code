import random
import pygame
import sqlite3

con = sqlite3.connect('score.sqlite')
cur = con.cursor()
def create_database():
    que_create = '''
            CREATE TABLE IF NOT EXISTS score (
                id INTEGER PRIMARY KEY,
                name TEXT,
                score INTEGER 
            )
        
    '''
    cur.execute(que_create)
    con.commit()

def insert_data(name, score):
    que_insert = '''
        INSERT INTO score (name, score) VALUES
        ('{}', {})
    '''
    cur.execute(que_insert.format(name,score))
    con.commit()
create_database()

pygame.init()


widht , height = 500,500

win = pygame.display.set_mode((widht,height))

class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('ing.png')
        self.image = pygame.transform.scale(self.image, (120,80))
        self.rect = self.image.get_rect()
        self.health = 10
    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_UP]:
            self.rect.top -= 5
        elif keys[pygame.K_DOWN]:
            self.rect.top += 5
        elif keys [pygame.K_LEFT]:
            self.rect.left -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.left += 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('b.webp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.right = widht
        self.health = 10

    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w]:
            self.rect.top -= 5
        elif keys[pygame.K_s]:
            self.rect.top += 5
        elif keys [pygame.K_a]:
            self.rect.top -= 5
        elif keys[pygame.K_d]:
            self.rect.top += 5

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)


enemy_sprites = pygame.sprite.Group()
enemy = Enemy(enemy_sprites)

FPS = 60
clock = pygame.time.Clock()

score = 0
f1 = pygame.font.Font(None, 36)
text = f1.render(str(score), True,
                 (0, 0, 0))
name = input('введите имя: ')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            insert_data(name, score)
            exit()
    win.fill((255,255,255))
    win.blit(text, (0,0))
    all_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.draw(win)
    enemy_sprites.update()
    hits = pygame.sprite.spritecollide(player, enemy_sprites, False)
    if len(hits) > 0:
        hits[0].rect.left = random.randint(0, widht - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, height - hits[0].rect.height)
        score += 1
        text = f1.render(str(score), True,(0, 0, 0))

    pygame.display.update()

    clock.tick(FPS)







