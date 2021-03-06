import sys
import gameLib as game
estTime = 0
#0:midgame 1:endgame
# stepW = 0
# stepB = 0
def checkStep(board):
    numW,numB = 0,0
    for b in board:
        if b == 'W':
            numW+=1
        elif b == 'B':
            numB+=1
    #endgame
    if numB == 3 and numW == 3:return 3
    elif numW == 3:return 1
    elif numB == 3:return 2
    else: return 0


def static(board):#flag: 0 white 1 black
    global estTime
    numW,numB = 0,0
    for b in board:
        if b == 'W':
            numW+=1
        elif b == 'B':
            numB+=1
    estTime+=1
    if numB<=2: return 10000
    if numW<=2: return -10000
    inv = game.getInverse(board)
    if numB==3:
        moves = len(game.generateHopping(inv))
    else:
        moves = len(game.generateMove(inv))
    #print(1000*(numW-numB)-moves,numW,numB,moves)
    return 1000*(numW-numB)-moves

#============================Midgame
def MidMaxMin(board,depth):#white turn
    game.change(board)
    if depth==0: 
        return [static(board),board,board]
    flag = checkStep(board)
    if flag==1 or flag==3:
        return EndMaxMin(board,depth)
    
    positions = game.generateMove(board)
    if not positions:
        return [-10000,board,board]
    else:
        v = [-float('inf'),None,None]
        for pos in positions:
            v = max(v,MidMinMax(pos,depth-1)[:-1]+[pos],key = lambda x:x[0])
        return v
def MidMinMax(board,depth):#black turn
    if depth==0:
         return [static(board),board,board]
    flag = checkStep(board)
    if flag==2 or flag==3:
        return EndMinMax(board,depth)

    inv = game.getInverse(board)

    positions = game.generateMove(inv)
    if not positions:
        return [10000,board,board]
    else:
        v = [float('inf'),None,None]
        for pos in positions:
            v = min(v,MidMaxMin(pos,depth-1)[:-1]+[pos],key = lambda x:x[0])
        return v
#============================Endgame
def EndMaxMin(board,depth):#white turn
    score = static(board)
    if abs(score)==10000: return [score,board,board]
    positions = game.generateHopping(board)

    if not positions:
        return [-10000,board,board]
    else:
        v = [-float('inf'),None,None]
        for pos in positions:
            v = max(v,MidMinMax(pos,depth-1)[:-1]+[pos],key = lambda x:x[0])
        return v

def EndMinMax(board,depth):#black turn
    score = static(board)
    if abs(score)==10000: return [score,board,board]
    inv = game.getInverse(board)
    positions = game.generateHopping(inv)

    if not positions: 
        return [10000,board,board]
    else:
        v = [float('inf'),None,None]
        for pos in positions:
            v = min(v,MidMaxMin(pos,depth-1)[:-1]+[pos],key = lambda x:x[0])
        return v



if __name__ == "__main__":
    if len(sys.argv)!=4:
        sys.argv = [sys.argv[0],"test1.txt", "board4.txt", "3"]
    print(sys.argv)
    depth = int(sys.argv[3])
    board = game.readBoard(sys.argv[1])
    res = MidMaxMin(game.getInverse(board),depth)
    game.writeBoard(res[-1],sys.argv[2])

    print("Board Position:",''.join(res[-1]))
    print("Position evaluated by static estimation:",estTime)
    print("MINIMAX esitmate:", res[0])
    #game.show(board)
    #game.show(res[-1])
    #game.show(res[1])
