# 삼성 공채 코딩테스트 모의고사 3 - 봄버맨

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n = int(input().rstrip())
    board = [[*input().rstrip()] for _ in range(n)]
    bomb_list = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 'B']
    return n, board, bomb_list

def size_up(bomb_list):
    visited = [[False]*n for _ in range(n)]
    for x, y in bomb_list: visited[x][y] = True

    new_bomb = bomb_list[:]
    for x, y in bomb_list:
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): return False
            if visited[nx][ny]: continue
            if board[nx][ny] == '#': return False
            new_bomb.append((nx, ny))
            visited[nx][ny] = True
    return new_bomb

def move(bomb_list, d):
    new_bomb = []
    for x, y in bomb_list:
        dx, dy = direction[d]
        nx, ny = x+dx, y+dy
        if not ((0 <= nx < n) and (0 <= ny < n)): return False
        if board[nx][ny] == '#': return False
        new_bomb.append((nx, ny))
    return new_bomb

def simulate():
    result = 1
    bomb = deque([bomb_list])
    while bomb:
        curr_bomb = bomb.popleft()
        for idx in range(len(bomb_size)):
            if len(curr_bomb) == bomb_size[idx]: result = max(result, idx+1)
        for dir in range(4):
            move_bomb = move(curr_bomb, dir)
            if move_bomb: 
                new_bomb = size_up(move_bomb)
                if new_bomb: bomb.append(new_bomb)
    return result

n, board, bomb_list = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bomb_size = [1, 5, 13, 25]
result = simulate()
print(result)