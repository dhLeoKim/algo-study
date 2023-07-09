import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

brackets = input()

stack = []
ret = []
ret = []
for bracket in brackets:
    if bracket == '(' or bracket == '[':
        stack.append(bracket)
        ret.append(0)
    elif bracket == ')':
        if not stack:
            ret = [0]
            break
        if stack[-1] == '(':
            stack.pop()
            temp = ret.pop()
            if temp == 0:
                if not ret:
                    ret.append(2)
                else:
                    ret[-1] += 2
            elif not ret:
                ret.append(temp*2)
            else:
                ret[-1] += temp*2
        elif stack[-1] == '[':
            ret = [0]
            break
    elif bracket == ']':
        if not stack:
            ret = [0]
            break
        if stack[-1] == '[':
            stack.pop()
            temp = ret.pop()
            if temp == 0:
                if not ret:
                    ret.append(3)
                else:
                    ret[-1] += 3
            elif not ret:
                ret.append(temp*3)
            else:
                ret[-1] += temp*3
        elif stack[-1] == '(':
            ret = [0]
            break

print(ret[0])