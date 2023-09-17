import sys

# 3XN 크기의 벽을 2X1, 1X2 크기의 타일로 채우는 경우의 수
# N은 1 이상 30 이하

N = int(sys.stdin.readline().strip())
memo = [0] * 31

# N이 짝수인 경우
if N % 2 == 0:
    # 기존 3X2가 반복되는 경우 -> *3
    # 3XN (N은 2가 아닌 짝수인 자연수) -> *2
    # N의 고유한 형태 -> 2
    memo[2] = 3
    memo[4] = 3 * 3 + 2
    for i in range(6, 31, 2):
        # 기존 3X2가 반복되는 경우 -> *3
        memo[i] = 3 * memo[i-2]
        # 3XN (N은 2가 아닌 짝수인 자연수) -> *2
        for j in range(i-4, -1, -2):
            memo[i] += 2 * memo[j]
        # N의 고유한 형태 -> 2
        memo[i] += 2

# print(memo)
print(memo[N])