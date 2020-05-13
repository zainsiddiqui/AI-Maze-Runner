# AI-Maze-Runner
This program explores various Artificial Intelligence pathfinding algorithms, both in the traditional application of path
planning, and more abstractly in the construction and design of complex objects. The program generates a maze of a given density and runs an pathfinding algorithm on the maze. To see full detailed analysis, please view **Report.pdf** 

<p align="center">
<img align="center" img width="370" alt="Screen Shot 2020-05-13 at 7 43 24 PM" src="https://user-images.githubusercontent.com/39894720/81877068-29d67980-9552-11ea-82ad-5e68f3c99e10.png">
</p>

The algorithms implemented:

• **Depth-First Search**

• **Breadth-First Search**

•**A (star): where the heuristic is to estimate the distance remaining via the Euclidean Distance**

d((x1, y1),(x2, y2)) = sqrt((x1 − x2)^2 + (y1 − y2)^2)

•**A (star): where the heuristic is to estimate the distance remaining via the Manhattan Distance**

d((x1, y1),(x2, y2)) = |x1 − x2| + |y1 − y2|

• **Bi-Directional Breadth-First Search**

<p align="center">
  
<img width="377" alt="Screen Shot 2020-05-13 at 7 43 29 PM" src="https://user-images.githubusercontent.com/39894720/81877069-2cd16a00-9552-11ea-8a60-86982a2ab1b2.png">


<img width="302" alt="Screen Shot 2020-05-13 at 7 43 46 PM" src="https://user-images.githubusercontent.com/39894720/81877076-2fcc5a80-9552-11ea-879d-8b0a2678ebcd.png">


<img width="316" alt="Screen Shot 2020-05-13 at 7 43 53 PM" src="https://user-images.githubusercontent.com/39894720/81877081-32c74b00-9552-11ea-839f-888e1f786b45.png">
</p>
