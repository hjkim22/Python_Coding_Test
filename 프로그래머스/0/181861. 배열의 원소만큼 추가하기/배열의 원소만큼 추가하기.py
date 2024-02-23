def solution(arr):
    result = []
    for num in arr:
        result.extend([num] * num)
    return result

print(solution([5, 1, 4]))
print(solution([6, 6]))
print(solution([1]))