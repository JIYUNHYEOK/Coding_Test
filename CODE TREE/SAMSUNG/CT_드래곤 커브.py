# 삼성 SW 역량테스트 2018 상반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    curve_infos = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, curve_infos

def dragon_curve(x, y, d, g):
    global max_x, max_y
    move_dir, move_axis = [d], set()
    move_axis.add((x, y))
    x, y = x+direction[d][0], y+direction[d][1]
    move_axis.add((x, y))
    for _ in range(g):
        for i in move_dir[::-1]:
            i = (i+1)%4
            x, y = x+direction[i][0], y+direction[i][1]
            move_dir.append(i); move_axis.add((x, y))
    for i, j in move_axis:
        max_x = max(i, max_x); max_y = max(j, max_y)
    return move_axis

def check(x, y):
    if (x, y) not in dragon_axis: return False
    if (x+1, y) not in dragon_axis: return False
    if (x, y+1) not in dragon_axis: return False
    if (x+1, y+1) not in dragon_axis: return False
    return True

def solution():
    global dragon_axis
    result = 0
    for x, y, d, g in curve_infos: dragon_axis += dragon_curve(x, y, d, g)
    for i in range(max_x):
        for j in range(max_y):
            if check(i, j): result += 1
    return result

n, curve_infos = input_data()
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
max_x, max_y, result = int(-1e9), int(-1e9), 0
dragon_axis = []
result = solution()
print(result)