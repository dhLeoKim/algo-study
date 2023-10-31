import sys
sys.stdin = open('input_1162.txt')
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra(now):
    h = []
    d[now][0] = 0
    heappush(h, (0, now, 0))

    while h:
        dist, now, k = heappop(h)
        if dist > d[now][k]:
            continue
        for nxt, w in graph[now]:
            ndist = dist + w
            if ndist < d[nxt][k]:                   # 포장하지 않는 경우
                d[nxt][k] = ndist
                heappush(h, (ndist, nxt, k))
            if k < K and dist < d[nxt][k+1]:        # 포장하는 경우
                d[nxt][k+1] = dist
                heappush(h, (dist, nxt, k+1))


N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

INF = 1e11                                  # INF = 1e9로 설정시 오답발생 -> 문제 읽고 최대값 확인하기
d = [[INF]*(K+1) for _ in range(N+1)]       # d[i][j] : j번 포장했을 때, i번 노드까지 가는 최소값

dijkstra(1)
print(min(d[N]))