## 백준 1012 유기농 배추

import sys
from collections import deque
sys.stdin = open('B1012_input.txt', 'r')

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    n, m, k = map(int, input().split())

    matrix = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] += 1

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        matrix[x][y] = 0

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if matrix[nx][ny] == 1:
                        matrix[nx][ny] = 0
                        queue.append((nx, ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)