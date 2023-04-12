# 삼성 SW 역량테스트 2021 하반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m, k = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    # wall_list = [tuple(map(int, input().rstrip().split())) for _ in range(m)]
    wall_list = []
    for _ in range(m):
        x, y, d = map(int, input().rstrip().split())
        wall_list.append((x-1, y-1, d))
    return n, m, k, board, wall_list

def isrange(x, y):
    if not ((0 <= x < n) and (0 <= y < n)): return False
    return True

# 벽이 에어컨 바로 옆에 주어지는 경우는 없으며, 벽이 외벽에 포함되게 주어지는 경우 역시 없다고 가정
def air_conditioner(x, y, num):
    visited = [[False]*n for _ in range(n)]

    if num == 2:
        queue = deque([(x, y-1, 5)])
        
        while queue:
            x, y, temp = queue.popleft()
            if visited[x][y]: continue
            visited[x][y] = True
            temp_arr[x][y] += temp
            if temp <= 1: continue

            # 왼쪽
            if isrange(x, y-1) and ((x, y, 1) not in wall_list) and (not visited[x][y-1]):
                queue.append((x, y-1, temp-1))
            # 왼쪽 위
            if isrange(x-1, y-1) and (((x-1, y, 1) not in wall_list) and ((x, y, 0) not in wall_list)) and (not visited[x-1][y-1]):
                queue.append((x-1, y-1, temp-1))
            # 왼쪽 아래
            if isrange(x+1, y-1) and (((x+1, y, 1) not in wall_list) and ((x+1, y, 0) not in wall_list)) and (not visited[x+1][y-1]):
                queue.append((x+1, y-1, temp-1))
            
    if num == 3:
        queue = deque([(x-1, y, 5)])
        
        while queue:
            x, y, temp = queue.popleft()
            if visited[x][y]: continue
            visited[x][y] = True
            temp_arr[x][y] += temp
            if temp <= 1: continue

            # 위쪽
            if isrange(x-1, y) and ((x, y, 0) not in wall_list) and (not visited[x-1][y]):
                queue.append((x-1, y, temp-1))
            # 왼쪽 위
            if isrange(x-1, y-1) and (((x, y, 1) not in wall_list) and ((x, y-1, 0) not in wall_list)) and (not visited[x-1][y-1]):
                queue.append((x-1, y-1, temp-1))
            # 오른쪽 위
            if isrange(x-1, y+1) and (((x, y+1, 1) not in wall_list) and ((x, y+1, 0) not in wall_list)) and (not visited[x-1][y+1]):
                queue.append((x-1, y+1, temp-1))

    if num == 4:
        queue = deque([(x, y+1, 5)])

        while queue:
            x, y, temp = queue.popleft()
            if visited[x][y]: continue
            visited[x][y] = True
            temp_arr[x][y] += temp
            if temp <= 1: continue

            # 오른쪽
            if isrange(x, y+1) and ((x, y+1, 1) not in wall_list) and (not visited[x][y+1]):
                queue.append((x, y+1, temp-1))
            # 오른쪽 위
            if isrange(x-1, y+1) and ((x, y, 0) not in wall_list) and ((x-1, y+1, 1) not in wall_list) and (not visited[x-1][y+1]):
                queue.append((x-1, y+1, temp-1))
            # 오른쪽 아래
            if isrange(x+1, y+1) and ((x+1, y, 0) not in wall_list) and ((x+1, y+1, 1) not in wall_list) and (not visited[x+1][y+1]):
                queue.append((x+1, y+1, temp-1))

    if num == 5:
        queue = deque([(x+1, y, 5)])
        
        while queue:
            x, y, temp = queue.popleft()
            if visited[x][y]: continue
            visited[x][y] = True
            temp_arr[x][y] += temp
            if temp <= 1: continue

            # 아래쪽
            if isrange(x+1, y) and ((x+1, y, 0) not in wall_list) and (not visited[x+1][y]):
                queue.append((x+1, y, temp-1))
            # 왼쪽 아래
            if isrange(x+1, y-1) and (((x, y, 1) not in wall_list) and ((x+1, y-1, 0) not in wall_list)) and (not visited[x+1][y-1]):
                queue.append((x+1, y-1, temp-1))
            # 오른쪽 아래
            if isrange(x+1, y+1) and (((x, y+1, 1) not in wall_list) and ((x+1, y+1, 0) not in wall_list)) and (not visited[x+1][y+1]):
                queue.append((x+1, y+1, temp-1))

def adjust():
    global temp_arr
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    temp = [item[:] for item in temp_arr]

    for x in range(n):
        for y in range(n):
            for i in range(len(direction)):
                nx, ny = x+direction[i][0], y+direction[i][1]
                if not isrange(nx, ny): continue

                diff = (temp_arr[x][y] - temp_arr[nx][ny]) // 4
                if diff <= 0 : continue
                if (i == 0) and ((x, y, 0) in wall_list): continue
                if (i == 1) and ((nx, ny, 0) in wall_list): continue
                if (i == 2) and ((x, y, 1) in wall_list): continue
                if (i == 3) and ((nx, ny, 1) in wall_list): continue
                temp[x][y] -= diff
                temp[nx][ny] += diff

    temp_arr = temp

    for i in range(n):
        if temp_arr[i][0] > 0:
            temp_arr[i][0] -= 1
        if temp_arr[i][n-1] > 0:
            temp_arr[i][n-1] -= 1
    for i in range(1, n-1):
        if temp_arr[0][i] > 0:
            temp_arr[0][i] -= 1
        if temp_arr[n-1][i] > 0:
            temp_arr[n-1][i] -= 1

def simulate():
    global time
    while True:
        time += 1
        for x, y, num in machines:
            air_conditioner(x, y, num)
        adjust()

        cnt = 0
        for i, j in room:
            if temp_arr[i][j] >= k: cnt += 1
        if cnt == len(room): return time
        if time > 100: return -1

n, m, k, board, wall_list = input_data()
temp_arr = [[0]*n for _ in range(n)]
room = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
machines = [(i, j, board[i][j]) for i in range(n) for j in range(n) if 1 < board[i][j] < 6]
time = 0
result = simulate()
print(result)