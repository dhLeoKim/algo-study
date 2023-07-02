import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    left_list = []
    right_list = []
    data = input()
    for i in data:
        if i == '-':
            if left_list: #왼쪽 스택에 있을 경우
                left_list.pop()
        elif i == '<': # 왼쪽 스택에 있는 문자 오른쪽 스택으로
            if left_list:
                right_list.append(left_list.pop())
        elif i == '>': # 오른쪽 스택에 있는 문자 왼쪽 스택으로
            if right_list:
                left_list.append(right_list.pop())
        else:
            left_list.append(i)
    left_list.extend(reversed(right_list)) # 오른쪽 스택에 있는 문자들은 뒤집어서 붙여야 한다.
    print(''.join(left_list))