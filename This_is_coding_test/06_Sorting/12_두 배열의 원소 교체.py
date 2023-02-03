# 6-12 두 배열의 원소 교체

n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

for _ in range(k):
    a_list.sort()
    b_list.sort()
    
    if a_list[0] < b_list[-1]:
        a_list[0], b_list[-1] = b_list[-1], a_list[0]

print(sum(a_list))