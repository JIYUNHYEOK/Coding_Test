from collections import deque

n, m = map(int, input().split())

# 미로 생성
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 상, 하, 좌, 우로 이동할 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4방향으로 확인
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 범위를 벗어났을 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우
            if board[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우만 최단 거리 기록
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른 쪽 아래까지의 최단 거리 반환
    return board[n-1][m-1]

print(bfs(0,0))