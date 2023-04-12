# 삼성 SW 역량테스트 2021 상반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    like_dict = dict()
    for _ in range(n**2):
        n_list = [*map(int, input().rstrip().split())]
        like_dict[n_list[0]] = n_list[1:]
    return n, like_dict

def select_pos():
    global board
    for i in like_dict.keys():
        temp_list = []
        for x in range(n):
            for y in range(n):
                if board[x][y]: continue
                cnt, blank_cnt = 0, 0
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if not ((0 <= nx < n) and (0 <= ny < n)): continue
                    if board[nx][ny] in like_dict[i]: cnt += 1
                    if board[nx][ny] == 0: blank_cnt += 1
                temp_list.append((cnt, blank_cnt, x, y))
        temp_list.sort(key= lambda x: (-x[0], -x[1], x[2], x[3]))
        board[temp_list[0][2]][temp_list[0][3]] = i

def get_score():
    score = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if not ((0 <= nx < n) and (0 <= ny < n)): continue
                if board[nx][ny] in like_dict[board[x][y]]: cnt += 1
            if cnt: score += (10**(cnt-1))
    return score

n, like_dict = input_data()
board = [[0]*n for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
select_pos()
result = get_score()
print(result)