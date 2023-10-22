from sys import stdin
from collections import deque

stdin = open("input/BOJ_1707_이분_그래프.txt")

K = int(stdin.readline().rstrip())
for _ in range(K):
    V, E = map(int, stdin.readline().rstrip().split())
    graph = [[] for _ in range(V+1)]
    visited = [1] + [0 for _ in range(V)]
    ans = "YES"

    for edge in range(E):
        a, b = map(int, stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(node):
        global cnt
        q = deque([(node, 1)])

        while q:
            (now, level) = q.popleft()
            visited[now] = level

            if graph[now]:
                for next in graph[now]:
                    if not visited[next]:
                        visited[next] = -level
                        q.append((next, -level))
                    elif visited[next] != -level:
                        return "NO"
            else: return "YES"
        return "YES"

    for node in range(1, V):
        if not visited[node]:
            ans = bfs(node)
            if ans == "NO" : break

    print(ans)


        