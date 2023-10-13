import sys
sys.stdin = open('input_2533.txt')
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(now):
    visited[now] = True

    for nxt in tree[now]:
        if not visited[nxt]:
            dfs(nxt)
            dp[now][0] += dp[nxt][1]     # 자신이 얼리 어답터가 아닌 경우 : 자식 노드가 무조건 얼리 어답터여야 함
            dp[now][1] += min(dp[nxt])   # 자신이 얼리 어답터가 맞는 경우 : 자식 노드 중 최소값으로 dp 갱신


N = int(input())
tree = [[]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 1] for _ in range(N+1)]       # dp[정점번호] = [얼리 어답터 아닐때 현재까지의 얼리 어답터 최수 수, 맞을때]
visited = [False]*(N+1)

dfs(1)
print(min(dp[1]))