# 삼성 SW 역량테스트 2020 상반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m, c = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    car = [*map(lambda x: int(x)-1, input().rstrip().split())]
    start_info, end_info = [], []
    for _ in range(m):
        x_s, y_s, x_e, y_e = [*map(lambda x: int(x)-1, input().rstrip().split())]
        start_info.append([x_s, y_s]); end_info.append([x_e, y_e])
    return n, m, c, board, car, start_info, end_info

def search_passenger(start):
    queue = deque([start])
    visited = [[0]*n for _ in range(n)]
    visited[start[0]][start[1]] = 1
    passenger_list = []

    while queue:
        x, y = queue.popleft()
        if [x, y] in start_info: 
            if passenger_list and visited[x][y]-1 > passenger_list[-1][0]: break
            passenger_list.append((visited[x][y]-1, x, y))
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == 1: continue
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y]+1
    if passenger_list: return sorted(passenger_list, key=lambda x: (x[0], x[1], x[2]))[0]

def move(start, end):
    queue = deque([start])
    visited = [[0]*n for _ in range(n)]
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()
        if [x, y] == end: return visited[x][y]-1
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == 1: continue
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y]+1
    return -1

def simulate():
    global car
    result = c
    for _ in range(m):
        next_info = search_passenger(car)
        if not next_info: return -1
        if next_info[0] > result: return -1
        result -= next_info[0]
        idx = start_info.index([next_info[1], next_info[2]])
        start, end = start_info.pop(idx), end_info.pop(idx)
        dist = move(start, end)
        if dist == -1: return -1
        if dist > result: return -1
        car = end
        result += dist
    return result

n, m, c, board, car, start_info, end_info = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = simulate()
print(result)