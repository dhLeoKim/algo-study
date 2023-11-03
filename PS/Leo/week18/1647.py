import sys
sys.stdin = open('input_1647.txt')
input = sys.stdin.readline

# from heapq import heappop, heappush

# def prim(start):
#     mst[start] = True
#     h = []
#     for cost, nxt in graph[start]:
#         heappush(h, (cost, nxt))

#     max_val = 0
#     ret = 0
#     cnt = 0
#     while cnt < N-1:
#         cost, now = heappop(h)
#         if mst[now]:
#             continue
#         mst[now] = True
#         ret += cost
#         cnt += 1
#         if cost > max_val:
#             max_val = cost
#         for ncost, nxt in graph[now]:
#             if not mst[nxt]:
#                 heappush(h, (ncost, nxt))

#     return ret, max_val


# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     u, v, w = map(int, input().split())
#     graph[u].append((w, v))
#     graph[v].append((w, u))

# mst = [False]*(N+1)
# ret, max_val = prim(1)

# print(ret-max_val)


##########################################


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
    max_val = 0
    ret = 0
    for u, v, w in edge:
        if find(u) == find(v):
            continue
        ret += w
        if w > max_val:
            max_val = w
        union(u, v)

    return ret, max_val


N, M = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(M)]
edge.sort(key=lambda x:x[2])

p = [-1]*(N+1)
ret, max_val = kruskal()
print(ret-max_val)