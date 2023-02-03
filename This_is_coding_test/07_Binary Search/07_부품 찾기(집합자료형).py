# 7-7 부품 찾기 (집합자료형)

n = int(input())
n_list = set(map(int, input().split()))

for i in input().split():
    n_list[int(i)] = 1

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')