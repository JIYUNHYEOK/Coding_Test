# 삼성 SW 역량테스트 2021 하반기 오후 2번 문제

import sys, copy
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
from collections import deque

def input_data():
    n, k = map(int, input().rstrip().split())
    queue_list = [deque([*map(int, input().rstrip().split())])]
    return n, k, queue_list

# 1. 밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어줍니다.(가장 작은 위치가 여러 개라면 모두 넣기)
def add_flour():
    min_val = min(queue_list[0])
    for i in range(len(queue_list[0])):
        if queue_list[0][i] == min_val: queue_list[0][i] += 1

# 2. 도우를 말아줍니다.
def roll_dough():
    global queue_list
    left_flour = queue_list[0].popleft()
    queue_list.append(deque([left_flour]))

    while len(queue_list) <= len(queue_list[0])-len(queue_list[-1]):
        temp_list = []
        for _ in range(len(queue_list[-1])):
            temp = deque()
            for i in range(len(queue_list)):
                temp.append(queue_list[i].popleft())
            temp_list.append(temp)
        queue_list = [queue_list[0]]
        for i in range(len(temp_list)-1, -1, -1):
            queue_list.append(temp_list[i])

# 3. 도우를 꾹 눌러줍니다.
def press_dough():
    global queue_list
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    temp = copy.deepcopy(queue_list)

    for x in range(len(queue_list)):
        for y in range(len(queue_list[x])):
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if nx >= 0 and ny >= 0:
                    try:
                        diff = queue_list[nx][ny] - queue_list[x][y]
                        if diff >= 5: temp[x][y] += (diff//5)
                        elif diff <= -5: temp[x][y] -= ((diff*(-1))//5)
                    except: continue
    
    queue_list = [deque()]
    size = len(temp[-1])
    for _ in range(size):
        for x in range(len(temp)):
            queue_list[0].append(temp[x].popleft())
    while temp[0]: queue_list[0].append(temp[0].popleft())

# 4. 도우를 두 번 반으로 접어줍니다.
def fold_dough():
    global queue_list
    for i in range(len(queue_list)-1, -1, -1):
        temp = deque()
        for _ in range(len(queue_list[i])//2):
            temp.appendleft(queue_list[i].popleft())
        queue_list.append(temp)

# 5. 3의 과정만 한번 더 반복합니다.

def solution():
    result = 0
    while True:
        add_flour()
        roll_dough()
        press_dough()
        fold_dough()
        fold_dough()
        press_dough()
        result += 1
        min_val, max_val = min(map(min, queue_list)), max(map(max, queue_list))
        if max_val - min_val <= k: return result

n, k, queue_list = input_data()
result = solution()
print(result)