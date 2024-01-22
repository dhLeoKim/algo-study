from sys import stdin

stdin = open("input/BOJ_1976_여행_가자.txt")

n = int(stdin.readline())
m = int(stdin.readline())
tree = [i for i in range(n+1)]


def find(n):
    if tree[n] != n:
        tree[n] = find(tree[n])
    return tree[n]


def union(node1, node2):
    anc1 = find(node1)
    anc2 = find(node2)
    tree[anc2] = anc1

def find_path(path):
    ans = find(path[0])
    for p in path:
        if find(p) != ans:
            print("NO")
            return
    print("YES")


for i in range(n):
    edges = list(map(int, stdin.readline().rstrip().split()))
    for j in range(n):
        if edges[j] == 1: union(i+1, j+1)

path = list(map(int, stdin.readline().rstrip().split()))
find_path(path)