# Search Algorithms
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ASK COWAN IF WE NEED FINAL PATH OR THE PATH THAT THE PROGRAM TAKES
def dfs(map):
    visited = [[0 for x in range(len(map))] for y in range(len(map))]
    stack = []
    path = []
    stack.append(Coordinates(0, 0))
    while (len(stack) > 0):
        curr = stack.pop()
        path.append(curr)
        row = curr.x
        column = curr.y   
        if (row < 0 or row >= len(map) or column < 0 or column >= len(map) or visited[row][column] == 1 or map[row][column] == 1):
            path.pop()
            continue
        if (map[row][column] == "G"):
            visited[row][column] = 1
            print("PATH FOUND FOR DFS: ")
            for curr in path:
                print(curr.x, curr.y)
            return
        else:
            visited[row][column] = 1
            stack.append(Coordinates(row, column - 1))
            stack.append(Coordinates(row, column + 1))
            stack.append(Coordinates(row - 1, column)) 
            stack.append(Coordinates(row + 1, column))
    print("NO PATH FOUND FOR DFS")
    return


def bfs(map):
    visited = [[0 for x in range(len(map))] for y in range(len(map))]
    queue = []
    path = []
    queue.append(Coordinates(0, 0))
    while (len(queue) > 0):
        curr = queue.pop(0)
        path.append(curr)
        row = curr.x
        column = curr.y
        if (row < 0 or row >= len(map) or column < 0 or column >= len(map) or visited[row][column] == 1 or map[row][column] == 1):
            path.pop()
            continue
        if (map[row][column] == "G"):
            visited[row][column] = 1
            print("PATH FOUND FOR BFS: ")
            for curr in path:
                print(curr.x, curr.y)
            return
        else:
            visited[row][column] = 1
            queue.append(Coordinates(row, column - 1))
            queue.append(Coordinates(row, column + 1))
            queue.append(Coordinates(row - 1, column)) 
            queue.append(Coordinates(row + 1, column))
    print("NO PATH FOUND FOR BFS")
    return





# map = [["S", "0", "0"], ["0","1","0"], ["0","1","G"]]
# dfs(map)
# bfs(map)