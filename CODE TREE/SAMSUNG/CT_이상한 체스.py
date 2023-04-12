# 삼성 SW 역량테스트 2018 상반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt" , "r")

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, board

def move(x, y, delta, arr):
    for d in delta:
        nx, ny = x, y
        while True:
            nx += direction[d][0]
            ny += direction[d][1]
            if (not ((0 <= nx < n) and (0 <= ny < m))) or (arr[nx][ny] == 6): break
            elif arr[nx][ny] == 0: arr[nx][ny] = '#'

def dfs(cnt, board):
    global result
    if cnt == len(horse_list):
        count = 0
        for row in board: count += row.count(0)
        result = min(result, count)
        return
    
    arr = [item[:] for item in board]
    x, y, num = horse_list[cnt]
    for d in mode[num]:
        move(x, y, d, arr)
        dfs(cnt+1, arr)
        arr = [item[:] for item in board]

n, m, board = input_data()
result = int(1e9)
horse_list = [(i, j, board[i][j]) for i in range(n) for j in range(m) if 1 <= board[i][j] <= 5]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
mode = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
}
dfs(0, board)
print(result)