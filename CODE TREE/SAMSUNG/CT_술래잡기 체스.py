# 삼성 SW 역량테스트 2020 상반기 오전 2번 문제

import sys, copy
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    board = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        infos = [*map(int, input().rstrip().split())]
        for j in range(4):
            board[i][j] = [infos[2*j], infos[2*j+1]-1]
    return board

def dfs(board, sx, sy, score):
    global result
    score += board[sx][sy][0]
    result = max(result, score)
    board[sx][sy][0] = 0

    for fnum in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == fnum:
                    fx, fy = x, y
                    break

        if (fx, fy) == (-1, -1): continue
        fd = board[fx][fy][1]

        for i in range(8):
            nd = (fd+i)%8
            nx, ny = fx+direction[nd][0], fy+direction[nd][1]
            
            if not ((0 <= nx < 4) and (0 <= ny < 4)): continue
            if ((nx, ny) == (sx, sy)): continue
            board[fx][fy][1] = nd
            board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
            break
    
    sd = board[sx][sy][1]
    for i in range(4):
        nx, ny = sx+direction[sd][0]*i, sy+direction[sd][1]*i
        if (0 <= nx < 4) and (0 <= ny < 4) and (board[nx][ny][0] > 0):
            dfs(copy.deepcopy(board), nx, ny, score)

board = input_data()
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)] # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
result = 0
dfs(board, 0, 0, 0)
print(result)