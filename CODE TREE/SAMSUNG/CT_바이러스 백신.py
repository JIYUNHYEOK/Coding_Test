# 삼성 SW 역량테스트 2019 상반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, board

def dfs(depth, start):
    global res
    if depth == m:
        res = min(res, bfs())
        return
    for i in range(start, len(hospital)):
        board[hospital[i][0]][hospital[i][1]] = -1
        dfs(depth+1, i+1)
        board[hospital[i][0]][hospital[i][1]] = 2

def bfs():
    res, cnt, target = 1, 0, 0
    queue = deque()
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                queue.append((i, j))
                visited[i][j] = 1
            elif board[i][j] == 0:
                target += 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if board[nx][ny] == 1: continue
            if visited[nx][ny]: continue
            if board[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                res = max(res, visited[nx][ny])
                cnt += 1
            elif board[nx][ny] == 2:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    res = res-1 if target == cnt else int(1e9)
    return res

n, m, board = input_data()
direction = [(-1, 0), (1, 0), (0,-1), (0, 1)]
hospital = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 2]
res = int(1e9)
dfs(0, 0)
result = res if res != int(1e9) else -1
print(result)