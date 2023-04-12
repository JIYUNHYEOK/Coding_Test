# 삼성 SW 역량테스트 2019 하반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, k = map(int, input().rstrip().split())
    board = [[[] for _ in range(n)] for _ in range(n)]
    color_map = [[*map(int, input().rstrip().split())] for _ in range(n)]
    infos = [[]]
    for num in range(1, k+1):
        x, y, d = map(lambda x: int(x)-1, input().rstrip().split())
        board[x][y].append(num)
        infos.append([x, y, d])
    return n, k, board, color_map, board, infos

def change_dir(d):
    if (d == 0) or (d == 1): return (1-d)
    elif (d == 2) or (d == 3): return (5-d)

def move(h_num):
    x, y, d = infos[h_num]
    nx, ny = x+direction[d][0], y+direction[d][1]
    if (not ((0 <= nx < n) and (0 <= ny < n))) or (color_map[nx][ny] == 2):
        d = change_dir(d)
        infos[h_num][2] = d
        nx, ny = x+direction[d][0], y+direction[d][1]
        if (not ((0 <= nx < n) and (0 <= ny < n))) or (color_map[nx][ny] == 2): return True

    pos = []
    for idx, h_n in  enumerate(board[x][y]):
        if h_n == h_num:
            pos.extend(board[x][y][idx:])
            board[x][y] = board[x][y][:idx]
            break
    
    if color_map[nx][ny] == 1: pos = pos[::-1]

    for h in pos:
        infos[h][0], infos[h][1] = nx, ny
        board[nx][ny].append(h)

    if len(board[nx][ny]) >= 4: return False
    return True

def simulate():
    time = 0
    while True:
        time += 1
        for num in range(1, k+1):
            if not move(num): return time
        if time > 1000: return -1
        
n, k, board, color_map, board, infos = input_data()
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
result = simulate()
print(result)