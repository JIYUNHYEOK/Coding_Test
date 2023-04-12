# 삼성 SW 역량테스트 2017 상반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m = map(int, input().rstrip().split())
    x, y, d = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, x, y, d, board

def simulate():
    global x, y, d
    cnt = 1
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    while True:
        for _ in range(4):
            d = (d-1)%4
            nx, ny = x+direction[d][0], y+direction[d][1]
            if not ((0 <= nx < n) and (0 <= ny < m)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == 1: continue
            cnt += 1
            visited[nx][ny] = True
            x, y = nx, ny
            break
        else:
            nx, ny = x-direction[d][0], y-direction[d][1]
            if not ((0 <= nx < n) and (0 <= ny < m)) or board[nx][ny] == 1: break
            x, y = nx, ny
            for _ in range(4):
                d = (d-1)%4
                nx, ny = x+direction[d][0], y+direction[d][1]
                if not ((0 <= nx < n) and (0 <= ny < m)): continue
                if visited[nx][ny]: continue
                if board[nx][ny] == 1: continue
                cnt += 1
                visited[nx][ny] = True
                x, y = nx, ny
                break
    return cnt

n, m, x, y, d, board = input_data()
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = simulate()
print(result)