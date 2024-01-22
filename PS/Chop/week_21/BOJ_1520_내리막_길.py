from sys import stdin, setrecursionlimit
setrecursionlimit(250000)

stdin = open("input/BOJ_1520_내리막_길.txt")

m, n = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(m)]
check = [[-1] * n for _ in range(m)]
check[0][0] = 1
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def dfs(x, y):
    if check[x][y] != -1:  # 방문한 적 있으면 탐색 중지 (중복 탐색을 막음)
        return

    check[x][y] = 0  # 방문 처리

    for i in range(4):  # 인접 노드 방문
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[x][y] < graph[nx][ny]:
                dfs(nx, ny)
                check[x][y] += check[nx][ny]  # 메모이제이션


dfs(m-1, n-1)
print(check[-1][-1])
