## 백준 1697 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
visited = [0] * 100001

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()

        if x == k:
            break

        else:
            for nx in [x-1, x+1, 2*x]:
                if 0 <= nx <= 100000 and visited[nx] == 0:
                    visited[nx] = (visited[x] + 1)
                    queue.append(nx)

    return visited[x]

print(bfs(n))
