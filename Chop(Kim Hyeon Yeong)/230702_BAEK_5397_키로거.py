file = open("input/230702_BAEK_5397_키로거.txt")
t = int(file.readline().strip())

for tc in range(0, t):
    key_log = list(file.readline().strip())
    pw_left, pw_right = [], []
    for key in key_log:
        if key == "<":
            if pw_left:
                pw_right.append(pw_left.pop())
        elif key == ">":
            if pw_right:
                pw_left.append(pw_right.pop())
        elif key == "-":
            if pw_left:
                pw_left.pop()
        else:
            pw_left.append(key)
    
    pw_left.extend(reversed(pw_right))
    print(''.join(pw_left))