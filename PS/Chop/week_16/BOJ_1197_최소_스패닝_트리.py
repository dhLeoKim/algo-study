from sys import stdin
from heapq import *

stdin = open("input/BOJ_1197_최소_스패닝_트리.txt")

# # 크루스칼 알고리즘
# # 특정 원소가 속한 집합을 찾기
# def find_parent(p, x):
#     if p[x] != x:
#         p[x] = find_parent(p, p[x])
#     return p[x]

# # 두 원소가 속한 집합을 합치기
# def union_parent(p, a, b):
#     a = find_parent(p, a)
#     b = find_parent(p, b)
#     if a < b:
#         p[b] = a
#     else:
#         p[a] = b

# V, E = map(int, stdin.readline().rstrip().split())
# p = [0] * (V+1)
# edges = []
# res = 0

# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1, V+1):
#     p[i] = i

# # 간선을 입력받아 coat를 기준으로 오름차순 정렬
# for _ in range(E):
#     a, b, cost = map(int, stdin.readline().rstrip().split())
#     edges.append((cost, a, b))

# edges.sort()

# # 정렬된 간선을 하나씩 확인
# for e in edges:
#     cost, a, b = e
#     # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로  
#     if find_parent(p, a) != find_parent(p, b):
#         # 신장 트리에 간선 추가
#         union_parent(p, a, b)
#         res += cost

# print(res)

# 프림 알고리즘

def prim(start, weight):
    visit = [0] * (V + 1) # 정점 방문 처리
    q = [[weight, start]] # 힙 구조를 사용하기 위해 가중치를 앞에 둠
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수
    while cnt < V: # 간선의 개수 최대는 V-1
        k, v = heappop(q)
        if visit[v]: continue # 이미 방문한 정점이면 지나감
        visit[v] = 1 # 방문안했으면 방문처리
        ans += k # 해당 정점까지의 가중치를 더해줌
        cnt += 1 # 간선의 갯수 더해줌
        for u, w in G[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [w, u]) # 힙에 넣어줌
    return ans

V, E = map(int, stdin.readline().rstrip().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, stdin.readline().rstrip().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(prim(1, 0))