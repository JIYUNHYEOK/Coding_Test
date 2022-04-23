# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    # n을 k로 나눈 몫에 다시 k를 곱하는 방식 
    # -> 만약 n이 k로 나누어 떨어지지 않을 경우, 가장 가까운 k로 나누어 떨어지는 수를 찾을 수 있음
    target = (n // k) * k 
    # 총 연산을 수행하는 횟수 (1을 빼는 연산을 몇 번 할지를 계산하여 한 번에 넣어줌)
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
