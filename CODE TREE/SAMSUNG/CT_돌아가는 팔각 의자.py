# 삼성 SW 역량테스트 2017 하반기 오후 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    queue1 = deque([*map(int, input().rstrip())])
    queue2 = deque([*map(int, input().rstrip())])
    queue3 = deque([*map(int, input().rstrip())])
    queue4 = deque([*map(int, input().rstrip())])
    k = int(input().rstrip())
    rotate_infos = [[*map(int, input().rstrip().split())] for _ in range(k)]
    return queue1, queue2, queue3, queue4, k, rotate_infos

def rotate(n, d):
    if n == 1:
        if queue1[2] != queue2[-2]:
            if queue2[2] != queue3[-2]:
                if queue3[2] != queue4[-2]: queue4.rotate(-d)
                queue3.rotate(d)
            queue2.rotate(-d)
        queue1.rotate(d)
    elif n == 2:
        if queue1[2] != queue2[-2]: queue1.rotate(-d)
        if queue2[2] != queue3[-2]:
            if queue3[2] != queue4[-2]: queue4.rotate(d)
            queue3.rotate(-d)
        queue2.rotate(d)
    elif n == 3:
        if queue3[2] != queue4[-2]: queue4.rotate(-d)
        if queue2[2] != queue3[-2]:
            if queue1[2] != queue2[-2]: queue1.rotate(d)
            queue2.rotate(-d)
        queue3.rotate(d)
    elif n == 4:
        if queue4[-2] != queue3[2]:
            if queue3[-2] != queue2[2]:
                if queue2[-2] != queue1[2]: queue1.rotate(-d)
                queue2.rotate(d)
            queue3.rotate(-d)
        queue4.rotate(d)
        
def simulate():
    result = 0
    for n, d in rotate_infos:
        rotate(n, d)
    result = queue1[0] + queue2[0]*2 + queue3[0]*4 + queue4[0]*8
    return result

queue1, queue2, queue3, queue4, k, rotate_infos = input_data()
result = simulate()
print(result)