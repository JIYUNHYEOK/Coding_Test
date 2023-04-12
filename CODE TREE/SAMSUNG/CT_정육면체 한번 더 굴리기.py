# 삼성 SW 역량테스트 2021 하반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, board

def bfs(row, col):
    queue = deque([(row, col)])
    target = board[row][col]
    visited = [[False]*n for _ in range(n)]
    visited[row][col] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == target:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt*target

def roll_dice(d):
    if d == 0:
        dice[0], dice[2], dice[3], dice[4] = dice[3], dice[0], dice[4], dice[2]
    elif d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[0], dice[1], dice[4]
    elif d == 2:
        dice[0], dice[2], dice[3], dice[4] = dice[2], dice[4], dice[0], dice[3]
    elif d == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[4], dice[5], dice[0]

def simulate():
    global x, y, result, direction
    nx, ny = x+delta[direction][0], y+delta[direction][1]
    if not ((0 <= nx < n) and (0 <= ny < n)):
        direction = (direction + 2) % 4
        nx, ny = x+delta[direction][0], y+delta[direction][1]
    roll_dice(direction)
    result += bfs(nx, ny)
    if dice[4] > board[nx][ny]: direction = (direction + 1) % 4
    elif dice[4] < board[nx][ny]: direction = (direction - 1) % 4
    x, y = nx, ny
    

n, m, board = input_data()
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction, x, y, result = 0, 0, 0, 0
dice = [1, 2, 3, 4, 6, 5]
for _ in range(m): simulate()
print(result)
