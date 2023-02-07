# 8-8 효율적인 화폐 구성

n, m = map(int, input().split())
money_list = [int(input()) for _ in range(n)]

dp = [10001]*(m+1)

# 다이나믹 프로그래밍 진행 (보텀업)
dp[0] = 0
for i in range(n):
    for j in range(money_list[i], m+1):
        if dp[j-money_list[i]] != 10001:
            dp[j] = min(dp[j], dp[j-money_list[i]]+1)

result = dp[m] if dp[m] != 10001 else -1
print(result)
