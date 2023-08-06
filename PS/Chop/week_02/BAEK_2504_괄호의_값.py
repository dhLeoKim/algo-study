import sys

sys.stdin = open("input/BAEK_2504_괄호의_값.txt")
def input():
    return sys.stdin.readline().rstrip()

# 조건
# 1. 아직 닫히지 않은 마지막 괄호를 다른 종류의 괄호로 닫으면 안 됨
# 2. 여는 괄호와 닫는 괄호의 개수가 같아야 함

# 계산 방법
# 1. 여는 괄호가 나왔을 때 : 곱해줄 수를 증가 (곱하기)
# 2. 닫는 괄호가 나왔을 때
# 2-1. 직전 괄호가 여는 괄호였을 때 : 현재 곱해줄 수를 총 합계에 더해준 후, 곱해줄 수를 감소 (나누기)
# 2-2. 직전 괄호가 닫는 괄호였을 때 : 곱해줄 수를 감소 (나누기)

# 10799 쇠막대기와 유사

def b_to_num(x):
    return b_dict[x]
b_dict = {"(": 2, ")": -2, "[": 3, "]": -3}
brackets = list(map(b_to_num, input()))  # 괄호를 숫자로 변환한 리스트

b_stack = []   # 괄호 짝 판별을 위한 stack
multi_num = 1  # 곱해줄 수 (layers)
res = 0        # 총 합계 (sticks)

for i in range(len(brackets)):
    if brackets[i] > 0:                 # 여는 괄호일 때 : 곱해줄 수 증가
        b_stack.append(brackets[i])
        multi_num *= brackets[i]

    elif len(b_stack) != 0 and b_stack.pop() / brackets[i] == -1:  # 짝이 맞는 닫는 괄호일 때
        if brackets[i-1] > 0:                                      # 직전 괄호가 여는 괄호일 때 : 총 합계에 더해줌
            res += multi_num
        multi_num /= (-brackets[i])                                # 곱해줄 수 감소
    else:
        res = 0
        break

if b_stack:  # 여는 괄호가 더 많을 때
    res = 0

print(int(res))