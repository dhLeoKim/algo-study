import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

L = int(input())
for tc in range(L):
    password = input().strip()

    pw_left = []
    pw_right = []
    for char in password:
        if char == '<':
            if pw_left:
                pw_right.append(pw_left.pop())
        elif char == '>':
            if pw_right:
                pw_left.append(pw_right.pop())
        elif char == '-':
            if pw_left:
                pw_left.pop()
        else:
            pw_left.append(char)

    print(''.join(pw_left) + ''.join(pw_right[::-1]))

    ############ 시간 초과    
    # idx = 0
    # ret = []
    # for char in password:
    #     if char == '<':
    #         if idx > 0:
    #             idx -= 1
    #     elif char == '>':
    #         if idx < len(ret):
    #             idx += 1
    #     elif char == '-':
    #         if len(ret) <= 0:
    #             continue
    #         del ret[idx-1]
    #         if idx > 0:
    #             idx -= 1
    #     else:
    #         ret.insert(idx, char)
    #         idx += 1

    # print(''.join(ret))