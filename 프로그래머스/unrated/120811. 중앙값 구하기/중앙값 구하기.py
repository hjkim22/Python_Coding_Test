def solution(array):
    arr = sorted(array)
    middle_index = len(arr) // 2
    median = arr[middle_index]
    return median
    
print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))