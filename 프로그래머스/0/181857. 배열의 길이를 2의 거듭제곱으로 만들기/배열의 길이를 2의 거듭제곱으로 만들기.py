def solution(arr):
    n = len(arr)
    power_of_two = 1
    while power_of_two < n:
        power_of_two *= 2
    return arr + [0] * (power_of_two - n)

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [58, 172, 746, 89]

print(solution(arr1))
print(solution(arr2))