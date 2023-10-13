import sys

# 먹을 수 있는 초밥의 최대 가짓수
# 접시 수, 초밥 가지 수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = list(map(int, sys.stdin.readline().strip().split()))
belt = []
for _ in range(N):
    belt.append(int(sys.stdin.readline().strip()))
# print(belt)

# 딕셔너리 사용
total = {}
for i in range(0, k):
    if belt[i] in total:
        total[belt[i]] += 1
    else:
        total[belt[i]] = 1
if c in total:
    cnt = len(total)
else:
    cnt = len(total) + 1

# 슬라이딩 윈도우
s = 0
while s <= N - 1:
    if total[belt[s]] == 1:
        del total[belt[s]]
    else:
        total[belt[s]] -= 1
    if belt[(s+k) % N] in total:
        total[belt[(s+k) % N]] += 1
    else:
        total[belt[(s+k) % N]] = 1
    if c in total:
        temp = len(total)
    else:
        temp = len(total) + 1
    cnt = max(cnt, temp)
    s += 1
print(cnt)