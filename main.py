import pygame
import sys
from helper import *


black = (0, 0, 0) #RGB COLOR for black used for background
white = (200, 200, 200)  #RGB COLOR for white used in the empty square
gray = (90, 90, 90) #RGB COLOR for gray, used forr the wall square
green = (13, 223, 6)  #RGB COLOR for green used in the start square
red = (255, 0, 0)  #RGB COLOR for red, used in the goal square
blue = (0, 128, 255) #RGB COLOR for blue, used in the path squares
path = (220, 253, 113)
drawMode = (242, 103, 17) #RGB COLOR for orange, used in the draw mode in the menu


WINDOW_HEIGHT = 800  #sets the window height
WINDOW_WIDTH = 720  #sets window width
WIDTH = 50  #width of the squares being drawn on the screen
HEIGHT = 50 #height of the squares being drawn on the screen
MARGIN = 5 #sets the margin between the squares
ROWS = WINDOW_WIDTH // WIDTH
COLS = WINDOW_HEIGHT // HEIGHT
START_POS, GOAL_POS = None, None  #initializes the start and goal positions


pygame.display.set_caption("Maze Runners")   #sets the name of the window


def load_Grid():
    with open("default.txt", "r") as file:    #opens default text file
        grid = file.read()
    START_POS, GOAL_POS = None, None
    grid = [list(row) for row in grid.split("\n")] #puts each line into an array and splits it by the new lines

    # Converting grid to required format
    for r in range(12):     #goes through each position on the array
        for c in range(13):
            if grid[r][c] == "S":
                START_POS = r, c
            if grid[r][c] == "G":
                GOAL_POS = r, c
            grid[r][c] = grid[r][c].replace(" ", "EMPTY").replace(
                "G", "GOAL").replace("#", "WALL").replace("S", "START")        #converts the # to walls the spaces to empty, the G to goal and the S to start
    return (grid)


def remove_path(grid):
    for r in range(12): #goes though the entire array
        for c in range(13):
            if grid[r][c] == "PATH":   #checks if element is path and then sets it to an empty slot
                grid[r][c] = "EMPTY"


def clear_Grid(grid):
    for r in range(12):  #goes through the entire array
        for c in range(13):
            grid[r][c] = "EMPTY"  #sets every element to empty


def save_Grid(grid):
    saveGrid = grid
    remove_path(saveGrid) #removes path from the grid in the case that it's been solved
    for r in range(12): # goes through each element in the array
        for c in range(13):
            saveGrid[r][c] = saveGrid[r][c].replace("EMPTY", " ").replace(         
                "GOAL", "G").replace("WALL", "#").replace("START", "S")       #converts the walls to #, the empty to spaces, the goal to G and the start to S
    file = open("save.txt", "w") #opens the save file

    for r in range(12):   #goes through the entire grid arrray
        if r > 0:
            file.write("\n")  #adds a new line for each row
        for c in range(13):
            file.write(saveGrid[r][c])  #writes each row and column into the file


def load_Saved_Grid():
    with open("MazeSolver\patterns\save.txt", "r") as file:  #opens the save file
        loadGrid = file.read()   #reads the file
        START_POS, GOAL_POS = None, None
        loadGrid = [list(row) for row in loadGrid.split("\n")] #sets loadGrid array equal to the file and splits each row by the new line

    # Converting grid to required format
    for r in range(12):
        for c in range(13):
            if loadGrid[r][c] == "S":
                START_POS = r, c #sets start position
            if loadGrid[r][c] == "G":
                GOAL_POS = r, c   #sets goal position
            loadGrid[r][c] = loadGrid[r][c].replace(" ", "EMPTY").replace(
                "G", "GOAL").replace("#", "WALL").replace("S", "START")   #converts the # to walls the spaces to empty, the G to goal and the S to start
    return (loadGrid) #returns the grid


