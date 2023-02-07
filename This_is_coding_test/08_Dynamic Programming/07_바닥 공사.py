# 8-7 바닥 공사

n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
dp = [0]*1001

# 다이나믹 프로그래밍 진행 (보텀업)
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 796796


print(dp[n])