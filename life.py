from graphics import *
import numpy as np
import sys, pygame
from cairo._cairo import Surface

def printAll(points):
        global surface
        surface.fill((0,0,0))
        for rec in points:
            pygame.draw.rect(surface, (255,0,0), rec, 0)
        pygame.display.update()
        points = []

            
#Takes in current neighbors and determines if it should live through this generation
def determineLife(x,y):
        if EXPANDED_NEIGHBORHOOD:
            neighbors = checkExNeighbors(x,y)
        else:
            neighbors = checkNeighbors(x,y)
        #if neighbors != 0 and neighbors != 1 and neighbors != 2 and neighbors != 3:
            #print("LIVING: ", neighbors)
        if neighbors == 2 or neighbors == 3:
                return 1
        else:
            return 0

def determineDLife(x,y):
        if EXPANDED_NEIGHBORHOOD:
            neighbors = checkExNeighbors(x,y)
        else:
            neighbors = checkNeighbors(x,y)
        #if neighbors != 0 and neighbors != 1 and neighbors != 2 and neighbors != 3:
            #print("DEAD: ", neighbors)
        if neighbors == 3:
                return 1
        else:
            return 0    
        
# Check neighbors and update temp grid
def checkExNeighbors(x,y):
        global normGrid
        global MAX_SIZE
        neighbors = int(0)
        if x != 0 and y != 0 and x != MAX_SIZE - 1 and y != MAX_SIZE - 1:
            if normGrid[x-1][y] == 1:
                    neighbors += 1
            if normGrid[x][y+1] == 1:
                    neighbors += 1
            if normGrid[x+1][y] == 1:
                    neighbors += 1
            if normGrid[x][y-1] == 1:
                    neighbors += 1
            if normGrid[x-1][y-1] == 1:
                    neighbors += 1
            if normGrid[x-1][y+1] == 1:
                    neighbors += 1
            if normGrid[x+1][y+1] == 1:
                    neighbors += 1
            if normGrid[x+1][y-1] == 1:
                    neighbors += 1
            return neighbors
        
                    
        if x == 0:
            if y == 0:
                if normGrid[MAX_SIZE - 1][0] == 1:
                    neighbors += 1
                if normGrid[0][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[0][1] == 1:
                    neighbors += 1
                if normGrid[1][0] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[1][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[1][1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][1] == 1:
                    neighbors += 1
            else:
                if y == MAX_SIZE - 1:
                    if normGrid[MAX_SIZE - 1][MAX_SIZE - 1] == 1:
                        neighbors += 1
                    if normGrid[0][MAX_SIZE - 2] == 1:
                        neighbors += 1
                    if normGrid[0][0] == 1:
                        neighbors += 1
                    if normGrid[1][MAX_SIZE - 1] == 1:
                        neighbors += 1
                    if normGrid[MAX_SIZE - 1][MAX_SIZE - 1] == 1:
                        neighbors += 1
                    if normGrid[0][MAX_SIZE - 1] == 1:
                        neighbors += 1
                    if normGrid[0][1] == 1:
                        neighbors += 1
                    if normGrid[1][1] == 1:
                        neighbors += 1
                else:
                    if normGrid[MAX_SIZE - 1][y] == 1:
                        neighbors += 1
                    if normGrid[0][y-1] == 1:
                        neighbors += 1
                    if normGrid[0][y+1] == 1:
                        neighbors += 1
                    if normGrid[1][y] == 1:
                        neighbors += 1
                    if normGrid[MAX_SIZE - 1][y] == 1:
                        neighbors += 1
                    if normGrid[0][y] == 1:
                        neighbors += 1
                    if normGrid[0][y+1] == 1:
                        neighbors += 1
                    if normGrid[1][y+1] == 1:
                        neighbors += 1
            return neighbors
                    
        if y == 0:
            if x == MAX_SIZE - 1:
                if normGrid[MAX_SIZE - 2][0] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][1] == 1:
                    neighbors += 1
                if normGrid[0][0] == 1:
                    neighbors += 1
                if normGrid[0][1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 2][1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 2][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[0][MAX_SIZE - 1] == 1:
                    neighbors += 1
            else:
                if normGrid[x-1][0] == 1:
                    neighbors += 1
                if normGrid[x][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[x][1] == 1:
                    neighbors += 1
                if normGrid[x+1][0] == 1:
                    neighbors += 1
                if normGrid[x+1][1] == 1:
                    neighbors += 1
                if normGrid[x-1][1] == 1:
                    neighbors += 1
                if normGrid[x-1][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[x+1][MAX_SIZE - 1] == 1:
                    neighbors += 1
            return neighbors
                    
        if x == MAX_SIZE - 1:
            if y == MAX_SIZE - 1:
                if normGrid[MAX_SIZE - 2][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][MAX_SIZE - 2] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][0] == 1:
                    neighbors += 1
                if normGrid[0][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 2][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][1] == 1:
                    neighbors += 1
                if normGrid[0][1] == 1:
                    neighbors += 1
            else:
                if normGrid[MAX_SIZE - 2][y] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][y-1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][y+1] == 1:
                    neighbors += 1
                if normGrid[0][y] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 2][y] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][y] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][y+1] == 1:
                    neighbors += 1
                if normGrid[0][y+1] == 1:
                    neighbors += 1
            return neighbors
                    
        if y == MAX_SIZE - 1:
            if normGrid[x-1][MAX_SIZE - 1] == 1:
                neighbors += 1
            if normGrid[x][MAX_SIZE - 2] == 1:
                neighbors += 1
            if normGrid[x][0] == 1:
                neighbors += 1
            if normGrid[x+1][MAX_SIZE - 1] == 1:
                neighbors += 1
            if normGrid[x-1][MAX_SIZE - 1] == 1:
                neighbors += 1
            if normGrid[x][MAX_SIZE - 1] == 1:
                neighbors += 1
            if normGrid[x][1] == 1:
                neighbors += 1
            if normGrid[x+1][1] == 1:
                neighbors += 1
            return neighbors
            
        return neighbors
    
