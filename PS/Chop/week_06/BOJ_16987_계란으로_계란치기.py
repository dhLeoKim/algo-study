from sys import stdin

stdin = open("input/BOJ_16987_계란으로_계란치기.txt")

N = int(stdin.readline().rstrip())
eggs_S, eggs_W = [], []

for _ in range(N):
    s, w = map(int, stdin.readline().rstrip().split())
    eggs_S.append(s)
    eggs_W.append(w)

max_cnt = 0

def dfs(e, eggs_S, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    if e == N:
        return
    elif eggs_S[e] <= 0:
        dfs(e+1, eggs_S, cnt)
    else:
        for i in range(N):
            next = cnt                          # 계란을 깬 후의 카운트 (초기화)
            if i != e:
                if eggs_S[i] > 0:
                    eggs_S[e] -= eggs_W[i]      # 계란 깨기
                    eggs_S[i] -= eggs_W[e]
                    for egg in [eggs_S[e], eggs_S[i]]:
                        if egg <= 0: next += 1
                    dfs(e+1, eggs_S, next)      # 다음 계란으로 넘어가기
                    eggs_S[e] += eggs_W[i]      # 계란 내구도 초기화
                    eggs_S[i] += eggs_W[e]

dfs(0, eggs_S, 0)  
print(max_cnt)