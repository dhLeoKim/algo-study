import sys
sys.stdin = open('input_1707.txt')
input = sys.stdin.readline

from collections import deque

def bfs(now):
    queue = deque()
    queue.append(now)
    visited[now] = 1
    
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if visited[nxt] == 0:
                visited[nxt] = -visited[now]
                queue.append(nxt)
            else:
                if visited[nxt] == visited[now]:
                    return False

    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0]*(V+1)

    for i in range(1, V+1):
        # 그래프가 2개 이상일수도 있음, 모두 이분그래프인지 확인!
        if visited[i] == 0:
            ret = bfs(i)
            if not ret:         # 하나라도 아니라면 NO 출력
                break
    
    print('YES' if ret else 'NO')