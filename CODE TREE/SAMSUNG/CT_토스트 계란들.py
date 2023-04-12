# 삼성 SW 역량테스트 2018 하반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, l, r = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, l, r, board

def bfs(row, col):
    global board
    queue = deque([(row, col)])
    visited[row][col] = True
    group, value = [(row, col)], board[row][col]

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            diff = abs(board[x][y] - board[nx][ny])
            if l <= diff <= r:
                value += board[nx][ny]
                visited[nx][ny] = True
                queue.append((nx, ny))
                group.append((nx, ny))
    
    value //= len(group)
    for i, j in group: board[i][j] = value

def simulate():
    global visited
    time = 0

    while True:
        temp = [item[:] for item in board]
        visited = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    bfs(i, j)
        if temp == board: return time
        time += 1

n, l, r, board = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*n for _ in range(n)]
result = simulate()
print(result)