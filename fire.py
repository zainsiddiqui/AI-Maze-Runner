import random as r
import numpy as np
import matplotlib.pyplot as plt
import copy
from searches import Coordinates
from map import printMap

def main():
    inputDim = input("Enter dimension for FIRE map: ")
    inputP = input("Enter density for FIRE map 0<=p<=1: ")
    inputQ = input("Enter flammabilty for FIRE map 0<=y<=1: ")
    q = float(inputQ)
    # Generating Fire Mze given dimensions and density
    result = generateFireMaze(int(inputDim),float(inputP))
    map = result[0]
    mazeStart = result[0]
    # Extracting origin of fire
    firex = result[1]
    firey = result[2]
    mazeVisual(map)
    current = (0, 0)
    map[0][0] = 9
    # Making origin of fire a coordinate
    originFire = Coordinates(firex, firey)
    # Initalizing path with start
    path = [(0,0)]
    end = True
    while (end == True):
  
        score = 0
        # Fire potentially spreading to a new cell
        map = updateFire(map, q)
        # Getting all neighbors of current cell
        neighbors = get_neighbors(map,current)

        # For every neighbor 
        for x in neighbors:
            # Calculate heaurstic of neghbor cell
            result = calculateHeaurstic(map, x, originFire)
            
            # If true, then we have found the goal cell
            if result[1] == True:
                map[x[0]][x[1]] = 9
                path.append(x)
                #print(path)
                #printMap(map) 
                end = False
            # If current cells's heuristic is greater, make new score and current cell
            if result[0] > score:
                score = result[0]
                current = x
                #print(current)

        #print(current)
        if (end == False):
            break

        (x,y) = current
        # Mark as visited cell
        map[x][y]=9
        
        # 
        path.append(current)
        #printMap(mazeStart)
        #printMap(map)
    temp = copy.deepcopy(map)

    for x in range(len(map)):
        for y in range(len(map)):
            if temp[x][y] == 0:
                temp[x][y] = 4
            elif temp[x][y] == 1:
                temp[x][y] = 0
            else:
                temp[x][y] = 2
    #print(path)
    for (x, y) in path:
        temp[x][y] = 3
    #print("HERE")
    M = np.array(temp)
    plt.figure(2)
    plt.imshow(M, cmap=plt.hot())
    plt.plot()
    plt.title("FIRE MAZE SOLUTION")
    plt.xlabel('Column')
    plt.ylabel('Row')

    plt.show()
        
            
   

def get_neighbors(map,current):

    (row,column) = current
    neighbors = []
    
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        position = (row + new_position[0], column + new_position[1])
        if position[0] > (len(map) - 1) or position[0] < 0 or position[1] > (len(map[len(map)-1]) -1) or position[1] < 0:
            continue
        if map[position[0]][position[1]] != 0:
            continue
        neighbors.append(position)
                          
    return neighbors
    
  

def num_burning_neighbors(temp, x, y):
    count = 0
    if (x + 1 >= 0 and x + 1 < len(temp) and y >= 0 and y < len(temp) and temp[x + 1][y] == 2):
        count = count + 1
    if (x - 1 >= 0 and x - 1 < len(temp) and y >= 0 and y < len(temp) and temp[x - 1][y] == 2):
        count = count + 1
    if (x >= 0 and x < len(temp) and y + 1 >= 0 and y + 1 < len(temp) and temp[x][y + 1] == 2):
        count = count + 1
    if (x >= 0 and x < len(temp) and y - 1 >= 0 and y - 1 < len(temp) and temp[x][y - 1] == 2):
        count = count + 1
    return count

def updateFire(map, q):
    temp = copy.deepcopy(map)
    for x in range(len(temp)):
        for y in range(len(temp)):
            k = num_burning_neighbors(temp, x, y)
            if (temp[x][y] == 0 and k > 0):
                prob = 1 - ((1 - q) ** k)
                v = [2, 0]
                weights = [prob, 1 - prob]
                value = r.choices(v, weights)
                temp[x][y] = value[0]  
    return temp

            



def generateFireMaze(dim, p):
    map = [[0 for x in range(dim)] for y in range(dim)]
    v = [0,1]
    weights = [1-p,p]
    for row in range(len(map)):
        for col in range(len(map)):
            value = r.choices(v,weights)
            map[row][col] = value[0]
    x = 0
    y = 0
    while ((x == 0 and y == 0) or (x == dim - 1 and y == dim -1) or (map[x][y] == 1)):
        x = r.randrange(0, dim - 1)
        y = r.randrange(0, dim - 1)
    map[x][y] = 2
    map[0][0] = 0
    map[len(map) - 1][len(map) - 1] = 0
    return [map, x, y]

def mazeVisual(map):
    temp = copy.deepcopy(map)
    for x in range(len(map)):
        for y in range(len(map)):
            if temp[x][y] == 0:
                temp[x][y] = 4
            elif temp[x][y] == 1:
                temp[x][y] = 0
            else:
                temp[x][y] = 2
    temp[0][0] = 3

    #temp[0][0] = 3
    #temp[len(temp) - 1][len(temp) - 1] = 3
    M = np.array(temp)
    plt.figure(1)
    plt.imshow(M, cmap=plt.hot())
    plt.plot()
    plt.title("MAZE")
    plt.xlabel('Column (MAZE)')
    plt.ylabel('Row (MAZE)')
    
## Calculates manhattan distance from current coordinate to origin coordinate
def calculateHeaurstic(map, currentCell, origin_fire):
    (x,y) = currentCell
    if (x == len(map)-1 and y == len(map)-1):
        return [0,True]
    else:
        score = (abs(x - origin_fire.x) + abs(y - origin_fire.y))
        return [score, False]

main()