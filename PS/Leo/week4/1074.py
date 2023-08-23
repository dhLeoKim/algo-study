import sys
sys.stdin = open('input_1074.txt')
input = sys.stdin.readline

# 2**(N-1)의 크기로 4등분 한 후, 재귀적으로 방문 처리
# 0의 위치일 때, Z(N-1, r, c)
# 1의 위치일 때, half*half + Z(N-1, r, c-half)
# 2의 위치일 때, 2*half*half + Z(N-1, r-half, c)
# 3의 위치일 때, 3*half*half + Z(N-1, r-half, c-half)

def Z(N, r, c):
    if N == 0:
        return 0
    
    half = 2**(N-1)

    if r < half and c < half:
        return Z(N-1, r, c)
    elif r < half and c >= half:
        return half*half + Z(N-1, r, c-half)
    elif r >= half and c < half:
        return 2*half*half + Z(N-1, r-half, c)
    elif r >= half and c >= half:
        return 3*half*half + Z(N-1, r-half, c-half)


N, r, c = map(int, input().split())
print(Z(N, r, c))