import sys

ab = sys.stdin.readline().strip()
a = ab.count('a')

# 원형인 문자열
abab = ab + ab
# print(abab)
cnt = 1000
for i in range(len(abab) - a):
    # 슬라이딩 윈도우
    # a를 모두 연속으로 만들기 위해서는 b의 개수를 세서 그 개수만큼만 교환
    cnt = min(cnt, abab[i:i+a].count('b'))
print(cnt)