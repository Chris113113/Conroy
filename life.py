import numpy as np
import sys, pygame, time

def printAll(points):
        global surface
        surface.fill((0,0,0))
        for rec in points:
            pygame.draw.rect(surface, (0,0,255), rec, 0)
        mainSurface.blit(surface, (0,50),None,0)
        pygame.display.update()
        points = []

            
#Takes in current neighbors and determines if it should liev through this generation
def determineLife(x,y):
        if EXPANDED_NEIGHBORHOOD:
            neighbors = checkExNeighbors(x,y, True)
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
            neighbors = checkExNeighbors(x,y, False)
        else:
            neighbors = checkNeighbors(x,y)
        #if neighbors != 0 and neighbors != 1 and neighbors != 2 and neighbors != 3:
            #print("DEAD: ", neighbors)
        if neighbors == 3:
                return 1
        else:
            return 0    
        
# Check neighbors and update temp grid
def checkExNeighbors(x,y, live):
        global normGrid
        global MAX_SIZE
        neighbors = int(0)
        tx = x%(MAX_SIZE)
        ty = y%(MAX_SIZE)
        if live:
            if normGrid[(x-1)%MAX_SIZE][y%MAX_SIZE] == 1:
                    neighbors += 1
            else:
                    deadSet.add(((x-1)%MAX_SIZE,y%MAX_SIZE))
            if normGrid[x%MAX_SIZE][(y+1)%MAX_SIZE] == 1:
                    neighbors += 1
            else:
                    deadSet.add((x%MAX_SIZE,(y+1)%MAX_SIZE))
            if normGrid[(x+1)%MAX_SIZE][y%MAX_SIZE] == 1:
                    neighbors += 1
            else:
                    deadSet.add(((x+1)%MAX_SIZE,y%MAX_SIZE))
            if normGrid[x%MAX_SIZE][(y-1)%MAX_SIZE] == 1:
                    neighbors += 1
            else:
                    deadSet.add((x%MAX_SIZE,(y-1)%MAX_SIZE))
            if normGrid[(x-1)%MAX_SIZE][(y-1)%MAX_SIZE] == 1:
                    neighbors += 1
            else:        
                    deadSet.add(((x-1)%MAX_SIZE,(y-1)%MAX_SIZE))
            if normGrid[(x-1)%MAX_SIZE][(y+1)%MAX_SIZE] == 1:
                    neighbors += 1
            else:        
                    deadSet.add(((x-1)%MAX_SIZE,(y+1)%MAX_SIZE))
            if normGrid[(x+1)%MAX_SIZE][(y+1)%MAX_SIZE] == 1:
                    neighbors += 1
            else:
                    deadSet.add(((x+1)%MAX_SIZE,(y+1)%MAX_SIZE))
            if normGrid[(x+1)%MAX_SIZE][(y-1)%MAX_SIZE] == 1:
                    neighbors += 1
            else:        
                    deadSet.add(((x+1)%MAX_SIZE,(y-1)%MAX_SIZE))
        else:
            if normGrid[(x-1)%MAX_SIZE][y%MAX_SIZE] == 1:
                    neighbors += 1
            if normGrid[x%MAX_SIZE][(y+1)%MAX_SIZE] == 1:
                    neighbors += 1
            if normGrid[(x+1)%MAX_SIZE][y%MAX_SIZE] == 1:
                    neighbors += 1
            if normGrid[x%MAX_SIZE][(y-1)%MAX_SIZE] == 1:
                    neighbors += 1
            if normGrid[(x-1)%MAX_SIZE][(y-1)%MAX_SIZE] == 1:
                    neighbors += 1
            if normGrid[(x-1)%MAX_SIZE][(y+1)%MAX_SIZE] == 1:
                    neighbors += 1
            if normGrid[(x+1)%MAX_SIZE][(y+1)%MAX_SIZE] == 1:
                    neighbors += 1
            if normGrid[(x+1)%MAX_SIZE][(y-1)%MAX_SIZE] == 1:
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
                    if normGrid[x][y] == 1:
                            tempLiving[x][y] = determineLife(x,y)
                            if tempLiving[x][y] == 1:
                                points.append(pygame.Rect(constant*x,constant*y,constant*2,constant*2))
    #Check dead neighbors
    while len(deadSet) != 0:
        curDead = deadSet.pop()
        x = curDead[0]
        y = curDead[1]
        tempLiving[x][y] = determineDLife(x,y)
        if tempLiving[x][y] == 1:
            points.append(pygame.Rect(constant*x,constant*y,constant*2,constant*2))
    return (tempLiving, points)

def updateHeader(gen):
     txtstr = "Generation %d:" %gen
     text = genFont.render(txtstr, 1, (255,255,255), (0,0,0))
     mainSurface.blit(text, (2,2), None, 0)
    

# One tick of the game, call to start game
def tick():
    global normGrid
    ret = tempLiving()
    normGrid = ret[0]
    printAll(ret[1])

def main():
    global surface 
    global normGrid
    points = []
    rec = pygame.Rect(100,0,10,10)
    
    # initial grid
    for x in range (0,MAX_SIZE):
            for y in range (0,MAX_SIZE):
                    if normGrid[x][y] != 1:
                        normGrid[x][y] == 0
    genNum = 0
    while genNum > -1:
        updateHeader(genNum)
        tick()
        time.sleep(.01)
        genNum += 1

MAX_SIZE                = 150
RESOLUTION              = 500
FILL_PERCENTAGE         = 20
EXPANDED_NEIGHBORHOOD   = True
pygame.init()
mainSurface = pygame.display.set_mode((RESOLUTION,RESOLUTION+50))
surface = pygame.Surface((RESOLUTION, RESOLUTION), 0, mainSurface)
deadSet = set()
genFont = pygame.font.Font(None, 24)
normGrid = [[np.random.randint(int(100/FILL_PERCENTAGE)) for i in range(MAX_SIZE)] for i in range(MAX_SIZE)]
main()
