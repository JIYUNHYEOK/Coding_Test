# 시간초과가 걸릴 수 있는 코드
n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
max1, max2 = lst[-1], lst[-2]

cnt = 0
result = 0
for i in range(m):
    cnt += 1
    if cnt >= k:
        cnt = 0
        result += max2
    else:
        result += max1

print(result)

# 수정 코드
n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
max1, max2 = lst[-1], lst[-2]

# 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += count * max1
result += (m-count) * max2

print(result)