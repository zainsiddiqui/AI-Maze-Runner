import random as r
import numpy as np
import matplotlib.pyplot as plt
import copy

def main():
    inputDim = input("Enter dimension for FIRE map: ")
    inputP = input("Enter probability for FIRE map 0<=p<=1: ")
    inputQ = input("Enter flammabilty for FIRE map 0<=y<=1: ")
    q = float(inputQ)
    map = generateFireMaze(int(inputDim),float(inputP))
    mazeVisual(map)
    plt.show()

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

    return map

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

main()
