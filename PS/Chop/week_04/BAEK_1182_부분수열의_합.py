from sys import stdin

stdin = open("input\BAEK_1182_부분수열의_합.txt")

n, s = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))
cnt = 0
def subset_sum(idx, sub_sum):
    global cnt

    if idx >= n:
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1
    
    subset_sum(idx+1, sub_sum)            # 현재 arr[idx]를 선택한 경우의 가지
    subset_sum(idx+1, sub_sum - arr[idx]) # 현재 arr[idx]를 선택하지 않은 경우의 가지

subset_sum(0, 0)
print(cnt)