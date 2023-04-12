# 삼성 SW 역량테스트 2019 상반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    r, c, k = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(3)]
    return r, c, k, board

def calculate():
    global board
    row_len, col_len, max_size = len(board), len(board[0]), 0

    if row_len >= col_len:
        temp = [[] for _ in range(row_len)]
        for i in range(row_len):
            count, count_dict = [], dict()
            for j in range(col_len):
                if board[i][j]:
                    if board[i][j] not in count_dict: count_dict[board[i][j]] = 1
                    else: count_dict[board[i][j]] += 1
            for num in list(count_dict.keys()):
                count.append([num, count_dict[num]])
            count.sort(key=lambda x: (x[1], x[0]))
            for value in count: temp[i] += value
            max_size = max(max_size, len(temp[i]))
    
        for row in temp:
            if len(row) < max_size:
                row += [0]*(max_size-len(row))
        board = temp

    else:
        board = list(map(list, zip(*board)))
        temp = [[] for _ in range(col_len)]
        for i in range(col_len):
            count, count_dict = [], dict()
            for j in range(row_len):
                if board[i][j]:
                    if board[i][j] not in count_dict: count_dict[board[i][j]] = 1
                    else: count_dict[board[i][j]] += 1
            for num in list(count_dict.keys()):
                count.append([num, count_dict[num]])
            count.sort(key=lambda x: (x[1], x[0]))
            for value in count: temp[i] += value
            max_size = max(max_size, len(temp[i]))
    
        for row in temp:
            if len(row) < max_size:
                row += [0]*(max_size-len(row))
        board = list(map(list, zip(*temp)))

def simulate():
    time = 0
    while True:
        if time > 100: return -1
        if (len(board) >= r) and (len(board[0]) >= c):
            if board[r-1][c-1] == k: return time
        time += 1
        calculate()

r, c, k, board = input_data()
result = simulate()
print(result)