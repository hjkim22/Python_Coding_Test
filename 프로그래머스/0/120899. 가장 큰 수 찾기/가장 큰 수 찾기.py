def solution(array):
    max_num = max(array)
    max_index = array.index(max_num)
    return [max_num, max_index]

result1 = solution([1, 8, 3])
print(result1)

result2 = solution([9, 10, 11, 8])
print(result2)