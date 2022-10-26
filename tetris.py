import pygame
import sys
import time
import random
pygame.init()
pygame.display.set_caption("Tetris")
x = 350
y = 400
point = 0
screen = pygame.display.set_mode((x, y))
t1 = time.time()
t = 0
speed = 0.2                         #speed of falling
stop = 0
field = []              #work field
s = 20                                 #size
figure_o = [
    [[0,0,s,s],[20,0,s,s],[0,20,s,s],[20,20,s,s]],     #1 rotation
    [[0,0,s,s],[20,0,s,s],[0,20,s,s],[20,20,s,s]],     #2 rotation
    [[0,0,s,s],[20,0,s,s],[0,20,s,s],[20,20,s,s]],     #3 rotation
    [[0,0,s,s],[20,0,s,s],[0,20,s,s],[20,20,s,s]]      #4 rotation
    ]

figure_L = [
    [[0,0,s,s],[0,20,s,s],[0,40,s,s],[20,40,s,s]],          #1 rotation
    [[0,0,s,s],[0,20,s,s],[20,0,s,s],[40,0,s,s]],           #2 rotation
    [[0,0,s,s],[20,0,s,s],[20,20,s,s],[20,40,s,s]],         #3 rotation
    [[0,20,s,s],[20,20,s,s],[40,20,s,s],[40,0,s,s]]         #4 rotation
    ]
figure_T = [
    [[0,0,s,s],[20,0,s,s],[40,0,s,s],[20,20,s,s]],          #1 rotation
    [[0,20,s,s],[20,0,s,s],[20,20,s,s],[20,40,s,s]],        #2 rotation
    [[20,0,s,s],[0,20,s,s],[20,20,s,s],[40,20,s,s]],        #3 rotation
    [[0,0,s,s],[0,20,s,s],[0,40,s,s],[20,20,s,s]]           #4 rotation
]
figure_I= [
    [[0,0,s,s],[0,20,s,s],[0,40,s,s],[0,60,s,s]],
    [[0,0,s,s],[20,0,s,s],[40,0,s,s],[60,0,s,s]],
    [[0,0,s,s],[0,20,s,s],[0,40,s,s],[0,60,s,s]],
    [[0,0,s,s],[20,0,s,s],[40,0,s,s],[60,0,s,s]]
]
figure_Q = [
    [[0,0,s,s],[0,20,s,s],[20,20,s,s],[20,40,s,s]],
    [[0,20,s,s],[20,0,s,s],[40,0,s,s],[20,20,s,s]],
    [[0, 0, s, s], [0, 20, s, s], [20, 20, s, s], [20, 40, s, s]],
    [[0, 20, s, s], [20, 0, s, s], [40, 0, s, s], [20, 20, s, s]]
]
fig = []      #working figure
rotation = 0      #figure rotation
def get_values(a,b):
    for i in range(len(b)):
        a.append([])
        for j in range(len(b[i])):
            a[i].append([])
            for k in range(len(b[i][j])):
                a[i][j].append(b[i][j][k])
    return a
fig = get_values(fig,figure_L)
def draw_figure():
    for i in fig[rotation]:
       pygame.draw.rect(screen, (255, 0, 0), i, 0)
    for j in field:
        pygame.draw.rect(screen, (255, 0, 0), j, 0)
def move_down_figure():
    for i in range(4):
        for j in fig[i]:
            j[1] += 20
def draw_lines():
    for i in range(20,220,20):
        pygame.draw.aaline(screen,(0,0,0),(i,0),(i,y))
    for i in range(20,400,20):
        pygame.draw.aaline(screen,(0,0,0),(0,i),(200,i))
def select_figure():
    a = random.randint(1,5)
    global fig
    fig = []
    if a == 1:
        fig = get_values(fig,figure_o)
    elif a == 2:
        fig = get_values(fig,figure_L)
    elif a == 3:
        fig = get_values(fig,figure_T)
    elif a == 4:
        fig = get_values(fig,figure_I)
    elif a == 5:
        fig = get_values(fig,figure_Q)
