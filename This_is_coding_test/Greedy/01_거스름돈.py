# 거스름돈 입력받기
n = int(input())

# 거슬러 줘야 할 동전 갯수
count = 0

# 동전의 종류
coins = [500, 100, 50, 10]

# 가장 큰 동전부터 거슬러주기
# 거슬러주는 횟수만큼 더하고, 남은 금액은 작은 동전으로 넘기기
for coin in coins:
    count += (n//coin)
    n %= coin

# 거슬로 줘야하는 동전 갯수 출력
print(count)