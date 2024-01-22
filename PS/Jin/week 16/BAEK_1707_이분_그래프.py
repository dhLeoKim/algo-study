import sys
from collections import deque

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    adjList = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().strip().split())
        adjList[u].append(v)
        adjList[v].append(u)

    def bfs(i, visited_num):
        q = deque([i])
        visited[i] = visited_num
        while q:
            x = q.popleft()
            for nxt in adjList[x]:
                if not visited[nxt]:
                    visited[nxt] = -1 * visited[x]
                    q.append(nxt)
                elif visited[nxt] == visited[x]:
                    return False
        return True


    for i in range(1, V+1):
        if not visited[i]:
            res = bfs(i, 1)
            if not res:
                print('NO')
                break
    else:
        print('YES')