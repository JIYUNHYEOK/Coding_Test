# 삼성 SW 역량테스트 2019 상반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m, t = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, t, board

def search():
    for x in range(n):
        if board[x][0] == -1: sx, sy = x, 0; break
    return sx, sy

def diffusion():
    global board
    temp = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if board[x][y] == -1: temp[x][y] = -1; continue
            diff_val = board[x][y] // 5
            remain_val = board[x][y]
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if not ((0 <= nx < n) and (0 <= ny < m)): continue
                if board[nx][ny] == -1: continue
                temp[nx][ny] += diff_val
                remain_val -= diff_val
            temp[x][y] += remain_val
    board = temp
            
def cleaning():
    global board
    queue1, queue2 = [], []
    value1, value2 = deque(), deque()
    for i in range(1, m-1):
        queue1.append((sx, i))
        value1.append(board[sx][i])
        queue2.append((sx+1, i))
        value2.append(board[sx+1][i])
    
    for i in range(sx, 0, -1):
        queue1.append((i, m-1))
        value1.append(board[i][m-1])
    for i in range(sx+1, n-1):
        queue2.append((i, m-1))
        value2.append(board[i][m-1])

    for i in range(m-1, 0, -1):
        queue1.append((0, i))
        value1.append(board[0][i])
        queue2.append((n-1, i))
        value2.append(board[n-1][i])

    for i in range(0, sx):
        queue1.append((i, 0))
        value1.append(board[i][0])
    for i in range(n-1, sx+1, -1):
        queue2.append((i, 0))
        value2.append(board[i][0])

    value1.rotate(1); value2.rotate(1)
    value1[0], value2[0] = 0, 0

    for idx, (i, j) in enumerate(queue1):
        board[i][j] = value1[idx]

    for idx, (i, j) in enumerate(queue2):
        board[i][j] = value2[idx]

def simulate():
    for _ in range(t):
        diffusion()
        cleaning()
    return sum(map(sum, board)) + 2

n, m, t, board = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
sx, sy = search()
result = simulate()
print(result)