## 백준 2178 미로탐색

# import sys
from collections import deque

# input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if matrix[nx][ny] == 0:
                continue

            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))

    return matrix[n-1][m-1]

print(bfs(0,0))
            