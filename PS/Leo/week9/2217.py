import sys
sys.stdin = open('input_2217.txt')
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

# 최대 중량 = 선택한 로프 중 가장 낮은 최대중량 * 선택한 로프의 수
ret = []
for i in range(len(lst)):
    temp = lst[i]*(i+1)
    ret.append(temp)

print(max(ret))