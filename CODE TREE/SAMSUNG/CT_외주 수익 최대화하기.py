# 삼성 SW 역량테스트 2017 상반기 오전 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    work_list = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, work_list

def dfs(depth, tot):
    global result
    if depth == n:
        result = max(result, tot)
        return
    dfs(depth+1, tot)
    if depth + work_list[depth][0] <= n: dfs(depth+work_list[depth][0], tot+work_list[depth][1])

n, work_list = input_data()
result = int(-1e9)
dfs(0, 0)
print(result)