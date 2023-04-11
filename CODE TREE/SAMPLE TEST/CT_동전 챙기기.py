# 삼성 공채 코딩테스트 모의고사 1 - 동전 챙기기
# https://www.codetree.ai/training-field/problems/collect-coins/description

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n = int(input().rstrip())
    board = [[*input().rstrip()] for _ in range(n)]
    return n, board

def search():
    coin_info = dict()
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#' or board[i][j] == '.': continue
            elif board[i][j] == 'S': start = (i, j)
            elif board[i][j] == 'E': end = (i, j)
            else:
                coin = int(board[i][j])
                coin_info[coin] = (i, j)
    coin_info = sorted(coin_info.items())
    return start, end, coin_info

def dfs(depth, start, temp):
    global coin_comb
    if depth >= 3:
        coin_comb.append(temp[:])
        return
    for i in range(start, len(coin_info)):
        dfs(depth+1, i+1, temp + [coin_info[i]])
    
def bfs(start, end):
    visited = [[False]*n for _ in range(n)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == end: return cnt
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == '#': continue
            queue.append((nx, ny, cnt+1))
            visited[nx][ny] = True
    return int(1e9)
            
    
n, board = input_data()
start, end, coin_info = search()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
coin_comb = []
dfs(0, 0, [])
# print(coin_comb)
result = int(1e9)
for i in range(len(coin_comb)):
    dist, coin_start, flag = 0, start, False
    for coin_num, (x, y) in coin_comb[i]:
        dist += bfs(coin_start, (x, y))
        if dist == int(1e9): flag = True; break
        coin_start = (x, y)
    if flag: continue
    dist += bfs(coin_start, end)
    result = min(result, dist)
print(-1 if result == int(1e9) else result)