#Project Title: Python Tic Tac Toe

#pip install pygame on cmd


#importing libraries
import pygame
from pygame.locals import *
pygame.init()

#setup game window
width = 300 #300 pixels
height = 300 #300 pixels
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TicTacToe')


#define variables
line_width = 6
markers=[]

#drawing game grid
def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x * 100), (width, x*100), line_width) #horizontal lines
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, height), line_width)  #vertical lines

#list to store game data
for x in range(3):
    row = [0] * 3
    markers.append(row)

print(markers)

#create a game loop with exit option
run = True #run is always true
while run:

    draw_grid()

    #add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()
#quit pygame
pygame.quit()
