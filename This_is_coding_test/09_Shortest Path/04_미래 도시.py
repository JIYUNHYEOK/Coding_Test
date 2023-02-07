# 9-4 미래 도시
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b: graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b], graph[b][a] = 1, 1

x, k = map(int, input().rstrip().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k]+graph[k][x] if (graph[1][k]+graph[k][x] < INF) else -1
print(distance)
