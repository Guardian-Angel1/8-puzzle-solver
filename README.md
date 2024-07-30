# 8-puzzle-solver using A* Algorithm


This program is designed to solve the 8-puzzle, a sliding puzzle game consisting of a 3x3 grid with numbered tiles. The objective is to arrange the tiles in ascending order. To achieve this, the program employs the A* search algorithm, leveraging different heuristics to guide its search.

The implemented heuristics include:
Misplacd Tile Heuristic(Hamming Distance): Evaluates the number of tiles that are not in their correct positions.

Manhattan Distance Heuristic: Measures the total distance each tile is from its correct position, summing up the horizontal and vertical distances.

Manhattan Distance with Linear Conflict: Extends the traditional Manhattan Distance by considering additional conflicts arising from linear arrangements of tiles in the same row or column.


### Steps to run code:

Save all the 4 code files in the same folder and run main.py program





### Features


- Solves 8-puzzle instances using A* search.
- Implements different heuristics for A* search.
- Evaluates solvability of puzzle instances.
- Measures time taken and nodes removed from the frontier for each heuristic.



### Usage

The program generates random solvable instances of the 8-puzzle and solves them using A* search with different heuristics. The results, including the number of steps, time taken, and nodes removed from the frontier, are displayed at the end.


### Heuristics
- Missing Tile Heuristic
- Manhattan Distance Heuristic
- Manhattan Distance with Linear Conflict Heuristic



### Results


The program displays the number of steps, total time taken by each heuristic, and the number of nodes removed from the frontier for analysis
