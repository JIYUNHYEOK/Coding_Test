# 얼음 틀의 세로길이, 가로길이 입력 받기
n, m = map(int, input().split())

# 얼음 틀 생성
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 얼음의 라벨값 설정
ice = 2

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드 방문
def dfs(x, y):
    # 전역변수인 ice를 사용
    global ice
    # 아직 방문하지 않았을 경우
    if board[x][y] == 0:
        # 노드 방문 처리
        board[x][y] = ice
        # 상하좌우 위치 모두 재귀적으로 호출
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx, ny)
        return True

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
            ice += 1

print(board)