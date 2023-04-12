# 삼성 SW 역량테스트 2020 하반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, q = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(2**n)]
    rotate_level = [*map(int, input().rstrip().split())]
    return n, q, board, rotate_level

def rotate(level):
    global board
    temp = [[0]*(2**n) for _ in range(2**n)]
    dir = 0
    size = level // 2
    if size >= 1:
        for x in range(0, 2**n, level):
            for y in range(0, 2**n, level):
                pos_x, pos_y = x, y
                for _ in range(4):
                    for i in range(size):
                        for j in range(size):
                            nx, ny = (pos_x+i)+direction[dir][0]*size, (pos_y+j)+direction[dir][1]*size
                            temp[nx][ny] = board[pos_x+i][pos_y+j]
                    pos_x, pos_y = pos_x+direction[dir][0]*size, pos_y+direction[dir][1]*size
                    dir += 1
                dir = 0
        board = temp

def melting():
    global board
    temp_list = []
    for x in range(2**n):
        for y in range(2**n):
            if board[x][y]:
                cnt = 0
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if not ((0 <= nx < 2**n) and (0 <= ny < 2**n)): continue
                    if board[nx][ny]: cnt += 1
                if cnt < 3: temp_list.append((x, y))
    for x, y in temp_list: board[x][y] -= 1

def bfs(row, col):
    queue = deque([(row, col)])
    visited[row][col] = True
    cnt, area_sum = 1, board[row][col]

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < (2**n)) and (0 <= ny < (2**n))): continue
            if visited[nx][ny]: continue
            if not board[nx][ny]: continue
            visited[nx][ny] = True
            queue.append((nx, ny))
            cnt += 1
            area_sum += board[nx][ny]
    return cnt, area_sum

def simulate():
    result1, result2 = 0, 0
    for i in range(q):
        rotate(2**(rotate_level[i]))
        melting()

    for i in range(2**n):
        for j in range(2**n):
            if (board[i][j]) and (not visited[i][j]):
                cnt, area = bfs(i, j)
                result1 += area
                result2 = max(result2, cnt)
    return result1, result2

n, q, board, rotate_level = input_data()
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[0]*(2**n) for _ in range(2**n)]
result = simulate()
print(*result, sep='\n')