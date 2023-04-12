# 삼성 공채 코딩테스트 모의고사 2 - 하나가 되고 싶어

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n = int(input().rstrip())
    board = [[*input().rstrip()] for _ in range(n)]
    wall_list = [(i, j) for i in range(n) for j in range(n) if board[i][j] == '#']
    return n, board, wall_list

def bfs(row, col):
    global visited
    queue = deque([(row, col)])
    visited[row][col] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == '#': continue
            queue.append((nx, ny))
            visited[nx][ny] = True

def dfs(depth, cnt, start, n_list):
    global temp_list
    if depth == cnt:
        temp_list.append(n_list[:])
        return
    for i in range(start, len(wall_list)):
        dfs(depth, cnt+1, i+1, n_list + [wall_list[i]])

def simulate():
    global visited, temp_list
    result = 0

    while True:
        temp_list = []
        dfs(result, 0, 0, [])
        for idx in range(len(temp_list)):
            visited = [[False]*n for _ in range(n)]
            for i, j in temp_list[idx]: board[i][j] = '.'
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if (board[i][j] == '.') and (not visited[i][j]):
                        bfs(i, j)
                        cnt += 1
            if cnt == 1: return result
            for i, j in temp_list[idx]: board[i][j] = '#'
        result += 1
        if result > 6: return - 1

n, board, wall_list = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited, temp_list = None, None
result = simulate()
print(result)