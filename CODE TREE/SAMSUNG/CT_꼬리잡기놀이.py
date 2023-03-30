# 삼성 SW 역량테스트 2022 상반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m, k = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    start_axis = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
    return n, m, k, board, start_axis

def bfs(row, col):
    team, value = deque([(row, col)]), deque([board[row][col]])
    visited = [[False]*n for _ in range(n)]
    queue = deque([(row, col)])
    visited[row][col] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            if not board[nx][ny]: continue
            if board[nx][ny] - board[x][y] <= 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                team.append((nx, ny))
                value.append(board[nx][ny])
    return team, value

def make_rail():
    team_list, value_list, team_len = [], [], []
    for i in range(len(start_axis)):
        team, value = bfs(*start_axis[i])
        team_list.append([team, 1])
        value_list.append(value)
        team_len.append(len([item for item in value if item <= 3]))
    return team_list, value_list, team_len

def move():
    global board
    temp = [[0]*n for _ in range(n)]
    for i in range(len(team_list)):
        team_list[i][0].rotate(team_list[i][1])
        for j in range(len(team_list[i][0])):
            x, y = team_list[i][0][j]
            temp[x][y] = value_list[i][j]
    board = temp

def get_score(time):
    global result
    stage = time%(4*n)
    if stage < n:
        for i in range(n):
            if 1 <= board[stage][i] <= 3:
                result += (search_num(stage, i)**2)
                flag = False
                for x in range(len(team_list)):
                    if (stage, i) in team_list[x][0]:
                        value_list[x] = deque(list(value_list[x])[:team_len[x]][::-1] + list(value_list[x])[team_len[x]:])
                        team_list[x][1] *= -1
                        flag = True
                        break
                if flag: break
    elif stage < 2*n:
        for i in range(n-1, -1, -1):
            if 1 <= board[i][stage-n] <= 3:
                result += (search_num(i, stage-n)**2)
                flag = False
                for x in range(len(team_list)):
                    if (i, stage-n) in team_list[x][0]:
                        value_list[x] = deque(list(value_list[x])[:team_len[x]][::-1] + list(value_list[x])[team_len[x]:])
                        team_list[x][1] *= -1
                        flag = True
                        break
                if flag: break
    elif stage < 3*n:
        for i in range(n-1, -1, -1):
            if 1 <= board[3*n-stage-1][i] <= 3:
                result += (search_num(3*n-stage-1, i)**2)
                flag = False
                for x in range(len(team_list)):
                    if (3*n-stage-1, i) in team_list[x][0]:
                        value_list[x] = deque(list(value_list[x])[:team_len[x]][::-1] + list(value_list[x])[team_len[x]:])
                        team_list[x][1] *= -1
                        flag = True
                        break
                if flag: break
    elif stage < 4*n:
        for i in range(n):
            if 1 <= board[i][4*n-stage-1] <= 3:
                result += (search_num(i, 4*n-stage-1)**2)
                flag = False
                for x in range(len(team_list)):
                    if (i, 4*n-stage-1) in team_list[x][0]:
                        value_list[x] = deque(list(value_list[x])[:team_len[x]][::-1] + list(value_list[x])[team_len[x]:])
                        team_list[x][1] *= -1
                        flag = True
                        break
                if flag: break

def search_num(row, col):
    queue = deque([(row, col, 1)])
    visited = [[False]*n for _ in range(n)]
    visited[row][col] = True

    while queue:
        x, y, cnt = queue.popleft()
        if board[x][y] == 1: return cnt
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((0 <= nx < n) and (0 <= ny < n)): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == 4: continue
            if not board[nx][ny]: continue
            if board[x][y] == 3 and board[nx][ny] == 1: continue
            if board[nx][ny]-board[x][y] <= 1:
                queue.append((nx, ny, cnt+1))
                visited[nx][ny] = True
    return 0

n, m, k, board, start_axis = input_data()
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0

team_list, value_list, team_len = make_rail()

for time in range(k):
    move()
    get_score(time)
print(result)