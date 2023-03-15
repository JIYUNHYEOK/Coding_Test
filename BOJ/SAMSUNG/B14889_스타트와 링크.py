# 백준 14889 스타트와 링크

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [False] * n

result = int(1e9)
def solution(cnt, start):
    global result

    if cnt == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        result = min(result, abs(start-link))

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            solution(cnt+1, i+1)
            visited[i] = False

solution(0, 0)
print(result)
