# 삼성 SW 역량테스트 2022 상반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n = int(input().rstrip())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, board

def bfs(row, col, num):
    global temp
    cnt = 1
    queue = deque([(row, col)])
    visited[row][col] = True
    temp[row][col] = num
    value = board[row][col]

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] != value: continue
            cnt += 1
            queue.append((nx, ny))
            temp[nx][ny] = num
            visited[nx][ny] = True
    return cnt

def idx_matrix():
    num = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                area = bfs(i, j, num)
                idx_area.append((area, board[i][j]))
                num += 1

def adj_matrix():
    for x in range(n):
        for y in range(n):
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if not ((0 <= nx < n) and (0 <= ny < n)): continue
                if temp[nx][ny] != temp[x][y]:
                    matrix[temp[x][y]][temp[nx][ny]] += 1

def get_score():
    score = 0
    for i in range(len(idx_area)):
        for j in range(i+1, len(idx_area)):
            if matrix[i][j]:
                score += (idx_area[i][0]+idx_area[j][0])*idx_area[i][1]*idx_area[j][1]*matrix[i][j]
    return score

def rotate():
    global board
    arr = [[0]*n for _ in range(n)]
    mid_list = board[n//2]
    arr[n//2] = [board[i][n//2] for i in range(n)]
    for i in range(n): arr[i][n//2] = mid_list.pop()

    temp1 = [[board[i][j] for j in range(n//2)] for i in range(n//2)]
    temp1 = [list(i)[::-1] for i in zip(*temp1)]
    for i in range(n//2):
        for j in range(n//2):
            arr[i][j] = temp1[i][j]

    temp2 = [[board[i][j] for j in range((n//2)+1, n)] for i in range(n//2)]
    temp2 = [list(i)[::-1] for i in zip(*temp2)]
    for i in range(n//2):
        for j in range(n//2):
            arr[i][j-(n//2)] = temp2[i][j]

    temp3 = [[board[i][j] for j in range(n//2)] for i in range((n//2)+1, n)]
    temp3 = [list(i)[::-1] for i in zip(*temp3)]
    for i in range(n//2):
        for j in range(n//2):
            arr[i-(n//2)][j] = temp3[i][j]

    temp4 = [[board[i][j] for j in range((n//2)+1, n)] for i in range((n//2)+1, n)]
    temp4 = [list(i)[::-1] for i in zip(*temp4)]
    for i in range(n//2):
        for j in range(n//2):
            arr[i-(n//2)][j-(n//2)] = temp4[i][j]
    board = arr

def artistry():
    global result, idx_area, visited, temp, matrix
    for _ in range(4):
        idx_area = []
        visited = [[False]*n for _ in range(n)]
        temp = [[int(1e9)]*n for _ in range(n)]
        idx_matrix()
        matrix = [[0]*len(idx_area) for _ in range(len(idx_area))]
        adj_matrix()
        result += get_score()
        rotate()
        
n, board = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
idx_area, result = [], 0
visited = [[False]*n for _ in range(n)]
temp = [[int(1e9)]*n for _ in range(n)]
matrix = [[0]*len(idx_area) for _ in range(len(idx_area))]
artistry()
print(result)