def solution(new_id):
    char = ['-', '_', '.']
    
    new_id = new_id.lower()

    answer = ''
    for i in new_id:
        if i.isalpha() or i.isdecimal() or i in char: 
            answer += i

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer.strip('.')

    if answer == '': 
        answer += 'a'

    n = len(answer)
    if n >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')

    if n <= 2:
        answer += answer[-1]*(3-n)
    
    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "z-+.^."
new_id = "=.="
new_id = "123_.def"
new_id = "abcdefghijklmn.p"

print(solution(new_id))