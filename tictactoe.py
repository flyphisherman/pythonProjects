# Basic Tic Tac Toe Game
# Author: FlyPhisherMan Zach
# Date Created: 8/11/2019

def printBoard():
    rowCount = 0
    for row in boardArray:
        columnCount = 0
        if rowCount == 0:
            print("   1   2   3")
            print("A  ", end='')
        elif rowCount == 1:
            print("   -   -   -")
            print("B  ", end='')
        elif rowCount == 2:
            print("   -   -   -")
            print("C  ", end='')
        else:
            print("[!] Error: printBoard function")
        for column in row:
            print(column, end='')
            if columnCount < 2:
                print(' | ', end='')
            columnCount += 1
        print("")
        rowCount += 1

def playPiece(piece, playerPiece):
    pieceRow = piece[0].upper()
    if pieceRow == 'A':
        if boardArray[0][int(piece[1]) - 1] == " ":
            boardArray[0][int(piece[1]) - 1] = playerPiece
            return True
        else:
            print("[!] There is already a piece there.  Please try again")
            return False
    elif pieceRow == 'B':
        if boardArray[1][int(piece[1]) - 1] == " ":
            boardArray[1][int(piece[1]) - 1] = playerPiece
            return True
        else:
            print("[!] There is already a piece there.  Please try again")
            return False
    elif pieceRow == 'C':
        if boardArray[2][int(piece[1]) - 1] == " ":
            boardArray[2][int(piece[1]) - 1] = playerPiece
            return True
        else:
            print("[!] There is already a piece there.  Please try again")
            return False
    else:
        print("[!] Error: Invalid location on the board")
        print("[*] Please use the letter of the row followed by the number of the column")
        return False

def printRules():
    print("""Each player takes turns placing a piece.
The goal is to place three of your piece in a row: horizontally, veritcally or diagonally.
Place the piece by using the letter of the row and the number of the column eg. 'A1'
""")

def winnerPresent():
    if (boardArray[0][0] == " " and boardArray[1][1] == " " and boardArray[2][2] == " "):
        return False, "NA"
    if (boardArray[0][0] != " "):
        if (boardArray[0][0] == boardArray[0][1]):
            if (boardArray[0][0] == boardArray[0][2]):
                return True, boardArray[0][0]
        elif (boardArray[0][0] == boardArray[1][1]):
            if (boardArray[0][0] == boardArray[2][2]):
                return True, boardArray[0][0]
        elif (boardArray[0][0] == boardArray[1][0]):
            if (boardArray[0][0] == boardArray[2][0]):
                return True, boardArray[0][0]
    if (boardArray[1][0] != " "):
        if (boardArray[1][0] == boardArray[1][1]):
            if (boardArray[1][0] == boardArray[1][2]):
                return True, boardArray[1][0]
    if (boardArray[2][0] != " "):
        if (boardArray[2][0] == boardArray[2][1]):
            if (boardArray[2][0] == boardArray[2][2]):
                return True, boardArray[2][0]
    if (boardArray[0][1] != " "):
        if (boardArray[0][1] == boardArray[1][1]):
            if (boardArray[0][1] == boardArray[2][1]):
                return True, boardArray[0][1]
    if (boardArray[2][0] != " "):
        if (boardArray[0][2] == boardArray[1][2]):
            if (boardArray[0][2] == boardArray[2][2]):
                return True, boardArray[0][2]
        elif (boardArray[0][2] == boardArray[1][1]):
            if (boardArray[0][2] == boardArray[2][0]):
                return True, boardArray[0][2]
    stalemate = False
    for row in boardArray:
        if " " not in row:
            stalemate = True
        else:
            stalemate = False
    if stalemate:
        return True, "NA"
    else:
        return False, "NA"

boardArray = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player1 = input("Please enter the name for Player 1: ")
player2 = input("Please enter the name for Player 2: ")

player1Piece = input("%s please choose which piece you would like (X or O): " % (player1))
while player1Piece != 'X' and player1Piece != 'O':
    print("Oops! You need to choose X or O")
    player1Piece = input("%s please choose which piece you would like (X or O): " % (player1))

if player1Piece == 'X':
    player2Piece = 'O'
else:
    player2Piece = 'X'

print(" ")
printRules()

print("The board:")
winnerStatus = False
playerNumber = 1
while not winnerStatus:
    print(" ")
    printBoard()
    piecePlacement = input("Please enter the place you want to put your piece: ")
    if ((playerNumber % 2) == 0):
        returnValue = playPiece(piecePlacement, "O")
        while (not returnValue):
            piecePlacement = input("Please enter the place you want to put your piece: ")
            returnValue = playPiece(piecePlacement, "O")
    else:
        returnValue = playPiece(piecePlacement, "X")
        while (not returnValue):
            piecePlacement = input("Please enter the place you want to put your piece: ")
            returnValue = playPiece(piecePlacement, "X")
    playerNumber += 1
    winnerStatus, winnerPlayer = winnerPresent()
print(" ")
printBoard()
if (winnerPlayer == player1Piece):
    print("The winner is: %s" % player1)
elif (winnerPlayer == player2Piece):
    print("The winner is: %s" % player2)
else:
    print("It is a stalemate")




