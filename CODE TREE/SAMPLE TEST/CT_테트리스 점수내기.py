# 삼성 공채 코딩테스트 모의고사 3 - 테트리스 점수내기

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, board

block_list = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],

    [[0, 0], [0, 1], [1, 0], [1, 1]],

    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 0]],
    [[1, 0], [0, 1], [1, 1], [2, 1]],

    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[2, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 2], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 0]],

    [[0, 1], [0, 2], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 1], [1, 0], [1, 1], [2, 0]]
]

def check(board):
    result = 0
    for row in range(n):
        cnt = 0
        for col in range(m):
            if board[row][col]: 
                cnt += 1
        if cnt == m: 
            result += 1
    return result

def simulate():
    result = 0
    for col in range(m):
        for blocks in block_list:
            for row in range(n):
                cnt = 0
                temp = [item[:] for item in board]
                for block in blocks:
                    x, y = block
                    nx, ny = x+row, y+col
                    if not ((0 <= nx < n) and (0 <= ny < m)): break
                    if board[nx][ny] == 1: break
                    cnt += 1
                if cnt < 4: break
                if cnt == 4:
                    for block in blocks:
                        x, y = block
                        nx, ny = x+row, y+col
                        temp[nx][ny] += 2
                    result = max(result, check(temp))

    return result

n, m, board = input_data()
result = simulate()
print(result)