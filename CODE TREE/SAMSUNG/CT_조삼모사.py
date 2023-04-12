# 삼성 SW 역량테스트 2017 하반기 오전 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    board = [[*map(int, input().rstrip().split())] for _ in range(n)]
    return n, board

def dfs(depth, start, n_list):
    global result
    if depth == n//2:
        team1, team2 = n_list, [i for i in range(n) if i not in n_list]
        sum1, sum2 = 0, 0
        for i in range(n//2):
            for j in range(i+1, n//2):
                sum1 += board[team1[i]][team1[j]]+board[team1[j]][team1[i]]
                sum2 += board[team2[i]][team2[j]]+board[team2[j]][team2[i]]
        result = min(result, abs(sum1-sum2))
        return
    
    for i in range(start, n):
        dfs(depth+1, i+1, n_list+[i])

n, board = input_data()
result = int(1e9)
dfs(0, 0, [])
print(result)