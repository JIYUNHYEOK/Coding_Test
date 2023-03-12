# 13458 시험 감독

import sys
input = sys.stdin.readline

n = int(input().rstrip())
n_list = list(map(int, input().rstrip().split()))
b, c = map(int, input().rstrip().split())

result = 0
for num in n_list:
    if num >= b:
        num -= b
        if num % c == 0:
            result += num//c
        else:
            result += (num//c) + 1

print(result)