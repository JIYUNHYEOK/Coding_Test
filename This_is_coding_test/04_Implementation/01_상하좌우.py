n = int(input())
x, y= 1, 1
moves = input().split()

# L, R, U, D 순서로 방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(len(direction)):
        if move == direction[i]:
            nx, ny = x + dx[i], y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x,y  = nx, ny

print(x, y)