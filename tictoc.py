import os
import time

def initBoard(l):
    board=[]
    for i in range(l):
        temp = []
        for j in range(l):
            temp.append(0)
        board.append(temp)
    return board

def showBoard(board):
    os.system("clear")
    print("   _a____b_____c_____d_____e_\n")
    for i in range(len(board)):
        print(i+1, end=' | ')
        for j in range(len(board[i])):
            c = ' '
            if board[i][j] == 1:
                c = 'O'
            elif board[i][j] == 2:
                c = 'X'
            print(c, end='  |  ')
        # todo: rewrite for
        print("\n______________________________\n")

def checkSelectIsValid(board, s):
    if not s[0].isnumeric() or len(s) > 2:
        return False
    x = int(s[0]) - 1
    y = int(ord(s[1])) - int(ord('a'))
    if x > 6 or y > 6 :
        return False
    elif  board[x][y] != 0:
        return False
    return True

def reloadBoard(board, s, i):
    x = int(s[0]) - 1
    y = int(ord(s[1])) - int(ord('a'))
    board[x][y] = i
    return board

def checkUserWin(board):
    # Check rows
    for x in range(l):
        p1_cnt = p2_cnt = 0
        for y in range(l):
            if board[x][y] == 0:
                break
            elif board[x][y] == 1:
                p1_cnt += 1
            else:
                p2_cnt += 1
        if p1_cnt == 5 or p2_cnt == 5:
            return True
    # Check clmns
    for x in range(l):
        p1_cnt = p2_cnt = 0
        for y in range(l):
            if board[y][x] == 0:
                break
            elif board[y][x] == 1:
                p1_cnt += 1
            else:
                p2_cnt += 1
        if p1_cnt == 5 or p2_cnt == 5:
            return True
    return False

player1 = input("please insert name of player 1 ")
player2 = input("please insert name of player 2 ")
l = 5
my_board = initBoard(l)
i = 1
while True:  
    current_player = ""    
    os.system("clear")       
    showBoard(my_board)
    if i == 1:
        i+=1
        current_player = player1
    else:
        i = 1
        current_player = player2
    palyer_select = input(f'{current_player} insert chooise ')

    if checkSelectIsValid(my_board, palyer_select):
        my_board = reloadBoard(my_board, palyer_select, i)
        if checkUserWin(my_board):
            os.system("clear")       
            showBoard(my_board)
            print(f'{current_player} WINNN ...')
            break
    else:
        print('your select is not valid')
        i = 1 if i == 2 else 2
        time.sleep(1)
