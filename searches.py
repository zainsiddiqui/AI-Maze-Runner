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


def check_bi_bfs(curr, queue):
    for temp in queue:
        if (temp.x == curr.x and temp.y == curr.y):
            return True
    return False

def bidirectional_bfs(map):
    visited = [[0 for x in range(len(map))] for y in range(len(map))]
    queueS = []
    queueG = []
    path = []
    
    queueS.append(Coordinates(0, 0))
    queueG.append(Coordinates(len(map) - 1, len(map) - 1))
    

    while (len(queueS) > 0 and len(queueG) > 0):
        if (len(queueS) > 0):
            currStart = queueS.pop(0)
            path.append(currStart)
            rowS = currStart.x
            columnS = currStart.y
            
            if (rowS < 0 or rowS >= len(map) or columnS < 0 or columnS >= len(map) or visited[rowS][columnS] == 1 or map[rowS][columnS] == 1):
                path.pop()
                #continue
                
            elif (map[rowS][columnS] == "G" or check_bi_bfs(currStart, queueG)):
                visited[rowS][columnS] = 1
                print("PATH FOUND FOR BI-BFS: ")
                for curr in path:
                    print(curr.x, curr.y)
                return
            else:
                visited[rowS][columnS] = 1
                queueS.append(Coordinates(rowS, columnS - 1))
                queueS.append(Coordinates(rowS, columnS + 1))
                queueS.append(Coordinates(rowS - 1, columnS)) 
                queueS.append(Coordinates(rowS + 1, columnS))
        
        if (len(queueG) > 0):
            currGoal = queueG.pop(0)
            path.append(currGoal)
            rowG = currGoal.x
            columnG = currGoal.y
            if (rowG < 0 or rowG >= len(map) or columnG < 0 or columnG >= len(map) or visited[rowG][columnG] == 1 or map[rowG][columnG] == 1):
                path.pop()
            elif (map[rowG][columnG] == "S" or check_bi_bfs(currGoal, queueS)):
                visited[rowG][columnG] = 1
                print("PATH FOUND FOR BI-BFS: ")
                for curr in path:
                    print(curr.x, curr.y)
                return
            else:
                visited[rowG][columnG] = 1
                queueG.append(Coordinates(rowG, columnG - 1))
                queueG.append(Coordinates(rowG, columnG + 1))
                queueG.append(Coordinates(rowG - 1, columnG)) 
                queueG.append(Coordinates(rowG + 1, columnG))
    print("NO PATH FOUND FOR BI-BFS")
    return










map = [["S", 0, 0], [0,1,0], [0,1,"G"]]
bidirectional_bfs(map)
# dfs(map)
# bfs(map)