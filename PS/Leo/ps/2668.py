import sys
sys.stdin = open('input_2668.txt')
input = sys.stdin.readline

def dfs(u, visited):
    visited.add(u)
    chk[u] = True
    for v in lst[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            ret.extend(list(visited))
            return
        

N = int(input())
lst = [[] for _ in range(N+1)]
for i in range(1, N+1):
    n = int(input())
    lst[n].append(i)

chk = [False for _ in range(N+1)]
ret = []
for i in range(1, N+1):
    if not chk[i]:
        dfs(i, set())

ret.sort()
print(len(ret))
for num in ret:
    print(num)



# 연결리스트로 정리하여 생각하면
# 사이클을 가지는 노드들을 찾아내는 것과 동일함