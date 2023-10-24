import sys
sys.stdin = open('input_22856.txt')
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 문제 조건 : 유사 중위 순회의 끝은 (진짜)중위 순회할 때 마지막 노드
def inorder(now):   
    global endNode

    if lc[now] != -1: inorder(lc[now])
    endNode = now
    if rc[now] != -1: inorder(rc[now])


def similarInorder(now):
    global ret

    if lc[now] != -1:
        similarInorder(lc[now])
        ret += 1

    if now == endNode:
        print(ret)
        exit()
    ret += 1

    if rc[now] != -1:
        similarInorder(rc[now])
        ret += 1


N = int(input())
lc = [-1]*(N+1)
rc = [-1]*(N+1)

for _ in range(N):
    a, b, c = map(int, input().split())
    lc[a] = b
    rc[a] = c

inorder(1)
# print(endNode)

ret = 0
similarInorder(1)