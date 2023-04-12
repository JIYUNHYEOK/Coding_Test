# 삼성 SW 역량테스트 2015 하반기 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*input().rstrip()] for _ in range(n)]
    return n, m, board

def search():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': rx, ry = i, j
            elif board[i][j] == 'B': bx, by = i, j
    return rx, ry, bx, by

def move(x, y, direction):
    cnt = 0
    dx, dy = direction
    while True:
        nx, ny = x+dx, y+dy
        if board[nx][ny] == '#': break
        if board[x][y] == 'O': break
        x, y = nx, ny
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 1)])
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = True

    while queue:
        rx, ry, bx, by, cnt = queue.popleft()

        if cnt > 10: return -1

        for d in range(4):
            next_rx, next_ry, r_cnt = move(rx, ry, direction[d])
            next_bx, next_by, b_cnt = move(bx, by, direction[d])
        
            if board[next_bx][next_by] == 'O': continue
            if board[next_rx][next_ry] == 'O': return cnt

            if (next_rx, next_ry) == (next_bx, next_by):
                if r_cnt > b_cnt:
                    next_rx -= direction[d][0]
                    next_ry -= direction[d][1]
                else:
                    next_bx -= direction[d][0]
                    next_by -= direction[d][1]
            
            if visited[next_rx][next_ry][next_bx][next_by]: continue
            visited[next_rx][next_ry][next_bx][next_by] = True
            queue.append((next_rx, next_ry, next_bx, next_by, cnt+1))
    return -1

n, m, board = input_data()
rx, ry, bx, by = search()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = bfs(rx, ry, bx, by)
print(result)