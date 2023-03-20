# 백준 14503 로봇 청소기

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
row, col, direction = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(n)]



