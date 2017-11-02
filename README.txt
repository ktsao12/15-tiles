Kevin Tsao
15 Tiles

Originally Homework #6: Informed Searches
for CS411: Artificial Intelligence with Professor Piotr J. Gmytrasiewicz
AI, search algorithms, Python

The purpose of this assignment was to solve any given 15-tile puzzle using a variety of methods and then compare their runtime performance. Three methods were chosen: breadth-first search, iterative deepening depth-first search, and A* with two heuristics - displacement and Manhattan distance. The program comes with a default board that is of medium difficulty and requires 13 moves, but it can also generate new boards if the user so requires.

The sliding tile puzzle is a classic puzzle that consists of a (N^2 - 1)# of numbered tiles and a blank tile, sometimes represented as an empty space and in this program represented as the number zero. The objective is to move the blank tile around until the grid fits a goal configuration. In the case of a 8-tile puzzle, the goal may be (from left to right, top to bottom) 1 2 3 4 5 6 7 8 0. Thus the first objective of this program is to solve the puzzle by attempting various moves until the board reaches the goal state. But because the 15-tile puzzle can require an inordinate amount of moves to solve, running with an inferior method may result in the process either running for an absurd amount of time, or running out of memory, hence the actual purpose of this program.

The program was written in three parts as follows:

Part 1:
This application uses an uninformed breadth-first search to solve a 15-tile puzzle. The board itself is abstracted as a list of integers, and then a list of lists is created that serves as a tree for the application. The program then checks every possible move by iterating through the outer list. If none of the immediate moves from the current board is the goal state, then all of those moves are appended to the list, and the solver then checks each possible move from every one of those moves. Thus, the tree grows at a geometric rate. It is not advised to run this solver with difficult boards as the runtime can quickly become extreme.

Part 2:
The second solver is an iterative deepening depth-first search. This search method uses two functions to step through each state and all possible branching states. With each iteration, the depth at which the solver will travel is increased until a solution is found. My solution uses a recursive function that calls itself by checks against the fixed depth, which increases with every iteration of the loop in my main function.

Part 3:
The third solver is using the A* search algorithm. This method works by checking branching states and finding the optimal one using a specified heuristic. Then by choosing the "best" branch each time, eventually a solution is found that is composed of the best possible path. Because less time is wasted checking paths that are suboptimal or already visited, this algorithm is also quite fast. My program includes two heuristics available: a displacement formula, and a Manhattan Distance formula.
