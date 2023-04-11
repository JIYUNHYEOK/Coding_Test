# 삼성 공채 코딩테스트 모의고사 1 - 신기한 Bucket
# https://www.codetree.ai/training-field/problems/special-bucket/description

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def drop(block_num, pos):
    for i in range(n, -1, -1):
        if board[i][pos] == 0:
            board[i][pos] = block_num
            break
            
def bomb():
    score = 0
    for i in range(n + 1):
        if board[i][1] and board[i][2] and board[i][3] and board[i][4]:
            board[i][1] = board[i][2] = board[i][3] = board[i][4] = 0
            score += 1
    return score

def gravity():
    for i in range(n + 1):
        for j in range(1, 5):
            temp[i][j] = 0
    
    for j in range(1, 5):
        idx = n
        for i in range(n, -1, -1):
            if board[i][j]:
                temp[idx][j] = board[i][j]
                idx -= 1
    
    for i in range(n + 1):
        for j in range(1, 5):
            board[i][j] = temp[i][j]

def in_range(x, y):
    return 0 <= x <= n and 1 <= y <= 4

def update(x, y, block_num):
    if temp[x][y] == 0 or temp[x][y] > block_num: temp[x][y] = block_num

def move():
    for i in range(n + 1):
        for j in range(1, 5): temp[i][j] = 0
    
    for x in range(n + 1):
        for y in range(1, 5):
            if not board[x][y]: continue
            
            block_num = board[x][y]
            for move_dir in block_infos[block_num]:
                dx, dy = direction[move_dir][0], direction[move_dir][1]
                nx, ny = x + dx, y + dy
                
                if  0 <= nx <= n and 1 <= ny <= 4:
                    if (not temp[nx][ny]) or (temp[nx][ny] > block_num): temp[nx][ny] = block_num
                    break
    
    for i in range(n + 1):
        for j in range(1, 5):
            board[i][j] = temp[i][j]

def score():
    curr_score = 0
    for i in range(n + 1):
        for j in range(1, 5):
            board[i][j] = 0
    
    for i in range(n):
        block_num, pos = block_drops[i]

        drop(block_num, pos)
        curr_score += bomb()
        gravity()

        move()
        gravity()

        curr_score += bomb()
        gravity()
    return curr_score

def dfs(cnt):
    global result
    if cnt == len(candidates):
        result = max(result, score())
        return
    
    for i in range(1, 5):
        block_drops[candidates[cnt]][1] = i
        dfs(cnt + 1)

def input_data():
    n = int(input().rstrip())
    block_infos = [[0]*8] + [[*map(lambda x: int(x)-1, input().rstrip().split())] for _ in range(8)]
    block_drops = [[*map(int, input().rstrip().split())] for _ in range(4)]
    candidates = [i for i in range(len(block_drops)) if not block_drops[i][1]]
    return n, block_infos, block_drops, candidates

n, block_infos, block_drops, candidates = input_data()
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
board = [[0]*5 for _ in range(101)]
temp = [[0]*5 for _ in range(101)]
result = 0

dfs(0)
print(result)