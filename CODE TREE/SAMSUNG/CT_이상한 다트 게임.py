# 삼성 SW 역량테스트 2019 하반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m, q = map(int, input().rstrip().split())
    board = [deque([*map(int, input().rstrip().split())]) for _ in range(n)]
    rotate_infos = [[*map(int, input().rstrip().split())] for _ in range(q)]
    return n, m, q, board, rotate_infos

def rotate(x, d, k):
    global board
    for i in range(x-1, n, x):
        if d == 0: r = k
        else: r = (-1)*k
        board[i].rotate(r)

def check():
    global board
    temp_idx = set()
    for x in range(n):
        for y in range(m-1):
            if not board[x][y]: continue
            if board[x][y] == board[x][y+1]: temp_idx.add((x, y)); temp_idx.add((x, y+1))
    for x in range(n):
        if not board[x][0]: continue
        if board[x][0] == board[x][m-1]: temp_idx.add((x, 0)); temp_idx.add((x, m-1))
    for x in range(n-1):
        for y in range(m):
            if not board[x][y]: continue
            if board[x][y] == board[x+1][y]: temp_idx.add((x, y)); temp_idx.add((x+1, y))
    
    if not temp_idx: return True
    for x, y in temp_idx: board[x][y] = 0

def regulate():
    global board
    tot = sum(map(sum, board))
    cnt = len([(i, j) for i in range(n) for j in range(m) if board[i][j] > 0])
    if cnt > 0:
        avg = tot//cnt
        for x in range(n):
            for y in range(m):
                if board[x][y]:
                    if board[x][y] > avg: board[x][y] -= 1
                    elif board[x][y] < avg: board[x][y] += 1
def simulate():
    for i in range(q):
        x, d, k = rotate_infos[i]
        rotate(x, d, k)
        if check(): regulate()
    result = sum(map(sum, board))
    return result
             
n, m, q, board, rotate_infos = input_data()
result = simulate()
print(result)