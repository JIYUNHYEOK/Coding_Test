# 7-6 부품 찾기 (계수정렬)

n = int(input())
n_list = [0]*1000001

for i in input().split():
    n_list[int(i)] = 1

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if n_list[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')