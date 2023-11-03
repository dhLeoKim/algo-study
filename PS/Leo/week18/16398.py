import sys
sys.stdin = open('input_16398.txt')
input = sys.stdin.readline

from heapq import heappush, heappop

# def prim(start):
#     ret = 0
#     h = []
#     mst[start] = True
#     for i in range(N):
#         if graph[start][i] == 0: continue
#         heappush(h, (graph[start][i], i))

#     cnt = 0
#     while cnt < N-1:
#         cost, now = heappop(h)
#         if mst[now]:
#             continue
#         mst[now] = True
#         ret += cost
#         cnt += 1
#         for nxt in range(N):
#             if not mst[nxt] and graph[now][nxt]:
#                 heappush(h, (graph[now][nxt], nxt))

#     return ret

# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]

# mst = [False]*(N+1)

# print(prim(0))


######################################


# def prim(start):
#     mst[start] = True
#     h = []
#     for cost, nxt in graph[start]:
#         heappush(h, (cost, nxt))

#     ret = 0
#     cnt = 0
#     while cnt < N-1:
#         cost, now = heappop(h)
#         if mst[now]:
#             continue
#         mst[now] = True
#         ret += cost
#         cnt += 1
#         for ncost, nxt in graph[now]:
#             if not mst[nxt]:
#                 heappush(h, (ncost, nxt))
        
#     return ret


# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
# graph = [[] for _ in range(N+1)]
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         graph[i+1].append((lst[i][j], j+1))

# mst = [False]*(N+1)
# print(prim(1))


######################################

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
    for w, u, v in edge:
        if find(u) == find(v):
            continue
        ret += w
        union(u, v)

    return ret


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
edge = []
for i in range(N):
    for j in range(i+1, N):
        edge.append((lst[i][j], i, j))

edge.sort()
p = [-1]*(N+1)

print(kruskal())