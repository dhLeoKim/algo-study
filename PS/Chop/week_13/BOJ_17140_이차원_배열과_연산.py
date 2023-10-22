from sys import stdin
from collections import defaultdict

stdin = open("input/BOJ_17140_이차원_배열과_연산.txt")

def get_sorted_list(nums):
  num_to_count = defaultdict(int)
  for num in nums:
    if num == 0: continue
    num_to_count[num] += 1
                                            
  num_to_count = list(num_to_count.items())   
  num_to_count.sort(key = lambda x:x[0])
  num_to_count.sort(key = lambda x:x[1])   
                                          
  return [num_to_count[i][j] for i in range(len(num_to_count)) for j in range(2)]
                             

r, c, k = map(int, stdin.readline().rstrip().split())
r -= 1
c -= 1
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(3)]
             
for i in range(101):    
  width = len(graph[0])
  height = len(graph)    
  if r <= height-1 and c <= width-1 and graph[r][c] == k:
    break

  lines = []             
  next_width = 0
  next_height = 0
  if height >= width:
    next_height = height
    for i in range(height):
      lines.append(get_sorted_list(graph[i]))
      next_width = max(next_width, len(lines[-1]))
  else:                          
    next_height = width
    for j in range(width):             
      lines.append(get_sorted_list(list(zip(*graph))[j]))    
      next_width = max(next_width, len(lines[-1]))   

  graph = [[0]*next_width for _ in range(next_height)]
  for i in range(next_height):
    for j in range(len(lines[i])):
      graph[i][j] = lines[i][j]
                 
  if height < width:       
    graph = list(zip(*graph))    
    
  if next_width > 100:
    for i in range(next_height):
      graph[i] = graph[i][:100]
  if next_height > 100:
    graph = graph[:100]
else:
  i = -1
    
print(i)