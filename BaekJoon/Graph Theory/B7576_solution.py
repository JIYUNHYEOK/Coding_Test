## 백준 7576 토마토

import sys
from collections import deque
# sys.stdin = open('B7576_input.txt', 'r')
input = sys.stdin.readline

# 가로, 세로를 행과 열로 바꾸어서 입력받음
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 방향벡터 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))

# BFS 함수 정의
def bfs():

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))

bfs()

cnt=0
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    cnt = max(cnt, max(i))

print(cnt-1)