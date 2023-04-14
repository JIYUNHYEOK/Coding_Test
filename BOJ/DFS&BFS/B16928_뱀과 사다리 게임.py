# 백준 16928 뱀과 사다리 게임

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, m = map(int, input().rstrip().split())
    pre, curr = [], []
    for _ in range(n+m):
        x, y = map(int, input().rstrip().split())
        pre.append(x); curr.append(y)
    return n, m, pre, curr

def bfs():
    queue = deque([(1, 0)])

    while queue:
        new_queue = deque()
        for _ in range(len(queue)):
            pos, cnt = queue.popleft()
            for step in range(1, 7):
                next_pos = pos+step
                if next_pos > 100: break
                if next_pos in pre: next_pos = curr[pre.index(next_pos)]
                if next_pos == 100: return cnt+1
                if (next_pos, cnt+1) not in new_queue: new_queue.append((next_pos, cnt+1))
        queue = new_queue

n, m, pre, curr = input_data()
result = bfs()
print(result)