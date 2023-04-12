# 삼성 SW 역량테스트 2018 상반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, h = map(int, input().rstrip().split())
    board = [[0]*(n+1) for _ in range(h+1)]
    for _ in range(m):
        x, y = map(int, input().rstrip().split())
        board[x][y] = 1
    ladder = []
    for i in range(1,h+1):
        for j in range(1, n):
            if (not board[i][j-1]) and (not board[i][j]) and (not board[i][j+1]):
                ladder.append([i, j])
    return n, m, h, board, ladder

def ladder_check():
    for start in range(1, n+1):
        idx = start
        for row in range(1, h+1):
            if board[row][idx]:
                idx += 1
            elif board[row][idx-1]:
                idx -= 1
        if idx != start:
            return False
    return True

def dfs(depth, start):
    global result
    if depth >= 4:
        return
    if ladder_check():
        result = min(result, depth)
        return
    for i in range(start, len(ladder)):
        x, y = ladder[i]
        if (not board[x][y-1]) and (not board[x][y+1]):
            board[x][y] = 1
            dfs(depth+1, i+1)
            board[x][y] = 0 

n, m, h, board, ladder = input_data()
result = int(1e9)
dfs(0, 0)
result = -1 if result == int(1e9) else result
print(result)