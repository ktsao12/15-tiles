"""
Kevin Tsao
15 Tile Puzzle Solver

By default, the program uses a medium-difficulty board. It also
has an option to use a randomly-generated board, with a function
that uses proof by inversions to check if these boards are
solvable. However, this is not advised as high difficulty boards
require a very long amount of time to solve.
"""
import time
import math
from random import shuffle

""" A simple function that prints out the board. """
def display(list):
    print("---------------------")
    print("| %-2i | %-2i | %-2i | %-2i |"
          % (list[0], list[1], list[2], list[3]))
    print("---------------------")
    print("| %-2i | %-2i | %-2i | %-2i |"
          % (list[4], list[5], list[6], list[7]))
    print("---------------------")
    print("| %-2i | %-2i | %-2i | %-2i |"
          % (list[8], list[9], list[10], list[11]))
    print("---------------------")
    print("| %-2i | %-2i | %-2i | %-2i |"
          % (list[12], list[13], list[14], list[15]))
    print("---------------------")

    """
    A function that uses proof by inversion to check if a
    given puzzle can be solved. This assumes that the goal
    state has the blank tile in the bottom right corner. It
    uses loops to count the amount of lesser tiles on the
    board for each tile, then checks to see if the total
    count is an odd number.
    """
def checkSolvable(board):
    count = 0
    for i in range(0, 15):
        for j in range(i + 1, 16):
            if board[i] > board[j]:
                count += 1
    if (count % 2) == 0:
        return 0
    return 1

    """
    The BFS function. This function creates a tree of sorts
    by creating a list of lists, each inner list being a
    possible board state, and then traversing the outer list
    and checking each inner list to see if any of them are the
    victory board state. If not, each possible move of each of
    those states are appended to the outer list.
    """
def solverBFS(board):
    exploredStates = []
    visitedStates = 0
    current = [board]
    i = 0
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    while True:
        # Iterate through outer list to check each board state
        result = current[i]
        # If current state is goal, end immediately
        if result == goal:
            break
        # If current state has been explored already, skip
        if result in exploredStates:
            i += 1
            continue
        # Check all possible branching states of current state
        for j in findPaths(result):
            if j in exploredStates:
                continue
            current.append(j)
        exploredStates.append(result)
        visitedStates += 1
    print("Puzzle was successfully solved.")
    print("Amount of states explored: ", visitedStates)
    return current[i]

    """
    A simple function that takes in a board state and then finds
    all possible moves from that state. Checks for collision with
    walls of the board by doing simple index checks. Each board
    state resulting from a possible move is appended to a list of
    lists and returned.
    """
def findPaths(start):
    branches = []
    grid = start
    i = grid.index(0)
    if i > 3:
        moveUp(grid, i)
        branches.append(list(grid))
        moveUp(grid, i)
    if (i != 3) & (i != 7) & (i != 11) & (i != 15):
        moveRight(grid, i)
        branches.append(list(grid))
        moveRight(grid, i)
    if i < 12:
        moveDown(grid, i)
        branches.append(list(grid))
        moveDown(grid, i)
    if (i != 0) & (i != 4) & (i != 8) & (i != 12):
        moveLeft(grid, i)
        branches.append(list(grid))
        moveLeft(grid, i)
    return branches

    """ Four helper functions that perform "moves" on the board."""
def moveUp(state, zero):
    temp = state[zero - 4]
    state[zero - 4] = state[zero]
    state[zero] = temp
    return state

def moveRight(state, zero):
    temp = state[zero + 1]
    state[zero + 1] = state[zero]
    state[zero] = temp
    return state

def moveDown(state, zero):
    temp = state[zero + 4]
    state[zero + 4] = state[zero]
    state[zero] = temp
    return state

def moveLeft(state, zero):
    temp = state[zero - 1]
    state[zero - 1] = state[zero]
    state[zero] = temp
    return state

    """
    The iterative deepening depth-first search solver. This two-function
    solution steps through possible states with a constrained depth in an
    attempt to find the solution state. With each iteration, the amount of
    depth traveled by the solver increases. Thus starting from the initial
    board, the solver will run through possible moves and the children of
    those moves in an endless loop.
    """
def solverDFS(board):
    i = 0
    while True:
        result = DFS(board, i)
        if result is not None:
            print("Puzzle was successfully solved.")
            print("Depth reached was: ", i)
            return result
        i += 1

