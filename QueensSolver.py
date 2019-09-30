"""
Files A - H are 0-7
Ranks 1-8 are 0-7
I will write a function to translate

Queens in the board will be represented with a 1
"""
#define some constants to be used to avoid magic numbers
QUEEN = 1
EMPTY = 0
AFILE = 0
HFILE = 7
RANK1 = 0
RANK8 = 7


def numToRealFileAndRank(rank, file):
    """
    Takes the underlying representations of files and ranks and
    coverts them to the standard notation. ie 0,3 to A4
    """
    realFile = (chr)(65 + file) #convert file to A-H
    realRank = 1 + rank # convert rank to 1-8
    return realFile + str(realRank) + ' ' # return the board position

def isValid(board, startRank, startFile):
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
    diagFile = startFile - 1
    diagRank = startRank - 1
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

def printSolution(board):
    listOfPositions = ' '
    NumRanksandFiles = 8
    #go through the board
    for f in range(NumRanksandFiles):
        for r in range(NumRanksandFiles):
            if(board[r][f] == QUEEN):
                listOfPositions += numToRealFileAndRank(r,f) #add position to solution
                r = 8 #end the search for a queen in this rank
    print(listOfPositions) #print out the solution

def findQueensSlow(board, file = AFILE):
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
                findQueensSlow(board, file + 1)
            else: # file must equal the H-File and we have 8 queens on the board so let's print a solution
                printSolution(board)
        
        board[rank][file] = EMPTY # now that we went through that position, clear queen before trying next position
        rank += 1 #advance rank for next iteration

        if rank > RANK8: # we are out of bounds for this file, so return to previous
            return

board = [ [EMPTY for file in range(8)] for rank in range(8) ]
findQueensSlow(board)