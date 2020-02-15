from searches import dfs
from searches import astar
from searches import *
from map import generateMap, printMap
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt

# Genetic Algorithm

# DFS With Max Fringe Size

# A* Manhattan With Max Nodes Expanded


def main():

    inputAlgo = input("Enter dfs or a*: ")

    if (inputAlgo == "dfs"):
        pop = genetic_algorithm("dfs")
        temp = pop[2]
        temp[0][0] = 0
        temp[len(temp) - 1][len(temp) - 1] = 0

        for x in range(len(temp)):
            for y in range(len(temp)):
                if temp[x][y] == 0:
                    temp[x][y] = 4
                elif temp[x][y] == 1:
                    temp[x][y] = 0
        result = pop[0]
        for (x, y) in result:
            temp[x][y] = 3
        M = np.array(temp)
        plt.figure(1)
        plt.imshow(M, cmap=plt.gray())
        plt.plot()
        plt.title("HARD MAZE FOR DFS WITH MAX FRINGE SIZE")
        plt.xlabel('Column')
        plt.ylabel('Row')
        plt.show()
    elif (inputAlgo == "a*"):
        pop = genetic_algorithm("a*")
        print("HERE")
        temp = pop[2]
        temp[0][0] = 0
        temp[len(temp) - 1][len(temp) - 1] = 0
        for x in range(len(temp)):
            for y in range(len(temp)):
                if temp[x][y] == 0:
                    temp[x][y] = 4
                elif temp[x][y] == 1:
                    temp[x][y] = 0
        result = pop[0]
        for (x, y) in result:
            temp[x][y] = 3
        
        M = np.array(temp)
        plt.figure(2)
        plt.imshow(M, cmap=plt.gray())
        plt.plot()
        plt.title("HARD MAZE FOR A STAR MANHATTAN WITH MAX NODES EXPANDED")
        plt.xlabel('Column')
        plt.ylabel('Row')
        plt.show()

    


def genetic_algorithm(algo):
    dim = 10
    prob = .2
    count = 0
    population = []
    while count != 100:
        map = generateMap(dim, prob)
        if (algo == "dfs"):
            result = dfs(map)
        else:
            map[0][0] = 0
            map[len(map) - 1][len(map) - 1] = 0
            result = astar(map,0)
            print(result == None)

            '''
            try:
                result = astar(map,0)[0]
            except IOError:
                result = None
            '''
        if (result == None):
            continue
        else:
            population.append(result)
            result.append(map)
            count = count + 1

    count = 0

    while count != 50:
        population = sorted(population, key = itemgetter(1), reverse = True)
        dad = population[0]
        mom = population[1]
        kid = [[0 for x in range(dim)] for y in range(dim)]

        map1 = dad[2]
        map2 = mom[2]
        go = 0
        stop = (dim * dim) / 2
        for x in range(dim):
            for y in range(dim):
                if (go < stop):
                    kid[x][y] = map1[x][y]
                else:
                    kid[x][y] = map2[x][y]
                go = go + 1
        #printMap(map1)
        #printMap(map2)
        #printMap(kid)
        if algo == "dfs":
            final = dfs(kid)
        else:
            try:
                final[0][0] = 0
                final[len(final) - 1][len(final) - 1] = 0
                final = astar(kid, 0)
            except IOError:
                final = None

        if (final == None):
            population.pop(0)
        else:
            population.pop()
            population.append(final)
        count = count + 1
    return population[0]

main()



