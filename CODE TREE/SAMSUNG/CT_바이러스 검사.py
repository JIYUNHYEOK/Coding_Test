# 삼성 SW 역량테스트 2015 하반기 1번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    n = int(input().rstrip())
    n_list = [*map(int, input().rstrip().split())]
    num1, num2 = map(int, input().rstrip().split())
    return n, n_list, num1, num2

n, n_list, num1, num2 = input_data()
result = n
for i in range(len(n_list)):
    if n_list[i] > num1:
        cnt, rem = divmod(n_list[i]-num1, num2)
        if rem: result += (cnt+1)
        else: result += cnt
print(result)