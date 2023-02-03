# 백준 14502 연구소

import sys
import copy
from collections import deque

# sys.stdin = open('B14502_input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    temp = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))

    global result
    cnt = 0
    for i in temp:
        cnt += i.count(0)
    result = max(result, cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(cnt + 1)
                board[i][j] = 0


wall(0)
print(result)
