# 8-6 개미 전사

# 정수 N 입력받기
n = int(input())

# 모든 식량 정보 입력받기
k = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
dp = [0] * 100

# 다이나믹 프로그래밍 진행 (보텀업)
dp[0] = k[0]
dp[1] = max(k[0], k[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+k[i])

print(dp[n-1])

