# 삼성 SW 역량테스트 2017 상반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, board

def tetromino1(depth, tot, x, y):
    global result
    if depth == 4:
        result = max(result, tot)
        return
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if not ((0 <= nx < n) and (0 <= ny < m)): continue
        if visited[nx][ny]: continue
        visited[nx][ny] = True
        tetromino1(depth+1, tot+board[nx][ny], nx, ny)
        visited[nx][ny] = False

def tetromino2(x, y):
    global result
    for i in range(4):
        tot = board[x][y]
        for j in range(3):
            dir = (i+j)%4
            nx, ny = x+direction[dir][0], y+direction[dir][1]
            if not ((0 <= nx < n) and (0 <= ny < m)): break
            tot += board[nx][ny]
        result = max(tot, result)

def simulate():
    global visited
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            tetromino1(1, board[i][j], i, j)
            visited[i][j] = False
            tetromino2(i, j)

n, m, board = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*m for _ in range(n)]
result = int(-1e9)
simulate()
print(result)