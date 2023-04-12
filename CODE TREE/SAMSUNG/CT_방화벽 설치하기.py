# 삼성 SW 역량테스트 2017 상반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    wall_list, fire_list = [], []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0: wall_list.append((i, j))
            elif board[i][j] == 2: fire_list.append((i, j))  
    return n, m, board, wall_list, fire_list

def bfs(board):
    queue = deque()
    visited = [[False]*m for _ in range(n)]
    for i, j in fire_list: queue.append((i, j)); visited[i][j] = True
    cnt = len([(i, j) for i in range(n) for j in range(m) if board[i][j] == 0])

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < m)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt -= 1
    return cnt

def dfs(depth, start):
    global result
    if depth == 3:
        result = max(result, bfs(board))
        return
    for i in range(start, len(wall_list)):
        board[wall_list[i][0]][wall_list[i][1]] = 1
        dfs(depth+1, i+1)
        board[wall_list[i][0]][wall_list[i][1]] = 0

n, m, board, wall_list, fire_list = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = int(-1e9)
dfs(0, 0)
print(result)