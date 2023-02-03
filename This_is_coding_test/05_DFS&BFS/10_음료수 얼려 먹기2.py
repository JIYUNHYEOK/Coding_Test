# 필요한 모듈 불러오기
import sys

# 입력값 한줄씩 받기
input = sys.stdin.readline

# 얼음 틀의 세로길이, 가로길이 입력받기
n, m = map(int, input().rstrip().split())
# board = [map(int, input().rstrip().split()) for _ in range(n)]

# 얼음 틀 생성
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))

# 둘레를 1로 감싼 확장된 얼음틀 생성 (1은 움직일 수 없는 벽)
board_extension = [[1]*(m+2) for _ in range(n+2)]
for i in range(1, len(board_extension)-1):
        for j in range(1, len(board_extension[i])-1):
            board_extension[i][j] = board[i-1][j-1]

# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 얼음을 기존과 다른 숫자로 표현
# 각기 다른 얼음을 구분하기 위함
ice = 2

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드 방문
def dfs(x,y):
    global ice

    # 아직 방문하지 않았을 경우
    if board_extension[x][y] == 0:

        # 각 구역별 얼음을 표시
        board_extension[x][y] = ice

        # 상하좌우의 위치를 탐색
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 상하좌우 위치를 모두 재귀적으로 탐색 -> 0과 붙어있는 모든 구역에 대해 얼음으로 영역 표시
            dfs(nx,ny)

        # 만약 0인 구역이 존재할 경우 True로 표시
        return True

# 얼음의 갯수
count = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        # DFS 알고리즘을 통해 얼음의 갯수를 파악
        # 0인 구역이 존재할 경우 해당 경우는 모두 같은 얼음으로 간주하고
        # 탐색이 끝나면 다른 얼음과 구분하기 위해 ice값에 1을 새로 더해줌
        if dfs(i,j):
            ice += 1
            count += 1

# 얼음이라고 표시한 값들을 모두 포함하기 위한 리스트
area = []

# 확장된 구역에서 얼음을 모두 리스트에 담기
for i in range(len(board_extension)):
    for j in range(len(board_extension[i])):
        if board_extension[i][j] > 1:
            area.append(board_extension[i][j])

# 각 얼음의 순서를 정렬
area.sort()

# 각 얼음의 값을 하나씩 표현하기 위해 집합으로 표현
area_set = set(area)

# 각 얼음에 대한 갯수를 담는 리스트
result = []

# 각 얼음에 대한 크기를 포함
for i in area_set:
    result.append(area.count(i))

print(f"얼음의 갯수: {count}")
print("얼음의 넓이: ", end = '')
print(*result)

