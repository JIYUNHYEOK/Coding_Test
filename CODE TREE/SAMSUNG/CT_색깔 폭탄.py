# 삼성 SW 역량테스트 2021 상반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, m, board

def bfs(row, col):
    global visited
    bomb_list = [(board[row][col], row, col)]
    queue = deque([(row, col)])
    visited[row][col] = True
    color = board[row][col]
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if board[nx][ny] == -1: continue
            if board[nx][ny] == -2: continue
            if visited[nx][ny]: continue
            elif board[nx][ny] == color or board[nx][ny] == 0:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
                bomb_list.append((board[nx][ny], nx, ny))
    if cnt >= 2:
        bomb_list.sort(key = lambda x: (-x[0], -x[1], x[2]))

        red_cnt = 0
        for c, x, y in bomb_list:
            if c == 0: visited[x][y] = False; red_cnt += 1

        return [cnt, red_cnt, bomb_list[0][1], bomb_list[0][2], bomb_list]
    else: return 0

def gravity():
    global board
    temp = [[-2]*n for _ in range(n)]
    for y in range(n):
        idx = n-1
        for x in range(n-1, -1, -1):
            if board[x][y] == -1:
                temp[x][y] = -1
                idx = x-1
            elif board[x][y] >= 0:
                temp[idx][y] = board[x][y]
                idx -= 1
    board = temp

def rotate():
    global board
    temp = deque()
    for row in zip(*board):
        temp.appendleft(list(row))
    board = list(temp)

def simulate():
    global visited, board, result
    while True:
        visited = [[False]*n for _ in range(n)]
        bomb_list = []
        # 1. 폭탄 크기의 묶음 집합을 구함
        for x in range(n):
            for y in range(n):
                if visited[x][y]: continue
                if board[x][y] > 0:
                    cnt = bfs(x, y)
                    if cnt: bomb_list.append(cnt)

        if not bomb_list: return result

        # 2. 폭탄 묶음을 선택
        bomb_list.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

        # 3. 폭탄을 제거
        bomb = bomb_list[0][4]

        for _, x, y in bomb:
            board[x][y] = -2
        result += len(bomb)**2

        # 4. 중력 작용
        gravity()

        # 5. 반시계 방향으로 90도 회전
        rotate()

        # 6. 중력작용
        gravity()

n, m, board = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*n for _ in range(n)]
result = 0
simulate()
print(result)