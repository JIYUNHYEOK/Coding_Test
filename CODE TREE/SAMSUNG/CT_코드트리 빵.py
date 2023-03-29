# 삼성 SW 역량테스트 2022 하반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    infos = [[n+1, n+1]] + [[*map(lambda x: int(x)-1, input().rstrip().split())] for _ in range(m)]
    return n, m, board, infos

def search_basecamp(num):
    queue = deque([(infos[num][0], infos[num][1], 0)])
    visit_temp = [[False]*n for _ in range(n)]
    while queue:
        basecamp = []
        for _ in range(len(queue)):
            x, y, cnt = queue.popleft()
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if not ((0 <= nx < n) and (0 <= ny < n)): continue
                if visit_temp[nx][ny]: continue
                if visited[nx][ny]: continue
                if board[nx][ny] == 1: basecamp.append((nx, ny))
                visit_temp[nx][ny] = True
                queue.append((nx, ny, cnt+1))
        if basecamp: return sorted(basecamp, key= lambda x: (x[0], x[1]))[0]

def shortest_path(row, col, num): # visit: [(row, col)]
    queue = deque([(row, col, [])])
    visit_temp = [[False]*n for _ in range(n)]
    while queue:
        store = []
        for _ in range(len(queue)):
            x, y, dir = queue.popleft()
            for i in range(len(direction)):
                nx, ny = x+direction[i][0], y+direction[i][1]
                if not ((0 <= nx < n) and (0 <= ny < n)): continue
                if visit_temp[nx][ny]: continue
                if visited[nx][ny]: continue
                if [nx, ny] == infos[num]: store.append((nx, ny, dir+[i]))
                visit_temp[nx][ny] = True
                queue.append((nx, ny, dir+[i]))
        if store: return sorted(store, key= lambda x: (x[2][0]))[0][2][0]

n, m, board, infos = input_data()
visited = [[False]*n for _ in range(n)]
direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
time, cnt = 0, 0
arrive = [False]*m
start = [[] for _ in range(m+1)]

while True:
    for i in range(1, len(start)):
        if not arrive[i-1] and start[i]:
            dir = shortest_path(start[i][0], start[i][1], i)
            start[i] = [start[i][0]+direction[dir][0], start[i][1]+direction[dir][1]]
            if start[i] == infos[i]: 
                arrive[i-1] = True
                visited[infos[i][0]][infos[i][1]] = True
    if time < m:
        if not start[time+1]:
            start[time+1] = search_basecamp(time+1)
            visited[start[time+1][0]][start[time+1][1]] = True
  
    time += 1
    if sum(arrive) == m:
        break

print(time)