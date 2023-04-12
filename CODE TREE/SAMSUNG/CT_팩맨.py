# 삼성 SW 역량테스트 2021 하반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    m, t = map(int, input().rstrip().split())
    r, c = map(lambda x: int(x)-1, input().rstrip().split())
    pos_infos = [[*map(lambda x: int(x)-1, input().rstrip().split())] for _ in range(m)]
    return m, t, r, c, pos_infos

def simulate():
    global board, pos_infos, dead_board, r, c
    
    # 1. 몬스터 복제 시도
    temp_pos = [item[:] for item in pos_infos]

    # 2. 몬스터 이동
    # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
    arr = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if board[x][y]:
                for i in range(len(board[x][y])):
                    for d in range(8):
                        nd = (board[x][y][i]+d)%8
                        dx, dy = direction[nd]
                        nx, ny = x+dx, y+dy
                        if not ((0 <= nx < 4) and (0 <= ny < 4)): continue
                        if (nx, ny) == (r, c): continue
                        if dead_board[nx][ny]: continue
                        arr[nx][ny].append(nd)
                        break
                    else:
                        arr[x][y].append(board[x][y][i])
    board = arr

    # 3. 팩맨 이동
    move_list = []
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                nx1, ny1 = r + delta[d1][0], c + delta[d1][1]
                if not ((0 <= nx1 < 4) and (0 <= ny1 < 4)): continue
                nx2, ny2 = nx1 + delta[d2][0], ny1 + delta[d2][1]
                if not ((0 <= nx2 < 4) and (0 <= ny2 < 4)): continue
                nx3, ny3 = nx2 + delta[d3][0], ny2 + delta[d3][1]
                if not ((0 <= nx3 < 4) and (0 <= ny3 < 4)): continue
                cnt = len(board[nx1][ny1]) + len(board[nx2][ny2]) + len(board[nx3][ny3])
                if (nx1, ny1) == (nx2, ny2): cnt -= len(board[nx1][ny1])
                if (nx1, ny1) == (nx3, ny3): cnt -= len(board[nx1][ny1])
                if (nx2, ny2) == (nx3, ny3): cnt -= len(board[nx2][ny2])
                move_list.append((cnt, d1, d2, d3))
    move_list.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    move_dir = move_list[0][1:]
    for d in move_dir:
        r += delta[d][0]; c += delta[d][1]
        if board[r][c]: dead_board[r][c] = 3; board[r][c] = []

    # 4. 몬스터 시체 소멸
    for i in range(4):
        for j in range(4):
            if dead_board[i][j]: dead_board[i][j] -= 1

    # 5. 몬스터 복제 완성
    for x, y, d in temp_pos:
        board[x][y].append(d)

    new_pos = []
    for x in range(4):
        for y in range(4):
            if board[x][y]:
                for i in range(len(board[x][y])):
                    new_pos.append((x, y, board[x][y][i]))
    pos_infos = new_pos

m, t, r, c, pos_infos = input_data()
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
board = [[[] for _ in range(4)] for _ in range(4)]
dead_board = [[0]*4 for _ in range(4)]
for x, y, d in pos_infos:
    board[x][y].append(d)

for _ in range(t):
    simulate()

result = 0
for i in range(4):
    for j in range(4):
        result += len(board[i][j])

print(result)