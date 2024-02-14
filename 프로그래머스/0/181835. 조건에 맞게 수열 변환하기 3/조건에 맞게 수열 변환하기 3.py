def solution(arr, k):
    if k % 2 == 1:
        return [num * k for num in arr]
    else:
        return [num + k for num in arr]

arr1 = [1, 2, 3, 100, 99, 98]
arr2 = [1, 2, 3, 100, 99, 98]
k1 = 3
k2 = 2

print(solution(arr1, k1))
print(solution(arr2, k2))