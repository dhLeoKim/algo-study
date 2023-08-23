
# map과 함께 사용하기
numbers = [1, 2, 3, 4]
mapped_numbers = list(map(lambda x: x*2, numbers))
print(mapped_numbers)
# [2, 4, 6, 8]

# sort와 함께 사용하기
students = [{"name": "chop", "grade": 10}, {
    "name": "pop", "grade": 12}, {"name": "hop", "grade": 8}]
# 각 원소의 "grade" 기준으로 오름차순 정렬
sorted_arr = sorted(students, key=lambda x: x["grade"])
print(sorted_arr)
# [{"name": "hop", "grade": 8}, {"name": "chop", "grade": 10}, {"name": "pop", "grade": 12}]
