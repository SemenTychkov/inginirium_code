import pygame

black = (0, ) * 3
gray = (100, ) * 3
white  = (255, ) * 3
red  = (255, 0, 0 )
yellow = (255, 255, 0)
lightgreen  = (0, 200, 200)

cross = '#046582'
circle = '#e4bad4'

pygame.init()
W,H = 600, 600
screen = pygame.display.set_mode((W, H))
class Board:
    def __init__(self, W, H,size):

        self.W, self.H = W , H
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.move = 1

    def click(self, mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move

    def render(self, screen):
        pygame.draw.line(screen, gray, (0,200), (self.W, 200))
        pygame.draw.line(screen, gray, (0, 400), (self.W, 400))
        pygame.draw.line(screen, gray, (200, 0), (200, self.H))
        pygame.draw.line(screen, gray, (400, 0), (400, self.H))
        for y in range(3):
            for x in range (3):
                if self.board[y][x] == 1:
                    draw_cross(screen, x, y, self.size)
                elif self.board[y][x] == -1:
                    draw_circle(screen, x, y, self.size)
def draw_circle(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pygame.draw.circle(sc, circle, (x, y), (size - 3) // 2, 3)
def draw_cross(sc, x, y, size):
    x = x * size + 3
    y = y * size + 3
    pygame.draw.line(sc, cross, (x, y), (x + size - 3, y + size - 3), 3)
    pygame.draw.line(sc, cross, (x + size - 3, y - 3),(x, y + size - 3), 3)

board = Board(W, H, 200)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(event.pos)

    screen.fill(white)
    board.render(screen)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()