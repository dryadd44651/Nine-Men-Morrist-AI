import sys
import gameLib as game
estTime = 0
#0:midgame 1:endgame
# stepW = 0
# stepB = 0
def static(board):
    global estTime
    numW,numB,offset = 0,0,0
    for i,b in enumerate(board):
        if b == 'W':
            numW+=1
        elif b == 'B':
            numB+=1
        else:# 'x'
            mills = game.Mills(i)
            for m in mills:
                if board[m[0]]=='W' and board[m[1]]=='W':offset+=0.4
                if board[m[0]]=='B' and board[m[1]]=='B':offset-=0.4
    estTime+=1
    return numW-numB+offset
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




#============================Midgame
def MidMaxMin(board,depth,a,b):#white turn
    game.change(board)
    if depth==0: 
        return [static(board),board,board]
    flag = checkStep(board)
    if flag==1 or flag==3:
        return EndMaxMin(board,depth,a,b)

    positions = game.generateMove(board)
    if depth==0 or not positions: 
        return [static(board),board,board]
    else:
        v = [-float('inf'),None,None]
        for pos in positions:
            v = max(v,MidMinMax(pos,depth-1,a,b)[:-1]+[pos],key = lambda x:x[0])
            if(v[0]>=b): return v
            else: a = max(v[0],a)
        return v
def MidMinMax(board,depth,a,b):#black turn
    if depth==0:
         return [static(board),board,board]
    flag = checkStep(board)
    if flag==2 or flag==3:
        return EndMinMax(board,depth,a,b)
    inv = game.getInverse(board)
    positions = game.generateMove(inv)
    
    if depth==0 or not positions:
         return [static(board),board,board]
    else:
        v = [float('inf'),None,None]
        for pos in positions:
            v = min(v,MidMaxMin(pos,depth-1,a,b)[:-1]+[pos],key = lambda x:x[0])
            if(v[0]<=a): return v
            else: b = min(v[0],b)
        return v
#============================Endgame
def EndMaxMin(board,depth,a,b):#white turn
    score = static(board)
    if abs(score)==10000: return [score,board,board]
    positions = game.generateHopping(board)

    if not positions:
        return [-10000,board,board]
    else:
        v = [-float('inf'),None,None]
        for pos in positions:
            v = max(v,MidMinMax(pos,depth-1,a,b)[:-1]+[pos],key = lambda x:x[0])
            if(v[0]>=b): return v
            else: a = max(v[0],a)
        return v

def EndMinMax(board,depth,a,b):#black turn
    score = static(board)
    if abs(score)==10000: return [score,board,board]
    inv = game.getInverse(board)
    positions = game.generateHopping(inv)

    if not positions: 
        return [10000,board,board]
    else:
        v = [float('inf'),None,None]
        for pos in positions:
            v = min(v,MidMaxMin(pos,depth-1,a,b)[:-1]+[pos],key = lambda x:x[0])
            if(v[0]<=a): return v
            else: b = min(v[0],b)
        return v



if __name__ == "__main__":
    if len(sys.argv)!=4:
        sys.argv = [sys.argv[0],"board3.txt", "board4.txt", "4"]
    print(sys.argv)
    depth = int(sys.argv[3])
    board = game.readBoard(sys.argv[1])
    res = MidMaxMin(game.getInverse(board),depth,-float('inf'),float('inf'))
    game.writeBoard(res[-1],sys.argv[2])
    # print([ 'x' if val=='x' else (i,val) for i,val in enumerate(board)])
    # print([ 'x' if val=='x' else (i,val) for i,val in enumerate(res[1])])
    print("Board Position:",''.join(res[-1]))
    print("Position evaluated by static estimation:",estTime)
    print("MINIMAX esitmate:", res[0])
    # game.show(board)
    # game.show(res[-1])
    # game.show(res[1])
