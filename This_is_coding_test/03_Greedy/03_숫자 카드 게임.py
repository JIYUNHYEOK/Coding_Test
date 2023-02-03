n, m = map(int, input().split())

result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
   
print(result)