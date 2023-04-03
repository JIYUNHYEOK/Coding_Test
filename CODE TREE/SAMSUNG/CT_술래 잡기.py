# 삼성 SW 역량테스트 2022 상반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, h, k = map(int, input().rstrip().split())
    board = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, d = map(lambda x: int(x)-1, input().rstrip().split())
        board[x][y].append(d+1)
    tree = [[*map(lambda x: int(x)-1, input().rstrip().split())] for _ in range(h)]
    return n, m, h, k, board, tree

def move(pos_x, pos_y):
    global board
    temp = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                if abs(pos_x-x)+abs(pos_y-y) <= 3:
                    for i in board[x][y]:
                        nx, ny = x+direction[i][0], y+direction[i][1]
                        if ((0 <= nx < n) and (0 <= ny < n)): 
                            if (nx, ny) == (pos_x, pos_y): temp[x][y].append(i)
                            else: temp[nx][ny].append(i)
                        else:
                            i = (i+2)%4
                            nx, ny = x+direction[i][0], y+direction[i][1]
                            if (nx, ny) == (pos_x, pos_y): temp[x][y].append(i)
                            else: temp[nx][ny].append(i)
                else:
                    for i in board[x][y]:
                        temp[x][y].append(i)
    board = temp

def make_pos():
    x, y, d = n//2, n//2, 0
    pos_info, cnt = [], 1
    while True:
        flag = False
        for _ in range(2):
            for _ in range(cnt):
                if (x, y) == (0, 0): 
                    flag = True
                    pos_info.append((0, 0, (d+2)%4))
                    break
                pos_info.append((x, y, d))
                x, y = x+direction[d][0], y+direction[d][1]
            if flag: break
            d = (d+1)%4
        cnt += 1
        if len(pos_info) == n*n: break

    x, y, d = 0, 0, 2
    while (x, y) != (n-2, 0):
        x, y = x+direction[d][0], y+direction[d][1]
        pos_info.append((x, y, d))

    x, y = x+direction[d][0], y+direction[d][1]
    cnt, d = n-1, (d-1)%4
    while True:
        flag = False
        for _ in range(2):
            for _ in range(cnt):
                if (x, y) == (n//2, n//2): 
                    flag = True
                    break
                pos_info.append((x, y, d))
                x, y = x+direction[d][0], y+direction[d][1]
            if flag: break
            d = (d-1)%4
        cnt -= 1
        if len(pos_info) == n*n*2-2: break
    return pos_info

n, m, h, k, board, tree = input_data()
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pos_info = make_pos()
result = 0

pos_info = make_pos()
for stage in range(k):
    move(pos_info[stage%len(pos_info)][0], pos_info[stage%len(pos_info)][1])
    pos_x, pos_y, dir = pos_info[(stage+1)%len(pos_info)]
    nx, ny = pos_x+direction[dir][0]*2, pos_y+direction[dir][1]*2
    cnt = 0
    for x in range(max(0, min(pos_x, nx)), min(n, max(pos_x, nx)+1)):
        for y in range(max(0, min(pos_y, ny)), min(n, max(pos_y, ny)+1)):
            if board[x][y]:
                if [x, y] in tree: continue
                cnt += len(board[x][y])
                board[x][y] = []
    result += cnt*(stage+1)
print(result)