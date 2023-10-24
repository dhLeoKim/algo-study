import sys
sys.stdin = open('input_1240.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append((start, 0))
    visited = [False]*(N+1)
    visited[start] = True

    while queue:
        now, now_w = queue.popleft()
        for nxt, nxt_w in tree[now]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, now_w + nxt_w))
                if nxt == end:
                    return now_w + nxt_w


N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))