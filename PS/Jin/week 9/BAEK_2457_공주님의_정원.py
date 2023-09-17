import sys

# 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어있도록

N = int(sys.stdin.readline().strip())
flower = []
for _ in range(N):
    a, b, c, d = list(map(int, sys.stdin.readline().strip().split()))
    # 범위 벗어나는 경우 제외
    if c < 3 or a > 11:
        continue
    else:
        flower.append([a, b, c, d])
cnt = 0
if not flower:
    print(cnt)
else:
    # 꽃이 피는 날짜가 빠른 순으로 정렬
    # 피는 날짜가 같다면 지는 날짜가 느린 순으로 정렬
    flower.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]))

    month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # 시작 날짜나 끝나는 날짜를 포함하지 않는 경우
    if flower[0][0] > 3 or (flower[0][0] == 3 and flower[0][1] > 1) or flower[-1][0] > 11:
        print(cnt)
    else:
        sm, sd, lm, ld = 1, 1, 3, 1
        idx = 0
        while True:
            tmpm, tmpd = 0, 0
            for i in range(idx, len(flower)):
                if flower[i][0] < lm or (flower[i][0] == lm and flower[i][1] <= ld):
                    if tmpm < flower[i][2] or (tmpm == flower[i][2] and tmpd < flower[i][3]):
                        tmpm, tmpd = flower[i][2], flower[i][3]