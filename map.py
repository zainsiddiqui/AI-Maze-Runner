import random as r


def main():
  inputDim = input("Enter dimension of map: ")
  map=generateMap(int(inputDim))
  printMap(map)

def printMap(a):
  print("map:")
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))
  print()

def generateMap(dim):
  map = [[0 for x in range(dim)] for y in range(dim)]
  p = [0,1]
  for row in range(len(map)):
    for col in range(len(map)):
      map[row][col]= r.choice(p)

  map[0][0] = "s"
  map[dim-1][dim-1] = "x"
  return map





main()
