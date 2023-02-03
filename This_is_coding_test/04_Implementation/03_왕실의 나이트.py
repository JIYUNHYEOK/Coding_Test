position = list(input())
x, y = int(ord(position[0])-96), int(position[1])

# 나이트가 움직일 수 있는 범위
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

cnt = 0
for i in range(8):
    nx, ny = x + dx[i], y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)