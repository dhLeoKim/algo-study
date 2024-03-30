import sys
sys.stdin = open('input_11779.txt')
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra(start):
    h = []
    d[start] = 0
    heappush(h, (0, start, [start]))

    while h:
        cost_now, now, lst = heappop(h)

        if d[now] < cost_now:
            continue

        for nxt, w in graph[now]:
            nxt_cost = cost_now + w
            if d[nxt] > nxt_cost:
                d[nxt] = nxt_cost
                temp = lst[:]
                temp.append(nxt)
                d_lst[nxt] = temp
                heappush(h, (nxt_cost, nxt, temp))


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
start, end = map(int, input().split())

INF = 1e11
d = [INF]*(N+1)
d_lst = [[] for _ in range(N+1)]

dijkstra(start)

print(d[end])
print(len(d_lst[end]))
print(*d_lst[end])