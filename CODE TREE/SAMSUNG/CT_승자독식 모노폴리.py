# 삼성 SW 역량테스트 2020 상반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, k = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    dirs = [*map(lambda x: int(x)-1, input().rstrip().split())]
    move_priority = [[] for _ in range(m)]
    for i in range(m):
        for _ in range(4):
            move_priority[i].append([*map(lambda x: int(x)-1, input().rstrip().split())])
    return n, m, k, board, dirs, move_priority

def make_board():
    for i in range(n):
        for j in range(n):
            if arr[i][j][1] > 0: arr[i][j][1] -= 1
            if board[i][j]: arr[i][j] = [board[i][j], k]

def move():
    global board, arr
    temp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                idx = board[x][y]-1
                d = dirs[idx]
                found = False

                for nd in move_priority[idx][d]:
                    nx, ny = x+direction[nd][0], y+direction[nd][1]
                    if not ((0 <= nx < n) and (0 <= ny < n)): continue
                    if arr[nx][ny][1] == 0:
                        dirs[idx] = nd
                        if temp[nx][ny] == 0:
                            temp[nx][ny] = board[x][y]
                        else:
                            temp[nx][ny] = min(board[x][y], temp[nx][ny])
                        found = True
                        break
                if found: continue

                for nd in move_priority[idx][d]:
                    nx, ny = x+direction[nd][0], y+direction[nd][1]
                    if not ((0 <= nx < n) and (0 <= ny < n)): continue
                    if arr[nx][ny][0] == board[x][y]:
                        dirs[idx] = nd
                        temp[nx][ny] = board[x][y]
                        break
    board = temp

def simulate():
    time = 0
    while True:
        time += 1
        make_board()
        move()
        
        check = True
        for i in range(n):
            for j in range(n):
                if board[i][j] > 1: check = False

        if check: return time
        if time > 1000: return -1

n, m, k, board, dirs, move_priority = input_data()
arr = [[[0]*2 for _ in range(n)] for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = simulate()
print(result)