import sys
sys.stdin = open('input_1197.txt')
input = sys.stdin.readline

####################################
# 1. prim

# from heapq import heappop, heappush

# def prim(start):
#     mst[start] = True
#     h = []
#     for w, v in graph[start]:
#         heappush(h, (w, v))                     # u와 연결된 간선 우선순위 큐에 추가

#     ret = 0
#     cnt = 0
#     while cnt < N-1:                            # N-1개가 추가될 때까지 반복
#         w, v = heappop(h)
#         if mst[v]:                              # mst에 포함된 정점을 연결한 간선이면 continue
#             continue
#         mst[v] = True                           # mst에 포함되지 않은 정점을 연결하는 간선이면, mst에 추가
#         ret += w
#         cnt += 1
#         for nw, nv in graph[v]:                 # v와 연결된 정점중
#             if not mst[nv]:                     # mst에 포함되지 않은 정점을 연결하는 간선을 우선순위 큐에 추가
#                 heappush(h, (nw, nv))

#     return ret


# N, E = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u].append((w, v))
#     graph[v].append((w, u))

# mst = [False]*(N+1)
# print(prim(1))


####################################
# 2. kruskal

def find(x):                                    # 부모 찾기
    if p[x] < 0:
        return x
    return find(p[x])


def union(u, v):                                # 합치기
    pu = find(u)
    pv = find(v)
    if p[pu] == p[pv]:                          # 랭크가 같다면 한쪽을 -1
        p[pu] -= 1
    if p[pu] < p[pv]:                           # 랭크가 낮은 쪽으로 합치기
        p[pv] = pu
    else:
        p[pu] = pv


def kruskal():
    ret = 0
    for w, u, v in edge:
        if find(u) == find(v):                  # 같은 그룹이면 continue
            continue
        ret += w                                # 다른 그룹이면 최소 신장 트리 추가
        union(u, v)                             # 같은 그룹으로 변경

    return ret


N, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((w, u, v))                      # 간선 배열

edge.sort()                                     # 비용 기준으로 오름차순
p = [-1]*(N+1)                                  # 부모 배열, rank -1로 초기화

print(kruskal())