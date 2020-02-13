import heapq

class coordNode():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, a):
        return self.f < a.f

    def __eq__(self, a):
        if (self.position == a.position):
            return True
        else: 
            return False

    # Hash method for visited set
    def __hash__(self):              
        return hash(self.position)
        
       
def calculateEuclidean(current,goal):
    # Not incorporating sqrt function as computationally expensive
    return (((current.position[0] - goal.position[0]) ** 2) + ((current.position[1] - goal.position[1]) ** 2))

def calculateManhattan(current,goal):
    return (abs(current.position[0] - goal.position[0]) + abs(current.position[1] - goal.position[1]))

def astar(map, h):
    # Create and initialize start node
    start = (0,0)
    dim = len(map)-1
    end = (dim,dim)
    startNode = coordNode(None, start)
    startNode.f = 0
    startNode.g = 0
    startNode.h = 0

    # Create and initialize end node
    goalNode = coordNode(None, end)
    goalNode.f = 0
    goalNode.g = 0
    goalNode.h = 0


    # Initialize both priority queue and visited list of coord nodes
    pqueue = []
    # Initialiaing to set as makes algorithm more efficient
    visited = set()


    # Add the start node to priority queue with priority f
    heapq.heappush(pqueue, (startNode.f, startNode))

    # Loop until priority queue is empty as you have reached the end
    while len(pqueue) > 0:
        # Get the current coordNode
        (v,current_coordNode) = heapq.heappop(pqueue)
        # Pushing item back into priority queue
        heapq.heappush(pqueue,(v,current_coordNode))
        current_index = 0

        for index, (_,item) in enumerate(pqueue):
            if item.f < current_coordNode.f:
                current_coordNode = item
                current_index = index

      
        # Pop current off open list, add to closed list
        pqueue.pop(current_index)
        visited.add(current_coordNode)

        # Found the goalNode
        if current_coordNode.position == goalNode.position:
            path = []
            current = current_coordNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            ##print(len(pqueue))
            # Return reversed path
            return path[::-1] 

        # List of children nodes
        children = []

         # Adjacent cells
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # Get coordNode position
            coordNode_position = (current_coordNode.position[0] + new_position[0], current_coordNode.position[1] + new_position[1])

            # Make sure within range
            if coordNode_position[0] > (len(map) - 1) or coordNode_position[0] < 0 or coordNode_position[1] > (len(map[len(map)-1]) -1) or coordNode_position[1] < 0:
                continue

            # Make sure valid cells
            if map[coordNode_position[0]][coordNode_position[1]] != 0:
                continue

            # Create new coordNode
            new_coordNode = coordNode(current_coordNode, coordNode_position)

            # Appending to children list
            children.append(new_coordNode)

        # Loop through children list
        for child in children:
            # Child is on the closed list
            if child in visited:
                continue
            
            # Calculating g value
            child.g = current_coordNode.g + 1

            # Calculating heuristic h
            if (h == 1):
                # Using Euclidean distance for heuristic
                child.h = calculateEuclidean(child,goalNode)
            else:
                 # Using Manhattan distance for heuristic
                child.h = calculateManhattan(child,goalNode)
            
            # Calculating f value from g and h
            child.f = child.g + child.h

            # Child is already in the priority queue
            for (_,open_coordNode) in pqueue:
                if child.position == open_coordNode.position and child.g > open_coordNode.g:
                    continue

            # Add the child to the priority queue with priority f
            heapq.heappush(pqueue, (child.f, child))
            











  





















class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dfs(map):
    visited = [[0 for x in range(len(map))] for y in range(len(map))]
    stack = []
    path = []
    stack.append(Coordinates(0, 0))
    while (len(stack) > 0):
        curr = stack.pop()
        row = curr.x
        column = curr.y
        
        if (row < 0 or row >= len(map) or column < 0 or column >= len(map) or visited[row][column] == 1 or map[row][column] == 1):
            continue
        
        path.append(curr)
        visited[row][column] = 1
        if (map[row][column] == "G"):
            visited[row][column] = 1
            print("PATH FOUND FOR DFS: ")
            for curr in path:
                print(curr.x, curr.y)
            return
        if (has_neighbors(row, column, map, visited) == False):
            temp = path
            for curr in list(reversed(temp)):
                x = curr.x
                y = curr.y
                #print(x, y)
                #print(has_neighbors(x, y, map, visited))
                if (has_neighbors(x, y, map, visited) == False):
                    temp.pop()
                else:
                    break
            path = temp 

        '''
        if (row < 0 or row >= len(map) or column < 0 or column >= len(map) or visited[row][column] == 1 or map[row][column] == 1):
            path.pop()
            continue
        '''

        stack.append(Coordinates(row, column - 1))
        stack.append(Coordinates(row, column + 1))
        stack.append(Coordinates(row - 1, column)) 
        stack.append(Coordinates(row + 1, column))
    print("NO PATH FOUND FOR DFS")
    return

def has_neighbors(row, column, map, visited):
    if (row >= 0 and row < len(map) and column - 1 >= 0 and column - 1 < len(map) and visited[row][column - 1] == 0 and (map[row][column - 1] == 0 or map[row][column - 1] == "G") and map[row][column - 1] != "S"):
        return True
    elif (row >= 0 and row < len(map) and column + 1 >= 0 and column + 1 < len(map) and visited[row][column + 1] == 0 and (map[row][column + 1] == 0 or map[row][column + 1] == "G") and map[row][column + 1] != "S"):
        return True
    elif (row - 1 >= 0 and row - 1 < len(map) and column >= 0 and column < len(map) and visited[row - 1][column] == 0 and (map[row - 1][column] == 0 or map[row - 1][column] == "G") and map[row - 1][column] != "S"):
        return True
        
    elif (row + 1 >= 0 and row + 1 < len(map) and column >= 0 and column < len(map) and visited[row + 1][column] == 0 and (map[row + 1][column] == 0 or map[row + 1][column] == "G") and map[row + 1][column] != "S"):
        return True
    else:
        return False


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
            currgoalNode = queueG.pop(0)
            path.append(currgoalNode)
            rowG = currgoalNode.x
            columnG = currgoalNode.y
            if (rowG < 0 or rowG >= len(map) or columnG < 0 or columnG >= len(map) or visited[rowG][columnG] == 1 or map[rowG][columnG] == 1):
                path.pop()
            elif (map[rowG][columnG] == "S" or check_bi_bfs(currgoalNode, queueS)):
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










# map = [["S", 0, 0], [0,1,0], [0,1,"G"]]
# bidirectional_bfs(map)
# dfs(map)
# bfs(map)