from sys import stdin

stdin = open("input/BOJ_1717_집합의_표현.txt")

n, m = map(int, stdin.readline().rstrip().split())

tree = [i for i in range(n+1)]

# 각 집합의 대표노드를 찾는 함수
def find(n):
    if tree[n] != n:
        tree[n] = find(tree[n])
    return tree[n]

# 두 개의 집합을 합치는 함수
def union(node1, node2):
    anc1 = find(node1)
    anc2 = find(node2)
    tree[anc2] = anc1

for _ in range(m):
    q, a, b = map(int, stdin.readline().rstrip().split())
    if q == 0:
        union(a, b)
    else:
        if find(a) == find(b) : print("YES")
        else: print("NO")
        
print(tree)
