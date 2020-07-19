import sys
import gameLib as game
estTime = 0

def static(board):
    global estTime
    numW,numB = 0,0
    for b in board:
        if b == 'W':
            numW+=1
        elif b == 'B':
            numB+=1
    estTime+=1
    return numW-numB

def MaxMin(board,depth):#white turn
    game.change(board)
    if depth==0: return [static(board),board,board]
    positions = game.generateAdd(board)
    if not positions:
        return (static(board),board,board)
    else:
        v = [-float('inf'),None,None]
        for pos in positions:
            v = max(v,MinMax(pos,depth-1)[:-1]+[pos],key = lambda x:x[0])
        return v


def MinMax(board,depth):#black turn
    if depth==0: return [static(board),board,board]
    inv = game.getInverse(board)
    positions = game.generateAdd(inv)
    if not positions:
        return (static(board),board,board)
    else:
        v = [float('inf'),None,None]
        for pos in positions:
            v = min(v,MaxMin(pos,depth-1)[:-1]+[pos],key = lambda x:x[0])
        return v

if __name__ == "__main__":
    if len(sys.argv)!=4:
        sys.argv = [sys.argv[0],"board1.txt", "board2.txt", "3"]
    print(sys.argv)
    depth = int(sys.argv[3])
    board = game.readBoard(sys.argv[1])

    res = MaxMin(game.getInverse(board),depth)
    game.writeBoard(res[-1],sys.argv[2])
    #print([ 'x' if val=='x' else (i,val) for i,val in enumerate(board)])
    #print([ 'x' if val=='x' else (i,val) for i,val in enumerate(res[1])])
    print("Board Position:",''.join(res[-1]))
    print("Position evaluated by static estimation:",estTime)
    print("MINIMAX esitmate:", res[0])
    #game.show(board)
    #game.show(res[-1])
    #game.show(res[1])

