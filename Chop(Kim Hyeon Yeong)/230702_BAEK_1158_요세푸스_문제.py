from collections import deque

file = open("input/230702_BAEK_1158_요세푸스_문제.txt")
N, K = map(int, file.readline().rstrip().split())
num_arr = deque([str(i) for i in range(1, N+1)])
removed_arr = []

while num_arr:
    for _ in range(K-1):
        num_arr.append(num_arr.popleft())
    removed_arr.append(num_arr.popleft())
ans = "<" + ", ".join(removed_arr) + ">"
print(ans)
    