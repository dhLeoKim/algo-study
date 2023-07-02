N, K = map(int, input().split())
circle = [i+1 for i in range(N)]
# print(circle)

answer = []
# idx 더할거니까 -1
idx = -1
while circle:
    idx = (idx + K) % len(circle)
    a = circle.pop(idx)
    # 출력형식을 맞추기 위해 join을 사용하기 때문에 str 형태로 추가
    answer.append(str(a))
    # idx 더할거니까 -1
    idx -= 1
# print(answer)
print("<", ", ".join(answer), ">", sep="")