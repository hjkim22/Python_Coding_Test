def solution(array, n):
    closest_num = array[0]
    min_diff = abs(array[0] - n)

    for num in array[1:]:
        diff = abs(num - n)
        if diff < min_diff or (diff == min_diff and num < closest_num):

            min_diff = diff
            closest_num = num

    return closest_num

result1 = solution([3, 10, 28], 20)
result2 = solution([10, 11, 12], 13)

print(result1)
print(result2)