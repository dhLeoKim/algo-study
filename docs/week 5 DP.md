## DP(Dynamic Programming, 동적 계획법)

- 개념
  
  - 그리디 알고리즘과 같이 **최적화 문제**를 해결하는 알고리즘
  
  - 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여 최종적으로 원래 주어진 입력의 문제를 해결

- 조건
  
  - 중복된 하위 문제
    
    - 큰 문제를 작은 부분 문제로 나누어 풀 때, 작은 부분 문제들이 중복적으로 반복해서 나타나는 경우
  
  - 최적 부분 구조
    
    - 큰 문제의 최적해가 작은 문제들의 최적해를 결합해서 얻을 수 있는 경우

- 방법
  
  - Top-down 방식 (Memoization)
    
    - 큰 문제를 해결하기 위해 작은 문제들을 호출하고, 작은 문제들이 이전에 해결한 적이 있는지 확인하여 이미 계산된 결과를 재활용
    
    - 재귀적으로 호출되기 때문에 깊이가 깊어질 경우에는 재귀 스택의 크기를 초과할 수 있음
      
      ```python
      # 피보나치
      def fibonacci(n):
          # if memo[n]:
          #   pass
          if n < 2:
              memo[n] = n
          elif memo[n] == 0:
              memo[n] = fibonacci(n-1) + fibonacci(n-2)
          return memo[n]
      
      memo = [0] * maxV
      print(fibonacci(50))         # 12586269025
      print(fibonacci(100))        # 354224848179261915075
      ```
  
  - Bottom-up 방식 (Tabulation)
    
    - 작은 문제부터 시작하여 점진적으로 큰 문제들을 해결해 나가며 결과를 테이블에 저장
    
    - 반복문을 사용하므로 호출 스택의 크기에 제약이 없음
      
      - append 이용
        
        ```python
        # 피보나치
        def fibonacci(n):
            table = [0, 1]
            for i in range(2, n+1):
                table.append(table[i-1] + table[i-2])
            return table[n]
        
        print(fibonacci(50))         # 12586269025
        print(fibonacci(100))        # 354224848179261915075
        ```
      
      - 크기가 정해진 경우 미리 설정하는 것이 편리
        
        ```python
        # 피보나치
        def fibonacci(n):
            table[0] = 0
            table[1] = 1
            for i in range(2, n+1):
                table[i] = table[i-1] + table[i-2]
            return table[n]
        
        table = [0] * maxV
        
        print(fibonacci(50))         # 12586269025
        print(fibonacci(100))        # 354224848179261915075
        ```
