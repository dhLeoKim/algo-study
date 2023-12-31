## Greedy algorithm 탐욕 알고리즘
* 지금 가장 최적인 답을 근시안적으로 택하는 알고리즘
* 관찰을 통해서 탐색 범위를 줄이는 알고리즘
* 여러 경우의 수 중에서, 선택을 해야하는 그 시점에서는 최적의 해이지만,
* 그것이 전체의 최적해라는 보장은 없음

## 풀이 흐름
1. 관찰을 통해 탐색 범위를 줄이는 방법, 문제의 규칙 찾기
2. 탐색 범위를 줄여도 올바른 결과를 낸다는 사실을 수학적으로 증명 (귀류법 반례, 귀납법)
3. 구현

## 그리디 풀이 전략
* 쉬운 문제이거나, 비슷한 문제를 풀어봐서 그리디 풀이를 확신한다!
  * => 빠르게 구현해서 제출해보고, 실패한다면 빠르게 손절
* 확신할수는 없지만 대충 감을 잡아 적당한 그리디 풀이를 떠올렸다!
  * => 일단은 넘어가서 다른 문제 풀이 후, 제일 후순위로 그리디 문제 풀이
* 코테에 자주 등장하는 문제가 아니기도 하고,
* 그리디로 풀면 안되는 문제를 그리디로 풀려고 하다가 틀리는 경우가 많으니 주의!!
  * https://www.acmicpc.net/problem/12865