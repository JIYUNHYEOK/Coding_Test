# 삼성 SW 역량테스트 2019 하반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, board

def check(r, c, d1, d2):
    if not ((0 <= r < n) and (0 <= c < n)): return False
    if not ((0 <= (r-d1) < n) and (0 <= (c+d1) < n)): return False
    if not ((0 <= (r-d1-d2) < n) and (0 <= (c+d1-d2) < n)): return False
    if not ((0 <= (r-d2) < n) and (0 <= (c-d2) < n)): return False
    return True

def border(x, y, d1, d2, arr):
    dist = [d1, d2] * 2
    
    for i in range(4):
        for _ in range(dist[i]):
            x, y = x+direction[i][0], y+direction[i][1]
            arr[x][y] = True

def divide(r, c, d1, d2, arr):
    border(r, c, d1, d2, arr)
    tot = sum(map(sum, board))
    area = [0] * 5

    for i in range(r-d2):
        for j in range(c+d1-d2+1):
            if arr[i][j]: break
            area[1] += board[i][j]

    for i in range(r-d1+1):
        for j in range(n-1, c+d1-d2, -1):
            if arr[i][j]: break
            area[2] += board[i][j]

    for i in range(r-d2, n):
        for j in range(c):
            if arr[i][j]: break
            area[3] += board[i][j]

    for i in range(r-d1+1, n):
        for j in range(n-1, c-1, -1):
            if arr[i][j]: break
            area[4] += board[i][j]
    
    area[0] = tot - sum(area)
    return max(area) - min(area)

def get_score():
    result = int(1e9)
    for r in range(n):
        for c in range(n):
            for d1 in range(1,n):
                for d2 in range(1,n):
                    if check(r, c, d1, d2):
                        arr = [[False]*n for _ in range(n)]
                        result = min(result, divide(r, c, d1, d2, arr))
    return result

n, board = input_data()
direction = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
result = get_score()
print(result)