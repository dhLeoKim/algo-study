import sys
sys.stdin = open('input_14500.txt')
input = sys.stdin.readline

######### 비교1 : dfs + 가지치기 -> 184ms

def dfs(i, j, depth, total):
    global ret

    if depth == 4:
        ret = max(ret, total)
        return
    
    if total + max_val*(4-depth) <= ret:    # 가지치기
        return
    
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 'ㅜ' 모양 블럭 만들기
            if depth == 2:
                visited[ni][nj] = True
                dfs(i, j, depth+1, total+lst[ni][nj])
                visited[ni][nj] = False

            visited[ni][nj] = True
            dfs(ni, nj, depth+1, total+lst[ni][nj])
            visited[ni][nj] = False


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]
max_val = max(map(max, lst))

ret = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, lst[i][j])
        visited[i][j] = False

print(ret)


######### 비교2 : 하드코딩 -> 904ms

# N, M = map(int, input().split())
# lst = [[0]*(M+4)]
# for _ in range(N):
#     lst.append([0] + list(map(int, input().split())) + [0]*3)
# for _ in range(3):
#     lst.append([0]*(M+4))

# def chkTetromino(i, j):
#     t = [0]*19

#     t[0] = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i][j+3]
#     t[1] = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i+3][j]
    
#     t[2] = lst[i][j] + lst[i][j+1] + lst[i+1][j] + lst[i+1][j+1]
    
#     t[3] = lst[i][j+1] + lst[i][j] + lst[i+1][j] + lst[i+2][j]
#     t[4] = lst[i][j-1] + lst[i][j] + lst[i+1][j] + lst[i+2][j]
#     t[5] = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i+2][j+1]
#     t[6] = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i+2][j-1]
#     t[7] = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i+1][j+2]
#     t[8] = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i-1][j+2]
#     t[9] = lst[i+1][j] + lst[i][j] + lst[i][j+1] + lst[i][j+2]
#     t[10] = lst[i-1][j] + lst[i][j] + lst[i][j+1] + lst[i][j+2]
    
#     t[11] = lst[i][j] + lst[i+1][j] + lst[i+1][j+1] + lst[i+2][j+1]
#     t[12] = lst[i][j] + lst[i+1][j] + lst[i+1][j-1] + lst[i+2][j-1]
#     t[13] = lst[i][j] + lst[i][j+1] + lst[i-1][j+1] + lst[i-1][j+2]
#     t[14] = lst[i][j] + lst[i][j+1] + lst[i+1][j+1] + lst[i+1][j+2]
    
#     t[15] = lst[i][j] + lst[i][j+1] + lst[i+1][j+1] + lst[i][j+2]
#     t[16] = lst[i][j] + lst[i][j+1] + lst[i-1][j+1] + lst[i][j+2]
#     t[17] = lst[i][j] + lst[i+1][j] + lst[i+1][j+1] + lst[i+2][j]
#     t[18] = lst[i][j] + lst[i+1][j] + lst[i+1][j-1] + lst[i+2][j]

#     tetromino.append(max(t))


# tetromino = []
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         chkTetromino(i, j)

# print(max(tetromino))