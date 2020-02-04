import random as r
import numpy as np

def main():
  inputDim = input("Enter dimension of map: ")
  map=generateMap(int(inputDim))
  printMap(map)

def printMap(a):
    for row in range(len(a)):
        for col in range (len(a[row])):
            print("{:8.3f}".format(a[row][col]), end = " ")
        print()

def generateMap(dim):
  map = [[0 for x in range(dim)] for y in range(dim)]
  r.choice(map)
  return map





main()
