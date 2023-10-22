from sys import stdin

stdin = open("input/BOJ_22856_트리_순회.txt")

N = int(stdin.readline().rstrip())

tree = {}
edges = 0

for _ in range(N):
    n, l, r = map(int, stdin.readline().rstrip().split())
    tree[n] = [l, r]
    for e in [l, r]:
        edges += 1 if e > 0 else 0

now, depth = 1, 0
while True:
    if tree[now][1] > 0:
        depth += 1
        now = tree[now][1]
    else:
        break

ans = 2 * edges - depth

print(ans)
