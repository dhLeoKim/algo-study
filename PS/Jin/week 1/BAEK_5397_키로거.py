# pwd = []
# cursor = 0의 방식으로 풀면 시간초과 남

# 커서를 기준으로 left 배열과 right 배열을 만들어 해결
# right는 거꾸로 입력을 받은 뒤 reversed 함수를 이용해 정렬

T = int(input())
for _ in range(T):
    keyboard = list(input())
    # print(keyboard)

    l = []
    r = []
    for w in keyboard:
        if w == '-':
            if l:
                a = l.pop()
        elif w == '<':
            if l:
                a = l.pop()
                r.append(a)
        elif w == '>':
            if r:
                a = r.pop()
                l.append(a)
        else:
            l.append(w)

    r = reversed(r)
    l.extend(r)

    print(''.join(l))