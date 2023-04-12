# 삼성 SW 역량테스트 2017 하반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n, l = map(int, input().rstrip().split())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, l, board

def check_line(road):
    slope = [False] * n
    for i in range(1, n):
        if abs(road[i] - road[i-1]) > 1: return False
        if road[i] < road[i-1]:
            for j in range(l):
                if (i+j >= n) or (road[i] != road[i+j]) or (slope[i+j]): return False
                if road[i] == road[i+j]: slope[i+j] = True
        elif road[i] > road[i-1]:
            for j in range(l):
                if (i-j-1 < 0) or (road[i-1] != road[i-j-1]) or (slope[i-j-1]): return False
                if road[i-1] == road[i-j-1]: slope[i-j-1] = True
    return True

def simulate():
    result = 0
    for i in range(n):
        if check_line([board[i][j] for j in range(n)]): result += 1
        if check_line([board[j][i] for j in range(n)]): result += 1
    return result

n, l, board = input_data()
result = simulate()
print(result)