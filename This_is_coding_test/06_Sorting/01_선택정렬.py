# 6-1 선택정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 원소를 넣을 인덱스
    min_idx = i
    # 가장 작은 원소를 넣을 인덱스를 제외하고 그 뒤에만 탐색
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)