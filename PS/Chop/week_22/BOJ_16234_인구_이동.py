from sys import stdin
from collections import deque

stdin = open("input/BOJ_16234_인구_이동.txt")

n, l, r = map(int, stdin.readline().rstrip().split())
population = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(a, b):
    global flag
    cnt = population[a][b]
    q = deque([(a, b)])
    idxArr = [(a, b)]

    while q:
        [x, y] = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(population[x][y] - population[nx][ny]) <= r :
                flag = True
                visited[nx][ny] = True
                cnt += population[nx][ny]
                q.append((nx, ny))
                idxArr.append((nx, ny))

    avg = cnt / len(idxArr)

    for (i, j) in idxArr:
        population[i][j] = avg

flag = True
ans = -1

while flag:
    flag = False  # 이 줄을 while 루프 안쪽으로 이동시킵니다.
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
    ans += 1
print(ans)

    

                

