T = int(input())

for _ in range(T):
    # 동전의 가지 수
    N = int(input())
    # 동전의 금액
    coin = list(map(int, input().split()))
    # 만들어야 할 금액
    M = int(input())

    # 방법 계산하기
    # 0원을 1으로 지정해 한 가지 방법으로 생각하고 계산
    ways = [0] * (M+1)
    ways[0] = 1

    for i in range(len(coin)):
        for j in range(1, len(ways)):
            if j >= coin[i]:
                ways[j] += ways[j - coin[i]]

    print(ways[M])