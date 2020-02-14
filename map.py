import random as r
from searches import bfs
from searches import dfs
from searches import bi_bfs
from searches import astar
import time
import signal
import numpy as np
import matplotlib.pyplot as plt
import copy


def main(): 
  inputDim = input("Enter dimension of map: ")
  inputP = input("Enter probability 0<p<1: ")
  map=generateMap(int(inputDim),float(inputP))
  #printMap(map)
  mazeVisual(map)
  #printMap(map)
  count = 2
  search = input("Choose search option: visuals, dfs, bfs, a*, bi-bfs, all \n")
  if (search == "dfs"):
    start_time = time.time()
    result = dfs(map)
    print("--- %s seconds ---" % (time.time() - start_time))
    if (result == None):
      print("NO DFS PATH FOUND")
    visual(map, result, "DFS", count)
   

  elif (search == "bfs"):
    start_time = time.time()
    result = bfs(map)
    print("--- %s seconds ---" % (time.time() - start_time))
    if (result == None):
      print("NO BFS PATH FOUND")
      return

    visual(map, result, "BFS", count) 
  elif (search == "a*" or search == "a" ):
    
    # Setting up map
    map[0][0]=0
    map[len(map)-1][len(map)-1] = 0

    flag = input("Enter number: (0) Manhattan (1) Euclidean \n")
    # 1 for Euclidean
    # 0 for Manhattan
    start_time = time.time()
    time.time()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(25)
    try:
      ##path = astar(map,int(flag))
      path = astar(map,flag)
    except IOError:
      path = None

    if path is None:
      print("A* path does not exist")
      return
    #else:
      #print(path)
    print("--- %s seconds ---" % (time.time() - start_time)) 
    result = path
    visual(map, result, "A*", count)
    
  elif (search == "bi-bfs"):
    start_time = time.time()
    result = bi_bfs(map)
    print("--- %s seconds ---" % (time.time() - start_time))
    if (result == None):
      print("NO BI-BFS PATH FOUND")
      #return
    visual(map, result, "BI-DIRECTIONAL BFS", count)
  elif (search == "all"):
    start_time = time.time()
    path = dfs(map)
    ##print(path)
    print("dfs path length: "+ str(len(path)))
    print("--- dfs took %s seconds ---" % (time.time() - start_time)) 
    start_time = time.time()
    path = bfs(map)
    ##print(path)
    print("bfs path length: "+ str(len(path)))
    print("--- bfs took %s seconds ---" % (time.time() - start_time)) 
    # Setting up map
    map[0][0]=0
    map[len(map)-1][len(map)-1] = 0
    start_time = time.time()
    time.time()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(3)
    try:
      path = astar(map,0)
    except IOError:
      path = None

    if path is None:
      print("NO PATH FOUND FOR A* MANHATTAN")
    else:
      ##print(path)
      print("a* manhatttan path length: "+ str(len(path)))
    print("--- a* manhatttan took %s seconds ---" % (time.time() - start_time)) 
    # Setting up map
    map[0][0]=0
    map[len(map)-1][len(map)-1] = 0
    start_time = time.time()
    time.time()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(3)
    try:
      path = astar(map,1)
    except IOError:
      path = None

    if path is None:
      print("NO PATH FOUND FOR A* EUCLIDEAN")
    else:
      ##print(path)
      print("a* euclidean path length: "+ str(len(path)))
    print("--- a* euclidean took %s seconds ---" % (time.time() - start_time)) 
    start_time = time.time()
    path = bi_bfs(map)
    ##print(path)
    print("bi-bfs path length: "+ str(len(path)))
<<<<<<< HEAD
  elif (search == "visuals"):
    temp = copy.deepcopy(map)
    temp[0][0]=0
    temp[len(map)-1][len(map)-1] = 0
    result1 = dfs(map)
    result2 = bfs(map)
    result3 = bi_bfs(map)
    result4 = astar(temp, 0)
    result5 = astar(temp, 1)

    if (result1 == None):
      print("NO DFS PATH FOUND")
    else:
      visual(map, result1, "DFS", count)
      count = count + 1

    if (result2 == None):
      print("NO BFS PATH FOUND")
    else:
      visual(map, result2, "BFS", count)
      count = count + 1

    if (result3 == None):
      print("NO BI-BFS PATH FOUND")  
    else:
      visual(map, result3, "BI-BFS", count)
      count = count + 1 

    if (result4 == None):
      print("NO A* EUCLIDEAN PATH FOUND")
    else:
      visual(temp, result4, "A* EUCLIDEAN", count)
      count = count + 1

    if (result5 == None):
      print("NO A* MANHATTAN PATH FOUND")
    else:
      visual(temp, result5, "A* MANHATTAN", count)
      count = count + 1

   



  plt.show()
