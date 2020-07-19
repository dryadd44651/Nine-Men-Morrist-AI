# commom lib
# 20      21        22
#   17    18    19 
#      14 15 16
# 8  9 10    11 12  13
#       6     7
#    3     4     5
# 0        1         2

def neighbors(loc):
    if loc==0:
        return [1,3,8]
    elif loc==1:
        return [0,4,2]
    elif loc==2:
        return [1,5,13]
    elif loc==3:
        return [0,4,6,9]
    elif loc==4:
        return [1,3,5]
    elif loc==5:
        return [2,4,7,12]
    elif loc==6:
        return [3,7,10]
    elif loc==7:
        return [6,5,11]
    elif loc==8:
        return [0,9,20]
    elif loc==9:
        return [3,8,10,17]
    elif loc==10:
        return [6,9,14]
    elif loc==11:
        return [7,12,16]
    elif loc==12:
        return [5,11,13,19]
    elif loc==13:
        return [2,12,22]
    elif loc==14:
        return [10,15,17]
    elif loc==15:
        return [14,16,18]
    elif loc==16:
        return [11,15,19]
    elif loc==17:
        return [9,14,18,20]
    elif loc==18:
        return [15,17,19,21]
    elif loc==19:
        return [12,16,18,22]
    elif loc==20:
        return [8,17,21]
    elif loc==21:
        return [18,20,22]
    elif loc==22:
        return [13,19,21]

# commom lib
# 20      21        22
#   17    18    19 
#      14 15 16
# 8  9 10    11 12  13
#       6     7
#    3     4     5
# 0        1         2

def closeMill(loc,board,turn='W'):
    #token = board[loc]
    return checkMills(loc,board,turn)

def checkMills(loc,board,turn):
    token=turn
    if(loc==0):
        if((board[1]==token and board[2]==token) or (board[3]==token and board[6]==token) or (board[8]==token and board[20]==token)):
            return True
        return False
    
    elif(loc==1):
        if(board[0]==token and board[2]==token):
            return True
        return False
    
    elif(loc==2):
        if((board[0]==token and board[1]==token) or (board[13]==token and board[22]==token) or (board[5]==token and board[7]==token)):
            return True
        return False
    
    elif(loc==3):
        if((board[0]==token and board[6]==token) or (board[4]==token and board[5]==token) or (board[9]==token and board[17]==token)):
            return True
        return False
    
    elif(loc==4):
        if(board[3]==token and board[5]==token):
            return True
        return False

    elif(loc==5):
        if((board[3]==token and board[4]==token)  or (board[12]==token and board[19]==token) or (board[2]==token and board[7]==token)):
            return True
        return False    
    
    elif(loc==6):
        if((board[0]==token and board[3]==token) or (board[10]==token and board[14]==token)):
            return True
        return False 
    
    elif(loc==7):
        if((board[2]==token and board[5]==token) or (board[11]==token and board[16]==token)):
            return True
        return False
    
    elif(loc==8):
        if((board[0]==token and board[20]==token) or (board[9]==token and board[10]==token)):
            return True
        return False
    
    elif(loc==9):
        if((board[8]==token and board[10]==token) or (board[3]==token and board[17]==token)):
            return True
        return False

    elif(loc==10):
        if((board[6]==token and board[14]==token)or (board[8]==token and board[9]==token)):
            return True
        return False 
    
    elif(loc==11):
        if((board[7]==token and board[16]==token) or (board[12]==token and board[13]==token)):
            return True
        return False
    
    elif(loc==12):
        if((board[11]==token and board[13]==token) or (board[5]==token and board[19]==token)):
            return True
        return False
    
    elif(loc==13):
        if((board[11]==token and board[12]==token) or (board[2]==token and board[22]==token)):
            return True
        return False    
    
    elif(loc==14):
        if((board[17]==token and board[20]==token) or (board[15]==token and board[16]==token) or (board[6]==token and board[10]==token)):
            return True
        return False 
    
    elif(loc==15):
        if((board[14]==token and board[16]==token) or (board[18]==token and board[21]==token)):
            return True
        return False
    
    elif(loc==16):
        if((board[14]==token and board[15]==token) or (board[7]==token and board[11]==token) or (board[19]==token and board[22]==token)):
            return True
        return False

    elif(loc==17):
        if((board[3]==token and board[9]==token) or (board[14]==token and board[20]==token) or (board[18]==token and board[19]==token)):
            return True
        return False

    elif(loc==18):
        if((board[17]==token and board[19]==token) or (board[15]==token and board[21]==token)):
            return True
        return False
    
    elif(loc==19):
        if((board[17]==token and board[18]==token) or (board[5]==token and board[12]==token) or (board[16]==token and board[22]==token)):
            return True
        return False    
    
    elif(loc==20):
        if((board[0]==token and board[8]==token) or (board[14]==token and board[17]==token) or (board[21]==token and board[22]==token)):
            return True
        return False
    
    elif(loc==21):
        if((board[20]==token and board[22]==token) or (board[15]==token and board[18]==token)):
            return True
        return False
    
    elif(loc==22):
        if((board[2]==token and board[13]==token) or (board[20]==token and board[21]==token) or (board[16]==token and board[19]==token)):
            return True
        return False
    else:
        print("Error")
        return False

