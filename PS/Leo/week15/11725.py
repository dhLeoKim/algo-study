import sys
sys.stdin = open('input_11725.txt')
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(now):
    for nxt in tree[now]:
        if not visited[nxt]:
            visited[nxt] = now
            dfs(nxt)


from collections import deque

def bfs(now):
    queue = deque()
    queue.append(now)

    while queue:
        now = queue.popleft()
        for nxt in tree[now]:
            if not visited[nxt]:
                visited[nxt] = now
                queue.append(nxt)


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [0]*(N+1)
dfs(1)
bfs(1)

for i in range(2, N+1):
    print(visited[i])