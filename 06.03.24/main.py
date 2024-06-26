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

    def check_end(self):
        is_end_info = is_end(self.board)
        shift = self.W // 10
        if is_end_info is not None:
            type_end = is_end_info[0]
            number = is_end_info[1]
            if type_end == 'col':
                x0, y0 = (number + .5) * self.size, shift
                x1, y1 = (number + .5) * self.size, self.size * 3 - shift
            elif type_end == 'line':
                x0, y0 = shift ,(number + .5) * self.size
                x1, y1 = 3 * self.size - shift, (number + .5) * self.size

            elif type_end == 'diag':
                if number == 1:
                    x0, y0 = shift, shift
                    x1, y1 = 3 * self.size - shift, 3 * self.size - shift
                else:
                    x0, y0 = 3 * self.size - shift, shift
                    x1, y1 = shift, 3 * self.size - shift
            pygame.draw.line(screen, red, (x0, y0), (x1, y1), 10)
            pygame.display.update()
            pygame.time.delay(3000)
            return  True
        else:
            return  False

def draw_circle(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pygame.draw.circle(sc, circle, (x, y), (size - 3) // 2, 3)
def draw_cross(sc, x, y, size):
    x = x * size + 3
    y = y * size + 3
    pygame.draw.line(sc, cross, (x, y), (x + size - 3, y + size - 3), 3)
    pygame.draw.line(sc, cross, (x + size - 3, y - 3),(x, y + size - 3), 3)
def is_end(board):
    for i in range(3):
        if check_i_col(board, i):
            return 'col', i
        if check_i_line(board, i):
            return 'line', i
    if check_main_diag(board):
        return'diag', 1
    if check_secondary_diag(board):
        return'diag', 2
    return  None

def check_i_line(x, i):
    if x[i][0] == x[i][1] == x[i][2] != 0:
        return True
    else:
        return False

def check_i_col(x, i):
    if x[0][i] == x[1][i] == x[2][i] != 0:
        return True
    else:
        return False

def check_main_diag(x):
    if x[0][0] == x[1][1] == x[2][2] != 0:
        return True
    else:
        return False

def check_secondary_diag(x):
    if x[0][2] == x[1][1] == x[2][0] != 0:
        return True
    else:
        return False





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
    if keys[pygame.K_ESCAPE] or board.check_end():
        pygame.quit()
        exit()