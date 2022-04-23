n,m,k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
num1 = data[n-1] # max
num2 = data[n-2] # second max

result = 0

while(True):
  for i in range(k): # 최대 더할 수 있는 횟수
    if m==0: # 숫자가 더해지는 횟수
      break
    result += num1
    m -= 1

  if m==0:
    break
  result += num2 # 최대 더할 수 있는 횟수 종료 후 두번째로 큰 수 더하기
  m -= 1

print(result)