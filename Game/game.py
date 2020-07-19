import sys
import gameLib as game
import ABGame
import ABOpening

# 20      21        22
#   17    18    19 
#      14 15 16
# 8  9 10    11 12  13
#       6     7
#    3     4     5
# 0        1         2


def available(board):
    loc1 = []
    loc2 = []
    for i in range(23):
        if board[i]=='B':
            loc1.append(i)
            for j in game.neighbors(i):
                if board[j]=='x':
                    loc2.append(j)
    return [loc1,set(loc2)]

def candidate(board,loc):
    locations = []
    if board[loc]=='B':
        for j in game.neighbors(loc):
            if board[j]=='x':
                locations.append(j)
    return locations


if __name__ == "__main__":
    print("enter difficulty (1~4)")
    depth = int(input())
    board = ['x' for _ in range(23)]
    score = 0
    print("opening game")
    for _ in range(9):
        print("AI turn",score)
        res = ABOpening.MaxMin(game.getInverse(board),depth,-float('inf'),float('inf'))
        score = ABOpening.static(board)
        board = res[-1]
        game.show(board)
        print("Your turn",score)
        loc = int(input())
        board[loc] = 'B'
        game.show(board)
        if game.closeMill(loc,board,turn='B'):
            print("Pick the location to remove")
            loc = int(input())
            board[loc] = 'x'
        score = ABOpening.static(board)
        game.show(board)
    

    #board = game.readBoard("board3.txt")
    print("mid game")
    while abs(score)!=10000:
        print("AI turn",score)
        res = ABGame.MidMaxMin(game.getInverse(board),depth,-float('inf'),float('inf'))
        score = ABGame.static(board)
        board = res[-1]
        game.show(board)
        print("Your turn",score)
        print("Choose loc from : ", available(board))
        print("From",end=' ')
        loc = int(input())
        candidate(board,loc)
        print("to", end=' ' )
        to = int(input())

        board[loc] = 'x'
        board[to] = 'B'
        game.show(board)
        if game.closeMill(to,board,turn='B'):
            print("Pick the location to remove")
            loc = int(input())
            board[loc] = 'x'
        score = ABGame.static(board)
        game.show(board)
        

    print(score)
