import sys
sys.stdin = open('input_1931.txt')
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간이 빠른 순서 대로,
# 끝나는 시간이같다면 시작시간이 빠른 순서 대로
lst.sort()
lst.sort(key= lambda x: x[1])

end = 0
ret = 0
for i in lst:
    if i[0] >= end:
        ret += 1
        end = i[1]

print(ret)