def generateRemove(board,positions):
    turn='W'
    rival = 'B'
    count = 0
    #show(board)
    size = len(board)
    for loc in range(size):
        if board[loc]==rival:
            if not closeMill(loc,board,rival):
                count+=1
                tmp = board[:]
                tmp[loc]='x'
                positions.append(tmp)
                #print(tmp)
    if count==0:
        positions.append(board[:])

# a list L of all positions reachable by a black add.
def generateAdd(board):#turn = W or B
    turn = 'W'
    size = len(board)
    positions = []
    for i in range(size):
        if board[i]=='x':
            tmp = board[:]
            tmp[i] = turn
            if closeMill(i,tmp):
                generateRemove(tmp,positions)
            else:
                positions.append(tmp)
    return positions
def generateHopping(board):
    turn = 'W'
    size = len(board)
    positions = []
    for i in range(size):
        if board[i]==turn:
            for j in range(size):
                if board[j]=='x':
                    tmp = board[:]
                    tmp[j] = turn
                    tmp[i] = 'x'
                    if closeMill(j,tmp):
                        generateRemove(tmp,positions)
                    else:
                        positions.append(tmp)
    return positions
def generateMove(board):
    turn = 'W'
    size = len(board)
    positions = []
    for i in range(size):
        if board[i]==turn:
            for j in neighbors(i):
                if board[j]=='x':
                    tmp = board[:]
                    tmp[j] = turn
                    tmp[i] = 'x'
                    if closeMill(j,tmp):
                        #print(tmp)
                        generateRemove(tmp,positions)
                    else:
                        positions.append(tmp)

    return positions
def getInverse(board):
    size = len(board)
    inv = ['x' for _ in range(size)]
    
    for i in range(size):
        if board[i]=='W':
            inv[i] = 'B'
        elif board[i]=='B':
            inv[i] = 'W'
    return inv
def change(board):
    for i in range(len(board)):
        if board[i]=='W':
            board[i] = 'B'
        elif board[i]=='B':
            board[i] = 'W'
def changePos(positions):
    for i in range(len(positions)):
        change(positions[i])
def readBoard(fileName):
    file = open(fileName,"r")
    board = list()
    for line in file:
        for s in line:
            board.append(s)
    file.close()
    return board

def writeBoard(board,fileName):
    file = open(fileName,"w")
    for b in board:
        file.write(b)
    file.close()

def show(b):
    board = ['_' if i=='x' else i for i in b]
    print('{:>2}{:>6}{:>6}'.format(board[20],board[21],board[22]))
    print('{:>4}{:>4}{:>4}'.format(board[17],board[18],board[19]))
    print('{:>6}{:>2}{:>2}'.format(board[14],board[15],board[16]))
    print('{:>2}{:>2}{:>2}{:>4}{:>2}{:>2}'.format(board[8],board[9],board[10],board[11],board[12],board[13]))
    print('{:>6}{:>4}'.format(board[6],board[7]))
    print('{:>4}{:>4}{:>4}'.format(board[3],board[4],board[5]))
    print('{:>2}{:>6}{:>6}'.format(board[0],board[1],board[2]))
    print()

def Mills(loc):
    if loc==0:
        return [[1,2],[3,6],[8,20]]
    
    elif loc==1:
        return [[0,2]]
    
    elif loc==2:
        return [[0,1],[13,22],[5,7]]
    
    elif loc==3:
        return [[0,6],[4,5],[9,17]]
    
    elif loc==4:
        return [[3,5]]

    elif loc==5:
        return [[3,4],[12,19],[2,7]]
    
    elif loc==6:
        return [[0,3],[10,14]]
    
    elif loc==7:
        return [[2,5],[11,16]]
    
    elif loc==8:
        return [[0,20],[9,10]]
    
    elif loc==9:
        return [[8,10],[3,17]]

    elif loc==10:
        return [[6,14], [8,9]]

    elif loc==11:
        return [[7,16],[12,13]]

    elif loc==12:
        return [[11,13],[5,19]]

    elif loc==13:
        return [[11,12],[2,22]]

    elif loc==14:
        return [[17,20],[15,16],[6,10]]

    elif loc==15:
        return [[14,16],[18,21]]

    elif loc==16:
        return [[14,15],[7,11],[19,22]]

    elif loc==17:
        return [[3,9],[14,20],[18,19]]

    elif loc==18:
        return [[17,19],[15,21]]

    elif loc==19:
        return [[17,18],[5,12],[16,22]]

    elif loc==20:
        return [[0,8],[14,17],[21,22]]

    elif loc==21:
        return [[20,22],[15,18]]

    elif loc==22:
        return [[2,13],[20,21],[16,19]]

    else:
        print("error")
