# AI-Maze-Runner
This program explores various Artificial Intelligence pathfinding algorithms, both in the traditional application of path
planning, and more abstractly in the construction and design of complex objects. The program generates a maze of a given density and runs an pathfinding algorithm on the maze.

The algorithms implemented:
• Depth-First Search

• Breadth-First Search

•A (star): where the heuristic is to estimate the distance remaining via the Euclidean Distance 
d((x1, y1),(x2, y2)) = sqrt((x1 − x2)^2 + (y1 − y2)^2)

•A (star): where the heuristic is to estimate the distance remaining via the Manhattan Distance
d((x1, y1),(x2, y2)) = |x1 − x2| + |y1 − y2|

• Bi-Directional Breadth-First Search
