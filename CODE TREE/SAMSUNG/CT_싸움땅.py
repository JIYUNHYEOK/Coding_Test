# 삼성 SW 역량테스트 2022 하반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, k = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    matrix = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j].append(board[i][j])
    player_infos, player_map = [], [[0]*n for _ in range(n)]
    for player_num in range(1, m+1):
        x, y, d, s = map(int, input().rstrip().split())
        player_infos.append([x-1, y-1, d, s, 0])
        player_map[x-1][y-1] = player_num
    return n, m, k, matrix, player_infos, player_map

n, m, k, matrix, player_infos, player_map = input_data()
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = [0]*m

for stage in range(1, k+1):
    for i in range(len(player_infos)):
        x, y, d, s, gun = player_infos[i]
        player_map[x][y] = 0
        nx, ny = x+direction[d][0], y+direction[d][1]
        if not ((0 <= nx < n) and (0 <= ny < n)):
            d = (d+2)%4
            nx, ny = x+direction[d][0], y+direction[d][1]
        meet = False
        for j in range(len(player_infos)):
            if i == j: continue
            if (nx, ny) == (player_infos[j][0], player_infos[j][1]):
                meet = True
                new_x, new_y, new_d, new_s, new_gun = player_infos[j]
                stat, new_stat = s+gun, new_s+new_gun
                if (stat > new_stat) or ((stat == new_stat) and (s > new_s)):
                    result[i] += (stat-new_stat)
                    matrix[nx][ny].append(gun)
                    matrix[nx][ny].append(new_gun)
                    matrix[nx][ny].sort()
                    gun = matrix[nx][ny].pop()
                    for dir in range(4):
                        next_d = (new_d+dir)%4
                        next_x, next_y = new_x+direction[next_d][0], new_y+direction[next_d][1]
                        if not ((0 <= next_x < n) and (0 <= next_y < n)): continue
                        if player_map[next_x][next_y]: continue
                        matrix[next_x][next_y].sort()
                        new_gun = matrix[next_x][next_y].pop() if matrix[next_x][next_y] else 0
                        break
                    player_map[nx][ny], player_map[next_x][next_y] = i+1, j+1
                    player_infos[i] = [nx, ny, d, s, gun]
                    player_infos[j] = [next_x, next_y, next_d, new_s, new_gun]
                elif stat < new_stat or ((stat == new_stat) and (s < new_s)):
                    result[j] += (new_stat-stat)
                    matrix[nx][ny].append(gun)
                    matrix[nx][ny].append(new_gun)
                    matrix[nx][ny].sort()
                    new_gun = matrix[nx][ny].pop()
                    for dir in range(4):
                        next_d = (d+dir)%4
                        next_x, next_y = nx+direction[next_d][0], ny+direction[next_d][1]
                        if not ((0 <= next_x < n) and (0 <= next_y < n)): continue
                        if player_map[next_x][next_y]: continue
                        matrix[next_x][next_y].sort()
                        gun = matrix[next_x][next_y].pop() if matrix[next_x][next_y] else 0
                        break
                    player_map[nx][ny], player_map[next_x][next_y] = j+1, i+1
                    player_infos[i] = [next_x, next_y, next_d, s, gun]
                    player_infos[j] = [nx, ny, new_d, new_s, new_gun]
                break

        if not meet:
            if matrix[nx][ny]:
                matrix[nx][ny].append(gun)
                matrix[nx][ny].sort()
                gun = matrix[nx][ny].pop()
            player_infos[i] = [nx, ny, d, s, gun]
            player_map[nx][ny] = i+1
        
print(*result)
