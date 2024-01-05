def solution(array, n):
    answer = array.count(n)
    return answer

arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [0, 2, 3, 4]

print(solution(arr1, 1))
print(solution(arr2, 1))