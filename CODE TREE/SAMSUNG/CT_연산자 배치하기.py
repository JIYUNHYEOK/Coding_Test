# 삼성 SW 역량테스트 2017 하반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    num_list = [*map(int, input().rstrip().split())]
    add, sub, mul = map(int, input().rstrip().split())
    return n, num_list, add, sub, mul

def calculate(depth, add, sub, mul, tot):
    global min_val, max_val
    if depth == n-1:
        min_val, max_val = min(min_val, tot), max(max_val, tot)
        return
    
    if add >= 1:
        calculate(depth+1, add-1, sub, mul, tot+num_list[depth+1])
    if sub >= 1:
        calculate(depth+1, add, sub-1, mul, tot-num_list[depth+1])
    if mul >= 1:
        calculate(depth+1, add, sub, mul-1, tot*num_list[depth+1])
    

n, num_list, add, sub, mul = input_data()
min_val, max_val = int(1e9), int(-1e9)
calculate(0, add, sub, mul, num_list[0])
print(min_val, max_val)