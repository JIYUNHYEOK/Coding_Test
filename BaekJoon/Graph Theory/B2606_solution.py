## 백준 2606 바이러스

n = int(input())
t = int(input())
infos = []
edges = [[]]

for _ in range(t):
    infos.append(list(map(int, input().split())))

for i in range(1, n+1):
    nodes = []
    for a, b in infos:
        if i == a:
            nodes.append(b)
        if i == b:
            nodes.append(a)
    edges.append(nodes)

result = []
def dfs(graph, v, visited):
    global result
    visited[v] = True
    result.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return result

visited = [False] * (n+1)
result = dfs(edges, 1, visited)
result.remove(1)
print(len(result))

