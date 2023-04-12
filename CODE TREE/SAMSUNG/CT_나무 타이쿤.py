# 삼성 SW 역량테스트 2021 상반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    move_infos = []
    for _ in range(m):
        d, s = map(int, input().rstrip().split())
        move_infos.append((d-1, s))
    return n, m, board, move_infos

def move(idx):
    global nutrients_pos, board
    temp_pos = []
    for x, y in nutrients_pos:
        dx, dy = direction[move_infos[idx][0]]
        nx, ny = (x+dx*move_infos[idx][1])%n, (y+dy*move_infos[idx][1])%n
        board[nx][ny] += 1
        temp_pos.append((nx, ny))
    nutrients_pos = temp_pos

def growth():
    global board
    temp = [item[:] for item in board]
    for x, y in nutrients_pos:
        cnt = 0
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if board[nx][ny] >= 1:
                cnt += 1
        temp[x][y] += cnt
    board = temp

def cut():
    global nutrients_pos
    temp_pos = []
    for i in range(n):
        for j in range(n):
            if (i, j) in nutrients_pos: continue
            if board[i][j] >= 2: temp_pos.append((i, j)); board[i][j] -= 2
    nutrients_pos = temp_pos

def simulate():
    for year in range(m):
        move(year)
        growth()
        cut()
    tot = sum(map(sum, board))
    return tot

n, m, board, move_infos = input_data()
delta = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
direction = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
nutrients_pos = [(n-2, 0), (n-1, 0), (n-2, 1), (n-1, 1)]
result = simulate()
print(result)