def colision():
    a = 0
    for i in range(len(fig)):
        if (fig[rotation][i][1]+20 >=y):
            a = 1
    for i in range(len(fig)):
        for j in field:
            if fig[rotation][i][1]+20 == j[1] and fig[rotation][i][0] == j[0]:
                a=1
    if a == 1:
        return True
    else:
        return False
def add_field():
    for i in range(len(fig[rotation])):
        field.insert(len(field),[])
        for j in range(len(fig[rotation][i])):
            field[len(field)-1].append(fig[rotation][i][j])
def r_colision():
    global rotation
    rotation1 = 0
    if rotation == 3:
        rotation1 = 0
    else:
        rotation1 = rotation+1
    a = 0
    for i in range(len(fig)):
        if (fig[rotation1][i][1] + 20 >= y or fig[rotation1][i][0] + 20>=200):
            a = 1
    for i in range(len(fig)):
        for j in field:
            if fig[rotation1][i][1] == j[1] and fig[rotation1][i][0] == j[0]:
                a = 1
    if a == 1:
        return False
    else:
        return True
def ri_colision():
    a = 0
    for i in range(len(fig)):
        if (fig[rotation][i][0] + 20 >= 200):
            a = 1
    for i in range(len(fig)):
        for j in field:
            if fig[rotation][i][0]+20 == j[0] and fig[rotation][i][1] == j[1]:
                a = 1
    if a == 1:
        return False
    else:
        return True
def le_colision():
    a = 0
    for i in range(len(fig)):
        if (fig[rotation][i][0]  <= 0):
            a = 1
    for i in range(len(fig)):
        for j in field:
            if fig[rotation][i][0] - 20 == j[0] and fig[rotation][i][1] == j[1]:
                a = 1
    if a == 1:
        return False
    else:
        return True
def top_colision():
    global stop
    for i in field:
        if 20 >= i[1]:
            stop = 1
            font = pygame.font.SysFont('couriernew', 20,bold=True)
            text1 = font.render(str('Game Over'), True, (255, 255, 255))
            screen.blit(text1, (205, 210))
def line_delete():
    global point
    k=0
    arr = []
    for i in range(0,400,20):
        for j in range(0,220,20):
            for x in range(len(field)):
                if field[x][0] == j and field[x][1]==i:
                    k+=1
        if k>=10:
            arr.append(i)
        k=0
    for i in arr:
        for j in range(0,220,20):
            if [j,i,s,s] in field:
                field.remove([j,i,s,s])
        point += 200
    arr = sorted(arr)
    for i in arr:
        for j in range(len(field)):
            if field[j][1] < i:
                field[j][1] +=20
def print_point():
    font = pygame.font.SysFont('couriernew', 16, bold=True)
    font1 = pygame.font.SysFont('couriernew', 12)
    text = font1.render(str('Made by:'), True, (255, 250, 200))
    text2 = font1.render(str('Yuriy Yarmola'), True, (255, 250, 200))
    text1 = font.render(str('Point: ' + str(point)), True, (0, 250, 200))
    screen.blit(text1, (205, 190))
    screen.blit(text, (205, 365))
    screen.blit(text2, (205, 380))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if r_colision():
                    if rotation == 3:
                        rotation = 0
                    else:
                        rotation += 1
            elif event.key == pygame.K_RIGHT:
                if ri_colision():
                    for i in range(len(fig)):
                        for j in range(len(fig[i])):
                            fig[i][j][0] += 20
            elif event.key == pygame.K_LEFT:
                if le_colision():
                    for i in range(len(fig)):
                        for j in range(len(fig[i])):
                            fig[i][j][0] -= 20
    if t1 - t >= speed and stop != 1:
        t = t1
        screen.fill((50, 50, 50))
        draw_figure()
        draw_lines()
        print_point()
        top_colision()
        if colision():
            add_field()
            line_delete()
            select_figure()

        else:
            move_down_figure()
    pygame.display.flip()
    t1 = time.time()


