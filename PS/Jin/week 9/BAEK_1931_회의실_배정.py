import sys

N = int(sys.stdin.readline().strip())
time = []
for _ in range(N):
    time.append(list(map(int, sys.stdin.readline().strip().split())))

# 종료시간이 빠른 순서로 정렬
# 종료시간이 동일한 경우 시작시간이 빠른 순서로 정렬
time.sort(key=lambda x: (x[1], x[0]))
# print(time)

cnt = 0
# 종료시간
l = 0
for i in range(N):
    # 시작시간이 이전 종료시간보다 크거나 같으면
    if time[i][0] >= l:
        cnt += 1
        l = time[i][1]
print(cnt)