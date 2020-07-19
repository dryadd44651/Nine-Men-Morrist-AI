import sys
import gameLib as game
import MiniMaxGame




if __name__ == "__main__":
    if len(sys.argv)!=4:
        sys.argv = [sys.argv[0],"board3.txt", "board4.txt", "3"]
    print(sys.argv)
    depth = int(sys.argv[3])
    board = game.readBoard(sys.argv[1])

    # res = MiniMaxGame.MidMinMax(board,depth)
    
    res = MiniMaxGame.MidMaxMin(board,depth)
    res[1] = game.getInverse(res[1])
    res[-1] = game.getInverse(res[-1])

    
    
    game.writeBoard(res[-1],sys.argv[2])
    print("Board Position:",''.join(res[-1]))
    print("Position evaluated by static estimation:",MiniMaxGame.estTime)
    print("MINIMAX esitmate:", res[0])
    # game.show(board)
    # game.show(res[-1])
    # game.show(res[1])
