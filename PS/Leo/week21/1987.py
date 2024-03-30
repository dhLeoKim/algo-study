import sys
sys.stdin = open('input_1987.txt')
input = sys.stdin.readline

#####################################################
# 풀이1 : 경로저장x, 남은 갯수로 가지치기 (느림)

# def dfs(i, j, depth, rest):
#     global ret

#     if depth == 26:
#         ret = 26
#         print(ret)
#         exit()

#     if depth + rest < ret:
#         return

#     for k in range(4):
#         ni, nj = i+di[k], j+dj[k]
#         if 0 <= ni < R and 0 <= nj < C and not visited[lst[ni][nj]]:
#             visited[lst[ni][nj]] = True
#             dfs(ni, nj, depth+1, rest-cnt[lst[ni][nj]])
#             visited[lst[ni][nj]] = False
#     else:
#         ret = max(ret, depth)
            

# R, C = map(int, input().split())
# cnt = [0]*26
# lst = []
# for _ in range(R):
#     row = list(input().strip())
#     for i in range(C):
#         num = ord(row[i])-65
#         cnt[num] += 1
#         row[i] = num
#     lst.append(row)


# di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
# visited = [False]*26
# visited[lst[0][0]] = True
# ret = 0
# dfs(0, 0, 1, R*C-cnt[lst[0][0]])

# print(ret)

#####################################################
# 풀이2 : 경로 저장o, 경로로 가지치기

def dfs(i, j, depth, path):
    global ret 

    path = lst[i][j]
    stack = [(i, j, depth, path)]
    visited_path = [['']*C for _ in range(R)]

    while stack:
        i, j, depth, path = stack.pop()
        if depth > ret:
            ret = depth
            if ret == 26:
                break

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < R and 0 <= nj < C and lst[ni][nj] not in path:
                nxt_path = path + lst[ni][nj]
                if nxt_path not in visited_path[ni][nj]:
                    visited_path[ni][nj] = nxt_path
                    stack.append((ni, nj, depth+1, nxt_path))


R, C = map(int, input().split())
lst = [list(input().strip()) for _ in range(R)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
ret = 0
dfs(0, 0, 1, lst[0][0])

print(ret)