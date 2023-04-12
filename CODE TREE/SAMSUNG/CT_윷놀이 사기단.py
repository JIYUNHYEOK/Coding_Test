# 삼성 SW 역량테스트 2019 하반기 오후 2번 문제

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def input_data():
    move_list = [*map(int, input().rstrip().split())]
    return move_list

def shortcut(curr_pos):
    return (curr_pos != START) and (curr_pos % 5 == 0)

def get_next_pos(curr_pos, move_num):
    if curr_pos == END: return END
    if move_num == 0: return curr_pos
    next_pos = curr_pos + 1
    
    if curr_pos in [23, 27, 33]: next_pos = 41
    elif curr_pos == 19: next_pos = 44
    elif curr_pos == 44: next_pos = END
    
    return get_next_pos(next_pos, move_num - 1)

def is_overlapped():
    for i in range(4):
        for j in range(i+1, 4):
            if (curr_pos[i] == curr_pos[j]) and (curr_pos[i] != START) and (curr_pos[i] != END): return True
    return False

def search_max_score(depth, score):
    global result
    
    if depth == 10: result = max(result, score); return
    
    for i in range(4):
        if curr_pos[i] == END: continue
        
        temp = curr_pos[i]    
        if shortcut(curr_pos[i]): curr_pos[i] = get_next_pos(curr_pos[i] + 16, move_list[depth] - 1)
        else: curr_pos[i] = get_next_pos(curr_pos[i], move_list[depth])       
        if not is_overlapped(): search_max_score(depth + 1, score + board[curr_pos[i]])
        curr_pos[i] = temp

board = [
#   0, 1, 2, 3, 4,  5,  6,  7,  8,  9, 10, 11, 12, 23, 14, 15, 16, 17, 18, 19,20 
    0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 0,
#   21, 22, 23,24,25
    13, 16, 19, 0, 0,
#   26, 27,28,29,30
    22, 24, 0, 0, 0,
#   31, 32, 33,34,35
    28, 27, 26, 0, 0,
#  36,37,38,39,40 
    0, 0, 0, 0, 0,
#   41, 42, 43, 44 
    25, 30, 35, 40 
]

move_list = input_data()
START, END = 0, 20
curr_pos = [START, START, START, START]
result = 0
search_max_score(0, 0)
print(result)







