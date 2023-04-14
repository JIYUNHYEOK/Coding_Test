# SWEA 2382 미생물 격리

# import sys
# # input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, k = map(int, input().rstrip().split())
    board = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        x, y, c, d = map(int, input().rstrip().split())
        board[x][y].append([c, d-1])
    return n, m, k, board

def move():
    global board
    temp = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                for i in range(len(board[x][y])):
                    cnt, dir = board[x][y][i]
                    nx, ny = x+direction[dir][0], y+direction[dir][1]
                    if (nx == 0) or (ny == 0) or (nx == n-1) or (ny == n-1):
                        cnt //= 2
                        if dir == 0 or dir == 1: dir = (1-dir)
                        else: dir = (5-dir)
                    temp[nx][ny].append([cnt, dir])
        
    for x in range(n):
        for y in range(n):
            if len(temp[x][y]) >= 2:
                temp[x][y].sort(key=lambda x: -x[0])
                dir = temp[x][y][0][1]
                cnt = 0
                for i in range(len(temp[x][y])):
                    cnt += temp[x][y][i][0]
                temp[x][y] = [[cnt, dir]]
    board = temp

def count_microbe():
    result = 0
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                result += board[x][y][0][0]
    return result

def simulate():
    for _ in range(m):
        move()
        result = count_microbe()
    return result

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
t = int(input().rstrip())
for tc in range(1, t+1):
    n, m, k, board = input_data()
    result = simulate()
    print(f"#{tc} {result}")