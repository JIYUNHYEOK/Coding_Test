# 삼성 SW 역량테스트 2020 하반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, m, k = map(int, input().rstrip().split())
    board = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, w, s, d = map(int, input().rstrip().split())
        board[x-1][y-1].append((w, s, d))
    return n, m, k, board

def move():
    global board
    for _ in range(k):
        temp1 = [[[] for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if board[x][y]:
                    for i in range(len(board[x][y])):
                        m, s, d = board[x][y][i]
                        # dx, dy = direction[d]
                        nx, ny = (x+direction[d][0]*s)%n, (y+direction[d][1]*s)%n
                        temp1[nx][ny].append((m, s, d))
        board = temp1

        temp2 = [[[] for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                size = len(board[x][y])
                if size == 1:
                    m, s, d = board[x][y][0]
                    temp2[x][y].append((m, s, d))
                elif size >= 2:
                    weight, velocity, odd_cnt, even_cnt = 0, 0, 0, 0
                    for i in range(size):
                        m, s, d = board[x][y][i]
                        weight += m
                        velocity += s
                        if d%2: odd_cnt += 1
                        else: even_cnt += 1
                    weight = (weight//5)
                    velocity = (velocity//size)
                    if weight:
                        if odd_cnt == size or even_cnt == size:
                            for dir in [0, 2, 4, 6]: 
                                temp2[x][y].append((weight, velocity, dir))
                        else:
                            for dir in [1, 3, 5, 7]: 
                                temp2[x][y].append((weight, velocity, dir))
        board = temp2

def get_score():
    score = 0
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                for i in range(len(board[x][y])):
                    score += board[x][y][i][0]
    return score

n, m, k, board = input_data()
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
move()
result = get_score()
print(result)