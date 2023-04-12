# 삼성 SW 역량테스트 2020 하반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, board

def move(cnt, dx, dy, direction):
    global result
    for _ in range(cnt):
        pos[0], pos[1] = pos[0]+dx, pos[1]+dy
        if pos[0] < 0 or pos[1] < 0: break

        spreads = 0
        for dx, dy, r in rate[direction]:
            nx, ny = pos[0]+dx, pos[1]+dy

            if r == 0: sand = board[pos[0]][pos[1]] - spreads
            else: sand = int(board[pos[0]][pos[1]]*r)
            
            if (0 <= nx < n) and (0 <= ny < n): board[nx][ny] += sand
            else: result += sand

            spreads += sand

left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, 1, 0.01), (-1, 0, 0.07), (-1, -1, 0.1), (1, 1, 0.01), (1, 0, 0.07), (1, -1, 0.1), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(-x, y, z) for x, y, z in down]
rate = {'left': left, 'right': right, 'down': down, 'up': up}
n, board = input_data()
pos = [n//2, n//2]
result = 0

for i in range(1, n+1):
    if i%2 == 1:
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    else:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')

print(result)