N = int(input())
eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))
visited = [0] * N
answer = 0

def dfs(i):
    global answer
    # 계란 치는 과정 종료 (N-1 아니고 N)
    if i == N:
        temp = 0
        for c in range(N):
            if eggs[c][0] <= 0:
                temp += 1
        if answer < temp:
            answer = temp
        return
    # 손에 든 계란이 깨진 경우
    if eggs[i][0] <= 0:
        dfs(i+1)
    else:
        temp2 = 0
        for j in range(N):
            if i != j and eggs[j][0] > 0:
                temp2 += 1
                eggs[j][0] -= eggs[i][1]
                eggs[i][0] -= eggs[j][1]
                dfs(i+1)
                eggs[j][0] += eggs[i][1]
                eggs[i][0] += eggs[j][1]
        else:
            # 깨지지 않은 다른 계란이 없는 경우
            if temp2 == 0:
                dfs(i+1)

dfs(0)
print(answer)