import pygame
import sys
from helper import *

black = (0, 0, 0)
white = (200, 200, 200)  # EMPTY
gray = (90, 90, 90)
green = (13, 223, 6)
red = (255, 0, 0)
blue = (0, 128, 255)
path = (220, 253, 113)  # PATH

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 720
WIDTH = 50
HEIGHT = 50
MARGIN = 5
ROWS = WINDOW_WIDTH // WIDTH
COLS = WINDOW_HEIGHT // HEIGHT
START_POS, STOP_POS = None, None

SEARCH_MODES = [
    ("DFS", DFS_random),
    ("A*", A_star)
]
CUR_SEARCH_MODE_INDEX = 0
CUR_SEARCH_MODE_FUNCTION = SEARCH_MODES[CUR_SEARCH_MODE_INDEX][1]

pygame.display.set_caption("Maze Runners")
grid = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


'''
creates empty grid
for row in range(12):
    grid.append([])
    for column in range(13):
        grid[row].append(0)




defaultMazeFile = open("./MazeSolver/patterns/default.txt", "r")
for line in defaultMazeFile:
    line = line.rstrip('\n').split(' ')
    grid.append(line)
'''


def draw_grid(grid):
    color_table = {
        "WALL": (80, 80, 80),
        "EMPTY": (237, 240, 252),
        "GOAL": (0, 171, 28),
        "START": (255, 0, 0),
        "PATH": (220, 235, 113)
    }

    x, y = 0, 0
    for i in range(ROWS):
        for j in range(COLS):
            cell = pygame.Rect(x + WIDTH*j, y + HEIGHT*i, WIDTH, HEIGHT)
            cell_color = color_table.get(grid[i][j], color_table["EMPTY"])
            draw_rect_with_border(screen, cell_color, cell, 1, (0, 0, 0))


def remove_path(grid):
    for i in range(COLS):
        for j in range(ROWS):
            if grid[i][j] == "PATH":
                grid[i][j] == "EMPTY"


def main():
    global screen, CLOCK

    globIndex = -1
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(black)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                font = pygame.font.Font('freesansbold.ttf', 22)
                if event.key == pygame.K_q:
                    print(globIndex)

                    if globIndex < 3:
                        globIndex += 1

                    elif globIndex == 3:
                        globIndex = -1

                    if globIndex == -1:
                        text = font.render('NONE', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break

                    if globIndex == 0:
                        text = font.render('NONE', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)

                        text = font.render('WALL', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break

                    if globIndex == 1:
                        text = font.render('WALL', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)

                        text = font.render('EMPTY', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break

                    if globIndex == 2:
                        text = font.render('EMPTY', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)

                        text = font.render('START', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break

                    if globIndex == 3:
                        text = font.render('START', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)

                        text = font.render('GOAL', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-200, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break
                        globIndex = -1

                if event.key == pygame.K_c:
                    print("cleared the array")
                    for r in range(12):
                        for c in range(13):
                            grid[r][c] = 0

                if event.key == pygame.K_RETURN:
                   # DFS_random(grid, START_POS, STOP_POS)
                    path = CUR_SEARCH_MODE_FUNCTION(grid, START_POS, STOP_POS)
                    print(path)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
                if globIndex == 0:
                    grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
                elif globIndex == 1:
                    grid[row][column] = 0
                    print("Click ", pos, "Grid coordinates: ", row, column)
                elif globIndex == 2:
                    for r in range(12):
                        for c in range(13):
                            if grid[r][c] == 2:
                                grid[r][c] = 0
                            else:
                                grid[row][column] = 2
                                START_POS = grid[row][column]
                    print("Click ", pos, "Grid coordinates: ", row, column)
                elif globIndex == 3:
                    for r in range(12):
                        for c in range(13):
                            if grid[r][c] == 3:
                                grid[r][c] = 0
                            else:
                                grid[row][column] = 3
                                STOP_POS = grid[row][column]
                    print("Click ", pos, "Grid coordinates: ", row, column)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for row in range(12):
            for column in range(13):
                if grid[row][column] == 0:
                    color = white
                elif grid[row][column] == 1:
                    color = gray
                elif grid[row][column] == 2:
                    color = green
                    START_POS = grid[row][column]
                elif grid[row][column] == 3:
                    color = red
                    STOP_POS = grid[row][column]
                elif grid[row][column] == 4:
                    color = blue

                pygame.draw.rect(screen, color, [
                                 (MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
        font = pygame.font.Font('freesansbold.ttf', 22)
        draw = font.render('Draw Mode:', True, white, black)
        controls = font.render('Controls:', True, white, black)
        pressQ = font.render('Press Q to change draw mode', True, white, black)
        clear = font.render('Press C to clear Maze', True, white, black)
        contRect = controls.get_rect()
        pressQRect = pressQ.get_rect()
        clearRect = clear.get_rect()
        drawRect = draw.get_rect()

        contRect.center = ((WINDOW_HEIGHT // 2) + 100,
                           (WINDOW_WIDTH // 2) + 320)
        pressQRect.center = ((WINDOW_HEIGHT // 2) + 100,
                             (WINDOW_WIDTH // 2) + 350)
        clearRect.center = ((WINDOW_HEIGHT // 2) + 100,
                            (WINDOW_WIDTH // 2) + 380)
        drawRect.center = ((WINDOW_HEIGHT // 2) - 300,
                           (WINDOW_WIDTH // 2) + 320)

        screen.blit(draw, drawRect)
        screen.blit(controls, contRect)
        screen.blit(pressQ, pressQRect)
        screen.blit(clear, clearRect)

        pygame.display.flip()


main()