def DFS(node, depth):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    if depth == 0 and node == goal:
        return node
    elif depth > 0:
        # For each neighbor of current path, dive with a reduced depth
        for i in findPaths(node):
            result = DFS(i, depth - 1)
            if result is not None:
                return result
    return None

    """
    A pair of heuristic functions for the A* Search algorithm. The first
    counts the number of displaced tiles, and the second calculates the
    Manhattan Distance of the board, which is the distance each tile is
    from its goal position. The displacement algorithm just uses a simple
    loop to check each position against the tile at that position since my
    representation of the board is a simple list. The Manhattan Distance
    algorithm converts the list into a two-dimensional list to represent a
    grid, then computes the goal x and y coordinates of each tile and
    checks the tile against that goal.
    """
def heuristicOne(board):
    count = 0
    for i in range(0, 16):
        if i != 15:
            if i != (board[i]) + 1:
                count += 1
        else:
            if 0 != (board[i]) + 1:
                count += 1
    return count

def heuristicTwo(board):
    grid = [[], [], [], []]
    for x in range(0, 16):
        if x < 4:
            grid[0].append(board[x])
        elif 3 < x < 8:
            grid[1].append(board[x])
        elif 7 < x < 12:
            grid[2].append(board[x])
        else:
            grid[3].append(board[x])
    count = 0
    for i in range(4):
        for j in range(4):
            value = grid[i][j]
            if value != 0:
                x = math.floor((value - 1) / 4)
                y = math.floor((value - 1) % 4)
                dx = abs(i - x)
                dy = abs(j - y)
                count += dx + dy
    return count

    """
    The A* search algorithm. This sophisticated method is a "best"
    first search algorithm that uses a heuristic as a way of
    finding the best possible branching state from any current
    state. By computing this for every neighbor of every state that
    is visited, the algorithm builds a best possible path once a
    solution is found. By not wasting time checking suboptimal paths
    or revisiting previously explored paths, this algorithm also
    achieves great performance.
    """
def solverAStar(board):
    exploredStates = []
    visitedStates = 0
    current = [board]
    i = 0
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    while True:
        # Iterate through outer list to check each board state
        result = current[i]
        # If current state is goal, end immediately
        if result == goal:
            break
        # If current state has been explored already, skip
        if result in exploredStates:
            i += 1
            continue
        # Check all possible branching states of current state
        for j in findPaths(result):
            if j in exploredStates:
                continue
        # If new path is not better than current state, skip
        # Change heuristicTwo to heuristicOne to use displacement
            if heuristicTwo(result) <= heuristicTwo(j):
                continue
            current.append(j)
        exploredStates.append(result)
        visitedStates += 1
    print("Puzzle was successfully solved.")
    print("Amount of states explored: ", visitedStates)
    return current[i]

def main():
    print("CS411 - Homework #6")
    print("Kevin Tsao / ktsao5")
    print("15 Tile Puzzle Solver")
    mode = input("Press 1 to use default board, or 2 for random board: ")
    board = []
    if (mode == '1'):
        #board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
        board = [1, 3, 4, 8, 5, 2, 6, 11, 9, 14, 10, 7, 13, 0, 15, 12]
    elif (mode == '2'):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        shuffle(board)
        while checkSolvable(board) != 1:
            shuffle(board)
    print("\nStarting board is:")
    display(board)
    one = "Press 1 to use Breadth-First Search, "
    two = "or 2 to use Iterative Deepening Depth-First Search, "
    three = "or 3 to use A* Search, or 4 to use all three: "
    string = one + two + three
    mode = input(string)
    if (mode == '1'):
        start = time.time()
        solverBFS(board)
        print("Amount of time taken was: %s seconds." % (time.time() - start))
    elif (mode == '2'):
        start = time.time()
        solverDFS(board)
        print("Amount of time taken was: %s seconds." % (time.time() - start))
    elif (mode == '3'):
        start = time.time()
        solverAStar(board)
        print("Amount of time taken was: %s seconds." % (time.time() - start))
    elif (mode == '4'):
        start = time.time()
        print("\nFirst using Breadth-First Search...")
        result = solverBFS(board)
        BFStime = time.time() - start
        start = time.time()
        print("Now using Iterative Deepening Depth-First Search...")
        solverDFS(board)
        DFStime = time.time() - start
        start = time.time()
        print("Finally using A* Search...")
        solverAStar(board)
        AStime = time.time() - start
        print("Final board is:")
        display(result)
        print("Time taken by each algorithm was as follows:")
        print("  BFS: ", BFStime, "seconds")
        print("IDDFS: ", DFStime, "seconds")
        print("   A*: ", AStime, "seconds")
    
if __name__ == "__main__":
    main()