def main():
    grid = load_Grid()  #loads default grid
    global screen
    globIndex = -1

    pygame.init() #initalizes the pygame library
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #creates the GUI window
    screen.fill(black) #fills the background with black

    while 1:
        for event in pygame.event.get():  #checks for events while the program is running
            if event.type == pygame.KEYDOWN: #checks for keypresses
                font = pygame.font.Font('freesansbold.ttf', 22)
                if event.key == pygame.K_q:  #if Q is pressed to change draw mode
                    print(globIndex)

                    if globIndex < 3:
                        globIndex += 1

                    elif globIndex == 3:
                        globIndex = -1

                    if globIndex == -1:
                        text = font.render('NONE', True, drawMode, black)   #sets the parameters for the text on the screen
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320)   #gives the text a position to draw
                        screen.blit(text, textRect) #draws the text on the screen
                        break

                    if globIndex == 0:
                        text = font.render('NONE', True, black, black) #sets the parameters for the text on the screen
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320) #gives the text a position to draw
                        screen.blit(text, textRect) #draws the text on the screen

                        text = font.render('WALL', True, drawMode, black) #sets the parameters for the text on the screen
                        textRect = text.get_rect()
                        textRect.center = (
                            (WINDOW_HEIGHT // 2)-160, (WINDOW_WIDTH // 2) + 320) #gives the text a position to draw
                        screen.blit(text, textRect) #draws the text on the screen
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

                if event.key == pygame.K_c:  #clears the grid when C is pressed
                    print("cleared the Grid")
                    clear_Grid(grid) #calls cleargrid
                if event.key == pygame.K_RETURN: #sends all the grid info to the A* algorithm
                    remove_path(grid)
                    #path = DFS(grid, START_POS, GOAL_POS)
                    path = A_star(grid, START_POS, GOAL_POS) #sends the path and a* algorithm
                    if path is not None: #checks the path that the algorithm returns
                        for pos in path:
                            grid[pos[0]][pos[1]] = "PATH"  #sets the positions in the path to path so the GUI can display it

                if event.key == pygame.K_s:  #saves the grid when S is pressed
                    print("saved grid")
                    save_Grid(grid) #calls the save grid method
                    grid = load_Saved_Grid()

                if event.key == pygame.K_l: #loads saved grid when L is pressed
                    print("loaded grid")
                    grid = load_Saved_Grid() #calls the loadsavedgrid method

            if event.type == pygame.MOUSEBUTTONDOWN: #when clicked on the screen the GUI gets the position
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos() #gets the current x,y position of the mouse on the screen
                if pos[1] < 659: #checks if the mouse is out of the grid
                    column = pos[0] // (WIDTH + MARGIN)  #converts the mouse position to a position in the grid array
                    row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                    if globIndex == 0:    #checks which draw mode is selected
                        grid[row][column] = "WALL" #changes the space to wall in the grid array
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    elif globIndex == 1: #checks which draw mode is selected
                        grid[row][column] = "EMPTY"
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    elif globIndex == 2: #checks which draw mode is selected
                        for r in range(12): #checks if there is already a start position finds the previous one and changes it to an empty space
                            for c in range(13):
                                if grid[r][c] == "START": 
                                    grid[r][c] = "EMPTY"
                                    grid[row][column] = "START"
                                else:
                                    grid[row][column] = "START"
                                    START_POS = row, column
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    elif globIndex == 3: #checks if there is already a end position finds the previous one and changes it to an empty space
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

        for row in range(12):   #goes through the entire grid and draws it to the screen
            for column in range(13):
                if grid[row][column] == "EMPTY": #checks what each space is and then sets it to its respective color
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
                                 #fills the window with rectangles based on the color the were set to and the size of the window

        #All the code below draws the controls on the screen
        font = pygame.font.Font('freesansbold.ttf', 22)
        draw = font.render('Draw Mode:', True, white, black) #sets the wording, color and background color for the text
        controls = font.render('Controls:', True, white, black) 
        pressQ = font.render('Press Q To Change Draw Mode', True, white, black)
        clear = font.render('Press C To Clear Maze', True, white, black)
        pressEnter = font.render(
            'Press Enter To Solve Maze', True, white, black)
        save = font.render('Press S To Save Maze', True, white, black)
        load = font.render('Press L To Load Maze', True, white, black)

        contRect = controls.get_rect()  #grabs the size of the text and then uses it for the positioning
        pressQRect = pressQ.get_rect()
        clearRect = clear.get_rect()
        pressEnterRect = pressEnter.get_rect()
        drawRect = draw.get_rect()
        SaveRect = save.get_rect()
        LoadRect = load.get_rect()

        contRect.center = ((WINDOW_HEIGHT // 2) + 100, 
                           (WINDOW_WIDTH // 2) + 320) #gives the text its position and offset on the screen
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

        screen.blit(draw, drawRect)  #draws the text on the screen
        screen.blit(save, SaveRect)
        screen.blit(load, LoadRect)
        screen.blit(controls, contRect)
        screen.blit(pressQ, pressQRect)
        screen.blit(clear, clearRect)
        screen.blit(pressEnter, pressEnterRect)

        pygame.display.flip() #updates the window everytime this is called


main() #starts the program
