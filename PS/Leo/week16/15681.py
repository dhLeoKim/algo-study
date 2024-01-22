import sys
sys.stdin = open('input_15681.txt')
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(now):
    visited[now] = 1
    for nxt in tree[now]:
        if not visited[nxt]:
            dfs(nxt)
            visited[now] += visited[nxt]


N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [0]*(N+1)
dfs(R)

for _ in range(Q):
    u = int(input())
    print(visited[u])