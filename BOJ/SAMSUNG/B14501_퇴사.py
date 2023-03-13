# 백준 14501 퇴사

import sys
input = sys.stdin.readline

n = int(input().rstrip())

T, P = [0]*n, [0]*n
for i in range(n):
    T[i], P[i] = map(int, input().rstrip().split())

dp = [0] * (n+1)
for i in range(len(T)-1, -1, -1):
    tmp = i + T[i]
    if tmp <= n:
        dp[i] = max(dp[tmp]+P[i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])