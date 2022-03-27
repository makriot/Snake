import pygame
import snake_objects
import random

FPS = 60
DARK_MAGENTA = (139,0,139)
BLACK = (0,0,0)
THISTLE = (216,191,216)
DARK_RED = (139,0,0)
W = 600
H = 600
size = 12
x,y = size, size + size*(((H-2*size)//2)//size)
control = 24
step = 3
step_x = 0
step_y = 0
flag_x = 0
flag_y = 0
flag_x_1,flag_y_1 = 0,0
ate = True
stop = False
stop_move = False

pygame.init()

sc = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
Snake = snake_objects.Snake(sc, DARK_MAGENTA, size, [x,y], control, step)

def food_position(x,y):
    global W,H,size,Snake
    x_1 = control * random.randrange(1, W // control) + size
    y_1 = control * random.randrange(1, H // control) + size
    while [x_1,y_1] in Snake.all_positions:
        x_1 = control * random.randrange(1, W // control) + size
        y_1 = control * random.randrange(1, H // control) + size
    return [x_1,y_1]

for i in range(0,Snake.k*3):
    if not i%Snake.k:
        Snake.move(step, 0, flag=True)
    else:
        Snake.move(step, 0, flag=False)

while True:

    sc.fill(THISTLE)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_DOWN:
                if not (flag_x_1 == 0 and flag_y_1 == -1):
                    flag_x = 0
                    flag_y = 1
            elif i.key == pygame.K_UP:
                if not (flag_x_1 == 0 and flag_y_1 == 1):
                    flag_x = 0
                    flag_y = -1
            elif i.key == pygame.K_LEFT:
                if not (flag_x_1 == 1 and flag_y_1 == 0):
                    flag_x = -1
                    flag_y = 0
            elif i.key == pygame.K_RIGHT:
                if not (flag_x_1 == -1 and flag_y_1 == 0):
                    flag_x = 1
                    flag_y = 0
            elif i.key == pygame.K_ESCAPE:
                stop = True
            elif i.key == pygame.K_r:

                stop_move = False
                step_x,step_y,flag_x,flag_y = 0,0,0,0

                sc = pygame.display.set_mode((W, H))
                clock = pygame.time.Clock()
                Snake = snake_objects.Snake(sc, DARK_MAGENTA, size, [x, y], control, step)

                for j in range(0, Snake.k * 3):
                    if not j % Snake.k:
                        Snake.move(step, 0, flag=True)
                    else:
                        Snake.move(step, 0, flag=False)

    if (Snake.head_x-size)%control==0 and (Snake.head_y-size)%control==0:
        if flag_x or flag_y:
            step_x = step * flag_x
            step_y = step * flag_y
            flag_x_1,flag_y_1 = flag_x,flag_y
            flag_x,flag_y = 0,0
            stop_move = False
        if stop:
            stop_move = True
            stop = False
        if [Snake.head_x,Snake.head_y] in Snake.all_positions[1:-1]:
            stop_move = True
        if Snake.head_x > W-size or Snake.head_x < size or Snake.head_y < size or Snake.head_y > H-size:
            stop_move = True

    if ate:
        food = food_position(Snake.head_x,Snake.head_y)
        ate = False
    pygame.draw.polygon(sc, DARK_RED,
                        ((food[0] - size, food[1] - size), (food[0] + size, food[1] - size),
                         (food[0] + size, food[1] + size), (food[0] - size, food[1] + size)))
    if Snake.head_x == food[0] and Snake.head_y == food[1]:
        ate = True

    if (step_x or step_y) and not stop_move:
        Snake.move(step_x,step_y, flag=ate)
    Snake.draw()

    clock.tick(FPS)