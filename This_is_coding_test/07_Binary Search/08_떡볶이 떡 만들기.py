# 7-8 떡볶이 떡 만들기

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start, end = 0, max(arr)

# 이진탐색 수행 (반복적)
result = 0
while start <= end:
    total = 0
    # 자르는 크기
    mid = (start+end)//2
    for i in arr:
        # 절단 후 떡의 양 계산
        if i > mid:
            total += (i-mid)
    # 떡의 양이 부족한 경우, 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid-1
    # 떡의 양이 충분한 경우, 덜 자르기 (오른쪽 부분 탐색)
    else:
        # 최대한 덜 자르는 것이 목표: 해당 부분에서 result를 기록
        result = mid
        start = mid+1
    
print(result)