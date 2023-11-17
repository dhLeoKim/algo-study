import sys
from collections import deque

# bfs + 이분탐색
def bfs(start, end, weight):
    q = deque()
    visited = [0] * (N+1)
    q.append(start)
    visited[start] = 1
    while q:
        x = q.popleft()
        if x == end:
            return True
        for i, w in adjList[x]:
            if not visited[i] and w >= weight:
                visited[i] = 1
                q.append(i)
    return False

N, M = map(int, input().split())
adjList = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    adjList[A].append((B, C))
    adjList[B].append((A, C))
# 가중치가 큰 순서대로 정렬
for i in range(N+1):
    adjList[i].sort(key=lambda x:(x[0], -x[1]))
i1, i2 = map(int, input().split())
# 이분탐색
low, high = 1, 100000000000000
while low <= high:
    mid = (low + high) // 2
    if bfs(i1, i2, mid):
        res = mid
        low = mid + 1
    else:
        high = mid - 1
print(res)