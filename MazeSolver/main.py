import pygame
import sys
import random

black = (0, 0, 0)
white = (200, 200, 200)
gray = 	(90, 90, 90)
green = (13, 223, 6)
red = (255, 0, 0)
WINDOW_HEIGHT = 1200
WINDOW_WIDTH = 1286
WIDTH = 75
HEIGHT = 75
MARGIN = 5
modes = {"WALL","EMPTY","END","START"}
grid = []
for row in range(12):
    grid.append([])
    for column in range(16):
        grid[row].append(0)


pygame.display.set_caption("Maze Runners")

def main():
    global screen, CLOCK
    globIndex = -1
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(black)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                font = pygame.font.Font('freesansbold.ttf', 32)
                if event.key == pygame.K_q:
                    print(globIndex)
                    if globIndex < 3:
                        globIndex += 1
                    elif globIndex == 3:
                        globIndex = -1
                    if globIndex == -1:
                        text = font.render('NONE', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)
                        break
                    if globIndex == 0:
                        text = font.render('NONE', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)

                        text = font.render('WALL', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)
                        break
                    if globIndex == 1:
                        text = font.render('WALL', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)
                        
                        text = font.render('EMPTY', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)
                        break
                    if globIndex == 2:
                        text = font.render('EMPTY', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)

                        text = font.render('START', True, white, black)
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)
                        break
                    if globIndex == 3:
                        text = font.render('START', True, black, black)
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)
                        
                        text = font.render('END', True, white, black) 
                        textRect = text.get_rect()
                        textRect.center = ((WINDOW_HEIGHT // 2)+150, (WINDOW_WIDTH // 2) +400)
                        screen.blit(text, textRect)
                        break
                        globIndex = -1
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
                    grid[row][column] = 2
                    print("Click ", pos, "Grid coordinates: ", row, column)
                elif globIndex == 3:
                    grid[row][column] = 3
                    print("Click ", pos, "Grid coordinates: ", row, column)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for row in range(12):
            for column in range(16):
                if grid[row][column] == 0:
                    color = white
                elif grid[row][column] == 1:
                    color = gray
                elif grid[row][column] == 2:
                    color = green
                elif grid[row][column] == 3:
                    color = red
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Draw Mode:', True, white, black)
        textRect = text.get_rect()
        textRect.center = ((WINDOW_HEIGHT // 2), (WINDOW_WIDTH // 2) +400)
        screen.blit(text, textRect)
        '''
        for row in range(12):
            for col in range(16):
                print(grid[row][col])
        '''

        pygame.display.flip()
   

    

main()