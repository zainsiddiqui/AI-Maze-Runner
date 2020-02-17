import heapq
import math

# Coordnode class
class coordNode():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, a):
        return self.f < a.f

    # Comparing nodes
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
    return ((current.position[0] - goal.position[0]) ** 2) + ((current.position[1] - goal.position[1]) ** 2)

def calculateManhattan(current,goal):
    return (abs(current.position[0] - goal.position[0]) + abs(current.position[1] - goal.position[1]))


def astar(map,h):
    h = int(h)
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
    visited = []


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
        visited.append(current_coordNode)

        # Found the goalNode
        if current_coordNode.position == goalNode.position:
            path = []
            current = current_coordNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            ##print(len(pqueue))
            # Return reversed path
            return [path[::-1], len(visited), map]

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
    return None
            

# Object used for coordinates for dfs, bfs, bi-bfs
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Helper function that will take in a path of coordinate objects and return a list of tuples
# The list of tuples will contain the path that an algorithm takes
def pathList(path):
    temp = []
    for curr in path:
        temp.append(tuple((curr.x, curr.y)))
    return temp

# DFS
def dfs(map):
    # We start with a fringe size of 1 becuase we are at the orgin node
    maxFringeSize = 1
    # We create a 2D array to track our visited nodes
    visited = [[0 for x in range(len(map))] for y in range(len(map))]
    # Stack for neighbors and traversal
    stack = []
    # THis will store the path that the algorithm takes and will be what we return
    path = []
    # We append our origin becuase that is where our algorithm will work from
    stack.append(Coordinates(0, 0))
    # This while loop will terminate when DFS has no nodes to go to or operate on
    # Or it will return the path within the while loop
    while (len(stack) > 0):
        # we recopmute the max fringe size after addign neighbors
        maxFringeSize = max(maxFringeSize, len(stack))
        # store the values of the current node into variables
        curr = stack.pop()
        row = curr.x
        column = curr.y
        # if the current node is already visited, blocked, or is not a valid coordinate then we just continue and don;t operate on the node 
        if (row < 0 or row >= len(map) or column < 0 or column >= len(map) or visited[row][column] == 1 or map[row][column] == 1):
            continue
        
        # since the node is worth operating on we put it into our path and set it as visited
        path.append(curr)
        visited[row][column] = 1
        # if we reach the goal node: add it to visited then return the final path 
        if (map[row][column] == "G"):
            visited[row][column] = 1
            result = pathList(path)
            return [result, maxFringeSize, map]
        # This if statement is crucial: if we reach a deadend in DFS we must take out all the nodes in path 
        # until we reach a node where we can start exploring again
        # This make ssur ethat when we return path we wil return the true path the algorithm takes
        if (has_neighbors(row, column, map, visited) == False):
            temp = path
            for curr in list(reversed(temp)):
                x = curr.x
                y = curr.y
                if (has_neighbors(x, y, map, visited) == False):
                    temp.pop()
                else:
                    break
            path = temp 
        # We append all neighbors, if any are invalid our ealrier if statement will check that for next iterations
        stack.append(Coordinates(row, column - 1))
        stack.append(Coordinates(row, column + 1))
        stack.append(Coordinates(row - 1, column)) 
        stack.append(Coordinates(row + 1, column))
    # If we exit the while loop without returning the path we know that there isn;t a valid one
    return
# This helper method will simply tell us if a specified node has any neighbors thta we can explore
# If it returns false then we no we have reached a dead end 
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

