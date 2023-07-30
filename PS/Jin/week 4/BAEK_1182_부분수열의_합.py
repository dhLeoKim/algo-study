import itertools

N, S = list(map(int, input().split()))
num = list(map(int, input().split()))
# 오름차순 정렬
num = sorted(num)
count = 0

for i in range(1, N+1):
    nCr = itertools.combinations(num, i)
    # print(list(nCr))
    for k in list(nCr):
        # print(k)
        if sum(k) == S:
            count += 1

print(count)