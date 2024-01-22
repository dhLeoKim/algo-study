import sys
sys.stdin = open('input_15684.txt')
input = sys.stdin.readline

N, M, H = map(int, input().split())

visited = [[False] * (N+1) for _ in range(H+1)]
lst = []
for _ in range(M):
    a, b = map(int, input().split())
    visited[a][b] = True

def chkLadder():
    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if visited[j][now-1]:
                now -= 1
            elif visited[j][now]:
                now += 1
                
        if now != i:
            return False
        
    return True


def dfs(depth, idx):
    global ret
    if depth > 3:
        return
    
    if chkLadder():
        ret = depth
        return

    for c in range(idx, len(lst)):
        i, j = lst[c]
        if not visited[i][j-1] and not visited[i][j+1]:
            visited[i][j] = True
            dfs(depth+1, c+1)
            visited[i][j] = False


for i in range(1, H+1):
    for j in range(1, N):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            lst.append([i, j])

ret = 4
dfs(0, 0)

print(-1 if ret > 3 else ret)