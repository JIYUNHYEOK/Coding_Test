## 백준 2667 단지번호붙이기

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

house = 2
def dfs(x, y):
    if matrix[x][y] == 1:
        matrix[x][y] = house
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                dfs(nx, ny)
        return True

count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            house += 1
            count += 1

print(count)

house_size = [0]*count
for i in range(2, count+2):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == i:
                house_size[i-2] += 1

house_size.sort()
for i in house_size:
    print(i)
