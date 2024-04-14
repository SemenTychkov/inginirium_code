import random
import pygame
import sqlite3

con = sqlite3.connect('score.sqlite')
cur = con.cursor()

def create_database():
    que_create = '''
        CREATE TABLE IF NOT EXISTS score(
            id INTEGER PRIMARY KEY,
            name TEXT,
            score INTEGER
        )
    '''
    cur.execute(que_create)
    con.commit()

def insert_data(name,score):
    que_insert = '''
        INSERT INTO score (name, score) VALUES
        ('{}',{})
    '''
    cur.execute(que_insert.format(name,score))
    con.commit()
create_database()
pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width,height))

class Player(pygame.sprite.Sprite):
    def __init__(self,*group):
        super().__init__(*group)
        self.image = pygame.image.load('ing.png')
        self.image = pygame.transform.scale(self.image,(120,90))
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
    def __init__(self,*group):
        super().__init__(*group)
        self.image = pygame.image.load('b.webp')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.right=width

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

enemy_sprites = pygame.sprite.Group()
enemy = Enemy(enemy_sprites)
FPS = 60
clock = pygame.time.Clock()
score =0

font = pygame.font.Font(None,36)

name = input('ведите Ваше имя:')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            insert_data(name,score)
            exit()
    hits = pygame.sprite.spritecollide(player,enemy_sprites,False)
    if len(hits)> 0:
        score+=1
        hits[0].rect.left = random.randint(0,width - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, height - hits[0].rect.height)

    win .fill((255,255,255))
    text = font.render(str(score), True,(180,0,0))

    all_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.draw(win)
    enemy_sprites.update()
    win.blit(text, (0, 0))
    pygame.display.update()
    clock.tick(FPS)