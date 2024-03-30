import sys
sys.stdin = open('input_13023.txt')
input = sys.stdin.readline

def dfs(d, now):
    global ret

    if d == 4:
        ret = 1
        return

    if ret == 1:
        return

    for nxt in lst[now]:
        if not visited[nxt]:
            visited[now] = True
            dfs(d+1, nxt)
            visited[now] = False


N, M = map(int, input().split())
lst = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

visited = [False]*N
ret = 0
for start in range(N):
    dfs(0, start)
    if ret == 1:
        break

print(ret)