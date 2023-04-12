# 삼성 SW 역량테스트 2018 상반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, board

def search():
    house, hospital = [], []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2: hospital.append((i, j))
            elif board[i][j] == 1: house.append((i, j))
    return house, hospital

def dfs(depth, start):
    global result
    if depth == m:
        tot = 0
        for sx, sy in house:
            min_dist = int(1e9)
            for ex, ey in temp:
                dist = abs(sx-ex) + abs(sy-ey)
                min_dist = min(dist, min_dist)
            tot += min_dist
            if tot > result: return
        result = min(result, tot)
        return

    for i in range(start, len(hospital)):
        temp.append(hospital[i])
        dfs(depth+1, i+1)
        temp.pop()

n, m, board = input_data()
house, hospital = search()
temp, result = [], int(1e9)
dfs(0, 0)
print(result)