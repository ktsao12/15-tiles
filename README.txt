Kevin Tsao
15 Tiles

Originally Homework #6: Informed Searches
for CS411: Artificial Intelligence
AI, search algorithms, Python

The purpose of this assignment was to solve any given 15-tile puzzle using a variety of methods and then compare their runtime performance. Three methods were chosen: breadth-first search, iterative deepening depth-first search, and A* with two heuristics - displacement and Manhattan distance. The program was written in three parts as follows:

Part 1:
This application uses an uninformed breadth-first search to solve a 15-tile puzzle. The board itself is abstracted as a list of integers, and then a list of lists is created that serves as a tree for the application. The program then checks every possible move by iterating through the outer list until it finds the solution state.

Part 2:
The second solver is an iterative deepening depth-first search. This search method uses two functions to step through each state and all possible branching states. With each iteration, the depth at which the solver will travel is increased until a solution is found.

Part 3:
The third solver is using the A* search algorithm. This method works by checking branching states and finding the optimal one using a specified heuristic. Then by choosing the "best" branch each time, eventually a solution is found that is composed of the best possible path. Because less time is wasted checking paths that are suboptimal or already visited, this algorithm is also quite fast. My program includes two heuristics available: a displacement formula, and a Manhattan Distance formula.