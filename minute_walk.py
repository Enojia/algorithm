#/!bin/bash/python2

def isValidWalk(walk):
    board = [[0 for i in range(21)] for j in range(21)] ##creating a board
    
    xOrigin = xPlace = 10
    yOrigin = yPlace = 10

    ## main algo

    for command in walk:
        if command == "n":
            yPlace += 1
            board[xPlace][yPlace] = 1
            board[xPlace][yPlace-1] = 0
        elif command == "s":
            yPlace -= 1
            board[xPlace][yPlace] = 1
            board[xPlace][yPlace+1] = 0
        elif command == "e":
            xPlace += 1
            board[xPlace][yPlace] = 1
            board[xPlace-1][yPlace] = 0
        elif command == "w":
            xPlace -= 1
            board[xPlace][yPlace] = 1
            board[xPlace+1][yPlace]

    return board[10][10]==1

walk = ["w","w","w","w","w","e","e","e","e","s"]
print isValidWalk(walk)
