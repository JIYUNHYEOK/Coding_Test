## 숫자가 작을 때까지만 해당
n, k = map(int, input().split())
cnt = 0

while n >= k:
    while n%k != 0:
        n -= 1
        cnt += 1
    n //= k
    cnt += 1

while n>1:
    n -= 1
    cnt += 1

print(cnt)

## N의 범위가 10만보다 클 경우
n, k = map(int, input().split())
cnt = 0

while True:
    # n이 k로 나누어질 때까지 1을 빼기
    target = (n//k)*k
    cnt += (n-target)
    n = target

    # n이 k보다 작을 때, 즉 더이상 나눌 수 없을 때 반복문 탈출
    if n < k:
        break
    
    # n으로 나누기
    n /= k
    cnt += 1

# 마지막에 1로 만들기
cnt += (n-1)
print(cnt)