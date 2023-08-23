import sys
sys.stdin = open('input_1941.txt')
input = sys.stdin.readline

from collections import deque

def bfs(si, sj):
    queue = deque()
    visited2 = [[0]*5 for _ in range(5)]
    queue.append((si,sj))
    visited2[si][sj]=1
    cnt = 1
    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

    while queue:
        ci,cj = queue.popleft()
        for k in range(4):
            ni,nj = ci+di[k], cj+dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5 and visited2[ni][nj] == 0 and visited[ni][nj] == 1:
                queue.append((ni,nj))
                visited2[ni][nj] = 1
                cnt += 1
    
    return cnt==7


def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j]==1:
                return bfs(i,j)


def dfs(n, cnt, s_cnt):
    global ret
    if cnt>7:                           # 7명 가지치기
        return

    if n == 25:
        if cnt == 7 and s_cnt >= 4:     # 7명 그룹, S가 4명이상인 경우
            if check():                 # 인접했는지 체크해서 모두 인접시 += 1
                ret+=1
        return

    visited[n//5][n%5]=1                # 포함하는 경우
    dfs(n+1, cnt+1, s_cnt + int(lst[n//5][n%5] == 'S'))
    visited[n//5][n%5]=0                # 원상복구
    dfs(n+1, cnt, s_cnt)                # 포함하지 않는 경우


lst = [input() for _ in range(5)]
ret = 0
visited = [[0]*5 for _ in range(5)]

dfs(0, 0, 0)    # 학생번호 인덱스, 포함학생수, S 학생수

print(ret)