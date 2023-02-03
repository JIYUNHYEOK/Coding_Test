# 백준 14502 연구소

import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]
result = []
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 깊이 우선 탐색 (DFS)를 통해 각 바이러스가 사방으로 퍼지도록 함
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상, 하, 좌, 우 중 바이러스가 퍼질 수도 있는 경우
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스를 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)


# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
    score = 0

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score


# 깊이 우선 탐색 (DFS)를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result

    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(count + 1)
                board[i][j] = 0


dfs(0)
print(result)