# BFS
def bfs(map):
    # 2D array to keep track of visited nodes
    visited = [[0 for x in range(len(map))] for y in range(len(map))]
    # Dictionary that will help with constructing the final path
    children = {}
    # A lsit to mimic a queue for BFS
    queue = []
    # The return list that will be our true path
    path = []
    # We add the origin to the queue and start operating on it first
    queue.append(Coordinates(0, 0))
    # This while loop with terminate when we have no nodes in the queue to operate on
    while (len(queue) > 0):
        # Get the first element in the queue and save its properties in variables
        curr = queue.pop(0)
        path.append(curr)
        row = curr.x
        column = curr.y
        # If we have a node that has been visited, blocked, or is not a valid coordinate then we continue and dont operate on it
        if (row < 0 or row >= len(map) or column < 0 or column >= len(map) or visited[row][column] == 1 or map[row][column] == 1):
            continue
        # If we reach the goal: add to visited, then run our true path finder for BFS
        if (map[row][column] == "G"):
            visited[row][column] = "G"
            result = printBFS(path, children, map)
            result = pathList(result)
            return result
        # If not at goal: add to visisted, and add all valid neighbors to queue
        # For every neighbor add into "children" dictionary that its parent is current
        # This will later help us backtrack and return our true path
        else:
            visited[row][column] = 1
            if (checkValid(row, column - 1, visited, map)):
                queue.append(Coordinates(row, column - 1))
                children[Coordinates(row, column - 1)] = curr
            if (checkValid(row, column + 1, visited, map)):
                queue.append(Coordinates(row, column + 1))
                children[Coordinates(row, column + 1)] = curr
            if (checkValid(row - 1, column, visited, map)):
                queue.append(Coordinates(row - 1, column))
                children[Coordinates(row - 1, column)] = curr
            if (checkValid(row + 1, column, visited, map)):
                queue.append(Coordinates(row + 1, column))
                children[Coordinates(row + 1, column)] = curr 
    # return None if we don't find a path and we don't have any nodes in queue
    return

# Helper method that will help us print our true path
# We start at the goal node and go through out dictionary of children to get the parent of each node 
# This backtracking will eventually lead us back to the origin and give us the true path
# Then we reverse the backtracked nodes which will gives us a clear path from origin to goal as found by our BFS
def printBFS(path, children, map):
    final = []
    curr = Coordinates(len(map) - 1, len(map) - 1)
    while (curr.x != 0 or curr.y != 0):
        final.append(curr)
        for key, value in children.items():
            if (curr.x == key.x and curr.y == key.y):
                curr = children[key]
    final.append(Coordinates(0, 0))
    final.reverse()
    return final

# A helper method that is a variation of the above method that is used for bi-bfs
# We must specify the start position of where we are backtracing from based on which bfs path we are using
# Since we have two BFS running at the same time this is crucial for the true path to be returned
def printBFS2(path, children, map, node, terminator):
    final = []
    curr = Coordinates(node.x, node.y)
    while (curr.x != terminator.x or curr.y != terminator.y):
        final.append(curr)
        for key, value in children.items():
            if (curr.x == key.x and curr.y == key.y):
                curr = children[key]
    final.append(Coordinates(terminator.x, terminator.y))
    final.reverse()
    return final

# Helper function that checks if a node is valid, not blocked, and not visited already
def checkValid(row, column, visited, map):
    if (row < 0 or row >= len(map) or column < 0 or column >= len(map) or visited[row][column] == 1 or map[row][column] == 1):
        return False
    return True

# Helper fucntions that will tell us if a certain node already exists in a queue
def check_bi_bfs(curr, queue):
    for temp in queue:
        if (temp.x == curr.x and temp.y == curr.y):
            return True
    return False
def check_bi_bfs2(curr, queue):
    for temp in queue:
        if (temp.x == curr.x and temp.y == curr.y):
            return temp

