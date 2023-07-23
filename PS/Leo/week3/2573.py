import sys
sys.stdin = open('input_2573.txt')
input = sys.stdin.readline

from collections import deque

def bfs(i, j):
    visited = [[False]*M for _ in range(N)]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

    while queue:
        i, j = queue.popleft()
        chk[i][j] = True
        cnt = 0
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and lst1[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
                if lst1[ni][nj] == 0:
                    cnt += 1
        
        # 주변의 0 개수 만큼 빼기
        if lst2[i][j] > cnt:
            lst2[i][j] -= cnt
        else:
            lst2[i][j] = 0


N, M = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(N)]
lst2 = [row[:] for row in lst1]

ret = -1
while True:
    ret += 1
    ice = 0
    chk = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if lst1[i][j] != 0 and not chk[i][j]:
                bfs(i, j)
                ice += 1
    
    # 두 덩어리 이상으로 분리 확인
    if ice > 1: 
        break
    
    # 다음 루프 준비
    lst1 = []
    chk_sum = 0
    for row in lst2:
        lst1.append(row[:])
        chk_sum += sum(row)

    # 다 녹을 때까지 두 덩어리 이상으로 분리되지 않는 경우
    if chk_sum == 0:
        ret = 0
        break

print(ret)