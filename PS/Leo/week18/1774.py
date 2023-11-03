import sys
sys.stdin = open('input_1774.txt')
input = sys.stdin.readline

from heapq import heappush, heappop

# def prim(start):
#     mst[start] = True
#     h = []
#     for dist, nxt in graph[start]:
#         heappush(h, (dist, nxt))

#     ret = 0
#     cnt = 0
#     while cnt < N-1:
#         dist, now = heappop(h)
#         if mst[now]:
#             continue
#         mst[now] = True
#         ret += dist
#         cnt += 1
#         for ndist, nxt in graph[now]:
#             if not mst[nxt]:
#                 heappush(h, (ndist, nxt))

#     return ret         


# N, M = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(N)]

# graph = [[] for _ in range(N+1)]
# for u in range(N):
#     for v in range(u+1, N):
#         dist = round(((lst[u][0]-lst[v][0])**2 + (lst[u][1]-lst[v][1])**2 )**(1/2), 4)
#         graph[u+1].append((dist, v+1))
#         graph[v+1].append((dist, u+1))
        
# for _ in range(M):                      # 이미 선택된 정점은 거리 0으로 추가하여 처리
#     u, v = map(int, input().split())
#     graph[u].append((0, v))                 
#     graph[v].append((0, u))

# mst = [False]*(N+1)
# ret = prim(1)

# print(f'{ret:.2f}')


############################################


def find(x):
    if p[x] < 0:
        return x
    return find(p[x])


def union(u, v):
    pu = find(u)
    pv = find(v)
    if p[pu] == p[pv]:
        p[pu] -= 1
    if p[pu] < p[pv]:
        p[pv] = pu
    else:
        p[pu] = pv


def kruskal():
    ret = 0
    for dist, u, v in edge:
        if find(u) == find(v):
            continue
        ret += dist
        union(u, v)
    
    return ret


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
edge = []
for u in range(N):
    for v in range(u+1, N):
        dist = round(((lst[u][0]-lst[v][0])**2 + (lst[u][1]-lst[v][1])**2 )**(1/2), 4)
        edge.append((dist, u+1, v+1))

for _ in range(M):                      # 이미 선택된 정점은 거리 0으로 추가하여 처리
    u, v = map(int, input().split())
    edge.append((0, u, v))

edge.sort()
p = [-1]*(N+1)

ret = kruskal()

print(f'{ret:.2f}')