def checkNeighbors(x,y):
        global normGrid
        global MAX_SIZE
        neighbors = int(0)
        if x != 0 and y != 0 and x != MAX_SIZE - 1 and y != MAX_SIZE - 1:
            if normGrid[x-1][y] == 1:
                    neighbors += 1
            if normGrid[x][y+1] == 1:
                    neighbors += 1
            if normGrid[x+1][y] == 1:
                    neighbors += 1
            if normGrid[x][y-1] == 1:
                    neighbors += 1
            return neighbors
        
                    
        if x == 0:
            if y == 0:
                if normGrid[MAX_SIZE - 1][0] == 1:
                    neighbors += 1
                if normGrid[0][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[0][1] == 1:
                    neighbors += 1
                if normGrid[1][0] == 1:
                    neighbors += 1
            else:
                if y == MAX_SIZE - 1:
                    if normGrid[MAX_SIZE - 1][MAX_SIZE - 1] == 1:
                        neighbors += 1
                    if normGrid[0][MAX_SIZE - 2] == 1:
                        neighbors += 1
                    if normGrid[0][0] == 1:
                        neighbors += 1
                    if normGrid[1][MAX_SIZE - 1] == 1:
                        neighbors += 1
                else:
                    if normGrid[MAX_SIZE - 1][y] == 1:
                        neighbors += 1
                    if normGrid[0][y-1] == 1:
                        neighbors += 1
                    if normGrid[0][y+1] == 1:
                        neighbors += 1
                    if normGrid[1][y] == 1:
                        neighbors += 1
            return neighbors
                    
        if y == 0:
            if x == MAX_SIZE - 1:
                if normGrid[MAX_SIZE - 2][0] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][1] == 1:
                    neighbors += 1
                if normGrid[0][0] == 1:
                    neighbors += 1
            else:
                if normGrid[x-1][0] == 1:
                    neighbors += 1
                if normGrid[x][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[x][1] == 1:
                    neighbors += 1
                if normGrid[x+1][0] == 1:
                    neighbors += 1
            return neighbors
                    
        if x == MAX_SIZE - 1:
            if y == MAX_SIZE - 1:
                if normGrid[MAX_SIZE - 2][MAX_SIZE - 1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][MAX_SIZE - 2] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][0] == 1:
                    neighbors += 1
                if normGrid[0][MAX_SIZE - 1] == 1:
                    neighbors += 1
            else:
                if normGrid[MAX_SIZE - 2][y] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][y-1] == 1:
                    neighbors += 1
                if normGrid[MAX_SIZE - 1][y+1] == 1:
                    neighbors += 1
                if normGrid[0][y] == 1:
                    neighbors += 1
            return neighbors
                    
        if y == MAX_SIZE - 1:
            if normGrid[x-1][MAX_SIZE - 1] == 1:
                neighbors += 1
            if normGrid[x][MAX_SIZE - 2] == 1:
                neighbors += 1
            if normGrid[x][0] == 1:
                neighbors += 1
            if normGrid[x+1][MAX_SIZE - 1] == 1:
                neighbors += 1
            return neighbors
        

def tempLiving():
    global normGrid
    global points
    points = []
    constant = RESOLUTION / MAX_SIZE
    tempLiving = [[0 for i in range(MAX_SIZE)] for i in range(MAX_SIZE)]
    for x in range(MAX_SIZE):
            for y in range(MAX_SIZE):
                    if normGrid[x][y] == 0:
                            tempLiving[x][y] = determineDLife(x,y)
                            if tempLiving[x][y] == 1:
                                points.append(pygame.Rect(constant*x,constant*y,constant*2,constant*2))
                    if normGrid[x][y] == 1:
                            tempLiving[x][y] = determineLife(x,y)
                            if tempLiving[x][y] == 1:
                                points.append(pygame.Rect(constant*x,constant*y,constant*2,constant*2))
    return (tempLiving, points)

# One tick of the game, call to start game
def tick():
    global normGrid
    ret = tempLiving()
    normGrid = ret[0]
    printAll(ret[1])

def main():
    pygame.init()
    global surface 
    global normGrid
    points = []
    
    # initial grid
    for x in range (0,MAX_SIZE):
            for y in range (0,MAX_SIZE):
                    if normGrid[x][y] != 1:
                        normGrid[x][y] == 0
    genNum = 0
    while genNum < 200:
        if genNum%10 == 0:
            print("Generation ", genNum)
        tick()
        genNum += 1

MAX_SIZE                = 100
RESOLUTION              = 400
FILL_PERCENTAGE         = 20
EXPANDED_NEIGHBORHOOD   = True
surface = pygame.display.set_mode((RESOLUTION, RESOLUTION), 0, 0)
normGrid = [[np.random.randint(100/FILL_PERCENTAGE) for i in range(MAX_SIZE)] for i in range(MAX_SIZE)]
main()