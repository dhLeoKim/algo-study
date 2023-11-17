# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    # 모든 대문자를 대응되는 소문자로 치환
    text = new_id.lower()
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    temp = ''
    chk = '~!@#$%^&*()=+[{]}:?,<>/'
    for i in range(len(text)):
        if text[i] not in chk:
            temp += text[i]
    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    cnt = 0
    for i in range(len(temp)):
        if temp[i] == '.':
            cnt += 1
        else:
            if not cnt:
                answer += temp[i]
            else:
                answer = answer + '.' + temp[i]
                cnt = 0
    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    if answer:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 빈 문자열이라면, "a"를 대입
    if answer == '':
        answer = 'a'
    # 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(answer) >= 16:
        answer = answer[:15]
        # 만약 제거 후 마침표(.)가 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        if answer[-1] == '.':
            answer = answer[:-1]
    # 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    if len(answer) == 1:
        answer = answer * 3
    if len(answer) == 2:
        answer = answer + answer[-1]
    return answer