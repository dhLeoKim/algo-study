import sys
sys.stdin = open('input_20055.txt')
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))

# 초기화
step = 0                    # 단계
cnt = 0                     # 0의 개수
robot = deque([0]*2*N)

########################## 시간비교1 : rotate 사용
while cnt < K:
    step += 1

    # 1. 벨트 회전
    belt.rotate(1)
    robot.rotate(1)

    # 로봇 내리기
    robot[N-1] = 0

    # 2. 로봇 이동
    for i in range(N-2, -1, -1):
        if robot[i] != 0 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1

    # 로봇 내리기
    robot[N-1] = 0

    # 3. 로봇 올리기
    if belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1

    # 4. 종료 확인 후, 1로 돌아가기

print(step)


########################## 시간비교2 : 인덱스 이동 사용
# start = 0                   # 벨트 시작위치
# end = N-1                   # 벨트 끝위치
# while cnt < K:
#     step += 1

#     # 1. 벨트 회전
#     start = (start-1)%(2*N)
#     end = (end-1)%(2*N)

#     # 로봇 내리기
#     robot[end] = 0

#     # 2. 로봇 이동
#     for k in range(N):
#         i = end-k-1
#         if robot[i] != 0 and robot[i+1] == 0 and belt[i+1] >= 1:
#             robot[i] = 0
#             robot[i+1] = 1
#             belt[i+1] -= 1
#             if belt[i+1] == 0:
#                 cnt += 1

#     # 로봇 내리기
#     robot[end] = 0

#     # 3. 로봇 올리기
#     if belt[start] != 0:
#         robot[start] = 1
#         belt[start] -= 1
#         if belt[start] == 0:
#             cnt += 1

#     # 4. 종료 확인 후, 1로 돌아가기

# print(step)


########################## 결과
# 1번이 더 빠름(유의미한 차이x)