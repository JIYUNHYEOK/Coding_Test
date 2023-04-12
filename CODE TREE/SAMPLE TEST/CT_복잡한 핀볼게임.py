# 삼성 공채 코딩테스트 모의고사 2 - 복잡한 핀볼게임

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    blank = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 3]
    n_list, ball_pos = [*map(int, input().rstrip().split())], []
    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for i in range(4):
        for j in range(n):
            if n_list[i*n+j]:
                if i == 0: ball_pos.append((-1, j, i))
                elif i == 1: ball_pos.append((j, n, i))
                elif i == 2: ball_pos.append((n, (n-1)-j, i))
                elif i == 3: ball_pos.append(((n-1)-j, -1, i))
    return n, board, blank, ball_pos, direction

def change_dir(s, d):
    if s == 1:
        if (d == 0) or (d == 1): return (1-d)
        elif (d == 2) or (d == 3): return (5-d)
    if s == 2: return (3-d)

def dfs(depth, start):
    global result
    if depth == len(blank):
        result = max(result, simulate())
    for i in range(start, len(blank)):
        for num in range(3):
            board[blank[i][0]][blank[i][1]] = num
            dfs(depth+1, i+1)
            board[blank[i][0]][blank[i][1]] = 3

def simulate():
    result = 0
    curr_ball = ball_pos[:]
    while curr_ball:
        next_pos, temp = [], [[[] for _ in range(n)] for _ in range(n)]
        for i in range(len(curr_ball)):
            x, y, d = curr_ball[i]
            dx, dy = direction[d]
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): result += 1; continue
            if board[nx][ny] == 0: temp[nx][ny].append((nx, ny, d))
            else: temp[nx][ny].append((nx, ny, change_dir(board[nx][ny], d)))
        
        for i in range(n):
            for j in range(n):
                if len(temp[i][j]) == 1:
                    next_pos.append(temp[i][j][0])
        curr_ball = next_pos
    return result

n, board, blank, ball_pos, direction = input_data()
result = 0
dfs(0, 0)
print(result)