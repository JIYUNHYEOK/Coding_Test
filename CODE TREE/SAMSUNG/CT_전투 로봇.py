# 삼성 SW 역량테스트 2019 하반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n = int(input().rstrip())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, board

def search():
    monster_list = []
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                if board[i][j] == 9: start = (i, j)
                else: monster_list.append((i, j))
    return start, monster_list

def bfs(start):
    queue = deque([start])
    visited = [[0]*n for _ in range(n)]
    visited[start[0]][start[1]] = 1

    attack_list = []
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if not ((0 <= nx < n) and (0 <= ny < n)): continue
                if visited[nx][ny]: continue
                if board[nx][ny] > size: continue
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if (0 < board[nx][ny] < size) and ((nx, ny) in monster_list):
                    attack_list.append((visited[nx][ny]-1, nx, ny))
        if attack_list:
            attack_list.sort(key=lambda x: (x[0], x[1], x[2]))
            return attack_list[0][0], (attack_list[0][1], attack_list[0][2])

def simulate():
    global start, size
    result, cnt = 0, 0
    while True:
        next_info = bfs(start)
        if next_info:
            board[start[0]][start[1]] = 0
            time, start = next_info
            board[start[0]][start[1]] = 9
            cnt += 1
            result += time
        else:
            return result
        if cnt == size:
            size += 1
            cnt = 0

n, board = input_data()
start, monster_list = search()
size = 2
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = simulate()
print(result)