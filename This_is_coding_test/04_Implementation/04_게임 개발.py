## 개인 풀이
n, m = map(int, input().split())
x, y, d = map(int, input().split())
cnt, result = 0, 1

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

direction = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}

while cnt < 4:
    cnt = 0
    for _ in range(4):
        nx, ny = x + direction[d][0], y + direction[d][1]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if board[nx][ny] == 0:
                x, y = nx, ny
                result += 1
                board[x][y] = 1
                break
        
        cnt += 1
        d = (d+1)%4

print(result)

## 함수화 풀이
# 행렬의 크기 N,M을 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위해 맵을 만들고 0으로 초기화
visit = [[0]*m for _ in range(n)]

# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())

# 현재 좌표 방문을 처리
visit[x][y] = 1

# 전체 맵의 정보를 입력받기
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 방향전환하는 함수 생성
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:

    # 왼쪽으로 회전
    turn_left()
    nx, ny = x + dx[direction], y + dy[direction]

    # 회전 이후에 정면에 가보지 않은 칸이 존재하는 경우
    if visit[nx][ny] == 0 and board[nx][ny] == 0:
        visit[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue

    # 회전 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 4방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx, ny = x - dx[direction], y - dy[direction]

        # 뒤로 갈 수 있는 경우에는 뒤로 이동
        if board[nx][ny] == 0:
            x, y= nx, ny

        # 뒤가 바다로 막혀 있다면
        else:
            break
        turn_time = 0

print(count)

