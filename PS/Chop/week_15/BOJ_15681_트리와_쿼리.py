from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

stdin = open("input/BOJ_15681_트리와_쿼리.txt")

N, R, Q = map(int, stdin.readline().rstrip().split())

tree = {}
sub_tree = {}

for _ in range(N-1):
    a, b = map(int, stdin.readline().rstrip().split())
    if tree.get(a):
        tree[a].append(b)
    else:
        tree[a] = [b]
    if tree.get(b):
        tree[b].append(a)
    else:
        tree[b] = [a]

quests = [int(stdin.readline().rstrip()) for _ in range(Q)]
root = quests[0]

def make_tree(node, parent):
    if tree.get(node):
        sub_tree[node] = 1
        for son in tree[node]:
            if son != parent:
                make_tree(son, node)
                sub_tree[node] += sub_tree[son]
    else:
        sub_tree[node] = 1

make_tree(R, R)

for q in quests:
    print(sub_tree[q])