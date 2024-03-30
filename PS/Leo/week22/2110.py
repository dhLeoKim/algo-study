import sys
sys.stdin = open('input_2110.txt')
input = sys.stdin.readline

def binarySearch(start, end):
    global ret

    while start <= end:
        # 설치간격(mid)에 대해서 이분탐색
        mid = (start+end)//2
        now = lst[0]                    # 첫번째 집 선택
        cnt = 1

        for i in range(1, N):           # 두번째 집부터 고려
            if lst[i] >= now + mid:     # 선택된 설치간격보다 큰 집 선택
                cnt += 1
                now = lst[i]            # 다음집

        # 설치할수 있는 개수가 C개를 넘어가면 더 넓게 설치할 수 있다 -> mid+1
        if cnt >= C:
            start = mid+1
            ret = mid
        # 설치할수 있는 개수가 C개를 안넘어가면 더 좁게 설치해야한다 -> mid-1
        else:
            end = mid-1


N, C = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

start = 1
end = lst[-1]-lst[0]
ret = 0
binarySearch(start, end)

print(ret)