# 삼성 SW 역량테스트 2020 상반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    k = int(input().rstrip())
    infos = [[*map(int, input().rstrip().split())] for _ in range(k)]
    return k, infos

def check_red():
    global result1
    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if red[i][j]: cnt += 1
        if cnt == 4:
            remove_red(j)
            result1 += 1

def remove_red(idx):
    for j in range(idx, 0, -1):
        for i in range(4):
            red[i][j] = red[i][j-1]

    for i in range(4):
        red[i][0] = 0

def move_red(t, x):
    global red
    if (t == 1) or (t == 2):
        for i in range(1, 6):
            if red[x][i]:
                red[x][i-1] = 1
                if t == 2:
                    red[x][i-2] = 1
                break
            elif (i == 5):
                red[x][i] = 1
                if t == 2:
                    red[x][i-1] = 1
    else:
        for i in range(1, 6):
            if red[x][i] or red[x+1][i]:
                red[x][i-1], red[x+1][i-1] = 1, 1
                break
            elif (i == 5):
                red[x][i], red[x+1][i] = 1, 1

    check_red()

    for j in range(2):
        for i in range(4):
            if red[i][j]:
                remove_red(5)
                break

def check_yellow():
    global result1
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if yellow[i][j]: cnt += 1
        if cnt == 4:
            remove_yellow(i)
            result1 += 1

def remove_yellow(idx):
    for i in range(idx, 0, -1):
        for j in range(4):
            yellow[i][j] = yellow[i-1][j]

    for i in range(4):
        yellow[0][i] = 0

def move_yellow(t, y):
    global yellow
    if (t == 1) or (t == 3):
        for i in range(1, 6):
            if yellow[i][y]:
                yellow[i-1][y] = 1
                if t == 3:
                    yellow[i-2][y] = 1
                break
            elif (i == 5):
                yellow[i][y] = 1
                if t == 3:
                    yellow[i-1][y] = 1
    else:
        for i in range(1, 6):
            if yellow[i][y] or yellow[i][y+1]:
                yellow[i-1][y], yellow[i-1][y+1] = 1, 1
                break
            elif (i == 5):
                yellow[i][y], yellow[i][y+1] = 1, 1

    check_yellow()

    for i in range(2):
        for j in range(4):
            if yellow[i][j]:
                remove_yellow(5)
                break

def simulate():
    for i in range(k):
        t, x, y = infos[i]
        move_red(t, x)
        move_yellow(t, y)

def get_score():
    red_cnt, yellow_cnt = 0, 0
    simulate()
    for i in range(4):
        for j in range(2, 6):
            if red[i][j]:
                red_cnt += 1

    for i in range(2, 6):
        for j in range(4):
            if yellow[i][j]:
                yellow_cnt += 1
    return red_cnt+yellow_cnt

k, infos = input_data()
red, yellow = [[0]*6 for _ in range(4)], [[0]*4 for _ in range(6)]
result1 = 0
result2 = get_score()
print(result1, result2, sep='\n')