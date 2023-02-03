# 7-5 부품 찾기 (이진탐색)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return None

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()
for i in m_list:
    result = binary_search(n_list, i, 0, len(n_list)-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')