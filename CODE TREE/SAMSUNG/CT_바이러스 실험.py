# 삼성 SW 역량테스트 2018 하반기 오후 1번 문제

import sys, copy
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, k = map(int, input().rstrip().split())
    food = [[*map(int, input().rstrip().split())] for _ in range(n)]
    virus = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        r, c, val = map(int, input().rstrip().split())
        virus[r-1][c-1].append(val)
    return n, m, k, food, virus

def feed():
    global board, virus
    temp = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if virus[x][y]:
                dead_list = []
                virus[x][y].sort()
                for i in range(len(virus[x][y])):
                    if board[x][y] >= virus[x][y][i]:
                        board[x][y] -= virus[x][y][i]
                        temp[x][y].append(virus[x][y][i]+1)
                    else: dead_list = virus[x][y][i:]; break
                for val in dead_list: board[x][y] += (val//2)
    virus = temp

def breed():
    global board, virus
    temp = copy.deepcopy(virus)
    for x in range(n):
        for y in range(n):
            board[x][y] += food[x][y]
            if virus[x][y]:
                for i in range(len(virus[x][y])):
                    if (virus[x][y][i] > 0) and (virus[x][y][i] % 5 == 0):
                        for dx, dy in direction:
                            nx, ny = x+dx, y+dy
                            if not ((0 <= nx < n) and (0 <= ny < n)): continue
                            temp[nx][ny].append(1)
    virus = temp

def growth():
    global board
    for x in range(n):
        for y in range(n):
            board[x][y] += food[x][y]

def simulate():
    global board, virus
    result = 0
    for _ in range(k):
        feed()
        breed()
        growth()

    for i in range(n):
        for j in range(n):
            if virus[i][j]:
                result += len(virus[i][j])
    return result

n, m, k, food, virus = input_data()
board = [[5]*n for _ in range(n)]
direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 1), (1, 0)]
result = simulate()
print(result)