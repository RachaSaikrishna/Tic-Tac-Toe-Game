spaces=10*' '
board=list(spaces)
player=1
#############win#############
win=1
draw=-1
running=0
stop=1
#############################
game=running
mark='X'
def drawboard():
    print("%c|%c|%c"%(board[1],board[2],board[3]))
    print("_|_|_")
    print("%c|%c|%c"%(board[4],board[5],board[6]))
    print("_|_|_")
    print("%c|%c|%c"%(board[7],board[8],board[9]))
    print(" | | ")
def checkpos(x):
    if(board[x]==' '):
        return True
    else:
        return False
def checkwin():
    global game
    if(board[1]==board[2] and board[2]==board[3] and board[2]!=' '):
        game=win
    elif(board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
        game=win
    elif(board[7]==board[8] and board[8]==board[9] and board[8]!=' '):
        game=win
    elif(board[1]==board[4] and board[4]==board[7] and board[4]!=' '):
        game=win
    elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
        game=win
    elif(board[3]==board[6] and board[6]==board[9] and board[9]!=' '):
        game=win
    elif(board[1]==board[5] and board[5]==board[9] and board[1]!=' '):
        game=win
    elif(board[3]==board[5] and board[5]==board[7] and board[3]!=' '):
        game=win
    elif ' ' not in board:
        game=draw
    else:
        game=running
print("Tic-Tac-Toe Game")
print("Player1[X]---player2[O]")
while(game==running):
    drawboard()
    if(player%2!=0):
        print("player 1's chance")
        mark='X'
    else:
        print("player 2's chance")
        mark='O'
    ch=int(input("enter the position b/w [1-9] :"))
    if(checkpos(ch)):
        board[ch]=mark
        player+=1
        checkwin()

drawboard()
if(game==draw):
    print("Game Draw")
elif(game==win):
    player-=1
    if(player%2!=0):
        print("Player 1 won")
    else:
        print("Player 1 won")
