# 삼성 SW 역량테스트 2021 상반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    attack_infos = [[*map(int, input().rstrip().split())] for _ in range(m)]
    return n, m, board, attack_infos

def attack_monster(idx):
    global board, result
    x, y = n//2, n//2
    d, s = attack_infos[idx]
    dx, dy = direction[d]
    for _ in range(s):
        nx, ny = x+dx, y+dy
        if not board[nx][ny]: break
        result += board[nx][ny]
        board[nx][ny] = 0
        x, y = nx, ny

def fill_blank():
    global board
    temp = [[0]*n for _ in range(n)]

    x, y = n//2, n//2
    rotate_axis, rotate_val = [(x, y)], [0]
    cnt, d = 1, 0

    while cnt <= n-1:
        for _ in range(2):
            for _ in range(cnt):
                x, y = x+delta[d][0], y+delta[d][1]
                rotate_axis.append((x, y))
                if board[x][y]: rotate_val.append(board[x][y])
            d = (d+1)%4
        cnt += 1

    for i in range(n-2, -1, -1): 
        rotate_axis.append((0, i))
        if board[0][i]: rotate_val.append(board[0][i])

    for i in range(len(rotate_val)):
        x, y = rotate_axis[i]
        temp[x][y] = rotate_val[i]
    board = temp
    return rotate_axis, rotate_val

def remove_monster():
    global rotate_axis, rotate_val, board, result
    while True:
        remove_idx = []
        temp = [1]
        for i in range(2, len(rotate_val)):
            if rotate_val[i] == rotate_val[temp[-1]]:
                temp.append(i)
            else:
                if len(temp) >= 4:
                    remove_idx += temp
                temp = [i]
            if i == len(rotate_val)-1 and len(temp) >= 4:
                remove_idx += temp
        result += sum([rotate_val[i] for i in remove_idx])
        rotate_val = [rotate_val[i] for i in range(len(rotate_val)) if i not in remove_idx]
        if not remove_idx: break

    temp = [[0]*n for _ in range(n)]
    for i in range(len(rotate_val)):
        x, y = rotate_axis[i]
        temp[x][y] = rotate_val[i]
    board = temp
    return rotate_axis, rotate_val

def count_monster():
    global rotate_axis, rotate_val, board
    cnt, prev, temp = 1, rotate_val[1], []
    for i in range(2, len(rotate_val)):
        if rotate_val[i] == prev:
            cnt += 1
        else:
            temp += [cnt, prev]
            prev = rotate_val[i]
            cnt = 1
        if i == len(rotate_val)-1:
            temp += [cnt, prev]
    
    rotate_val = [0] + temp
    temp = [[0]*n for _ in range(n)]
    if len(rotate_val) > len(rotate_axis):
        rotate_val = rotate_val[:len(rotate_axis)]
    for i in range(len(rotate_val)):
        x, y = rotate_axis[i]
        temp[x][y] = rotate_val[i]
    board = temp

def simulate():
    global rotate_axis, rotate_val
    for stage in range(m):
        attack_monster(stage)
        rotate_axis, rotate_val = fill_blank()
        rotate_axis, rotate_val = remove_monster()
        count_monster()

n, m, board, attack_infos = input_data()
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
rotate_axis, rotate_val = [], []
result = 0
simulate()
print(result)