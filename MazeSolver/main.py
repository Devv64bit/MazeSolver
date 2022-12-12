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
drawMode = (242, 103, 17)


WINDOW_HEIGHT = 800
WINDOW_WIDTH = 720
WIDTH = 50
HEIGHT = 50
MARGIN = 5
ROWS = WINDOW_WIDTH // WIDTH
COLS = WINDOW_HEIGHT // HEIGHT
START_POS, GOAL_POS = None, None


pygame.display.set_caption("Maze Runners")


def load_Grid():
    with open("MazeSolver\patterns\default.txt", "r") as file:
        grid = file.read()
    START_POS, GOAL_POS = None, None
    grid = [list(row) for row in grid.split("\n")]

    # Converting grid to required format
    for r in range(12):
        for c in range(13):
            if grid[r][c] == "S":
                START_POS = r, c
            if grid[r][c] == "G":
                GOAL_POS = r, c
            grid[r][c] = grid[r][c].replace(" ", "EMPTY").replace(
                "G", "GOAL").replace("#", "WALL").replace("S", "START")
    return (grid)


def remove_path(grid):
    for r in range(12):
        for c in range(13):
            if grid[r][c] == "PATH":
                grid[r][c] = "EMPTY"


def clear_Grid(grid):
    for r in range(12):
        for c in range(13):
            grid[r][c] = "EMPTY"


def save_Grid(grid):
    saveGrid = grid
    remove_path(saveGrid)
    for r in range(12):
        for c in range(13):
            if saveGrid[r][c] == "S":
                START_POS = r, c
            if saveGrid[r][c] == "G":
                GOAL_POS = r, c
            saveGrid[r][c] = saveGrid[r][c].replace("EMPTY", " ").replace(
                "GOAL", "G").replace("WALL", "#").replace("START", "S")
    file = open("MazeSolver\patterns\save.txt", "w")

    for r in range(12):
        if r > 0:
            file.write("\n")
        for c in range(13):
            file.write(saveGrid[r][c])


def load_Saved_Grid():
    with open("MazeSolver\patterns\save.txt", "r") as file:
        loadGrid = file.read()
        START_POS, GOAL_POS = None, None
        loadGrid = [list(row) for row in loadGrid.split("\n")]

    # Converting grid to required format
    for r in range(12):
        for c in range(13):
            if loadGrid[r][c] == "S":
                START_POS = r, c
            if loadGrid[r][c] == "G":
                GOAL_POS = r, c
            loadGrid[r][c] = loadGrid[r][c].replace(" ", "EMPTY").replace(
                "G", "GOAL").replace("#", "WALL").replace("S", "START")
    return (loadGrid)


def main():
    grid = load_Grid()
    global screen
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
                        text = font.render('NONE', True, drawMode, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break

                    if globIndex == 0:
                        text = font.render('NONE', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)

                        text = font.render('WALL', True, drawMode, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break

                    if globIndex == 1:
                        text = font.render('WALL', True,  black, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)

                        text = font.render('EMPTY', True, drawMode, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break

                    if globIndex == 2:
                        text = font.render('EMPTY', True,  black, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)

                        text = font.render('START', True, drawMode, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break

                    if globIndex == 3:
                        text = font.render('START', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)

                        text = font.render('GOAL', True, drawMode, black)
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)
                        screen.blit(text, textRect)
                        break
                        globIndex = -1

                if event.key == pygame.K_c:
                    print("cleared the Grid")
                    clear_Grid(grid)
                if event.key == pygame.K_RETURN:
                    remove_path(grid)
                    #path = DFS(grid, START_POS, GOAL_POS)
                    path = A_star(grid, START_POS, GOAL_POS)
                    if path is not None:
                        for pos in path:
                            grid[pos[0]][pos[1]] = "PATH"

                if event.key == pygame.K_s:
                    print("saved grid")
                    save_Grid(grid)
                    grid = load_Saved_Grid()
                if event.key == pygame.K_l:
                    print("loaded grid")
                    grid = load_Saved_Grid()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                if pos[1] < 659:
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                    if globIndex == 0:
                        grid[row][column] = "WALL"
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    elif globIndex == 1:
                        grid[row][column] = "EMPTY"
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    elif globIndex == 2:
                        for r in range(12):
                            for c in range(13):
                                if grid[r][c] == "START":
                                    grid[r][c] = "EMPTY"
                                    grid[row][column] = "START"
                                else:
                                    grid[row][column] = "START"
                                    START_POS = row, column
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    elif globIndex == 3:
                        for r in range(12):
                            for c in range(13):
                                if grid[r][c] == "GOAL":
                                    grid[r][c] = "EMPTY"
                                    grid[row][column] = "GOAL"
                                else:
                                    grid[row][column] = "GOAL"
                                    GOAL_POS = row, column
                        print("Click ", pos, "Grid coordinates: ", row, column)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for row in range(12):
            for column in range(13):
                if grid[row][column] == "EMPTY":
                    color = white
                elif grid[row][column] == "WALL":
                    color = gray
                elif grid[row][column] == "START":
                    color = green
                    START_POS = row, column
                elif grid[row][column] == "GOAL":
                    color = red
                    GOAL_POS = row, column
                elif grid[row][column] == "PATH":
                    color = blue

                pygame.draw.rect(screen, color, [
                                 (MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

        font = pygame.font.Font('freesansbold.ttf', 22)
        draw = font.render('Draw Mode:', True, white, black)
        controls = font.render('Controls:', True, white, black)
        pressQ = font.render('Press Q To Change Draw Mode', True, white, black)
        clear = font.render('Press C To Clear Maze', True, white, black)
        pressEnter = font.render(
            'Press Enter To Solve Maze', True, white, black)
        save = font.render('Press S To Save Maze', True, white, black)
        load = font.render('Press L To Load Maze', True, white, black)

        contRect = controls.get_rect()
        pressQRect = pressQ.get_rect()
        clearRect = clear.get_rect()
        pressEnterRect = pressEnter.get_rect()
        drawRect = draw.get_rect()
        SaveRect = save.get_rect()
        LoadRect = load.get_rect()

        contRect.center = ((WINDOW_HEIGHT // 2) + 100,
                           (WINDOW_WIDTH // 2) + 320)
        pressQRect.center = ((WINDOW_HEIGHT // 2) + 100,
                             (WINDOW_WIDTH // 2) + 350)
        clearRect.center = ((WINDOW_HEIGHT // 2) + 100,
                            (WINDOW_WIDTH // 2) + 380)
        pressEnterRect.center = (
            (WINDOW_HEIGHT // 2) + 100, (WINDOW_WIDTH // 2) + 410)
        drawRect.center = ((WINDOW_HEIGHT // 2) - 270,
                           (WINDOW_WIDTH // 2) + 320)
        SaveRect.center = ((WINDOW_HEIGHT // 2) - 270,
                           (WINDOW_WIDTH // 2) + 350)
        LoadRect.center = ((WINDOW_HEIGHT // 2) - 270,
                           (WINDOW_WIDTH // 2) + 380)

        screen.blit(draw, drawRect)
        screen.blit(save, SaveRect)
        screen.blit(load, LoadRect)
        screen.blit(controls, contRect)
        screen.blit(pressQ, pressQRect)
        screen.blit(clear, clearRect)
        screen.blit(pressEnter, pressEnterRect)

        pygame.display.flip()


load_Grid()
main()
