# 삼성 SW 역량테스트 2020 하반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, k = map(int, input().rstrip().split())
    rail = deque([*map(int, input().rstrip().split())])
    return n, k, rail

def simulate():
    time = 0
    arr = deque([0 for _ in range(n)])
    while True:
        if rail.count(0) >= k: return time

        if arr[n-1]: arr[n-1] = 0
        arr.rotate(1)
        rail.rotate(1)

        arr[n-1] = 0
        for i in range(n-2, -1, -1):
            if not arr[i]: continue
            if arr[i+1]: continue
            if rail[i+1] >= 1:
                rail[i+1] -= 1
                arr[i], arr[i+1] = 0, 1
        
        if rail[0] >= 1 and not arr[0]:
            arr[0] = 1
            rail[0] -= 1
        time += 1

n, k, rail = input_data()
result = simulate()
print(result)
