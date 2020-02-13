import random as r
from searches import bfs
from searches import dfs
from searches import bi_bfs
from searches import astar,astare,astarm
import time
import signal
 


def main(): 
  inputDim = input("Enter dimension of map: ")
  inputP = input("Enter probability 0<p<1: ")
  map=generateMap(int(inputDim),float(inputP))
  printMap(map)
  search = input("Choose search option: dfs, bfs, a*, bi-bfs or all \n")
  if (search == "dfs"):
    start_time = time.time()
    dfs(map)
    print("--- %s seconds ---" % (time.time() - start_time)) 
  elif (search == "bfs"):
    start_time = time.time()
    bfs(map)
    print("--- %s seconds ---" % (time.time() - start_time)) 
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
      path = astare(map,(0,0),(len(map)-1,len(map)-1))
    except IOError:
      path = None

    if path is None:
      print("path does not exist")
    else:
      print(path)
    print("--- %s seconds ---" % (time.time() - start_time)) 
    
  elif (search == "bi-bfs"):
    start_time = time.time()
    bi_bfs(map)
    print("--- %s seconds ---" % (time.time() - start_time))
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
      path = astarm(map,(0,0),(len(map)-1,len(map)-1))
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
      path = astare(map,(0,0),(len(map)-1,len(map)-1))
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
    print("--- bi-bfs took %s seconds ---" % (time.time() - start_time))
   
    



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
