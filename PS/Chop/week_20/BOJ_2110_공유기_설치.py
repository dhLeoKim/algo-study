from sys import stdin

stdin = open("input/BOJ_2110_공유기_설치.txt")

# 1. 간격 설정 (평균값)
# 2. 설정한 간격을 지키며 공유기 설치
# 3. 설치된 공유기 개수가 문제의 조건을 만족하면 (temp == c) 종료
# 4. 설치된 공유기 개수가 문제의 조건을 만족하지 못하면 이분 탐색으로 간격 설정
# 5. 2-4 반복


def find_dist(dist, start):
    prev, cnt = start, 1
    ans = 10000000

    for now in area:
        if now-prev >= dist:
            ans = min(now-prev, ans)
            prev = now
            cnt += 1
        if cnt > c:
            return 0
    if cnt == c:
        return ans
    else:
        return -1


n, c = map(int, stdin.readline().rstrip().split())
area = [int(stdin.readline()) for _ in range(n)]
area.sort()

start, end = area[0], area[len(area)-1]
avg = (end - start) // (c-1)
l, r, m = 0, avg, avg // 2

while True:
    m = (l+r) // 2
    temp = find_dist(m, start)
    if temp > 0:
        print(temp)
        break
    if temp == 0:
        l = m+1
    else:
        r = m-1
