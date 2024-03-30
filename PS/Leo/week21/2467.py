import sys
sys.stdin = open('input_2467.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

ret = [1e11, (0, 0)]
j = N-1
for i in range(N):
    while j > i:
        temp = lst[i]+lst[j]
        if abs(temp) <= ret[0]:
            ret[0] = abs(temp)
            ret[1] = (lst[i], lst[j])
        if temp < 0:
            break

        j -= 1

print(*ret[1])

#################################

# l = 0
# r = N-1
# while l < r:
#     temp = lst[l]+lst[r]

#     if abs(temp) <= ret[0]:
#         ret[0] = abs(temp)
#         ret[1] = (l, r)
#     if temp < 0:
#         l += 1
#     else:
#         r -= 1