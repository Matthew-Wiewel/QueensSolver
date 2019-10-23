# QueensSolver

The 8-Queens problem is to find a way to place 8 queens on a chess board such that none of the queens are attacking each other. This program uses an algorithm to solve the problem in Python.

findQueensAll is the first function used to solve the problem. It approaches the problem with a depth-first-search method, placing one queen on each file and finding a good place where it is not attacked before moving to the next file. If a queen cannot find a safe space in its file, it will back up and adjust preceding queens. This function will find all possible solutions. Do not use this for large values of N if just finding 1 solution is your goal.

findQueensDFS is logically the same as findQueensAll given its depth-first traversal, but instead of finding all solutions it only finds 1.

More methods of traversal coming up
