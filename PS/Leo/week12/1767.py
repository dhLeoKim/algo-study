import sys
sys.stdin = open('input_1767.txt')
input = sys.stdin.readline

def dfs(idx, core, length):
    global ret
    if idx == M:
        if core > ret[0]:
            ret = [core, length]
        elif core == ret[0] and length < ret[1]:
            ret = [core, length]
        return
     
    if core + M - idx < ret[0]:
        return
 
    ci, cj = cell[idx]
    for k in range(4):
        i, j = ci, cj
        tmp_length = 0
        while True:
            ni, nj = i + di[k], j + dj[k]
 
            if ni == -1 or ni == N or nj == -1 or nj == N:
                core += 1
                length += tmp_length
                break
 
            if 0 <= ni < N and 0 <= nj < N:
                if lst[ni][nj] == 0:
                    lst[ni][nj] = 2
                    tmp_length += 1
                else:
                    break
 
            i, j = ni, nj
 
        dfs(idx+1, core, length)
 
        if i == 0 or i == N-1 or j == 0 or j == N-1:
            length -= tmp_length
            core -= 1
         
        if lst[i][j] == 1:
            continue
 
        while True:
            lst[i][j] = 0
            ni, nj = i - di[k], j - dj[k]
            if ni == ci and nj == cj:
                break
            i, j = ni, nj
 
 
T = int(input())
for tc in range(1, T+1):
     
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
 
    di, dj = [0, -1, 0, 1], [-1, 0, 1, 0]
    cell = []
 
    for i in range(N):
        for j in range(N):
            if lst[i][j] and 0 < i < N-1 and 0 < j < N-1:
                cell.append((i, j))
 
    M = len(cell)
    # [core 수, 전선길이 합] core 수는 max, 전선길이는 min
    ret = [0, 144]                      
    dfs(0, 0, 0)
 
    print(f'#{tc}', ret[1])