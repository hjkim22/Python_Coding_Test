def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_val = min(arr)
        arr.remove(min_val)
        return arr

arr1 = [4, 3, 2, 1]
arr2 = [10]
print(solution(arr1))
print(solution(arr2))