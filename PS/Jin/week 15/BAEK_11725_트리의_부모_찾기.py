import sys

# 자기 호출 개수 제한
sys.setrecursionlimit(10**6)

N = int(input())
con = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    con[a].append(b)
    con[b].append(a)

def dfs(d):
    for i in con[d]:
        if visited[i] == 0:
            visited[i] = d
            dfs(i)

dfs(1)
for i in range(2, N+1):
    print(visited[i])