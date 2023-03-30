# 삼성 SW 역량테스트 2022 상반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

# 1. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장
# 2. 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행
    # 각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식 
# 3. 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제
    # 4개의 대각선 방향으로 k칸만큼 전파
    # 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라짐
    # 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지
    # 만약 박멸시키는 나무의 수가 동일한 칸이 있는 경우에는 행이 작은 순서대로, 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됨
# 4. 3개의 과정이 1년에 걸쳐 진행된다고 했을 때, m년 동안 총 박멸한 나무의 그루 수를 구하는 프로그램

def input_data():
    n, m, k, c = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    wall_list = [(i, j) for i in range(n) for j in range(n) if board[i][j] == -1]
    return n, m, k, c, board, wall_list

def growth():
    global board
    temp = [item[:] for item in board]
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0:
                cnt = 0
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if not ((0 <= nx < n) and (0 <= ny < n)): continue
                    if board[nx][ny] <= 0: continue
                    cnt += 1
                temp[x][y] += cnt
    board = temp

def breed():
    global board
    temp = [item[:] for item in board]
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0:
                cnt = 0
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if not ((0 <= nx < n) and (0 <= ny < n)): continue
                    if board[nx][ny]: continue
                    if board[nx][ny] < 0: continue
                    cnt += 1
                if cnt:
                    tree = board[x][y]//cnt
                    for dx, dy in direction:
                        nx, ny = x+dx, y+dy
                        if not ((0 <= nx < n) and (0 <= ny < n)): continue
                        if board[nx][ny]: continue
                        if board[nx][ny] < 0: continue
                        temp[nx][ny] += tree
    board = temp

def select_herbicide():
    global result, board
    temp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0:
                temp[x][y] += board[x][y]
                for dx, dy in direction_diag:
                    for i in range(1, k+1):
                        nx, ny = x+dx*i, y+dy*i
                        if not ((0 <= nx < n) and (0 <= ny < n)): break
                        if (nx, ny) in wall_list: break
                        if board[nx][ny] <= 0: break
                        if board[nx][ny] > 0: temp[x][y] += board[nx][ny]

    max_val = max(map(max, temp))
    herbicide_list = []
    for i in range(n):
        for j in range(n):
            if temp[i][j] == max_val:
                herbicide_list.append((temp[i][j], i, j))
    herbicide_list.sort(key=lambda x: (-x[0], x[1], x[2]))

    herbicide = herbicide_list[0]
    result += herbicide[0]

    temp = [item[:] for item in board]
    temp[herbicide[1]][herbicide[2]] = -(c+1)
    for dx, dy in direction_diag:
        for i in range(1, k+1):
            flag = False
            nx, ny = herbicide[1]+dx*i, herbicide[2]+dy*i
            if not ((0 <= nx < n) and (0 <= ny < n)): break
            if (nx, ny) in wall_list: break
            if board[nx][ny] <= 0: flag = True
            temp[nx][ny] = -(c+1)
            if flag: break
    board = temp

def recover_herbicide():
    global board
    for i in range(n):
        for j in range(n):
            if board[i][j] < 0:
                if (i, j) in wall_list: continue
                board[i][j] += 1

n, m, k, c, board, wall_list = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_diag = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
result = 0

for _ in range(m):
    growth()
    breed()
    select_herbicide()
    recover_herbicide()
print(result)