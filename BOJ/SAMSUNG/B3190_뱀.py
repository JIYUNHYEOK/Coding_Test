import sys
from collections import deque
input = sys.stdin.readline

# 보드의 크기 입력 받기
n = int(input().rstrip())

# 사과의 갯수 입력받기
k = int(input().rstrip())

# 보드판 새로 생성
board = [[0]*(n+1) for _ in range(n+1)]

# 보드에 사과의 위치를 1로 표시
for _ in range(k):
    row, col = map(int, input().rstrip().split())
    board[row][col] = 1

# 뱀의 방향 변환 정보 입력 받기
l = int(input().rstrip())
infos = []
for _ in range(l):
    x, c = input().rstrip().split()
    infos.append((int(x), c))

time = 0
# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, info):
    if info == "L":
        direction = (direction-1)%4
    elif info == 'D':
        direction = (direction+1)%4
    return direction

queue = deque()

def simulate():
    x, y = 1, 1
    board[x][y] = 2
    direction = 0
    time = 0
    index = 0
    queue.append((x, y))

    while queue:
        # x, y = queue.popleft()
        nx, ny = x+dx[direction], y+dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx, ny))
                px, py = queue.popleft()
                board[px][py] = 0
            elif board[nx][ny] == 1:
                board[nx][ny] = 2
                queue.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1

        if index < l and time == infos[index][0]:
            direction = turn(direction, infos[index][1])
            index += 1
            
    return time

result = simulate()
print(result)