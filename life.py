from graphics import *
import numpy as np
import sys, pygame
from cairo._cairo import Surface

def printAll():
        global points
        global normGrid
        global surface
        points = []
        for x in range (0,100):
                for y in range (0,100):
                        if normGrid[x][y] == 1:
                            points.append(pygame.Rect(4*x,4*y,4*2,4*2))
        surface.fill((0,0,0))
        for rec in points:
            pygame.draw.rect(surface, (255,0,0), rec, 0)
        pygame.display.update()

            
#Takes in current neighbors and determines if it should live through this generation
def determineLife(x,y):
        neighbors = checkNeighbors(x,y)
        #if neighbors != 0 and neighbors != 1 and neighbors != 2 and neighbors != 3:
            #print("LIVING: ", neighbors)
        if neighbors == 2 or neighbors == 3:
                return 1
        else:
            return 0

def determineDLife(x,y):
        neighbors = checkNeighbors(x,y)
        #if neighbors != 0 and neighbors != 1 and neighbors != 2 and neighbors != 3:
            #print("DEAD: ", neighbors)
        if neighbors == 3:
                return 1
        else:
            return 0    
        
# Check neighbors and update temp grid
def checkNeighbors(x,y):
        global normGrid
        neighbors = int(0)
        # print("x: %d  y: %d", x, y)
        if x != 0 and y != 0 and x != 99 and y != 99:
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
                if normGrid[99][0] == 1:
                    neighbors += 1
                if normGrid[0][99] == 1:
                    neighbors += 1
                if normGrid[0][1] == 1:
                    neighbors += 1
                if normGrid[1][0] == 1:
                    neighbors += 1
                if normGrid[99][99] == 1:
                    neighbors += 1
                if normGrid[1][99] == 1:
                    neighbors += 1
                if normGrid[1][1] == 1:
                    neighbors += 1
                if normGrid[99][1] == 1:
                    neighbors += 1
            if y == 99:
                if normGrid[99][99] == 1:
                    neighbors += 1
                if normGrid[0][98] == 1:
                    neighbors += 1
                if normGrid[0][0] == 1:
                    neighbors += 1
                if normGrid[1][99] == 1:
                    neighbors += 1
                if normGrid[99][99] == 1:
                    neighbors += 1
                if normGrid[0][99] == 1:
                    neighbors += 1
                if normGrid[0][1] == 1:
                    neighbors += 1
                if normGrid[1][1] == 1:
                    neighbors += 1
            else:
                if normGrid[99][y] == 1:
                    neighbors += 1
                if normGrid[0][y-1] == 1:
                    neighbors += 1
                if normGrid[0][y+1] == 1:
                    neighbors += 1
                if normGrid[1][y] == 1:
                    neighbors += 1
                if normGrid[99][y] == 1:
                    neighbors += 1
                if normGrid[0][y] == 1:
                    neighbors += 1
                if normGrid[0][y+1] == 1:
                    neighbors += 1
                if normGrid[1][y+1] == 1:
                    neighbors += 1
            return neighbors
                    
        if y == 0:
            if x == 99:
                if normGrid[98][0] == 1:
                    neighbors += 1
                if normGrid[99][99] == 1:
                    neighbors += 1
                if normGrid[99][1] == 1:
                    neighbors += 1
                if normGrid[0][0] == 1:
                    neighbors += 1
                if normGrid[0][1] == 1:
                    neighbors += 1
                if normGrid[98][1] == 1:
                    neighbors += 1
                if normGrid[98][99] == 1:
                    neighbors += 1
                if normGrid[0][99] == 1:
                    neighbors += 1
            else:
                if normGrid[x-1][0] == 1:
                    neighbors += 1
                if normGrid[x][99] == 1:
                    neighbors += 1
                if normGrid[x][1] == 1:
                    neighbors += 1
                if normGrid[x+1][0] == 1:
                    neighbors += 1
                if normGrid[x+1][1] == 1:
                    neighbors += 1
                if normGrid[x-1][1] == 1:
                    neighbors += 1
                if normGrid[x-1][99] == 1:
                    neighbors += 1
                if normGrid[x+1][99] == 1:
                    neighbors += 1
            return neighbors
                    
        if x == 99:
            if y == 99:
                if normGrid[98][99] == 1:
                    neighbors += 1
                if normGrid[99][98] == 1:
                    neighbors += 1
                if normGrid[99][0] == 1:
                    neighbors += 1
                if normGrid[0][99] == 1:
                    neighbors += 1
                if normGrid[98][99] == 1:
                    neighbors += 1
                if normGrid[99][99] == 1:
                    neighbors += 1
                if normGrid[99][1] == 1:
                    neighbors += 1
                if normGrid[0][1] == 1:
                    neighbors += 1
            else:
                if normGrid[98][y] == 1:
                    neighbors += 1
                if normGrid[99][y-1] == 1:
                    neighbors += 1
                if normGrid[99][y+1] == 1:
                    neighbors += 1
                if normGrid[0][y] == 1:
                    neighbors += 1
                if normGrid[98][y] == 1:
                    neighbors += 1
                if normGrid[99][y] == 1:
                    neighbors += 1
                if normGrid[99][y+1] == 1:
                    neighbors += 1
                if normGrid[0][y+1] == 1:
                    neighbors += 1
            return neighbors
                    
        if y == 99:
            if normGrid[x-1][99] == 1:
                neighbors += 1
            if normGrid[x][98] == 1:
                neighbors += 1
            if normGrid[x][0] == 1:
                neighbors += 1
            if normGrid[x+1][99] == 1:
                neighbors += 1
            if normGrid[x-1][99] == 1:
                neighbors += 1
            if normGrid[x][99] == 1:
                neighbors += 1
            if normGrid[x][1] == 1:
                neighbors += 1
            if normGrid[x+1][1] == 1:
                neighbors += 1
            return neighbors
            
        return neighbors
                    

# One tick of the game, call to start game
def tick():
        tempLiving = [[0 for i in range(100)] for i in range(100)]
        global normGrid
        for x in range (0,100):
                for y in range (0,100):
                        if normGrid[x][y] != 1:
                                tempLiving[x][y] = determineDLife(x,y)
                        if normGrid[x][y] == 1:
                                tempLiving[x][y] = determineLife(x,y)
        normGrid = tempLiving
        printAll()
        time.sleep(.05)
        tick()

def main():
    size = width, height = 320, 240
    pygame.init()
    global surface 
    global normGrid
    points = []
    
    # initial grid
    for x in range (0,100):
            for y in range (0,100):
                    if normGrid[x][y] == 1:
                            points.append(pygame.Rect(4*x,4*y,4*2,4*2))
                    else:
                        normGrid[x][y] == 0
    
    tick()
 
surface = pygame.display.set_mode((400, 400), 0, 0)
normGrid = [[np.random.randint(10) for i in range(100)] for i in range(100)]
main()