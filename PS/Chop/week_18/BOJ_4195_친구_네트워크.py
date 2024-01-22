from sys import stdin
from collections import defaultdict

stdin = open("input/BOJ_4195_친구_네트워크.txt")

def find(n):
    if tree[n] == []:
        tree[n] = [n, 1]
    if tree[n][0] != n:
        tree[n] = find(tree[n][0])
    return tree[n]

def union(node1, node2):
    anc1 = find(node1)[0]
    anc2 = find(node2)[0]
    if anc1[0] != anc2[0]:
        tree[anc2][0] = anc1
        tree[anc1][1] += tree[anc2][1] 

T = int(stdin.readline())

for _ in range(T):
    F = int(stdin.readline())
    tree = defaultdict(list)
    for _ in range(F):
        a, b = stdin.readline().rstrip().split()
        union(a, b)
        print(find(b)[1])