=======
    print("--- bi-bfs took %s seconds ---" % (time.time() - start_time))
   
>>>>>>> fa56e81050cea9076f51d1023382074586101a92
    
def mazeVisual(map):
  temp = copy.deepcopy(map)
  for x in range(len(map)):
    for y in range(len(map)):
      if temp[x][y] == 0:
        temp[x][y] = 4
      elif temp[x][y] == 1:
        temp[x][y] = 0
  temp[0][0] = 3
  temp[len(temp) - 1][len(temp) - 1] = 3
  M = np.array(temp)
  plt.figure(1)
  plt.imshow(M, cmap=plt.gray())
  plt.plot()
  plt.title("MAZE")
  plt.xlabel('Column (MAZE)')
  plt.ylabel('Row (MAZE)')

def visual(map, result, strr, count):

  temp = copy.deepcopy(map)

  for x in range(len(map)):
    for y in range(len(map)):
      if temp[x][y] == 0:
        temp[x][y] = 4
      elif temp[x][y] == 1:
        temp[x][y] = 0

  for (x, y) in result:
    temp[x][y] = 3
  
  M = np.array(temp)
  plt.figure(count)
  plt.imshow(M, cmap=plt.gray())
  plt.plot()
  plt.title(strr)
  plt.xlabel('Column')
  plt.ylabel('Row')
  #plt.pause(0.1)
  '''
  for x in range(len(map)):
    for y in range(len(map)):
  '''

def printMap(a):
  print("map:")
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))
  print()

def generateMap(dim,p):
  map = [[0 for x in range(dim)] for y in range(dim)]
  v = [0,1]
  weights = [1-p,p]
  for row in range(len(map)):
    for col in range(len(map)):
      value = r.choices(v,weights)
      map[row][col] = value[0]
  map[0][0] = "S"
  map[dim-1][dim-1] = "G"
  return map

# Calculates solvability
def calculateSolvability():
 
  i = 10
  i2 = i
  solvable = 0
  unsolvable = 0
  while (i > 0):
    map = None
    map = generateMap(int(10),0)
    printMap(map)
    map[0][0] = 0
    map[9][9] = 0
    path = astar(map,int(1))
    print(path)
    if path is None:
     unsolvable = unsolvable + 1
    else:
      solvable = solvable + 1
    i=i-1

  print("Generated: "+ str(i2) +" and # Solvable: " + str(solvable))
  print("Success Percent: "+ str((solvable/i2)*100))

def handler(signum, frame):
    raise IOError("Timeout")
 
def slow_function():
    time.sleep(30)
 
# Calculates average shortest path length
def calculateAvgPathLength():
 
  i = 100
  i2 = i
  solvable = 0
  unsolvable = 0
  pathLen = []
  while (i > 0):
    map = None
    map = generateMap(int(100),0.3)
    printMap(map)
    map[0][0] = 0
    map[99][99] = 0
    time.time()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
 
    try:
      path = astar(map,int(1))
    except IOError:
      time.time()
      unsolvable = unsolvable + 1
      continue
   
    print(path)
    if path is None:
     unsolvable = unsolvable + 1
    else:
      pathLen.append(len(path))
      solvable = solvable + 1
    i=i-1

  print("Generated: "+ str(i2) +"maps and # solvable: " + str(solvable))
  print(pathLen)
  print("Avg Path Length: "+ str(sum(pathLen)/len(pathLen)))

def compareHeuristics():
  timeList = []
  while (len(timeList) < 10):
    time.time()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    map = None
    map = generateMap(int(100),0.15)
 # Setting up map
    map[0][0]=0
    map[len(map)-1][len(map)-1] = 0
    start_time = time.time()
    time.time()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    try:
      path = astar(map,1)
    except IOError:
      path = None

    if path is None:
      print("path does not exist")
    else:
      print(path)
      print("--- %s seconds ---" % (time.time() - start_time)) 
      timeList.append((time.time() - start_time))
    
  print(timeList)
  print("Avg time: "+str(sum(timeList)/len(timeList)))

main()
