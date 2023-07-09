from collections import deque

file = open("input/BAEK_5397_키로거.txt")
t = int(file.readline().strip())

## 문자열 slicing 사용했을 때 시간 초과
## deque 사용해서 해결

for _ in range(t):
    pw_left, pw_right = deque([]), deque([])
    key_log = input()
    
    for key in key_log:
        if key == "<":
            if pw_left:
                pw_right.appendleft(pw_left.pop())
        elif key == ">":
            if pw_right:
                pw_left.append(pw_right.popleft())
        elif key == "-":
            if pw_left:
                pw_left.pop()
        else:
            pw_left.append(key)
    pw = pw_left + pw_right
    
    print(''.join(pw))