from searches import dfs
from searches import astar
from map import generateMap, printMap
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
import copy
import signal
import time

# Genetic Algorithm

# DFS With Max Fringe Size

# A* Manhattan With Max Nodes Expanded


def handler(signum, frame):
    raise IOError("Timeout")
 

def main():
    # Ask user for which algo/paired metric they want to run
    inputAlgo = input("Enter dfs or a*: ")

    if (inputAlgo == "dfs"):
        # This runs our gentic algo for dfs
        pop = genetic_algorithm("dfs")
        temp = pop[2]
        temp[0][0] = 0
        temp[len(temp) - 1][len(temp) - 1] = 0
        # This is solely for visualtions and colormap schemes
        for x in range(len(temp)):
            for y in range(len(temp)):
                if temp[x][y] == 0:
                    temp[x][y] = 4
                elif temp[x][y] == 1:
                    temp[x][y] = 0
        result = pop[0]
        # we have the path our gentic algo takes for a hard maze and we simply construct that path for the visual
        for (x, y) in result:
            temp[x][y] = 3
        # Using matplotlib for visuals
        M = np.array(temp)
        plt.figure(1)
        plt.imshow(M, cmap=plt.gray())
        plt.plot()
        plt.title("HARD MAZE FOR DFS WITH MAX FRINGE SIZE")
        plt.xlabel('Column')
        plt.ylabel('Row')
        plt.show()
    elif (inputAlgo == "a*"):
        # same concept as above but we run a star version of our gentic algo 
        pop = genetic_algorithm("a*")
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
    dim = 15
    prob = .4
    count = 0
    # Population will hold our valid hard mazes
    population = []
    # While loop halts when we have 100 hard mazes in the population
    while count != 100:
        # create a random map
        map = generateMap(dim, prob)
        if (algo == "dfs"):
            result = dfs(map)
        else:
            temp = copy.deepcopy(map)
            temp[0][0]=0
            temp[len(temp)-1][len(temp)-1] = 0
            start_time = time.time()
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(1)
            try:
                result = astar(temp,0)
            except IOError:
                result = None
        if (result == None):
            continue
        else:
            # if w ehave a valid solvable maze then add to population
            result.append(map)
            population.append(result)
            count = count + 1
            #print("Population count "+ str(count))

    count = 0
    # while loop halts once we have costruced 50 valid children
    while count != 50:
        # sort the population by our heuristic and reverse so the highest score is first
        population = sorted(population, key = itemgetter(1), reverse = True)
        # dad is the best hard maze we have
        dad = population[0]
        # mom is the second best hard maze we have
        mom = population[1]
        # set up child as 2D array which is how enivroments are used in backend
        kid = [[0 for x in range(dim)] for y in range(dim)]
        map1 = dad[2]
        map2 = mom[2]
        # Thsi snippet of code perform recombination
        # we take the first half of dad and second half of mom and populate the child accrodingly
        go = 0
        stop = (dim * dim) / 2
        for x in range(dim):
            for y in range(dim):
                if (go < stop):
                    kid[x][y] = map1[x][y]
                else:
                    kid[x][y] = map2[x][y]
                go = go + 1
        # We run whichever algo the user had chosen on the newly created kid maze 
        if algo == "dfs":
            final = dfs(kid)
        else:
            kid[0][0] = 0
            kid[len(kid) - 1][len(kid) - 1] = 0
            start_time = time.time()
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(1)
            try:
                final = astar(kid,0)
            except IOError:
                final = None
        # if child is not solvable we get rid of dad and try again with a differnt set of mazes
        if (final == None):
            population.pop(0)
        # if child is valid we append the kid and pop the worst in popualtion
        # Later the kid will be placed in the right position during out sorting phase
        else:
            population.pop()
            population.append(final)
        count = count + 1
    # we return the most fit maze or hardest maze in our population as our answer
    return population[0]

main()


