# 삼성 SW 역량테스트 2019 상반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, k = map(int, input().rstrip().split())
    board = [[[] for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y, s, d, b = map(int, input().rstrip().split())
        board[x-1][y-1].append([s, d-1, b])
    return n, m, k, board

def change_dir(d):
    if d == 0 or d == 1: return (1-d)
    elif d == 2 or d == 3: return (5-d)

def mold_collect(pos):
    global board
    for i in range(n):
            if board[i][pos]:
                res = board[i][pos][0][2]
                board[i][pos] = []
                return res
    return 0
    
def move():
    global board
    temp = [[[] for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if board[x][y]:
                for i in range(len(board[x][y])):
                    s, d, b = board[x][y][i]
                    px, py, pd = x, y, d
                    for _ in range(s):
                        nx, ny = px+direction[pd][0], py+direction[pd][1]
                        if not ((0 <= nx < n) and (0 <= ny < m)):
                            pd = change_dir(pd)
                            nx, ny = px+direction[pd][0], py+direction[pd][1]
                        px, py = nx, ny
                    if not temp[px][py]: temp[px][py].append([s, pd, b])
                    else:
                        if b > temp[px][py][0][2]:
                            temp[px][py] = [[s, pd, b]]
    board = temp

def simulate():
    result = 0
    for pos in range(m):
        result += mold_collect(pos)
        move()
    return result

n, m, k, board = input_data()
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
result = simulate()
print(result)