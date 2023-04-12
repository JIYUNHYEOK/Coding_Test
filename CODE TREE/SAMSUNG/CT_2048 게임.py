# 삼성 SW 역량테스트 2016 하반기 2번 문제

import sys, copy
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, board

def up(board):
    for col in range(n):
        idx = 0
        for row in range(1, n):
            if board[row][col]:
                temp = board[row][col]
                board[row][col] = 0
                if not board[idx][col]:
                    board[idx][col] = temp
                elif board[idx][col] == temp:
                    board[idx][col] = 2*temp
                    idx += 1
                else:
                    idx += 1
                    board[idx][col] = temp
    return board

def down(board):
    for col in range(n):
        idx = n-1
        for row in range(n-2, -1, -1):
            if board[row][col]:
                temp = board[row][col]
                board[row][col] = 0
                if not board[idx][col]:
                    board[idx][col] = temp
                elif board[idx][col] == temp:
                    board[idx][col] = 2*temp
                    idx -= 1
                else:
                    idx -= 1
                    board[idx][col] = temp
    return board

def left(board):
    for row in range(n):
        idx = 0
        for col in range(1, n):
            if board[row][col]:
                temp = board[row][col]
                board[row][col] = 0
                if not board[row][idx]:
                    board[row][idx] = temp
                elif board[row][idx] == temp:
                    board[row][idx] = 2*temp
                    idx += 1
                else:
                    idx += 1
                    board[row][idx] = temp
    return board

def right(board):
    for row in range(n):
        idx = n-1
        for col in range(n-2, -1, -1):
            if board[row][col]:
                temp = board[row][col]
                board[row][col] = 0
                if not board[row][idx]:
                    board[row][idx] = temp
                elif board[row][idx] == temp:
                    board[row][idx] = 2*temp
                    idx -= 1
                else:
                    idx -= 1
                    board[row][idx] = temp
    return board

def dfs(board, depth):
    if depth == 5:
        return max(map(max, board))
    
    return max(dfs(up(copy.deepcopy(board)), depth+1), dfs(down(copy.deepcopy(board)), depth+1), dfs(left(copy.deepcopy(board)), depth+1), dfs(right(copy.deepcopy(board)), depth+1))

n, board = input_data()
result = dfs(board, 0)
print(result)