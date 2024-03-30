def solution(s):
    L = len(s)
    ret = 1e9
    for num in range(1, L+1):
        flag = False
        cnt = 1
        temp = ''
        for i in range(0, L-num, num):
            sub_s = s[i:i+num]
            if sub_s == s[i+num:i+num*2]:
                flag = True
                cnt += 1
            elif flag:
                temp += str(cnt) + s[i:i+num]
                flag = False
                cnt = 1
            else:
                temp += s[i:i+num]

        if cnt > 1:
            temp += str(cnt) + sub_s
        else:
            temp += sub_s
        ret = min(ret, len(temp))

    return ret


s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"

print(solution(s))