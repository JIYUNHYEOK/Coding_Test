# 삼성 SW 역량테스트 2016 하반기 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, x, y, k = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    rotate_infos = [*map(lambda x: int(x)-1, input().rstrip().split())]
    return n, m, x, y, k, board, rotate_infos

def roll_dice(d):
    global dice
    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif d == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

def simulate():
    global x, y
    for i in range(k):
        dir = rotate_infos[i]
        nx, ny = x+direction[dir][0], y+direction[dir][1]
        if not ((0 <= nx < n) and (0 <= ny < m)): continue

        if board[x][y]: dice[5], board[x][y] = board[x][y], 0
        else: board[x][y] = dice[5]

        x, y = nx, ny
        roll_dice(dir)
        print(dice[0])

n, m, x, y, k, board, rotate_infos = input_data()
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0, 0, 0, 0, 0, 0]
simulate()