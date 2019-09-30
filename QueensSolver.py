"""
idea of findQueens func
will place a queen as far to the top as it can, going down each file until getting a solution
base case will be if going to the I file to stop
each time it returns to the caller, the caller should call it again down one more rank, until trying to place a queen on the 9th rank
//scratch this: should return a string of locations for the queens (maybe an array of ints or whatnot)
will need to pass a board to each call
queens can be represented either by a 1 (with blanks being a 0) or an enum
when placing a queen, it should check whether or not that space is valid (moving down)
if it cannot find a valid placement for the queen, it should remove the queen and return to the calling instance
the calling instance should then move one down and re-call the next file

what do I need in the parameters:
1. a board
2. the knowledge of which file I'm placing queens into
3. knowledge of which ranks I've tried before

what do I need to return
1. whether or not I was successful

what do I need to do to give a person the result
1. If I have successfully placed a queen on the H file (assuming I start at A), I print out the locations of the queens

how can I make recursive calls
1. we know there is a solution. the call from the A file should NEVER return until a solution is found
but a call from file b - h may exhaust all possible ranks, so those should be able to return.
2. So when a caller moves down one rank (or more if needed) it should reset the rank its callee starts on

working prototype

bool findQueens(board, start rank, file)
{
    place queen on start rank, check if this is okay
    if not, keep going down a rank until finding an okay position
    
    call findQueens(board, start rank = 0, file + 1)
    while the call returns false, move down
    but if file becomes 8 (assuming 0-7 is valid) then return

    if all queens are on board (successful placement in fil = 7, 0-7 are the files)
    locations of the queens (may want a fancy schmancy function for this)
}

for checking the board, working prototype
bool checkBoard(board, position to check from)
{
    //no need to check up/down or right as the function takes care of those

    if there is a queen in the left up diagonal, return false
    if there is a queen in the same rank, return false
    if there is a queen in the left down diagonal, return false
    otherwise return true
}
"""

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
    #go through the board
    for r in range(8):
        for f in range(8):
            if(board[r][f] == QUEEN):
                listOfPositions += numToRealFileAndRank(f,r) #add position to solution
                f = 8 #end the search for a queen in this rank
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
        
        # your issue is that when you return, you don't clear the previous queen
        # so instead of moving the queen down one on a return, you're just adding
        # a new one to the file.

board = [ [EMPTY for file in range(8)] for rank in range(8) ]
findQueensSlow(board)