# 재귀, 백트래킹
## 1. 재귀
### 재귀(Recursion)란? 
- 자신을 정의할 때 자기 자신을 재참조하는 방법
### 재귀함수(Recursion deftion)란? 
- 함수에서 자기 자신을 다시 호출해 작업을 수행하는 방식
- 특정 분기까지 자기 자신을 계속해서 호출하는데, 주로 반복문을 구현할 때 사용
- for, while 등의 반복문으로 구현가능한 로직은 모두 재귀함수로도 가능하고 그 반대 역시 가능 
- 재귀함수의 가장 대표적인 사용 예제는 팩토리얼(Factorial)
### 재귀함수 공식
```python
def 함수이름(매개변수) :
    if 종료조건 :
        return 종료값
    return 점화식  # 결과값을 받을 변수 = 함수이름(입력변수)
```
### 재귀함수 사용시 주의할 점
- 스택 오버플로우(stack overflow)를 주의
- 함수가 멈추지 않고 무한대로 실행되는 것을 방지하기 위해 종료 조건을 반드시 명시

### 재귀함수의 장단점
**장점**
1. 변수를 여럿 만들 필요가 없음
- 현재 상태를 저장하기 위해 변수를 따로 만들기보다 메서드를 재귀적으로 호출하며 변경된 상태를 전달함으로써 변수의 수를 줄일 수 있음
2. while, for문 등의 반복문을 사용하지 않아도 되어 코드가 간결해짐
**단점**
1. 지속적으로 함수를 호출하면서 지역변수, 입력값(매개변수), 결과값 등이 모두 스택이라는 데이터 저장 공간에 보관됨. 선언한 변수의 값만 사용하는 반복문에 비해 메모리를 더 많이 사용하게 되어 속도 저하가 일어날 수 있음  
2. 함수 호출 -> 복귀를 위한 context switching 비용이 발생
- 따라서 이러한 재귀함수의 단점을 보완하는 방법 중 하나가 바로 '꼬리 재귀'

### 꼬리재귀 (Tail Recursion)
- 재귀 호출이 끝나면 아무 일도 하지 않고 결과만 바로 반환되도록 하는 방법
- 이렇게 하면 이전 함수의 상태를 유지하지도 않고 추가 연산을 하지도 않아서 스택이 넘쳐나는 문제를 해결할 수 있게 된다. 
- 꼬리 재귀 함수는 이름처럼 항상 함수의 마지막에서 실행되는데, return 되기 전에 값이 정해지며 호출 당한 함수의 결과값이 호출하는 함수의 결과값으로 반환된다. 
- ex) 팩토리얼 풀이 비교
```python
//반복문 사용
def factorial(num):
    var result = 1
    for i in range(10):
        result *= i
    return result
print(factorial(10)) //3628800
```
```python
//일반 재귀 방식
def factorial(num):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(10)) //3628800
```
```python
//꼬리 재귀 방식
def factorial(num, total):
    if num == 1:
        return total
    return factorial(num - 1, num * total)
print(factorial(10, 1)) //3628800
```
- 꼬리 재귀의 핵심은 반환부분에 연산이 없어야 한다는 점!

## 2. 백트래킹
### 백트래킹 이란?
- 재귀적으로 문제를 하나씩 풀어나가되, 현재 재귀를 통해 확인 중인 노드가 제한 조건에 위배되는 경우 제외하고 다음 단계로 나아가는 방식
- 모든 경우의 수를 체크 하지 않고 필요한 것만 체크하여 전체 풀이 시간을 단축
- 백트래킹을 사용하는 알고리즘 중 하나는 대표적으로 DFS가 있음
- DFS는 재귀를 통해 가능한 경로 중 유망한 경로만 찾아서 탐색을 수행한 뒤 다시 돌아와 그 중 가장 최적의 경로를 반환
- 시간복잡도가 보통 Exponential(지수)이며, 대부분 Dynamic Programming, 그리디 알고리즘 등으로 더 빠르게 해결할 수 있음
- 하지만 일부 경우의 문제들은 여전히 백트래킹으로만 해결이 가능한 문제도 있음

### 특징
1. 조건들을 하나씩 대입해가면서 만약 조건에 맞지 않는다면 그 즉시 중단하고 다음으로 넘어감
2. 상태공간트리를 DFS(깊이우선탐색)으로 탐색
3. 방문 중인 노드에서 더 하위 노드로 가면 해답이 없을 경우, 해당 노드의 하위 트리를 방문하지 않고 부모 노드로 되돌아감
```python
def dfs():
	# 유망하면 계속해서 dfs탐색
	if promising(x):
		dfs()

def promising(x):
	if 유먕 여부: return True
    	return False
```