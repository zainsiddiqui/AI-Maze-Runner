import random as r
from searches import bfs
from searches import dfs
from searches import *


def main():
  inputDim = input("Enter dimension of map: ")
  inputP = input("Enter probability 0<p<1: ")
  map=generateMap(int(inputDim),float(inputP))
  printMap(map)
  search = input("Choose search option: dfs, bfs, a*, bi-bfs \n")
  if (search == "dfs"):
    dfs(map)
  elif (search == "bfs"):
    bfs(map)
    dfs(map)
  elif (search == "a*"):
    print("")
  elif (search == "bi-bfs"):
    bidirectional_bfs(map)


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





main()
