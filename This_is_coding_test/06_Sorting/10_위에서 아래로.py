# 6-10 위에서 아래로

n = int(input())
n_list = [int(input()) for _ in range(n)]

print(*sorted(n_list, reverse=True))