import sys

sys.stdin = open("input/BAEK_10799_쇠막대기.txt")
def input():
    return sys.stdin.readline().rstrip()

brackets = list(input())
layers = 1  # 레이저로 잘릴 층수 (i가 1부터 시작이라서 1로 시작)
sticks = 0  # 총 쇠막대기 수

for i in range(1, len(brackets)):
    if brackets[i] == "(":       # 여는 괄호면 층수 추가
        layers += 1
    else:
        layers -= 1               # 닫는 괄호면 층수 감소 (레이저 or 쇠막대기 끝)
        if brackets[i-1] == "(":  # 직전 괄호가 여는 괄호일 때 : 레이저로 자름
            sticks += layers
        else:                     # 직전 괄호가 닫는 괄호일 때 : 쇠막대기 끝
            sticks += 1

print(sticks)