# BI-DIRECTIONAL BFS
def bi_bfs(map):
    # 2D array for visited which will be used for both BFS paths
    visited = [[0 for x in range(len(map))] for y in range(len(map))]
    # A separate queue for the path starting from start and goal
    queueS = []
    queueG = []
    # Two final paths from start and goal bfs
    pathS = []
    pathG = []
    # Two children dictionaries to keep track of true path for each bfs being used
    childrenS = {}
    childrenG = {}
    # Add origins of each path to the respective queue
    queueS.append(Coordinates(0, 0))
    queueG.append(Coordinates(len(map) - 1, len(map) - 1))
    # Outer while loop makes sure both queues have nodes to operate on
    while (len(queueS) > 0 and len(queueG) > 0):
        # Operate on start queue
        if (len(queueS) > 0):
            # Store variables of the current node
            currStart = queueS.pop(0)
            pathS.append(currStart)
            rowS = currStart.x
            columnS = currStart.y
            # If the node is blocked, visited, or invalid then coninute and don't operate
            if (rowS < 0 or rowS >= len(map) or columnS < 0 or columnS >= len(map) or visited[rowS][columnS] == 1 or map[rowS][columnS] == 1):
                continue 
            # if we reach the goal then we know one of our paths has found a valid path  
            if (map[rowS][columnS] == "G"):
                visited[rowS][columnS] = "G"
                result = printBFS(pathS, childrenS, map)
                return result
            # check if the current node exists in the opposite paths queue which means we have a connection
            # If this is true then get an array of each path and find the true path for each
            # append the to together to create a full path 
            elif (check_bi_bfs(currStart, queueG)):
                node = check_bi_bfs2(currStart, queueG)
                final1 = []
                final1 = printBFS2(pathG, childrenG, map, node, Coordinates(len(map) - 1, len(map) - 1))
                final2 = printBFS2(pathS, childrenS, map, node, Coordinates(0, 0))
                final2.reverse()
                final2 = final2[1:]
                final = final1 + final2
                final.reverse()
                result = pathList(final)
                return result
            # add neighbors to respective queue, mark as visisted, and add that each neighbor has the current node as a parent in our chlidren dictionary
            else:
                visited[rowS][columnS] = 1
                if (checkValid(rowS, columnS - 1, visited, map)):
                    queueS.append(Coordinates(rowS, columnS - 1))
                    childrenS[Coordinates(rowS, columnS - 1)] = currStart
                if (checkValid(rowS, columnS + 1, visited, map)):
                    queueS.append(Coordinates(rowS, columnS + 1))
                    childrenS[Coordinates(rowS, columnS + 1)] = currStart
                if (checkValid(rowS - 1, columnS, visited, map)):
                    queueS.append(Coordinates(rowS - 1, columnS))
                    childrenS[Coordinates(rowS - 1, columnS)] = currStart
                if (checkValid(rowS + 1, columnS, visited, map)):
                    queueS.append(Coordinates(rowS + 1, columnS))
                    childrenS[Coordinates(rowS + 1, columnS)] = currStart 
        # DO THE SAME THING AS ABOVE IF STATMENT BUT FLIP IT FOR THE OTHER PATH
        # This path will start at the goal and perform the same operations
        if (len(queueG) > 0):
            currGoal = queueG.pop(0)
            pathG.append(currGoal)
            rowG = currGoal.x
            columnG = currGoal.y
            if (rowG < 0 or rowG >= len(map) or columnG < 0 or columnG >= len(map) or visited[rowG][columnG] == 1 or map[rowG][columnG] == 1):
                continue   
            if (map[rowG][columnG] == "S"):
                visited[rowG][columnG] = "S"
                result = printBFS(pathG, childrenG, map)
                result = pathList(result)
                return result
            elif (check_bi_bfs(currGoal, queueS)):
                node = check_bi_bfs2(currGoal, queueS)
                final1 = []
                final1 = printBFS2(pathS, childrenS, map, node, Coordinates(0, 0))
                final2 = printBFS2(pathG, childrenG, map, node, Coordinates(len(map) - 1, len(map) - 1))
                final2.reverse()
                final2 = final2[1:]
                final = final1 + final2
                result = pathList(final)
                return result
            else:
                visited[rowG][columnG] = 1
                if (checkValid(rowG, columnG - 1, visited, map)):
                    queueG.append(Coordinates(rowG, columnG - 1))
                    childrenG[Coordinates(rowG, columnG - 1)] = currGoal
                if (checkValid(rowG, columnG + 1, visited, map)):
                    queueG.append(Coordinates(rowG, columnG + 1))
                    childrenG[Coordinates(rowG, columnG + 1)] = currGoal
                if (checkValid(rowG - 1, columnG, visited, map)):
                    queueG.append(Coordinates(rowG - 1, columnG))
                    childrenG[Coordinates(rowG - 1, columnG)] = currGoal
                if (checkValid(rowG + 1, columnG, visited, map)):
                    queueG.append(Coordinates(rowG + 1, columnG))
                    childrenG[Coordinates(rowG + 1, columnG)] = currGoal 
    # No path found for bi-bfs
    return