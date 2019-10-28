"""
With the standard 8x8 chess board
Files A - H are 0-7
Ranks 1-8 are 0-7
"""
#define some constants to be used to avoid magic numbers
#to change the NxN board size, change NumRanksAndFile to the desired N
import time
from typing import List
QUEEN: int = 1
EMPTY: int = 0
AFILE: int = 0
RANK1: int = 0
NumRanksandFiles: int = 8
HFILE: int = NumRanksandFiles - 1
RANK8: int = NumRanksandFiles - 1


def numToRealFileAndRank(rank: int, file: int) -> str:
    """
    Takes the underlying representations of files and ranks and
    coverts them to the standard notation. ie 0,3 to A4
    """
    realFile = (chr)(65 + file) #convert file to A-H
    realRank = 1 + rank # convert rank to 1-8
    return realFile + str(realRank) + ' ' # return the board position

def isValid(board, startRank: int, startFile: int) -> bool:
    """
    This function checks whether or not a queen is placed on a 
    valid square of the chess board.
    The reason it only checks only for queens in one direction is because
    same file attacks are negated by the way queens are placed with each call
    being a separate file. In addition to that, when a queen is placed, there are
    no queens to its right on the board so that region is clear. Therefore only
    the left diagonals and rank needs to be checked as those are the only avenues
    for a potential attack on the queen.
    """
    #check to the left of the queen first
    for f in range(startFile):
        if board[startRank][f] == QUEEN:
            return False #found a queen that can attack, not a good square
    
    #now to check the lower left diagonal
    diagFile: int = startFile - 1
    diagRank: int = startRank - 1
    while diagFile >= AFILE and diagRank >= RANK1:
        if board[diagRank][diagFile] == QUEEN:
            return False
        #now prepare for next iteration
        diagFile -= 1
        diagRank -= 1
    
    #now to check upper left diagonal
    diagFile = startFile - 1
    diagRank = startRank + 1
    while diagFile >= AFILE and diagRank <= RANK8:
        if board[diagRank][diagFile] == QUEEN:
            return False
        #then prepare for next iteration  
        diagFile -= 1
        diagRank += 1
    
    #if we made it through the three checks, then the queen is in a valid place
    return True

def printSolution(board: List[List[int]]) -> None:
    listOfPositions = ''# initialize an empty list
    #go through the board by file
    for f in range(NumRanksandFiles):
        for r in range(NumRanksandFiles):
            if(board[r][f] == QUEEN):
                listOfPositions += numToRealFileAndRank(r,f) #add position to solution
                r = NumRanksandFiles #end the search for a queen in this file
    print(listOfPositions) #print out the solution

def findQueensAll(board: List[List[int]], file: int = AFILE) -> None:
    """
    This is a function to find locations for 8 queens on a chess board such that
    no queen is being attacked by another queen. It will use a depth-first method,
    hence being labelled a slow version. 
    """
    #when placing queens, we will start by placing them on the first rank in the file
    rank = RANK1

    # emulate a do while to place queens and make recursive calls
    while True:

        #place a queen on the board in this file
        board[rank][file] = QUEEN

        if isValid(board, rank, file): #we have a valid position so we'll either make a call or print a solution
            if file < HFILE: #we have a valid queen but haven't placed 8 yet so go to the next file
                findQueensAll(board, file + 1)
            else: # file must equal the H-File and we have 8 queens on the board so let's print a solution
                printSolution(board)
        
        board[rank][file] = EMPTY # now that we went through that position, clear queen before trying next position
        rank += 1 #advance rank for next iteration

        if rank > RANK8: # we are out of bounds for this file, so return to previous
            return

def findQueensDFS(board: List[List[int]], file: int = AFILE) -> bool:
    """
    This function finds 1 solution for the board using a DFS search
    """

    rank: int = RANK1 # when placing queens, start by placing them on the first rank in the file
    haveFoundSolution: bool = False # used to note if we have found a solutuion

    # do-while we have not found a soluiton
    while not haveFoundSolution:

        #place queen in this square
        board[rank][file] = QUEEN

        if isValid(board, rank, file): # if it's a valid board, we either have a solution or can go deeper in DFS
            if file < HFILE: # the case where we have not yet placed all N queens, recurse
                haveFoundSolution = findQueensDFS(board, file +1)
            else: #we've got a solution, so print it and return True because we've found a solution
                printSolution(board)
                return True
        
        #clear our bad queen and get ready to place on in the next rank
        board[rank][file] = EMPTY
        rank += 1

        # if we've exceeded the bounds of the board or we've found a solution, let's return
        if rank > RANK8 or haveFoundSolution:
            return haveFoundSolution

# if we've got a relatively small N, then we'll find all the solutions
# otherwise it may take some time to run. N=11 take a couple second, N=12 takes a little less than half a minute, N=13 takes a couple minutes
# and my personal preference when using this program is to not take long on this part        
if NumRanksandFiles < 12:
    board = [ [EMPTY for file in range(NumRanksandFiles)] for rank in range(NumRanksandFiles) ]
    print("Finding all solutions to the board with DFS")
    findQueensAll(board)

board: List[List[int]] = [ [EMPTY for file in range(NumRanksandFiles)] for rank in range(NumRanksandFiles)]
print("Finding one solution to the board with DFS")
startTime = time.process_time()
findQueensDFS(board)
endTime = time.process_time()
print("Time taken: ", endTime - startTime)