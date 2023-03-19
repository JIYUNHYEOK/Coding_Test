# 백준 14888 연산자 끼워넣기

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().rstrip().split()))
operator = list(map(int, input().rstrip().split()))

min_val, max_val = int(1e9), int(-1e9)
def solution(num, idx, add, sub, mul, div):
    global min_val, max_val

    if idx == n:
        min_val = min(num, min_val)
        max_val = max(num, max_val)
        return
    
    if add > 0:
        solution(num + data[idx], idx+1, add-1, sub, mul, div)
    if sub > 0:
        solution(num - data[idx], idx+1, add, sub-1, mul, div)
    if mul > 0:
        solution(num * data[idx], idx+1, add, sub, mul-1, div)
    if div > 0:
        if num < 0:
            solution((num*(-1) // data[idx])*(-1), idx+1, add, sub, mul, div-1)
        else:
            solution(num // data[idx], idx+1, add, sub, mul, div-1)
    
solution(data[0], 1, operator[0], operator[1], operator[2], operator[3])
print(max_val)
print(min_val)