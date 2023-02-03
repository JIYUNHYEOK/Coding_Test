## 백준 11724 연결 요소의 개수

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

visited = [0]*(n+1)
edges = []
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)

result = 0
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        result += 1

print(result)
